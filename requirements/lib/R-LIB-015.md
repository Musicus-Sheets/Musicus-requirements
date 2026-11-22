---
id: R-LIB-015
level: 3
title: Archive number of a piece
priority: should
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-001, R-LIB-004]
  verified_by:
    - crates/musicus-server/tests/api.rs::archive_numbers_are_free_text_searchable_and_not_unique
    - crates/musicus-api/src/naming.rs::archive_numbers
    - crates/musicus-api/src/dto.rs::score_input_trims_the_archive_number
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-api/src/naming.rs
    - crates/musicus-web/src/pages/forms.rs
    - crates/musicus-web/src/pages/library.rs
    - crates/musicus-server/schema.sql
---

# R-LIB-015 Archive number of a piece

## Statement

The system shall store for each score optionally an archive number: free text of at most 40 characters (e.g. "0304" or "A-12"), trimmed, an empty entry meaning none. The number is not required to be unique. The library shall show it with the piece, shall find a piece by it (also without leading zeros or separators: "304" finds "0304", "A12" finds "A-12") and shall offer to sort the list by it in natural order ("28" before "304").

## Rationale

Ensembles keep their paper sheets in numbered folders. The number links a piece in Musicus to its folder, lets a librarian find a piece by the label on the folder, and lets an import of many files recognise pieces that are already in the library.

## Acceptance criteria

- A piece saved with the archive number " 0304 " shows "0304" after reloading.
- Searching "304" or "0304" finds it; a member finds it only if they may read one of its parts.
- Two pieces may have the same archive number.
- An archive number of 41 characters is rejected with HTTP 400.

## Notes

Not unique on purpose: real archives contain gaps, double numbers and typos, and a unique constraint would block the import of such an archive. The import uses the number only to suggest a match, which the librarian confirms.
