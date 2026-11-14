---
id: R-OPS-003
level: 3
title: Container
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by: [Dockerfile, compose.yaml]
---

# R-OPS-003 Container

## Statement

The project shall provide a container image and a Compose file that start the system with persistent data in a volume.

## Acceptance criteria

- 'docker compose up -d --build' starts a healthy system on port 8080.
