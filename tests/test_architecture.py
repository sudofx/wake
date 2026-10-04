from pathlib import Path
import re
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

    def test_recent_invocation_views_use_explicit_recorded_time_order(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("const invocationTime=item=>", app)
        self.assertIn("Date.parse(item?.time||item?.finished||'')", app)
        self.assertIn("Object.values(s.invocations || {}).sort(", app)
        self.assertIn("invocationTime(a)-invocationTime(b)", app)
        self.assertIn("String(a?.id||'').localeCompare(String(b?.id||''))", app)

    def test_now_story_leads_with_latest_accepted_wake_receipt(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('LATEST ACCEPTED WAKE', app)
        self.assertIn('const latestAcceptedEvent=accepted.at(-1)||null', app)
        self.assertIn('item?.invocation===latestAcceptedId', app)
        self.assertIn('latestAcceptedProposal?.actions', app)
        self.assertIn('latestAcceptedActions.slice(0,4)', app)
        self.assertIn("action?.statement||action?.task||action?.title||action?.status||action?.reason", app)
        self.assertIn('open exact receipt for full proposal', app)
        self.assertIn('EXACT RECEIPT →', app)
        self.assertIn('href="#history/${encodeURIComponent(latestAcceptedId)}"', app)
        self.assertIn('No durable journal summary is attached to the latest accepted wake.', app)
        self.assertIn('.ops-latest-wake', css)
        self.assertIn('.ops-latest-action-list', css)
        self.assertIn('.ops-latest-action', css)
        self.assertIn('.ops-latest-wake-meta', css)

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
        self.assertIn("matrixPct===null?'not enabled':matrixPct+'% tested'", app)
        self.assertIn("do not certify the truth of its research claims", app)
        self.assertIn("DEEP METRICS / VERIFY THE STORY", app)
        self.assertIn("the story can be checked rather than merely believed", app)
        self.assertNotIn("what is true", app)

    def test_deep_metric_verification_routes_are_direct_and_unique(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('DEEP METRICS / VERIFY THE STORY', app)
        self.assertIn('class="ops-verify-index"', app)
        for target in (
            "verify-actions",
            "verify-outcomes",
            "verify-continuity",
            "verify-yield",
            "verify-belief",
            "verify-frontier",
            "verify-space",
            "verify-provider",
            "verify-telemetry",
        ):
            self.assertEqual(app.count(f'id="{target}"'), 1)
            self.assertIn(f'href="#metrics" data-verify-target="{target}"', app)
        self.assertIn("event.target.closest('[data-story-target],[data-verify-target]')", app)
        self.assertIn("scrollLink.dataset.storyTarget||scrollLink.dataset.verifyTarget", app)
        self.assertIn('.ops-verify-index', css)
        self.assertIn('#verify-actions,#verify-outcomes,#verify-continuity,#verify-yield,#verify-belief,#verify-frontier,#verify-space,#verify-provider,#verify-telemetry{scroll-margin-top:72px}', css)
        self.assertIn('.ops-verify-index{display:grid;grid-template-columns:repeat(9,minmax(0,1fr))', css)
        self.assertIn('@media(min-width:701px) and (max-width:1000px){.ops-verify-index{grid-template-columns:repeat(3,minmax(0,1fr))}', css)
        self.assertIn('grid-auto-columns:minmax(126px,42vw)', css)
        self.assertIn('.ops-deep-dive-heading>p:not(.eyebrow)', css)

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

    def test_memory_omission_profile_uses_only_explicit_receipts(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('OMISSION PROFILE / RECENT CONTEXT DELIVERY', app)
        self.assertIn('item?.context_delivery?.omitted_categories', app)
        self.assertIn('Counts come only from explicit omitted_categories receipts.', app)
        self.assertIn('No omission is inferred from payload size or compression ratio.', app)
        self.assertIn('.ops-omission-profile', css)
        self.assertIn('.ops-omission-row', css)

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

    def test_publication_story_uses_stored_notebook_and_evidence_edges(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('PUBLICATION LINEAGE / AUDITABLE ARTIFACT CHAIN', app)
        self.assertIn("Array.isArray(post?.notebooks)?post.notebooks:[]", app)
        self.assertIn("Array.isArray(post?.evidence)?post.evidence:[]", app)
        self.assertIn("filter(post=>post?.project&&post?.status!=='superseded')", app)
        self.assertIn('Reflections without research-project lineage are intentionally excluded.', app)
        self.assertIn('href="#projects/notebook:', app)
        self.assertIn('href="#evidence/', app)
        self.assertIn("const exists=Boolean(evidenceById[id])", app)
        self.assertIn('not in current state', app)
        self.assertIn('record present', app)
        self.assertIn('href="#blog/', app)
        self.assertIn('.ops-publication-row', css)
        self.assertIn('.ops-publication-sources small,.ops-publication-notebooks small', css)
        self.assertEqual(css.count('.ops-publication-lineage{'), 1)

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
        self.assertIn('EVIDENCE → BELIEF / CURRENT GOVERNED LINEAGE', app)
        self.assertIn('Array.isArray(belief?.evidence)?belief.evidence:[]', app)
        self.assertIn('Boolean(evidenceById[id])', app)
        self.assertIn('missing from current state', app)
        self.assertIn('Presence proves linkage in the record', app)
        self.assertIn('not that the cited evidence is true or sufficient.', app)
        self.assertIn('.ops-lineage-row', css)
        self.assertIn('.ops-lineage-root.missing', css)

    def test_belief_lineage_keeps_current_retractions_visible_without_duplicate_ledger(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('EVIDENCE → BELIEF / CURRENT GOVERNED LINEAGE', app)
        self.assertIn("Number(b?.updated_version||0)-Number(a?.updated_version||0)", app)
        self.assertIn("String(belief?.status||'unknown').toLowerCase()", app)
        self.assertIn("String(belief?.updated_by||'')", app)
        self.assertIn("Array.isArray(belief?.evidence)?belief.evidence:[]", app)
        self.assertIn('Active and retracted beliefs remain visible here.', app)
        self.assertIn('.ops-lineage-belief.retracted', css)
        self.assertNotIn('BELIEF REVISION LEDGER / CURRENT GOVERNED STATE', app)
        self.assertNotIn('.ops-belief-ledger-list', css)

    def test_belief_action_history_is_bounded_to_published_accepted_receipts(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('RECENT BELIEF ACTIONS / PUBLISHED EVENT WINDOW', app)
        self.assertIn("accepted.forEach(event=>", app)
        self.assertIn("actions.filter(action=>action?.type==='belief')", app)
        self.assertIn('visibleBeliefConfidence', app)
        self.assertIn('This panel does not claim to contain revisions outside the published event window.', app)
        self.assertIn('href="#history/', app)
        self.assertIn('.ops-belief-history-list', css)
        self.assertIn('.ops-belief-action.retracted', css)

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

    def test_story_keeps_generic_lifecycle_in_verification_layer(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        deep = app.index('DEEP METRICS / VERIFY THE STORY')
        lifecycle = app.index('APPLICATION LIFECYCLE / GENERIC SUDOFX EVIDENCE')
        self.assertGreater(lifecycle, deep)
        self.assertIn('.ops-tertiary-grid>.ops-beliefs{grid-column:1/-1}', css)
        self.assertIn('.ops-tertiary-grid>.ops-context,.ops-tertiary-grid>.ops-provenance{border-top:0}', css)
        self.assertNotIn('.ops-tertiary-grid>.ops-lifecycle{border-left', css)

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

    def test_handoff_rate_is_unavailable_without_fulfilled_obligations(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("const handoffRate=fulfilled.length?Math.round(100*inheritedFulfilled.length/fulfilled.length):null", app)
        self.assertIn("handoffRate===null?'—':handoffRate+'%'", app)
        self.assertIn("'No fulfilled obligations yet'", app)

    def test_empty_performance_denominators_are_unavailable(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("const acceptanceRate=completed.length?Math.round(100*acceptedCount/completed.length):null", app)
        self.assertIn("const fallbackRate=completed.length?100*fallbackWakes/completed.length:null", app)
        self.assertIn("const rejectionRate=completed.length?100*rejectedCount/completed.length:null", app)
        self.assertIn("const actionPerAccepted=acceptedCount?(actionTotal/acceptedCount):null", app)
        self.assertIn("const evidencePerAccepted=acceptedCount?(evidenceCount/acceptedCount):null", app)
        self.assertIn("acceptanceRate===null?'—':acceptanceRate+'%'", app)
        self.assertIn("fallbackRate===null?'—':fallbackRate.toFixed(1)+'%'", app)
        self.assertIn("rejectionRate===null?'—':rejectionRate.toFixed(1)+'%'", app)
        self.assertIn("actionPerAccepted===null?'—':actionPerAccepted.toFixed(2)", app)
        self.assertIn("evidencePerAccepted===null?'—':evidencePerAccepted.toFixed(2)", app)

        self.assertIn("const wakesPerHour=recordHours>0?completed.length/recordHours:null", app)
        self.assertIn("const acceptedPerHour=recordHours>0?acceptedCount/recordHours:null", app)
        self.assertIn("wakesPerHour===null?'—':wakesPerHour.toFixed(2)+'/h'", app)
        self.assertIn("acceptedPerHour===null?'—':acceptedPerHour.toFixed(2)+'/h'", app)
        self.assertIn("const ratio=wall>0?effective/wall:null", app)
        self.assertIn("const tone=ratio===null?'unknown':ratio===0?'frozen'", app)

        self.assertIn("const topicCoveragePct=configuredTopicCount?100*topicActive/configuredTopicCount:null", app)
        self.assertIn("configuredTopicCount?topicActive+'/'+configuredTopicCount:'—'", app)
        self.assertIn("'No configured research topics'", app)

    def test_verification_panels_mark_unmeasured_populations(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("fulfilled.length?inheritedFulfilled.length:'—'", app)
        self.assertIn("fulfilled.length?'obligations fulfilled by a later invocation':'no fulfilled obligations yet'", app)
        self.assertIn("matrixEnabled?matrixCompleted+'/'+matrixTotal:'NOT ENABLED'", app)
        self.assertIn("matrixEnabled?matrixFailed:'—'", app)
        self.assertIn("WAKE has not recorded an enabled campaign in this generation.", app)

    def test_story_marks_disabled_matrix_campaign_as_unmeasured(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("const matrixPct=matrixEnabled&&matrixTotal?Math.round(100*matrixCompleted/matrixTotal):null", app)
        self.assertIn("matrixPct===null?'not enabled':matrixPct+'% tested'", app)
        self.assertIn("matrixPct===null?'continuity@1 not enabled':matrixPct+'% of continuity@1 tested'", app)
        self.assertIn("matrixPct===null?'—':matrixPct+'%'", app)
        self.assertIn("matrixPct===null?'not enabled':'covered'", app)

    def test_belief_story_links_recorded_evidence_and_update_receipts(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('EVIDENCE → BELIEF / CURRENT GOVERNED LINEAGE', app)
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

    def test_metrics_story_literal_ids_and_scroll_targets_stay_coherent(self):
        page = self.read('wake/assets/index.html')
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        markup = page + app
        literal_ids = re.findall(r'\bid="([^"]+)"', markup)
        duplicates = sorted({item for item in literal_ids if literal_ids.count(item) > 1})
        self.assertEqual(duplicates, [])
        targets = (
            re.findall(r'data-story-target="([^"]+)"', app)
            + re.findall(r'data-verify-target="([^"]+)"', app)
        )
        self.assertTrue(targets)
        for target in targets:
            self.assertEqual(literal_ids.count(target), 1, target)
        self.assertNotRegex(css, r'\d+(?:px|em|rem|fr|%)\.[A-Za-z_-][\w-]*\{')
        self.assertNotRegex(css, r'repeat\([^{}]+\)\.[A-Za-z_-]')

    def test_site_operator_link_goes_directly_to_github_actions(self):
        page = self.read('wake/assets/index.html')
        self.assertIn('href="https://github.com/sudofx/wake/actions"', page)
        self.assertNotIn('WAKE_CONTROL_URL', page)
        self.assertNotIn('control.js', page)
        self.assertFalse((ROOT / 'control-worker').exists())

if __name__ == '__main__':
    unittest.main()
