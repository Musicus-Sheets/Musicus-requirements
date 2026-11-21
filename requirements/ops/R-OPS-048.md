---
id: R-OPS-048
level: 3
title: Switch to a new version at a safe moment
priority: must
status: accepted
links:
  refines: [F-OPS-008]
  depends_on: [R-OPS-033, R-OPS-047]
---

# R-OPS-048 Switch to a new version at a safe moment

## Statement

When the server comes back with another version than the open web client, the client shall show "Musicus has been updated", save anything pending and then reload automatically, but never while the user is reading or drawing.

## Acceptance criteria

- The client compares its own version with `GET /api/version` after every reconnect.
- On a difference it shows the notice, saves pending markings, and reloads only at a safe moment: not while the reader (or an editor with unsaved input) is open; for example when the user navigates to the library or the programme list.
- While waiting for the safe moment, the old client keeps working as far as the server accepts its requests.

## Notes

"Safe moment" is to be defined exactly during implementation (for example: no reader open, no unsaved form, no pending save).
