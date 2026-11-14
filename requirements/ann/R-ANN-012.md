---
id: R-ANN-012
level: 3
title: Editing on two devices
priority: must
status: verified
links:
  refines: [F-ANN-003]
  depends_on: [R-ANN-005]
  verified_by:
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
    - crates/musicus-api/src/ink.rs::merge_keeps_both_sides_additions_and_deletions
    - crates/musicus-api/src/ink.rs::merge_with_empty_base_is_a_union
  implemented_by:
    - crates/musicus-server/src/routes/annotations.rs
    - crates/musicus-web/src/pages/viewer.rs
    - crates/musicus-api/src/ink.rs
  decided_in: [tech:d-optimistic]
---

# R-ANN-012 Editing on two devices

## Statement

The system shall detect when a page was saved by another device in the meantime (revision check), and the web client shall then merge both versions so that additions and deletions from both devices are kept.

## Acceptance criteria

- A save based on an outdated revision gets HTTP 409 with the current revision.
- After the merge, strokes added on both devices are present and strokes deleted on either device are gone.
