---
id: R-READ-008
level: 3
title: Conductor push
priority: could
status: proposed
links:
  refines: [F-READ-002]
---

# R-READ-008 Conductor push

## Statement

When the conductor selects the next piece of a programme, the web client of every member reading that programme shall offer to open it.

## Acceptance criteria

- Within 2 s after the conductor's selection, members see the next piece offered.

## Notes

Needs a server push channel (Server-Sent Events or WebSocket), which version 0.1 does not have. With PostgreSQL, LISTEN/NOTIFY could carry the signal across several server instances.
