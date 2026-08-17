#!/usr/bin/env python3
"""Create a topic directory from the bundled Bun-style document shell."""

from __future__ import annotations

import argparse
import os
from datetime import date
from html import escape
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "docs-shell"
COMPONENT_SOURCE = SKILL_ROOT / "assets" / "document-home.js"
FILES = ("index.html", "styles.css", "app.js")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="New topic directory")
    parser.add_argument(
        "--title",
        required=True,
        help="Novice-facing reader question or familiar problem; avoid internal terminology",
    )
    parser.add_argument(
        "--summary",
        required=True,
        help="Plain-language symptom, cause, and core idea without source symbols",
    )
    parser.add_argument("--label", default="TECHNICAL DOCUMENT", help="Compact header label")
    parser.add_argument("--root", type=Path, help="Optional documentation root boundary")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.expanduser().resolve()
    root = output.parents[1]

    if args.root:
        root = args.root.expanduser().resolve()
        if root not in output.parents:
            raise SystemExit(f"output must be a topic subdirectory below {root}")

    conflicts = [name for name in FILES if (output / name).exists()]
    if conflicts:
        raise SystemExit(f"refusing to overwrite existing files: {', '.join(conflicts)}")

    missing = [name for name in FILES if not (TEMPLATE_ROOT / name).is_file()]
    if not COMPONENT_SOURCE.is_file():
        missing.append("document-home.js")
    if missing:
        raise SystemExit(f"skill assets are incomplete: {', '.join(missing)}")

    output.mkdir(parents=True, exist_ok=True)
    component_target = root / "assets" / "document-home.js"
    component_target.parent.mkdir(parents=True, exist_ok=True)
    if not component_target.exists():
        component_target.write_text(COMPONENT_SOURCE.read_text(encoding="utf-8"), encoding="utf-8")

    replacements = {
        "__DOC_TITLE__": escape(args.title, quote=True),
        "__DOC_SUMMARY__": escape(args.summary, quote=True),
        "__DOC_LABEL__": escape(args.label, quote=True),
        "__DOC_DATE__": date.today().isoformat(),
        "__DOC_HOME_COMPONENT__": Path(os.path.relpath(component_target, output)).as_posix(),
    }

    for name in FILES:
        content = (TEMPLATE_ROOT / name).read_text(encoding="utf-8")
        if name == "index.html":
            for token, value in replacements.items():
                content = content.replace(token, value)
        (output / name).write_text(content, encoding="utf-8")

    print(output / "index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
