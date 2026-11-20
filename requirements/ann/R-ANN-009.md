---
id: R-ANN-009
level: 3
title: Choosing the set when reading
priority: must
status: verified
links:
  refines: [F-ANN-002]
  depends_on: [R-ANN-008]
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/viewer.rs, crates/musicus-web/src/names.rs, crates/musicus-server/src/routes/annotations.rs]
---

# R-ANN-009 Choosing the set when reading

## Statement

When the reader opens, the web client shall show the set linked to the current programme, else the default set; when a member draws without any set, it shall create one named after the programme, or an unnamed one shown as 'My annotations' in the user interface language (R-I18N-006); members can switch sets or hide all markings.

## Acceptance criteria

- Opening the march from the Christmas programme shows the set linked to it.
- The first stroke on a part without sets creates a set.
