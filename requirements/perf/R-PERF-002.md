---
id: R-PERF-002
level: 3
title: Bounded password hashing
priority: must
status: implemented
links:
  refines: [F-PERF-001]
  constrains: [R-ACC-004]
  implemented_by: [crates/musicus-server/src/auth.rs, crates/musicus-server/src/state.rs]
  decided_in: [tech:d-hashing]
---

# R-PERF-002 Bounded password hashing

## Statement

The server shall run at most as many password hash computations at the same time as it has CPU cores.

## Acceptance criteria

- 60 simultaneous logins on a 1-core machine need no more than about 20 MB for hashing.
