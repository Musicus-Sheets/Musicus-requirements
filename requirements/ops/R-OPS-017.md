---
id: R-OPS-017
level: 3
title: Going back never widens access
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  constrains: [R-ACL-001, R-OPS-014]
  decided_in: [tech:d-update-model]
---

# R-OPS-017 Going back never widens access

## Statement

When an installation is taken back to an older release, no user shall be able to read a part, file, programme or annotation that the newer release denied them.

## Acceptance criteria

- Test for every release that adds a restriction of access (for example grant expiry, R-ACL-006): a user denied by the restriction in release N is also denied after the downgrade to every release that may start.
- Each such change is classified as a removal in the release's database update (see the plan) and named in the release notes.

## Notes

An older release does not know a newer restriction and would ignore it. The newer release therefore either mirrors the restriction into the data the older release reads (for example removes an expired grant from the old grant table), or, where that is impossible, raises the oldest release allowed to start as soon as the restriction is used, which shortens the downgrade window (R-OPS-014). Interpretation of the user's rule "changes that restrict access always count as removals"; to confirm.
