---
id: R-ANN-003
level: 3
title: Undo and redo
priority: must
status: implemented
links:
  refines: [F-ANN-001]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs]
---

# R-ANN-003 Undo and redo

## Statement

The web client shall let members undo and redo their changes on the current page.

## Acceptance criteria

- Undo after erasing restores the erased object; redo removes it again.
