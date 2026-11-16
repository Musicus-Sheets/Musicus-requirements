---
id: R-LIB-013
level: 3
title: Tags entered as chips
priority: should
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/tag_input.rs
    - crates/musicus-web/src/pages/forms.rs
---

# R-LIB-013 Tags entered as chips

## Statement

When a librarian edits the tags of a piece, the web client shall show every finished tag as a non-editable chip like the tags in the library, with a remove button, and a text field before, between or after the chips for the next tag.

## Acceptance criteria

- Typing a comma or pressing Enter turns the typed text into a chip; Enter does not submit the form; text typed without a final comma becomes a chip when the field is left.
- Surrounding spaces are removed, empty tags are ignored, and a tag that already exists (ignoring letter case) is not added again; its chip is highlighted briefly.
- Pasting "Christmas, New Year, Encore" creates three chips; a comma typed on a keyboard that sends no key event (Android) also finishes the tag.
- With the text field empty, the arrow keys (and Home / End) move it between the chips; Backspace at its start removes the chip before it and Delete at its end the chip after it; the caret never enters a chip.
- The "×" of a chip (touch target at least 44 px) removes it; clicking a chip places the text field after it.
