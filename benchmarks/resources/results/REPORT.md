# Resource-consumption benchmark report

Generated: 2026-11-07T20:42:43.014182+00:00 · results: /home/research/projects/zeroRL/benchmarks/resources/results

## Resource consumption (experiment R)

Fixed workloads, device CPU. CPU% = sum over the live process tree (multiprocess sums may exceed 100%); RSS summed across tree processes (shared pages may repeat — PSS/USS recorded in the raw rows); GPU = device-level telemetry only (workload does not use the GPU); energy recorded only when reliable telemetry exists.

| workload | framework | wall (s) | cpu util avg (%) | cpu total (s) | cpu s / 1k | rss peak (MiB) | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collect | zeroRL | 25.6 ± 0.2 | 916.9 ± 6.5 | 235.0 ± 0.8 | 2.35 ± 0.01 | 819.0 ± 16.0 | 7 |
| collect | SB3 | 25.6 ± 0.2 | 916.1 ± 8.1 | 235.7 ± 0.9 | 2.36 ± 0.01 | 846.7 ± 3.6 | 5 |
| collect | TorchRL | 34.6 ± 0.4 | 705.8 ± 8.5 | 244.5 ± 2.4 | 2.44 ± 0.02 | 986.4 ± 4.8 | 5 |
| ppo | zeroRL | 219.4 ± 1.5 | 873.0 ± 4.4 | 1,911.8 ± 8.4 | 7.29 ± 0.03 | 1,033.7 ± 5.4 | 3 |
| ppo | SB3 | 263.7 ± 1.1 | 902.8 ± 3.1 | 2,378.0 ± 5.4 | 9.07 ± 0.02 | 1,049.9 ± 3.2 | 3 |
| ppo | TorchRL | 395.6 ± 1.9 | 814.0 ± 2.7 | 3,201.3 ± 5.5 | 12.21 ± 0.02 | 1,068.2 ± 3.4 | 3 |

- GPU telemetry: unavailable — NVML unavailable or produced no samples.
- Energy: unavailable — GPU power telemetry unsupported on this device and no RAPL/powercap energy interface for CPU/whole-system energy.
- Raw per-run rows: `results/resources.jsonl` (validation runs kept separately in `resources_validation.*`).

_Memory note: raw values are bytes (v2; v1 rows/sample files used KiB); averages are time-weighted (trapezoidal); summed RSS may double-count shared pages — PSS/USS are the attributable views; v1 rows show — (never 0)._

### Memory (RSS / PSS / USS) — collect

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 819.0 ± 16.0 | 811.2 ± 15.9 | 809.9 ± 15.9 | 814.6 ± 15.8 | 7 |
| SB3 | 846.7 ± 3.6 | 839.1 ± 3.6 | 837.8 ± 3.6 | 844.3 ± 6.0 | 5 |
| TorchRL | 986.4 ± 4.8 | 979.0 ± 4.9 | 977.7 ± 4.9 | 986.4 ± 4.8 | 5 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 813.8 ± 16.0 | 805.9 ± 16.0 | 804.6 ± 16.0 | 7 |
| SB3 | 843.2 ± 5.4 | 835.5 ± 5.6 | 834.2 ± 5.6 | 5 |
| TorchRL | 985.3 ± 5.8 | 977.9 ± 5.8 | 976.6 ± 5.8 | 5 |

### Memory (RSS / PSS / USS) — ppo

**Peak (end-to-end)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | peak rss — measure phase (MiB) | n |
| --- | --- | --- | --- | --- | --- |
| zeroRL | 1,033.7 ± 5.4 | 1,016.6 ± 5.4 | 1,007.2 ± 5.4 | 1,033.6 ± 5.4 | 3 |
| SB3 | 1,049.9 ± 3.2 | 1,032.8 ± 3.3 | 1,023.5 ± 3.3 | 1,049.9 ± 3.3 | 3 |
| TorchRL | 1,068.2 ± 3.4 | 1,051.2 ± 3.3 | 1,041.8 ± 3.3 | 1,068.2 ± 3.4 | 3 |

**Average (end-to-end, time-weighted)**

| framework | rss (MiB) | pss (MiB) | uss (MiB) | n |
| --- | --- | --- | --- | --- |
| zeroRL | 1,031.9 ± 4.8 | 1,014.8 ± 4.9 | 1,005.4 ± 4.9 | 3 |
| SB3 | 1,048.5 ± 4.3 | 1,031.6 ± 4.2 | 1,022.2 ± 4.2 | 3 |
| TorchRL | 1,064.8 ± 2.9 | 1,048.0 ± 2.9 | 1,038.6 ± 2.9 | 3 |
