---
id: R-PERF-007
level: 3
title: Playing without network
priority: must
status: implemented
links:
  refines: [F-PERF-002]
  depends_on: [R-PROG-003]
  implemented_by: [crates/musicus-web/js/bridge.js]
---

# R-PERF-007 Playing without network

## Statement

Once a programme was prepared, the web client shall be able to show and turn all its pages without further sheet downloads.

## Acceptance criteria

- After the prefetch completes, the network can be disconnected and all pieces of the programme still open.

## Notes

Annotation loading and saving still need the network.
