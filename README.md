# Musicus – requirements

The requirements of [Musicus](https://github.com/NelDav/Musicus): what the
system must do and under which constraints. Written for humans and coding
agents alike. This repository is the submodule `docs/requirements` of the main
repository; the architecture is described next to it in `docs/technical`.

Start with the generated overview: **[index.md](index.md)**.

## Levels

| Level | Prefix | Name | Answers | Contains |
| --- | --- | --- | --- | --- |
| 1 | `G-` | Goal | *Why* the product exists, from a stakeholder's view | Outcomes; no technology; not directly testable |
| 2 | `F-` | Feature | *What* the system offers, as a user or operator sees it | Capabilities and quality targets, testable at system level |
| 3 | `R-` | Requirement | *Exactly how* it must behave | One precise, testable statement with acceptance criteria |

Quality requirements (performance, security, operation) are areas, not levels:
they appear as features and requirements like everything else.

## IDs

- Goals: `G-001`. Features: `F-<AREA>-001`. Requirements: `R-<AREA>-001`.
- The number is never reused, and the ID never changes, even if the item gets
  another parent. The hierarchy is expressed by links, not by the ID.
- The file name is the ID: `goals/G-001.md`, `features/F-PROG-002.md`,
  `requirements/prog/R-PROG-003.md`.

| Area | Topic |
| --- | --- |
| `ACC` | Accounts, login, sessions, roles |
| `ACL` | Access to sheets (groups, grants) |
| `LIB` | Library: scores, parts, metadata, search |
| `FILE` | Sheet files: upload, versions, delivery |
| `PROG` | Concert programmes |
| `READ` | The reader (displaying and turning pages) |
| `ANN` | Annotations |
| `SEC` | Security and privacy |
| `PERF` | Performance and resource use |
| `OPS` | Installation, operation, updates and platforms |
| `OFF` | Offline app (future) |
| `TECH` | Technology constraints |
| `I18N` | Languages and localisation (UI language, formats, error texts) |

## File format

One Markdown file per item. The YAML block at the top holds the metadata and
the links; the body holds the text.

```markdown
---
id: R-PROG-003
level: 3
title: Prefetch the sheets of an opened programme
priority: must
status: verified
links:
  refines: [F-PROG-002]
  depends_on: [R-ACL-001]
  conflicts_with:
    - id: R-SEC-001
      note: Sheets are kept in memory only; a reload downloads them again.
  verified_by: [e2e/smoke.mjs]
  implemented_by: [crates/musicus-web/src/pages/programmes.rs]
  decided_in: [tech:d-no-client-storage]
---

# R-PROG-003 Prefetch the sheets of an opened programme

## Statement

When a member opens a programme, the web client shall ...

## Rationale

Why this is needed.

## Acceptance criteria

- Observable, checkable conditions.

## Notes

Optional.
```

| Field | Values |
| --- | --- |
| `level` | `1`, `2`, `3` (must match the ID prefix) |
| `priority` | `must`, `should`, `could` |
| `status` | `proposed` (idea, not agreed) → `accepted` (agreed, not built) → `implemented` (built) → `verified` (covered by an automated test); or `deprecated` |
| Body sections | `Statement` always; `Rationale` for goals and features; `Acceptance criteria` for requirements; `Notes` optional |

Statements use the forms "The system shall ..." or "When ..., the ...
shall ...". One statement per requirement; split instead of using "and"
between unrelated behaviours.

## Links

Every link is stored once, in the item it starts from. The opposite direction
("refined by", "required by", ...) is computed into `index.md` and
`requirements.json`, so the two directions can never contradict each other.

### Between requirements

| Link | Meaning ("this item ...") | Rules |
| --- | --- | --- |
| `refines` | ... is part of, or a more precise version of, the target | Required for levels 2 and 3; target is exactly one level higher; one or more targets |
| `depends_on` | ... cannot be fulfilled without the target | Any level; no cycles |
| `constrains` | ... limits how the target may be fulfilled | Any level; typically a quality requirement constraining a functional one |
| `conflicts_with` | ... makes the target harder to fulfil; a trade-off was made | Any level; a `note` describing the resolution is required |

### To other places

| Link | Target | Example |
| --- | --- | --- |
| `verified_by` | Test file, optionally `::test_name`, relative to the main repository | `crates/musicus-server/tests/api.rs::members_only_reach_granted_parts` |
| `implemented_by` | File or directory in the main repository | `crates/musicus-server/src/access.rs` |
| `decided_in` | Decision record in the technical documentation, as `tech:<label>` | `tech:d-access` |

Never reference database update files (`crates/musicus-server/migrations/…`, except
`migrations/releases.txt`) in `verified_by` / `implemented_by`: previews are merged and deleted at
a release. Reference the code and tests instead, or the schema snapshot `crates/musicus-server/schema.sql`
once it exists. The validator rejects such paths.

A link target is either a plain ID / path, or an object with `id` and `note`
when the link needs an explanation. There is deliberately no generic
"relates to" link: every link must say what the connection means.

## Tools

`tools/validate.py` checks the catalogue and regenerates the overview:

```sh
uv run tools/validate.py            # check and regenerate index.md + requirements.json
uv run tools/validate.py --check    # check only; fails if index.md is outdated (pull-request check)
```

(Without `uv`: `pip install pyyaml` and run it with `python3`.)

It checks that IDs are unique and match file name and level, that every level
2 and 3 item refines an item one level up, that link targets exist, that
`depends_on` has no cycles, that every `conflicts_with` has a note, that the
required sections exist, and, when the main repository is next to this one
(`../..`), that `verified_by` / `implemented_by` paths and test names and
`decided_in` labels exist.

## Working rules

- Change the status in the same pull request as the code that implements or
  tests a requirement, and add `implemented_by` / `verified_by`.
- Do not delete requirements that were implemented; set `deprecated` and say
  why in `Notes`.
- After editing, run the validator and commit the regenerated `index.md` and
  `requirements.json`.
