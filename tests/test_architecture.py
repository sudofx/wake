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

    def test_in_app_history_discloses_bounded_window_and_links_full_export(self):
        page = self.read('wake/assets/index.html')
        app = self.read('wake/assets/app.js')
        help_js = self.read('wake/assets/help.js')
        live = self.read('wake/live.py')
        report = self.read('wake/report.py')
        self.assertIn('MAX_EVENTS = 400', live)
        self.assertIn('"events": store.tail_events_all(MAX_EVENTS)', live)
        self.assertIn('RECENT EVENT WINDOW / AUDIT TRAIL', page)
        self.assertIn('bounded recent event window', page)
        self.assertIn('href="events.html">Standalone full history →</a>', page)
        self.assertIn('All visible events', page)
        self.assertIn('More visible events ↓', page)
        self.assertIn('← All visible events', app)
        self.assertIn('Receipt not in the recent event window.', app)
        self.assertIn('This exact ID may have aged out of the bounded browser projection.', app)
        self.assertIn('href="events.html">Open standalone full history →</a>', app)
        self.assertIn('The in-app History panel carries a bounded recent event window', help_js)
        self.assertNotIn('History lists every saved event', help_js)
        self.assertIn('"History", "THE APPEND-ONLY RECORD", "Exact history."', report)
        self.assertIn('"events", "events.jsonl"', report)

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

    def test_journal_survives_when_accepted_receipt_ages_out_of_event_window(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("const i=s.invocations[j.invocation]||{}, event=decisions[j.invocation]||null", app)
        self.assertIn("Array.isArray(event?.payload?.proposal?.actions)?event.payload.proposal.actions:null", app)
        self.assertIn('proposal detail outside published event window', app)
        self.assertIn('accepted proposal receipt is outside this bounded event window', app)
        self.assertNotIn('event=decisions[j.invocation], actions=event.payload.proposal.actions', app)

    def test_now_story_uses_durable_latest_status_and_bounded_receipt_detail(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('LATEST ACCEPTED WAKE', app)
        self.assertIn("const latestAcceptedJournal=(s.journal||[]).at(-1)||null", app)
        self.assertIn("const latestAcceptedInvocationFallback=[...invocations].reverse().find(item=>item?.status==='accepted')||null", app)
        self.assertIn("String(latestAcceptedJournal?.invocation||latestAcceptedInvocationFallback?.id||'')", app)
        self.assertIn("find(event=>String(event?.payload?.id||'')===latestAcceptedId)", app)
        self.assertIn("Array.isArray(latestAcceptedProposal?.actions)?latestAcceptedProposal.actions:null", app)
        self.assertIn('latestAcceptedActions?latestAcceptedActions.slice(0,4)', app)
        self.assertIn("action?.statement||action?.task||action?.title||action?.status||action?.reason", app)
        self.assertIn('const latestAcceptedReceiptLink=latestAcceptedEvent', app)
        self.assertIn('EXACT RECEIPT →', app)
        self.assertIn('JOURNAL ENTRY →', app)
        self.assertIn('EVENT OUTSIDE PUBLISHED WINDOW', app)
        self.assertIn('Proposal detail is outside the published event window.', app)
        self.assertIn('no action count is inferred', app)
        self.assertIn('No durable journal summary is attached to the latest accepted wake.', app)
        self.assertNotIn('No accepted wake is present in the published record.', app)
        self.assertIn('.ops-latest-wake', css)
        self.assertIn('.ops-latest-action-list', css)
        self.assertIn('.ops-latest-action', css)
        self.assertIn('.ops-latest-wake-meta', css)

    def test_latest_wake_transition_marks_receipt_fields_unavailable_outside_window(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn("event?.kind==='invocation_started'", app)
        self.assertIn("event?.payload?.id||''", app)
        self.assertIn('latestAcceptedStartEvent?.payload?.base_version', app)
        self.assertIn('latestAcceptedEvent?.payload?.result_hash', app)
        self.assertIn('latestAcceptedEvent?.payload?.hash_fields', app)
        self.assertIn('start receipt unavailable in published event window', app)
        self.assertIn('hash field list unavailable in published event window', app)
        self.assertIn('BASE REVISION', app)
        self.assertIn('ACCEPTED REVISION', app)
        self.assertIn('RESULT HASH', app)
        self.assertIn('.ops-latest-transition', css)
        self.assertIn('.ops-latest-effect-strip', css)

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

    def test_deep_metrics_disclose_full_history_vs_event_window_fallbacks(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("hasFullRejectionMetrics=Object.prototype.hasOwnProperty.call(fullMetrics,'rejection_reasons')", app)
        self.assertIn("FULL-HISTORY METRICS", app)
        self.assertIn("PUBLISHED EVENT WINDOW FALLBACK", app)
        self.assertIn("const acceptedActionMetricSource=fullActions?", app)
        self.assertIn("A fallback is explicitly bounded to the published event window", app)

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

    def test_longitudinal_story_distinguishes_declared_and_legacy_reflections(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('LONGITUDINAL RECORD / DURABLE REFLECTIONS', app)
        self.assertIn('post?.reflection_cycle', app)
        self.assertIn("const legacyClassified=!declared&&created>0&&created%10===0", app)
        self.assertIn("origin:declared?'declared':'legacy'", app)
        self.assertIn('legacy cycle-10 reflections preserved by historical governance', app)
        self.assertIn("item.origin==='declared'?'DECLARED':'LEGACY'", app)
        self.assertIn('.ops-history-dot.legacy i', css)
        self.assertIn('DECLARED RECEIPT', app)
        self.assertIn('LEGACY REPLAY CLASSIFICATION', app)
        self.assertIn('class="ops-history-legend"', app)
        self.assertIn('.ops-history-legend .legacy i', css)
        self.assertIn('Gaps remain gaps.', app)
        self.assertNotIn('Only explicit reflection receipts are plotted.', app)
        self.assertNotIn('inferred era', app.lower())

    def test_longitudinal_record_hands_off_to_current_state_without_inference(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('const reflectionVersionSpan=hasReflectionBaseline?', app)
        self.assertIn('Transition from durable reflection history to current governed state', app)
        self.assertIn('LAST REFLECTION RECEIPT', app)
        self.assertIn('CURRENT GOVERNED STATE', app)
        self.assertIn('version span ${reflectionVersionSpan}', app)
        self.assertIn('no baseline inferred', app)
        self.assertIn('${historyToNowHtml}', app)
        self.assertIn('.ops-present-bridge{display:grid', css)
        self.assertIn('.ops-present-line i{position:absolute', css)
        self.assertIn('@media(min-width:1600px){', css)
        self.assertIn('@media(max-width:430px){.ops-present-bridge{grid-template-columns:minmax(0,1fr) 34px minmax(0,1fr)}', css)

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

    def test_reflection_delta_does_not_read_belief_const_before_initialization(self):
        app = self.read('wake/assets/app.js')
        delta = app.index('const sinceReflection={')
        beliefs = app.index('const opsBeliefs=')
        self.assertGreaterEqual(delta, 0)
        self.assertGreater(beliefs, delta)
        self.assertIn("beliefs:Object.values(s.beliefs||{}).filter", app[delta:beliefs])
        self.assertNotIn('beliefs:opsBeliefs.filter', app[delta:beliefs])

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

    def test_journal_handoff_metric_does_not_claim_process_freshness(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("'Across distinct invocations'", app)
        self.assertNotIn("'Across fresh invocations'", app)

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
        self.assertIn('rejected receipts in published event window', app)
        self.assertIn('Family bars may use full-history metrics; these rows are bounded to the public event window', app)
        self.assertNotIn('rejected receipts in published history', app)
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

    def test_matrix_cells_are_explorable_without_public_result_bodies(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('data-matrix-cell', app)
        self.assertIn('COORDINATE INSPECTOR / PUBLIC TELEMETRY', app)
        self.assertIn('data-matrix-inspector="ordinal"', app)
        self.assertIn('data-matrix-inspector="status"', app)
        self.assertIn('data-matrix-inspector="semantic"', app)
        self.assertIn('data-matrix-inspector="exposure"', app)
        self.assertIn('data-matrix-inspector="pressure"', app)
        self.assertIn("event.key==='ArrowLeft'", app)
        self.assertIn("event.key==='ArrowRight'", app)
        self.assertIn("event.key==='ArrowUp'", app)
        self.assertIn("event.key==='ArrowDown'", app)
        self.assertIn("cell.closest('.matrix-plane-grid')", app)
        self.assertIn("item.tabIndex=item===cell?0:-1", app)
        self.assertIn("grid.addEventListener('click'", app)
        self.assertIn("grid.addEventListener('focusin'", app)
        self.assertIn("grid.addEventListener('keydown'", app)
        self.assertNotIn("cell.addEventListener('click'", app)
        self.assertIn('result summaries and scores remain outside this projection', app)
        self.assertNotIn('matrixProgress?.results', app)
        self.assertIn('.ops-matrix-explorer', css)
        self.assertIn('.continuity-cell[aria-pressed="true"]', css)

    def test_evidence_to_belief_bridge_uses_only_stored_citation_state(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('EVIDENCE → BELIEF / STORED CITATION BOUNDARY', app)
        self.assertIn('Stored linkage only. Citation presence does not prove truth, sufficiency, or causation.', app)
        self.assertIn('CURRENT EVIDENCE RECORDS', app)
        self.assertIn('UNIQUE CITED EVIDENCE IDS', app)
        self.assertIn('STORED CITATION EDGES', app)
        self.assertIn('BELIEFS WITH CITATIONS', app)
        self.assertIn('present · ${missingCitedEvidenceIds} missing now', app)
        self.assertIn('.ops-evidence-belief-bridge{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-evidence-belief-grid{display:grid;grid-template-columns:minmax(150px,1.05fr)', css)
        self.assertIn('.ops-evidence-belief-grid{grid-template-columns:repeat(2,minmax(0,1fr))}', css)
        self.assertIn('.ops-evidence-belief-grid>i{display:none}', css)

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

    def test_verification_rail_keeps_thumb_sized_targets(self):
        css = self.read('wake/assets/style.css')
        self.assertIn('.ops-verify-index a{position:relative;display:grid;gap:3px;min-width:0;min-height:44px;align-content:center', css)

    def test_ultrawide_pairs_frontier_and_inquiry_drive_only(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('<div class="ops-frontier-pair">', app)
        self.assertIn('.ops-frontier-pair{display:grid;grid-template-columns:1fr}', css)
        self.assertIn('.ops-frontier-pair{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);border-top:1px solid var(--ops-line)}', css)
        self.assertIn('.ops-frontier-pair>.ops-drive{border-left:1px solid var(--ops-line)}', css)

    def test_phone_story_microtype_keeps_meaningful_labels_legible(self):
        css = self.read('wake/assets/style.css')
        self.assertIn('.ops-provenance-jump a small,.ops-audit-steps small,.ops-history-legend span,.ops-present-endpoint small{font-size:7px}', css)

    def test_phone_verification_rail_raises_microtype(self):
        css = self.read('wake/assets/style.css')
        self.assertIn('.ops-verify-index span{font-size:8px}.ops-verify-index strong{font-size:9px}', css)

    def test_metrics_opens_with_compact_control_room_overview(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('CONTROL ROOM / CURRENT PUBLISHED PROJECTION', app)
        self.assertIn('class="ops-command-zones" aria-hidden="true"', app)
        self.assertIn('<span>OPERATIONS</span><span>SCIENTIFIC INSTRUMENTS</span><span>AUDIT</span>', app)
        self.assertIn('Fast orientation only. Open a cell for the underlying story, provenance, or record evidence.', app)
        self.assertIn('href="#metrics/ops-now"', app)
        self.assertIn('href="#metrics/ops-pressure"', app)
        self.assertIn('href="#metrics/ops-horizon"', app)
        self.assertIn('href="#metrics/ops-matrix"', app)
        self.assertIn('href="map3d.html#record=root%3Awake"', app)
        self.assertIn('href="events.html"', app)
        self.assertIn('data-route="STORY 01 / NOW"', app)
        self.assertIn('data-route="STORY 02 / PRESSURE"', app)
        self.assertIn('data-route="STORY 06 / FRONTIER"', app)
        self.assertIn('data-route="STORY 07 / SPACE"', app)
        self.assertIn('data-route="3D / PROVENANCE"', app)
        self.assertIn('data-route="RECORD / FULL HISTORY"', app)
        self.assertIn('success-labelled', app)
        self.assertIn('seven bars = semantic-plane completion · deterministic test space, not research quality', app)
        self.assertIn('bars = relative accepted-action weight of top topic lanes · open 3D provenance', app)
        self.assertIn('const commandMatrixBars=semanticAxis.map', app)
        self.assertIn("cells.filter(status=>status==='completed')", app)
        self.assertIn('const commandTopicBars=visibleTopics.slice(0,7).map', app)
        self.assertIn('100*topic.total/opsTopicMax', app)
        self.assertIn('class="ops-command-micro" aria-hidden="true"', app)
        self.assertIn('local replay + SQLite integrity evidence', app)
        self.assertIn('const providerQuotaPct=Number.isFinite(providerDailyLimit)&&providerDailyLimit>0', app)
        self.assertIn('charged request slots', app)
        self.assertIn("ops-command-meter ${providerQuotaPct===null?'unavailable':''}", app)
        self.assertIn("ops-command-meter ${matrixPct===null?'unavailable':''}", app)
        self.assertIn("ops-command-meter ${topicCoveragePct===null?'unavailable':''}", app)
        self.assertIn('const commandProviderBars=providerTraceSource.slice(-7).map', app)
        self.assertIn("const tone=['success','accepted','ok'].includes(result)?'ok':'warn'", app)
        self.assertIn('class="ops-command-micro provider"', app)
        self.assertIn('bars = recent attempt latency', app)
        self.assertIn('const frontierBucketMax=Math.max(1,...obligationBuckets.map', app)
        self.assertIn('const commandFrontierBars=obligationBuckets.map', app)
        self.assertIn('class="ops-command-micro frontier"', app)
        self.assertIn('bars = overdue → later due horizon', app)
        self.assertIn("ops-command-meter acceptance ${acceptanceRate===null?'unavailable':''}", app)
        self.assertIn('const frontierOverduePct=openObligations?', app)
        self.assertIn('class="ops-command-meter pressure"', app)
        self.assertIn('class="ops-command-lamps" aria-label="Durable record integrity checks"', app)
        self.assertIn("class=\"${recordReplayOk?'ok':'warn'}\"", app)
        self.assertIn("class=\"${sqliteQuickOk?'ok':'warn'}\"", app)
        self.assertIn('data-instrument="continuity"', app)
        self.assertIn('data-instrument="provenance"', app)
        self.assertIn('ops-command-meter acceptance', app)
        self.assertIn('const frontierOverduePct=openObligations?', app)
        self.assertIn('ops-command-meter pressure', app)
        self.assertIn('ops-command-lamps', app)
        self.assertIn('REPLAY', app)
        self.assertIn('SQLITE', app)
        self.assertIn('.ops-command-meter.acceptance:after', css)
        self.assertIn('.ops-command-meter.pressure:after', css)
        self.assertIn('.ops-command-lamps{display:flex', css)
        self.assertIn('@media(min-width:1500px){', css)
        self.assertIn('.ops-command-zones{display:grid;grid-template-columns:3fr 4fr 1fr', css)
        self.assertIn('.ops-command-zones span:nth-child(2){color:var(--ops-cyan)}', css)
        self.assertIn('.ops-command-zones span:last-child{border-right:0;text-align:center;color:var(--ops-green)}', css)
        self.assertIn('.ops-command-grid{grid-template-columns:repeat(8,minmax(0,1fr))}', css)
        self.assertIn('.ops-command-grid>a[data-instrument]{grid-column:span 2;min-height:110px', css)
        self.assertIn('.ops-command-micro{display:grid;grid-template-columns:repeat(7,minmax(0,1fr))', css)
        self.assertIn('.ops-command-grid>a[data-instrument="continuity"] .ops-command-micro i{background:var(--ops-orange)', css)
        self.assertIn('.ops-command-grid>a[data-instrument="provenance"] .ops-command-micro i{background:var(--ops-green)', css)
        self.assertIn('.ops-command-micro.provider i.ok{background:var(--ops-green)', css)
        self.assertIn('.ops-command-micro.provider i.warn{background:var(--ops-amber)', css)
        self.assertIn('.ops-command-micro.frontier{grid-template-columns:repeat(5,minmax(0,1fr))}', css)
        self.assertIn('.ops-command-micro.frontier i.danger{background:var(--ops-red)', css)
        self.assertIn('.ops-command-micro.frontier i.warning{background:var(--ops-amber)', css)
        self.assertIn('.ops-command-meter{position:relative;display:block;height:3px', css)
        self.assertIn('.ops-command-meter.unavailable:after{display:none}', css)
        self.assertIn('.ops-command-meter.acceptance:after{background:linear-gradient', css)
        self.assertIn('.ops-command-meter.pressure:after{background:linear-gradient', css)
        self.assertIn('.ops-command-lamps{display:flex;align-items:center', css)
        self.assertIn('.ops-command-lamps .ok i{border-color:var(--ops-green)', css)
        self.assertIn('.ops-command-lamps .warn i{border-color:var(--ops-amber)', css)
        self.assertIn('.ops-command-grid>a[data-instrument="continuity"] span{color:var(--ops-orange)}', css)
        self.assertIn('.ops-command-grid>a[data-instrument="provenance"] span{color:var(--ops-green)}', css)
        self.assertIn('.ops-command-deck{margin:0 0 10px', css)
        self.assertIn('.ops-command-grid{display:grid;grid-template-columns:repeat(6,minmax(0,1fr))}', css)
        self.assertIn('.ops-command-grid{grid-template-columns:none;grid-auto-flow:column', css)
        self.assertIn('.ops-command-grid>a[data-route]:after{content:attr(data-route)', css)
        self.assertIn('.ops-command-grid>a[data-route]{padding-top:21px}', css)
        self.assertIn('.ops-command-grid>a[data-tone="ok"]:before,.ops-command-grid>a[data-tone="running"]:before', css)
        self.assertIn('@media(min-width:1800px)', css)

    def test_wide_control_room_groups_zones_and_labels_destinations(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('class="ops-command-zones" aria-hidden="true"', app)
        self.assertIn('<span>OPERATIONS</span><span>SCIENTIFIC INSTRUMENTS</span><span>AUDIT</span>', app)
        self.assertIn('data-route="STORY 01 / NOW"', app)
        self.assertIn('data-route="STORY 02 / PRESSURE"', app)
        self.assertIn('data-route="STORY 06 / FRONTIER"', app)
        self.assertIn('data-route="STORY 07 / SPACE"', app)
        self.assertIn('data-route="3D / PROVENANCE"', app)
        self.assertIn('data-route="RECORD / FULL HISTORY"', app)
        self.assertIn('.ops-command-zones{display:none}', css)
        self.assertIn('.ops-command-grid>a[data-route]:after{content:attr(data-route)', css)
        self.assertIn('.ops-command-zones{display:grid;grid-template-columns:3fr 4fr 1fr', css)
        self.assertIn('.ops-command-grid>a[data-instrument]{grid-column:span 2;min-height:110px', css)

    def test_control_room_source_badges_report_projection_authority_and_access(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('class="ops-command-badges" aria-label="Projection source status"', app)
        self.assertIn('<b>PROJECTED</b>', app)
        self.assertIn('<b>AUTHORITY</b>', app)
        self.assertIn('<b>ACCESS</b>', app)
        self.assertIn('${esc(sourceAuthority)}', app)
        self.assertIn("accessEnabled===true?'ENABLED':accessEnabled===false?'DISABLED':'UNKNOWN'", app)
        self.assertIn("const currentStatus=accessEnabled===false?'STOPPED':wakeStatus.pending?'PENDING':wakeStatus.next_eligible?'WAITING':'IDLE';", app)
        self.assertIn('.ops-command-badges{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))', css)
        self.assertNotIn('ops-command-head-side{display:grid!important', css)
        self.assertIn('.ops-command-badges>span.ok{', css)
        self.assertIn('.ops-command-badges>span.warn{', css)
        self.assertIn('.ops-command-badges>span.unknown{border-style:dashed}', css)

    def test_control_room_recent_receipt_pulse_is_bounded_linked_and_phone_safe(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn("const commandPulseSource=[...completed]", app)
        self.assertIn(".slice(-48)", app)
        self.assertIn("['accepted','rejected','deferred','failed','recovered'].includes(item.status)", app)
        self.assertIn('class="ops-command-pulse" aria-label="Recent completed wake receipts"', app)
        self.assertIn('RECENT WAKE PULSE', app)
        self.assertIn('href="#history/${encodeURIComponent(item.id||\'\')}"', app)
        self.assertIn('.ops-command-pulse{display:grid;grid-template-columns:minmax(190px,.55fr) minmax(0,1.45fr)', css)
        self.assertIn('.ops-command-pulse-cell.accepted,.ops-command-pulse-cell.recovered{background:var(--ops-green)', css)
        self.assertIn('.ops-command-pulse-cell.rejected{background:var(--ops-orange)', css)
        self.assertIn('.ops-command-pulse-cell.failed{background:var(--ops-red)', css)
        self.assertIn('.ops-command-pulse-track{display:flex;gap:4px;overflow-x:auto', css)
        self.assertIn('.ops-command-pulse-cell{flex:0 0 28px;height:44px}', css)

    def test_frontier_to_space_keeps_application_work_separate_from_test_geometry(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('FRONTIER → SPACE / DOMAIN BOUNDARY', app)
        self.assertIn('Application work beside deterministic test geometry.', app)
        self.assertIn('No mapping is implied. Open commitments are WAKE application state; continuity@1 coordinates are reusable continuity-test coverage.', app)
        self.assertIn('OPEN COMMITMENTS', app)
        self.assertIn('CONTINUITY COVERAGE', app)
        self.assertIn('NEXT UNCOVERED', app)
        self.assertIn('OPEN SPACE CHAPTER →', app)
        self.assertIn('.ops-frontier-space-bridge{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-frontier-space-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr)) 28px repeat(2,minmax(0,1fr)) auto', css)
        self.assertIn('.ops-frontier-space-grid{grid-template-columns:repeat(2,minmax(0,1fr))}', css)
        self.assertIn('.ops-frontier-space-grid>a{grid-column:1/-1;min-height:44px}', css)

    def test_belief_to_frontier_is_population_boundary_not_causal_edge(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('BELIEF → FRONTIER / STORY BOUNDARY', app)
        self.assertIn('Adjacent governed populations only. No causal edge from belief state to commitment state is asserted here.', app)
        self.assertIn('ACTIVE BELIEFS', app)
        self.assertIn('RETRACTED BELIEFS', app)
        self.assertIn('OPEN COMMITMENTS', app)
        self.assertIn('OVERDUE', app)
        self.assertIn('OPEN FRONTIER CHAPTER →', app)
        self.assertIn('.ops-belief-frontier-bridge{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-belief-frontier-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr)) 28px repeat(2,minmax(0,1fr)) auto', css)
        self.assertIn('.ops-belief-frontier-grid{grid-template-columns:repeat(2,minmax(0,1fr))}', css)
        self.assertIn('.ops-belief-frontier-grid>a{grid-column:1/-1;min-height:44px}', css)

    def test_pressure_to_memory_handoff_uses_only_explicit_context_delivery_receipt(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('PRESSURE → MEMORY / LATEST RECORDED CONTEXT BOUNDARY', app)
        self.assertIn('Story transition only. This does not claim pressure caused compression', app)
        self.assertIn('const contextRichChars=Number(contextDelivery?.rich_context_chars||0)', app)
        self.assertIn('const contextDeliveredChars=Number(contextDelivery?.delivered_request_chars||contextDelivery?.delivered_context_chars||0)', app)
        self.assertIn('const contextDeliveredPct=contextDelivery&&contextRichChars>0?', app)
        self.assertIn('const contextOmittedCount=Array.isArray(contextDelivery?.omitted_categories)?', app)
        self.assertIn('OPEN CONTEXT RECEIPT →', app)
        self.assertIn('.ops-memory-flow{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-memory-flow-grid{display:grid;grid-template-columns:minmax(100px,.75fr)', css)
        self.assertIn('.ops-memory-flow-grid{grid-template-columns:repeat(2,minmax(0,1fr))}', css)
        self.assertIn('.ops-memory-flow-grid>a,.ops-memory-flow-unavailable{grid-column:1/-1;min-height:44px', css)

    def test_control_room_hands_off_explicitly_to_evidence_story(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('FROM GLANCE TO EVIDENCE', app)
        self.assertIn('Read the record in sequence.', app)
        self.assertIn('The control room compresses current signals.', app)
        self.assertIn('what happened, what resisted, what survived, what was observed, what is carried, what remains, and where continuity has been tested', app)
        self.assertIn('.ops-story-gate{display:grid;grid-template-columns:auto auto minmax(0,1fr)', css)
        self.assertIn('.ops-story-gate{grid-template-columns:1fr;gap:4px;padding:9px 10px}', css)

    def test_phone_control_room_is_glance_grid_while_story_stays_swipeable(self):
        css = self.read('wake/assets/style.css')
        self.assertIn('.ops-command-grid{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-flow:row;grid-auto-columns:auto;overflow:visible;scroll-snap-type:none}', css)
        self.assertIn('.ops-command-grid>a:nth-child(2n){border-right:0}', css)
        self.assertIn('.ops-command-grid>a:nth-last-child(-n+2){border-bottom:0}', css)
        self.assertIn('.ops-storyline{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:minmax(138px,48vw)}', css)

    def test_primary_control_room_microvisuals_are_data_driven(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('const commandMatrixBars=semanticAxis.map((semantic,index)=>{', app)
        self.assertIn("const cells=matrixStatuses.slice(index*49,index*49+49)", app)
        self.assertIn("cells.filter(status=>status==='completed').length", app)
        self.assertIn('seven bars = semantic-plane completion', app)
        self.assertIn('const commandTopicBars=visibleTopics.slice(0,7).map(topic=>{', app)
        self.assertIn('const pct=100*topic.total/opsTopicMax', app)
        self.assertIn('bars = relative accepted-action weight of top topic lanes', app)
        self.assertIn('.ops-command-micro{display:grid;grid-template-columns:repeat(7,minmax(0,1fr))', css)
        self.assertIn('data-instrument="continuity"', app)
        self.assertIn('data-instrument="provenance"', app)

    def test_control_room_24h_activity_is_projection_anchored_and_bounded(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn("const projectionMs=Date.parse(data.generated||'')", app)
        self.assertIn("const commandActivityBuckets=Array.from({length:24}", app)
        self.assertIn("const ageHours=Math.floor((projectionMs-timeMs)/36e5)", app)
        self.assertIn("if(ageHours<0||ageHours>=24)return", app)
        self.assertIn("commandActivityBuckets[23-ageHours][status]+=1", app)
        self.assertIn('24H WAKE ACTIVITY', app)
        self.assertIn('hourly bins by projection timestamp · spacing represents time, not receipt order', app)
        self.assertIn('.ops-command-activity{display:grid', css)
        self.assertIn('.ops-command-activity-track{display:grid;grid-template-columns:repeat(24', css)
        self.assertIn('.ops-command-activity{grid-template-columns:1fr', css)

    def test_control_room_recent_wake_pulse_is_receipt_backed_and_device_aware(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('const commandPulseSource=[...completed]', app)
        self.assertIn('.slice(-48)', app)
        self.assertIn('class="ops-command-pulse" aria-label="Recent completed wake receipts"', app)
        self.assertIn('RECENT WAKE PULSE', app)
        self.assertIn('each cell is a recorded outcome', app)
        self.assertIn('href="#history/${encodeURIComponent(item.id||\'\')}"', app)
        self.assertIn('.ops-command-pulse{display:grid;grid-template-columns:minmax(190px,.55fr) minmax(0,1.45fr)', css)
        self.assertIn('.ops-command-pulse-track{display:flex;align-items:stretch;gap:2px', css)
        self.assertIn('.ops-command-pulse-cell.accepted,.ops-command-pulse-cell.recovered', css)
        self.assertIn('.ops-command-pulse-cell.rejected', css)
        self.assertIn('.ops-command-pulse-cell.deferred', css)
        self.assertIn('.ops-command-pulse-cell.failed', css)
        self.assertIn('.ops-command-pulse>header{display:grid;grid-template-columns:1fr auto', css)
        self.assertIn('.ops-command-pulse-cell{flex:0 0 28px;height:44px}', css)

    def test_now_to_pressure_flow_uses_only_terminal_invocation_statuses(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn("const completed=invocations.filter(i=>['accepted','rejected','deferred','failed','recovered'].includes(i.status))", app)
        self.assertIn('const statusShare=count=>completed.length?100*count/completed.length:0', app)
        self.assertIn('NOW → PRESSURE / TERMINAL STATUS DISTRIBUTION', app)
        self.assertIn('Durable invocation statuses only.', app)
        self.assertIn('style="--share:${statusShare(acceptedCount).toFixed(2)}%"', app)
        self.assertIn('style="--share:${statusShare(rejectedCount).toFixed(2)}%"', app)
        self.assertIn('style="--share:${statusShare(deferredCount).toFixed(2)}%"', app)
        self.assertIn('style="--share:${statusShare(failedCount).toFixed(2)}%"', app)
        self.assertIn('style="--share:${statusShare(recoveredCount).toFixed(2)}%"', app)
        self.assertIn('.ops-decision-flow{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-decision-cells{display:grid;grid-template-columns:repeat(5,minmax(0,1fr))', css)
        self.assertIn('.ops-decision-flow>header{display:block;padding:9px 10px 8px}', css)

    def test_memory_to_evidence_handoff_keeps_receipt_and_state_scopes_distinct(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('const contextRetrievalEvidence=Number.isFinite(Number(contextMetrics.retrieval_evidence_count))', app)
        self.assertIn('const contextRehydratedEvidence=Number.isFinite(Number(contextMetrics.retrieval_rehydrated_evidence_count))', app)
        self.assertIn('const contextTrustRoots=Number.isFinite(Number(contextMetrics.trust_compact_evidence_root_count))', app)
        self.assertIn('MEMORY → EVIDENCE / LATEST CONTEXT RECEIPT', app)
        self.assertIn('Recovery scope beside governed evidence state.', app)
        self.assertIn('These populations have different scopes. They are shown side by side, not as a conservation funnel.', app)
        self.assertIn('CURRENT GOVERNED EVIDENCE', app)
        self.assertIn('RETRIEVAL ROOTS SELECTED', app)
        self.assertIn('EXACT EVIDENCE REHYDRATED', app)
        self.assertIn('COMPACT TRUST ROOTS', app)
        self.assertIn('.ops-memory-evidence-bridge{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-memory-evidence-steps{display:grid;grid-template-columns:minmax(150px,1.15fr)', css)
        self.assertIn('.ops-memory-evidence-steps{grid-template-columns:repeat(2,minmax(0,1fr))}', css)

    def test_evidence_to_belief_boundary_uses_only_stored_citation_linkage(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('const beliefsWithEvidence=opsBeliefs.filter', app)
        self.assertIn('const citedEvidenceIds=[...new Set(opsBeliefs.flatMap', app)
        self.assertIn('const presentCitedEvidenceIds=citedEvidenceIds.filter(id=>Boolean(evidenceById[id])).length', app)
        self.assertIn('const missingCitedEvidenceIds=Math.max(0,citedEvidenceIds.length-presentCitedEvidenceIds)', app)
        self.assertIn('EVIDENCE → BELIEF / STORED CITATION BOUNDARY', app)
        self.assertIn('Stored linkage only. Citation presence does not prove truth, sufficiency, or causation.', app)
        self.assertIn('UNIQUE CITED EVIDENCE IDS', app)
        self.assertIn('STORED CITATION EDGES', app)
        self.assertIn('BELIEFS WITH CITATIONS', app)
        self.assertIn('.ops-evidence-belief-bridge{border-top:1px solid var(--ops-line)', css)
        self.assertIn('.ops-evidence-belief-grid{display:grid;grid-template-columns:minmax(150px,1.05fr)', css)
        self.assertIn('.ops-evidence-belief-grid{grid-template-columns:repeat(2,minmax(0,1fr))}', css)

    def test_metrics_story_links_only_explicit_3d_provenance_branches(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('3D PROVENANCE / EXPLICIT EXPORTED BRANCHES', app)
        self.assertIn('Recorded parent → child relationships only. This view is separate from continuity@1 test geometry.', app)
        self.assertIn('map3d.html#record=root%3Awake', app)
        self.assertIn('map3d.html#record=root%3Aprojects', app)
        self.assertIn('map3d.html#record=root%3Aevidence', app)
        self.assertIn('map3d.html#record=root%3Acommitments', app)
        self.assertIn('map3d.html#record=root%3Aresearch', app)
        self.assertNotIn('map3d.html#record=root%3Abeliefs', app)
        self.assertNotIn('map3d.html#record=root%3Amatrix', app)
        self.assertIn('.ops-provenance-jump{display:grid', css)
        self.assertIn('.ops-provenance-jump nav{display:grid', css)
        self.assertIn('.ops-provenance-jump nav{grid-template-columns:none;grid-auto-flow:column', css)

    def test_data_story_exposes_story_verify_record_audit_path(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        self.assertIn('READING DEPTH / FOLLOW THE RECEIPTS', app)
        self.assertIn('Story → verification → record.', app)
        self.assertIn('data-story-target="ops-now"', app)
        self.assertIn('data-verify-target="verify-actions"', app)
        self.assertIn('<a href="#history"><b>03</b><span>RECORD</span>', app)
        self.assertIn('class="ops-audit-export" href="events.html"', app)
        self.assertIn('LAYER 02 / VERIFY', app)
        self.assertIn('LAYER 03 · RECENT EVENT WINDOW →', app)
        self.assertIn('FULL EXPORTED EVENTS ↗', app)
        self.assertIn('.ops-audit-ladder{display:grid', css)
        self.assertIn('.ops-audit-steps{display:grid', css)
        self.assertIn('.ops-verify-depth{display:flex', css)
        self.assertIn('.ops-audit-steps{grid-template-columns:none;grid-auto-flow:column', css)

    def test_data_story_transition_sequence_is_complete_and_ordered(self):
        app = self.read('wake/assets/app.js')
        labels = [
            'NOW → PRESSURE',
            'PRESSURE → MEMORY',
            'MEMORY → EVIDENCE',
            'EVIDENCE → BELIEF',
            'BELIEF → FRONTIER',
            'FRONTIER → SPACE',
        ]
        positions = []
        for label in labels:
            self.assertIn(label, app)
            positions.append(app.index(label))
        self.assertEqual(positions, sorted(positions))

    def test_wide_screen_story_chapters_are_explicit_without_changing_mobile_order(self):
        app = self.read('wake/assets/app.js')
        css = self.read('wake/assets/style.css')
        expected = [
            ('ops-now', '01', 'NOW'),
            ('ops-pressure', '02', 'PRESSURE'),
            ('ops-context', '03', 'MEMORY'),
            ('ops-evidence', '04', 'EVIDENCE'),
            ('ops-beliefs', '05', 'BELIEF'),
            ('ops-horizon', '06', 'FRONTIER'),
            ('ops-matrix', '07', 'SPACE'),
        ]
        positions = []
        for target, chapter, name in expected:
            marker = f'id="{target}" data-story-chapter="{chapter}" data-story-name="{name}"'
            self.assertIn(marker, app)
            positions.append(app.index(marker))
        self.assertEqual(positions, sorted(positions))
        self.assertIn('.ops-story-chapter{position:relative}', css)
        self.assertIn('@media(min-width:1600px){', css)
        self.assertIn('content:attr(data-story-chapter) " · " attr(data-story-name)', css)

    def test_metrics_story_chapters_support_direct_routes_from_other_views(self):
        app = self.read('wake/assets/app.js')
        self.assertIn("if(page==='metrics'){", app)
        self.assertIn("document.getElementById(selected)", app)
        self.assertIn("scrollIntoView({behavior:'auto',block:'start'})", app)
        self.assertIn("const targetedMetrics=/^#metrics\\/[^/]+/.test(location.hash)", app)
        self.assertIn("if(!targetedMetrics)resetPageScroll()", app)

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
