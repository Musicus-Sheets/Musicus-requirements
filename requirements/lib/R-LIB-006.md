---
id: R-LIB-006
level: 3
title: Thumbnails in the library
priority: must
status: implemented
links:
  refines: [F-LIB-001]
  depends_on: [R-FILE-003]
  implemented_by: [crates/musicus-web/src/pages/library.rs]
---

# R-LIB-006 Thumbnails in the library

## Statement

The web client shall show for each readable part a thumbnail of its first page, if the server could create one.

## Acceptance criteria

- After uploading a PDF, the library shows the part with an image of its first page.
