---
id: R-READ-011
level: 3
title: Views of whole systems at a minimum staff size
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-READ-010, R-READ-014]
  verified_by:
    - crates/musicus-api/src/layout.rs::tests
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-api/src/layout.rs
    - crates/musicus-web/src/pages/viewer.rs
    - crates/musicus-web/js/bridge.js
  decided_in: [tech:d-system-layout]
---

# R-READ-011 Views of whole systems at a minimum staff size

## Statement

In the system view, the web client shall show as many whole systems as fit on the screen at the user's minimum staff height, stacked and cropped to the horizontal extent of the music, and enlarge them to fill the screen; a system shall never be cut. If even one system cannot reach the minimum height because the music is wider than the screen, it shall be shown at the full screen width.

## Acceptance criteria

- A larger staff size gives fewer systems per view, never a cut system.
- The crops are rendered sharp at the device pixel ratio; the next view is rendered ahead.
- Turning the tablet re-plans the views and keeps the reading position.
- The view algorithm is the one documented in the technical documentation, chapter "System view".
