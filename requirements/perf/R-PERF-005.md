---
id: R-PERF-005
level: 3
title: Fast access check
priority: must
status: implemented
links:
  refines: [F-PERF-002]
  constrains: [R-ACL-001]
  implemented_by:
    - crates/musicus-server/src/access.rs
  decided_in: [tech:d-access]
---

# R-PERF-005 Fast access check

## Statement

The server shall decide whether a user may read a part in less than 1 ms for a library of 200 000 parts.

## Acceptance criteria

- Prototype benchmark with 200 000 parts: about 25 µs per check.
