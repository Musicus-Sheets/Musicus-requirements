---
id: R-ACL-007
level: 3
title: Several ensembles on one server
priority: could
status: proposed
links:
  refines: [F-ACL-001]
---

# R-ACL-007 Several ensembles on one server

## Statement

The system shall allow one server to host several independent ensembles, each with its own users, groups, instruments, library and programmes that the other ensembles cannot see.

## Acceptance criteria

- Members of ensemble A never see scores, groups or users of ensemble B.

## Notes

Open question whether this is needed (e.g. a music school, or an association with a youth band). Implementation idea: an `ensemble_id` on groups, scores, instruments and programmes, scoping every query. Cheap to add early, expensive to retrofit; not added in version 0.1.
