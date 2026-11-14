---
id: R-ANN-004
level: 3
title: Palm rejection
priority: must
status: implemented
links:
  refines: [F-ANN-001]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs]
---

# R-ANN-004 Palm rejection

## Statement

Once a pen was used in the reader, the web client shall ignore touch input for drawing.

## Acceptance criteria

- Resting the hand on the screen while writing with a pen draws nothing.
