---
id: R-OPS-050
level: 3
title: Listen on several addresses at once
priority: could
status: proposed
links:
  refines: [F-OPS-001]
  depends_on: [R-OPS-002]
---

# R-OPS-050 Listen on several addresses at once

## Statement

The plain program shall accept a list of listening addresses (e.g. `MUSICUS_LISTEN=127.0.0.1:8080,[::1]:8080`) and serve the same application on each of them.

## Acceptance criteria

- With `MUSICUS_LISTEN=127.0.0.1:8080,[::1]:8080` the server answers on 127.0.0.1 and ::1 and on no other address.
- If one of the listed addresses cannot be bound, the server does not start and names that address.
- A shutdown closes all listeners; the health check tries the listed addresses in order.

## Notes

Not built for now (decided 2026-11-23). Use cases: "local only" on both IPv4 and IPv6 without a firewall, and
servers with several networks that should expose Musicus on only some of them.

Reasons for not building it yet:

- Docker, the preferred way to run Musicus, already covers both cases (`MUSICUS_LOCAL_ONLY=true`; specific
  addresses via `compose.override.yaml` with `ports: !override`).
- Behind a reverse proxy on the same host, a single `MUSICUS_LISTEN=127.0.0.1:8080` with
  `proxy_pass http://127.0.0.1:8080` is enough; reachable directly, the default `[::]:8080` with a firewall is
  more robust.
- Specific addresses are fragile: at boot the network may not be up yet (DHCP, late IPv6 addresses), and
  addresses change (DHCP leases, IPv6 privacy addresses), so the server would fail to start or listen in the
  wrong place.
- Common in infrastructure software (nginx, OpenSSH, PostgreSQL), uncommon in web applications that run behind a
  reverse proxy.

Revisit if an ensemble needs it.
