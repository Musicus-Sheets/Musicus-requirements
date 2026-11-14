---
id: R-ACC-011
level: 3
title: Login through an identity provider
priority: could
status: proposed
links:
  refines: [F-ACC-001]
---

# R-ACC-011 Login through an identity provider

## Statement

The system shall allow users to log in through an external OpenID Connect provider (e.g. Keycloak, Authentik, Google) configured by the operator.

## Acceptance criteria

- With a provider configured, a user can log in without a Musicus password and gets the same session as with a password login.

## Notes

For ensembles that already run an identity provider. Candidate crate: `openidconnect`. Group membership could later be mapped from provider claims.
