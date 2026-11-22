---
id: R-OPS-030
level: 3
title: Web client inside the program
priority: must
status: verified
links:
  refines: [F-OPS-006]
  constrains: [R-OPS-001]
  verified_by:
    - crates/musicus-server/tests/embedded_web.rs::every_embedded_file_is_served
    - crates/musicus-server/tests/embedded_web.rs::web_dir_overrides_the_builtin_client
    - crates/musicus-server/src/web.rs
  implemented_by:
    - crates/musicus-server/build.rs
    - crates/musicus-server/src/web.rs
    - crates/musicus-server/src/main.rs
    - crates/musicus-server/Cargo.toml
    - Dockerfile
---

# R-OPS-030 Web client inside the program

## Statement

The plain program shall contain the web client, so that it runs without a separate web folder.

## Acceptance criteria

- Starting the release program with only `--data-dir` serves the web client.
- `--web-dir` still overrides the built-in client (development).

## Notes

User decision: the plain program is a single file on every system. Implemented as the cargo feature `embed-web` of the server: a release build (`cargo build --release -p musicus-server --features embed-web`, after `dx bundle --release`) contains every file of the built client; a build without the feature contains none and warns at start (development). The container image uses the built-in client too (no separate web folder). The client files are embedded uncompressed (about 5.4 MB); precompressed `.br`/`.gz` copies are served when the build folder has them. Verified with a test fixture in CI and by hand with the real client (browser smoke test); not yet on Windows or macOS (R-OPS-032).
