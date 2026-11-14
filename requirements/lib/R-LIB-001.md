---
id: R-LIB-001
level: 3
title: Score metadata
priority: must
status: verified
links:
  refines: [F-LIB-001]
  verified_by:
    - e2e/smoke.mjs
    - crates/musicus-server/tests/api.rs::programmes_and_search
  implemented_by:
    - crates/musicus-server/src/routes/library.rs
    - crates/musicus-web/src/pages/manage.rs
---

# R-LIB-001 Score metadata

## Statement

The system shall store for each score a title (required, at most 200 characters) and optionally a subtitle, composer, arranger, genre, a list of up to 30 tags, and notes.

## Acceptance criteria

- Creating a score without title is rejected with HTTP 400.
- All fields entered on the score page are shown again after reloading.
- Duplicate tags differing only in letter case are stored once.
