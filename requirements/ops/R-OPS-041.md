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
  implemented_by:
    - crates/musicus-api/src/dto.rs
    - crates/musicus-api/src/layout.rs
    - crates/musicus-api/src/import/review.rs
    - crates/musicus-server/src/auth.rs
    - crates/musicus-server/src/routes/auth.rs
    - crates/musicus-server/src/routes/users.rs
    - crates/musicus-server/src/routes/files.rs
    - crates/musicus-server/src/routes/import.rs
    - crates/musicus-web/src/pages/viewer.rs
    - crates/musicus-web/src/pages/layout_edit.rs
    - crates/musicus-web/src/pages/users.rs
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

State: the second criterion (fallbacks) and the checklist line are done. Inventory of stored values and their fallbacks: `docs/agents/data-model.md` § Stored values (decision a-stored-fallbacks): unknown role ⇒ no login; unknown band kind ⇒ page shown whole; unknown ink format ⇒ page shown without the annotations and locked; unknown import states ⇒ left out; unknown error codes ⇒ `unknown`; nothing read through a fallback is written back. Tested with rows written directly into the database (`crates/musicus-server/tests/api.rs`: `an_unknown_role_cannot_log_in_and_is_never_written_back`, `layouts_of_a_newer_release_show_whole_pages_and_are_not_overwritten`, `annotation_pages_of_a_newer_format_are_served_unchanged`, `import_items_and_files_of_a_newer_release_are_left_out`). The first criterion (test data of real releases in the upgrade/downgrade matrix) is still open, so the status stays `accepted`.
