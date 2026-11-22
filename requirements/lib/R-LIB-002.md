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
    - crates/musicus-server/tests/api.rs::parts_with_several_voices
    - crates/musicus-api/src/naming.rs::voices_are_cleaned
    - crates/musicus-api/src/dto.rs::part_input_accepts_blank_label_and_numeric_voices
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-api/src/naming.rs
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-web/src/pages/score_edit.rs
    - crates/musicus-web/src/pages/forms.rs
    - crates/musicus-server/schema.sql
---

# R-LIB-002 Part metadata

## Statement

The system shall store for each part an optional custom name, one or more instruments, an ordered list of up to 10 voices (none, one or several; each free text of up to 20 characters, e.g. '2', '1a', 'Solo'), an optional key (R-LIB-011), and notes. It shall store the voices so that it knows which voices a part contains (R-ACL-005), keep their order, ignore blank entries and drop repeated voices, ignoring letter case.

## Acceptance criteria

- A part can be tagged with two instruments ('Flute / Piccolo').
- A part can be created without a custom name; the voice '1a' is stored as entered; a voice longer than 20 characters or more than 10 voices are rejected with HTTP 400.
- Voices ' 2 ', 1, '', '2', 'solo', 'Solo' are stored as '2', '1', 'solo' in this order; '3 & 4' entered as one voice is stored as the two voices '3' and '4' ('&' separates voices in names, R-LIB-010).
- In the web client the voices are entered as chips: comma, '&' or Enter finish a voice, Backspace removes the one before the cursor.

## Notes

Until migration 0002 the label was required and the voice was a number 0–99; existing labels became custom names and numeric voices text (R-LIB-012). Until migration 0005 a part had at most one voice; it became the only entry of the list.
