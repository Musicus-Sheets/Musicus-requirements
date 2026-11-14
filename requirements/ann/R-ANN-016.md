---
id: R-ANN-016
level: 3
title: Sets belong to a file version
priority: must
status: verified
links:
  refines: [F-ANN-005]
  depends_on: [R-FILE-002]
  verified_by:
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
  implemented_by:
    - crates/musicus-server/src/routes/annotations.rs
    - crates/musicus-web/src/pages/viewer.rs
---

# R-ANN-016 Sets belong to a file version

## Statement

The system shall bind every annotation set to the file version it was drawn on, show the member when a newer version exists, and move the set to the current version on request if the page count is unchanged; otherwise it shall refuse the move.

## Acceptance criteria

- After a corrected upload with the same page count, 'Move them to the current version' succeeds.
- With a different page count the move is refused with HTTP 409.
