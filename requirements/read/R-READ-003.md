---
id: R-READ-003
level: 3
title: Screen stays on
priority: must
status: implemented
links:
  refines: [F-READ-001]
  depends_on: [R-OPS-006]
  implemented_by: [crates/musicus-web/js/bridge.js]
---

# R-READ-003 Screen stays on

## Statement

While the reader is open, the web client shall keep the screen from dimming where the browser supports the screen wake lock, and re-acquire it after the tab becomes visible again.

## Acceptance criteria

- On a tablet the screen does not turn off during a 10-minute piece.
