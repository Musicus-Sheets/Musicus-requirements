---
id: R-LIB-002
level: 3
title: Part metadata
priority: must
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-003]
  verified_by:
    - crates/musicus-server/tests/api.rs::members_only_reach_granted_parts
    - crates/musicus-server/tests/api.rs::part_names_keys_and_part_search
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-web/src/pages/score_edit.rs
    - crates/musicus-web/src/pages/forms.rs
---

# R-LIB-002 Part metadata

## Statement

The system shall store for each part an optional custom name, one or more instruments, an optional voice as free text of up to 20 characters (e.g. '2', '1a', 'Solo'), an optional key (R-LIB-011), and notes.

## Acceptance criteria

- A part can be tagged with two instruments ('Flute / Piccolo').
- A part can be created without a custom name; the voice '1a' is stored as entered; a voice longer than 20 characters is rejected with HTTP 400.

## Notes

Until migration 0002 the label was required and the voice was a number 0–99; existing labels became custom names and numeric voices text (R-LIB-012).
