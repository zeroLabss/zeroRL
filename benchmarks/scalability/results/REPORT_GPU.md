# Scalability benchmark report

Generated: 2026-11-10T13:09:19.688417+00:00 · rows: 225 · figures in `figures/`

## Environment

| key | value |
| --- | --- |
| python | 3.13.14 |
| platform | Linux-6.8.12-tegra-aarch64-with-glibc2.39 |
| processor | aarch64 |
| device | cuda |
| hostname | gpu1 |
| torch | 2.13.0+cu130 |
| torch_num_threads | 14 |
| cuda_available | True |
| gymnasium | 1.3.0 |
| sb3 | 2.9.0 |
| torchrl | 0.14.1 |
| tensordict | 0.14.3 |
| git_sha | c5d014dbdc2fb19f09576fd854161f74fe9b278b |

## Methodology (summary)

- Frameworks: zeroRL (this repo, official `rollout_phase` / `BaseTrain.train()`), Stable-Baselines3, TorchRL — same shared-trunk policy/weights where policies apply (see `policy_reference.py`).
- Experiments A/B count individual env transitions with a warmup of 16,000 (excluded) + 100,000 measured transitions per run; Experiments C/D train PPO for exactly 262,144 transitions per run.
- Repetitions: 5 seeds per cell for A/B, 3 for C/D; every reported statistic aggregates **all** ok repetitions (mean ± std), never best-of.
- Metrics: `throughput = measured / measure_seconds`, `speedup(N) = t(baseline) / t(N)`, `environment_scaling_efficiency(N) = speedup(N) / N`, `worker_parallel_efficiency(W) = speedup(W) / (W / 1)`.
- Phase timing: `init` = env + policy construction + weight load (+ TorchRL collector/worker spawn); `warmup` (A/B only, excluded); `boundary` (A/B only) = warmup→measure phase reset / collector-worker restart, timed as `boundary_seconds`; `measure` = the official training/collection steady state. Full framework-specific details in `INSPECTION.md`.
- Device: CPU (`CUDA_VISIBLE_DEVICES=""`); protocol C/D hyperparameters in `ppo_protocols.py` (lr 3e-4 linear-decay, gamma .99, gae_lambda .95, clip .2, entropy .01, value .5, epochs 10, batch 64, grad-clip .5).

## Experiment A — GPU (device=cuda) [gpu]

Rows recorded with device=cuda; every statistic in this section is computed on this side only and never combined with CPU rows.

| framework | N | throughput (trans/s) | mean time (s) | speedup (paired) | env-scaling efficiency (paired) | pairs (n) |
| --- | --- | --- | --- | --- | --- | --- |
| zeroRL | 1 | 1,058.9 ± 20.6 | 94.47 | 1.00 | 1.00 | 5 |
| zeroRL | 2 | 1,904.9 ± 155.9 | 52.80 | 1.80 ± 0.14 | 0.90 ± 0.07 | 5 |
| zeroRL | 4 | 3,369.4 ± 74.7 | 29.69 | 3.18 ± 0.12 | 0.80 ± 0.03 | 5 |
| zeroRL | 8 | 5,711.1 ± 46.8 | 17.51 | 5.40 ± 0.10 | 0.67 ± 0.01 | 5 |
| zeroRL | 16 | 8,518.4 ± 793.2 | 11.83 | 8.05 ± 0.79 | 0.50 ± 0.05 | 5 |
| SB3 | 1 | 1,268.7 ± 49.8 | 78.92 | 1.00 | 1.00 | 5 |
| SB3 | 2 | 2,385.1 ± 69.0 | 41.96 | 1.88 ± 0.10 | 0.94 ± 0.05 | 5 |
| SB3 | 4 | 4,125.1 ± 149.4 | 24.27 | 3.25 ± 0.11 | 0.81 ± 0.03 | 5 |
| SB3 | 8 | 6,774.8 ± 177.9 | 14.77 | 5.35 ± 0.21 | 0.67 ± 0.03 | 5 |
| SB3 | 16 | 9,676.4 ± 264.8 | 10.34 | 7.63 ± 0.30 | 0.48 ± 0.02 | 5 |
| TorchRL | 1 | 560.9 ± 21.9 | 178.51 | 1.00 | 1.00 | 5 |
| TorchRL | 2 | 1,090.9 ± 39.2 | 91.77 | 1.95 ± 0.03 | 0.97 ± 0.01 | 5 |
| TorchRL | 4 | 2,065.7 ± 22.6 | 48.41 | 3.69 ± 0.14 | 0.92 ± 0.04 | 5 |
| TorchRL | 8 | 3,574.1 ± 181.6 | 28.04 | 6.38 ± 0.31 | 0.80 ± 0.04 | 5 |
| TorchRL | 16 | 6,345.4 ± 72.2 | 15.76 | 11.32 ± 0.37 | 0.71 ± 0.02 | 5 |

![throughput](figures/expA_gpu_gpu_throughput.png)

![speedup](figures/expA_gpu_gpu_speedup.png)

![efficiency](figures/expA_gpu_gpu_efficiency.png)


## Experiment B — GPU (device=cuda) [gpu]

Rows recorded with device=cuda; every statistic in this section is computed on this side only and never combined with CPU rows.

| framework | W | throughput (trans/s) | mean time (s) | speedup (paired) | worker parallel efficiency (paired) | pairs (n) |
| --- | --- | --- | --- | --- | --- | --- |
| zeroRL | 1 | 5,638.6 ± 120.5 | 17.74 | 1.00 | 1.00 | 5 |
| SB3 | 1 | 6,638.2 ± 310.9 | 15.09 | 1.00 | 1.00 | 5 |
| SB3 | 8 | 6,786.9 ± 176.9 | 14.74 | 1.02 ± 0.06 | 0.13 ± 0.01 | 5 |
| TorchRL | 1 | 3,726.7 ± 30.4 | 26.84 | 1.00 | 1.00 | 5 |
| TorchRL | 2 | 6,236.8 ± 91.0 | 16.04 | 1.67 ± 0.03 | 0.84 ± 0.01 | 5 |
| TorchRL | 4 | 6,625.1 ± 90.7 | 15.10 | 1.78 ± 0.03 | 0.44 ± 0.01 | 5 |
| TorchRL | 8 | 7,311.1 ± 67.7 | 13.68 | 1.96 ± 0.01 | 0.25 ± 0.00 | 5 |

**Unsupported (recorded, not run)**:

- zeroRL W=2: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=2: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=2: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=2: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=2: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=4: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=4: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=4: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=4: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=4: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=8: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=8: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=8: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=8: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- zeroRL W=8: zeroRL has no multi-process environment path (vectorize_env -> SyncVectorEnv only); W>=2 unsupported
- SB3 W=2: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=2 unsupported
- SB3 W=2: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=2 unsupported
- SB3 W=2: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=2 unsupported
- SB3 W=2: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=2 unsupported
- SB3 W=2: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=2 unsupported
- SB3 W=4: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=4 unsupported
- SB3 W=4: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=4 unsupported
- SB3 W=4: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=4 unsupported
- SB3 W=4: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=4 unsupported
- SB3 W=4: SB3 SubprocVecEnv runs exactly one process per env, so only W=1 (DummyVecEnv) and W=8 (SubprocVecEnv) exist; W=4 unsupported

![throughput](figures/expB_gpu_gpu_throughput.png)

![speedup](figures/expB_gpu_gpu_speedup.png)

![efficiency](figures/expB_gpu_gpu_efficiency.png)


## Experiment C — GPU (device=cuda) [gpu]

Rows recorded with device=cuda; every statistic in this section is computed on this side only and never combined with CPU rows.

| framework | N | updates | throughput (trans/s) | mean time (s) | mean return (last 100) | reps |
| --- | --- | --- | --- | --- | --- | --- |
| zeroRL | 1 | 128 | 685.9 ± 5.1 | 382.2 | -12.0 ± 2.1 | 3 |
| zeroRL | 2 | 64 | 1,067.9 ± 14.0 | 245.5 | -14.1 ± 1.9 | 3 |
| zeroRL | 4 | 32 | 1,500.8 ± 29.6 | 174.7 | -17.9 ± 0.4 | 3 |
| zeroRL | 8 | 16 | 1,948.0 ± 20.2 | 134.6 | -30.1 ± 0.6 | 3 |
| zeroRL | 16 | 8 | 2,315.0 ± 9.8 | 113.2 | -50.4 ± 1.0 | 3 |
| SB3 | 1 | 128 | 578.2 ± 3.4 | 453.4 | -8.6 ± 0.4 | 3 |
| SB3 | 2 | 64 | 741.5 ± 6.6 | 353.6 | -13.3 ± 6.7 | 3 |
| SB3 | 4 | 32 | 875.4 ± 3.7 | 299.5 | -18.7 ± 5.9 | 3 |
| SB3 | 8 | 16 | 961.0 ± 3.8 | 272.8 | -21.7 ± 2.4 | 3 |
| SB3 | 16 | 8 | 1,023.7 ± 8.3 | 256.1 | -39.9 ± 1.0 | 3 |
| TorchRL | 1 | 128 | 311.5 ± 5.8 | 841.8 | -8.9 ± 0.7 | 3 |
| TorchRL | 2 | 64 | 421.0 ± 2.6 | 622.7 | -8.1 ± 0.4 | 3 |
| TorchRL | 4 | 32 | 526.0 ± 4.3 | 498.4 | -11.5 ± 0.6 | 3 |
| TorchRL | 8 | 16 | 588.7 ± 3.7 | 445.3 | -16.9 ± 0.4 | 3 |
| TorchRL | 16 | 8 | 629.4 ± 1.6 | 416.5 | -37.5 ± 0.3 | 3 |

![throughput](figures/expC_gpu_gpu_throughput.png)

![returns](figures/expC_gpu_gpu_returns.png)


## Experiment D — GPU (device=cuda) [gpu]

Rows recorded with device=cuda; every statistic in this section is computed on this side only and never combined with CPU rows.

| framework | N | updates | throughput (trans/s) | mean time (s) | mean return (last 100) | reps |
| --- | --- | --- | --- | --- | --- | --- |
| zeroRL | 1 | 128 | 697.2 ± 11.1 | 376.0 | -12.0 ± 2.1 | 3 |
| zeroRL | 2 | 128 | 1,050.1 ± 18.0 | 249.7 | -11.8 ± 1.7 | 3 |
| zeroRL | 4 | 128 | 1,484.7 ± 26.8 | 176.6 | -13.0 ± 0.9 | 3 |
| zeroRL | 8 | 128 | 1,885.3 ± 15.2 | 139.0 | -12.0 ± 0.6 | 3 |
| zeroRL | 16 | 128 | 2,257.7 ± 17.6 | 116.1 | -13.4 ± 1.5 | 3 |
| SB3 | 1 | 128 | 573.5 ± 6.2 | 457.1 | -8.6 ± 0.4 | 3 |
| SB3 | 2 | 128 | 735.8 ± 3.1 | 356.3 | -8.5 ± 1.1 | 3 |
| SB3 | 4 | 128 | 862.7 ± 10.0 | 303.9 | -8.2 ± 0.8 | 3 |
| SB3 | 8 | 128 | 931.5 ± 11.3 | 281.4 | -8.0 ± 0.4 | 3 |
| SB3 | 16 | 128 | 981.1 ± 6.3 | 267.2 | -8.6 ± 1.0 | 3 |
| TorchRL | 1 | 128 | 292.9 ± 2.1 | 895.0 | -8.9 ± 0.7 | 3 |
| TorchRL | 2 | 128 | 397.9 ± 2.3 | 658.8 | -7.7 ± 0.4 | 3 |
| TorchRL | 4 | 128 | 503.0 ± 7.5 | 521.2 | -7.7 ± 0.6 | 3 |
| TorchRL | 8 | 128 | 575.7 ± 3.1 | 455.3 | -8.1 ± 0.8 | 3 |
| TorchRL | 16 | 128 | 618.3 ± 3.7 | 424.0 | -7.4 ± 0.4 | 3 |

![throughput](figures/expD_gpu_gpu_throughput.png)

![returns](figures/expD_gpu_gpu_returns.png)


## Findings (computed from the data)


## Data integrity

| experiment | ok | failed | unsupported |
| --- | --- | --- | --- |

All ok rows recorded an exact transition budget.

GPU rows: 225 (device=cuda)

Total rows: 225.

---
See `README.md` (reproduction), `INSPECTION.md` (framework findings), `results/*.jsonl` (raw data).
