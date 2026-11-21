---
id: R-OPS-041
level: 3
title: Patch releases write no new kinds of stored values
priority: must
status: accepted
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-018]
  constrains: [R-OPS-014]
  decided_in: [tech:d-update-model]
---

# R-OPS-041 Patch releases write no new kinds of stored values

## Statement

A patch release shall not store kinds of values that an earlier release of the same minor cannot read, even without a change of the database structure.

## Acceptance criteria

- Data written by the newest patch of a minor (test data covering roles, system layout region kinds, ink format versions and error codes stored in import problems) is read without error by the first release of that minor (upgrade/downgrade test matrix).
- Every stored enumeration read from the database has a fallback for unknown values (as `ErrorCode` has), so a value from a newer release is shown as unknown instead of failing the request.
- The release checklist contains the line "patch: no new stored values".

## Notes

R-OPS-018 forbids database updates in patches; the database check (R-OPS-038, R-OPS-040) cannot see new values written into existing columns (a new role, a new region kind, a new ink format version, a new error code in `import_files.problem`). This requirement closes that gap; the fallbacks are part of phase 0.
