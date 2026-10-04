from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ArchitectureSeparationTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding='utf-8')

    def test_legacy_import_is_explicit_migration_only(self):
        """Normal sudofx store construction must not expose legacy import as runtime mode."""
        source = self.read('wake/sudofx_store.py')
        self.assertIn('def migrate_legacy(cls, directory, legacy_store)', source)
        constructor = source.split('def __init__', 1)[1].split('def migrate_legacy', 1)[0]
        self.assertNotIn('legacy_store=', constructor)
        authority = self.read('wake/authority.py')
        self.assertIn('SudofxStore.migrate_legacy(data_directory, legacy)', authority)

    def test_live_runtime_does_not_depend_on_legacy_store_module(self):
        """Legacy SQLite persistence stays quarantined from normal runtime/domain code."""
        for path in (
            "wake/engine.py",
            "wake/report.py",
            "wake/provenance.py",
            "wake/trust.py",
            "wake/experimental.py",
            "wake/experiment.py",
            "wake/sudofx_application.py",
            "wake/sudofx_store.py",
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

    def test_phase_e_rehearsal_reads_compressed_authority_checkpoint(self):
        workflow = self.read('.github/workflows/phase-e-production-rehearsal.yml')
        self.assertIn('data/sudofx.sqlite.gz', workflow)
        self.assertIn('gzip -dc', workflow)
        self.assertIn('data/sudofx.sqlite', workflow)

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
        self.assertIn('"authority": "sudofx SQLite"', live)
        self.assertIn('"authority": "legacy WAKE SQLite"', live)
        self.assertNotIn('"authority": "SQLite"', live)
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
        report = self.read('wake/report.py')
        self.assertIn('performance = store.performance_snapshot()', report)
        self.assertIn('"metrics": _full_history_metrics(store, state, performance)', report)
        self.assertIn("if(!data.metrics)", app)

    def test_research_operations_console_is_derived_only(self):
        live = self.read('wake/live.py')
        app = self.read('wake/assets/app.js')
        self.assertIn('"authoritative": False', live)
        self.assertIn('"matrix_progress": _matrix_metrics(store)', live)
        self.assertIn('"application_observability": build_application_observability', live)
        self.assertIn('RESEARCH OPERATIONS', app)
        self.assertIn('DERIVED / LIVE', app)
        self.assertIn('TIME DILATION / EXPERIMENTAL REGIME', app)
        self.assertIn('RECENT INVOCATION TRACE', app)
        self.assertIn('GOVERNANCE PRESSURE', app)
        self.assertIn('PROVIDER QUOTA PRESSURE', app)
        self.assertNotIn('record_continuity_matrix_result(', app)
        self.assertNotIn('enable_continuity_matrix(', app)
        self.assertNotIn('set_time_dilation(', app)

    def test_operations_console_story_chapters_remain_evidence_scoped(self):
        app = self.read('wake/assets/app.js')
        for label in ("NOW", "PRESSURE", "MEMORY", "EVIDENCE", "BELIEF", "FRONTIER", "SPACE"):
            self.assertIn(label, app)
        for anchor in ("ops-now", "ops-pressure", "ops-context", "ops-evidence", "ops-beliefs", "ops-horizon", "ops-matrix"):
            self.assertIn(f'data-story-target="{anchor}"', app)
            self.assertEqual(app.count(f'id="{anchor}"'), 1)
        self.assertIn('href="#metrics" data-story-target=', app)
        self.assertNotIn('ops-story-rail', app)
        self.assertNotIn("what is true", app)

    def test_live_projection_keeps_receipt_telemetry_without_provider_bodies(self):
        live = self.read('wake/live.py')
        self.assertIn('"temporal", "context_delivery", "working_set_metrics", "runtime_performance"', live)
        self.assertNotIn('"request", "response"', live)

    def test_operations_console_declares_mobile_and_wide_screen_breakpoints(self):
        css = self.read('wake/assets/style.css')
        self.assertIn('@media(max-width:430px)', css)
        self.assertIn('@media(max-width:700px)', css)
        self.assertIn('@media(min-width:1600px)', css)
        self.assertIn('@media(min-width:2200px)', css)
        self.assertIn('.ops-tertiary-grid', css)
        self.assertIn('body.metrics-ops-active #metrics.view{width:100%;max-width:none', css)

    def test_external_visual_reference_names_never_enter_repository_text(self):
        blocked = ("de" + "los", "west" + "world")
        roots = (ROOT / "wake", ROOT / "docs", ROOT / "tests")
        suffixes = {".py", ".js", ".css", ".html", ".md", ".toml", ".yml", ".yaml"}
        offenders = []
        for root in roots:
            if not root.exists():
                continue
            for path in root.rglob("*"):
                if not path.is_file() or path.suffix.lower() not in suffixes:
                    continue
                text = path.read_text(errors="ignore").lower()
                if any(term in text for term in blocked):
                    offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual(offenders, [])

    def test_site_operator_link_goes_directly_to_github_actions(self):
        page = self.read('wake/assets/index.html')
        self.assertIn('href="https://github.com/sudofx/wake/actions"', page)
        self.assertNotIn('WAKE_CONTROL_URL', page)
        self.assertNotIn('control.js', page)
        self.assertFalse((ROOT / 'control-worker').exists())

if __name__ == '__main__':
    unittest.main()
