---
id: R-OPS-019
level: 3
title: Snapshot before database updates
priority: must
status: accepted
links:
  refines: [F-OPS-005, F-OPS-002]
  depends_on: [R-FILE-004]
  conflicts_with:
    - id: R-FILE-009
      note: 'A future removal of unused files must treat files referenced by a kept snapshot as used.'
  decided_in: [tech:d-update-model]
---

# R-OPS-019 Snapshot before database updates

## Statement

Before the system applies a database update at start, it shall write a consistent copy of the database into the data directory and keep the three most recent of these copies.

## Acceptance criteria

- Starting a newer release on a data directory with pending updates creates `snapshots/<file>` before the first update runs; the file opens as a valid database of the old state.
- After a fourth such start, the oldest of the snapshots is deleted and three remain.
- A start without pending updates writes no snapshot.
- If there is not enough free space for the snapshot, no update runs and the start fails with a message naming the space needed.

## Notes

Files (blobs) need no copy: they are immutable and only added (R-FILE-004), so a snapshot stays consistent with the blob folder.
