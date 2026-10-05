# =============================================================================
# EXPERIMENT — the offline measurement harness. Deterministic fixtures isolate architectural claims from live-provider variability. Measurements describe observed behavior; they do not become governance merely because a test reports them.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# The architecture is intentionally explicit.  A future human or AI maintainer
# should be able to follow authority from input, through validation, to durable
# record without relying on folklore.  Comments explain why boundaries exist,
# what failure means, and which tempting shortcuts would weaken accountability.
# =============================================================================

"""Executable claims, isolated state, deterministic fixtures. Zero API calls."""

import json
from pathlib import Path
import subprocess
import sys
import time

from .audit import verify_history
from .authority import open_authoritative_store
from .engine import Engine
from .governance import require
from .providers import Fixture
from .report import atomic_write, export
from .event_format import canonical, now

def run_experiment(directory, cycles=100, output="site"):
    root = Path(directory).resolve()
    require(cycles >= 100 and cycles <= 1000, "Use 100–1000 cycles for the longitudinal experiment")
    require(not (root / "wake.sqlite").exists() and not (root / "wake.sqlite3").exists(),
            "Experiment requires a new data directory; existing state is never erased")
    root.mkdir(parents=True, exist_ok=True)
    calls = []
    def cli(*args, expected=0, data_dir=root):
        started = time.perf_counter()
        result = subprocess.run([sys.executable, "-m", "wake", "--data", str(data_dir), *args],
                                capture_output=True, text=True, timeout=90)
        elapsed = time.perf_counter() - started
        require(result.returncode == expected, f"Experiment command {args} failed: {result.stderr or result.stdout}")
        calls.append({"arguments": list(args), "exit_code": result.returncode,
                      "elapsed_seconds": round(elapsed, 3)})
        return json.loads(result.stdout) if result.stdout.strip() else None

    cli("init")
    cli("observe", "--source", "fixture:sensor", "--text", "Synthetic baseline: sensor reading 10, tolerance 9–11.")
    for n in range(1, cycles + 1):
        if n == 5:
            cli("observe", "--source", "fixture:sensor", "--text", "Synthetic second measurement: sensor reading 10.2, tolerance 9–11.")
        if n == 10:
            cli("observe", "--source", "fixture:sensor", "--text", "Synthetic counterexample: sensor reading 17, outside tolerance 9–11.")
        cli("wake", "--provider", "fixture", "--model", "fixture-a" if n % 2 else "fixture-b")
        if n % 25 == 0:
            wake_timings = [call["elapsed_seconds"] for call in calls if call["arguments"][0] == "wake"]
            recent = wake_timings[-25:]
            print(
                f"Experiment: {n}/{cycles} fresh cycles committed; "
                f"latest={wake_timings[-1]:.3f}s "
                f"recent25_avg={sum(recent) / len(recent):.3f}s "
                f"all_avg={sum(wake_timings) / len(wake_timings):.3f}s.",
                file=sys.stderr,
                flush=True,
            )

    engine = Engine(root, store=open_authoritative_store(root, allow_initialize=True))
    s = engine.store.load()
    checks = {}
    starts = [e for e in engine.store.events() if e["kind"] == "invocation_started"]
    checks["fresh_sessions"] = {"passed": all(e["payload"]["request"]["context"]["version"] == i for i,e in enumerate(starts)),
                                "detail": "Each cycle launches and exits a separate interpreter; durable context version increases by one."}
    commitments = list(s["commitments"].values())
    fulfilled = [c for c in commitments if c["status"] == "fulfilled"]
    open_handoffs = [c for c in commitments if c["status"] == "open"]
    checks["commitment_handoff"] = {
        "passed": (
            len(open_handoffs) == 1
            and len(fulfilled) == len(commitments) - 1
            and all(c["created_by"] != c["resolved_by"] for c in fulfilled)
        ),
        "count": len(fulfilled),
        "total_created": len(commitments),
        "open_count": len(open_handoffs),
        "detail": (
            "Fresh invocations inherit obligations without another human reminder; "
            "forced Attention shifts preserve them unchanged until an eligible later shift."
        ),
    }
    beliefs = [e["payload"]["proposal"]["actions"] for e in engine.store.events() if e["kind"] == "accepted"]
    lifecycle = [a for actions in beliefs for a in actions if a["type"] == "belief"]
    lifecycle_statuses = [a["status"] for a in lifecycle]
    retained_evidence = list(s["beliefs"]["sensor"]["evidence"])
    checks["evidence_lifecycle"] = {
        "passed": lifecycle_statuses == ["active", "active", "retracted"] and len(retained_evidence) == 3,
        "statuses": lifecycle_statuses,
        "retained_evidence_count": len(retained_evidence),
        "retained_evidence": retained_evidence,
        "detail": "Baseline claim, new supporting measurement, then counterexample and retraction; all citations retained.",
    }
    checks["longitudinal"] = {"passed": s["version"] == cycles, "accepted_cycles": s["version"]}

    # Controlled intervention: identical backed-up state, a single human focus change.
    branch = root / "causal-branch"
    engine.store.backup(branch / "wake.sqlite")
    cli("focus", "evidence quality", "--reason", "Controlled intervention; change persisted focus only.", data_dir=branch)
    cli("wake", "--provider", "fixture", "--model", "fixture-a", data_dir=branch)
    branch_engine = Engine(branch, store=open_authoritative_store(branch, allow_initialize=True))
    after = branch_engine.store.load()["journal"][-1]["summary"]
    control = root / "causal-control"
    engine.store.backup(control / "wake.sqlite")
    cli("wake", "--provider", "fixture", "--model", "fixture-a", data_dir=control)
    control_engine = Engine(control, store=open_authoritative_store(control))
    control_summary = control_engine.store.load()["journal"][-1]["summary"]
    checks["causal_state"] = {"passed": "evidence quality" in after and "evidence quality" not in control_summary and after != control_summary,
                              "control": control_summary, "intervention": after,
                              "detail": "Identical state copies, same provider, same next cycle. Only persisted focus differs."}
    export(branch_engine.store, branch / "export")
    export(control_engine.store, control / "export")
    branch_engine.store.close()
    control_engine.store.close()

    # Try an explicitly unauthorized model action. It must become a rejected audit event.
    with engine.store.lock():
        inv, request = engine.start("fixture", "adversarial-fixture")
        proposal = json.loads(Fixture().propose(request)[0])
        proposal["actions"].append({"type": "change_rules", "allow_everything": True})
        result = engine.finish(inv, json.dumps(proposal))
        checks["invalid_transition"] = {"passed": result["status"] == "rejected" and engine.store.load()["version"] == cycles,
                                         "reason": result["reason"], "invocation": inv}
    engine.store.close()

    # SIGKILL-equivalent immediate exits at two distinct durable boundaries.
    # Wake reconstructs from its governed event log directly, so there is no
    # second mutable projection cache to corrupt or repair in this experiment.
    cli("wake", "--provider", "fixture", "--crash-at", "after-start", expected=85)
    cli("recover")
    cli("wake", "--provider", "fixture", "--crash-at", "during-commit", expected=86)
    cli("recover")
    engine = Engine(root, store=open_authoritative_store(root, allow_initialize=True))
    recovered = engine.store.load()
    checks["recovery"] = {"passed": recovered["version"] == cycles and recovered["beliefs"] == s["beliefs"] and recovered["commitments"] == s["commitments"] and
                          sum(i["status"] == "recovered" for i in recovered["invocations"].values()) == 2,
                          "detail": "After-start death and pre-commit process death recover from wake.kernel authority without changing accepted WAKE state."}
    export(engine.store, output)
    replayed, head = verify_history(Path(output) / "events.jsonl", (Path(output) / "head.txt").read_text())
    checks["audit_reconstruction"] = {"passed": canonical(replayed) == canonical(recovered), "head": head,
                                       "detail": "Observer reconstructs exact objective, beliefs, commitments, evidence, journal and invocations using JSONL alone."}
    require(all(c["passed"] for c in checks.values()), f"Experiment checks failed: {checks}")
    result = {"schema": 1, "generated": now(), "mode": "deterministic fixture simulation", "api_calls": 0,
              "cycles": cycles, "fresh_processes": sum(c["arguments"][0] == "wake" for c in calls),
              "checks": checks, "commands": calls,
              "limitations": ["No live model comprehension tested.", "Evidence references are validated; semantic truth is not.",
                              "Single filesystem writer; quota accounting does not span separate state directories.",
                              "Hash chain requires an independently retained head to detect total rewrites or truncation."]}
    atomic_write(root / "experiment.json", json.dumps(result, indent=2))
    export(engine.store, output, result)
    engine.store.close()
    return result
