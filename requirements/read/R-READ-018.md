---
id: R-READ-018
level: 3
title: Annotations in the system view
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-ANN-005, R-ANN-012]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/ink.rs, crates/musicus-web/src/pages/viewer.rs]
---

# R-READ-018 Annotations in the system view

## Statement

In the system view, annotations shall be shown on every crop and drawn, erased, stamped and typed there exactly as in the page view, stored in the coordinates of the whole page.

## Acceptance criteria

- A stroke drawn in the system view appears at the same place of the page in the page view, and the other way round.
- A straight stroke drawn across several systems of a page stays straight and continuous, also after a reload and in the page view (it cannot continue onto the next page).
