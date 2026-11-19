---
id: R-LIB-020
level: 3
title: Instrument aliases of the import
priority: should
status: verified
links:
  refines: [F-LIB-004]
  depends_on: [R-LIB-003, R-ACL-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::import_stages_reviews_commits_and_undoes
    - crates/musicus-api/src/import/review.rs::instruments_resolve_through_aliases_names_and_the_dictionary
  implemented_by:
    - crates/musicus-server/src/routes/import.rs
    - crates/musicus-api/src/import/review.rs
  decided_in: [tech:d-import-staging]
---

# R-LIB-020 Instrument aliases of the import

## Statement

The import shall never create an instrument by itself. For an unknown or abbreviated instrument word, the librarian shall choose an existing instrument or create a new one with an explicit action; the choice shall be stored as an alias of that word and applied at once to every row of every open import and to future imports.

## Rationale

Instruments are a controlled vocabulary (R-LIB-003) and decide who reads a part (R-ACL-001). A silently created "Klar." instrument would hide all clarinet parts from the clarinet group.

## Acceptance criteria

- Mapping "Klar" to "Clarinet" once turns every part named "Klar …" green, in this and later batches.
- "Partitur" and "Direktion" can be created as instruments from the review; both exist side by side.
