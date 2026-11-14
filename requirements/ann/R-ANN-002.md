---
id: R-ANN-002
level: 3
title: 'Eraser, stamps and text'
priority: must
status: implemented
links:
  refines: [F-ANN-001]
  implemented_by:
    - crates/musicus-web/src/pages/viewer.rs
    - crates/musicus-web/src/ink.rs
    - crates/musicus-api/src/ink.rs
---

# R-ANN-002 Eraser, stamps and text

## Statement

The web client shall let members erase whole objects by touching them, place musical stamps (breath mark, fermata, glasses, sharp, flat, natural, accent, caesura) with one tap, and place short text notes.

## Acceptance criteria

- Touching a stroke with the eraser removes the whole stroke.
- Choosing 'fermata' and tapping places a fermata at that point.
