#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Checks the Musicus requirements and generates index.md and requirements.json.

Usage:
    uv run tools/validate.py            # check and regenerate the overview
    uv run tools/validate.py --check    # check only; exit 1 if the overview is outdated
    uv run tools/validate.py --code-root PATH   # main repository (default: ../..)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIRS = {1: "goals", 2: "features", 3: "requirements"}
PREFIX = {"G": 1, "F": 2, "R": 3}
LEVEL_NAME = {1: "Goal", 2: "Feature", 3: "Requirement"}
ID_RE = re.compile(r"^(G-\d{3}|[FR]-[A-Z][A-Z0-9]*-\d{3})$")
STATUSES = ["proposed", "accepted", "implemented", "verified", "deprecated"]
PRIORITIES = ["must", "should", "could"]
REQ_LINKS = ["refines", "depends_on", "constrains", "conflicts_with"]
EXT_LINKS = ["verified_by", "implemented_by", "decided_in"]
REVERSE = {
    "refines": "refined_by",
    "depends_on": "required_by",
    "constrains": "constrained_by",
    "conflicts_with": "conflicts_with",
}
AREAS = {
    "ACC": "Accounts, login, sessions, roles",
    "ACL": "Access to sheets",
    "LIB": "Library",
    "FILE": "Sheet files",
    "PROG": "Concert programmes",
    "READ": "Reader",
    "ANN": "Annotations",
    "SEC": "Security and privacy",
    "PERF": "Performance and resources",
    "OPS": "Installation and operation",
    "OFF": "Offline app",
    "TECH": "Technology constraints",
    "I18N": "Languages and localisation",
}


@dataclass
class Link:
    target: str
    note: str | None = None


@dataclass
class Item:
    id: str
    level: int
    title: str
    priority: str
    status: str
    path: Path
    links: dict[str, list[Link]] = field(default_factory=dict)
    sections: dict[str, str] = field(default_factory=dict)
    incoming: dict[str, list[Link]] = field(default_factory=dict)

    @property
    def area(self) -> str | None:
        parts = self.id.split("-")
        return parts[1] if len(parts) == 3 else None

    @property
    def statement(self) -> str:
        return " ".join(self.sections.get("Statement", "").split())


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def parse_links(raw: object, where: str, report: Report) -> dict[str, list[Link]]:
    links: dict[str, list[Link]] = {}
    if raw is None:
        return links
    if not isinstance(raw, dict):
        report.error(where, "`links` must be a mapping")
        return links
    for kind, targets in raw.items():
        if kind not in REQ_LINKS + EXT_LINKS:
            report.error(where, f"unknown link type `{kind}` (allowed: {', '.join(REQ_LINKS + EXT_LINKS)})")
            continue
        if targets is None:
            continue
        if not isinstance(targets, list):
            report.error(where, f"`{kind}` must be a list")
            continue
        parsed = []
        for t in targets:
            if isinstance(t, str):
                parsed.append(Link(t))
            elif isinstance(t, dict) and isinstance(t.get("id"), str):
                parsed.append(Link(t["id"], t.get("note")))
            else:
                report.error(where, f"`{kind}` entries must be an ID/path or {{id, note}}")
        links[kind] = parsed
    return links


def parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current = None
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            current = m.group(1)
            sections[current] = ""
        elif current:
            sections[current] += line + "\n"
    return {k: v.strip() for k, v in sections.items()}


def load(report: Report) -> dict[str, Item]:
    items: dict[str, Item] = {}
    for level, dirname in DIRS.items():
        for path in sorted((ROOT / dirname).rglob("*.md")):
            rel = path.relative_to(ROOT)
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
            if not m:
                report.error(str(rel), "missing YAML block between `---` lines")
                continue
            try:
                meta = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError as e:
                report.error(str(rel), f"invalid YAML: {e}")
                continue
            iid = str(meta.get("id", ""))
            where = f"{rel}"
            if not ID_RE.match(iid):
                report.error(where, f"invalid id `{iid}`")
                continue
            if path.stem != iid:
                report.error(where, f"file name must be `{iid}.md`")
            if PREFIX[iid[0]] != level:
                report.error(where, f"`{iid}` belongs in `{DIRS[PREFIX[iid[0]]]}/`")
            if meta.get("level") != PREFIX[iid[0]]:
                report.error(where, f"`level` must be {PREFIX[iid[0]]} for `{iid}`")
            if level == 3 and path.parent.name != iid.split("-")[1].lower():
                report.error(where, f"must be in `requirements/{iid.split('-')[1].lower()}/`")
            area = iid.split("-")[1] if iid[0] != "G" else None
            if area and area not in AREAS:
                report.error(where, f"unknown area `{area}`")
            status, priority = meta.get("status"), meta.get("priority")
            if status not in STATUSES:
                report.error(where, f"`status` must be one of {STATUSES}")
            if priority not in PRIORITIES:
                report.error(where, f"`priority` must be one of {PRIORITIES}")
            if not meta.get("title"):
                report.error(where, "`title` is missing")
            unknown = set(meta) - {"id", "level", "title", "priority", "status", "links"}
            if unknown:
                report.error(where, f"unknown fields: {', '.join(sorted(unknown))}")
            item = Item(
                id=iid,
                level=PREFIX[iid[0]],
                title=str(meta.get("title", "")),
                priority=str(priority),
                status=str(status),
                path=rel,
                links=parse_links(meta.get("links"), where, report),
                sections=parse_sections(m.group(2)),
            )
            heading = re.search(r"^#\s+(.+)$", m.group(2), re.M)
            if not heading or heading.group(1).strip() != f"{iid} {item.title}":
                report.error(where, f"first heading must be `# {iid} {item.title}`")
            required = ["Statement"] + (["Rationale"] if level < 3 else ["Acceptance criteria"])
            for s in required:
                if not item.sections.get(s):
                    report.error(where, f"section `## {s}` is missing or empty")
            if iid in items:
                report.error(where, f"duplicate id `{iid}` (also {items[iid].path})")
            items[iid] = item
    return items


def check_links(items: dict[str, Item], code_root: Path | None, report: Report) -> None:
    tech_labels: set[str] | None = None
    if code_root:
        chapters = code_root / "docs" / "technical" / "chapters"
        if chapters.is_dir():
            tech_labels = set()
            for f in chapters.glob("*.typ"):
                tech_labels |= set(re.findall(r"<([A-Za-z0-9_-]+)>", f.read_text(encoding="utf-8")))

    for item in items.values():
        where = str(item.path)
        refines = item.links.get("refines", [])
        if item.level > 1 and not refines:
            report.error(where, "levels 2 and 3 must `refine` an item one level up")
        if item.level == 1 and refines:
            report.error(where, "goals cannot refine anything")
        for kind in REQ_LINKS:
            for link in item.links.get(kind, []):
                target = items.get(link.target)
                if target is None:
                    report.error(where, f"`{kind}` target `{link.target}` does not exist")
                    continue
                if link.target == item.id:
                    report.error(where, f"`{kind}` points to itself")
                if kind == "refines" and target.level != item.level - 1:
                    report.error(where, f"`refines {link.target}`: target must be level {item.level - 1}")
                if kind == "conflicts_with" and not link.note:
                    report.error(where, f"`conflicts_with {link.target}` needs a `note` with the resolution")
                if target.status == "deprecated" and item.status != "deprecated":
                    report.warn(where, f"links to deprecated `{link.target}`")
                target.incoming.setdefault(REVERSE[kind], []).append(Link(item.id, link.note))

        for kind in ("verified_by", "implemented_by"):
            for link in item.links.get(kind, []):
                path, _, test = link.target.partition("::")
                if code_root is None:
                    continue
                full = code_root / path
                if not full.exists():
                    report.error(where, f"`{kind}` path `{path}` does not exist in {code_root}")
                elif test and test not in full.read_text(encoding="utf-8"):
                    report.error(where, f"`{kind}` test `{test}` not found in `{path}`")
        for link in item.links.get("decided_in", []):
            if not link.target.startswith("tech:"):
                report.error(where, f"`decided_in` must look like `tech:<label>`, got `{link.target}`")
            elif tech_labels is not None and link.target[5:] not in tech_labels:
                report.error(where, f"`decided_in` label `{link.target[5:]}` not found in the technical documentation")

        if item.level == 3 and item.status == "verified" and not item.links.get("verified_by"):
            report.error(where, "status `verified` needs `verified_by`")
        if item.level == 3 and item.status in ("implemented", "verified") and not item.links.get("implemented_by"):
            report.warn(where, f"status `{item.status}` without `implemented_by`")

    for item in items.values():
        if item.level < 3 and item.status != "deprecated" and not item.incoming.get("refined_by"):
            report.warn(str(item.path), "nothing refines this item yet")

    # depends_on must be acyclic
    state: dict[str, int] = {}

    def visit(iid: str, stack: list[str]) -> None:
        state[iid] = 1
        for link in items[iid].links.get("depends_on", []):
            if link.target not in items:
                continue
            if state.get(link.target) == 1:
                cycle = stack[stack.index(link.target):] + [link.target] if link.target in stack else [iid, link.target]
                report.error(str(items[iid].path), f"`depends_on` cycle: {' -> '.join(cycle)}")
            elif state.get(link.target) is None:
                visit(link.target, stack + [link.target])
        state[iid] = 2

    for iid in items:
        if iid not in state:
            visit(iid, [iid])


# --- Generated overview -----------------------------------------------------

def md_link(item: Item) -> str:
    return f"[{item.id}]({item.path.as_posix()})"


def status_badge(item: Item) -> str:
    return f"`{item.status}`"


def render_index(items: dict[str, Item]) -> str:
    by_level = {lvl: sorted((i for i in items.values() if i.level == lvl), key=lambda i: i.id) for lvl in (1, 2, 3)}
    out = [
        "<!-- Generated by tools/validate.py. Do not edit by hand. -->",
        "",
        "# Musicus requirements – overview",
        "",
        "How to read and write requirements: see [README.md](README.md).",
        "",
        "## Summary",
        "",
        "| Level | " + " | ".join(STATUSES) + " | Total |",
        "| --- | " + " | ".join("---:" for _ in STATUSES) + " | ---: |",
    ]
    for lvl in (1, 2, 3):
        counts = [sum(1 for i in by_level[lvl] if i.status == s) for s in STATUSES]
        out.append(f"| {lvl} {LEVEL_NAME[lvl]}s | " + " | ".join(str(c) for c in counts) + f" | {len(by_level[lvl])} |")

    out += ["", "## Goals and features", "", "Solid arrows: `refines`. Dashed: `depends_on`, `constrains`, `conflicts_with` (between goals and features).", "", "```mermaid", "flowchart LR"]
    for i in by_level[1] + by_level[2]:
        out.append(f'  {i.id.replace("-", "_")}["{i.id}<br/>{i.title.replace(chr(34), "")}"]')
    for i in by_level[2]:
        for link in i.links.get("refines", []):
            out.append(f'  {i.id.replace("-", "_")} --> {link.target.replace("-", "_")}')
    for i in by_level[1] + by_level[2]:
        for kind in ("depends_on", "constrains", "conflicts_with"):
            for link in i.links.get(kind, []):
                if link.target in items and items[link.target].level < 3:
                    out.append(f'  {i.id.replace("-", "_")} -. {kind} .-> {link.target.replace("-", "_")}')
    out += ["```", "", "## Hierarchy", "", "Every goal with the features that refine it, and their requirements.", ""]

    def children(parent: Item) -> list[Item]:
        return sorted((items[l.target] for l in parent.incoming.get("refined_by", [])), key=lambda i: i.id)

    for goal in by_level[1]:
        out.append(f"### {goal.id} {goal.title} {status_badge(goal)}")
        out.append("")
        out.append(goal.statement)
        out.append("")
        for feat in children(goal):
            out.append(f"- {md_link(feat)} {feat.title} {status_badge(feat)}")
            for req in children(feat):
                out.append(f"  - {md_link(req)} {req.title} {status_badge(req)}")
        out.append("")

    out += ["## Requirements by area", ""]
    for area, name in AREAS.items():
        reqs = [i for i in by_level[3] if i.area == area]
        if not reqs:
            continue
        out += [f"### {area} – {name}", "", "| ID | Title | Priority | Status | Refines |", "| --- | --- | --- | --- | --- |"]
        for r in reqs:
            parents = ", ".join(l.target for l in r.links.get("refines", []))
            out.append(f"| {md_link(r)} | {r.title} | {r.priority} | {r.status} | {parents} |")
        out.append("")

    out += ["## Cross links", "", "All links other than `refines`.", "", "| From | Link | To | Note |", "| --- | --- | --- | --- |"]
    for i in sorted(items.values(), key=lambda i: i.id):
        for kind in ("depends_on", "constrains", "conflicts_with"):
            for link in i.links.get(kind, []):
                if link.target in items:
                    note = (link.note or "").replace("|", "\\|").replace("\n", " ")
                    out.append(f"| {md_link(i)} | {kind} | {md_link(items[link.target])} | {note} |")
    out.append("")
    return "\n".join(out)


def render_json(items: dict[str, Item]) -> str:
    data = []
    for i in sorted(items.values(), key=lambda i: i.id):
        data.append({
            "id": i.id,
            "level": i.level,
            "area": i.area,
            "title": i.title,
            "priority": i.priority,
            "status": i.status,
            "path": i.path.as_posix(),
            "statement": i.statement,
            "links": {k: [{"target": l.target, **({"note": l.note} if l.note else {})} for l in v] for k, v in i.links.items() if v},
            "incoming": {k: [{"source": l.target, **({"note": l.note} if l.note else {})} for l in v] for k, v in sorted(i.incoming.items())},
        })
    return json.dumps({"generated_by": "tools/validate.py", "items": data}, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="do not write files; fail if they are outdated")
    parser.add_argument("--code-root", type=Path, default=ROOT.parent.parent, help="main repository (default: ../..)")
    args = parser.parse_args()

    code_root = args.code_root.resolve()
    if not (code_root / "Cargo.toml").exists():
        print(f"note: main repository not found at {code_root}; skipping path and label checks")
        code_root = None

    report = Report()
    items = load(report)
    check_links(items, code_root, report)

    for w in report.warnings:
        print(f"warning: {w}")
    for e in report.errors:
        print(f"error: {e}")
    if report.errors:
        print(f"\n{len(report.errors)} error(s)")
        return 1

    outputs = {ROOT / "index.md": render_index(items), ROOT / "requirements.json": render_json(items)}
    stale = [p.name for p, content in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
    if args.check:
        if stale:
            print(f"outdated: {', '.join(stale)} (run tools/validate.py without --check)")
            return 1
    else:
        for p, content in outputs.items():
            p.write_text(content, encoding="utf-8")
    print(f"ok: {len(items)} items, {len(report.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
