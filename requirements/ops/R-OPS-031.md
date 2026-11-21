---
id: R-OPS-031
level: 3
title: Usual data folder of the operating system
priority: could
status: proposed
links:
  refines: [F-OPS-006]
---

# R-OPS-031 Usual data folder of the operating system

## Statement

When no data directory is configured, the plain program shall use the usual folder for application data of the operating system.

## Acceptance criteria

- Without `--data-dir`, data goes to the documented folder per system (for example `%APPDATA%` on Windows, `~/Library/Application Support` on macOS); the folder is printed at start.
- The container image keeps `/data`.

## Notes

Today the default is `data` relative to the working directory, which depends on how the program is started (for example a double click on Windows).
