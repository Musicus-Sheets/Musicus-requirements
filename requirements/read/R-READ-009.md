---
id: R-READ-009
level: 3
title: Swipe to turn pages
priority: should
status: verified
links:
  refines: [F-READ-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs]
---

# R-READ-009 Swipe to turn pages

## Statement

In reading mode, the web client shall turn to the next page on a swipe to the left and to the previous page on a swipe to the right.

## Acceptance criteria

- A horizontal swipe on a tablet turns the page in the swipe direction.
- A move counts as a swipe from 60 CSS px, and only if it is at least twice as wide as high; the tap that ends a swipe does not turn again.
- In the system view, swipes turn views (R-READ-012).
