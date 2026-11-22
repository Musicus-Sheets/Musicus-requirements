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
- By default the port is published over IPv4 and IPv6 (127.0.0.1 and ::1 both answer on the host); with MUSICUS_BIND=127.0.0.1 it is reachable only from the host, again over 127.0.0.1 and ::1.

## Notes

Port lines and the reasons: decision a-dual-stack-listen in docs/agents/decisions.md of the main repository.
