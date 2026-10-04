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
        self.assertIn('performance = store.performance_snapshot()', live)
        self.assertIn('"metrics": _full_history_metrics(store, state, performance)', live)
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
        ordered = ("ops-now", "ops-pressure", "ops-context", "ops-evidence", "ops-beliefs", "ops-horizon", "ops-matrix")
        positions = [app.index(f'id="{anchor}"') for anchor in ordered]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("WHAT THE RECORD SAYS NOW", app)
        self.assertIn("role:payload?.evidence_role||'source'", app)
        self.assertIn("!['discovery','metadata'].includes(item.role)", app)
        self.assertIn("<b>SPACE</b> where continuity has been tested", app)
        self.assertIn("<strong>${evidenceCount} records</strong>", app)
        self.assertIn("<strong>${matrixPct}% tested</strong>", app)
        self.assertIn("do not certify the truth of its research claims", app)
        self.assertIn("DEEP METRICS / VERIFY THE STORY", app)
        self.assertIn("the story can be checked rather than merely believed", app)
        self.assertNotIn("what is true", app)

    def test_longitudinal_story_uses_recorded_reflection_receipts(self):
        app = self.read('wake/assets/app.js')
        self.assertIn('LONGITUDINAL RECORD / DURABLE REFLECTIONS', app)
        self.assertIn('post?.reflection_cycle', app)
        self.assertIn("created%10===0", app)
        self.assertIn('Gaps remain gaps.', app)
        self.assertNotIn('inferred era', app.lower())

    def test_reflection_delta_story_uses_only_versioned_record_fields(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('SINCE LAST REFLECTION RECEIPT', app)
        self.assertIn('latestReflection?.post?.created_version', app)
        self.assertIn('item?.version', app)
        self.assertIn('item?.updated_version', app)
        self.assertIn('item?.created_version', app)
        self.assertIn('Versioned record deltas only.', app)
        self.assertIn('WAKE does not infer a comparison window.', app)
        self.assertIn('.ops-since-reflection', css)
        self.assertIn('.ops-since-grid', css)
        self.assertNotIn('12px.ops-since-reflection', css)
        self.assertNotIn('repeat(4,1fr).ops-since-grid', css)

    def test_live_projection_keeps_receipt_telemetry_without_provider_bodies(self):
        live = self.read('wake/live.py')
        self.assertIn('"temporal", "context_delivery", "working_set_metrics", "runtime_performance"', live)
        self.assertNotIn('"request", "response"', live)

    def test_metrics_show_context_continuity_without_inventing_handoffs(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('DURABLE CONTINUITY THREAD / RECENT INVOCATIONS', app)
        self.assertIn('observed record revision span', app)
        self.assertIn('source revision → governed context → recorded outcome', app)
        self.assertIn('item.source_revision', app)
        self.assertIn('context.payload_bytes', app)
        self.assertIn("includes('context_delivered')", app)
        self.assertIn('.ops-continuity-track', css)
        self.assertIn('.ops-continuity-node.delivered', css)
        self.assertNotIn('DURABLE CONTINUITY THREAD / FRESH INVOCATIONS', app)

    def test_handoff_story_requires_recorded_distinct_creator_and_resolver(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("c.status==='fulfilled'", app)
        self.assertIn('c.created_by&&c.resolved_by&&c.created_by!==c.resolved_by', app)
        self.assertIn('Each row is a commitment whose recorded creator and resolver are different invocations.', app)
        self.assertIn('No cross-invocation fulfillments recorded yet.', app)

    def test_frontier_queue_is_exact_open_commitment_state(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('FRONTIER QUEUE / EXACT OPEN WORK', app)
        self.assertIn("const openCommitments=obligations.filter(c=>c.status==='open')", app)
        self.assertIn('item?.due_cycle', app)
        self.assertIn('item?.created_version', app)
        self.assertIn('item?.created_by', app)
        self.assertIn('Every item comes directly from current governed commitment state.', app)
        self.assertIn('.ops-frontier-list', css)
        self.assertIn('.ops-frontier-item.overdue', css)

    def test_pressure_story_links_recent_rejections_to_exact_receipts(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('REJECTION LEDGER / EXACT RECENT RESISTANCE', app)
        self.assertIn("filter(event=>event?.kind==='rejected')", app)
        self.assertIn("event?.payload?.reason", app)
        self.assertIn("event?.payload?.proposal?.title", app)
        self.assertIn('href="#history/', app)
        self.assertIn('Family bars summarize pressure; these rows expose the latest recorded reasons and exact receipts.', app)
        self.assertIn('.ops-rejection-list', css)
        self.assertIn('.ops-rejection-row', css)

    def test_evidence_story_maps_recorded_topics_to_recorded_tiers(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('TOPIC × PROVENANCE TIER / OBSERVED EVIDENCE', app)
        self.assertIn("topic:payload?.topic_domain||'unattributed'", app)
        self.assertIn("tier:payload?.host_tier||'unspecified'", app)
        self.assertIn('evidenceTopicTierCounts', app)
        self.assertIn('This shows collection shape, not source quality or truth.', app)
        self.assertIn('--evidence-tier-count', app)
        self.assertIn('.ops-evidence-matrix-row', css)
        self.assertIn('var(--evidence-tier-count)', css)

    def test_matrix_story_reconciles_axis_marginals_to_same_cells(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('COVERAGE MARGINALS / THREE AXES', app)
        self.assertIn('const matrixCoverageSummary=statuses=>', app)
        self.assertIn('const matrixSemanticMarginals=', app)
        self.assertIn('const matrixExposureMarginals=', app)
        self.assertIn('const matrixPressureMarginals=', app)
        self.assertIn("status==='completed'", app)
        self.assertIn("status==='failed'", app)
        self.assertIn("status==='deferred'", app)
        self.assertIn('Each row reconciles to the same continuity@1 cells above.', app)
        self.assertIn('.ops-matrix-marginal-grid', css)

    def test_matrix_story_names_exact_next_uncovered_coordinate(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('const nextMatrixOrdinal=Number(matrixProgress?.next_ordinal||0)', app)
        self.assertIn('const nextMatrixSemanticIndex=', app)
        self.assertIn('const nextMatrixExposureIndex=', app)
        self.assertIn('const nextMatrixPressureIndex=', app)
        self.assertIn('NEXT UNCOVERED · #', app)
        self.assertIn('Failed or deferred coordinates remain uncovered until completed.', app)
        self.assertIn("matrix-plane ${isCurrentPlane?'current':''}", app)
        self.assertIn('.ops-matrix-frontier', css)
        self.assertIn('.matrix-plane.current', css)

    def test_belief_lineage_uses_only_stored_evidence_ids(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('EVIDENCE → BELIEF / EXPLICIT CITATION LINEAGE', app)
        self.assertIn('Array.isArray(belief?.evidence)?belief.evidence:[]', app)
        self.assertIn('Boolean(evidenceById[id])', app)
        self.assertIn('missing from current state', app)
        self.assertIn('Presence proves linkage in the record, not that the cited evidence is true or sufficient.', app)
        self.assertIn('.ops-lineage-row', css)
        self.assertIn('.ops-lineage-root.missing', css)

    def test_record_spine_links_use_receipt_ids_not_sequence_numbers(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("const receiptId=String(event.payload?.id||'')", app)
        self.assertIn("const href=receiptId?", app)
        self.assertNotIn('href="#history/${encodeURIComponent(event.seq', app)

    def test_operations_console_declares_mobile_and_wide_screen_breakpoints(self):
        css = self.read('wake/assets/style.css')
        self.assertIn('@media(max-width:430px)', css)
        self.assertIn('@media(max-width:700px)', css)
        self.assertIn('@media(min-width:701px) and (max-width:1000px)', css)
        self.assertIn('@media(min-width:1600px)', css)
        self.assertNotIn('@media(max-width:1000px){.ops-storyline{grid-template-columns:repeat(4,1fr)}', css)
        self.assertNotIn('.ops-storyline{grid-template-columns:repeat(2,1fr)}', css)
        self.assertIn('.ops-storyline{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:minmax(138px,48vw)}', css)
        self.assertIn('@media(min-width:2200px)', css)
        self.assertIn('.ops-tertiary-grid', css)
        self.assertIn('body.metrics-ops-active #metrics.view{width:100%;max-width:none', css)

    def test_data_story_navigator_tracks_scroll_position(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('function bindStoryNavigation()', app)
        self.assertIn("link.classList.toggle('is-active',active)", app)
        self.assertIn("link.setAttribute('aria-current','step')", app)
        self.assertIn("if(id===activeId)return", app)
        self.assertIn("window.addEventListener('scroll',storyScrollHandler,{passive:true})", app)
        self.assertIn('.ops-storyline{position:sticky', css)
        self.assertIn('scroll-snap-type:x proximity', css)
        self.assertIn('.ops-storyline a.is-active:after', css)

    def test_memory_story_exposes_exact_cross_invocation_handoffs(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('CROSS-INVOCATION HANDOFF / DURABLE OBLIGATIONS', app)
        self.assertIn('commitment.created_by', app)
        self.assertIn('commitment.resolved_by', app)
        self.assertIn('created_by&&c.resolved_by&&c.created_by!==c.resolved_by', app)
        self.assertIn('href="#history/${encodeURIComponent(createdId)}"', app)
        self.assertIn('href="#history/${encodeURIComponent(resolvedId)}"', app)
        self.assertIn('.ops-handoff-list', css)
        self.assertIn('.ops-handoff-path', css)

    def test_belief_story_links_recorded_evidence_and_update_receipts(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('EVIDENCE → BELIEF / EXPLICIT CITATION LINEAGE', app)
        self.assertIn('belief?.evidence', app)
        self.assertIn('belief?.updated_by', app)
        self.assertIn('belief?.updated_version', app)
        self.assertIn('href="#evidence/', app)
        self.assertIn('UPDATED BY', app)
        self.assertIn('FALSIFIER RECORDED', app)
        self.assertIn('.ops-lineage-list', css)
        self.assertIn('.ops-lineage-belief-meta', css)
        self.assertNotIn('.ops-belief-lineage-grid', css)

    def test_metrics_route_anchor_is_unique(self):
        page = self.read('wake/assets/index.html')
        app = self.read('wake/assets/app.js')
        self.assertEqual(page.count('id="metrics"'), 1)
        self.assertIn('id="journal-metrics"', page)
        self.assertIn("$('journal-metrics').innerHTML", app)

    def test_site_operator_link_goes_directly_to_github_actions(self):
        page = self.read('wake/assets/index.html')
        self.assertIn('href="https://github.com/sudofx/wake/actions"', page)
        self.assertNotIn('WAKE_CONTROL_URL', page)
        self.assertNotIn('control.js', page)
        self.assertFalse((ROOT / 'control-worker').exists())

if __name__ == '__main__':
    unittest.main()
