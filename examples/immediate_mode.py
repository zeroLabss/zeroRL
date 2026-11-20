import numpy as np
import torch
from tqdm import tqdm
from torch import optim
from torch.optim.lr_scheduler import LambdaLR
from zerorl.algorithms.ppo import ppo_func, gae_compute
from zerorl.helpers.factory import ActorCriticAgent
from zerorl.buffer import Buffer
from zerorl.config import TrainConfig, AlgoConfig
from zerorl.logger import create_logger
from zerorl.functions import (processing_state,
                              parse_dict_to_tensor,
                              to_env_action,
                              try_agent,
                              get_obs_act,
                              vectorize_env,
                              set_seed,
                              get_last_obs)


cfg = TrainConfig(model_name="Lunar-model", project_name="Lunar-example", num_envs=4, device="cpu")
algo_cfg = AlgoConfig()
seed = set_seed(42, cfg.num_envs)
env = vectorize_env("LunarLander-v3", num_envs = cfg.num_envs)
obs_dim, act_dim, obs_n, act_n, is_discrete = get_obs_act(env)
agent = ActorCriticAgent(obs_n, act_n, is_discrete).to(cfg.device)
buffer = Buffer(capacity = cfg.rollout_steps,
                num_envs = cfg.num_envs,
                schema = {"state": obs_dim, "action": act_dim,
                          "reward": (), "terminated": (), "truncated": (),
                          "entropy": (), "value": (), "return": (), "log_prob": (),
                          "advantage": (), "final_value": ()},
                device = cfg.device)
optimizer = optim.Adam(agent.parameters(), lr=algo_cfg.lr, eps=1e-5)
scheduler = LambdaLR(optimizer, lambda step_: 1.0 - (step_ / cfg.num_update))
log = create_logger(cfg, algo_cfg, use_tb=True)
reward_tensor = torch.zeros(cfg.num_envs, device=cfg.device)
state, _ = env.reset(seed = seed)
obs_shape = getattr(env, "single_observation_space", env.observation_space)

for step in tqdm(range(cfg.num_update)):
    episodic_reward = []
    metrics = {}
    for i in range(cfg.rollout_steps):
        state_processed = processing_state(state)
        with torch.inference_mode():
            outputs = agent.get_action(state_processed)
        action  = to_env_action(outputs["action"], env)
        next_state, reward, terminated, truncated, info = env.step(action)
        outputs_final = {"state": state_processed, "next_state": next_state, "reward": reward,
                         "terminated": terminated, "truncated": truncated,
                         "info": info, **outputs} 
        outputs_final = parse_dict_to_tensor(outputs_final)
        info = outputs_final.pop("info", {})
        next_state = outputs_final.pop("next_state")
        is_term = outputs_final["terminated"] > 0
        is_trunc = outputs_final["truncated"] > 0
        done = is_term | is_trunc
        final_value = torch.zeros(cfg.num_envs, device = cfg.device)
        if is_trunc.any():
            last_obs = get_last_obs(info, cfg.num_envs, obs_shape.shape, cfg.device)
            if last_obs  is  not None:
                with torch.inference_mode():
                    last_obs_processed = processing_state(last_obs, update=False, device = cfg.device)
                    last_value = agent.get_action(last_obs_processed)["value"]
                final_value = torch.where(is_trunc, last_value, final_value)
        if i == cfg.rollout_steps - 1:
            with torch.inference_mode():
                state_processed = processing_state(next_state, update=False, device=cfg.device)
                val = agent.get_action(state_processed)["value"]
            final_value = torch.where(done, final_value, val)
        outputs_final["final_value"] = final_value
        buffer.insert(**outputs_final)
        reward_tensor += outputs_final["reward"]

        if done.any():
            episodic_reward.extend(reward_tensor[done].tolist())
            reward_tensor[done] = 0.0
        state = next_state

    with torch.inference_mode():
        state_processed = processing_state(state)
        last_output = agent.get_action(state_processed)

    data = buffer.get_all()
    gae_compute(data["reward"], data["value"], data["final_value"], data["terminated"], data["truncated"], buffer, algo_cfg)
    losses = ppo_func(agent, optimizer, buffer, algo_cfg, scheduler)
    if len(episodic_reward) > 0:
        recent = episodic_reward[-10:]
        mean_reward = float(np.mean(recent))
    else:
        mean_reward = 0.0
    metrics = {"train/mean_episodic_reward": mean_reward}
    for k, v in losses.items(): metrics[f"train/{k}"] = v
    log(metrics, step)
    buffer.clear()

env.close()
log.close()
try_agent("LunarLander-v3", agent, cfg)
