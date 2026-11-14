---
id: R-ANN-011
level: 3
title: Saving when the tab closes
priority: must
status: verified
links:
  refines: [F-ANN-003]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/js/bridge.js, crates/musicus-web/src/pages/viewer.rs]
  decided_in: [tech:d-reader-store]
---

# R-ANN-011 Saving when the tab closes

## Statement

When the tab is closed or reloaded while changes are unsaved, the web client shall still send them to the server.

## Acceptance criteria

- Drawing a stroke and reloading immediately stores the stroke (page revision increases).
