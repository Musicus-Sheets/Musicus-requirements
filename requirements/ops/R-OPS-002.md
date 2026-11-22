---
id: R-OPS-002
level: 3
title: Configuration
priority: must
status: implemented
links:
  refines: [F-OPS-001]
  implemented_by: [crates/musicus-server/src/config.rs, crates/musicus-server/src/listen.rs]
  verified_by:
    - crates/musicus-server/src/listen.rs::default_accepts_ipv4_and_ipv6
    - crates/musicus-server/src/listen.rs::falls_back_to_ipv4_when_ipv6_is_missing
    - crates/musicus-server/src/listen.rs::explicit_addresses_are_bound_as_given
---

# R-OPS-002 Configuration

## Statement

The server shall read every setting from a command-line option or an equivalent MUSICUS_* environment variable.

## Acceptance criteria

- MUSICUS_LISTEN=0.0.0.0:9000 makes the server listen on port 9000.
- Without MUSICUS_LISTEN the server accepts connections on port 8080 over IPv4 and IPv6 (127.0.0.1 and ::1 both answer), so a reverse proxy may connect to 'localhost'. On a host without IPv6 it listens on IPv4 only and logs a warning.
- An explicitly given address (e.g. 127.0.0.1:8080 or [::1]:8080) is used exactly as given.

## Notes

Dual-stack listening and the IPv4 fallback: decision a-dual-stack-listen in docs/agents/decisions.md of the main repository.
