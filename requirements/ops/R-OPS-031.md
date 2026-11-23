---
id: R-OPS-031
level: 3
title: Usual data folder of the operating system
priority: should
status: implemented
links:
  refines: [F-OPS-006]
  verified_by:
    - crates/musicus-server/src/config.rs::linux_uses_xdg_data_home_or_local_share
    - crates/musicus-server/src/config.rs::macos_uses_application_support
    - crates/musicus-server/src/config.rs::windows_uses_appdata
    - crates/musicus-server/src/config.rs::missing_home_asks_for_a_folder
    - crates/musicus-server/src/config.rs::configured_wins_then_existing_legacy_folder
  implemented_by:
    - crates/musicus-server/src/config.rs
    - crates/musicus-server/src/main.rs
    - Dockerfile
---

# R-OPS-031 Usual data folder of the operating system

## Statement

When no data directory is configured, the plain program shall use the usual folder for application data of the operating system.

## Acceptance criteria

- Without `--data-dir`, data goes to the documented folder per system (for example `%APPDATA%` on Windows, `~/Library/Application Support` on macOS); the folder is printed at start.
- The container image keeps `/data`.

## Notes

Before, the default was `data` relative to the working directory, which depends on how the program is started (for example a double click on Windows).

Folders (from environment variables, no library): Linux and other Unix `$XDG_DATA_HOME/musicus` (only if it is an absolute path) or else `~/.local/share/musicus`; macOS `~/Library/Application Support/Musicus`; Windows `%APPDATA%\Musicus`. Without `HOME` (or `APPDATA` on Windows) the program stops and asks for `--data-dir`. Every command (`serve`, `create-admin`, `backup`, `restore`, `retry-update`) uses the same rule and logs `data folder: <path>`. The image sets `MUSICUS_DATA_DIR=/data`.

Compatibility: if nothing is configured and `./data/musicus.sqlite` exists in the working directory (the old default), that folder is still used, with a warning that names the new default and `--data-dir data`; nothing is moved. This fallback should be removed before 1.0.

Status `implemented`, not `verified`: the rules are unit-tested with an injected environment for all three systems, but the program has run only on Linux (R-OPS-032).
