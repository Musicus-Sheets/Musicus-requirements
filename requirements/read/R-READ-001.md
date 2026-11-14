---
id: R-READ-001
level: 3
title: Page display
priority: must
status: verified
links:
  refines: [F-READ-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs, crates/musicus-web/js/bridge.js]
---

# R-READ-001 Page display

## Statement

The web client shall show one page at a time, scaled to fit the available space, rendered at the device's pixel density, and without blank flashes when the page changes.

## Acceptance criteria

- On a 1024x1366 tablet the whole A4 page is visible and sharp.
