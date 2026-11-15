---
id: R-ACC-015
level: 3
title: Assignments scale to many entries
priority: should
status: verified
links:
  refines: [F-ACC-004]
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/picker.rs
    - crates/musicus-web/src/pages/groups.rs
    - crates/musicus-web/src/pages/forms.rs
    - crates/musicus-web/src/pages/programme_edit.rs
---

# R-ACC-015 Assignments scale to many entries

## Statement

When a librarian or admin assigns users, instruments or scores to a group, instruments to a part, or pieces to a programme, the web client shall show only the assigned entries as a list, each with a remove control, and offer the other entries in a dropdown with a search field instead of one checkbox per existing entry.

## Acceptance criteria

- A group's members, instrument grants and score grants, a part's instruments (in the guided flow and in the part editor) and the pieces of a programme are each shown as a list of assigned entries with a "×" (touch target at least 44 px), or a text such as "No members yet." when empty.
- Opening the dropdown puts the focus in its search field; typing filters case- and diacritics-insensitively on all shown text ("zoe" finds "Zoë Brandt", a composer finds his pieces).
- Long lists scroll inside the dropdown; on a phone-width screen the dropdown stays inside the screen.
- The programme dropdown keeps pieces already in the programme selectable (encores) and marks them.
