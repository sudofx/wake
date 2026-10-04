import pathlib
import unittest


class SudofxKillSwitchWorkflowTest(unittest.TestCase):
    def test_global_kill_switch_precedes_provider_cycle(self):
        workflow = pathlib.Path(".github/workflows/wake.yml").read_text(encoding="utf-8")

        guard = "Enforce sudofx global application access"
        provider = "Run one governed research cycle"

        self.assertIn(guard, workflow)
        self.assertIn("SUDOFX_EXTERNAL_ACCESS_DISABLED", workflow)
        self.assertIn(provider, workflow)
        self.assertLess(
            workflow.index(guard),
            workflow.index(provider),
            "sudofx global kill switch must be enforced before any WAKE provider cycle",
        )


if __name__ == "__main__":
    unittest.main()
