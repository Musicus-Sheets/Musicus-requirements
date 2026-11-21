---
id: F-OPS-006
level: 2
title: Supported platforms
priority: must
status: accepted
links:
  refines: [G-005]
  depends_on: [F-OPS-001]
---

# F-OPS-006 Supported platforms

## Statement

Musicus runs with Docker Compose (the preferred way) and as a plain program on Linux, Windows and macOS, including 64-bit Raspberry Pi computers.

## Rationale

Ensembles use what they have: a Raspberry Pi in the rehearsal room, a small rented server, or an old laptop. Docker Compose makes installing and updating one copy-paste step; the plain program keeps Musicus usable where Docker is not available or not wanted.

## Notes

Plan: docs/technical, chapter "Updates, downgrades and platforms" (label `updates`).
