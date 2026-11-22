---
id: R-OPS-015
level: 3
title: Clear refusal outside the downgrade window
priority: must
status: implemented
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-014]
  decided_in: [tech:d-update-model]
  implemented_by:
    - crates/musicus-server/src/updates/runner.rs
    - crates/musicus-server/src/updates/mod.rs
  verified_by:
    - crates/musicus-server/tests/updates.rs::removal_runs_only_when_due_and_older_releases_are_then_refused
---

# R-OPS-015 Clear refusal outside the downgrade window

## Statement

When a release is started on a data directory that it may not use (outside the downgrade window), the system shall not change the data directory, shall exit with an error, and shall name the oldest release that can be started on it.

## Acceptance criteria

- Starting 1.1.0 on a data directory that requires at least 1.2.0 exits with a non-zero code and a message such as "This data was last used by Musicus 1.5.0. Musicus 1.1.0 can no longer use it; start Musicus 1.2.0 or newer."
- The database file and the blob folder are byte-identical before and after the refused start.
- In Docker the message is the last line of `docker compose logs musicus`.
