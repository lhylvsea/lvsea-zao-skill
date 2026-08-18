from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from context_sizer import measure  # noqa: E402
from runtime import run  # noqa: E402
from trigger_eval import evaluate  # noqa: E402
from validate_skill import validate  # noqa: E402


class PackageContractTests(unittest.TestCase):
    def test_package_contract(self) -> None:
        result = validate(ROOT)
        self.assertTrue(result["ok"], result)

    def test_trigger_regression(self) -> None:
        result = evaluate(ROOT, ROOT / "evals/trigger_cases.json")
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["summary"]["passed"], result["summary"]["total"])

    def test_context_budget(self) -> None:
        result = measure(ROOT)
        self.assertNotEqual(result["status"], "block")

    def test_windows_command_resolution(self) -> None:
        result = run(["python", "--version"], ROOT)
        self.assertTrue(result["ok"], result)


if __name__ == "__main__":
    unittest.main()
