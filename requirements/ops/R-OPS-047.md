---
id: R-OPS-047
level: 3
title: Unsaved annotations survive a server outage
priority: must
status: verified
links:
  refines: [F-OPS-008]
  depends_on: [R-ANN-011]
  constrains: [R-SEC-001]
  implemented_by:
    - crates/musicus-web/src/pages/viewer.rs
    - crates/musicus-web/src/connection.rs
    - crates/musicus-web/js/bridge.js
  verified_by:
    - e2e/outage.mjs
---

# R-OPS-047 Unsaved annotations survive a server outage

## Statement

The web client shall keep annotations not saved yet in the memory of the open tab while the server is shutting down, starting or unreachable, and save them automatically when the server is back, without storing them on the device; annotations drawn while the server is merely unreachable (no announcement) are kept the same way.

## Acceptance criteria

- Draw a stroke and stop the server before it was saved: it is sent at once and stored (R-OPS-044).
- With the network lost, draw strokes, then restore the network: all strokes are saved without user action (page revision increases), conflicts merged as usual (R-ANN-012).
- When the server refuses a page for good (for example `invalid_ink` from a server that was updated in between), the annotations stay in memory, the reader shows "These annotations couldn't be saved" with the reason, and nothing is dropped silently.
- Nothing is written to browser storage (R-SEC-001).
- Closing or reloading the tab while annotations are unsaved and the server is away (or refused them) asks the browser to warn the user (`beforeunload`).

## Notes

Unsaved pages are also sent with `keepalive` when the tab closes (R-ANN-011, d-reader-store); that fails when the server is away, hence the warning. No ink format conversion exists; the server keeps every old ink decoder as a cheap safety net.
