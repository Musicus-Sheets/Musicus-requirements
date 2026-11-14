---
id: R-OPS-008
level: 3
title: Graceful shutdown
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by: [crates/musicus-server/src/main.rs]
---

# R-OPS-008 Graceful shutdown

## Statement

When the server receives SIGTERM or Ctrl-C, it shall stop accepting connections and let running requests finish.

## Acceptance criteria

- Stopping the container during an annotation save does not lose the save.
