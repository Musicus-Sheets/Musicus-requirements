---
id: R-OPS-034
level: 3
title: Version in the user interface
priority: must
status: accepted
links:
  refines: [F-OPS-007]
  depends_on: [R-OPS-033]
---

# R-OPS-034 Version in the user interface

## Statement

The web client shall show the version of the running release to every user, for example in an "About" view.

## Acceptance criteria

- Every role, including members, can open the view that shows the version.
- The version shown equals `GET /api/version`.
