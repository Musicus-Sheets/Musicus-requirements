---
id: R-OPS-046
level: 3
title: Client notice while the server starts
priority: must
status: accepted
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-045]
---

# R-OPS-046 Client notice while the server starts

## Statement

When the server answers "starting", the web client shall show the banner "Server is starting" and remove it by itself as soon as the server is ready, by polling a status endpoint.

## Acceptance criteria

- With the server in the starting state, the open client shows "Server is starting" and polls (for example `GET /api/version`) at most every few seconds.
- When the server is ready, the banner disappears without a reload or a click, and blocked actions work again.
