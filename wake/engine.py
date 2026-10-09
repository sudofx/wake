# =============================================================================
# ENGINE — the orchestration layer. A wake is one governed work transition: reconstruct durable state, select bounded context, reserve/record the invocation, call a provider, then ask governance whether the proposal may become history. The engine coordinates these steps but never substitutes its own judgment for governance.
# =============================================================================

"""Research orchestration over an explicitly injected authoritative store.

    A scheduled wake may plan, collect and then request a final proposal; each
    inference phase has its own native reservation and receipt. Planning never
    advances accepted research. Context/memory are derived delivery, while domain
    policy and the application host decide the atomic durable transition.
    """

from datetime import datetime
import json
import os
from pathlib import Path
import re
import secrets
import tomllib
import uuid
from time import perf_counter
from zoneinfo import ZoneInfo

from wake.kernel import InvocationBarrierError

from .application_policy import _rotation_preflight, govern_proposal
from .governance import Rejected, bob_reflection_due_cycle, require, text
from .providers import (
    SCHEMA, SYSTEM, ConfiguredDailyLimitReached, DailyQuotaExceeded, ProviderRequestError, TransientProviderError,
    is_free_tier_daily_quota, retractable_quotes, schema_for_context,
)
from .scheduling import charged_request_slots
from .retrieval import build_retrieval_shadow
from .research import effective_evidence_role, effective_host_tier, source_observation_readable
from .event_format import canonical, digest, now
from .experimental import adoption_payload, defaults as experimental_defaults, temporal_snapshot, validate as validate_controls
from .trust import build_trust_compacts_shadow
from .memory import ACTIVE_MEMORY_SYSTEM, active_retrieval_plan, build_active_memory
from .attention import assessment as attention_assessment, plan as attention_plan
from .matrix_campaign import (
    MATRIX_SIDECAR_SYSTEM,
    add_continuity_response_schema,
    build_continuity_probe,
    continuity_result_record,
    evaluate_continuity_probe_response,
    failed_continuity_probe_evaluation,
)


def report_activity(observer, stage, **details):
    """Best-effort presentation telemetry, never permission or durable authority.

    A broken display observer must not change research acceptance or interrupt a
    provider effect. Only explicitly selected public identifiers cross this seam.
    """
    if observer is not None:
        try:
            observer(stage=stage, **details)
        except Exception:
            pass


INQUIRY_DRIVE_MIN_CYCLES = 20
TOPIC_COLORS = (
    "#ff5bb9", "#b25dff", "#46b5ff", "#ffe574", "#93ff74", "#ff9e64",
    "#73daca", "#7aa2f7", "#c0caf5", "#ff757f", "#e0af68", "#9ece6a",
    "#f7768e", "#9d7cd8", "#2ac3de", "#d8c25d", "#5fcf8d", "#c099ff",
    "#f68c65", "#54d4bc", "#8aa8ff", "#f2a2ca", "#b7d36b", "#f0bd75",
)


# Human-readable delivery labels, not model instructions or authority. Under
# pressure their shorter wording carries the same omission categories; the
# provenance policy and exact supplied records remain separate, unchanged fields.
COMPACT_OMISSION_LABELS = {
    "full durable evidence content": "full evidence bodies",
    "research and blog history outside the bounded working set": "older research/blog history",
    "core instruction prose compacted; response schema and governance unchanged": "core instruction prose",
    "active-memory instruction prose compacted; trust and retrieval boundaries unchanged": "memory instruction prose",
    "advisory source-selection diagnostics": "source-selection diagnostics",
    "belief review choices bounded to one new visible root per belief; durable roots unchanged": "extra eligible review citations",
    "extended recovery prose; project/frame and observation pointers retained": "extended recovery prose",
    "extended evidence excerpts; all visible evidence IDs retained": "extended source prose",
    "extended working prose; all belief/project/notebook identities and roots retained": "extended working prose",
    "shorter source excerpts; all visible evidence IDs and provenance retained": "shortened source excerpts",
    "prior notebook finding prose; artifact hashes and new-source eligibility retained": "prior notebook finding prose",
    "editorial reflection history excerpted; original window hash/counts retained, no missing content may be inferred": "editorial reflection prose",
    "editorial notebook titles omitted; eligibility, revisions and evidence roots retained": "editorial notebook titles",
    "minimal source excerpts; all evidence identities and provenance retained": "minimal source excerpts",
}


def _topic_colors(topics):
    """Assign a fresh, recorded color to each configured topic."""
    require(len(topics) <= len(TOPIC_COLORS), "Too many topics for unique topic colors")
    return dict(zip((topic["id"] for topic in topics), secrets.SystemRandom().sample(TOPIC_COLORS, len(topics))))


def _provider_response_schema(context, research):
    """Build the ordinary proposal contract plus an enabled continuity sidecar."""
    if research:
        base = schema_for_context(context)
    else:
        # A generic reference workload has no research charter. Offering its
        # domain actions would confound model behavior with a forbidden schema.
        base = json.loads(canonical(SCHEMA))
        base["properties"]["actions"]["items"]["anyOf"] = [
            action for action in base["properties"]["actions"]["items"]["anyOf"]
            if action["properties"]["type"]["enum"][0] in ("belief", "commit", "resolve")
        ]
        base["properties"]["base_version"]["enum"] = [context["version"]]
    probe = context.get("continuity_probe")
    if isinstance(probe, dict):
        return add_continuity_response_schema(base, probe)
    return base


DEFAULTS = {"timezone": "America/Los_Angeles", "objective": "Test durable continuity under mechanical governance.",
            "provider": "gemini", "model": "gemini-2.5-flash", "daily_call_limit": 20, "model_daily_call_limits": {},
            "max_context_chars": 48000, "max_output_tokens": 4096, "timeout_seconds": 60,
            "free_tier_confirmed": False, "gemini_fallback_models": [], "gemini_fallback_requires_primary_daily_quota": False,
            "memory_mode": "shadow", "research_google_search": False, "same_wake_research": False, "inquiry_drive_enabled": False, "research_topics_file": "research-topics.toml",
            "observation_mode": False, "research_collection_budget": 2, "research_collection_wall_seconds": 45}

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
        # A seed question is an operator-supplied starting coordinate, not a
        # permanent mission.  It is stored with the audited topic configuration
        # so old cycles remain truthful about whether a seed existed yet.
        allowed = {"id", "label", "query", "seed_question", "enabled", "source_kind", "repository"}
        require(isinstance(item, dict) and {"id", "label", "query"} <= set(item) <= allowed,
                "Each research topic needs id, label, query, and may include seed_question, enabled, source_kind, repository")
        require(isinstance(item["id"], str) and re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", item["id"]),
                "Research topic IDs must use letters, digits, underscores or hyphens")
        text(item["label"], "Research topic label", 120)
        text(item["query"], "Research topic query", 200)
        if "seed_question" in item:
            text(item["seed_question"], "Research topic seed question", 600)
        enabled = item.get("enabled", True)
        require(type(enabled) is bool, "Research topic enabled must be true or false")
        source_kind = item.get("source_kind", "web")
        require(source_kind in ("web", "repository"), "Research topic source_kind must be web or repository")
        if source_kind == "repository":
            repository = item.get("repository")
            require(isinstance(repository, str) and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository),
                    "Repository research topics require repository = owner/name")
        elif "repository" in item:
            require(False, "Only repository research topics may set repository")
        normalized.append({
            **{key: item[key] for key in ("id", "label", "query", "seed_question", "repository") if key in item},
            "enabled": enabled,
            "source_kind": source_kind,
        })
    require(len({item["id"] for item in normalized}) == len(normalized), "Research topic IDs must be unique")
    require(any(item["enabled"] for item in normalized), "At least one research topic must be enabled")
    return normalized

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
    require(type(result["research_google_search"]) is bool, "research_google_search must be boolean")
    require(type(result["same_wake_research"]) is bool, "same_wake_research must be boolean")
    require(result["memory_mode"] in ("shadow", "active"), "memory_mode must be shadow or active")
    require(type(result["inquiry_drive_enabled"]) is bool,
            "inquiry_drive_enabled must be true or false")
    require(type(result["observation_mode"]) is bool,
            "observation_mode must be true or false")
    require(type(result["gemini_fallback_requires_primary_daily_quota"]) is bool,
            "gemini_fallback_requires_primary_daily_quota must be true or false")
    require(type(result["research_collection_budget"]) is int and 2 <= result["research_collection_budget"] <= 8,
            "research_collection_budget must be between 2 and 8")
    require(type(result["research_collection_wall_seconds"]) is int and 10 <= result["research_collection_wall_seconds"] <= 120,
            "research_collection_wall_seconds must be between 10 and 120")
    text(result["objective"], "Objective", 2000)
    if result.get("mission"):
        text(result["mission"], "Research mission", 3000)
        project_name = result.get("project_name", result.get("pet_name", "WAKE✳"))
        text(project_name, "Project name", 80)
        result["project_name"] = project_name
        notes = result.get("editorial_notes", [])
        require(isinstance(notes, list) and len(notes) <= 8,
                "editorial_notes must be a list of at most 8 notes")
        for note in notes:
            text(note, "Editorial note", 1200)
        require(result.get("research_topics_file"), "research_topics_file is required when mission is configured")
        result["research_topics"] = _topics(result, config_path)
    return result

class Engine:
    def __init__(self, directory="data", settings=None, *, store=None, store_factory=None):
        self.config = settings or config()
        require(self.config.get("memory_mode", "shadow") in ("shadow", "active"), "memory_mode must be shadow or active")
        if self.config.get("mission"):
            if not self.config.get("research_topics"):
                filename = self.config.get("research_topics_file")
                require(filename, "research_topics_file is required when the research charter is enabled")
                topic_path = Path(filename)
                require(topic_path.is_file(), f"Research topics file not found: {topic_path}")
                self.config["research_topics"] = _topics(self.config, Path("wake.toml"))
            else:
                self.config["research_topics"] = _topics(self.config)
        if store is not None and store_factory is not None:
            raise ValueError("Choose an explicit store or store_factory, not both")
        if store is None:
            if store_factory is None:
                raise ValueError(
                    "Engine requires an explicit authority store; operational callers "
                    "must use open_authoritative_store(...). Compatibility fixtures "
                    "may provide an explicit store_factory."
                )
            store = store_factory(directory)
        self.store = store
    def initialize(self):
        state, _ = self.store.replay()
        if not state["objective"]:
            state = self.store.append("initialized", {"objective": self.config["objective"], "governance": 1})
        if self.config.get("mission") and not state.get("charter"):
            state = self.store.append("charter_adopted", {"mission": self.config["mission"],
                                     "pet_name": self.config.get("project_name", self.config.get("pet_name", "WAKE✳")),
                                     "topics": self.config["research_topics"],
                                     "topic_colors": _topic_colors(self.config["research_topics"]), "actor": "operator"})
        # A branding change is part of the durable identity. Record it as an
        # auditable event instead of rewriting the original charter or history.
        desired_name = self.config.get("project_name", self.config.get("pet_name", "WAKE✳"))
        if state.get("charter") and state.get("pet_name") != desired_name:
            state = self.store.append("pet_renamed", {"pet_name": desired_name, "actor": "operator"})
        desired_topics = self.config.get("research_topics", [])
        topic_ids = {topic["id"] for topic in desired_topics}
        if state.get("charter") and (state.get("research_topics") != desired_topics
                                      or set(state.get("topic_colors", {})) != topic_ids):
            self.store.append("research_topics_changed", {"topics": desired_topics,
                              "topic_colors": _topic_colors(desired_topics), "actor": "operator"})
        # A regime begins only when this version of WAKE is first run.  We append
        # that boundary instead of projecting controls backwards into old cycles.
        state = self.store.load(repair=True)
        if not state.get("experimental"):
            events = self.store.events()
            self.store.append("experimental_regime_adopted", adoption_payload(
                state, events, experimental_defaults(), "operator",
                "Initialize the default experimental instrument regime.", now(), len(events) + 1))
        return self.store.load(repair=True)

    def set_time_dilation(self, *, enabled=None, mode=None, scale=None, reason):
        """Append an operator intervention; provider proposals never reach here."""
        state = self.store.load()
        require(state.get("experimental"), "Initialize the record before changing controls")
        controls = {key: dict(value) for key, value in state["experimental"]["controls"].items()}
        item = controls["time_dilation"]
        if enabled is not None:
            item["enabled"] = enabled
        if mode is not None:
            item["mode"] = mode
        if scale is not None:
            item["scale"] = scale
        if item["mode"] in ("real", "frozen"):
            item["scale"] = 1.0
        controls = validate_controls(controls)
        require(controls != state["experimental"]["controls"], "Experimental controls are already set to those values")
        events = self.store.events()
        return self.store.append("experimental_regime_adopted", adoption_payload(
            state, events, controls, "operator", reason, now(), len(events) + 1))
    def recover(self, explicit=False):
        # Both the WAKE-compatible projection and the generic
        # WAKE kernel invocation journal describe the same provider boundary. Close
        # abandoned generic lifecycles first so process recovery cannot leave a
        # second, apparently-live attempt behind after WAKE resumes.
        if hasattr(self.store, "recover_invocation_lifecycles"):
            self.store.recover_invocation_lifecycles()
        state = self.store.load(repair=True)
        if state["pending"]:
            item = state["invocations"][state["pending"]]
            require(explicit or item["provider"] != "manual", "A manual proposal is pending; complete it or explicitly recover")
            state = self.store.append("recovered", {"id": state["pending"],
                                       "reason": "Previous invocation ended without a committed decision; resumed last valid state."})
        return state
    def observe(self, content, source, evidence_id=None):
        text(content, "Observation", 8000)
        text(source, "Source", 1000)
        state = self.store.load()
        require(state["pending"] is None, "Finish or recover the pending invocation before adding evidence")
        return self.store.append("observation", {"id": evidence_id or "e-" + uuid.uuid4().hex[:16],
                                                 "source": source, "content": content, "actor": "human"})
    def working_set(self, state):
        """Build a deliberately lossy, traceable shadow of the durable state.

        Preserve the historical shadow receipt in both delivery modes. Routine
        active delivery derives its model input from this same working-set owner.
        """
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
                "falsifier": excerpt(belief.get("falsifier", ""), 260),
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

    def bob_reflection_history(self, state):
        """Return a compact longitudinal window for a due Bob milestone.

        A reflection is editorial synthesis, not research evidence. Under context
        pressure Bob still needs enough durable history to notice change across
        wakes rather than paraphrasing the current snapshot.
        """
        milestone = bob_reflection_due_cycle(state)
        if milestone is None:
            return None

        def excerpt(value, limit):
            value = str(value or "")
            return value if len(value) <= limit else value[:limit - 1] + "…"

        previous_reflection = None
        for post in reversed(list(state.get("posts", {}).values())):
            declared = post.get("reflection_cycle")
            created = post.get("created_version")
            if (type(declared) is int and declared > 0) or (
                type(created) is int and created > 0 and created % 10 == 0
            ):
                previous_reflection = {
                    "id": post.get("id"),
                    "reflection_cycle": declared or created,
                    "title": excerpt(post.get("title"), 180),
                    "lede": excerpt(post.get("lede"), 320),
                    "body_excerpt": excerpt(post.get("body"), 1000),
                    "lens": excerpt(post.get("lens"), 400),
                }
                break

        acquisitions = []
        for project_id, summary in state.get("acquisition", {}).items():
            if not (summary.get("no_progress") or summary.get("capability_blocked")):
                continue
            receipt = summary.get("last_receipt") or {}
            acquisitions.append({
                "project": project_id,
                "no_progress": summary.get("no_progress", 0),
                "capability_blocked": bool(summary.get("capability_blocked")),
                "retry_after_version": summary.get("retry_after_version"),
                "last_outcome": receipt.get("outcome") or receipt.get("status"),
                "last_reason": excerpt(receipt.get("reason"), 260),
            })

        return {
            "milestone": milestone,
            "accepted_wakes": [
                {
                    "cycle": item.get("cycle"),
                    "invocation": item.get("invocation"),
                    "title": excerpt(item.get("title"), 180),
                    "summary": excerpt(item.get("summary"), 520),
                }
                for item in state.get("journal", [])[-10:]
            ],
            "projects": [
                {
                    "id": project.get("id"),
                    "title": excerpt(project.get("title"), 160),
                    "domain": project.get("domain"),
                    "status": project.get("status"),
                    "next_step": excerpt(project.get("next_step"), 260),
                }
                for project in list(state.get("projects", {}).values())[-8:]
            ],
            "research": [
                {
                    "id": item.get("id"),
                    "project": item.get("project"),
                    "domain": item.get("domain"),
                    "status": item.get("status"),
                    "query": excerpt(item.get("query"), 220),
                }
                for item in list(state.get("research", {}).values())[-10:]
            ],
            "notebooks": [
                {
                    "id": item.get("id"),
                    "project": item.get("project"),
                    "title": excerpt(item.get("title"), 160),
                    "summary": excerpt(item.get("summary"), 360),
                    "revision": item.get("revision"),
                }
                for item in list(state.get("notebooks", {}).values())[-6:]
            ],
            "acquisition_friction": acquisitions[-8:],
            "previous_reflection": previous_reflection,
            "boundary": (
                "Compact editorial history for Bob's milestone reflection. "
                "It describes the durable journey but does not qualify as research evidence."
            ),
        }

    def bounded_context(self, state, receipt, working_set, rich_context_chars):
        """Make the deterministic working set the bounded provider view.

        This is deliberately a one-way delivery adaptation: the full projection,
        event chain, and the shadow annotations remain exact in the durable record.
        The provider receives only bounded excerpts plus IDs that let governance and
        a later retrieval pass identify the authoritative material.
        """
        def excerpt(value, limit):
            value = str(value)
            return value if len(value) <= limit else value[:limit - 1] + "…"

        evidence_ids = list(dict.fromkeys(
            evidence_id for belief in working_set["beliefs"]
            for evidence_id in belief["provenance"]
        ))
        evidence = [{
            "id": item["id"], "source": item.get("source", ""),
            "actor": item.get("actor", ""), "version": item.get("version"),
            "scope": item.get("scope"), "content_omitted": True,
        } for evidence_id in evidence_ids if (item := state["evidence"].get(evidence_id))]
        context = {
            "version": state["version"], "objective": state["objective"],
            "focus": state["focus"], "receipt": receipt,
            "context_mode": "bounded",
            "bounded_context": {
                "principle": working_set["principle"],
                "rich_context_chars": rich_context_chars,
                "omitted_categories": [
                    "full durable evidence content", "recent journal bodies",
                    "completed-project archive", "full notebook bodies",
                    "research and blog history outside the bounded working set",
                ],
                "provenance_policy": "All retained claims and notebooks carry durable IDs; exact records remain available outside this provider request.",
                "retrieval_triggers": working_set["retrieval_triggers"],
            },
            "beliefs": [{
                "id": item["id"], "statement": item["claim"],
                "confidence": item["confidence"], "status": item["status"],
                "reason": item["why_retained"], "evidence": item["provenance"],
                "context_excerpt": True,
            } for item in working_set["beliefs"]],
            "commitments": [{
                "id": item["id"], "project": state["commitments"][item["id"]].get("project"),
                "task": item["task"], "due_cycle": item["due_cycle"],
                "reason": item["reason"], "status": "open",
                "created_version": state["commitments"][item["id"]].get("created_version"),
                "resolution_evidence": [], "context_excerpt": True,
            } for item in working_set["open_commitments"]],
            "evidence": evidence,
            "evidence_scope": "Metadata for evidence roots retained by the bounded working set; exact content remains in durable history.",
            "recent_journal": [],
        }
        if state.get("charter"):
            context["attention"] = attention_plan(state)
        if state.get("charter"):
            active = list(working_set.get("active_projects", []))
            # Attention may select a topic whose unfinished project is parked or
            # otherwise outside the active working set. That durable identity is
            # governance-critical: without it a fresh model can recreate the exact
            # question under a new ID. Inject selected-topic unfinished projects
            # before any later emergency compaction.
            selected_topic = context.get("attention", {}).get("selected_topic")
            active_ids = {item.get("id") for item in active}
            selected_existing = [
                project for project in state.get("projects", {}).values()
                if selected_topic
                and project.get("domain") == selected_topic
                and project.get("status") != "completed"
                and project.get("id") not in active_ids
            ]
            selected_existing.sort(
                key=lambda item: (item.get("updated_version", 0), item.get("id", ""))
            )
            active.extend({
                "id": project["id"],
                "title": project.get("title", ""),
                "question": project.get("question", ""),
                "next_step": project.get("next_step", ""),
            } for project in selected_existing[-8:])
            # Overflow must not erase recovery conditions. Keep only compact
            # identifiers and frames here; full observations remain durable.
            recovery = []
            for project_id, summary in state.get("acquisition", {}).items():
                if summary.get("capability_blocked"):
                    recovery.append({"project": project_id, "capability": summary,
                                     "frames": state.get("representations", {}).get(project_id, [])[-3:]})
            for parked in state.get("attention", {}).get("deferred", {}).values():
                for project in parked.get("parked_projects", []):
                    if not any(item["project"] == project["id"] for item in recovery):
                        recovery.append({"project": project["id"], "parked": project,
                                         "frames": state.get("representations", {}).get(project["id"], [])[-3:],
                                         "intervening_experience": [item["id"] for item in list(state.get("evidence", {}).values())[-6:]]})
            context.update({
                "mission": state["charter"], "pet_name": state["pet_name"],
                "research_topics": state.get("research_topics") or self.config.get("research_topics", []),
                "projects": [{
                    **{key: value for key, value in state["projects"][item["id"]].items()
                       if key not in ("title", "question", "next_step", "reason")},
                    "title": item["title"], "question": item["question"],
                    "next_step": item["next_step"],
                    "reason": excerpt(state["projects"][item["id"]].get("reason", ""), 220),
                    "context_excerpt": True,
                } for item in active],
                "notebooks": working_set.get("recent_notebooks", []),
                "blog_notebooks": {}, "working_notebook": None, "research": [],
                # Even under emergency compaction Bob must know whether a public
                # record already exists. Otherwise a later milestone can falsely
                # introduce him as if it were the first post.
                "recent_blog": [
                    {key: post.get(key) for key in (
                        "id", "project", "title", "created_version",
                        "reflection_cycle", "status", "supersedes", "superseded_by",
                    )}
                    for post in list(state.get("posts", {}).values())[-4:]
                ],
                "editorial_notes": [],
                "bob_reflection_cycle": bob_reflection_due_cycle(state),
                "bob_reflection_due": bob_reflection_due_cycle(state) is not None,
                "reflection_history": self.bob_reflection_history(state),
                "project_evidence": {},
                "representation_recovery": recovery,
            })
            for notebook in context["notebooks"]:
                context["blog_notebooks"].setdefault(notebook["project"], []).append({
                    # Compact notebook summaries may intentionally omit their
                    # evidence list. Preserve that omission instead of making
                    # an overflow recovery path fail before report export.
                    key: notebook.get(key, [] if key == "evidence" else None)
                    for key in ("id", "title", "revision", "evidence")
                })
        self.proposal_constraints(state, context)
        return context

    def proposal_constraints(self, state, context):
        """Retain mechanical action eligibility across every delivery mode.

        Counts and prior identities come from the full authoritative state, not
        the excerpted memory window. This view guides generation; governance
        still checks the original proposal without repairing it.
        """
        if not state.get("charter"):
            return
        queued = sorted(item["id"] for item in state.get("research", {}).values()
                        if item.get("status") == "queued")
        visible_projects = {item["id"] for item in context.get("projects", [])}
        attention = context.get("attention", {})
        selected = attention.get("selected_topic") if attention.get("enforce_selected_topic") else None
        notebooks = {}
        # One current revision target per visible project. Historical notebook
        # IDs are not an invitation to rewrite every old synthesis, and copying
        # all historical findings would defeat bounded delivery.
        latest = {}
        for item in sorted(state.get("notebooks", {}).values(), key=lambda n: (
                n.get("updated_version", n.get("created_version", 0)), n["id"])):
            if item.get("project") not in visible_projects:
                continue
            if selected and state["projects"][item["project"]]["domain"] != selected:
                continue
            latest[item["project"]] = item
        for item in latest.values():
            allowed = set(context.get("project_evidence", {}).get(item["project"], []))
            new = sorted(allowed - set(item.get("evidence", [])))
            notebooks[item["id"]] = {
                "project": item["project"], "new_evidence_ids": new,
                "findings_hash": digest(item.get("findings", "")),
                "prior_findings_excerpt": item.get("findings", "")[:400],
            }
        context["proposal_constraints"] = {
            "queued_search_ids": queued,
            "remaining_search_slots": max(0, 4 - len(queued)),
            "known_project_ids": sorted(state.get("projects", {})),
            "project_identities": {
                key: {field: state["projects"][key][field]
                      for field in ("title", "question", "domain")}
                for key in sorted(visible_projects)
            },
            "notebook_revisions": notebooks,
            "known_belief_ids": sorted(state.get("beliefs", {})),
            "belief_reviews": {
                item["id"]: {"new_evidence_ids": sorted(
                    {e["id"] for e in context.get("evidence", [])
                     if e.get("id") in state.get("evidence", {})}
                    - set(state["beliefs"][item["id"]].get("evidence", [])))}
                for item in context.get("beliefs", [])
                if item.get("id") in state.get("beliefs", {})
            },
        }
        active = [item for item in state.get("projects", {}).values()
                  if item.get("status") == "active"]
        if selected and len(active) >= 3 and not any(item["domain"] == selected for item in active):
            context["proposal_constraints"]["required_next_step"] = (
                "Park one existing active project first; all three active slots are full. "
                "Resume the selected-topic parked project on a later accepted transition.")
        outcomes = self.store.tail_events(("rejected", "failed"), 2)
        context["recent_problems"] = [item["payload"].get("reason", "") for item in outcomes]
        guidance = []
        for reason in context["recent_problems"]:
            if "four queued source searches" in reason:
                guidance.append("Use remaining_search_slots for the entire proposal, not per action. When zero, use collected evidence or let the collector drain queued work; do not add searches.")
            elif "cannot change title or research question" in reason:
                guidance.append("Copy an existing project's exact project_identities fields when updating status/next_step. A different question requires a genuinely new project ID, subject to Attention and capacity.")
            elif "revision needs changed findings" in reason:
                guidance.append("Revise the exact notebook ID only with changed findings and at least one of its new_evidence_ids. Fresh retrieval alone does not make a repeated finding a revision.")
        context["proposal_recovery"] = list(dict.fromkeys(guidance))

    def focus_synthesis_delivery(self, context):
        """Focus an overflowed working view on one synthesis-ready project.

        Emergency compaction must not repeatedly turn a ready research project
        back into a collection-only project. When exact readable evidence is
        already present, keep one auditable project/evidence handoff and drop
        competing working-set material before considering synthesis suppression.
        """
        ready = list(dict.fromkeys(context.get("synthesis_ready_projects", [])))
        if not ready:
            return False

        projects = {
            project.get("id"): project
            for project in context.get("projects", [])
            if isinstance(project, dict) and project.get("id")
        }
        visible_evidence = {
            item.get("id"): item
            for item in context.get("evidence", [])
            if isinstance(item, dict) and item.get("id") and item.get("content")
        }
        project_evidence = context.get("project_evidence", {})
        selected_topic = (context.get("attention") or {}).get("selected_topic")

        candidates = []
        for project_id in ready:
            project = projects.get(project_id)
            if not project or project.get("status") != "active":
                continue
            allowed = [
                evidence_id
                for evidence_id in project_evidence.get(project_id, [])
                if evidence_id in visible_evidence
            ]
            if not allowed:
                continue
            candidates.append((
                0 if selected_topic and project.get("domain") == selected_topic else 1,
                ready.index(project_id),
                project_id,
                allowed[:2],
            ))
        if not candidates:
            return False

        _, _, target_id, allowed = min(candidates)
        context["projects"] = [projects[target_id]]
        context["evidence"] = [visible_evidence[evidence_id] for evidence_id in allowed]
        context["project_evidence"] = {target_id: allowed}
        context["synthesis_ready_projects"] = [target_id]
        context["research"] = []
        context["notebooks"] = [
            item for item in context.get("notebooks", [])
            if item.get("project") == target_id
        ][-1:]
        context["working_notebook"] = None
        context["blog_notebooks"] = {
            target_id: context.get("blog_notebooks", {}).get(target_id, [])[-2:]
        } if context.get("blog_notebooks", {}).get(target_id) else {}
        bounded = context.setdefault("bounded_context", {})
        bounded["synthesis_focus"] = {
            "project": target_id,
            "evidence_ids": allowed,
            "boundary": (
                "Emergency delivery focused on a synthesis-ready project so "
                "context pressure cannot silently return it to collection."
            ),
        }
        return True

    def fit_active_request(self, request):
        """Remove duplicate prose and bound recovery detail without dropping obligations."""
        context = request["context"]
        if "bounded_context" in context:
            context["bounded_context"]["omitted_categories"] = list(dict.fromkeys(
                context["bounded_context"].get("omitted_categories", [])))
        visible = {item["id"]: item for item in context.get("evidence", []) if item.get("content")}
        for item in context["memory"]["retrieved_records"]:
            if item["kind"] == "evidence" and item["id"] in visible:
                item["value"].pop("content", None)
                item["content_location"] = {"field": "context.evidence", "id": item["id"]}
        # Retrieved working records can duplicate the same prose delivered in
        # the mandatory working set. Retain their exact retrieval hashes and
        # evidence roots, and point to the visible copy instead of paying for
        # both. A record outside that view must keep its delivered value.
        for kind, field in (("project", "projects"), ("notebook", "notebooks"),
                            ("research", "research"), ("commitment", "commitments")):
            working_ids = {item["id"] for item in context.get(field, [])}
            for item in context["memory"]["retrieved_records"]:
                if item["kind"] == kind and item["id"] in working_ids:
                    item["value"] = {key: item["value"][key] for key in
                                     ("id", "status", "evidence") if key in item["value"]}
                    item["content_location"] = {"field": "context." + field, "id": item["id"]}
                    item["context_excerpt"] = True
        if len(canonical(request)) <= self.config["max_context_chars"]:
            return
        # The detailed core prompt duplicates the response contract and research
        # guidance. Compact only that prefix, preserving application, memory,
        # probe and operator-question instructions verbatim. History is untouched.
        from .prompts import BOUNDED_SYSTEM
        if request.get("system", "").startswith(SYSTEM):
            request["system"] = BOUNDED_SYSTEM + request["system"][len(SYSTEM):]
            context.setdefault("bounded_context", {}).setdefault("omitted_categories", []).append(
                "core instruction prose compacted; response schema and governance unchanged")
            if len(canonical(request)) <= self.config["max_context_chars"]:
                return
        # Keep every memory trust/omission rule while avoiding a larger research
        # or matrix omission merely to carry verbose explanatory instructions.
        from .memory import BOUNDED_ACTIVE_MEMORY_SYSTEM
        if ACTIVE_MEMORY_SYSTEM in request.get("system", ""):
            request["system"] = request["system"].replace(
                ACTIVE_MEMORY_SYSTEM, BOUNDED_ACTIVE_MEMORY_SYSTEM, 1)
            context.setdefault("bounded_context", {}).setdefault("omitted_categories", []).append(
                "active-memory instruction prose compacted; trust and retrieval boundaries unchanged")
            if len(canonical(request)) <= self.config["max_context_chars"]:
                return
        if context.pop("evidence_quality", None) is not None:
            context["bounded_context"]["omitted_categories"].append("advisory source-selection diagnostics")
            if len(canonical(request)) <= self.config["max_context_chars"]:
                return
        # Review alternatives repeat new citation IDs in both context and schema.
        # Bound this optional choice set before shortening source material; every
        # offered review still requires a genuinely new delivered evidence root.
        reviews = context.get("proposal_constraints", {}).get("belief_reviews", {})
        if reviews:
            # Share an eligible new root across reviews where possible. Picking
            # each list's first ID independently repeats otherwise equivalent
            # schema alternatives and can permanently starve the matrix sidecar.
            # Never invent eligibility or remove a belief: this is only a choice
            # among each review's already supplied new roots.
            pending = {key: set(review["new_evidence_ids"])
                       for key, review in reviews.items() if review["new_evidence_ids"]}
            while pending:
                candidates = set().union(*pending.values())
                root = min(candidates, key=lambda value: (
                    -sum(value in eligible for eligible in pending.values()), value))
                covered = [key for key, eligible in pending.items() if root in eligible]
                for key in covered:
                    reviews[key]["new_evidence_ids"] = [root]
                    del pending[key]
            request["response_schema"] = _provider_response_schema(context, True)
            context.setdefault("bounded_context", {}).setdefault("omitted_categories", []).append(
                "belief review choices bounded to one new visible root per belief; durable roots unchanged")
            if len(canonical(request)) <= self.config["max_context_chars"]:
                return
        recovery = context.get("representation_recovery", [])
        if recovery:
            context["representation_recovery"] = [{
                "project": item["project"], "record_hash": item.get("record_hash") or digest(item),
                "context_excerpt": True, "details_omitted": True,
                "capability_blocked": bool(item.get("capability_blocked") or item.get("capability", {}).get("capability_blocked")),
                "parked_project": item.get("parked_project") or item.get("parked", {}).get("id"),
                "frames": [{key: frame[key] for key in ("id", "observations") if key in frame}
                           for frame in item.get("frames", [])],
                "intervening_experience": item.get("intervening_experience", []),
            } for item in recovery]
            context["bounded_context"]["omitted_categories"].append("extended recovery prose; project/frame and observation pointers retained")
        if len(canonical(request)) > self.config["max_context_chars"]:
            for item in context.get("evidence", []):
                if len(item.get("content", "")) > 900:
                    item["content"] = item["content"][:899] + "…"
                    item["context_excerpt"] = True
            context["bounded_context"]["omitted_categories"].append("extended evidence excerpts; all visible evidence IDs retained")
        if len(canonical(request)) > self.config["max_context_chars"]:
            for category, fields in (("beliefs", ("statement", "reason", "falsifier")),
                                     ("notebooks", ("summary", "findings", "limitations")),
                                     ("projects", ("question", "next_step", "reason"))):
                for item in context.get(category, []):
                    for field in fields:
                        if isinstance(item.get(field), str) and len(item[field]) > 180:
                            item[field] = item[field][:179] + "…"
                            item["context_excerpt"] = True
            context["bounded_context"]["omitted_categories"].append("extended working prose; all belief/project/notebook identities and roots retained")
        # Same-wake retrieval links and the final proposal instructions arrive
        # after the initial fit. Reserve their space by shortening source prose
        # again, without removing records, provenance, or durable obligations.
        if len(canonical(request)) > self.config["max_context_chars"]:
            for item in context.get("evidence", []):
                if len(item.get("content", "")) > 400:
                    item["content"] = item["content"][:399] + "…"
                    item["context_excerpt"] = True
            note = "shorter source excerpts; all visible evidence IDs and provenance retained"
            if note not in context["bounded_context"]["omitted_categories"]:
                context["bounded_context"]["omitted_categories"].append(note)
        if len(canonical(request)) > self.config["max_context_chars"]:
            research = context.get("same_wake_research", {})
            for item in research.get("requests", []):
                item.setdefault("record_hash", digest(item))
                if len(item.get("query", "")) > 180:
                    item["query"] = item["query"][:179] + "…"
                    item["context_excerpt"] = True
                if item.get("url"):
                    item["url_hash"] = digest(item.pop("url"))
                    item["url_omitted"] = True
            # Retrieved beliefs already appear in the mandatory belief working
            # set. Point at that copy while keeping the exact retrieval hash.
            beliefs = {item["id"] for item in context.get("beliefs", [])}
            for item in context["memory"]["retrieved_records"]:
                if item["kind"] == "belief" and item["id"] in beliefs:
                    item["value"] = {key: item["value"][key] for key in
                                     ("id", "status", "confidence", "evidence") if key in item["value"]}
                    item["content_location"] = {"field": "context.beliefs", "id": item["id"]}
                    item["context_excerpt"] = True
            for compact in context["memory"].get("trust_compacts", []):
                if len(compact.get("rule", "")) > 80:
                    compact.setdefault("rule_hash", digest(compact["rule"]))
                    compact["rule"] = compact["rule"][:79] + "…"
                    compact["context_excerpt"] = True
        if len(canonical(request)) > self.config["max_context_chars"]:
            for category, fields in (("beliefs", ("statement", "reason", "falsifier")),
                                     ("notebooks", ("title", "summary", "findings", "limitations")),
                                     ("projects", ("title", "question", "next_step", "reason")),
                                     ("recent_blog", ("title", "summary", "body"))):
                for item in context.get(category, []):
                    for field in fields:
                        if isinstance(item.get(field), str) and len(item[field]) > 80:
                            item[field] = item[field][:79] + "…"
                            item["context_excerpt"] = True
        for count in (4, 2, 0):
            compacts = context["memory"].get("trust_compacts", [])
            if len(canonical(request)) > self.config["max_context_chars"] and len(compacts) > count:
                # These are optional derived hints, ordered with challenges
                # first. Mandatory beliefs and obligations stay in the context.
                omitted = compacts[count:]
                omissions = context["memory"]["omissions"]
                omissions["compact_count"] += len(omitted)
                omissions["budget_compact_digest"] = digest({
                    "previous": omissions.get("budget_compact_digest"), "omitted": omitted})
                context["memory"]["trust_compacts"] = compacts[:count]

        # Prior finding prose helps compare revisions, but its exact identity and
        # eligible new-source IDs are the necessary contract. Never let those
        # optional excerpts crowd out the mechanical recovery boundary.
        if len(canonical(request)) > self.config["max_context_chars"]:
            for item in context.get("proposal_constraints", {}).get("notebook_revisions", {}).values():
                if item.pop("prior_findings_excerpt", None) is not None:
                    item["prior_findings_omitted"] = True
            note = "prior notebook finding prose; artifact hashes and new-source eligibility retained"
            if note not in context["bounded_context"]["omitted_categories"]:
                context["bounded_context"]["omitted_categories"].append(note)

        # Milestone editorial history is optional model input, not an obligation
        # or evidence root. Its longitudinal window can dominate a final request
        # even after all research prose has been excerpted. Bound that window too,
        # recording its original identity rather than silently erasing history.
        history = context.get("reflection_history")
        if len(canonical(request)) > self.config["max_context_chars"] and isinstance(history, dict):
            history.setdefault("record_hash", digest(history))
            history.setdefault("window_counts", {key: len(value) for key, value in history.items()
                                                  if isinstance(value, list)})
            history["context_excerpt"] = True
            note = "editorial reflection history excerpted; original window hash/counts retained, no missing content may be inferred"
            if note not in context["bounded_context"]["omitted_categories"]:
                context["bounded_context"]["omitted_categories"].append(note)
            for key, value in history.items():
                records = value if isinstance(value, list) else [value] if isinstance(value, dict) else []
                for item in records:
                    if not isinstance(item, dict):
                        continue
                    for field in ("title", "summary", "body_excerpt", "lede", "lens", "next_step", "query", "last_reason"):
                        if isinstance(item.get(field), str) and len(item[field]) > 80:
                            item[field] = item[field][:79] + "…"
            # Prefer a short longitudinal wake window over extra editorial
            # copies of projects/notebooks already represented in research context.
            for key in history["window_counts"]:
                if key != "accepted_wakes":
                    history[key] = []
            history["omitted_counts"] = {key: total - len(history[key])
                                         for key, total in history["window_counts"].items()}
            for count in (4, 2, 1, 0):
                if len(canonical(request)) <= self.config["max_context_chars"]:
                    break
                history["accepted_wakes"] = history.get("accepted_wakes", [])[-count:] if count else []
                history["omitted_counts"] = {key: total - len(history[key])
                                             for key, total in history["window_counts"].items()}

        # Blog eligibility is an editorial index, not a second notebook view.
        # Its titles duplicate working/retrieved notebooks and grow independently
        # of the source budget. Keep eligibility, revisions and evidence roots,
        # but omit display prose only when the final assembled request overflows.
        if len(canonical(request)) > self.config["max_context_chars"]:
            index = context.get("blog_notebooks", {})
            if index:
                context.setdefault("blog_notebooks_hash", digest(index))
            for notebooks in index.values():
                for item in notebooks:
                    if "title" in item:
                        item.pop("title")
                        item["title_omitted"] = True
            note = "editorial notebook titles omitted; eligibility, revisions and evidence roots retained"
            if note not in context["bounded_context"]["omitted_categories"]:
                context["bounded_context"]["omitted_categories"].append(note)
        if len(canonical(request)) > self.config["max_context_chars"]:
            for item in context.get("evidence", []):
                if len(item.get("content", "")) > 180:
                    item["content"] = item["content"][:179] + "…"
                    item["context_excerpt"] = True
            note = "minimal source excerpts; all evidence identities and provenance retained"
            if note not in context["bounded_context"]["omitted_categories"]:
                context["bounded_context"]["omitted_categories"].append(note)
        # Several assembly phases may refit one request. A compaction receipt is
        # a set of applied transformations, not an ever-growing retry transcript.
        if "bounded_context" in context:
            context["bounded_context"]["omitted_categories"] = list(dict.fromkeys(
                context["bounded_context"].get("omitted_categories", [])))
            # Audit explanations can themselves crowd out a probe after research
            # grows. Keep every category, shortening only its display label.
            # Unknown/new labels remain verbatim instead of silently disappearing.
            if len(canonical(request)) > self.config["max_context_chars"]:
                context["bounded_context"]["omitted_categories"] = list(dict.fromkeys(
                    COMPACT_OMISSION_LABELS.get(label, label)
                    for label in context["bounded_context"]["omitted_categories"]))
        if len(canonical(request)) > self.config["max_context_chars"]:
            fields = {"belief": "beliefs", "evidence": "evidence",
                      "project": "projects", "notebook": "notebooks",
                      "commitment": "commitments", "research": "research"}
            for item in context["memory"]["retrieved_records"]:
                field = fields.get(item["kind"])
                location = {"field": "context." + field, "id": item["id"]} if field else None
                record = next((value for value in context.get(field, [])
                               if value.get("id") == item["id"]), None) if field else None
                if record is None or item.get("content_location") != location:
                    continue
                value = item["value"]
                # Preserve conflicting provenance as explicit material. A full
                # record pointer may replace identical fields, never a different
                # source or evidence-root set that still needs reconciliation.
                if any(key in value and value[key] != record.get(key)
                       for key in ("evidence", "source")):
                    continue
                for key in list(value):
                    if key in record and value[key] == record[key]:
                        value.pop(key)

    def fit_bounded_request(self, request):
        """Deterministically shrink an already-bounded provider request below the hard ceiling.

        This is an emergency delivery adaptation only. Exact durable state is untouched.
        Preserve IDs, active project frames, Attention routing, milestone identity, and
        provenance roots while dropping duplicated prose and oversized recovery detail.
        """
        from .providers import BOUNDED_RESEARCH_SYSTEM

        context = request["context"]
        limit = self.config["max_context_chars"]
        # The rich research prompt explains every rule at human-documentation depth.
        # Under overflow, keep the same model-facing contract in compressed form;
        # deterministic governance remains the authority after generation.
        request["system"] = SYSTEM + BOUNDED_RESEARCH_SYSTEM
        if isinstance(context.get("continuity_probe"), dict):
            request["system"] += MATRIX_SIDECAR_SYSTEM

        def excerpt(value, size):
            value = str(value or "")
            return value if len(value) <= size else value[:size - 1] + "…"

        bounded = context.setdefault("bounded_context", {})
        omitted = list(bounded.get("omitted_categories", []))
        for item in (
            "verbose recovery frames",
            "extended bounded reflection history",
            "redundant evidence payload text",
            "low-priority bounded prose",
        ):
            if item not in omitted:
                omitted.append(item)
        bounded["omitted_categories"] = omitted
        bounded["emergency_compaction"] = True

        # Preserve the routing decision Attention needs, not its full diagnostic payload.
        attention = context.get("attention") or {}
        context["attention"] = {
            key: attention.get(key)
            for key in (
                "active", "selected_topic", "enforce_selected_topic",
                "rotation_required", "capability_blocked_topics",
                "deferred_topics", "reason",
            )
            if key in attention
        }

        # Recovery detail is durable elsewhere; IDs are enough to signal its existence.
        context["representation_recovery"] = [
            {"project": item.get("project")}
            for item in context.get("representation_recovery", [])[-2:]
        ]

        context["beliefs"] = [
            {
                "id": item.get("id"),
                "statement": excerpt(item.get("statement"), 220),
                "confidence": item.get("confidence"),
                "status": item.get("status"),
                "evidence": list(item.get("evidence", []))[-4:],
                "context_excerpt": True,
            }
            for item in context.get("beliefs", [])[-4:]
        ]
        context["commitments"] = [
            {
                **{key: item.get(key) for key in (
                    "id", "project", "due_cycle", "status", "created_version",
                )},
                "task": excerpt(item.get("task"), 220),
                "reason": excerpt(item.get("reason"), 160),
                "resolution_evidence": list(item.get("resolution_evidence", []))[-3:],
                "context_excerpt": True,
            }
            for item in context.get("commitments", [])[-4:]
        ]

        # Evidence content is never authoritative in this emergency view; retain roots only.
        synthesis_ids = {
            evidence_id
            for ids in context.get("project_evidence", {}).values()
            for evidence_id in ids
        }
        context["evidence"] = [
            {
                "id": item.get("id"),
                "source": item.get("source", ""),
                "actor": item.get("actor", ""),
                "version": item.get("version"),
                "scope": item.get("scope"),
                **(
                    {
                        "content": excerpt(item.get("content"), 500),
                        "context_excerpt": True,
                    }
                    if item.get("id") in synthesis_ids and item.get("content")
                    else {"content_omitted": True}
                ),
            }
            for item in context.get("evidence", [])[-6:]
        ]

        # Preserve active work and unfinished work on the selected topic even
        # under emergency compaction. Pure recency can erase the exact project a
        # fresh model is supposed to resume.
        project_candidates = context.get("projects", [])
        selected_topic = context.get("attention", {}).get("selected_topic")
        active_candidates = [p for p in project_candidates if p.get("status") == "active"]
        active_ids = {p.get("id") for p in active_candidates}
        selected_candidates = [
            p for p in project_candidates
            if p.get("id") not in active_ids
            and selected_topic
            and p.get("domain") == selected_topic
            and p.get("status") != "completed"
        ]
        priority_candidates = active_candidates + selected_candidates
        priority_ids = {p.get("id") for p in priority_candidates}
        other_candidates = [p for p in project_candidates if p.get("id") not in priority_ids]
        compact_projects = priority_candidates[:3]
        remaining_compact_slots = max(0, 3 - len(compact_projects))
        if remaining_compact_slots:
            compact_projects += other_candidates[-remaining_compact_slots:]
        context["projects"] = [
            {
                **{key: value for key, value in item.items()
                   if key not in ("title", "question", "next_step", "reason")},
                "title": excerpt(item.get("title"), 120),
                "question": excerpt(item.get("question"), 180),
                "next_step": excerpt(item.get("next_step"), 180),
                "reason": excerpt(item.get("reason"), 120),
                "context_excerpt": True,
            }
            for item in compact_projects
        ]

        context["notebooks"] = [
            {
                "id": item.get("id"), "project": item.get("project"),
                "title": excerpt(item.get("title"), 120),
                "summary": excerpt(item.get("summary"), 180),
                "revision": item.get("revision"),
                "evidence": list(item.get("evidence", []))[-3:],
                "context_excerpt": True,
            }
            for item in context.get("notebooks", [])[-2:]
        ]
        context["blog_notebooks"] = {}
        for notebook in context["notebooks"]:
            context["blog_notebooks"].setdefault(notebook.get("project"), []).append({
                key: notebook.get(key) for key in ("id", "title", "revision", "evidence")
            })

        history = context.get("reflection_history")
        if isinstance(history, dict):
            previous = history.get("previous_reflection")
            if isinstance(previous, dict):
                previous = {
                    "id": previous.get("id"),
                    "reflection_cycle": previous.get("reflection_cycle"),
                    "title": excerpt(previous.get("title"), 120),
                    "lede": excerpt(previous.get("lede"), 180),
                    "body_excerpt": excerpt(previous.get("body_excerpt"), 420),
                    "lens": excerpt(previous.get("lens"), 220),
                }
            context["reflection_history"] = {
                "milestone": history.get("milestone"),
                "accepted_wakes": [
                    {
                        "cycle": item.get("cycle"),
                        "invocation": item.get("invocation"),
                        "title": excerpt(item.get("title"), 120),
                        "summary": excerpt(item.get("summary"), 240),
                    }
                    for item in history.get("accepted_wakes", [])[-6:]
                ],
                "projects": [
                    {
                        "id": item.get("id"), "domain": item.get("domain"),
                        "status": item.get("status"),
                        "title": excerpt(item.get("title"), 100),
                        "next_step": excerpt(item.get("next_step"), 140),
                    }
                    for item in history.get("projects", [])[-4:]
                ],
                "research": [
                    {
                        "id": item.get("id"), "project": item.get("project"),
                        "domain": item.get("domain"), "status": item.get("status"),
                        "query": excerpt(item.get("query"), 140),
                    }
                    for item in history.get("research", [])[-4:]
                ],
                "notebooks": [
                    {
                        "id": item.get("id"), "project": item.get("project"),
                        "revision": item.get("revision"),
                        "title": excerpt(item.get("title"), 100),
                        "summary": excerpt(item.get("summary"), 160),
                    }
                    for item in history.get("notebooks", [])[-3:]
                ],
                "acquisition_friction": [
                    {
                        "project": item.get("project"),
                        "no_progress": item.get("no_progress"),
                        "capability_blocked": item.get("capability_blocked"),
                        "last_outcome": item.get("last_outcome"),
                        "last_reason": excerpt(item.get("last_reason"), 140),
                    }
                    for item in history.get("acquisition_friction", [])[-4:]
                ],
                "previous_reflection": previous,
                "boundary": history.get("boundary"),
            }

        # Rebuild dependent allowlists after trimming. If still oversized, strip
        # nonessential prose one final time while retaining action identities.
        request["response_schema"] = _provider_response_schema(context, True)
        if len(canonical(request)) > limit:
            context["beliefs"] = []
            context["representation_recovery"] = []
            if isinstance(context.get("reflection_history"), dict):
                context["reflection_history"]["research"] = []
                context["reflection_history"]["notebooks"] = []
                context["reflection_history"]["acquisition_friction"] = []
            request["response_schema"] = _provider_response_schema(context, True)

        # Before degrading the only readable source, collapse competing
        # working-set material around one synthesis-ready project. Without this
        # step, a runtime that lives near the context ceiling can repeatedly hit
        # the final safety valve and starve notebook creation forever.
        if len(canonical(request)) > limit and self.focus_synthesis_delivery(context):
            request["response_schema"] = _provider_response_schema(context, True)

        # Very small configured ceilings (including compaction tests) may not
        # have room for the normal 500-character synthesis excerpts. Degrade
        # source prose before abandoning the synthesis signal entirely.
        if len(canonical(request)) > limit:
            for item in context.get("evidence", []):
                if item.get("content"):
                    item["content"] = excerpt(item["content"], 160)
                    item["context_excerpt"] = True
            request["response_schema"] = _provider_response_schema(context, True)

        # Absolute safety valve: if even the focused single-project handoff plus
        # tiny readable excerpts cannot fit, preserve provenance roots and suppress
        # synthesis for this invocation. Normal production ceilings should reach
        # the focused path above; this branch is reserved for genuinely impossible
        # delivery budgets and deliberately exposes that loss in bounded_context.
        if len(canonical(request)) > limit:
            context["evidence"] = [
                {
                    "id": item.get("id"),
                    "source": item.get("source", ""),
                    "actor": item.get("actor", ""),
                    "version": item.get("version"),
                    "scope": item.get("scope"),
                    "content_omitted": True,
                }
                for item in context.get("evidence", [])
            ]
            context["project_evidence"] = {}
            context["synthesis_ready_projects"] = []
            context["retrieval_rehydration"] = {
                "evidence_ids": [],
                "boundary": (
                    "Configured provider ceiling could not fit readable synthesis "
                    "excerpts; exact records remain durable for a later invocation."
                ),
            }
            request["response_schema"] = _provider_response_schema(context, True)

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
    def topic_definition(self, state, domain):
        return next((topic for topic in state.get("research_topics", []) if topic.get("id") == domain), None)

    def repository_topic(self, state, domain):
        topic = self.topic_definition(state, domain)
        return topic if topic and topic.get("source_kind") == "repository" else None

    def repository_raw_prefix(self, state, domain):
        topic = self.repository_topic(state, domain)
        if not topic:
            return None
        return "https://raw.githubusercontent.com/" + topic["repository"] + "/"

    def durable_notebook_source_payload(self, state, evidence_id):
        """Return full durable source metadata only when a notebook may consider it.

        Provider-context evidence may be excerpted, so eligibility must never be
        inferred by reparsing the delivered copy. The durable record is the
        authoritative source for role/scope metadata.
        """
        evidence = state.get("evidence", {}).get(evidence_id)
        if not evidence or evidence.get("actor") != "collector" or evidence.get("scope") != "collected":
            return None
        try:
            payload = json.loads(evidence.get("content", ""))
        except (ValueError, TypeError):
            return None
        if not isinstance(payload, dict):
            return None
        role = effective_evidence_role(evidence.get("source", ""), payload)
        tier = effective_host_tier(evidence.get("source", ""), payload)
        if role != "source" or tier == "verification-metadata":
            return None
        if not source_observation_readable(payload):
            return None
        if payload.get("verification_required") is True:
            topic_domain = payload.get("topic_domain")
            if not isinstance(topic_domain, str) or not topic_domain.strip():
                return None
        return payload

    def notebook_qualifying_evidence_ids(self, state, notebook):
        """Return notebook citations that still qualify under current source rules.

        Historical notebooks remain durable even when their old evidence contract
        is no longer strong enough. Current maturation/provider context must not
        mistake those artifacts for valid present-day synthesis.
        """
        return [
            evidence_id for evidence_id in notebook.get("evidence", [])
            if self.durable_notebook_source_payload(state, evidence_id) is not None
        ]

    def durable_source_identity(self, state, evidence_id):
        """Return work-level identity for corroboration, falling back to URL."""
        evidence = state.get("evidence", {}).get(evidence_id, {})
        try:
            payload = json.loads(evidence.get("content", ""))
        except (ValueError, TypeError):
            payload = {}
        explicit = str(payload.get("source_identity") or "").strip().lower() if isinstance(payload, dict) else ""
        if explicit:
            return explicit
        # IDs discovered inside article text are retrieval leads, not
        # authoritative work identity. Explicit collector provenance is required
        # to collapse mirrors; historical records otherwise remain URL-distinct.
        return "url:" + str(evidence.get("source") or "").strip().lower()

    def commitment_resolution_evidence_ids(self, state, evidence_ids, commitment):
        """Return visible evidence eligible to fulfill one durable commitment.

        Legacy generic commitments retain the historical temporal gate. New
        research commitments carry a project ID and may resolve only from
        substantive collected evidence stamped to that project's topic.
        """
        created_version = commitment.get("created_version", 0)
        project_id = commitment.get("project")
        if not project_id:
            return [
                evidence_id for evidence_id in evidence_ids
                if evidence_id in state.get("evidence", {})
                and state["evidence"][evidence_id].get("actor") != "runtime"
                and state["evidence"][evidence_id].get("version", -1) >= created_version
            ]
        project = state.get("projects", {}).get(project_id)
        if not project:
            return []
        eligible = set(self.project_notebook_evidence_ids(
            state, evidence_ids, project, same_domain=True
        ))
        return [
            evidence_id for evidence_id in evidence_ids
            if evidence_id in eligible
            and state["evidence"][evidence_id].get("version", -1) >= created_version
        ]

    def project_notebook_evidence_ids(self, state, evidence_ids, project, *, same_domain=False):
        """Filter evidence IDs using authoritative durable metadata.

        Cross-topic source evidence remains available to the model because
        governance can accept materially relevant cross-topic support. The
        same_domain switch is only an attention/retrieval signal: an active
        project should not be considered serviced merely because some unrelated
        source happens to be visible.
        """
        eligible = []
        for evidence_id in evidence_ids:
            payload = self.durable_notebook_source_payload(state, evidence_id)
            if payload is None:
                continue
            evidence = state["evidence"][evidence_id]
            repository_prefix = self.repository_raw_prefix(state, project.get("domain"))
            if repository_prefix and not evidence.get("source", "").startswith(repository_prefix):
                continue
            if same_domain:
                # WAKE repository files are intrinsically domain-scoped by their
                # source boundary, including legacy records that predate an
                # explicit topic_domain stamp.
                if not self.repository_topic(state, project.get("domain")) and payload.get("topic_domain") != project.get("domain"):
                    continue
            eligible.append(evidence_id)
        return eligible

    def research_maturation(self, state):
        """Derive research-stage pressure and transition telemetry from durable state.

        This is a read-only projection: it does not add a mutable project status
        or weaken governance. Corroboration means two distinct source URLs already
        accepted into a notebook, not a claim that the sources are independent or true.
        """
        evidence_ids = list(state.get("evidence", {}))
        projects = []
        transition_cycles = {
            "project_to_first_evidence": [],
            "project_to_first_notebook": [],
            "first_notebook_to_corroboration": [],
        }
        stage_counts = {
            "needs_evidence": 0,
            "needs_synthesis": 0,
            "needs_corroboration": 0,
            "completion_ready": 0,
        }
        for project in state.get("projects", {}).values():
            if project.get("status") != "active":
                continue
            same_domain = self.project_notebook_evidence_ids(
                state, evidence_ids, project, same_domain=True
            )
            historical_notebooks = [
                item for item in state.get("notebooks", {}).values()
                if item.get("project") == project.get("id")
            ]
            notebooks = [
                item for item in historical_notebooks
                if self.notebook_qualifying_evidence_ids(state, item)
            ]
            latest = notebooks[-1] if notebooks else None

            def distinct_sources(notebook):
                return {
                    self.durable_source_identity(state, evidence_id)
                    for evidence_id in self.notebook_qualifying_evidence_ids(state, notebook)
                    if evidence_id in state.get("evidence", {})
                    and state["evidence"][evidence_id].get("source")
                }

            corroborated = [item for item in notebooks if len(distinct_sources(item)) >= 2]
            if not latest:
                if same_domain:
                    stage = "needs_synthesis"
                    missing = "provisional notebook"
                    priority = 2
                else:
                    stage = "needs_evidence"
                    missing = "first qualifying source"
                    priority = 1
            elif len(distinct_sources(latest)) < 2:
                stage = "needs_corroboration"
                missing = "targeted corroborating source"
                priority = 3
            else:
                stage = "completion_ready"
                missing = "completion review"
                priority = 4
            stage_counts[stage] += 1

            created = project.get("created_version")
            first_evidence = min(
                (state["evidence"][item].get("version") for item in same_domain
                 if type(state["evidence"][item].get("version")) is int),
                default=None,
            )
            first_notebook = min(
                (item.get("created_version") for item in notebooks
                 if type(item.get("created_version")) is int),
                default=None,
            )
            first_corroborated = min(
                ((item.get("updated_version")
                  if type(item.get("updated_version")) is int
                  else item.get("created_version"))
                 for item in corroborated
                 if type(item.get("updated_version")) is int
                 or type(item.get("created_version")) is int),
                default=None,
            )
            if type(created) is int and type(first_evidence) is int:
                transition_cycles["project_to_first_evidence"].append(max(0, first_evidence - created))
            if type(created) is int and type(first_notebook) is int:
                transition_cycles["project_to_first_notebook"].append(max(0, first_notebook - created))
            if type(first_notebook) is int and type(first_corroborated) is int:
                transition_cycles["first_notebook_to_corroboration"].append(
                    max(0, first_corroborated - first_notebook)
                )

            projects.append({
                "id": project["id"],
                "domain": project.get("domain"),
                "stage": stage,
                "priority": priority,
                "qualifying_same_domain_sources": len({
                    state["evidence"][item].get("source") for item in same_domain
                    if state["evidence"][item].get("source")
                }),
                "notebook_count": len(notebooks),
                "historical_notebook_count": len(historical_notebooks),
                "notebook_source_urls": len(distinct_sources(latest)) if latest else 0,
                "missing_requirement": missing,
            })

        projects.sort(key=lambda item: (-item["priority"], item["id"]))
        return {
            "projects": projects,
            "priority_order": [item["id"] for item in projects],
            "metrics": {
                "active_projects": len(projects),
                "stage_counts": stage_counts,
                "transition_cycles": transition_cycles,
                "boundary": (
                    "Derived from durable project/evidence/notebook records. "
                    "Completion-ready requires two distinct URLs in an accepted notebook; "
                    "this is workflow pressure, not proof of source independence or truth."
                ),
            },
        }

    def context(self, state, receipt):
        # Recent receipts and the newest supporting evidence for every belief stay visible.
        # All citation IDs remain in beliefs; full evidence is always in the durable export.
        # Persistence canonicalizes object keys, so dictionary iteration order is
        # not chronology after a fresh process reload. Select recent evidence by
        # durable observation metadata instead of random evidence IDs.
        recent_evidence = sorted(
            state["evidence"].items(),
            key=lambda item: (item[1].get("version", -1), item[1].get("time", ""), item[0]),
        )[-6:]
        wanted = {evidence_id for evidence_id, _ in recent_evidence}
        for belief in state["beliefs"].values():
            wanted.update(belief["evidence"][-3:])
        ordered_evidence = sorted(
            ((evidence_id, state["evidence"][evidence_id]) for evidence_id in wanted),
            key=lambda item: (item[1].get("version", -1), item[1].get("time", ""), item[0]),
        )
        context = {"version": state["version"], "objective": state["objective"], "focus": state["focus"],
                "receipt": receipt, "beliefs": list(state["beliefs"].values()),
                "commitments": [c for c in state["commitments"].values() if c["status"] == "open"],
                "acquisition": state.get("acquisition", {}),
                "evidence": [evidence for _, evidence in ordered_evidence],
                "recent_journal": state["journal"][-3:],
            "evidence_scope": "Recent observations plus newest three citations per belief; full evidence remains in history."}
        if state.get("experimental"):
            context["experimental_regime"] = {
                "id": state["experimental"]["id"], "controls": state["experimental"]["controls"],
                "boundary": "Operator-recorded regime. It informs context only; it does not relax governance or evidence rules.",
            }
            context["temporal"] = state.get("temporal", {})
        if state.get("charter"):
            context["mission"] = state["charter"]
            context["acquisition"] = state.get("acquisition", {})
            # Bounded, receipt-derived recovery view.  The provider can inspect
            # a stuck problem and intervening durable work without treating
            # either as evidence or inventing a connection between them.
            recovery = []
            for project_id, summary in state.get("acquisition", {}).items():
                if not summary.get("capability_blocked"):
                    continue
                project = state.get("projects", {}).get(project_id, {})
                recovery.append({"project": project_id, "question": project.get("question", ""),
                                 "blocker": summary.get("last_receipt", {}),
                                 "frames": state.get("representations", {}).get(project_id, [])[-3:],
                                 "open_commitments": [c["id"] for c in state.get("commitments", {}).values()
                                                      if c.get("status") == "open"],
                                 "intervening_experience": [e["id"] for e in list(state.get("evidence", {}).values())[-8:]
                                                            if e.get("actor") == "collector"]})
            context["representation_recovery"] = recovery
            for topic, parked in state.get("attention", {}).get("deferred", {}).items():
                for item in parked.get("parked_projects", []):
                    if any(entry["project"] == item["id"] for entry in recovery):
                        continue
                    recovery.append({"project": item["id"], "question": item.get("question", ""),
                                     "blocker": {"kind": "attention_deferral", "reason": parked.get("reason")},
                                     "frames": state.get("representations", {}).get(item["id"], [])[-3:],
                                     "open_commitments": [c["id"] for c in state.get("commitments", {}).values()
                                                          if c.get("status") == "open"],
                                     "intervening_experience": [e["id"] for e in list(state.get("evidence", {}).values())[-8:]
                                                                if e.get("actor") == "collector"]})
            context["observation_mode"] = {
                "active": self.config["observation_mode"],
                "boundary": "This is an overnight data-gathering profile. Record promising leads and failed approaches freely, but governance still decides what qualifies as evidence or a completed obligation.",
            }
            context["attention"] = {**attention_plan(state), "temporal": state.get("temporal", {}),
                                   "temporal_use": "observational; no time signal changes Attention eligibility yet"}
            context["pet_name"] = state["pet_name"]
            context["project_name"] = state["pet_name"]
            topics = state.get("research_topics") or self.config.get("research_topics", [])
            topics = [topic for topic in topics if topic.get("enabled", True)]
            projects = list(state["projects"].values())
            # Seeds are consumed by circumstance rather than mutated away.  Once
            # a topic owns any project, the seed disappears from provider context;
            # durable projects/questions take over and can wander, fail, or be
            # re-represented normally.  This keeps the seed from becoming a
            # repeated fixation instruction while retaining exact provenance in
            # the audited topic-configuration event.
            project_domains = {project.get("domain") for project in projects}
            context["research_topics"] = [
                {key: value for key, value in topic.items()
                 if key != "seed_question" or topic["id"] not in project_domains}
                for topic in topics
            ]
            context["seed_questions"] = [
                {"topic": topic["id"], "question": topic["seed_question"]}
                for topic in context["research_topics"] if topic.get("seed_question")
            ]
            context["seed_question_metrics"] = {
                "configured": sum(bool(topic.get("seed_question")) for topic in topics),
                "available": len(context["seed_questions"]),
                "started": sum(topic["id"] in project_domains and bool(topic.get("seed_question")) for topic in topics),
                "boundary": "Derived from audited topic configuration and durable project domains; seeds do not count as evidence."
            }
            # Keep project context bounded, but spend the parked-project budget
            # on the topic WAKE is actually being asked to work on. Otherwise old
            # unfinished work falls out of view and a fresh model can reinvent it
            # under a new ID instead of resuming the durable project.
            active_projects = [p for p in projects if p["status"] == "active"]
            nonactive_projects = [p for p in projects if p["status"] != "active"]
            selected_topic = context.get("attention", {}).get("selected_topic")
            selected_nonactive = [
                p for p in nonactive_projects
                if selected_topic and p.get("domain") == selected_topic
                and p.get("status") != "completed"
            ]
            selected_ids = {p["id"] for p in selected_nonactive}
            other_nonactive = [p for p in nonactive_projects if p["id"] not in selected_ids]
            selected_visible = selected_nonactive[-8:]
            remaining_project_slots = max(0, 8 - len(selected_visible))
            recent_other_visible = (
                other_nonactive[-remaining_project_slots:]
                if remaining_project_slots else []
            )
            visible_nonactive = selected_visible + recent_other_visible
            context["projects"] = active_projects + visible_nonactive
            usable_notebooks = [
                notebook for notebook in state["notebooks"].values()
                if self.notebook_qualifying_evidence_ids(state, notebook)
            ]
            context["notebooks"] = [
                {k:n[k] for k in ("id", "project", "title", "summary", "revision", "evidence")}
                for n in usable_notebooks[-8:]
            ]
            # Only notebooks that still satisfy the current substantive-source
            # contract may drive new publication or working synthesis. Historical
            # invalid notebooks remain in the durable/public audit.
            context["blog_notebooks"] = {}
            for notebook in usable_notebooks:
                context["blog_notebooks"].setdefault(notebook["project"], []).append(
                    {k:notebook[k] for k in ("id", "title", "revision", "evidence")}
                )
            working = [
                n for n in usable_notebooks
                if state["projects"][n["project"]]["status"] == "active"
            ]
            context["working_notebook"] = ({**working[-1], "findings": working[-1]["findings"][:3000],
                                           "context_excerpt": True} if working else None)
            context["research"] = list(state["research"].values())[-8:]
            context["recent_blog"] = [
                {**{key: post.get(key) for key in ("id", "project", "title", "lede", "lens", "created_version", "reflection_cycle",
                                                  "status", "supersedes", "superseded_by")},
                 "retractable_quotes": retractable_quotes(post)}
                for post in list(state.get("posts", {}).values())[-4:]
            ]
            # Bob receives a required editorial checkpoint after the opening
            # cycle and again after a stable quiet window. The provider must propose
            # it, but publication remains a sidecar and research never depends on it.
            context["bob_reflection_cycle"] = bob_reflection_due_cycle(state)
            context["bob_reflection_due"] = context["bob_reflection_cycle"] is not None
            context["reflection_history"] = (
                self.bob_reflection_history(state) if context["bob_reflection_due"] else None
            )
            # Source-controlled operator review notes are editorial context, not research evidence.
            # They can flag prior public wording for reconsideration without rewriting history.
            context["editorial_notes"] = list(self.config.get("editorial_notes", []))
            # Research excerpts are bounded. Full snapshots remain available in the lab.
            collector_sources = [v for v in state["evidence"].values()
                                 if v.get("actor") == "collector"]
            # Keep the ordinary research feed small, then reserve a compact,
            # distinct-URL budget for WAKE self-analysis.  The latter must have
            # at least two usable repository files, but carrying every repeated
            # README/source snapshot makes the response schema itself exceed the
            # context ceiling before a model can correct its citation choice.
            repository_prefixes = tuple(
                "https://raw.githubusercontent.com/" + topic["repository"] + "/"
                for topic in state.get("research_topics", [])
                if topic.get("source_kind") == "repository"
            )
            recent_sources = [v for v in collector_sources
                              if not repository_prefixes or not v.get("source", "").startswith(repository_prefixes)][-2:]
            repository_sources, seen_repository_urls = [], set()
            for item in reversed(collector_sources):
                source = item.get("source", "")
                if (not repository_prefixes or not source.startswith(repository_prefixes)
                        or source in seen_repository_urls):
                    continue
                repository_sources.append(item)
                seen_repository_urls.add(source)
                if len(repository_sources) == 4:
                    break
            sources = recent_sources + list(reversed(repository_sources))
            context["evidence"] = [{**e, "content": e["content"][:3000], "context_excerpt": len(e["content"]) > 3000}
                                   for e in context["evidence"] if e.get("actor") != "collector"][-3:]
            context["evidence"] += [{**e, "content": e["content"][:3000], "context_excerpt": len(e["content"]) > 3000} for e in sources]
            context["beliefs"] = [{**b, "evidence": b["evidence"][-6:]} for b in context["beliefs"]]
            outcomes = self.store.tail_events(("rejected", "failed"), 2)
            context["recent_problems"] = [e["payload"].get("reason", "") for e in outcomes]
            withheld = [i["editorial"] for i in state["invocations"].values() if i.get("editorial")][-2:]
            context["recent_problems"] += ["Blog withheld: " + note["reason"] for note in withheld]

            # Make the temporal resolution gate explicit instead of forcing the
            # disposable model to reconstruct it from hidden evidence metadata.
            # These are only IDs already present in the bounded delivered context;
            # governance remains authoritative and re-validates every citation.
            visible_evidence = {item["id"]: item for item in context["evidence"]}
            context["commitments"] = [
                {
                    **commitment,
                    "resolution_evidence": self.commitment_resolution_evidence_ids(
                        state, list(visible_evidence), commitment
                    ),
                }
                for commitment in context["commitments"]
            ]

            # Notebook provenance is also project-scoped. Expose the collector
            # evidence IDs that are eligible for each visible project so the
            # disposable model does not accidentally cross-wire domains.
            context["project_evidence"] = {}
            visible_evidence_ids = list(visible_evidence)
            for project in context["projects"]:
                # Eligibility is derived from the full durable record, not the
                # possibly truncated provider copy in visible_evidence.
                context["project_evidence"][project["id"]] = self.project_notebook_evidence_ids(
                    state, visible_evidence_ids, project
                )
            notebook_projects = {
                n.get("project") for n in state.get("notebooks", {}).values()
                if self.notebook_qualifying_evidence_ids(state, n)
            }
            context["synthesis_ready_projects"] = [
                project["id"] for project in context["projects"]
                if project.get("status") == "active"
                and context["project_evidence"].get(project["id"])
                and project["id"] not in notebook_projects
            ]
            context["research_maturation"] = self.research_maturation(state)
            self.proposal_constraints(state, context)
        return context

    def rehydrate_retrieval_context(self, state, context, retrieval_plan, content_limit=3000, max_records=3, *, force=False):
        """Materialize qualifying durable evidence selected by retrieval into provider context.

        The retrieval planner remains deterministic and ID-based. This step is the
        explicit boundary where selected durable records become visible again to a
        disposable model. It does not broaden governance: only successfully collected
        source records are rehydrated, discovery/search-result records stay excluded,
        and project-specific restrictions are rebuilt before schema generation.
        """
        if not state.get("charter"):
            return context

        requested = list(dict.fromkeys(retrieval_plan.get("evidence_ids", [])))
        existing = {item["id"] for item in context.get("evidence", [])}
        rehydrated = []

        active_projects = [
            project for project in context.get("projects", [])
            if project.get("status") == "active"
        ]
        # Metadata-only evidence roots are useful for provenance, but they are
        # not enough for a disposable model to synthesize findings. Treat only
        # collector records whose content is actually present in this request as
        # synthesis-visible. This prevents bounded context from falsely deciding
        # that a project is already serviced merely because an ID survived.
        readable_ids = [
            item["id"] for item in context.get("evidence", [])
            if item.get("actor") == "collector"
            and item.get("scope") == "collected"
            and item.get("content")
            and not item.get("content_omitted")
        ]
        missing_domains = {
            project.get("domain")
            for project in active_projects
            if not self.project_notebook_evidence_ids(
                state, readable_ids, project, same_domain=True
            )
        }
        projects_need_source = bool(missing_domains)

        # A near-due commitment is also an attention trigger when retrieval has
        # qualifying source records that are not presently visible. Do not let a
        # random human observation or unrelated source make that obligation look
        # serviced.
        hidden_requested_sources = [
            evidence_id for evidence_id in requested
            if evidence_id not in existing
            and self.durable_notebook_source_payload(state, evidence_id) is not None
        ]
        commitments_need_evidence = bool(hidden_requested_sources) and any(
            commitment.get("due_cycle", 10**9) <= state.get("version", 0) + 2
            for commitment in context.get("commitments", [])
        )
        if not force and not projects_need_source and not commitments_need_evidence:
            context["retrieval_rehydration"] = {
                "evidence_ids": [],
                "boundary": "Visible active projects already have same-domain source evidence and no near-due commitment requires hidden source recovery.",
            }
            return context

        # Prefer sources from domains that are absent for active projects while
        # preserving deterministic retrieval order inside each priority class.
        selected_topic = (context.get("attention") or {}).get("selected_topic")
        requested = sorted(
            requested,
            key=lambda evidence_id: (
                0 if (
                    (payload := self.durable_notebook_source_payload(state, evidence_id))
                    and payload.get("topic_domain") == selected_topic
                ) else 1 if (
                    payload and payload.get("topic_domain") in missing_domains
                ) else 2
            ),
        )

        repository_prefixes = tuple(
            "https://raw.githubusercontent.com/" + topic["repository"] + "/"
            for topic in state.get("research_topics", [])
            if topic.get("source_kind") == "repository"
        )
        visible_repository_urls = {
            item.get("source")
            for item in context.get("evidence", [])
            if item.get("actor") == "collector"
            and repository_prefixes
            and item.get("source", "").startswith(repository_prefixes)
        }

        for evidence_id in requested:
            payload = self.durable_notebook_source_payload(state, evidence_id)
            if payload is None:
                continue
            evidence = state["evidence"][evidence_id]

            # Preserve the existing WAKE self-analysis source budget. Retrieval
            # may replace missing attention, but it must not silently widen the
            # provider envelope beyond the four distinct repository sources that
            # context() deliberately exposes.
            source = evidence.get("source", "")
            is_repository_source = bool(repository_prefixes) and source.startswith(repository_prefixes)
            if evidence_id not in existing and is_repository_source:
                if source in visible_repository_urls or len(visible_repository_urls) >= 4:
                    continue

            rehydrated.append(evidence_id)
            visible_entry = next(
                (item for item in context.get("evidence", []) if item.get("id") == evidence_id),
                None,
            )
            needs_materialization = (
                visible_entry is None
                or not visible_entry.get("content")
                or visible_entry.get("content_omitted")
            )
            if needs_materialization:
                content = evidence.get("content", "")
                context["evidence"] = [
                    item for item in context.get("evidence", [])
                    if item.get("id") != evidence_id
                ]
                context.setdefault("evidence", []).append({
                    **evidence,
                    "content": content[:content_limit],
                    "context_excerpt": len(content) > content_limit,
                })
                existing.add(evidence_id)
                if is_repository_source:
                    visible_repository_urls.add(source)

            # One provisional notebook needs only one qualifying source; ordinary
            # rich context may carry a small comparison set. Emergency bounded
            # context can lower max_records so exact source recovery survives the
            # context ceiling without recreating the pressure that triggered it.
            if len(rehydrated) >= max_records:
                break

        context["retrieval_rehydration"] = {
            "evidence_ids": rehydrated,
            "boundary": (
                "Exact durable collector records selected by retrieval were reintroduced "
                "for this invocation; governance still decides whether any citation qualifies."
            ),
        }

        visible_evidence = {item["id"]: item for item in context.get("evidence", [])}

        # Rebuild the temporal resolution allowlist after rehydration. A near-due
        # commitment can now see qualifying post-commitment evidence that happened
        # to fall outside the ordinary recent-context slice.
        context["commitments"] = [
            {
                **commitment,
                "resolution_evidence": self.commitment_resolution_evidence_ids(
                    state, list(visible_evidence), commitment
                ),
            }
            for commitment in context.get("commitments", [])
        ]

        # Rebuild the notebook allowlist from the now-visible evidence. Topic
        # stamps are provenance rather than semantic relevance, so ordinary
        # projects may inspect cross-topic sources; WAKE self-analysis keeps its
        # stricter repository-source boundary.
        context["project_evidence"] = {}
        # Notebook choices must be evidence the model can actually read in this
        # invocation, not merely metadata roots whose exact content stayed out
        # of the bounded request.
        visible_evidence_ids = [
            evidence_id for evidence_id, evidence in visible_evidence.items()
            if evidence.get("actor") == "collector"
            and evidence.get("scope") == "collected"
            and evidence.get("content")
            and not evidence.get("content_omitted")
        ]
        for project in context.get("projects", []):
            context["project_evidence"][project["id"]] = self.project_notebook_evidence_ids(
                state, visible_evidence_ids, project
            )
        notebook_projects = {n.get("project") for n in state.get("notebooks", {}).values()}
        context["synthesis_ready_projects"] = [
            project["id"] for project in context.get("projects", [])
            if project.get("status") == "active"
            and context["project_evidence"].get(project["id"])
            and project["id"] not in notebook_projects
        ]

        return context
    def start(self, provider, model, charged=False, *, phase="proposal", question=None, research=None):
        started_at = perf_counter()
        phase_at = started_at
        state = self.store.load()
        load_ms = (perf_counter() - phase_at) * 1000
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
        # Capture the temporal environment before the next model boundary. This
        # measures a new interval; it never recalculates an earlier receipt.
        phase_at = perf_counter()
        temporal_anchor = (state.get("temporal") or {}).get(
            "anchor_seq", state["experimental"]["event_seq"]
        )
        temporal_counts = self.store.event_counts_since(
            temporal_anchor,
            ("accepted", "rejected", "failed", "observation", "research_collected", "attention_assessed"),
        )
        temporal = temporal_snapshot(state, temporal_counts, now())
        self.store.append("temporal_observed", temporal)
        state = self.store.load()
        temporal_ms = (perf_counter() - phase_at) * 1000
        invocation = "w-" + uuid.uuid4().hex[:16]
        receipt = "r-" + invocation[2:]
        phase_at = perf_counter()
        head = self.store.head()
        state = self.store.append("observation", {"id": receipt, "source": "runtime:continuity",
            "actor": "runtime", "content": canonical({"invocation": invocation, "process_id": os.getpid(),
                "base_version": state["version"], "previous_head": head,
                "inherited_commitments": [k for k, v in state["commitments"].items() if v["status"] == "open"],
                "scope": "Receipt proves state delivery to the provider boundary, not model comprehension."})})
        receipt_ms = (perf_counter() - phase_at) * 1000
        from .providers import RESEARCH_SYSTEM
        phase_at = perf_counter()
        delivered_context = self.context(state, receipt)
        if state.get("charter"):
            from .evidence_quality import evidence_quality
            quality = evidence_quality(state)
            delivered_context["evidence_quality"] = {
                key: quality[key] for key in ("distinct_works", "distinct_hosts", "largest_host_share", "cited_distinct_works", "uncited_readable_source_ids", "boundary")
            }
            delivered_context["evidence_quality"]["most_reused_works"] = sorted(
                quality["reused_works"], key=lambda item: (-item["notebook_count"], item["work"]))[:4]
        working_set_shadow = self.working_set(state)
        trust_compacts_shadow = build_trust_compacts_shadow(state)
        retrieval_shadow = build_retrieval_shadow(state, working_set_shadow, trust_compacts_shadow)
        delivered_context = self.rehydrate_retrieval_context(
            state, delivered_context, retrieval_shadow
        )
        continuity_probe_context = None
        matrix_progress = (
            self.store.continuity_matrix_progress()
            if hasattr(self.store, "continuity_matrix_progress")
            else None
        )
        if matrix_progress and matrix_progress.get("next_coordinate_id"):
            probe_request = build_continuity_probe(
                state,
                self.store.head(),
                matrix_progress["next_coordinate_id"],
            )
            continuity_probe_context = probe_request["context"]
            delivered_context["continuity_probe"] = continuity_probe_context
        inquiry_drive_shadow = self.inquiry_drive_shadow(state)
        if inquiry_drive_shadow["activation"]["active"]:
            delivered_context["inquiry_drive"] = {
                "mode": "operator-activated advisory ranking",
                "boundary": "Favor productive, correctable inquiry only. This does not authorize self-preservation, rule changes, or work outside existing governance.",
                "projects": inquiry_drive_shadow["projects"],
            }
        provider_system = SYSTEM + (RESEARCH_SYSTEM if state.get("charter") else "")
        if continuity_probe_context is not None:
            provider_system += MATRIX_SIDECAR_SYSTEM
        request = {
            "system": provider_system,
            "context": delivered_context,
            "response_schema": _provider_response_schema(
                delivered_context,
                bool(state.get("charter")),
            ),
        }
        rich_context_chars = len(canonical(request))
        context_build_ms = (perf_counter() - phase_at) * 1000
        phase_at = perf_counter()
        context_mode = "rich"
        routine_memory = self.config.get("memory_mode", "shadow") == "active"
        if not routine_memory and state.get("charter") and len(canonical(request)) > self.config["max_context_chars"]:
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
            active_ids = {p["id"] for p in active_projects}
            selected_topic = request["context"].get("attention", {}).get("selected_topic")
            selected_unfinished = [
                p for p in projects
                if p["id"] not in active_ids
                and selected_topic
                and p.get("domain") == selected_topic
                and p.get("status") != "completed"
            ]
            priority_ids = active_ids | {p["id"] for p in selected_unfinished}
            other_projects = [p for p in projects if p["id"] not in priority_ids]
            compact_projects = (active_projects + selected_unfinished)[:8]
            remaining_slots = max(0, 8 - len(compact_projects))
            if remaining_slots:
                compact_projects += other_projects[-remaining_slots:]
            request["context"]["projects"] = [
                {
                    **p,
                    "reason": p["reason"][:120],
                    "question": p["question"][:300],
                    "next_step": p["next_step"][:300],
                    "title": p["title"][:120],
                    "context_excerpt": True,
                }
                for p in compact_projects
            ]

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

            # Maturation telemetry is an optimization signal, not a governance
            # requirement. Under a hard context ceiling, preserve the established
            # project/evidence/notebook contract and omit this derived duplicate.
            request["context"].pop("research_maturation", None)

            # The response schema contains context-derived allowlists. Rebuild it
            # after shrinking the working view; otherwise stale project/notebook/
            # evidence alternatives from the pre-compaction context can keep the
            # request over the ceiling even though the delivered context is bounded.
            request["response_schema"] = _provider_response_schema(request["context"], True)

            # resolution_evidence exists primarily to construct the
            # constrained response schema, so that duplicate list can be dropped
            # under pressure. Keep project_evidence: the research prompt names
            # that compact allowlist explicitly, and retaining it makes cross-topic
            # evidence provenance inspectable instead of hiding the provider's
            # permitted citation set behind the schema alone.
            request["context"]["commitments"] = [
                {key: value for key, value in item.items() if key != "resolution_evidence"}
                for item in request["context"]["commitments"]
            ]
        if routine_memory or (state.get("charter") and len(canonical(request)) > self.config["max_context_chars"]):
            # Operator-enabled routine memory uses the same bounded owner as
            # overflow delivery. Shadow mode retains rich delivery when it fits.
            request["context"] = self.bounded_context(
                state, receipt, working_set_shadow, rich_context_chars
            )
            if continuity_probe_context is not None:
                request["context"]["continuity_probe"] = continuity_probe_context
            # Bounded delivery must not erase the handoff from collection
            # to synthesis. Rehydrate a tiny, project-prioritized set of exact
            # collector records whenever retrieval found qualifying evidence.
            # One source enables an honest provisional notebook; two can support
            # corroborated revision/publication without weakening governance.
            retrieval_plan = active_retrieval_plan(state, retrieval_shadow) if routine_memory else retrieval_shadow
            if research:
                retrieval_plan = {**retrieval_plan, "evidence_ids": list(dict.fromkeys(research["evidence_ids"] + retrieval_plan.get("evidence_ids", [])))}
            if retrieval_plan.get("evidence_ids"):
                request["context"] = self.rehydrate_retrieval_context(
                    state, request["context"], retrieval_plan,
                    content_limit=1800 if routine_memory else 900, max_records=3 if routine_memory else 2,
                    force=bool(research),
                )
            if routine_memory:
                # Same working-set owner as overflow delivery, activated by operator
                # choice rather than size. No shadow annotation becomes authority.
                from .providers import BOUNDED_RESEARCH_SYSTEM
                context = request["context"]
                context["memory"] = build_active_memory(state, trust_compacts_shadow, retrieval_plan,
                    visible_collector_ids={item["id"] for item in context.get("evidence", [])
                                           if item.get("actor") == "collector" and item.get("content")
                                           and not item.get("content_omitted")})
                context["bounded_context"]["activation_reason"] = "operator-active-memory"
                context["memory_mode"] = "active"
                # Non-collector falsifiers retain their original provenance. They
                # may support belief review but never acquire notebook eligibility.
                visible = {item["id"] for item in context.get("evidence", [])}
                for item in context["memory"]["retrieved_records"]:
                    if item["kind"] == "evidence" and item["value"].get("actor") != "collector":
                        context["evidence"] = [record for record in context.get("evidence", []) if record["id"] != item["id"]]
                        context["evidence"].append({**item["value"], "context_excerpt": item["context_excerpt"]})
                        visible.add(item["id"])
                context["evidence"].sort(key=lambda item: (item.get("version") or -1, item["id"]))
                context["notebooks"] = [dict(item) for item in context.get("notebooks", [])]
                for notebook in context.get("notebooks", []):
                    notebook["evidence"] = list(state["notebooks"][notebook["id"]]["evidence"])
                    context["blog_notebooks"].setdefault(notebook["project"], [])
                context["blog_notebooks"] = {
                    project: [{key: item.get(key) for key in ("id", "title", "revision", "evidence")}
                              for item in context.get("notebooks", []) if item["project"] == project]
                    for project in context.get("blog_notebooks", {})
                }
                # Source allowlists are rebuilt by rehydration. Human memory
                # records do not enter those scientific-source lists.
                for commitment in context.get("commitments", []):
                    commitment["resolution_evidence"] = self.commitment_resolution_evidence_ids(state, list(visible), commitment)
                request["system"] = SYSTEM + (BOUNDED_RESEARCH_SYSTEM if state.get("charter") else "") + ACTIVE_MEMORY_SYSTEM
                if continuity_probe_context is not None:
                    request["system"] += MATRIX_SIDECAR_SYSTEM
                # Receipt-only quality telemetry remains useful in routine memory.
                for key in ("evidence_quality", "inquiry_drive"):
                    if key in delivered_context:
                        context[key] = delivered_context[key]
            request["response_schema"] = _provider_response_schema(request["context"], bool(state.get("charter")))
            context_mode = "bounded"
            if routine_memory:
                self.fit_active_request(request)
            if not routine_memory and len(canonical(request)) > self.config["max_context_chars"]:
                self.fit_bounded_request(request)
        if question:
            text(question, "Operator question", 1000)
            request["context"]["operator_question"] = question
        if research:
            request["context"]["same_wake_research"] = json.loads(canonical(research))
            request["system"] += "\nAnswer the operator question or planned questions in summary using collected evidence IDs. Submit justified findings now in this proposal; disclose missing or insufficient evidence instead of claiming success.\n"
        # Rehydration and focusing can change visible citation eligibility. Build
        # the final contract from that view while retaining full-state queue and
        # prior artifact identities, even in routine compact memory.
        prior_constraints = request["context"].get("proposal_constraints")
        if state.get("charter"):
            request["context"]["evidence_quality"] = delivered_context["evidence_quality"]
        self.proposal_constraints(state, request["context"])
        if prior_constraints != request["context"].get("proposal_constraints"):
            request["response_schema"] = _provider_response_schema(request["context"], bool(state.get("charter")))
        if phase == "planning":
            from .research import RESEARCH_PLAN_SYSTEM, research_plan_schema
            request["context"].pop("continuity_probe", None)
            continuity_probe_context = None
            request["context"]["research_phase"] = "planning"
            request["system"] = RESEARCH_PLAN_SYSTEM + (ACTIVE_MEMORY_SYSTEM if routine_memory else "")
            request["response_schema"] = research_plan_schema(request["context"])
            if self.config.get("research_google_search"):
                request["tools"] = ["search_public_web"]
                request["system"] += "\nUse Google Search to cross-reference primary research, alternative explanations and indexed discussions (including Reddit where useful). Search snippets and discussions are discovery leads, not qualifying evidence. Prefer approved primary article URLs for collection. Return only the required JSON plan.\n"
        if routine_memory:
            self.fit_active_request(request)
        # A matrix sidecar is optional experiment work, never a prerequisite
        # for research. If mandatory delivery still cannot fit after prose
        # compaction, defer this coordinate rather than halt the installation.
        # No probe result is recorded: the same coordinate remains eligible.
        deferred_probe = None
        if (len(canonical(request)) > self.config["max_context_chars"]
                and continuity_probe_context is not None):
            deferred_probe = continuity_probe_context["campaign"]["coordinate_id"]
            request["context"].pop("continuity_probe", None)
            request["system"] = request["system"].replace(MATRIX_SIDECAR_SYSTEM, "")
            request["response_schema"] = _provider_response_schema(request["context"], bool(state.get("charter")))
            continuity_probe_context = None
            request["context"].setdefault("bounded_context", {}).setdefault("omitted_categories", []).append(
                "continuity sidecar deferred for context budget; coordinate remains untested")
            # Removing the probe rebuilds the final response contract. Fit that
            # exact envelope too, including deduplication of repeated receipts.
            if routine_memory:
                self.fit_active_request(request)
        require(len(canonical(request)) <= self.config["max_context_chars"],
                "Context ceiling reached; human review required, no model call made")
        compaction_ms = (perf_counter() - phase_at) * 1000
        shadow_chars = len(canonical(working_set_shadow))
        delivered_chars = len(canonical(request["context"]))
        delivered_request_chars = len(canonical(request))
        rehydrated_count = len(request["context"].get("retrieval_rehydration", {}).get("evidence_ids", []))
        runtime_performance = {
            "load_ms": round(load_ms, 3),
            "temporal_ms": round(temporal_ms, 3),
            "receipt_ms": round(receipt_ms, 3),
            "context_build_ms": round(context_build_ms, 3),
            "compaction_ms": round(compaction_ms, 3),
            "start_total_before_record_ms": round((perf_counter() - started_at) * 1000, 3),
            "store": self.store.performance_snapshot(),
        }
        self.store.append("invocation_started", {"id": invocation, "provider": provider, "model": model, "phase": phase,
            "charged": charged, "quota_day": day, "base_version": state["version"], "request": request,
            "request_hash": digest(request), "process_id": os.getpid(),
            "working_set_shadow": working_set_shadow,
            "trust_compacts_shadow": trust_compacts_shadow,
            "retrieval_shadow": retrieval_shadow,
            "inquiry_drive_shadow": inquiry_drive_shadow,
            **(
                {"continuity_probe_shadow": {"context": continuity_probe_context}}
                if continuity_probe_context is not None else {}
            ),
            "attention": delivered_context.get("attention", {"active": False}),
            "experimental_regime": state["experimental"], "temporal": temporal,
            "runtime_performance": runtime_performance,
            "context_delivery": {
                "mode": context_mode,
                "memory_mode": "active" if routine_memory else "shadow",
                **({"deferred_continuity_coordinate": deferred_probe,
                    "recovery": "optional-sidecar-deferred"} if deferred_probe else {}),
                "activation_reason": "operator-active-memory" if routine_memory else ("context-size" if context_mode == "bounded" else "rich-default"),
                "memory_digest": digest(request["context"]["memory"]) if routine_memory else None,
                "memory_retrieved_record_count": len(request["context"]["memory"]["retrieved_records"]) if routine_memory else 0,
                "rich_context_chars": rich_context_chars,
                "delivered_request_chars": delivered_request_chars,
                "delivered_context_chars": delivered_chars,
                "request_compression_ratio": round(delivered_request_chars / max(rich_context_chars, 1), 4),
                "retrieval_rehydrated_evidence_count": rehydrated_count,
                "working_set_chars": shadow_chars,
                "omitted_categories": request["context"].get("bounded_context", {}).get("omitted_categories", []),
                "provenance_policy": request["context"].get("bounded_context", {}).get("provenance_policy"),
            },
            "working_set_metrics": {
                "mode": context_mode,
                "working_set_chars": shadow_chars,
                "delivered_context_chars": delivered_chars,
                "working_to_delivered_ratio": round(shadow_chars / max(delivered_chars, 1), 4),
                "retrieval_candidate_count": retrieval_shadow["metrics"]["candidate_count"],
                "retrieval_evidence_count": retrieval_shadow["metrics"]["evidence_count"],
                "retrieval_rehydrated_evidence_count": rehydrated_count,
                "retrieval_trigger_counts": retrieval_shadow["metrics"]["trigger_counts"],
                "trust_compact_candidate_count": trust_compacts_shadow["metrics"]["candidate_count"],
                "trust_compact_settled_count": trust_compacts_shadow["metrics"]["settled_count"],
                "trust_compact_evidence_root_count": trust_compacts_shadow["metrics"]["evidence_root_count"],
                "inquiry_drive_project_count": len(inquiry_drive_shadow["projects"]),
            }})
        return invocation, request

    def _record_continuity_sidecar(self, state, invocation, response, research_status, activity=None):
        """Score one answered sidecar independently from normal research governance."""
        shadow = state["invocations"][invocation].get("continuity_probe_shadow")
        if not isinstance(shadow, dict) or not isinstance(shadow.get("context"), dict):
            return None
        probe_context = shadow["context"]
        report_activity(activity, "continuity", invocation_id=invocation,
                        coordinate_id=probe_context["campaign"]["coordinate_id"])
        try:
            if response is None:
                raise ValueError("continuity_probe sidecar missing or response was not parseable")
            evaluation = evaluate_continuity_probe_response(probe_context, response)
        except (ValueError, TypeError, KeyError) as error:
            evaluation = failed_continuity_probe_evaluation(probe_context, error)

        record = continuity_result_record(
            probe_context,
            evaluation,
            invocation,
            research_status,
            response=response,
        )
        progress = self.store.record_continuity_matrix_result(
            probe_context["campaign"]["coordinate_id"],
            record,
        )
        return {
            "status": "completed",
            "coordinate_id": probe_context["campaign"]["coordinate_id"],
            "score": record["score"],
            "passed": record["passed"],
            "completed": progress["completed_count"],
            "total": progress["cell_count"],
            "next_coordinate_id": progress["next_coordinate_id"],
        }

    def finish(self, invocation, raw, metadata=None, crash=False, *, activity=None):
        state = self.store.load()
        require(state["pending"] == invocation, "Response does not match the pending invocation")
        probe_response = None
        try:
            require(isinstance(raw, str) and len(raw) <= 64000, "Response exceeds 64,000 characters")
            proposal = json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError("Nonfinite JSON")))
            if (
                isinstance(proposal, dict)
                and isinstance(
                    state["invocations"][invocation].get("continuity_probe_shadow"),
                    dict,
                )
            ):
                probe_response = proposal.pop("continuity_probe", None)
            proposal, result, editorial, rotation_filter = govern_proposal(
                state, invocation, proposal
            )
        except (ValueError, TypeError, KeyError, Rejected) as exc:
            reason = str(exc)[:1000]
            self.store.append("rejected", {"id": invocation, "reason": reason,
                                          "raw_response": str(raw)[:64000], "metadata": metadata or {},
                                          "observation_receipt": ({"would_have_been_flagged": True,
                                                                   "rule_reason": reason,
                                                                   "mode": "observation"}
                                                                  if self.config["observation_mode"] else None),
                                          **({"provider_requests_sent": metadata["provider_requests_sent"]}
                                             if metadata and "provider_requests_sent" in metadata else {})})
            if state.get("charter"):
                self.store.append("attention_assessed", attention_assessment(
                    self.store.load(), invocation, "rejected"))
            probe_result = self._record_continuity_sidecar(
                state,
                invocation,
                probe_response,
                "rejected",
                activity=activity,
            )
            return {
                "status": "rejected",
                "id": invocation,
                "reason": reason,
                **(
                    {"continuity_matrix_probe": probe_result}
                    if probe_result is not None else {}
                ),
            }
        fields = ["version", "beliefs", "commitments", "journal"]
        if state.get("charter"):
            fields += ["projects", "notebooks", "research", "posts"]
        result_hash = digest({k: result[k] for k in fields})
        self.store.append("accepted", {"id": invocation, "proposal": proposal, "raw_response": raw,
                                       "metadata": metadata or {},
                                       **({"provider_requests_sent": metadata["provider_requests_sent"]}
                                          if metadata and "provider_requests_sent" in metadata else {}), "result_hash": result_hash, "hash_fields": fields,
                                       **({"editorial": editorial} if editorial else {}),
                                       **({"rotation_filter": rotation_filter} if rotation_filter else {})}, crash=crash)
        if state.get("charter"):
            self.store.append("attention_assessed", attention_assessment(
                state, invocation, "accepted", proposal))
        probe_result = self._record_continuity_sidecar(
            state,
            invocation,
            probe_response,
            "accepted",
            activity=activity,
        )
        return {"status": "accepted", "id": invocation, "cycle": result["version"],
                **({"editorial": {k: v for k, v in editorial.items() if k != "action"}} if editorial else {}),
                **({"rotation_filter": {
                    "selected_topic": rotation_filter["selected_topic"],
                    "withheld_count": rotation_filter["withheld_count"],
                    "inserted_capacity_park": rotation_filter["inserted_capacity_park"],
                    **({"bob_checkpoint": rotation_filter["bob_checkpoint"]}
                       if rotation_filter.get("bob_checkpoint") else {}),
                }} if rotation_filter else {}),
                **(
                    {"continuity_matrix_probe": probe_result}
                    if probe_result is not None else {}
                )}

    @staticmethod
    def _request_count(provider):
        if hasattr(provider, "provider_attempts"):
            return provider.diagnostics()
        count = getattr(provider, "provider_requests_sent", None)
        return {"provider_requests_sent": count} if count is not None else {}
    @staticmethod
    def _invocation_failure_outcome(error):
        """Map WAKE/provider-specific exceptions onto kernel outcomes."""
        if isinstance(error, TransientProviderError):
            return "temporary_failure"
        if isinstance(error, (DailyQuotaExceeded, ConfiguredDailyLimitReached)):
            return "quota_exhausted"
        return "provider_failure"

    @staticmethod
    def _invoke_external_effect(lifecycle, effect, checkpoint):
        """Delegate effect ordering to the WAKE kernel while keeping barrier failure distinct."""
        if lifecycle is None:
            if checkpoint:
                try:
                    checkpoint()
                except Exception as error:
                    raise InvocationBarrierError(error) from error
            return effect()
        return lifecycle.invoke(
            effect,
            effect_barrier=checkpoint,
            classify_error=Engine._invocation_failure_outcome,
        )

    def run(self, provider, crash_at=None, checkpoint=None, collector=None, *, question=None, activity=None):
        report_activity(activity, "record")
        try:
            with self.store.lock():
                self.initialize()
                self.recover()
                require(not question or (collector is not None and self.store.load().get("charter")),
                        "Immediate questions require a research collector and charter")
                research = None
                if collector and (self.config.get("same_wake_research") or question):
                    from .research import collect_planned
                    plan = self._run_invocation(provider, checkpoint=checkpoint, phase="planning", question=question, activity=activity)
                    if plan["status"] != "planned":
                        return plan
                    report_activity(activity, "collecting")
                    evidence_ids = collect_planned(self, plan["requests"])
                    research = {"planning_invocation": plan["id"], "requests": plan["requests"], "evidence_ids": evidence_ids}
                elif collector:
                    report_activity(activity, "collecting")
                    collector(self)
                result = self._run_invocation(provider, crash_at, checkpoint, question=question, research=research, activity=activity)
                if research:
                    result.setdefault("same_wake_research", research)
                return result
        finally:
            report_activity(activity, "idle")

    def _run_invocation(self, provider, crash_at=None, checkpoint=None, *, phase="proposal", question=None, research=None, activity=None):
        report_activity(activity, "context")
        invocation, request = self.start(provider.name, provider.model, provider.charged, phase=phase, question=question, research=research)
        lifecycle = (
            self.store.begin_invocation_lifecycle(
                invocation, request, provider.name, provider.model
            )
            if hasattr(self.store, "begin_invocation_lifecycle")
            else None
        )
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
            def record_attempt(phase, attempt):
                self.store.append("provider_attempt_" + phase, {"id": invocation, "attempt": attempt})
                if checkpoint:
                    checkpoint()
            provider.record_attempt = record_attempt
        if crash_at == "after-start":
            try:
                self._invoke_external_effect(
                    lifecycle,
                    lambda: os._exit(85),
                    checkpoint,
                )
            except InvocationBarrierError as error:
                raise error.cause
        def propose():
            probe = request.get("context", {}).get("continuity_probe", {}) if phase == "proposal" else {}
            report_activity(activity, "provider", invocation_id=invocation,
                            coordinate_id=probe.get("campaign", {}).get("coordinate_id"))
            return provider.propose(request)
        try:
            raw, metadata = self._invoke_external_effect(
                lifecycle,
                propose,
                checkpoint,
            )
        except InvocationBarrierError as error:
            raise error.cause
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
        except ConfiguredDailyLimitReached as exc:
            reason = str(exc)[:1000]
            payload = {"id": invocation, "reason": reason, "provider_error": exc.details,
                       "quota_exhausted": "configured_daily_limit", **self._request_count(provider)}
            self.store.append("deferred", payload)
            if checkpoint:
                checkpoint()
            return {"status": "deferred", "id": invocation, "reason": reason,
                    "provider_error": exc.details, "quota_exhausted": "configured_daily_limit", **self._request_count(provider)}
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
        if phase == "planning":
            plan_id = "wake-retrieval-plan-" + invocation
            if lifecycle is not None:
                lifecycle.proposal_received(plan_id)
            from .research import validate_research_plan
            try:
                requests = validate_research_plan(raw, request["context"], self.store.load())
            except (Rejected, ValueError) as exc:
                self.store.append("rejected", {"id": invocation, "reason": str(exc)[:1000],
                    "phase": "planning", "raw_response": str(raw)[:16000], "metadata": metadata,
                    **self._request_count(provider)})
                if lifecycle is not None:
                    lifecycle.governed(plan_id, None, "rejected")
                    lifecycle.complete(proposal_id=plan_id, detail="invalid-research-plan")
                if checkpoint:
                    checkpoint()
                return {"status": "rejected", "id": invocation, "phase": "planning", "reason": str(exc)}
            self.store.append("research_planned", {"id": invocation, "requests": requests,
                "raw": raw, "metadata": metadata, "reason": "Validated retrieval plan; no research transition committed",
                **self._request_count(provider)})
            if lifecycle is not None:
                lifecycle.governed(plan_id, None, "accepted")
                lifecycle.complete(proposal_id=plan_id, detail="research-planned")
            if checkpoint:
                checkpoint()
            return {"status": "planned", "id": invocation, "requests": requests}
        proposal_id = "wake-response-" + invocation
        if lifecycle is not None:
            lifecycle.proposal_received(proposal_id)
        report_activity(activity, "governance", invocation_id=invocation,
                        coordinate_id=request.get("context", {}).get("continuity_probe", {}).get("campaign", {}).get("coordinate_id"))
        result = self.finish(invocation, raw, metadata, crash=crash_at == "during-commit", activity=activity)
        if lifecycle is not None:
            lifecycle.governed(proposal_id, None, result["status"])
            lifecycle.complete(
                proposal_id=proposal_id,
                receipt_id=None,
                detail=result["status"],
            )
        if checkpoint:
            checkpoint()
        report_activity(activity, "receipt", invocation_id=invocation)
        if research:
            result["same_wake_research"] = research
            try:
                result["answer"] = json.loads(raw).get("summary", "")
            except (ValueError, AttributeError):
                pass
        return result
