---
id: R-ACC-016
level: 3
title: Several entries chosen at once, applied when the dropdown closes
priority: should
status: verified
links:
  refines: [F-ACC-004]
  depends_on: [R-ACC-015]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/picker.rs]
---

# R-ACC-016 Several entries chosen at once, applied when the dropdown closes

## Statement

When the assignment dropdown is open, ticking an entry shall not close it, and closing it by clicking or tapping outside, by pressing Escape, or with its "Add" button shall add all ticked entries to the assigned list.

## Acceptance criteria

- The dropdown shows how many entries are ticked; ticks are kept while the search text changes.
- Two members ticked in one go appear in the list after a click outside the dropdown.
- Keyboard: Down moves from the search field into the list, Up/Down move between entries, Enter or Space ticks, Enter in the search field ticks the first match, Escape closes and applies; Enter never submits the surrounding form.
- There is no cancel action; an entry ticked by mistake is unticked before closing or removed with "×" afterwards.
- Pieces chosen for a programme are appended in the order they were ticked.
