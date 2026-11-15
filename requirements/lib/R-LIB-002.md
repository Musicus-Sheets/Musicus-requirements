---
id: R-LIB-002
level: 3
title: Part metadata
priority: must
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-003]
  verified_by: [crates/musicus-server/tests/api.rs::members_only_reach_granted_parts]
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-web/src/pages/score_edit.rs
    - crates/musicus-web/src/pages/forms.rs
---

# R-LIB-002 Part metadata

## Statement

The system shall store for each part a label (e.g. '2nd Trumpet in Bb'), one or more instruments, an optional voice number between 0 and 99, an optional transposition, and notes.

## Acceptance criteria

- A part can be tagged with two instruments ('Flute / Piccolo').
- A voice outside 0–99 is rejected with HTTP 400.
