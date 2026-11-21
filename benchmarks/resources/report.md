# Resource-consumption benchmark report

Generated: 2026-11-21T13:08:44.755789+00:00 · results: /home/darrius/project/zerorl/benchmarks/resources/results

## Resource consumption (experiment R)

Fixed workloads, device CPU. CPU% = sum over the live process tree (multiprocess sums may exceed 100%); RSS summed across tree processes (shared pages may repeat — PSS/USS recorded in the raw rows); GPU = device-level telemetry only (workload does not use the GPU); energy recorded only when reliable telemetry exists.

| workload | framework | wall (s) | cpu util avg (%) | cpu total (s) | cpu s / 1k | rss peak (MiB) | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collect | zeroRL | 102.5 ± 0.5 | 428.3 ± 1.3 | 439.4 ± 3.1 | 4.39 ± 0.03 | 1,177.7 ± 170.7 | 5 |
| collect | SB3 | 102.1 ± 0.4 | 431.4 ± 2.4 | 440.8 ± 3.6 | 4.41 ± 0.04 | 1,288.8 ± 127.1 | 5 |
| collect | TorchRL | 115.7 ± 0.5 | 401.2 ± 2.0 | 463.7 ± 3.8 | 4.64 ± 0.04 | 1,453.7 ± 22.5 | 5 |
| ppo | zeroRL | 386.8 ± 4.9 | 677.0 ± 11.8 | 2,606.2 ± 20.5 | 9.94 ± 0.08 | 1,613.0 ± 447.0 | 3 |
| ppo | SB3 | 415.6 ± 1.2 | 691.8 ± 5.6 | 2,866.1 ± 18.9 | 10.93 ± 0.07 | 1,368.3 ± 9.8 | 3 |
| ppo | TorchRL | 565.3 ± 2.1 | 675.5 ± 2.6 | 3,789.5 ± 5.8 | 14.46 ± 0.02 | 1,414.1 ± 19.9 | 3 |

- GPU telemetry: unavailable — NVML unavailable or produced no samples.
- Energy: unavailable — GPU power telemetry unsupported on this device and no RAPL/powercap energy interface for CPU/whole-system energy.
- Raw per-run rows: `results/resources.jsonl` (validation runs kept separately in `resources_validation.*`).

_Memory note: raw values are bytes (v2; v1 rows/sample files used KiB); averages are time-weighted (trapezoidal); summed RSS may double-count shared pages — PSS/USS are the attributable views; v1 rows show — (never 0)._

### Memory (RSS / PSS / USS) — collect

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,177.7 ± 170.7 | 1,170.7 ± 170.6 | 1,169.3 ± 170.6 | 1,166.6 ± 175.4 | 5 |
| SB3 | 1,288.8 ± 127.1 | 1,281.9 ± 127.9 | 1,280.5 ± 127.9 | 1,254.0 ± 146.5 | 5 |
| TorchRL | 1,453.7 ± 22.5 | 1,450.0 ± 22.6 | 1,448.7 ± 22.6 | 1,453.7 ± 22.5 | 5 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,157.0 ± 174.7 | 1,150.0 ± 174.7 | 1,148.6 ± 174.7 | 5 |
| SB3 | 1,207.3 ± 35.5 | 1,200.2 ± 36.0 | 1,198.9 ± 36.0 | 5 |
| TorchRL | 1,414.0 ± 16.0 | 1,407.3 ± 16.0 | 1,405.9 ± 16.0 | 5 |

### Memory (RSS / PSS / USS) — ppo

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,613.0 ± 447.0 | 1,495.9 ± 272.1 | 1,466.3 ± 237.1 | 1,613.0 ± 447.0 | 3 |
| SB3 | 1,368.3 ± 9.8 | 1,352.1 ± 9.8 | 1,342.7 ± 9.8 | 1,368.3 ± 9.8 | 3 |
| TorchRL | 1,414.1 ± 19.9 | 1,398.3 ± 20.0 | 1,388.9 ± 20.0 | 1,414.1 ± 19.9 | 3 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,354.2 ± 2.1 | 1,338.0 ± 2.4 | 1,328.5 ± 2.5 | 3 |
| SB3 | 1,367.7 ± 9.8 | 1,351.8 ± 9.8 | 1,342.4 ± 9.8 | 3 |
| TorchRL | 1,390.5 ± 18.5 | 1,374.7 ± 18.5 | 1,365.3 ± 18.5 | 3 |

## Resource consumption — GPU (device=cuda)

Fixed workloads, device GPU (row `device=cuda`). Every statistic below is computed from GPU rows only and never combined with the CPU side above. CPU% = sum over the live process tree; RSS summed across tree processes; GPU = device-level telemetry of the workload's own device; energy recorded only when reliable telemetry exists.

| workload | framework | wall (s) | cpu util avg (%) | cpu total (s) | cpu s / 1k | rss peak (MiB) | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collect | zeroRL | 83.5 ± 0.6 | 107.1 ± 0.3 | 89.6 ± 0.8 | 0.90 ± 0.01 | 1,604.6 ± 46.4 | 5 |
| collect | SB3 | 80.4 ± 0.8 | 108.2 ± 0.7 | 87.1 ± 0.6 | 0.87 ± 0.01 | 1,932.1 ± 6.1 | 5 |
| collect | TorchRL | 101.1 ± 2.1 | 110.4 ± 0.4 | 111.6 ± 2.4 | 1.12 ± 0.02 | 1,765.8 ± 17.0 | 5 |
| ppo | zeroRL | 297.0 ± 2.3 | 109.0 ± 2.5 | 324.4 ± 6.2 | 1.24 ± 0.02 | 4,871.8 ± 3,472.7 | 3 |
| ppo | SB3 | 438.2 ± 3.1 | 110.1 ± 0.1 | 482.4 ± 3.3 | 1.84 ± 0.01 | 3,073.4 ± 3.6 | 3 |
| ppo | TorchRL | 739.8 ± 5.8 | 108.8 ± 0.3 | 805.2 ± 4.3 | 3.07 ± 0.02 | 3,136.4 ± 0.3 | 3 |

- GPU telemetry (device side cuda): unavailable — NVML unavailable or produced no samples.
- Energy (device side cuda): unavailable — GPU power telemetry unsupported on this device and no RAPL/powercap energy interface for CPU/whole-system energy.
- Raw per-run rows: `results/resources_gpu.jsonl`.

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
