---
id: R-OPS-005
level: 3
title: Online backup
priority: must
status: implemented
links:
  refines: [F-OPS-002]
  implemented_by: [crates/musicus-server/src/main.rs, crates/musicus-server/src/db.rs]
---

# R-OPS-005 Online backup

## Statement

The system shall provide a command that writes a consistent copy of the database while the server runs.

## Acceptance criteria

- 'musicus-server backup --to file' succeeds while the server serves requests; the copy opens as a valid database.
