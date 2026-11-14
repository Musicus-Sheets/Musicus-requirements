---
id: R-PERF-006
level: 3
title: Concurrent annotation saves
priority: must
status: implemented
links:
  refines: [F-PERF-002]
  implemented_by: [crates/musicus-server/src/db.rs]
  decided_in: [tech:d-sqlite]
---

# R-PERF-006 Concurrent annotation saves

## Statement

The server shall store 120 simultaneous annotation page saves in less than 1 s on one CPU core.

## Acceptance criteria

- Prototype benchmark: 120 saves of 8 KB in about 25 ms.
