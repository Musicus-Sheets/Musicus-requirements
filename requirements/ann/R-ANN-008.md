---
id: R-ANN-008
level: 3
title: Annotation sets
priority: must
status: verified
links:
  refines: [F-ANN-002]
  verified_by:
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
  implemented_by:
    - crates/musicus-server/src/routes/annotations.rs
    - crates/musicus-web/src/pages/viewer.rs
---

# R-ANN-008 Annotation sets

## Statement

The system shall let members create, rename, duplicate (with all pages), and delete named annotation sets per part, with names unique per member and part, mark exactly one set per part as default, and link a set to a programme.

## Acceptance criteria

- The first set of a part becomes the default.
- Duplicating 'Christmas 2026' as 'Spring 2027' copies its pages.
- Making another set the default removes the flag from the previous one.
