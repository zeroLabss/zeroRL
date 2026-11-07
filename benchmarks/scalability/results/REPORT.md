# Scalability benchmark report

Generated: 2026-11-07T20:59:38.092369+00:00 · rows: 150 · figures in `figures/`

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
| git_sha | 7813ea3a3711cfbcf6592ef8af5bb05b04fb4dc4 |

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
| zeroRL | 1 | 640.0 ± 5.6 | 156.26 | 1.00 | 1.00 | 5 |
| zeroRL | 2 | 910.0 ± 9.9 | 109.90 | 1.43 ± 0.01 | 0.72 ± 0.00 | 5 |
| zeroRL | 4 | 1,190.6 ± 10.6 | 84.00 | 1.87 ± 0.02 | 0.47 ± 0.01 | 5 |
| zeroRL | 8 | 1,398.2 ± 8.6 | 71.52 | 2.19 ± 0.02 | 0.27 ± 0.00 | 5 |
| zeroRL | 16 | 1,415.8 ± 8.9 | 70.63 | 2.21 ± 0.04 | 0.14 ± 0.00 | 5 |
| SB3 | 1 | 745.4 ± 14.9 | 134.20 | 1.00 | 1.00 | 5 |
| SB3 | 2 | 1,022.6 ± 12.2 | 97.80 | 1.38 ± 0.04 | 0.69 ± 0.02 | 5 |
| SB3 | 4 | 1,275.7 ± 17.0 | 78.40 | 1.71 ± 0.05 | 0.43 ± 0.01 | 5 |
| SB3 | 8 | 1,447.9 ± 11.7 | 69.07 | 1.96 ± 0.04 | 0.24 ± 0.01 | 5 |
| SB3 | 16 | 1,442.9 ± 6.8 | 69.31 | 1.95 ± 0.04 | 0.12 ± 0.00 | 5 |
| TorchRL | 1 | 373.3 ± 5.8 | 267.91 | 1.00 | 1.00 | 5 |
| TorchRL | 2 | 583.1 ± 20.5 | 171.69 | 1.55 ± 0.05 | 0.78 ± 0.02 | 5 |
| TorchRL | 4 | 855.7 ± 18.5 | 116.91 | 2.31 ± 0.06 | 0.58 ± 0.02 | 5 |
| TorchRL | 8 | 1,135.6 ± 18.2 | 88.08 | 3.11 ± 0.04 | 0.39 ± 0.00 | 5 |
| TorchRL | 16 | 1,331.5 ± 18.2 | 75.11 | 3.59 ± 0.06 | 0.22 ± 0.00 | 5 |

![throughput](figures/expA_gpu_gpu_throughput.png)

![speedup](figures/expA_gpu_gpu_speedup.png)

![efficiency](figures/expA_gpu_gpu_efficiency.png)


## Findings (computed from the data)


## Data integrity

| experiment | ok | failed | unsupported |
| --- | --- | --- | --- |

All ok rows recorded an exact transition budget.

GPU rows: 150 (device=cuda)

Total rows: 150.

---
See `README.md` (reproduction), `INSPECTION.md` (framework findings), `results/*.jsonl` (raw data).
