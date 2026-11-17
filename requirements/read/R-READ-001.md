---
id: R-READ-001
level: 3
title: Page display
priority: must
status: verified
links:
  refines: [F-READ-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs, crates/musicus-web/js/bridge.js, crates/musicus-api/src/pixels.rs]
---

# R-READ-001 Page display

## Statement

The web client shall show one page at a time, scaled to fit the available space, rendered at the device's pixel density, and without blank flashes when the page changes.

## Acceptance criteria

- On a 1024x1366 tablet the whole A4 page is visible and sharp.
- Sharp means shown 1:1: the rendered bitmap has exactly as many pixels as the screen area it covers (CSS size ×
  device pixel ratio, whole pixels), so the browser does not resample it; this holds in the page view and the system
  view, at fractional pixel ratios (e.g. 1.5, 2.625) and at any fit scale.
- When the pixel ratio changes without a size change (browser zoom, window moved to another screen) or the page is
  pinch-zoomed, the shown page is rendered again at the new resolution.
