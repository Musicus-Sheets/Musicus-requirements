---
id: R-OPS-046
level: 3
title: Client notice while the server starts
priority: must
status: verified
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-045]
  implemented_by:
    - crates/musicus-web/src/connection.rs
    - crates/musicus-web/src/ui.rs
    - crates/musicus-web/src/main.rs
  verified_by:
    - crates/musicus-web/src/connection.rs::tests
    - e2e/outage.mjs
---

# R-OPS-046 Client notice while the server starts

## Statement

When the server announces or answers "starting", the web client shall show the banner "Server is starting", keep blocking the actions that need the server (drawing included), and remove the banner by itself as soon as the server is ready.

## Acceptance criteria

- With the server in the starting state, the open client shows "Server is starting" and learns the end from the event stream or by polling `GET /api/health` (and then `GET /api/version`) every 3 s.
- When the server is ready, the banner disappears without a reload or a click, blocked actions work again and pending annotations are sent.
- A reload of the page while the server starts does not log the user out (the client asks again for the session).
