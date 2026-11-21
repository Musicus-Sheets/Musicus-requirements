---
id: R-OPS-030
level: 3
title: Web client inside the program
priority: should
status: proposed
links:
  refines: [F-OPS-006]
  constrains: [R-OPS-001]
---

# R-OPS-030 Web client inside the program

## Statement

The plain program shall contain the web client, so that it runs without a separate web folder.

## Acceptance criteria

- Starting the release program with only `--data-dir` serves the web client.
- `--web-dir` still overrides the built-in client (development).

## Notes

Proposed to make the plain program one file on every system; today `--web-dir` must point to a separate folder.
