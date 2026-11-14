---
id: R-ANN-014
level: 3
title: Only the owner sees annotations
priority: must
status: verified
links:
  refines: [F-ANN-004]
  verified_by:
    - crates/musicus-server/tests/api.rs::annotations_are_private_versioned_and_conflict_checked
    - e2e/smoke.mjs
  implemented_by: [crates/musicus-server/src/routes/annotations.rs]
---

# R-ANN-014 Only the owner sees annotations

## Statement

The system shall let only the member who created an annotation set read, change or delete it; no other user, administrators included, can access it through the system.

## Acceptance criteria

- An admin requesting another member's page gets HTTP 404 and sees no sets for that part.
