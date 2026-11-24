---
id: R-OPS-048
level: 3
title: Switch to a new version at a safe moment
priority: must
status: verified
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-033, R-OPS-047]
  implemented_by:
    - crates/musicus-web/src/connection.rs
    - crates/musicus-web/src/ui.rs
    - crates/musicus-web/js/bridge.js
  verified_by:
    - crates/musicus-web/src/connection.rs::tests
    - e2e/outage.mjs
---

# R-OPS-048 Switch to a new version at a safe moment

## Statement

When the server comes back with another version than the open web client, the client shall show "Musicus has been updated", save anything pending and then reload automatically, but never while the user is reading or drawing.

## Acceptance criteria

- The client compares its own version with the version of every `ready` state it receives (event stream, or `GET /api/version` when polling after a reconnect).
- On a difference it shows the notice with a "Reload now" button.
- It reloads by itself only at a safe moment: the server is ready, no part is open in the reader (reading or drawing; it reloads after the user left the reader for another page), no annotation page is pending, no request runs, and nothing was typed or chosen in a form since the last successful save or page change.
- While waiting for the safe moment, the old client keeps working as far as the server accepts its requests.
