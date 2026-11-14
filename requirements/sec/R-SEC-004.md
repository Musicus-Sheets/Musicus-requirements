---
id: R-SEC-004
level: 3
title: Cross-site request forgery
priority: must
status: verified
links:
  refines: [F-SEC-002]
  verified_by: [crates/musicus-server/tests/api.rs::login_sessions_and_csrf]
  implemented_by: [crates/musicus-server/src/auth.rs, crates/musicus-web/src/api.rs]
  decided_in: [tech:d-csrf]
---

# R-SEC-004 Cross-site request forgery

## Statement

The system shall send the session cookie only as HttpOnly, SameSite=Lax and (by default) Secure, and shall reject state-changing requests authenticated by cookie that lack the header x-musicus-csrf (HTTP 403).

## Acceptance criteria

- A POST with session cookie but without the header returns 403; with the header it succeeds.
