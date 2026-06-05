from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.audit_template_agents import audit


def write(path: Path, contents: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents, encoding="utf-8")


def create_complete_template(root: Path) -> None:
    write(root / "AGENTS.md", "Project guidance\n")
    write(root / ".gitignore", "*.personal*\n*.personal/\n*.secret*\n*.secret/\n")
    write(root / ".agents" / "AGENTS.md")
    write(root / ".agents" / "skills" / "real-workflow" / "SKILL.md")
    write(root / "!docs.ai" / "AGENTS.md")
    write(root / "!docs.ai" / "lessons" / "AGENTS.md")
    write(root / "!docs.ai" / "lessons" / "lesson-template.md")
    write(root / "!docs.ai" / "rules" / "AGENTS.md")
    write(root / "!docs.ai" / "rules" / "personal-ai-assets.md")
    write(root / "!docs.ai" / "rules" / "sensitive-file-access.md")


class AuditTemplateAgentsTests(unittest.TestCase):
    def test_complete_project_has_no_findings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            create_complete_template(root)

            self.assertEqual(audit(root), [])

    def test_template_placeholders_can_be_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            create_complete_template(root)
            write(root / "AGENTS.md", "Replace this section\nexample-workflow\n")
            (root / ".agents" / "skills" / "real-workflow" / "SKILL.md").unlink()
            write(root / ".agents" / "skills" / "example-workflow" / "SKILL.md")

            normal = audit(root)
            allowed = audit(root, allow_template_placeholders=True)

            self.assertGreater(len(normal), 0)
            self.assertEqual(allowed, [])

    def test_reports_misplaced_guidance_and_missing_ignore_patterns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            create_complete_template(root)
            write(root / "docs.ai" / "AGENTS.md")
            write(root / ".gitignore", "*.personal*\n")

            findings = audit(root)
            messages = [finding.message for finding in findings]

            self.assertTrue(any("consider `!docs.ai`" in message for message in messages))
            self.assertTrue(any("*.secret*" in message for message in messages))


if __name__ == "__main__":
    unittest.main()
