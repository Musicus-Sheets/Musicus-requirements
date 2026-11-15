---
id: R-LIB-004
level: 3
title: Search
priority: must
status: verified
links:
  refines: [F-LIB-002]
  verified_by:
    - crates/musicus-server/tests/api.rs::programmes_and_search
    - crates/musicus-server/src/routes/library.rs::fts_terms_quote_words_and_drop_operators
    - crates/musicus-server/tests/api.rs::part_names_keys_and_part_search
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-server/migrations/0001_init.sql
    - crates/musicus-server/migrations/0002_part_names.sql
    - crates/musicus-server/src/part_index.rs
---

# R-LIB-004 Search

## Statement

The system shall find scores for which every entered word is a word prefix of the title, subtitle, composer, arranger, genre or tags, or of the name of a part of the score the user may read (R-LIB-010), ignoring letter case and diacritics, and shall additionally filter by genre and tag.

## Acceptance criteria

- Searching 'fucik flor' finds 'Florentiner Marsch' by 'Julius Fučík'.
- Input such as '" OR NEAR(' is treated as plain words and causes no error.
- A member of the trumpet group finds the march with 'trumpet' and with 'fucik trumpet', but not with the name of its flute part.
