---
id: R-ANN-019
level: 3
title: Simple shapes
priority: could
status: proposed
links:
  refines: [F-ANN-001]
---

# R-ANN-019 Simple shapes

## Statement

The web client shall let members draw straight lines, rectangles and ellipses as annotation objects.

## Acceptance criteria

- A line drawn with the shape tool is stored as one object and erased as one object.

## Notes

Needs a new `InkObject` variant and therefore a new ink format version (keep decoding version 1).
