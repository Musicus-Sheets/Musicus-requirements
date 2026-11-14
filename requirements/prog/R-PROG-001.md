---
id: R-PROG-001
level: 3
title: Programme content
priority: must
status: verified
links:
  refines: [F-PROG-001]
  verified_by:
    - crates/musicus-server/tests/api.rs::programmes_and_search
    - crates/musicus-server/src/routes/programmes.rs::dates
    - e2e/smoke.mjs
  implemented_by:
    - crates/musicus-server/src/routes/programmes.rs
    - crates/musicus-web/src/pages/manage.rs
---

# R-PROG-001 Programme content

## Statement

The system shall store for each programme a title, an optional date (YYYY-MM-DD), notes, and an ordered list of up to 200 scores in which a score may appear more than once.

## Acceptance criteria

- A programme with the march at positions 1 and 3 (encore) keeps both.
- The date '24.12.2026' is rejected with HTTP 400.
