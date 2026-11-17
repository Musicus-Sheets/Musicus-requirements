---
id: R-READ-010
level: 3
title: Detect music systems of every file
priority: should
status: verified
links:
  refines: [F-READ-003]
  depends_on: [R-FILE-001]
  constrains: [R-PERF-008]
  verified_by:
    - crates/musicus-server/src/layout/mod.rs::tests
    - crates/musicus-server/tests/api.rs::system_layouts_are_detected_in_the_background_and_follow_file_access
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/layout/detect.rs
    - crates/musicus-server/src/layout/mod.rs
    - crates/musicus-server/src/layout/worker.rs
    - crates/musicus-server/src/routes/files.rs
  decided_in: [tech:d-system-layout]
---

# R-READ-010 Detect music systems of every file

## Statement

The server shall find, for every page of every PDF file, the staves, the music systems they form, the cut lines between the systems, a header above and a footer below them and a confidence value, once per file in the background after the upload, and serve the result to everyone who may read the file at `GET /api/files/{sha256}/layout`.

## Acceptance criteria

- An upload returns at once; the layout is `pending` until a background worker has analysed the file, then `done` (or `failed` if the PDF cannot be read).
- Staves connected by a system barline, brace or bracket form one system; a single staff without such a connection is a system of its own; five-line staves (incl. percussion) and six-line tablature staves are found.
- Markings between two systems (dynamics, tempo, lyrics, rehearsal marks) stay with their system: cuts lie in the longest ink-free band between the systems; ink starting within 4 line distances below the last staff (dynamics, 8vb lines, low notes) stays with the last system.
- Files that exist before this feature, and all files after the detection algorithm changed (`ALGORITHM_VERSION`), are analysed in the background after the start, newest first, without blocking requests.
- Someone who may not read the file gets 404.

## Notes

Regression on 23 real scores (local, not committed): see `docs/agents/layout.md`.
