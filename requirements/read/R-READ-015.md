---
id: R-READ-015
level: 3
title: Unsure pages are shown whole
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-READ-010]
  verified_by:
    - crates/musicus-api/src/layout.rs::tests
    - crates/musicus-server/src/layout/mod.rs::tests
  implemented_by: [crates/musicus-api/src/layout.rs, crates/musicus-server/src/layout/mod.rs, crates/musicus-web/src/pages/viewer.rs]
---

# R-READ-015 Unsure pages are shown whole

## Statement

A page without systems or with a detection confidence below 0.6 shall appear in the system view as one whole page, fitted to the screen, at its place in the sequence; while a file's layout is pending or failed, the reader shall show whole pages and say why.

## Acceptance criteria

- Title pages, text pages and blank pages appear whole.
- A file still being analysed opens in the page view with a note; the system view starts once the layout is there.
