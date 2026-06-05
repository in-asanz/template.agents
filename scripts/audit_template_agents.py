from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


EXPECTED_PATHS = [
    "AGENTS.md",
    ".agents/AGENTS.md",
    ".agents/skills",
    "!docs.ai/AGENTS.md",
    "!docs.ai/lessons/AGENTS.md",
    "!docs.ai/lessons/lesson-template.md",
    "!docs.ai/rules/AGENTS.md",
    "!docs.ai/rules/personal-ai-assets.md",
    "!docs.ai/rules/sensitive-file-access.md",
]

PERSONAL_IGNORE_PATTERNS = [
    "*.personal*",
    "*.personal/",
    "*.secret*",
    "*.secret/",
]

PLACEHOLDER_MARKERS = [
    "Replace this section",
    "Replace this list",
    "replace or delete this placeholder",
    "example-workflow",
]

MISPLACED_CANDIDATES = {
    "docs.ai": "!docs.ai",
    "docs/ai": "!docs.ai",
    "rules": "!docs.ai/rules",
    "lessons": "!docs.ai/lessons",
    "skills": ".agents/skills",
    ".codex/skills": ".agents/skills",
    ".claude/skills": ".agents/skills",
}


@dataclass
class Finding:
    severity: str
    path: str
    message: str


def contains_secret_part(path: Path) -> bool:
    return any("secret" in part.lower() for part in path.parts)


def read_text_safely(path: Path) -> str:
    if contains_secret_part(path):
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def audit(target: Path, *, allow_template_placeholders: bool = False) -> list[Finding]:
    findings: list[Finding] = []

    if not target.exists():
        return [Finding("error", str(target), "Target path does not exist.")]
    if not target.is_dir():
        return [Finding("error", str(target), "Target path is not a directory.")]

    for relative_path in EXPECTED_PATHS:
        candidate = target / relative_path
        if not candidate.exists():
            findings.append(
                Finding("missing", relative_path, "Expected template.agents path is absent.")
            )

    gitignore = target / ".gitignore"
    gitignore_text = read_text_safely(gitignore) if gitignore.exists() else ""
    for pattern in PERSONAL_IGNORE_PATTERNS:
        if pattern not in gitignore_text:
            findings.append(
                Finding("warning", ".gitignore", f"Missing ignore pattern `{pattern}`.")
            )

    for relative_path, destination in MISPLACED_CANDIDATES.items():
        candidate = target / relative_path
        if candidate.exists() and not contains_secret_part(candidate):
            findings.append(
                Finding(
                    "warning",
                    relative_path,
                    f"Potential misplaced AI guidance; consider `{destination}`.",
                )
            )

    agents_md = target / "AGENTS.md"
    if agents_md.exists():
        contents = read_text_safely(agents_md)
        if not allow_template_placeholders:
            for marker in PLACEHOLDER_MARKERS:
                if marker.lower() in contents.lower():
                    findings.append(
                        Finding("warning", "AGENTS.md", f"Placeholder content remains: `{marker}`.")
                    )
    else:
        findings.append(Finding("warning", "AGENTS.md", "Root agent guidance is missing."))

    skills_root = target / ".agents" / "skills"
    if skills_root.is_dir():
        skill_files = [
            path
            for path in skills_root.glob("*/SKILL.md")
            if not contains_secret_part(path.relative_to(target))
        ]
        if not skill_files:
            findings.append(
                Finding("warning", ".agents/skills", "No directly activatable skills found.")
            )
        elif (
            not allow_template_placeholders
            and all(path.parent.name == "example-workflow" for path in skill_files)
        ):
            findings.append(
                Finding(
                    "warning",
                    ".agents/skills/example-workflow",
                    "Only the placeholder skill is present.",
                )
            )

    return findings


def print_text(findings: list[Finding]) -> None:
    if not findings:
        print("No template.agents findings.")
        return
    for finding in findings:
        print(f"[{finding.severity}] {finding.path}: {finding.message}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit template.agents repository structure.")
    parser.add_argument("--target", default=".", help="Project root to audit.")
    parser.add_argument("--json", action="store_true", help="Emit JSON findings.")
    parser.add_argument(
        "--allow-template-placeholders",
        action="store_true",
        help="Allow the canonical template repository to keep placeholder guidance.",
    )
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    findings = audit(target, allow_template_placeholders=args.allow_template_placeholders)
    if args.json:
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    else:
        print_text(findings)


if __name__ == "__main__":
    main()
