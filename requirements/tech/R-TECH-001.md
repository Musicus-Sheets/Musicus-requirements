---
id: R-TECH-001
level: 3
title: Server technology
priority: must
status: implemented
links:
  refines: [F-TECH-001]
  implemented_by: [crates/musicus-server]
  decided_in: [tech:d-sqlite, tech:d-monolith]
---

# R-TECH-001 Server technology

## Statement

The server shall be written in Rust and use an embedded SQLite database.

## Acceptance criteria

- The server builds with cargo and needs no separate database server.
