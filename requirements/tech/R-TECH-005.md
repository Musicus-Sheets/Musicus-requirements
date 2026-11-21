---
id: R-TECH-005
level: 3
title: File store interface
priority: should
status: accepted
links:
  refines: [F-TECH-002]
  depends_on: [R-FILE-004]
---

# R-TECH-005 File store interface

## Statement

The server shall read and write stored files only through the file store module, without using its file system paths elsewhere.

## Acceptance criteria

- Outside the file store module no code builds or opens a path inside `blobs/`.
- Range requests are served through the file store interface.

## Notes

Today `BlobStore::path()` is used directly by the file routes and the layout worker. An object-storage implementation is not planned.
