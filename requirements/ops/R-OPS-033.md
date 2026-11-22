---
id: R-OPS-033
level: 3
title: Version endpoint
priority: must
status: verified
links:
  refines: [F-OPS-007]
  verified_by: [crates/musicus-server/tests/api.rs::version_is_public_and_matches_the_program]
  implemented_by:
    - crates/musicus-api/src/dto.rs
    - crates/musicus-server/src/routes/mod.rs
    - crates/musicus-server/src/config.rs
---

# R-OPS-033 Version endpoint

## Statement

The system shall answer `GET /api/version` without login with the version of the running release.

## Acceptance criteria

- `GET /api/version` returns 200 with JSON containing `version` equal to the release version (for example "1.2.0"), without a session.
- `musicus-server --version` prints the same version.

## Notes

Public on purpose (user decision); it reveals only the version number.
The number is the workspace `version` of the root `Cargo.toml` (`musicus_api::VERSION`),
shared by `--version`, the endpoint and the web client. The answer is not cached
(`Cache-Control: no-store`), so an open client can notice an update.
