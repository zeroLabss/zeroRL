# Resource-consumption benchmark report

Generated: 2026-11-09T22:47:01.283221+00:00 · results: /home/research/projects/zeroRL/benchmarks/resources/results

## Resource consumption (experiment R)

Fixed workloads, device CPU. CPU% = sum over the live process tree (multiprocess sums may exceed 100%); RSS summed across tree processes (shared pages may repeat — PSS/USS recorded in the raw rows); GPU = device-level telemetry only (workload does not use the GPU); energy recorded only when reliable telemetry exists.

| workload | framework | wall (s) | cpu util avg (%) | cpu total (s) | cpu s / 1k | rss peak (MiB) | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collect | zeroRL | 25.6 ± 0.2 | 917.0 ± 5.3 | 235.3 ± 0.9 | 2.35 ± 0.01 | 820.5 ± 15.0 | 12 |
| collect | SB3 | 25.6 ± 0.2 | 916.2 ± 7.0 | 235.6 ± 0.8 | 2.36 ± 0.01 | 850.5 ± 5.4 | 10 |
| collect | TorchRL | 34.9 ± 0.5 | 702.7 ± 11.9 | 245.1 ± 3.1 | 2.45 ± 0.03 | 986.1 ± 4.4 | 10 |
| ppo | zeroRL | 219.4 ± 0.9 | 872.7 ± 3.2 | 1,910.9 ± 7.6 | 7.29 ± 0.03 | 1,033.6 ± 4.8 | 6 |
| ppo | SB3 | 263.3 ± 1.1 | 903.3 ± 2.4 | 2,376.0 ± 5.5 | 9.06 ± 0.02 | 1,049.8 ± 2.9 | 6 |
| ppo | TorchRL | 395.5 ± 1.6 | 814.0 ± 1.8 | 3,201.1 ± 7.3 | 12.21 ± 0.03 | 1,068.2 ± 2.9 | 6 |

- GPU telemetry: unavailable — NVML unavailable or produced no samples.
- Energy: unavailable — GPU power telemetry unsupported on this device and no RAPL/powercap energy interface for CPU/whole-system energy.
- Raw per-run rows: `results/resources.jsonl` (validation runs kept separately in `resources_validation.*`).

_Memory note: raw values are bytes (v2; v1 rows/sample files used KiB); averages are time-weighted (trapezoidal); summed RSS may double-count shared pages — PSS/USS are the attributable views; v1 rows show — (never 0)._

### Memory (RSS / PSS / USS) — collect

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 820.5 ± 15.0 | 812.7 ± 15.0 | 811.4 ± 15.0 | 816.4 ± 15.4 | 12 |
| SB3 | 850.5 ± 5.4 | 842.8 ± 5.3 | 841.5 ± 5.3 | 849.3 ± 7.2 | 10 |
| TorchRL | 986.1 ± 4.4 | 978.7 ± 4.5 | 977.3 ± 4.5 | 986.1 ± 4.4 | 10 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 815.2 ± 15.1 | 807.4 ± 15.1 | 806.1 ± 15.1 | 12 |
| SB3 | 847.9 ± 6.7 | 840.1 ± 6.7 | 838.8 ± 6.7 | 10 |
| TorchRL | 985.1 ± 5.3 | 977.6 ± 5.3 | 976.3 ± 5.3 | 10 |

### Memory (RSS / PSS / USS) — ppo

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,033.6 ± 4.8 | 1,016.4 ± 4.8 | 1,007.0 ± 4.8 | 1,033.6 ± 4.9 | 6 |
| SB3 | 1,049.8 ± 2.9 | 1,032.6 ± 2.9 | 1,023.2 ± 2.9 | 1,049.8 ± 2.9 | 6 |
| TorchRL | 1,068.2 ± 2.9 | 1,051.1 ± 2.8 | 1,041.7 ± 2.8 | 1,068.2 ± 2.9 | 6 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,031.8 ± 4.5 | 1,014.5 ± 4.5 | 1,005.1 ± 4.5 | 6 |
| SB3 | 1,048.4 ± 3.8 | 1,031.3 ± 3.8 | 1,021.9 ± 3.8 | 6 |
| TorchRL | 1,064.6 ± 2.7 | 1,047.6 ± 2.7 | 1,038.3 ± 2.7 | 6 |
