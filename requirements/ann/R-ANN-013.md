---
id: R-ANN-013
level: 3
title: Pages without markings
priority: must
status: verified
links:
  refines: [F-ANN-003]
  verified_by:
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/annotations.rs
    - crates/musicus-web/src/api.rs
  decided_in: [tech:d-204]
---

# R-ANN-013 Pages without markings

## Statement

The system shall answer requests for an annotation page that was never saved as an empty page with revision 0, not as an error.

## Acceptance criteria

- Loading an unsaved page returns HTTP 204 with ETag "0"; the browser console shows no error.
