---
id: R-ANN-010
level: 3
title: Automatic saving
priority: must
status: verified
links:
  refines: [F-ANN-003]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs]
  decided_in: [tech:d-reader-store]
---

# R-ANN-010 Automatic saving

## Statement

The web client shall save a changed page 1.5 s after the last change, immediately when turning the page or leaving the reader, and show whether all changes are saved.

## Acceptance criteria

- About 2 s after a stroke, the status shows 'Saved'.
- Leaving the reader right after a stroke still stores it.
