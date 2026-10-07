"""WAKE domain event projection semantics.

This module owns deterministic WAKE state initialization and event reduction.
It contains no database authority. Both the wake application and the retired
legacy SQLite compatibility Store use the same semantics so migration cannot
fork domain meaning.
"""

from .event_format import digest
from .governance import Rejected, require, transition


def _normalize_legacy_attention_state(state):
    """Map retired attention field spellings into the current derived projection."""
    if "attention" not in state and "squirrel" in state:
        state["attention"] = state.pop("squirrel")
    else:
        state.pop("squirrel", None)
    for invocation in state.get("invocations", {}).values():
        if "attention" not in invocation and "squirrel" in invocation:
            invocation["attention"] = invocation.pop("squirrel")
        else:
            invocation.pop("squirrel", None)
    return state


def empty():
    return {"version": 0, "objective": "", "focus": "continuity", "beliefs": {},
            "commitments": {}, "evidence": {}, "journal": [], "posts": {},
            "invocations": {}, "pending": None, "attention": {"counters": {}, "deferred": {}},
            "acquisition": {}, "representations": {}}


# ---------------------------------------------------------------------------


# STEP: reduce_event


#


# This step exists as an explicit seam so its behavior can be


# inspected, tested, and replaced without giving a model hidden authority.


# Inputs should already belong to the layer named above; outputs remain data


# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


def reduce_event(state, event, historical=False):
    p, kind = event["payload"], event["kind"]
    if kind == "initialized":
        require(not state["objective"], "Duplicate initialization")
        state["objective"] = p["objective"]
    elif kind == "charter_adopted":
        require(not state.get("charter"), "Charter is already established")
        state.update(charter=p["mission"], pet_name=p["pet_name"], projects={}, notebooks={}, research={})
        # Older charter events predate configurable topics. Keep their replayed
        # projection byte-for-byte compatible; initialize records adoption later.
        if "topics" in p:
            state["research_topics"] = p["topics"]
        if "topic_colors" in p:
            state["topic_colors"] = p["topic_colors"]
    elif kind == "pet_renamed":
        require(state.get("charter"), "WAKE must exist before it can be renamed")
        require(p["pet_name"] != state.get("pet_name"), "Pet already has this name")
        state["pet_name"] = p["pet_name"]
    elif kind == "research_topics_changed":
        require(state.get("charter"), "Research charter is not enabled")
        require(isinstance(p.get("topics"), list) and p["topics"], "Research topics cannot be empty")
        state["research_topics"] = p["topics"]
        if "topic_colors" in p:
            state["topic_colors"] = p["topic_colors"]
    elif kind == "experimental_regime_adopted":
        # This is an operator intervention, not an editable preference.  Older
        # histories deliberately lack this key: replay must not pretend their
        # wakes ran under a regime that did not exist yet.
        from .experimental import validate
        validate(p["controls"])
        require(p.get("actor") == "operator", "Only an operator may adopt an experimental regime")
        state["experimental"] = {key: p[key] for key in
                                 ("id", "controls", "actor", "reason", "adopted_at", "event_seq",
                                  "effective_from_version", "effective_seconds")}
        state["temporal"] = {"anchor_time": p["adopted_at"],
                             "anchor_version": p["effective_from_version"],
                             "anchor_seq": event["seq"],
                             "effective_seconds": p["effective_seconds"]}
    elif kind == "temporal_observed":
        require(state.get("experimental"), "Temporal receipt requires an experimental regime")
        require(p["regime_id"] == state["experimental"]["id"], "Temporal receipt regime mismatch")
        state["temporal"] = {"anchor_time": p["observed_at"], "anchor_version": state["version"],
                             "anchor_seq": event["seq"], "effective_seconds": p["effective_seconds_total"]}
    elif kind == "research_collected":
        require(p.get("status") in ("collected", "failed", "superseded"), "Invalid research collection status")
        if p["id"] in state.get("research", {}):
            state["research"][p["id"]].update(status=p["status"], evidence=p.get("evidence"))
    elif kind == "project_adopted":
        # Legacy operator receipt retained for replay of historical fixtures;
        # providers cannot emit this event and normal project changes remain
        # governed inside accepted proposals.
        require(p["id"] not in state.get("projects", {}), "Project already exists")
        state.setdefault("projects", {})[p["id"]] = {**p, "type": "project",
            "created_version": state["version"], "updated_version": state["version"]}
    elif kind == "acquisition_assessed":
        require(p["project"] in state.get("projects", {}), "Acquisition receipt needs an existing project")
        summaries = state.setdefault("acquisition", {})
        prior = summaries.get(p["project"], {"no_progress": 0, "routes": []})
        routes = list(dict.fromkeys((prior.get("routes", []) + [p["route"]])))[-4:]
        if p["outcome"] in ("progress", "routing_progress"):
            # A readable source is substantive progress. A new identifier or
            # readable-source candidate is routing progress: it proves the
            # acquisition path is advancing without pretending research matured.
            no_progress = 0
        else:
            no_progress = prior.get("no_progress", 0) + 1
        blocked = no_progress >= 4 and len(routes) >= 2
        source_candidates = list(dict.fromkeys(
            prior.get("source_candidates", []) + p.get("source_candidates", [])
        ))[-12:]
        source_candidate_identities = dict(prior.get("source_candidate_identities", {}))
        source_candidate_identities.update(p.get("source_candidate_identities", {}))
        source_candidate_identities = {
            url: source_candidate_identities[url]
            for url in source_candidates
            if url in source_candidate_identities and source_candidate_identities[url]
        }
        summaries[p["project"]] = {"project": p["project"], "domain": p["domain"],
            "no_progress": no_progress, "routes": routes,
            "capability_blocked": blocked,
            "retry_after_version": state["version"] + 12 if blocked else None,
            "persistent_identifiers": list(dict.fromkeys(prior.get("persistent_identifiers", []) + p.get("persistent_identifiers", [])))[-12:],
            "source_candidates": source_candidates,
            "source_candidate_identities": source_candidate_identities,
            "last_receipt": {k: v for k, v in p.items() if k not in ("project", "domain")}}
    elif kind == "observation":
        require(p["id"] not in state["evidence"], "Duplicate evidence ID")
        state["evidence"][p["id"]] = {**p, "version": state["version"], "time": event["time"]}
    elif kind == "focus_changed":
        state["focus"] = p["focus"]
    elif kind in ("attention_assessed", "squirrel_assessed"):
        # Legacy event spelling is accepted only to replay existing hash-linked history.
        require(state.get("charter"), "Attention requires the research charter")
        require(p["invocation"] in state["invocations"], "Unknown Attention invocation")
        require(state["invocations"][p["invocation"]].get("status") == p["terminal"],
                "Attention receipt must follow its terminal invocation")
        attention = p.get("attention", state.get("attention", {}).get("attention"))
        state["attention"] = {"counters": p["counters"], "deferred": p["deferred"],
                             "last_receipt": {k: v for k, v in p.items()
                                              if k not in ("counters", "deferred", "attention")}}
        if attention:
            state["attention"]["attention"] = attention
    elif kind == "commitment_cancelled":
        item = state["commitments"].get(p["id"])
        require(item is not None and item["status"] == "open", "Only open commitments can be cancelled")
        item.update(status="cancelled", resolution_reason=p["reason"], resolved_by="human")
    elif kind == "invocation_started":
        require(state["pending"] is None and p["id"] not in state["invocations"], "Conflicting invocation")
        require(p["base_version"] == state["version"], "Start version mismatch")
        state["pending"] = p["id"]
        state["invocations"][p["id"]] = {k: v for k, v in p.items() if k != "request"}
        if "attention" not in state["invocations"][p["id"]] and "squirrel" in p:
            state["invocations"][p["id"]]["attention"] = p["squirrel"]
            state["invocations"][p["id"]].pop("squirrel", None)
        state["invocations"][p["id"]].update(status="pending", time=event["time"])
    elif kind == "provider_attempt_started":
        require(state["pending"] == p["id"], "Invocation is not pending")
        item = state["invocations"][p["id"]]
        attempts = item.setdefault("provider_attempts", [])
        require(not any(a["model"] == p["attempt"]["model"] for a in attempts),
                "Model already attempted in this invocation")
        require(not attempts or attempts[-1]["result"] in ("transient_failure", "daily_quota"),
                "Failover requires a transient availability or model-quota failure")
        attempts.append(p["attempt"])
        item.setdefault("provider_requests_sent", 0)
    elif kind == "provider_attempt_finished":
        require(state["pending"] == p["id"], "Invocation is not pending")
        item = state["invocations"][p["id"]]
        attempts = item.get("provider_attempts", [])
        require(attempts and attempts[-1]["result"] == "unknown"
                and attempts[-1]["model"] == p["attempt"]["model"], "Attempt does not match reservation")
        attempts[-1] = p["attempt"]
        item["provider_requests_sent"] += 1
        if p["attempt"]["result"] == "success":
            item["successful_model"] = p["attempt"]["model"]
    elif kind in ("accepted", "rejected", "failed", "deferred", "recovered", "research_planned"):
        require(state["pending"] == p["id"], "Invocation is not pending")
        if kind == "accepted":
            state = transition(state, p["proposal"], p["id"], historical=historical)
            fields = p.get("hash_fields", ["version", "beliefs", "commitments", "journal"])
            require(digest({k: state[k] for k in fields}) == p["result_hash"],
                    "Transition result hash mismatch")
        terminal = {"status": kind, "finished": event["time"], "reason": p.get("reason", "")}
        if "provider_requests_sent" in p:
            terminal["provider_requests_sent"] = p["provider_requests_sent"]
        diagnostics = p.get("metadata", p)
        for key in ("provider_attempts", "skipped_models", "successful_model"):
            if key in diagnostics:
                # Keep a reservation if persistence failed before its result was recorded.
                if key != "provider_attempts" or len(diagnostics[key]) >= len(state["invocations"][p["id"]].get(key, [])):
                    terminal[key] = diagnostics[key]
        if kind == "research_planned":
            terminal["requests"] = p["requests"]
        if "editorial" in p:
            terminal["editorial"] = p["editorial"]
        if "provider_error" in p:
            terminal["provider_error"] = p["provider_error"]
        if "quota_exhausted" in p:
            terminal["quota_exhausted"] = p["quota_exhausted"]
        state["invocations"][p["id"]].update(terminal)
        state["pending"] = None
    else:
        raise Rejected(f"Unknown event kind: {kind}")
    return state


# ---------------------------------------------------------------------------


# OBJECT: IntegrityError


#


# This object groups state/behavior exists as an explicit seam so its behavior can be


# inspected, tested, and replaced without giving a model hidden authority.


# Inputs should already belong to the layer named above; outputs remain data


# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


