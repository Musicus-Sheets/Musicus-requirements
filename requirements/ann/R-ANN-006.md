---
id: R-ANN-006
level: 3
title: Limits of an annotation page
priority: must
status: verified
links:
  refines: [F-ANN-003, F-SEC-002]
  verified_by:
    - crates/musicus-api/src/ink.rs::decode_rejects_bad_input
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
  implemented_by:
    - crates/musicus-api/src/ink.rs
    - crates/musicus-server/src/routes/annotations.rs
---

# R-ANN-006 Limits of an annotation page

## Statement

The system shall reject annotation pages with more than 20 000 objects, strokes with more than 20 000 points, texts longer than 1 000 characters, encodings larger than 4 MiB, duplicate object ids, or malformed content (HTTP 422).

## Acceptance criteria

- Saving malformed bytes returns HTTP 422 and keeps the previous version.
