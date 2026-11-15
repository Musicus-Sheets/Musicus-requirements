---
id: R-LIB-008
level: 3
title: Instrument list for every user
priority: should
status: verified
links:
  refines: [F-LIB-001]
  depends_on: [R-LIB-003]
  verified_by:
    - e2e/smoke.mjs
    - crates/musicus-server/tests/api.rs::instruments_are_listed_for_everyone_and_kept_while_in_use
  implemented_by:
    - crates/musicus-web/src/pages/instruments.rs
    - crates/musicus-server/src/routes/groups.rs
---

# R-LIB-008 Instrument list for every user

## Statement

The system shall show every logged-in user the instruments of the ensemble with their family, grouped by family.

## Acceptance criteria

- A member opens "Instruments" and sees "Trumpet" under "Brass".
- `GET /api/instruments` with a member's session returns all instruments with their families.
