---
id: R-OPS-004
level: 3
title: Automatic migrations
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by: [crates/musicus-server/src/db.rs, crates/musicus-server/src/updates]
  verified_by: [crates/musicus-server/tests/updates.rs::fresh_install_runs_every_update_and_writes_the_marker]
---

# R-OPS-004 Automatic migrations

## Statement

When the server starts, it shall bring the database schema to the current version automatically.

## Acceptance criteria

- Starting a new version on an old data directory upgrades the schema without manual steps.
