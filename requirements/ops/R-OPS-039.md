---
id: R-OPS-039
level: 3
title: Notice for pull requests that change the database
priority: should
status: implemented
links:
  refines: [F-OPS-005]
  depends_on: [R-OPS-023]
  constrains: [R-OPS-018]
  implemented_by:
    - .github/workflows/database.yml
    - scripts/check-db-changes.py
  verified_by:
    - scripts/test_check_db_changes.py
---

# R-OPS-039 Notice for pull requests that change the database

## Statement

When a pull request adds a preview database update, the continuous integration shall mark it with the label `db-change` and a short note that the next release must be a minor release, without blocking the pull request.

## Acceptance criteria

- A pull request that adds a file under `migrations/preview/` gets the label `db-change` and a comment or job summary: "This PR changes the database; the next release must be a minor release (x.Y.0), not a patch."
- The notice never fails the pull request.
- A pull request without a new preview update gets no such label from the check.

## Notes

Informational; the blocking rule is R-OPS-040. Job `db-change` of the workflow `Database`: one comment, found again by a hidden marker and updated in place; label and comment are taken back when the pull request no longer adds a preview. Pull requests from forks get a read-only token and only the job summary.
