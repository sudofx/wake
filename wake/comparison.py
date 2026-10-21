"""Paired behavioral trials on one frozen synthetic record, never operator data.

Real providers use Engine.run and its native reservation/effect/receipt boundary.
Manual replies use the same start/finish contract. Structural checks are kept
separate from human judgments about comprehension and explanation quality.
"""
from copy import deepcopy
from functools import wraps
import fcntl
import hashlib
import json
from pathlib import Path
import subprocess

from .authority import open_authoritative_store
from .engine import DEFAULTS, Engine
from .event_format import canonical, digest, now
from .governance import require
from .providers import Fixture, Gemini
from .report import atomic_write

ARMS = {"rich": "shadow", "active": "active"}
DECISION_ARMS = {"baseline": "active", "recall": "active", "ablation": "active"}
CLAIM = "comparison-sensor"
OBLIGATION = "comparison-review"
CONTRADICTION = "comparison-counterexample"


def _serialized(function):
    """One experiment writer, including the request-budget reservation."""
    @wraps(function)
    def call(output, *args, **kwargs):
        root = Path(output).resolve()
        with (root / "comparison.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                require(False, "Another comparison operation is running; no parallel API trials")
            return function(output, *args, **kwargs)
    return call


def _write(path, value):
    atomic_write(path, json.dumps(value, indent=2, ensure_ascii=False))


def _settings(settings, arm):
    # The same generic reference task is used in both arms. No collection,
    # Attention, matrix sidecar, or fallback inference can confound this trial.
    return {**deepcopy(DEFAULTS),
            **{k: deepcopy(v) for k, v in settings.items() if k in DEFAULTS},
            "objective": "Review inherited sensor claims against recorded measurements; retain provenance and explain revisions.",
            "memory_mode": {**ARMS, **DECISION_ARMS}[arm], "same_wake_research": False,
            "decision_memory_mode": "active" if arm in ("recall", "ablation") else "off",
            "gemini_fallback_models": [], "model_daily_call_limits": {},
            "daily_call_limit": 4, "inquiry_drive_enabled": False}


def create_comparison(output, settings, *, decision_memory=False):
    root = Path(output).resolve()
    require(not root.exists(), "Comparison output must be new; existing records are never replaced")
    root.mkdir(parents=True)
    baseline = root / "baseline"
    cfg = _settings(settings, "rich")
    engine = Engine(baseline, cfg, store=open_authoritative_store(baseline, allow_initialize=True))
    try:
        with engine.store.lock():
            engine.initialize()
            engine.observe("Synthetic baseline: sensor reading 10, tolerance 9–11. This is controlled test data, not scientific evidence.",
                           "fixture:sensor", evidence_id="comparison-baseline")
            invocation, request = engine.start("manual", "operator-seeded-comparison")
            actions = [dict(type="belief", id=CLAIM,
                            statement="The simulated sensor remains within its stated tolerance of 9–11.",
                            confidence=0.75, status="active", evidence=["comparison-baseline"],
                            reason="The baseline reading is 10; this provisional claim needs later measurement review.",
                            falsifier="Any recorded sensor reading outside 9–11."),
                       dict(type="commit", id=OBLIGATION,
                            task="Review the next sensor measurement against the inherited tolerance claim and explain any required correction with measurement provenance.",
                            due_cycle=2, reason="Carry the review obligation across fresh model calls.")]
            result = engine.finish(invocation, canonical(dict(base_version=request["context"]["version"],
                                   title="Seed a controlled comparison", summary="A provisional claim and an inherited obligation.", actions=actions)))
            require(result["status"] == "accepted", "Comparison seed failed governance")
            engine.observe("Synthetic counterexample: sensor reading 17, outside the tolerance of 9–11. This measured result contradicts the earlier reading-based claim.",
                           "fixture:sensor", evidence_id=CONTRADICTION)
            head = engine.store.head()
            state_hash = digest(engine.store.load())
            engine.store.backup(root / "baseline.sqlite")
        try:
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        except (OSError, subprocess.CalledProcessError):
            commit = None
        manifest = {"schema_version": 1, "created": now(), "source_commit": commit,
                    "source_tree_clean": _source_clean(), "baseline_head": head,
                    "baseline_state_hash": state_hash,
                    "baseline_sha256": hashlib.sha256((root / "baseline.sqlite").read_bytes()).hexdigest(),
                    "scenario": "controlled synthetic contradiction and inherited obligation",
                    "arms": DECISION_ARMS if decision_memory else ARMS, "settings": cfg, "trials": [],
                    "maximum_api_requests": 4,
                    "human_rubric": ["Does the explanation identify the conflict between 10 and 17?",
                                     "Does the revised claim stay within the measurements' scope?",
                                     "Does it explain the inherited obligation's completion rather than merely repeat an ID?"],
                    "limitations": ["One synthetic case cannot establish general research quality or behavioral equivalence.",
                                    "Model identity in manual trials is human-attested.",
                                    "Comparison request budget is local to this experiment; do not run parallel live experiments on the same API project.",
                                    "Structural checks do not grade explanation quality."]}
        # A commit alone cannot reproduce an uncommitted candidate. Preserve
        # the actual package used by this trial, excluding caches and secrets.
        package = Path(__file__).resolve().parent
        source_hashes = {}
        for path in sorted(package.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            relative = Path("wake") / path.relative_to(package)
            target = root / "source" / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            data = path.read_bytes()
            target.write_bytes(data)
            source_hashes[str(relative)] = hashlib.sha256(data).hexdigest()
        manifest["source_files"] = source_hashes
        manifest["source_digest"] = digest(source_hashes)
        _write(root / "comparison.json", manifest)
        return manifest
    finally:
        engine.store.close()


def _source_clean():
    try:
        return not bool(subprocess.check_output(["git", "status", "--porcelain"], text=True).strip())
    except (OSError, subprocess.CalledProcessError):
        return None


def _load(root):
    root = Path(root).resolve()
    manifest = json.loads((root / "comparison.json").read_text())
    require(hashlib.sha256((root / "baseline.sqlite").read_bytes()).hexdigest() == manifest["baseline_sha256"],
            "Frozen baseline changed; refusing comparison")
    return root, manifest


def _trial(root, manifest, arm, model):
    require(arm in manifest["arms"] and isinstance(model, str) and 0 < len(model) <= 120, "Invalid comparison arm or model")
    key = digest({"arm": arm, "model": model})[:16]
    require(not any(t["key"] == key for t in manifest["trials"]), "This arm/model already has a trial; preserve it and create another experiment for repeats")
    directory = root / "trials" / key
    directory.mkdir(parents=True)
    (directory / "wake.sqlite").write_bytes((root / "baseline.sqlite").read_bytes())
    engine = Engine(directory, _settings(manifest["settings"], arm), store=open_authoritative_store(directory))
    engine._decision_memory_ablation = arm == "ablation"
    require(engine.store.head() == manifest["baseline_head"] and digest(engine.store.load()) == manifest["baseline_state_hash"],
            "Trial did not start from the frozen baseline")
    trial = {"key": key, "arm": arm, "model": model, "starting_head": manifest["baseline_head"],
             "starting_state_hash": manifest["baseline_state_hash"], "status": "prepared", "api_requests": 0,
             "human_assessment": None}
    manifest["trials"].append(trial)
    # Persist intent before inference so interrupted attempts remain visible.
    _write(root / "comparison.json", manifest)
    return engine, trial, directory


@_serialized
def prepare_trial(output, arm, model):
    root, manifest = _load(output)
    engine, trial, directory = _trial(root, manifest, arm, model)
    try:
        with engine.store.lock():
            invocation, request = engine.start("manual", model)
            trial.update(invocation=invocation, request_hash=digest(request),
                         delivered_chars=len(canonical(request)), identity="human-attested")
            _write(directory / "request.json", {"invocation": invocation, **request})
        _write(root / "comparison.json", manifest)
        return {**trial, "request": str(directory / "request.json")}
    finally:
        engine.store.close()


def score_trial(engine, invocation):
    state = engine.store.load()
    item = state["invocations"][invocation]
    belief = state["beliefs"][CLAIM]
    obligation = state["commitments"][OBLIGATION]
    events = engine.store.events()
    accepted = next((e for e in reversed(events) if e["kind"] == "accepted" and e["payload"]["id"] == invocation), None)
    actions = accepted["payload"]["proposal"]["actions"] if accepted else []
    checks = {"governance_accepted": item["status"] == "accepted",
              "inherited_claim_retracted": belief["status"] == "retracted" and belief["confidence"] == 0,
              "contradiction_cited": any(a.get("type") == "belief" and a.get("id") == CLAIM and CONTRADICTION in a.get("evidence", []) for a in actions),
              "inherited_obligation_resolved": obligation["status"] == "fulfilled" and obligation.get("resolved_by") == invocation,
              "measurement_used_for_resolution": any(a.get("type") == "resolve" and a.get("id") == OBLIGATION and CONTRADICTION in a.get("evidence", []) for a in actions),
              "original_observation_retained": "comparison-baseline" in state["evidence"] and "comparison-baseline" in belief["evidence"]}
    recall = item.get("context_delivery", {}).get("decision_memory")
    memory_evaluation = None
    if recall is not None:
        terminal = next((e for e in reversed(events) if e["kind"] in ("accepted", "rejected", "failed")
                         and e["payload"].get("id") == invocation), {})
        memory_evaluation = {"selection": recall, "use": terminal.get("payload", {}).get("metadata", {}).get("decision_memory_use"),
                             "decision_changed": None, "outcome_improved": None}
    return {"checks": checks, "all_structural_checks_passed": all(checks.values()),
            **({"decision_memory": memory_evaluation} if memory_evaluation is not None else {}),
            "explanation": belief.get("reason"), "terminal_status": item["status"],
            "terminal_head": engine.store.head(), "human_assessment": None}


@_serialized
def complete_trial(output, key, reply_file):
    root, manifest = _load(output)
    trial = next((t for t in manifest["trials"] if t["key"] == key), None)
    require(trial is not None and trial["status"] == "prepared" and trial.get("identity") == "human-attested",
            "No pending manual comparison trial")
    file = Path(reply_file)
    require(file.stat().st_size <= 256000, "Reply exceeds the normal manual boundary")
    raw = file.read_text()
    directory = root / "trials" / key
    engine = Engine(directory, _settings(manifest["settings"], trial["arm"]), store=open_authoritative_store(directory))
    try:
        with engine.store.lock():
            invocation = trial["invocation"]
            require(engine.store.load()["pending"] == invocation, "Manual trial is not pending")
            _write(directory / "reply.json", {"raw": raw, "sha256": hashlib.sha256(raw.encode()).hexdigest()})
            result = engine.finish(invocation, raw, {"identity": "human-attested"})
            trial.update(status=result["status"], evaluation=score_trial(engine, invocation))
        _write(root / "comparison.json", manifest)
        return trial
    finally:
        engine.store.close()


@_serialized
def run_trial(output, arm, model, *, fixture=False):
    root, manifest = _load(output)
    if not fixture:
        reserved = sum(t.get("reserved_api_requests", 0) for t in manifest["trials"])
        require(reserved < manifest["maximum_api_requests"], "Comparison API request ceiling reached; no call sent")
        # Validate the selected model/credential before recording a trial.
        provider = Gemini(_settings(manifest["settings"], arm), model)
    else:
        provider = Fixture(model)
    engine, trial, directory = _trial(root, manifest, arm, model)
    try:
        trial["reserved_api_requests"] = 0 if fixture else 1
        trial["identity"] = "deterministic fixture" if fixture else "API-attested Gemini"
        _write(root / "comparison.json", manifest)
        result = engine.run(provider)
        invocation = result["id"]
        item = engine.store.load()["invocations"][invocation]
        trial.update(status=result["status"], invocation=invocation,
                     api_requests=item.get("provider_requests_sent", 0),
                     provider_attempts=item.get("provider_attempts", []),
                     request_hash=item.get("request_hash"),
                     delivered_chars=item.get("context_delivery", {}).get("delivered_request_chars"),
                     evaluation=score_trial(engine, invocation))
        trial["behavioral_evidence"] = not fixture and any(
            attempt.get("result") == "success" for attempt in trial["provider_attempts"])
        _write(root / "comparison.json", manifest)
        return trial
    finally:
        engine.store.close()


def comparison_report(output):
    root, manifest = _load(output)
    trials = deepcopy(manifest["trials"])
    for trial in trials:
        if trial.get("identity") == "API-attested Gemini":
            trial["behavioral_evidence"] = any(
                attempt.get("result") == "success" for attempt in trial.get("provider_attempts", []))
    attempted_pairs = sorted({t["model"] for t in trials if all(any(
        other["model"] == t["model"] and other["arm"] == arm and other.get("evaluation")
        for other in trials) for arm in manifest["arms"])})
    paired_models = sorted({t["model"] for t in trials if all(any(
        other["model"] == t["model"] and other["arm"] == arm and other.get("evaluation")
        and (other.get("behavioral_evidence") or
             (other.get("identity") == "human-attested" and other["status"] in ("accepted", "rejected")))
        for other in trials) for arm in manifest["arms"])})
    return {"schema_version": 1, "baseline_head": manifest["baseline_head"],
            "source_digest": manifest.get("source_digest"),
            "scenario": manifest["scenario"], "paired_models": paired_models,
            "attempted_pairs": attempted_pairs,
            "api_requests": sum(t.get("api_requests", 0) for t in trials),
            "trials": trials, "human_rubric": manifest["human_rubric"],
            "behavioral_equivalence_established": False,
            "limitations": manifest["limitations"]}


def evaluate_decision_memory(fixture_file):
    """A/B/C mechanical evaluation on frozen labeled projections; no inference.

    Native baseline backups/manual/model trials above remain the behavioral
    comparison path. This report never mistakes fixture selection for model use.
    """
    from time import perf_counter
    from .decision_memory import decision_context, rank_candidates, build_capsule, policy_config, validate_capsule, KINDS
    from .providers import provider_input_chars
    from .export_cache import code_fingerprint
    fixtures = json.loads(Path(fixture_file).read_text())
    require(fixtures.get("schema") == "decision-memory-fixtures@1", "Unknown decision-memory fixture schema")
    rows = []
    for case in fixtures["cases"]:
        state = deepcopy(case["state"])
        frozen = digest(state)
        head = digest({"synthetic_projection": state})
        before = perf_counter()
        decision = decision_context(state)
        policy = policy_config(case.get("policy"))
        plan = rank_candidates(state, case["retrieval"], decision, policy)
        context = {"version": state["version"], "evidence": list(state.get("evidence", {}).values()),
                   "beliefs": list(state.get("beliefs", {}).values()),
                   "commitments": [c for c in state.get("commitments", {}).values() if c.get("status") == "open"]}
        # The canonical eligibility owner is shared with live retrieval. These
        # fixtures supply exact prose, so no network/source fetch is necessary.
        eligible = [i for i in state.get("evidence", {}) if Engine.durable_notebook_source_payload(None, state, i) is not None]
        result = build_capsule(state, head, plan, context, eligible_source_ids=eligible)
        capsule = result["capsule"]
        require(capsule is not None, "Fixture capsule metadata exceeds its declared budget")
        validate_capsule(capsule, state, head)
        repeat = build_capsule(state, head, rank_candidates(state, case["retrieval"], decision, policy),
                               context, eligible_source_ids=eligible)
        selected = capsule["selected_memories"]
        ablate = next(({"kind": m["kind"], "id": m["id"]} for m in selected if m["kind"] != "commitment"), None)
        control = build_capsule(state, head, plan, context, eligible_source_ids=eligible, ablate=ablate)
        ids = {m["id"] for m in selected}
        candidates = {m["id"] for m in plan["candidates"]}
        required, irrelevant = set(case.get("required_ids", [])), set(case.get("irrelevant_ids", []))
        protected = deepcopy(context["commitments"])
        baseline_request = {"system": "Controlled offline fixture", "context": context}
        recall_request = {**baseline_request, "context": {**context, "decision_state_capsule": capsule}}
        ablation_request = {**baseline_request, "context": {**context, "decision_state_capsule": control["capsule"]}}
        sizes = {name: provider_input_chars(r) for name, r in (("baseline", baseline_request), ("recall", recall_request), ("ablation", ablation_request))}
        missing_provenance = sum(digest(state[KINDS[m["kind"]]][m["id"]]) != m["record_hash"] for m in selected)
        eligibility_errors = sum(m["kind"] == "evidence" and state["evidence"][m["id"]].get("actor") == "collector"
                                 and m["id"] not in eligible for m in selected)
        checks = {"required_selected": required <= ids, "irrelevant_excluded": not bool(irrelevant & ids),
                  "deterministic": canonical(result) == canonical(repeat),
                  "state_unchanged": digest(state) == frozen, "protected_obligations_retained": context["commitments"] == protected,
                  "provenance_exact": missing_provenance == 0, "source_eligibility_preserved": eligibility_errors == 0,
                  "capsule_budget": len(canonical(capsule)) <= policy["capsule_chars"],
                  "provider_budget": max(sizes.values()) <= 16000,
                  "ablation_removes_selected": ablate is None or ablate not in [{"kind": m["kind"], "id": m["id"]} for m in (control["capsule"] or {}).get("selected_memories", [])]}
        rows.append({"scenario": case["name"], "starting_state_hash": frozen, "synthetic_source_head": head,
                     "selected": [{k: m[k] for k in ("kind", "id", "selection_reasons")} for m in selected],
                     "exclusions": result["exclusions"], "omissions": capsule["omissions"],
                     "candidate_recall_coverage": len(required & candidates) / max(1, len(required)),
                     "labeled_relevant_selection_rate": len(required & ids) / max(1, len(required)),
                     "labeled_irrelevant_selection_count": len(irrelevant & ids),
                     "missing_provenance_count": missing_provenance, "incorrect_source_eligibility_count": eligibility_errors,
                     "missing_evidence_root_count": sum(len(m["missing_roots"]) for m in selected),
                     "provider_input_chars": sizes, "capsule_chars": len(canonical(capsule)),
                     "computation_ms": round((perf_counter() - before) * 1000, 3),
                     "checks": checks, "passed": all(checks.values()),
                     "cross_topic_selections": sum("cross_topic_hypothesis_only" in m["selection_reasons"] for m in selected)})
    return {"schema": "decision-memory-evaluation@1", "fixture_digest": digest(fixtures),
            "source_fingerprint": code_fingerprint(), "selection_policy": policy_config(),
            "scenario_count": len(rows), "passed": all(r["passed"] for r in rows), "scenarios": rows,
            "api_calls": 0, "model_responses": 0, "behavioral_quality_measured": False,
            "provenance_metric_boundary": "missing_provenance_count measures delivered record identity/hash errors; missing_evidence_root_count separately reports unresolved references, including intentionally incomplete fixtures.",
            "decision_changed": None, "outcome_improved": None,
            "limitations": ["Synthetic projection labels measure selection, not scientific correctness or model comprehension.",
                            "Capsule ablation does not remove protected or already delivered baseline information.",
                            "No measured long-term adaptive improvement; no weights or policy change automatically."]}
