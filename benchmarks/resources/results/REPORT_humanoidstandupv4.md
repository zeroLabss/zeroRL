# Resource-consumption benchmark report

Generated: 2026-11-08T23:35:46.556160+00:00 · results: /home/darrius/project/zerorl/benchmarks/resources/results

## Resource consumption (experiment R) [humanoidstandupv4]

Fixed workloads, device CPU. CPU% = sum over the live process tree (multiprocess sums may exceed 100%); RSS summed across tree processes (shared pages may repeat — PSS/USS recorded in the raw rows); GPU = device-level telemetry only (workload does not use the GPU); energy recorded only when reliable telemetry exists.

| workload | framework | wall (s) | cpu util avg (%) | cpu total (s) | cpu s / 1k | rss peak (MiB) | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collect | zeroRL | 112.0 ± 5.2 | 223.0 ± 1.8 | 249.2 ± 9.9 | 2.49 ± 0.10 | 1,269.0 ± 170.4 | 5 |
| collect | SB3 | 105.6 ± 7.4 | 226.7 ± 2.5 | 239.3 ± 13.9 | 2.39 ± 0.14 | 1,632.6 ± 74.2 | 5 |
| collect | TorchRL | 121.9 ± 3.1 | 207.1 ± 1.2 | 251.6 ± 4.0 | 2.52 ± 0.04 | 1,307.8 ± 57.5 | 5 |
| ppo | zeroRL | 421.0 ± 29.7 | 395.7 ± 18.6 | 1,672.8 ± 39.7 | 6.38 ± 0.15 | 1,441.2 ± 270.0 | 3 |
| ppo | SB3 | 416.4 ± 16.1 | 432.5 ± 5.0 | 1,806.2 ± 52.2 | 6.89 ± 0.20 | 1,295.9 ± 9.8 | 3 |
| ppo | TorchRL | 670.3 ± 24.2 | 385.3 ± 3.5 | 2,580.7 ± 88.4 | 9.84 ± 0.34 | 1,335.1 ± 17.1 | 3 |

- GPU telemetry: available (device-level only).
- Energy: unavailable — GPU power telemetry unsupported on this device and no RAPL/powercap energy interface for CPU/whole-system energy.
- Raw per-run rows: `results/resources_humanoidstandupv4.jsonl` (validation runs kept separately in `resources_validation.*`).

_Memory note: raw values are bytes (v2; v1 rows/sample files used KiB); averages are time-weighted (trapezoidal); summed RSS may double-count shared pages — PSS/USS are the attributable views; v1 rows show — (never 0)._

### Memory (RSS / PSS / USS) — collect

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,269.0 ± 170.4 | 1,266.4 ± 170.5 | 1,265.7 ± 170.5 | 1,197.7 ± 121.0 | 5 |
| SB3 | 1,632.6 ± 74.2 | 1,630.4 ± 74.2 | 1,629.6 ± 74.2 | 1,632.6 ± 74.2 | 5 |
| TorchRL | 1,307.8 ± 57.5 | 1,305.6 ± 57.6 | 1,304.8 ± 57.6 | 1,305.3 ± 62.4 | 5 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,203.0 ± 119.9 | 1,200.7 ± 119.8 | 1,199.9 ± 119.8 | 5 |
| SB3 | 1,475.3 ± 64.7 | 1,473.2 ± 64.5 | 1,472.4 ± 64.5 | 5 |
| TorchRL | 1,285.9 ± 59.3 | 1,283.7 ± 59.2 | 1,282.9 ± 59.2 | 5 |

### Memory (RSS / PSS / USS) — ppo

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,441.2 ± 270.0 | 1,376.2 ± 175.7 | 1,316.9 ± 86.2 | 1,441.2 ± 270.0 | 3 |
| SB3 | 1,295.9 ± 9.8 | 1,285.2 ± 9.8 | 1,277.6 ± 9.8 | 1,295.8 ± 9.8 | 3 |
| TorchRL | 1,335.1 ± 17.1 | 1,324.9 ± 16.7 | 1,317.3 ± 16.7 | 1,321.3 ± 21.1 | 3 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,284.7 ± 1.2 | 1,273.9 ± 1.6 | 1,266.0 ± 2.0 | 3 |
| SB3 | 1,295.8 ± 9.8 | 1,285.2 ± 9.8 | 1,277.6 ± 9.8 | 3 |
| TorchRL | 1,321.2 ± 21.0 | 1,311.0 ± 21.0 | 1,303.4 ± 21.0 | 3 |
