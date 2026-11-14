---
id: R-PERF-003
level: 3
title: Burst of downloads
priority: must
status: implemented
links:
  refines: [F-PERF-002]
  constrains: [R-FILE-005]
  implemented_by:
    - crates/musicus-server/src/routes/files.rs
    - crates/musicus-server/src/cache.rs
---

# R-PERF-003 Burst of downloads

## Statement

The server shall serve 120 simultaneous downloads of the same 3 MB file in less than 1 s of server time on one CPU core.

## Acceptance criteria

- Burst benchmark on one core: 120 clients complete within 1 s over loopback (prototype measured 0.2 s).

## Notes

Measured with the prototype in prototypes/musicus-proto; the product has no automated load test yet.
