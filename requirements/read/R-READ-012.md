---
id: R-READ-012
level: 3
title: Turning in the system view
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-READ-011, R-READ-002]
  verified_by:
    - crates/musicus-api/src/layout.rs::tests
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-api/src/layout.rs
    - crates/musicus-web/src/pages/viewer.rs
---

# R-READ-012 Turning in the system view

## Statement

In the system view, the keys, pedals, taps and swipes that turn pages shall turn views; if the current view shows at least three systems the next view shall start with its last system (one system overlap), otherwise with the system after it.

## Acceptance criteria

- With five systems per view, the fifth system of a view is the first of the next one.
- With one or two systems per view, no system is shown twice in a row.
- Turning back shows the previous view again.
