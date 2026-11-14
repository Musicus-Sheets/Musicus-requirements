---
id: R-SEC-007
level: 3
title: 'Minimal, unprivileged container'
priority: should
status: implemented
links:
  refines: [F-SEC-002, F-OPS-001]
  implemented_by: [Dockerfile]
  decided_in: [tech:d-distroless]
---

# R-SEC-007 Minimal, unprivileged container

## Statement

The container image shall contain only the server, the web assets and the C runtime, and run as an unprivileged user.

## Acceptance criteria

- The image has no shell; the process runs as UID 65532.
