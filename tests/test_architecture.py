from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ArchitectureSeparationTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding='utf-8')

    def test_cycle_lane_has_no_pages_work(self):
        workflow = self.read('.github/workflows/wake.yml')
        self.assertNotIn('deploy-pages', workflow)
        self.assertNotIn('upload-pages-artifact', workflow)
        self.assertNotIn('pages.yml', workflow)
        self.assertIn('group: wake-authority', workflow)
        self.assertIn('timeout-minutes: 30', workflow)

    def test_completed_wake_is_not_recheckpointed_before_live_projection(self):
        cloud = self.read('scripts/github_wake.py')
        self.assertIn('result_checkpointed = True', cloud)
        self.assertIn('if not result_checkpointed:', cloud)

    def test_pages_lane_has_no_model_execution(self):
        workflow = self.read('.github/workflows/pages.yml')
        self.assertNotIn('GEMINI_API_KEY', workflow)
        self.assertNotIn('Continue independent research', workflow)
        self.assertIn('group: wake-pages', workflow)

    def test_pages_triggers_only_from_site_paths(self):
        workflow = self.read('.github/workflows/pages.yml')
        for path in ('wake/assets/**','wake/report.py','wake/provenance.py','wake/rejected.py','wake/feeds.py'):
            self.assertIn(path, workflow)
        self.assertNotIn('wake.toml', workflow)
        self.assertNotIn('research-topics.toml', workflow)

    def test_live_projection_is_non_authoritative_and_outside_pages(self):
        cloud = self.read('scripts/github_wake.py')
        live = self.read('wake/live.py')
        self.assertIn('wake-live', cloud)
        self.assertIn('"authoritative": False', live)
        self.assertIn('"authority": "SQLite"', live)
        self.assertNotIn('site/live.json', cloud)

    def test_browser_polls_live_projection_without_reload(self):
        page = self.read('wake/assets/index.html')
        app = self.read('wake/assets/app.js')
        self.assertIn('wake-live/live.json', page)
        self.assertIn('window.WakeApplyLive?.(next)', page)
        self.assertNotIn('location.replace(url.toString())', page)
        self.assertIn('window.WakeApplyLive = next =>', app)

    def test_runtime_pin_survives_start_and_successor_dispatch(self):
        start = self.read('.github/workflows/operator-start.yml')
        runner = self.read('.github/workflows/wake-runner.yml')
        cycle = self.read('.github/workflows/wake.yml')
        self.assertIn('git/ref/heads/wake-runtime', start)
        self.assertIn('-f "runtime_ref=$runtime_ref"', start)
        self.assertNotIn('gh workflow run wake.yml', runner)
        self.assertIn('ref: ${{ inputs.runtime_ref || github.sha }}', cycle)
        self.assertIn('--ref wake-runtime', cycle)
        self.assertIn('runtime_ref=$RUNTIME_REF', cycle)

    def test_wake_zero_topics_are_the_operator_selected_ten(self):
        topics = self.read('research-topics.toml')
        self.assertEqual(topics.count('[[topics]]'), 10)
        for seed in (
            'What Is an Observer?',
            "How Do We Know We're Wrong?",
            'What Makes You You?',
            'Why Does Music Feel Like Something?',
            'Why Are Things Funny?',
            'How Does Information Survive?',
            'When Does Simple Become Smart?',
            'Can Two Honest Observers Disagree?',
            'What Actually Matters to Us?',
            'Can Curiosity Be Built?',
        ):
            self.assertIn(seed, topics)

    def test_bob_is_eli25_scientific_interpreter_without_a_quota(self):
        provider = self.read('wake/providers.py')
        self.assertIn('ELI25 audience', provider)
        self.assertIn('scientific method', provider)
        self.assertIn('No quota and no filler', provider)
        self.assertIn('what remains unknown', provider)

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

    def test_reset_auto_promotes_master_only_when_runtime_differs(self):
        reset = self.read('.github/workflows/operator-reset.yml')
        self.assertIn('Check whether runtime promotion is needed', reset)
        self.assertIn('master_sha="$(git rev-parse HEAD)"', reset)
        self.assertIn('runtime_sha="$(gh api "repos/$GITHUB_REPOSITORY/git/ref/heads/wake-runtime"', reset)
        self.assertIn("if: steps.promotion.outputs.needed == 'true'", reset)
        self.assertIn('python -m unittest discover -s tests -v', reset)
        self.assertIn('python -m wake --data /tmp/wake-reset-promote experiment --cycles 100', reset)
        self.assertIn('Promote verified master only when needed', reset)
        self.assertIn('-f "runtime_ref=$runtime_ref"', reset)
        self.assertLess(
            reset.index('Promote verified master only when needed'),
            reset.index('Dispatch the governed archive-first reset'),
        )

    def test_state_branch_current_tree_contract_is_sqlite_only(self):
        cloud = self.read('scripts/github_wake.py')
        self.assertIn('data/wake.sqlite3', cloud)
        self.assertIn('events.jsonl', cloud)
        self.assertIn('operation.json', cloud)
        self.assertIn('git("rm", "-r", "--ignore-unmatch"', cloud)
        self.assertNotIn('branch.checkout/"operation.json"', cloud)

    def test_metrics_use_full_history_aggregates_not_event_tail(self):
        live = self.read('wake/live.py')
        app = self.read('wake/assets/app.js')
        self.assertIn('_full_history_metrics', live)
        self.assertIn('store.history_metrics()', live)
        self.assertNotIn('store.db.execute', live)
        self.assertIn('"metrics": _full_history_metrics(store, state)', live)
        self.assertIn('fullMetrics.accepted_actions', app)
        self.assertIn('fullMetrics.rejection_reasons', app)
        self.assertIn('"metrics": _full_history_metrics(store, state)', self.read('wake/report.py'))
        self.assertIn("if(!data.metrics)", app)

    def test_site_operator_link_goes_directly_to_github_actions(self):
        page = self.read('wake/assets/index.html')
        self.assertIn('href="https://github.com/sudofx/wake/actions"', page)
        self.assertNotIn('WAKE_CONTROL_URL', page)
        self.assertNotIn('control.js', page)
        self.assertFalse((ROOT / 'control-worker').exists())

if __name__ == '__main__':
    unittest.main()
