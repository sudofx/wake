from pathlib import Path
import tomllib
import unittest

from support import TEST_RESEARCH_TOPICS

ROOT = Path(__file__).resolve().parents[1]

class ArchitectureSeparationTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding='utf-8')

    def test_legacy_import_is_explicit_migration_only(self):
        """Normal wake store construction must not expose legacy import as runtime mode."""
        source = self.read('wake/record_store.py')
        self.assertIn('def migrate_legacy(cls, directory, legacy_store)', source)
        constructor = source.split('def __init__', 1)[1].split('def migrate_legacy', 1)[0]
        self.assertNotIn('legacy_store=', constructor)
        authority = self.read('wake/authority.py')
        self.assertIn('RecordStore.migrate_legacy(data_directory, legacy)', authority)

    def test_live_runtime_does_not_depend_on_legacy_store_module(self):
        """Legacy SQLite persistence stays quarantined from normal runtime/domain code."""
        for path in (
            "wake/engine.py",
            "wake/report.py",
            "wake/provenance.py",
            "wake/trust.py",
            "wake/experimental.py",
            "wake/experiment.py",
            "wake/application.py",
            "wake/record_store.py",
            "wake/audit.py",
            "wake/__main__.py",
        ):
            self.assertNotIn("from .store import", self.read(path), path)

        authority = self.read("wake/authority.py")
        self.assertNotIn("from .store import Store", authority.split("def open_authoritative_store", 1)[0])
        self.assertIn("from .store import Store", authority)

        domain = self.read("wake/domain_events.py")
        self.assertNotIn("sqlite3", domain)
        self.assertNotIn("class Store", domain)
        self.assertIn("def reduce_event", domain)

    def test_retired_phase_labels_and_one_time_migration_tools_are_absent(self):
        retired = ("Phase" + " E", "phase" + "-e", "phase" + "_" + "e")
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or path.suffix not in {".py", ".md", ".yml", ".yaml", ".toml", ".js", ".html", ".css"}:
                continue
            content = path.read_text(encoding="utf-8")
            for label in retired:
                self.assertNotIn(label, content, str(path.relative_to(ROOT)))
            relative = str(path.relative_to(ROOT))
            for label in retired[1:]:
                self.assertNotIn(label, relative, relative)
        self.assertFalse((ROOT / ".github/workflows/operator-migrate-authority.yml").exists())
        self.assertFalse((ROOT / "scripts/github_migrate_authority.py").exists())

    def test_browser_polls_live_projection_without_reload(self):
        page = self.read('wake/assets/index.html')
        loader = self.read('wake/assets/reader-data.js')
        app = self.read('wake/assets/app.js')
        self.assertNotIn('raw.githubusercontent.com', page)
        self.assertIn('src="reader-data.js"', page)
        self.assertIn('window.WakeApplyLive?.(next)', loader)
        self.assertNotIn('location.replace(url.toString())', page)
        self.assertIn('window.WakeApplyLive = next =>', app)

    def test_wake_zero_topics_are_the_operator_selected_experiments(self):
        topics = self.read('research-topics.toml')
        configured = tomllib.loads(topics)['topics']
        from wake.research_expansion import ASSIGNMENTS
        self.assertEqual({topic['id'] for topic in configured},
                         {topic for group in ASSIGNMENTS.values() for topic in group})
        self.assertTrue(all(topic['enabled'] and topic['classification'] == 'experimental'
                            for topic in configured))

    def test_bob_is_plain_language_scientific_interpreter_without_a_quota(self):
        provider = self.read('wake/providers.py')
        prompts = self.read('wake/prompts.py')
        contract = provider + "\n" + prompts
        self.assertIn('Bob exists only inside a blog action', contract)
        self.assertIn('intelligent adult reader', contract)
        self.assertIn('scientific method', contract)
        self.assertIn('No quota and no filler', contract)
        self.assertIn('what remains unknown', contract)
        self.assertIn('"How to Win Friends and Influence People"', contract)
        self.assertIn('"Quantum Enigma"', contract)
        self.assertIn('strongest conflicting evidence', contract)
        self.assertIn('never repeat the first-post introduction', contract)
        self.assertIn('falsifier', contract)
        self.assertNotIn('ELI25 audience', contract)

    def test_research_page_keeps_revised_notebooks_ahead_of_research_notes(self):
        pet = self.read('wake/assets/pet.js')
        self.assertNotIn("const notebookShelf=books.length?", pet)
        research_default = pet[pet.index('else output=`<h2 class="shelf-title">The notebook shelf'):]
        self.assertLess(
            research_default.index("The notebook shelf"),
            research_default.index("Research notes"),
        )
        self.assertIn(
            "Object.values(s.notebooks||{}).sort((a,b)=>b.updated_version-a.updated_version)",
            pet,
        )

    def test_metrics_use_full_history_aggregates_not_event_tail(self):
        live = self.read('wake/live.py')
        app = self.read('wake/assets/app.js')
        self.assertIn('_full_history_metrics', live)
        self.assertIn('store.history_metrics()', live)
        self.assertNotIn('store.db.execute', live)
        self.assertIn('metrics = _full_history_metrics(store, state)', live)
        self.assertIn('fullMetrics.accepted_actions', app)
        self.assertIn('fullMetrics.rejection_reasons', app)
        self.assertIn('"metrics": _full_history_metrics(store, state, events)', self.read('wake/report.py'))
        self.assertIn("if(!data.metrics)", app)

if __name__ == '__main__':
    unittest.main()
