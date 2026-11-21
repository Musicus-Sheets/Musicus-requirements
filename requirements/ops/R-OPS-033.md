---
id: R-OPS-033
level: 3
title: Version endpoint
priority: must
status: accepted
links:
  refines: [F-OPS-007]
---

# R-OPS-033 Version endpoint

## Statement

The system shall answer `GET /api/version` without login with the version of the running release.

## Acceptance criteria

- `GET /api/version` returns 200 with JSON containing `version` equal to the release version (for example "1.2.0"), without a session.
- `musicus-server --version` prints the same version.

## Notes

Public on purpose (user decision); it reveals only the version number.
