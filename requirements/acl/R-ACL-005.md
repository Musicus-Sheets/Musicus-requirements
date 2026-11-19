---
id: R-ACL-005
level: 3
title: Grants per voice
priority: could
status: proposed
links:
  refines: [F-ACL-003]
  depends_on: [R-LIB-002, R-LIB-010]
---

# R-ACL-005 Grants per voice

## Statement

The system shall allow granting an instrument to a group for selected voices only (e.g. Trumpet voice 1), using the voices stored with each part (R-LIB-002): a part is readable through such a grant when it contains at least one of the granted voices.

## Acceptance criteria

- A group granted 'Trumpet, voice 1' reads '1st Trumpet' but not '2nd Trumpet'.
- A group granted 'Klarinette, voice 2' reads "Klarinette 2" and "Klarinette 1 & 2" but not "Klarinette 1".

## Notes

Prepared, not implemented: since migration 0005 the voices of a part are stored as rows of their own (`part_voices`, indexed by voice), so the access check can later join them like the instruments of a part.
