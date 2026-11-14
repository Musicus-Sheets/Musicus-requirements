---
id: R-PERF-004
level: 3
title: Hot files in memory
priority: must
status: verified
links:
  refines: [F-PERF-002]
  constrains: [R-PERF-001]
  verified_by: [crates/musicus-server/src/cache.rs::evicts_least_recently_used]
  implemented_by: [crates/musicus-server/src/cache.rs]
---

# R-PERF-004 Hot files in memory

## Statement

The server shall keep recently delivered files in a memory cache of configurable size (default 128 MB), evicting the least recently used, and share one copy between all simultaneous downloads.

## Acceptance criteria

- The cache test evicts the least recently used file first.
