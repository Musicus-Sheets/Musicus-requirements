---
id: R-ANN-005
level: 3
title: Device-independent position
priority: must
status: verified
links:
  refines: [F-ANN-001, F-ANN-003]
  verified_by:
    - crates/musicus-api/src/ink.rs::points_survive_delta_encoding_including_extremes
    - crates/musicus-api/src/ink.rs::round_trip_keeps_every_object
  implemented_by: [crates/musicus-api/src/ink.rs, crates/musicus-web/src/ink.rs]
  decided_in: [tech:d-ink-format]
---

# R-ANN-005 Device-independent position

## Statement

The system shall store annotation positions relative to the page, so that markings appear at the same place in the music on every screen size and zoom level.

## Acceptance criteria

- Markings drawn on a tablet appear at the same notes on a laptop.
- Coordinates at the page corners survive saving and loading unchanged.
