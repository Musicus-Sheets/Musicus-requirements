---
id: R-LIB-019
level: 3
title: Review of an import
priority: should
status: verified
links:
  refines: [F-LIB-004]
  depends_on: [R-LIB-017, R-LIB-018, R-ACL-001]
  verified_by:
    - e2e/smoke.mjs
    - crates/musicus-api/src/import/review.rs::instruments_resolve_through_aliases_names_and_the_dictionary
    - crates/musicus-api/src/import/review.rs::existing_pieces_are_suggested_not_chosen
    - crates/musicus-api/src/import/review.rs::contradictions_overrides_and_layout_warnings
    - crates/musicus-server/tests/api.rs::import_stages_reviews_commits_and_undoes
  implemented_by:
    - crates/musicus-web/src/pages/import_review.rs
    - crates/musicus-api/src/import/review.rs
    - crates/musicus-server/src/routes/import.rs
  decided_in: [tech:d-import-staging]
---

# R-LIB-019 Review of an import

## Statement

Before anything is created, the import shall show one row per proposed piece with its parts. Every value shall show where it comes from (file name, dictionary, stored alias, library, librarian) and a colour: green = sure, yellow = please check (abbreviation, guessed word, ambiguous key, numbers read as voices without a separator between them, a similar or matching piece already exists), red = unknown or contradictory (blocks the commit). Each part shall show a small preview of page 1, its resulting name and the groups that will be able to read it. A piece with the same archive number, or the same title and composer, as an existing piece shall be offered as "add the parts to the existing piece", which the librarian must confirm. Librarians shall be able to correct every value, including the list of voices of a part, edit several pieces at once (genre, composer, arranger), and skip single files. Where the system detection has analysed a file, a part named as full score with one staff per system, or a single-instrument part with four or more staves per system, shall be flagged.

## Acceptance criteria

- A part whose instrument word is unknown is red, and the piece cannot be committed.
- A piece whose number matches an existing piece is yellow until the librarian chooses "add to existing" or "new piece".
- The review lists, per part, the groups whose instrument grants include the part's instrument.
