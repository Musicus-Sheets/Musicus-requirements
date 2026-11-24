---
id: R-OPS-008
level: 3
title: Graceful shutdown
priority: must
status: verified
links:
  refines: [F-OPS-001]
  implemented_by: [crates/musicus-server/src/main.rs, crates/musicus-server/src/lifecycle.rs]
  verified_by: [crates/musicus-server/tests/shutdown.rs::the_process_drains_and_exits_after_the_last_request]
---

# R-OPS-008 Graceful shutdown

## Statement

When the server receives SIGTERM or Ctrl-C, it shall stop accepting connections and let running requests finish.

## Acceptance criteria

- Stopping the container during an annotation save does not lose the save.

## Notes

Refined by R-OPS-043 (announcement, grace, `server_shutting_down`).
