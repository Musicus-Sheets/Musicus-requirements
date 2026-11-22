---
id: R-OPS-011
level: 3
title: Upgrade from any older release
priority: must
status: implemented
links:
  refines: [F-OPS-005]
  constrains: [R-OPS-004]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/updates/runner.rs
    - crates/musicus-server/src/db.rs
  verified_by:
    - crates/musicus-server/tests/updates.rs::fresh_install_runs_every_update_and_writes_the_marker
    - crates/musicus-server/tests/updates.rs::baseline_equals_the_development_migrations
---

# R-OPS-011 Upgrade from any older release

## Statement

The system shall upgrade the data directory of any earlier release, from 1.0.0 on, directly to the current release at start, without requiring intermediate releases to be installed first.

## Acceptance criteria

- An automated test opens a data directory created by each earlier minor release (from 1.0.0) with the current release; each starts and passes the same data checks as R-OPS-012.
- Skipping releases (for example from 1.0.2 straight to 1.7.0) needs the same single start as an upgrade to the next release.

## Notes

Fixture data directories are created with each release (see the plan's test section).
