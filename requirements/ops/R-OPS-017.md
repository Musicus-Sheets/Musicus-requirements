---
id: R-OPS-017
level: 3
title: Going back never widens access
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-016]
  constrains: [R-ACL-001]
  decided_in: [tech:d-update-model]
---

# R-OPS-017 Going back never widens access

## Statement

When an installation is taken back to an older release, no user shall be able to read a part, file, programme or annotation that the newer release denied them; anything an older release cannot fully understand shall be invisible to it.

## Acceptance criteria

- Test for every release that adds a restriction of access (for example a grant with an expiry date, R-ACL-006): after the downgrade to every release inside the window, the restricted item gives no access at all (less access than in the newer release, never more).
- The restricted item is stored outside the structures the older release reads (for example the grant leaves the old grant table and lives in a new table with its expiry); the older release never sees it.
- After the next upgrade the item does not come back (R-OPS-016); librarians grant it again by hand.
- The downgrade window (R-OPS-014) is not shortened by the restriction.
- The release notes of a release that introduces a restriction say that a downgrade removes the restricted items and that they must be granted again.

## Notes

Fail closed: an older release ignores what it does not know, so a restriction it cannot read must take the restricted item away from it rather than leave it with its old, wider meaning. This replaces the earlier rule that a restriction could raise the oldest release allowed to start (user decision).
