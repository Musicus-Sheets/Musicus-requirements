---
id: R-OPS-006
level: 3
title: HTTPS
priority: must
status: implemented
links:
  refines: [F-OPS-004]
  implemented_by: [crates/musicus-server/src/main.rs, compose.yaml, deploy/Caddyfile]
---

# R-OPS-006 HTTPS

## Statement

The system shall support HTTPS either directly (certificate and key files) or behind a reverse proxy, and the project shall provide a Compose profile with automatic certificates.

## Acceptance criteria

- With --tls-cert and --tls-key the server answers on HTTPS.
- 'docker compose --profile https up' obtains a Let's Encrypt certificate for MUSICUS_DOMAIN.
