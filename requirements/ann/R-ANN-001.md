---
id: R-ANN-001
level: 3
title: Pen and highlighter
priority: must
status: verified
links:
  refines: [F-ANN-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs, crates/musicus-web/src/ink.rs]
---

# R-ANN-001 Pen and highlighter

## Statement

The web client shall let members draw freehand with a pen (4 colours, 3 widths, width following pen pressure) and a semi-transparent highlighter (3 colours) that is drawn below pen strokes.

## Acceptance criteria

- A stroke drawn with the mouse appears immediately and is saved.
- Highlighter marks never cover pen marks.
