---
id: R-READ-005
level: 3
title: Next and previous piece
priority: must
status: implemented
links:
  refines: [F-READ-002]
  depends_on: [R-PROG-003]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs]
---

# R-READ-005 Next and previous piece

## Statement

When a part was opened from a programme, the web client shall open the next piece when turning past the last page, open the previous piece when turning back before the first page, prefer a part that shares an instrument with the current one, and download the next piece in advance.

## Acceptance criteria

- Turning past the last page of piece 1 opens the trumpet part of piece 2.
- On the last page a 'Next piece' button is shown.
