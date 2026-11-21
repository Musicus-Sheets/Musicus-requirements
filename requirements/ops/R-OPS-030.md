---
id: R-OPS-030
level: 3
title: Web client inside the program
priority: should
status: accepted
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

User decision: the plain program is a single file on every system. Today `--web-dir` must point to a separate folder. The container image may keep serving the client from the embedded copy too.
