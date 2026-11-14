---
id: R-SEC-001
level: 3
title: No persistent data in the web client
priority: must
status: implemented
links:
  refines: [F-SEC-001]
  depends_on: [R-FILE-007]
  implemented_by: [crates/musicus-web/js/bridge.js]
  decided_in: [tech:d-no-client-storage]
---

# R-SEC-001 No persistent data in the web client

## Statement

The web client shall keep sheets and annotations only in memory and shall not use local storage, IndexedDB, the Cache API or a service worker.

## Acceptance criteria

- After closing the tab, no sheet or annotation data remains in the browser's site storage.
