import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/deploy-book.yml"


class BranchSelectionTest(unittest.TestCase):
    def select_branches(self, include, exclude):
        workflow = WORKFLOW.read_text()
        step = workflow.split("    - id: set-branches\n", 1)[1]
        script = textwrap.dedent(step.split("      run: |\n", 1)[1].split("\n    - name:", 1)[0])

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            git = path / "git"
            git.write_text("#!/bin/sh\nprintf '  origin/2025\\n  origin/2026\\n'\n")
            git.chmod(0o755)
            output = path / "output"
            env = {
                **os.environ,
                "PATH": f"{path}{os.pathsep}{os.environ['PATH']}",
                "BRANCHES_TO_DEPLOY": include,
                "BRANCHES_NOT_TO_DEPLOY": exclude,
                "GITHUB_OUTPUT": str(output),
            }
            subprocess.run(["bash", "-eo", "pipefail", "-c", script], cwd=path, env=env, check=True)
            lines = output.read_text().splitlines()
            self.assertEqual(len(lines), 1)
            self.assertTrue(lines[0].startswith("branches="))
            return json.loads(lines[0].removeprefix("branches="))

    def test_multiple_branches_are_written_on_one_line(self):
        self.assertEqual(self.select_branches("*", ""), ["2025", "2026"])

    def test_exclusions_apply_to_all_and_selected_branches(self):
        self.assertEqual(self.select_branches("*", "2026"), ["2025"])
        self.assertEqual(self.select_branches("2025 2026", "2026"), ["2025"])

    def test_excluding_all_branches_produces_an_empty_array(self):
        self.assertEqual(self.select_branches("*", "2025 2026"), [])


if __name__ == "__main__":
    unittest.main()
