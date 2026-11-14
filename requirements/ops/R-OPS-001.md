---
id: R-OPS-001
level: 3
title: 'One program, one data directory'
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by:
    - crates/musicus-server/src/main.rs
    - crates/musicus-server/src/routes/mod.rs
  decided_in: [tech:d-monolith]
---

# R-OPS-001 One program, one data directory

## Statement

The system shall run as a single server program that serves the API and the web client and keeps all data (database and files) in one configurable directory.

## Acceptance criteria

- Starting the server with --data-dir and --web-dir is all that is needed for a working installation.
