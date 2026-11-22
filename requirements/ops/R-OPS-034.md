---
id: R-OPS-034
level: 3
title: Version in the user interface
priority: must
status: verified
links:
  refines: [F-OPS-007]
  depends_on: [R-OPS-033]
  verified_by: [e2e/smoke.mjs]
  implemented_by:
    - crates/musicus-web/src/pages/about.rs
    - crates/musicus-web/src/api.rs
    - crates/musicus-web/src/pages/login.rs
    - crates/musicus-web/src/pages/account.rs
---

# R-OPS-034 Version in the user interface

## Statement

The web client shall show the version of the running release to every user, for example in an "About" view.

## Acceptance criteria

- Every role, including members, can open the view that shows the version.
- The version shown equals `GET /api/version`.

## Notes

The view is "About Musicus" at `/about`, reachable with and without a login (linked from the
login page and from the end of the account page); it also shows the licence and the source link.
