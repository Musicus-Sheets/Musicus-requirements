---
id: R-READ-013
level: 3
title: Systems continue across pages
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-READ-011, R-READ-005]
  verified_by: [crates/musicus-api/src/layout.rs::tests, e2e/smoke.mjs]
  implemented_by: [crates/musicus-api/src/layout.rs, crates/musicus-web/src/pages/viewer.rs]
---

# R-READ-013 Systems continue across pages

## Statement

The system view shall treat the systems of all pages of a part as one sequence, so that a view may show the last systems of one page and the first systems of the next; after the last view of a part in a programme it shall open the next piece as the page view does.

## Acceptance criteria

- A view can contain systems of two pages; the page counter shows the page of the view's first system.
- Page furniture is skipped: headers and footers smaller than 6 % of the page height except the title block of the first page.
