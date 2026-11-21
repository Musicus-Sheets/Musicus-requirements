---
id: R-OPS-044
level: 3
title: Client notices for a stopping or unreachable server
priority: must
status: accepted
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-043]
---

# R-OPS-044 Client notices for a stopping or unreachable server

## Statement

When the server answers "shutting down" or cannot be reached, the web client shall show a banner ("Server is shutting down" or "Server not reachable"), keep everything already loaded readable, and block only the actions that need the server.

## Acceptance criteria

- With the server stopped while a part is open in the reader: the banner "Server not reachable" appears at the first failed request; pages already loaded can still be turned and read, and drawing still works (R-OPS-047).
- An answer with code `server_shutting_down` shows "Server is shutting down".
- Actions that need the server (opening a piece not loaded, uploading, saving a form) are disabled or answered with the banner, not with a generic error.
- The banner disappears by itself when the server answers normally again.
