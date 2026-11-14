---
id: R-PERF-001
level: 3
title: Memory use
priority: must
status: implemented
links:
  refines: [F-PERF-001]
  implemented_by: [crates/musicus-server/src/]
  decided_in: [tech:d-monolith]
---

# R-PERF-001 Memory use

## Statement

The server shall use less than 50 MB of memory when idle and run on a Raspberry Pi 4 (arm64) and on a virtual server with 1 vCPU and 1 GB RAM.

## Acceptance criteria

- The release build idles below 50 MB RSS (measured: about 11 MB).

## Notes

Measured manually; no automated test yet. The arm64 build has not been tested yet.
