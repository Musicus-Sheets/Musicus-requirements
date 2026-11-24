---
id: R-OPS-003
level: 3
title: Container
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by: [Dockerfile, compose.yaml, compose.override.example.yaml]
---

# R-OPS-003 Container

## Statement

The project shall provide a container image and a Compose file that start the system with persistent data in a volume.

## Acceptance criteria

- 'docker compose up -d --build' starts a healthy system on port 8080.
- By default the port is published over IPv4 and IPv6 (127.0.0.1 and ::1 both answer on the host); with MUSICUS_LOCAL_ONLY=true it is reachable only from the host, again over 127.0.0.1 and ::1.
- Specific addresses can be chosen in the administrator's own compose.override.yaml, which updates never overwrite.
- In the same file the data can be kept in a host folder instead of the volume, with the files owned by the administrator's own user (the container runs as that user, never as root); a missing folder stops the start instead of being created for root.
- compose.override.example.yaml shows both cases.

## Notes

Port lines and the reasons: decision a-dual-stack-listen in docs/agents/decisions.md of the main repository; why these choices are not `.env` settings: decision a-compose-override.
