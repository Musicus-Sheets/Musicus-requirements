---
id: R-LIB-009
level: 3
title: Guided flow for adding a piece
priority: should
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-001, R-LIB-002, R-FILE-001]
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/pages/score_edit.rs
    - crates/musicus-web/src/pages/forms.rs
  decided_in: [tech:d-inline-management]
---

# R-LIB-009 Guided flow for adding a piece

## Statement

When a librarian adds a piece, the web client shall guide them in two visible steps, first the score details and then its parts, where each part is entered with label, instruments, voice, key and an optional PDF, several parts can be added one after another, and the upload state of every added part is shown.

## Acceptance criteria

- The step indicator shows "Details" and "Parts and PDFs"; the title is required in step 1.
- After adding a part the form is empty again (including the chosen instruments), and the added part shows "Uploading…" and then its version and page count, or "No PDF yet".
- "Finish" is disabled while uploads run and then opens the library with the new piece highlighted.
