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
    - crates/musicus-server/src/routes/library.rs::fts_query_quotes_words_and_drops_operators
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-server/migrations/0001_init.sql
---

# R-LIB-004 Search

## Statement

The system shall find scores whose title, subtitle, composer, arranger, genre or tags contain all entered words as word prefixes, ignoring letter case and diacritics, and shall additionally filter by genre and tag.

## Acceptance criteria

- Searching 'fucik flor' finds 'Florentiner Marsch' by 'Julius Fučík'.
- Input such as '" OR NEAR(' is treated as plain words and causes no error.
