---
id: R-SEC-005
level: 3
title: Security headers
priority: must
status: implemented
links:
  refines: [F-SEC-002]
  implemented_by: [crates/musicus-server/src/routes/mod.rs]
---

# R-SEC-005 Security headers

## Statement

The system shall send with every response the headers X-Content-Type-Options: nosniff, X-Frame-Options: DENY, Referrer-Policy: same-origin and a Permissions-Policy that disables camera, microphone and geolocation.

## Acceptance criteria

- Any response, including errors, carries the four headers.
