# Resource-consumption benchmark report

Generated: 2026-11-21T13:07:34.616612+00:00 · results: /home/darrius/project/zerorl/benchmarks/resources/results

## Resource consumption (experiment R) [gpu]

Fixed workloads, device CPU. CPU% = sum over the live process tree (multiprocess sums may exceed 100%); RSS summed across tree processes (shared pages may repeat — PSS/USS recorded in the raw rows); GPU = device-level telemetry only (workload does not use the GPU); energy recorded only when reliable telemetry exists.

| workload | framework | wall (s) | cpu util avg (%) | cpu total (s) | cpu s / 1k | rss peak (MiB) | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collect | zeroRL | 83.5 ± 0.6 | 107.1 ± 0.3 | 89.6 ± 0.8 | 0.90 ± 0.01 | 1,604.6 ± 46.4 | 5 |
| collect | SB3 | 80.4 ± 0.8 | 108.2 ± 0.7 | 87.1 ± 0.6 | 0.87 ± 0.01 | 1,932.1 ± 6.1 | 5 |
| collect | TorchRL | 101.1 ± 2.1 | 110.4 ± 0.4 | 111.6 ± 2.4 | 1.12 ± 0.02 | 1,765.8 ± 17.0 | 5 |
| ppo | zeroRL | 297.0 ± 2.3 | 109.0 ± 2.5 | 324.4 ± 6.2 | 1.24 ± 0.02 | 4,871.8 ± 3,472.7 | 3 |
| ppo | SB3 | 438.2 ± 3.1 | 110.1 ± 0.1 | 482.4 ± 3.3 | 1.84 ± 0.01 | 3,073.4 ± 3.6 | 3 |
| ppo | TorchRL | 739.8 ± 5.8 | 108.8 ± 0.3 | 805.2 ± 4.3 | 3.07 ± 0.02 | 3,136.4 ± 0.3 | 3 |

- GPU telemetry: unavailable — NVML unavailable or produced no samples.
- Energy: unavailable — GPU power telemetry unsupported on this device and no RAPL/powercap energy interface for CPU/whole-system energy.
- Raw per-run rows: `results/resources_gpu.jsonl` (validation runs kept separately in `resources_validation.*`).

_Memory note: raw values are bytes (v2; v1 rows/sample files used KiB); averages are time-weighted (trapezoidal); summed RSS may double-count shared pages — PSS/USS are the attributable views; v1 rows show — (never 0)._

### Memory (RSS / PSS / USS) — collect

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,604.6 ± 46.4 | 1,598.2 ± 46.4 | 1,596.8 ± 46.4 | 1,573.5 ± 54.3 | 5 |
| SB3 | 1,932.1 ± 6.1 | 1,925.1 ± 5.8 | 1,923.8 ± 5.8 | 1,932.1 ± 6.1 | 5 |
| TorchRL | 1,765.8 ± 17.0 | 1,758.9 ± 17.1 | 1,757.6 ± 17.1 | 1,765.8 ± 17.0 | 5 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,570.3 ± 61.1 | 1,563.9 ± 61.2 | 1,562.6 ± 61.2 | 5 |
| SB3 | 1,784.2 ± 6.1 | 1,777.3 ± 5.8 | 1,776.0 ± 5.8 | 5 |
| TorchRL | 1,764.8 ± 17.6 | 1,758.0 ± 17.7 | 1,756.6 ± 17.7 | 5 |

### Memory (RSS / PSS / USS) — ppo

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 4,871.8 ± 3,472.7 | 2,629.9 ± 125.4 | 2,266.8 ± 6.9 | 4,871.8 ± 3,472.7 | 3 |
| SB3 | 3,073.4 ± 3.6 | 2,764.0 ± 3.5 | 2,476.7 ± 3.5 | 3,073.4 ± 3.6 | 3 |
| TorchRL | 3,136.4 ± 0.3 | 2,827.0 ± 0.3 | 2,539.6 ± 0.3 | 3,136.4 ± 0.3 | 3 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 3,469.8 ± 1,044.8 | 2,572.4 ± 26.6 | 2,243.6 ± 45.5 | 3 |
| SB3 | 3,069.2 ± 9.6 | 2,759.8 ± 9.5 | 2,472.5 ± 9.5 | 3 |
| TorchRL | 3,136.2 ± 0.7 | 2,826.7 ± 0.6 | 2,539.3 ± 0.6 | 3 |
