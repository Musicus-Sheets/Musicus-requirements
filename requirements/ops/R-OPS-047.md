---
id: R-OPS-047
level: 3
title: Unsaved markings survive a server outage
priority: must
status: accepted
links:
  refines: [F-OPS-008]
  depends_on: [R-ANN-011]
  constrains: [R-SEC-001]
---

# R-OPS-047 Unsaved markings survive a server outage

## Statement

While the server is shutting down, starting or unreachable, the web client shall keep markings drawn in that time in the memory of the open tab and save them automatically when the server is back, without storing them on the device.

## Acceptance criteria

- Draw strokes on an open page, stop the server, draw more, start the server: all strokes are saved without user action (page revision increases), conflicts merged as usual (R-ANN-012).
- Nothing is written to browser storage (R-SEC-001).
- Closing or reloading the tab while markings are unsaved and the server is away asks the browser to warn the user (`beforeunload`).

## Notes

Today unsaved pages are sent with `keepalive` when the tab closes (R-ANN-011, d-reader-store); that fails when the server is away, hence the warning.
