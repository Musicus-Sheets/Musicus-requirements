---
id: R-OPS-002
level: 3
title: Configuration
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by: [crates/musicus-server/src/config.rs]
---

# R-OPS-002 Configuration

## Statement

The server shall read every setting from a command-line option or an equivalent MUSICUS_* environment variable.

## Acceptance criteria

- MUSICUS_LISTEN=0.0.0.0:9000 makes the server listen on port 9000.
