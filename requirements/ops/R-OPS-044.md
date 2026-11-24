---
id: R-OPS-044
level: 3
title: Client notices for a stopping or unreachable server
priority: must
status: verified
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-043]
  implemented_by:
    - crates/musicus-web/src/connection.rs
    - crates/musicus-web/src/api.rs
    - crates/musicus-web/src/ui.rs
    - crates/musicus-web/src/pages/viewer.rs
    - crates/musicus-web/js/bridge.js
  verified_by:
    - crates/musicus-web/src/connection.rs::tests
    - e2e/outage.mjs
---

# R-OPS-044 Client notices for a stopping or unreachable server

## Statement

When the server announces that it is shutting down, the web client shall show the banner "Server is shutting down", first block every action that needs the server (drawing included) and then immediately send everything it has not sent yet; when the server cannot be reached without such an announcement, it shall show "Server not reachable" and keep drawing possible. In both cases everything already loaded stays readable.

## Acceptance criteria

- On the event `shutting_down` (or an answer with code `server_shutting_down`): the banner "Server is shutting down" appears; no new stroke, eraser, stamp, text or undo is possible and no new request is sent; then every annotation page not saved yet (also a stroke still in the 1.5 s delay) is sent at once and stored by the server during its grace.
- If that flush fails, the annotations stay in the tab's memory and the reader says so; they are sent again when the server is back.
- With the network lost (no announcement): the banner "Server not reachable" appears; pages already loaded can still be turned and read, and drawing still works (R-OPS-047).
- Actions that need the server (opening a piece not loaded, uploading, saving a form) are refused with the banner's reason while the server announced that it is away, not with a generic error.
- The banner disappears by itself when the server answers normally again.

## Notes

Order and design: docs/agents decision a-client-outage. Annotation pages are the only writes the client queues; every other save is sent at once.
