---
id: R-OPS-020
level: 3
title: Automatic restore after a failed update
priority: must
status: verified
links:
  verified_by:
    - crates/musicus-server/tests/snapshots.rs::a_failed_update_puts_the_snapshot_back_and_is_not_retried
    - crates/musicus-server/tests/snapshots.rs::a_failed_first_start_leaves_an_empty_data_directory
  implemented_by:
    - crates/musicus-server/src/updates/start.rs
    - crates/musicus-server/src/updates/guard.rs
  refines: [F-OPS-005]
  depends_on: [R-OPS-019]
  decided_in: [tech:d-update-model]
---

# R-OPS-020 Automatic restore after a failed update

## Statement

When a database update fails at start, the system shall put back the snapshot taken before it, and stop with a message that says the update failed, that the data is unchanged and which release ran before.

## Acceptance criteria

- Test with a deliberately failing update: after the failed start the database equals the snapshot, the process exits with a non-zero code, and the previous release starts on the data directory again.
- The message names the snapshot file and asks to report the problem.
- Repeated automatic restarts (Docker restart policy) do not create more than the three kept snapshots and do not lose the pre-update state.
