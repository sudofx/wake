# =============================================================================
# ENGINE — the orchestration layer. A wake is one disposable shift: reconstruct durable state, select bounded context, reserve/record the invocation, call a provider, then ask governance whether the proposal may become history. The engine coordinates these steps but never substitutes its own judgment for governance.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# Read this file as part of a chain of custody.  WAKE✳︎ deliberately separates
# disposable cognition from durable authority.  Comments therefore explain not
# only what a function does, but why its boundary exists and what a refactor must
# not accidentally collapse.  Prefer explicit receipts, deterministic state
# transitions, and replayable facts over convenient hidden behavior.
# =============================================================================

"""One fresh process, one bounded proposal, one atomic decision."""

from datetime import datetime
import json
import os
from pathlib import Path
import re
import tomllib
import uuid
from zoneinfo import ZoneInfo

from .governance import Rejected, require, text, transition
from .providers import (
    SYSTEM, DailyQuotaExceeded, ProviderRequestError, TransientProviderError,
    is_free_tier_daily_quota, retractable_quotes, schema_for_context,
)
from .scheduling import charged_request_slots
from .retrieval import build_retrieval_shadow
from .store import Store, canonical, digest
from .trust import build_trust_compacts_shadow


INQUIRY_DRIVE_MIN_CYCLES = 20


DEFAULTS = {"timezone": "America/Los_Angeles", "objective": "Test durable continuity under mechanical governance.",
            "provider": "gemini", "model": "gemini-2.5-flash", "daily_call_limit": 20, "model_daily_call_limits": {},
            "max_context_chars": 48000, "max_output_tokens": 4096, "timeout_seconds": 60,
            "free_tier_confirmed": False, "gemini_fallback_models": [],
            "inquiry_drive_enabled": False, "research_topics_file": "research-topics.toml"}
# ---------------------------------------------------------------------------
# STEP: _topics
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
# ---------------------------------------------------------------------------


def _topics(settings, config_path=None):
    topics = settings.get("research_topics") if config_path is None else None
    filename = settings.get("research_topics_file")
    require(filename, "research_topics_file is required when the research charter is enabled")
    if config_path is not None:
        topic_path = Path(filename)
        if not topic_path.is_absolute():
            topic_path = config_path.parent / topic_path
        require(topic_path.is_file(), f"Research topics file not found: {topic_path}")
        topics = tomllib.loads(topic_path.read_text()).get("topics")
    require(isinstance(topics, list) and 1 <= len(topics) <= 24,
            "Research topics must contain 1–24 entries")
    normalized = []
    for item in topics:
        require(isinstance(item, dict) and set(item) == {"id", "label", "query"},
                "Each research topic needs exactly id, label, and query")
        require(isinstance(item["id"], str) and re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", item["id"]),
                "Research topic IDs must use letters, digits, underscores or hyphens")
        text(item["label"], "Research topic label", 120)
        text(item["query"], "Research topic query", 200)
        normalized.append({key: item[key] for key in ("id", "label", "query")})
    require(len({item["id"] for item in normalized}) == len(normalized), "Research topic IDs must be unique")
    return normalized
# ---------------------------------------------------------------------------
# STEP: config
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------


def config(path="wake.toml"):
    config_path = Path(path)
    result = {**DEFAULTS, **(tomllib.loads(config_path.read_text()) if config_path.exists() else {})}
    require(type(result["daily_call_limit"]) is int and 1 <= result["daily_call_limit"] <= 500,
            "daily_call_limit must be between 1 and 500")
    model_limits = result.get("model_daily_call_limits", {})
    require(isinstance(model_limits, dict), "model_daily_call_limits must be a table")
    for model, limit in model_limits.items():
        require(isinstance(model, str) and re.fullmatch(r"[a-zA-Z0-9._-]+", model), "Invalid quota model name")
        require(type(limit) is int and 1 <= limit <= 500, "Model daily call limits must be between 1 and 500")
    require(result["timezone"] == "America/Los_Angeles", "Daily quota timezone must be America/Los_Angeles")
    for key, low, high in (("max_context_chars", 4000, 64000), ("max_output_tokens", 256, 8192), ("timeout_seconds", 1, 120)):
        require(type(result[key]) is int and low <= result[key] <= high, f"Invalid {key}")
    require(type(result["inquiry_drive_enabled"]) is bool,
            "inquiry_drive_enabled must be true or false")
    text(result["objective"], "Objective", 2000)
    if result.get("mission"):
        text(result["mission"], "Research mission", 3000)
        text(result.get("pet_name", "WAKE✳"), "Pet name", 80)
        notes = result.get("editorial_notes", [])
        require(isinstance(notes, list) and len(notes) <= 8,
                "editorial_notes must be a list of at most 8 notes")
        for note in notes:
            text(note, "Editorial note", 1200)
        require(result.get("research_topics_file"), "research_topics_file is required when mission is configured")
        result["research_topics"] = _topics(result, config_path)
    return result
# ---------------------------------------------------------------------------
# OBJECT: Engine
#
# This object groups state/behavior exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.
# ---------------------------------------------------------------------------


class Engine:
    # ---------------------------------------------------------------------------
    # STEP: __init__
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
    # ---------------------------------------------------------------------------
    def __init__(self, directory="data", settings=None):
        self.config = settings or config()
        if self.config.get("mission"):
            if not self.config.get("research_topics"):
                filename = self.config.get("research_topics_file")
                require(filename, "research_topics_file is required when the research charter is enabled")
                topic_path = Path(filename)
                require(topic_path.is_file(), f"Research topics file not found: {topic_path}")
                self.config["research_topics"] = _topics(self.config, Path("wake.toml"))
            else:
                self.config["research_topics"] = _topics(self.config)
        self.store = Store(directory)
    # ---------------------------------------------------------------------------
    # STEP: initialize
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def initialize(self):
        state, _ = self.store.replay()
        if not state["objective"]:
            state = self.store.append("initialized", {"objective": self.config["objective"], "governance": 1})
        if self.config.get("mission") and not state.get("charter"):
            state = self.store.append("charter_adopted", {"mission": self.config["mission"],
                                     "pet_name": self.config.get("pet_name", "WAKE✳"),
                                     "topics": self.config["research_topics"], "actor": "operator"})
        # A branding change is part of the durable identity. Record it as an
        # auditable event instead of rewriting the original charter or history.
        desired_name = self.config.get("pet_name", "WAKE✳")
        if state.get("charter") and state.get("pet_name") != desired_name:
            state = self.store.append("pet_renamed", {"pet_name": desired_name, "actor": "operator"})
        desired_topics = self.config.get("research_topics", [])
        if state.get("charter") and state.get("research_topics") != desired_topics:
            self.store.append("research_topics_changed", {"topics": desired_topics, "actor": "operator"})
        return self.store.load(repair=True)
    # ---------------------------------------------------------------------------
    # STEP: recover
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def recover(self, explicit=False):
        state = self.store.load(repair=True)
        if state["pending"]:
            item = state["invocations"][state["pending"]]
            require(explicit or item["provider"] != "manual", "A manual proposal is pending; complete it or explicitly recover")
            state = self.store.append("recovered", {"id": state["pending"],
                                       "reason": "Previous invocation ended without a committed decision; resumed last valid state."})
        return state
    # ---------------------------------------------------------------------------
    # STEP: observe
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def observe(self, content, source, evidence_id=None):
        text(content, "Observation", 8000)
        text(source, "Source", 1000)
        state = self.store.load()
        require(state["pending"] is None, "Finish or recover the pending invocation before adding evidence")
        return self.store.append("observation", {"id": evidence_id or "e-" + uuid.uuid4().hex[:16],
                                                 "source": source, "content": content, "actor": "human"})
    # ---------------------------------------------------------------------------
    # STEP: working_set
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def working_set(self, state):
        """Build a deliberately lossy, traceable shadow of the durable state.

        Shadow mode does not replace the provider context yet. It lets WAKE measure
        what a purpose-conditioned working representation would look like without
        changing live-model behavior before a controlled comparison exists.
        """
        # ---------------------------------------------------------------------------
        # STEP: excerpt
        #
        # This step exists as an explicit seam so its behavior can be
        # inspected, tested, and replaced without giving a model hidden authority.
        # Inputs should already belong to the layer named above; outputs remain data
        # until the next boundary validates or records them. Callers may rely on this contract.
        # ---------------------------------------------------------------------------
        def excerpt(value, limit):
            value = str(value)
            return value if len(value) <= limit else value[:limit - 1] + "…"

        beliefs = []
        for belief in state["beliefs"].values():
            beliefs.append({
                "id": belief["id"],
                "claim": excerpt(belief["statement"], 320),
                "confidence": belief["confidence"],
                "status": belief["status"],
                "why_retained": excerpt(belief["reason"], 220),
                "provenance": list(belief["evidence"]),
            })

        commitments = [{
            "id": item["id"],
            "task": excerpt(item["task"], 320),
            "due_cycle": item["due_cycle"],
            "reason": excerpt(item["reason"], 220),
        } for item in state["commitments"].values() if item["status"] == "open"]

        working = {
            "mode": "shadow",
            "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
            "retrieval_triggers": [
                "material belief revision or retraction",
                "new contradiction or counterevidence",
                "high-consequence decision",
                "request for justification",
                "sign that an excerpt may hide a material distinction",
            ],
            "beliefs": beliefs,
            "open_commitments": commitments,
        }

        if state.get("charter"):
            working["active_projects"] = [{
                "id": project["id"],
                "title": excerpt(project["title"], 160),
                "question": excerpt(project["question"], 320),
                "next_step": excerpt(project["next_step"], 260),
            } for project in state["projects"].values() if project["status"] == "active"]
            working["recent_notebooks"] = [{
                "id": notebook["id"],
                "project": notebook["project"],
                "title": excerpt(notebook["title"], 160),
                "summary": excerpt(notebook["summary"], 320),
                "revision": notebook["revision"],
                "provenance": list(notebook["evidence"]),
            } for notebook in list(state["notebooks"].values())[-6:]]

        return working
    # ---------------------------------------------------------------------------
    # STEP: inquiry_drive_shadow
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def inquiry_drive_shadow(self, state):
        """Score durable research work without granting it any decision authority.

        This is deliberately an observational intervention.  The score is made
        only from auditable record structure, rather than sentiment inferred
        from model prose, and is retained with the invocation that calculated
        it.  It is not included in the provider request.
        """
        completed_scored_cycles = sum(
            1 for item in state.get("invocations", {}).values()
            if item.get("status") == "accepted" and "inquiry_drive_shadow" in item
        )
        activation = {
            "operator_enabled": self.config["inquiry_drive_enabled"],
            "completed_scored_cycles": completed_scored_cycles,
            "minimum_completed_scored_cycles": INQUIRY_DRIVE_MIN_CYCLES,
            "active": bool(self.config["inquiry_drive_enabled"]
                           and completed_scored_cycles >= INQUIRY_DRIVE_MIN_CYCLES),
        }
        if not state.get("charter"):
            return {"mode": "shadow", "enabled": False, "projects": [],
                    "principle": "No research charter is active.", "activation": activation}

        research = list(state["research"].values())
        notebooks = list(state["notebooks"].values())
        projects = []
        for project in state["projects"].values():
            if project["status"] != "active":
                continue
            project_research = [item for item in research if item["project"] == project["id"]]
            collected = [item for item in project_research if item["status"] == "collected"]
            queued = [item for item in project_research if item["status"] == "queued"]
            project_notebooks = [item for item in notebooks if item["project"] == project["id"]]
            latest = project_notebooks[-1] if project_notebooks else None

            # Each component is a transparent 0–1 proxy, not a claim about an
            # internal motive, importance, truth, or consciousness.
            components = {
                "continuity": 1.0 if project.get("next_step", "").strip() else 0.0,
                "novelty": min(1.0, (len(queued) + len(collected)) / 2),
                "coherence": min(1.0, len(collected) / 2),
                "generativity": min(1.0, (1 if project.get("question", "").strip() else 0)
                                      + (0.5 if latest and latest.get("next_questions", "").strip() else 0)),
                "self_correction": min(1.0, (0.5 if latest and latest.get("limitations", "").strip() else 0)
                                        + (0.5 if latest and len(latest.get("evidence", [])) >= 2 else 0)),
            }
            weights = {"continuity": 0.30, "novelty": 0.15, "coherence": 0.20,
                       "generativity": 0.20, "self_correction": 0.15}
            score = round(sum(components[key] * weights[key] for key in weights), 3)
            projects.append({
                "id": project["id"], "title": project["title"], "score": score,
                "components": components,
                "signals": {"collected_research": len(collected), "queued_research": len(queued),
                            "notebooks": len(project_notebooks)},
            })

        projects.sort(key=lambda item: (-item["score"], item["id"]))
        return {
            "mode": "shadow", "enabled": True,
            "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
            "weights": {"continuity": 0.30, "novelty": 0.15, "coherence": 0.20,
                        "generativity": 0.20, "self_correction": 0.15},
            "activation": activation,
            "projects": projects,
        }
    # ---------------------------------------------------------------------------
    # STEP: context
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def context(self, state, receipt):
        # Recent receipts and the newest supporting evidence for every belief stay visible.
        # All citation IDs remain in beliefs; full evidence is always in the durable export.
        wanted = set(list(state["evidence"])[-6:])
        for belief in state["beliefs"].values():
            wanted.update(belief["evidence"][-3:])
        context = {"version": state["version"], "objective": state["objective"], "focus": state["focus"],
                "receipt": receipt, "beliefs": list(state["beliefs"].values()),
                "commitments": [c for c in state["commitments"].values() if c["status"] == "open"],
                "evidence": [v for k, v in state["evidence"].items() if k in wanted],
                "recent_journal": state["journal"][-3:],
                "evidence_scope": "Recent observations plus newest three citations per belief; full evidence remains in history."}
        if state.get("charter"):
            context["mission"] = state["charter"]
            context["pet_name"] = state["pet_name"]
            context["research_topics"] = state.get("research_topics") or self.config.get("research_topics", [])
            projects = list(state["projects"].values())
            context["projects"] = [p for p in projects if p["status"] == "active"] + [p for p in projects if p["status"] != "active"][-8:]
            context["notebooks"] = [{k:n[k] for k in ("id", "project", "title", "summary", "revision", "evidence")}
                                    for n in list(state["notebooks"].values())[-8:]]
            # Give editorial actions a canonical project -> notebook map. This is
            # intentionally metadata-only: Bob can select real durable IDs without
            # guessing relationships or needing full notebook bodies in context.
            context["blog_notebooks"] = {}
            for notebook in state["notebooks"].values():
                context["blog_notebooks"].setdefault(notebook["project"], []).append(
                    {k:notebook[k] for k in ("id", "title", "revision", "evidence")}
                )
            working = [n for n in state["notebooks"].values() if state["projects"][n["project"]]["status"] == "active"]
            context["working_notebook"] = ({**working[-1], "findings": working[-1]["findings"][:3000],
                                           "context_excerpt": True} if working else None)
            context["research"] = list(state["research"].values())[-8:]
            context["recent_blog"] = [
                {**{key: post.get(key) for key in ("id", "project", "title", "lede", "lens", "created_version",
                                                  "status", "supersedes", "superseded_by")},
                 "retractable_quotes": retractable_quotes(post)}
                for post in list(state.get("posts", {}).values())[-4:]
            ]
            # Bob reflects on the whole durable journey every tenth accepted wake.
            # state.version is the accepted-cycle count before the pending wake.
            context["bob_reflection_cycle"] = state["version"] + 1
            context["bob_reflection_due"] = context["bob_reflection_cycle"] % 20 == 0
            # Source-controlled operator review notes are editorial context, not research evidence.
            # They can flag prior public wording for reconsideration without rewriting history.
            context["editorial_notes"] = list(self.config.get("editorial_notes", []))
            # Research excerpts are bounded. Full snapshots remain available in the lab.
            sources = [v for v in state["evidence"].values() if v.get("actor") == "collector"][-6:]
            context["evidence"] = [{**e, "content": e["content"][:3000], "context_excerpt": len(e["content"]) > 3000}
                                   for e in context["evidence"] if e.get("actor") != "collector"][-3:]
            context["evidence"] += [{**e, "content": e["content"][:3000], "context_excerpt": len(e["content"]) > 3000} for e in sources]
            context["beliefs"] = [{**b, "evidence": b["evidence"][-6:]} for b in context["beliefs"]]
            outcomes = [e for e in self.store.events() if e["kind"] in ("rejected", "failed")][-2:]
            context["recent_problems"] = [e["payload"].get("reason", "") for e in outcomes]
            withheld = [i["editorial"] for i in state["invocations"].values() if i.get("editorial")][-2:]
            context["recent_problems"] += ["Blog withheld: " + note["reason"] for note in withheld]
        return context
    # ---------------------------------------------------------------------------
    # STEP: start
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def start(self, provider, model, charged=False):
        state = self.store.load()
        require(state["pending"] is None, "An invocation is already pending")
        day = datetime.now(ZoneInfo(self.config["timezone"])).date().isoformat()
        if charged:
            exhausted = [
                item for item in state["invocations"].values()
                if item.get("charged")
                and item.get("provider") == provider
                and item.get("model") == model
                and item.get("quota_day") == day
                and item.get("provider_error", {}).get("result") == "daily_quota"
                and item.get("provider_error", {}).get("model") == model
                and is_free_tier_daily_quota(item.get("provider_error", {}))
            ]
            require(
                not exhausted,
                "Gemini free-tier daily quota exhausted for this model until Pacific midnight; no request sent",
            )
        used = sum(charged_request_slots(i) for i in state["invocations"].values()
                   if i["charged"] and i["quota_day"] == day)
        if charged and not self.config.get("model_daily_call_limits"):
            require(used < self.config["daily_call_limit"], "Daily call ceiling reached; no request sent")
        invocation = "w-" + uuid.uuid4().hex[:16]
        receipt = "r-" + invocation[2:]
        _, head = self.store.replay()
        state = self.store.append("observation", {"id": receipt, "source": "runtime:continuity",
            "actor": "runtime", "content": canonical({"invocation": invocation, "process_id": os.getpid(),
                "base_version": state["version"], "previous_head": head,
                "inherited_commitments": [k for k, v in state["commitments"].items() if v["status"] == "open"],
                "scope": "Receipt proves state delivery to the provider boundary, not model comprehension."})})
        from .providers import RESEARCH_SYSTEM, SCHEMA
        delivered_context = self.context(state, receipt)
        working_set_shadow = self.working_set(state)
        trust_compacts_shadow = build_trust_compacts_shadow(state)
        retrieval_shadow = build_retrieval_shadow(state, working_set_shadow, trust_compacts_shadow)
        inquiry_drive_shadow = self.inquiry_drive_shadow(state)
        if inquiry_drive_shadow["activation"]["active"]:
            delivered_context["inquiry_drive"] = {
                "mode": "operator-activated advisory ranking",
                "boundary": "Favor productive, correctable inquiry only. This does not authorize self-preservation, rule changes, or work outside existing governance.",
                "projects": inquiry_drive_shadow["projects"],
            }
        request = {"system": SYSTEM + (RESEARCH_SYSTEM if state.get("charter") else ""),
                   "context": delivered_context,
                   "response_schema": schema_for_context(delivered_context) if state.get("charter") else SCHEMA}
        if state.get("charter") and len(canonical(request)) > self.config["max_context_chars"]:
            # Crossing the context threshold is a retrieval problem, not a reason to
            # discard durable history. Keep the complete record in SQLite/public
            # exports and shrink only this invocation's working view.
            request["context"]["recent_journal"] = []
            request["context"]["notebooks"] = request["context"]["notebooks"][-4:]
            request["context"]["working_notebook"] = None

            # Completed projects are historical receipts, not all equally useful
            # working memory. Preserve every active project plus the four newest
            # completed projects so the model can continue work without dragging
            # the entire project archive into every future invocation.
            projects = request["context"]["projects"]
            active_projects = [p for p in projects if p["status"] == "active"]
            completed_projects = [p for p in projects if p["status"] != "active"][-4:]
            request["context"]["projects"] = [{**p, "reason": p["reason"][:120], "question": p["question"][:300],
                                               "next_step": p["next_step"][:300], "title": p["title"][:120],
                                               "context_excerpt": True}
                                              for p in active_projects + completed_projects]

            # blog_notebooks used to grow monotonically because it contained every
            # notebook ever written. Keep mappings only for projects the model can
            # currently see plus projects referenced by the recent public record.
            visible_projects = {p["id"] for p in request["context"]["projects"]}
            visible_projects.update(
                post.get("project") for post in request["context"].get("recent_blog", [])
                if post.get("project")
            )
            request["context"]["blog_notebooks"] = {
                project: notebooks[-3:]
                for project, notebooks in request["context"].get("blog_notebooks", {}).items()
                if project in visible_projects
            }

            # Recent research is a working queue, not the archive. Four records are
            # enough to preserve immediate collector handoffs; exact older requests
            # remain recoverable from durable history.
            request["context"]["research"] = request["context"].get("research", [])[-4:]

            # Retain every open obligation and belief ID; excerpts are explicitly labeled.
            for collection, fields in (("commitments", ("task", "reason")), ("beliefs", ("statement", "reason"))):
                request["context"][collection] = [{**item, **{key:item[key][:200] for key in fields},
                                                   "context_excerpt": True} for item in request["context"][collection]]
            for evidence in request["context"]["evidence"]:
                evidence["content"] = evidence["content"][:800]
                evidence["context_excerpt"] = True
        require(len(canonical(request)) <= self.config["max_context_chars"],
                "Context ceiling reached; human review required, no model call made")
        shadow_chars = len(canonical(working_set_shadow))
        delivered_chars = len(canonical(request["context"]))
        self.store.append("invocation_started", {"id": invocation, "provider": provider, "model": model,
            "charged": charged, "quota_day": day, "base_version": state["version"], "request": request,
            "request_hash": digest(request), "process_id": os.getpid(),
            "working_set_shadow": working_set_shadow,
            "trust_compacts_shadow": trust_compacts_shadow,
            "retrieval_shadow": retrieval_shadow,
            "inquiry_drive_shadow": inquiry_drive_shadow,
            "working_set_metrics": {
                "mode": "shadow",
                "working_set_chars": shadow_chars,
                "delivered_context_chars": delivered_chars,
                "working_to_delivered_ratio": round(shadow_chars / max(delivered_chars, 1), 4),
                "retrieval_candidate_count": retrieval_shadow["metrics"]["candidate_count"],
                "retrieval_evidence_count": retrieval_shadow["metrics"]["evidence_count"],
                "retrieval_trigger_counts": retrieval_shadow["metrics"]["trigger_counts"],
                "trust_compact_candidate_count": trust_compacts_shadow["metrics"]["candidate_count"],
                "trust_compact_settled_count": trust_compacts_shadow["metrics"]["settled_count"],
                "trust_compact_evidence_root_count": trust_compacts_shadow["metrics"]["evidence_root_count"],
                "inquiry_drive_project_count": len(inquiry_drive_shadow["projects"]),
            }})
        return invocation, request
    # ---------------------------------------------------------------------------
    # STEP: finish
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def finish(self, invocation, raw, metadata=None, crash=False):
        state = self.store.load()
        require(state["pending"] == invocation, "Response does not match the pending invocation")
        try:
            require(isinstance(raw, str) and len(raw) <= 64000, "Response exceeds 64,000 characters")
            proposal = json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError("Nonfinite JSON")))
            editorial = None
            try:
                result = transition(state, proposal, invocation)
            except Rejected as exc:
                actions = proposal.get("actions") if isinstance(proposal, dict) else None
                # Only the single optional final blog can be withheld. Research and
                # the original proposal envelope still cross the full governance boundary.
                if not (state.get("charter") and isinstance(actions, list) and 2 <= len(actions) <= 12
                        and all(isinstance(a, dict) and a.get("type") != "blog" for a in actions[:-1])
                        and isinstance(actions[-1], dict) and actions[-1].get("type") == "blog"):
                    raise
                accepted_proposal = {**proposal, "actions": actions[:-1]}
                transition(state, accepted_proposal, invocation)  # Research must validate independently.
                editorial = {"status": "withheld", "reason": str(exc)[:1000], "action": actions[-1]}
                accepted_proposal["summary"] = (proposal["summary"][:2100] +
                    "\n\nEditorial note: the proposed blog post was withheld. " + str(exc)[:180])
                proposal = accepted_proposal
                result = transition(state, proposal, invocation)
        except (ValueError, TypeError, KeyError) as exc:
            reason = str(exc)[:1000]
            self.store.append("rejected", {"id": invocation, "reason": reason,
                                          "raw_response": str(raw)[:64000], "metadata": metadata or {},
                                          **({"provider_requests_sent": metadata["provider_requests_sent"]}
                                             if metadata and "provider_requests_sent" in metadata else {})})
            return {"status": "rejected", "id": invocation, "reason": reason}
        fields = ["version", "beliefs", "commitments", "journal"]
        if state.get("charter"):
            fields += ["projects", "notebooks", "research", "posts"]
        result_hash = digest({k: result[k] for k in fields})
        self.store.append("accepted", {"id": invocation, "proposal": proposal, "raw_response": raw,
                                       "metadata": metadata or {},
                                       **({"provider_requests_sent": metadata["provider_requests_sent"]}
                                          if metadata and "provider_requests_sent" in metadata else {}), "result_hash": result_hash, "hash_fields": fields,
                                       **({"editorial": editorial} if editorial else {})}, crash=crash)
        return {"status": "accepted", "id": invocation, "cycle": result["version"],
                **({"editorial": {k: v for k, v in editorial.items() if k != "action"}} if editorial else {})}

    @staticmethod
    # ---------------------------------------------------------------------------
    # STEP: _request_count
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Keep this helper narrow so private mechanics do not leak into policy.
    # ---------------------------------------------------------------------------
    def _request_count(provider):
        if hasattr(provider, "provider_attempts"):
            return provider.diagnostics()
        count = getattr(provider, "provider_requests_sent", None)
        return {"provider_requests_sent": count} if count is not None else {}
    # ---------------------------------------------------------------------------
    # STEP: run
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def run(self, provider, crash_at=None, checkpoint=None, collector=None):
        with self.store.lock():
            self.initialize()
            self.recover()
            if collector:
                collector(self)
            invocation, request = self.start(provider.name, provider.model, provider.charged)
            if hasattr(provider, "record_attempt"):
                state = self.store.load()
                day = state["invocations"][invocation]["quota_day"]
                if self.config.get("model_daily_call_limits"):
                    used_by_model = {}
                    exhausted_models = set()
                    for item in state["invocations"].values():
                        if item["id"] == invocation or not item["charged"] or item["quota_day"] != day:
                            continue
                        for attempt in item.get("provider_attempts", []):
                            if attempt.get("result") == "daily_quota" and is_free_tier_daily_quota(attempt):
                                failed_model = attempt.get("model")
                                if failed_model:
                                    exhausted_models.add(failed_model)
                        for attempt in item.get("provider_attempts", []):
                            model = attempt.get("model")
                            if model:
                                used_by_model[model] = used_by_model.get(model, 0) + 1
                    provider.model_request_limits = {model: max(0, self.config["model_daily_call_limits"].get(model, self.config["daily_call_limit"]) - used_by_model.get(model, 0)) for model in provider.models}
                    for model in exhausted_models:
                        provider.model_request_limits[model] = 0
                else:
                    used = sum(charged_request_slots(i) for i in state["invocations"].values() if i["id"] != invocation and i["charged"] and i["quota_day"] == day)
                    provider.request_limit = min(len(provider.models), self.config["daily_call_limit"] - used)
                # ---------------------------------------------------------------------------
                # STEP: record_attempt
                #
                # This step exists as an explicit seam so its behavior can be
                # inspected, tested, and replaced without giving a model hidden authority.
                # Inputs should already belong to the layer named above; outputs remain data
                # until the next boundary validates or records them. Callers may rely on this contract.
                # ---------------------------------------------------------------------------

                def record_attempt(phase, attempt):
                    self.store.append("provider_attempt_" + phase, {"id": invocation, "attempt": attempt})
                    if checkpoint:
                        checkpoint()
                provider.record_attempt = record_attempt
            if checkpoint:
                checkpoint()  # Remote reservation must succeed before the model call.
            if crash_at == "after-start":
                os._exit(85)
            try:
                raw, metadata = provider.propose(request)
            except TransientProviderError as exc:
                reason = str(exc)[:1000]
                self.store.append("deferred", {"id": invocation, "reason": reason, "provider_error": exc.details, **self._request_count(provider)})
                if checkpoint:
                    checkpoint()
                return {"status": "deferred", "id": invocation, "reason": reason, "provider_error": exc.details, **self._request_count(provider)}
            except DailyQuotaExceeded as exc:
                reason = str(exc)[:1000]
                payload = {"id": invocation, "reason": reason, "provider_error": exc.details,
                           "quota_exhausted": "free_tier_daily", **self._request_count(provider)}
                self.store.append("deferred", payload)
                if checkpoint:
                    checkpoint()
                return {"status": "deferred", "id": invocation, "reason": reason,
                        "provider_error": exc.details, "quota_exhausted": "free_tier_daily", **self._request_count(provider)}
            except ProviderRequestError as exc:
                reason = str(exc)[:1000]
                self.store.append("failed", {"id": invocation, "reason": reason,
                                             "provider_error": exc.details, **self._request_count(provider)})
                if checkpoint:
                    checkpoint()
                return {"status": "failed", "id": invocation, "reason": reason,
                        "provider_error": exc.details, **self._request_count(provider)}
            except Exception as exc:
                reason = str(exc)[:1000] if isinstance(exc, Rejected) else f"Provider failed ({type(exc).__name__}); no automatic retry"
                self.store.append("failed", {"id": invocation, "reason": reason, **self._request_count(provider)})
                if checkpoint:
                    checkpoint()
                return {"status": "failed", "id": invocation, "reason": reason}
            result = self.finish(invocation, raw, metadata, crash=crash_at == "during-commit")
            if checkpoint:
                checkpoint()
            return result
