# =============================================================================
# PROVIDERS — the replaceable cognition boundary. Prompts and schemas define what a disposable model may propose; network/failover code records which model was attempted and which actually answered. A provider never receives direct write authority.
# =============================================================================

"""Provider boundary: one JSON request in, one untrusted proposal out."""

from copy import deepcopy
import errno
import json
import os
from pathlib import Path
import re
import socket
import time
import urllib.error
import urllib.request

from wake.kernel import (
    GenerationRequest,
    GeminiGenerationProvider,
    ProviderError as WakeProviderError,
    ProviderQuotaError as WakeProviderQuotaError,
    ProviderTemporaryError as WakeProviderTemporaryError,
)

from .governance import PUBLICATION_MIN_SOURCES, Rejected, require


from .prompts import BOUNDED_RESEARCH_SYSTEM, RESEARCH_SYSTEM, SYSTEM


def action_schema(kind, fields, enums=None, optional=()):
    """Keep each action's shape distinct, matching mechanical governance exactly."""
    required = ["type", *fields.split()]
    properties = {key: {"type": "string"} for key in [*required, *optional]}
    properties["type"] = {"type": "string", "enum": [kind]}
    for key, values in (enums or {}).items():
        properties[key] = {"type": "string", "enum": values}
    if "confidence" in properties:
        properties["confidence"] = {"type": "number", "minimum": 0, "maximum": 1}
    if "due_cycle" in properties:
        properties["due_cycle"] = {"type": "integer"}
    if "reflection_cycle" in properties:
        properties["reflection_cycle"] = {"type": "integer"}
    if "evidence" in properties or "observations" in properties:
        field = "evidence" if "evidence" in properties else "observations"
        properties[field] = {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 12}
    if "notebooks" in properties:
        properties["notebooks"] = {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 3}
    return {"type": "object", "properties": properties, "required": required, "additionalProperties": False}


SCHEMA = {"type": "object", "additionalProperties": False, "properties": {
    "base_version": {"type": "integer"}, "title": {"type": "string"}, "summary": {"type": "string"},
    "actions": {"type": "array", "maxItems": 12, "items": {"anyOf": [
        action_schema("belief", "id statement confidence status evidence reason falsifier", {"status": ["active", "retracted"]}),
        action_schema("commit", "id task due_cycle reason", optional=("project",)),
        action_schema("resolve", "id status evidence reason", {"status": ["fulfilled"]}),
        action_schema("project", "id title question domain status next_step reason",
                      {"status": ["active", "parked", "completed"]}),
        action_schema("research", "project query domain reason"),
        action_schema("reframe", "project old_frame new_frame assumptions_changed observations trigger strategy reason"),
        action_schema("notebook", "id project title summary findings limitations next_questions evidence reason"),
        action_schema("blog", "id project title lede body notebooks evidence reason", optional=("lens", "supersedes", "reflection_cycle")),
    ]}}}, "required": ["base_version", "title", "summary", "actions"]}

def schema_for_context(context):
    """Put the durable blog citation allowlist in the model's JSON contract.

    Governance still checks the exact chosen project/notebook/evidence relationship.
    No evidence is added, substituted, or silently repaired after generation.
    """
    schema = deepcopy(SCHEMA)
    # The model is proposing against one exact durable snapshot. Expose that
    # concurrency guard before generation instead of accepting any integer and
    # relying on governance to reject stale guesses afterward.
    if isinstance(context.get("version"), int):
        schema["properties"]["base_version"]["enum"] = [context["version"]]
    directive = context.get("attention", {})
    enforced_topic = directive.get("selected_topic") if directive.get("enforce_selected_topic") else None
    entries = [(project, notebook) for project, notebooks in context.get("blog_notebooks", {}).items()
               for notebook in notebooks]
    if enforced_topic:
        project_domains = {p["id"]: p.get("domain") for p in context.get("projects", [])}
        entries = [(project, notebook) for project, notebook in entries
                   if project_domains.get(project) == enforced_topic]
    choices = schema["properties"]["actions"]["items"]["anyOf"]

    # In research mode, new commitments belong to one existing durable project.
    # The base non-research kernel keeps generic commitments available.
    commit_action = next(a for a in choices if a["properties"]["type"]["enum"] == ["commit"])
    if context.get("mission") is not None:
        project_ids_for_commit = sorted({
            project["id"] for project in context.get("projects", [])
            if project.get("id")
            and (not enforced_topic or project.get("domain") == enforced_topic)
        })
        if project_ids_for_commit:
            commit_action["properties"]["project"] = {
                "type": "string", "enum": project_ids_for_commit
            }
            if "project" not in commit_action["required"]:
                commit_action["required"].append("project")
        else:
            choices.remove(commit_action)

    domains = list(dict.fromkeys([topic["id"] for topic in context.get("research_topics", [])]
                                 + [project["domain"] for project in context.get("projects", [])]))
    if domains:
        project_action = next(a for a in choices if a["properties"]["type"]["enum"] == ["project"])
        research_action = next(a for a in choices if a["properties"]["type"]["enum"] == ["research"])
        if enforced_topic:
            # A forced rotation must be valid before generation, not merely
            # rejected afterward. Constrain substantive project/research work
            # to the selected topic and expose explicit parking actions when
            # all three active slots are occupied.
            active_projects = [p for p in context.get("projects", []) if p.get("status") == "active"]
            selected_projects = [
                p for p in context.get("projects", [])
                if p.get("domain") == enforced_topic
            ]
            selected_project_ids = sorted(p["id"] for p in selected_projects)

            choices.remove(project_action)
            if len(active_projects) >= 3 and not any(
                    p.get("domain") == enforced_topic for p in active_projects):
                # Capacity recovery is deliberately a separate accepted shift.
                # First park one existing project; the next wake can create or
                # reactivate the selected-topic project without a doomed fourth
                # active project proposal.
                configured_domains = {t["id"] for t in context.get("research_topics", [])}
                blocked_domains = set(directive.get("capability_blocked_topics", []))
                parking_candidates = [
                    p for p in active_projects if p.get("domain") not in configured_domains
                ] or [
                    p for p in active_projects if p.get("domain") in blocked_domains
                ] or [
                    p for p in active_projects if p.get("domain") != enforced_topic
                ]
                for project in parking_candidates:
                    constrained = deepcopy(project_action)
                    constrained["properties"]["id"] = {"type": "string", "enum": [project["id"]]}
                    constrained["properties"]["title"] = {"type": "string", "enum": [project["title"]]}
                    constrained["properties"]["question"] = {"type": "string", "enum": [project["question"]]}
                    constrained["properties"]["domain"] = {"type": "string", "enum": [project["domain"]]}
                    constrained["properties"]["status"] = {"type": "string", "enum": ["parked"]}
                    choices.append(constrained)
                choices.remove(research_action)
            else:
                project_action["properties"]["domain"]["enum"] = [enforced_topic]
                selected_active = [
                    p for p in selected_projects if p.get("status") == "active"
                ]
                selected_parked = [
                    p for p in selected_projects if p.get("status") == "parked"
                ]
                if selected_parked and not selected_active:
                    # A forced rotation resumes durable unfinished work before
                    # allowing a fresh model to paraphrase the same inquiry under
                    # a new project ID. Reactivation is a distinct accepted shift;
                    # research follows once the durable project is active again.
                    for project in selected_parked:
                        constrained = deepcopy(project_action)
                        constrained["properties"]["id"] = {
                            "type": "string", "enum": [project["id"]]
                        }
                        constrained["properties"]["title"] = {
                            "type": "string", "enum": [project["title"]]
                        }
                        constrained["properties"]["question"] = {
                            "type": "string", "enum": [project["question"]]
                        }
                        constrained["properties"]["domain"] = {
                            "type": "string", "enum": [project["domain"]]
                        }
                        constrained["properties"]["status"] = {
                            "type": "string", "enum": ["active"]
                        }
                        choices.append(constrained)
                    choices.remove(research_action)
                else:
                    if not selected_project_ids:
                        # No durable project owns this selected topic yet, so a
                        # new active project is the only valid project transition.
                        project_action["properties"]["status"]["enum"] = ["active"]
                        choices.append(project_action)
                    else:
                        # Once this topic already has durable work, do not put the
                        # unconstrained create/update project action back into the
                        # provider schema. It lets a disposable model paraphrase an
                        # existing question under a fresh ID, only for governance to
                        # reject the duplicate. Existing active work should advance
                        # through research/notebook actions; parked work is handled
                        # by the explicit reactivation branch above.
                        pass
                    research_action["properties"]["domain"]["enum"] = [enforced_topic]
                    active_selected_ids = sorted(p["id"] for p in selected_active)
                    if active_selected_ids:
                        research_action["properties"]["project"]["enum"] = active_selected_ids
                    elif selected_project_ids:
                        choices.remove(research_action)
                    else:
                        # New projects need one accepted state transition before a
                        # research request can reference them. This prevents a model
                        # from inventing a same-response project ID that later fails
                        # another mechanical constraint.
                        choices.remove(research_action)
        else:
            project_action["properties"]["domain"]["enum"] = domains
            research_action["properties"]["domain"]["enum"] = domains

        # Collection and synthesis are different workflow stages. Once an active
        # project has qualifying visible evidence and no current notebook, do not
        # keep offering that same project another research action. Other projects
        # that still genuinely need evidence remain eligible. Deterministic WAKE
        # application policy separately requires the live proposal to cross the
        # synthesis checkpoint, so this schema narrowing prevents avoidable model
        # retries instead of becoming the authority itself.
        synthesis_ready = set(context.get("synthesis_ready_projects", []))
        if synthesis_ready and research_action in choices:
            researchable_projects = sorted({
                project["id"]
                for project in context.get("projects", [])
                if project.get("id")
                and project.get("status") == "active"
                and project["id"] not in synthesis_ready
                and (not enforced_topic or project.get("domain") == enforced_topic)
            })
            if researchable_projects:
                research_action["properties"]["project"]["enum"] = researchable_projects
            else:
                choices.remove(research_action)

    constraints = context.get("proposal_constraints", {})
    if "known_belief_ids" in constraints:
        belief = next(a for a in choices if a["properties"]["type"]["enum"] == ["belief"])
        known = constraints["known_belief_ids"]
        # New IDs cannot overwrite an existing belief. Reviews get a separate
        # alternative requiring evidence outside that belief's durable roots.
        if known:
            belief["properties"]["id"]["not"] = {"enum": known}
        belief["properties"]["status"] = {"type": "string", "enum": ["active"]}
        visible = {e.get("id") for e in context.get("evidence", []) if e.get("id")}
        groups = {}
        for identifier, review in constraints.get("belief_reviews", {}).items():
            new = tuple(sorted(set(review["new_evidence_ids"]) & visible))
            if new:
                groups.setdefault(new, []).append(identifier)
        for new, identifiers in groups.items():
            review = deepcopy(belief)
            review["properties"]["id"] = {"type": "string", "enum": sorted(identifiers)}
            review["properties"]["status"] = {"type": "string", "enum": ["active", "retracted"]}
            review["properties"]["evidence"].update({"contains": {"enum": list(new)}, "minContains": 1})
            choices.append(review)
    slots = constraints.get("remaining_search_slots")
    if isinstance(slots, int):
        if slots == 0:
            choices[:] = [item for item in choices
                          if item["properties"]["type"]["enum"] != ["research"]]
        else:
            # This is a proposal-wide limit: two individually valid searches
            # can still overflow the one remaining durable queue slot.
            schema["properties"]["actions"].update({
                "contains": {"type": "object", "properties": {
                    "type": {"enum": ["research"]}}, "required": ["type"]},
                "minContains": 0, "maxContains": slots,
            })

    identities = constraints.get("project_identities", {})
    known_projects = constraints.get("known_project_ids", [])
    for item in list(choices):
        if item["properties"]["type"]["enum"] != ["project"]:
            continue
        ids = item["properties"]["id"].get("enum")
        if ids:
            # Bounded project prose may be excerpted. Pin the original identity,
            # not the excerpt, in status/next-step update alternatives.
            if len(ids) == 1 and ids[0] in identities:
                for field, value in identities[ids[0]].items():
                    item["properties"][field] = {"type": "string", "enum": [value]}
            continue
        if not known_projects:
            continue
        item["properties"]["id"]["not"] = {"enum": known_projects}
        # The broad create action previously also allowed edits to immutable
        # existing identity. Offer separate, exact update alternatives instead.
        if not enforced_topic:
            for identifier, identity in identities.items():
                update = deepcopy(item)
                update["properties"]["id"] = {"type": "string", "enum": [identifier]}
                for field, value in identity.items():
                    update["properties"][field] = {"type": "string", "enum": [value]}
                choices.append(update)

    # Commitment resolution receives commitment-specific, governance-eligible
    # evidence alternatives. This prevents the provider from selecting only
    # pre-commitment evidence even when newer qualifying evidence is visible.
    resolve = next(a for a in choices if a["properties"]["type"]["enum"] == ["resolve"])
    commitments = context.get("commitments", [])
    if commitments:
        choices.remove(resolve)
        visible_evidence = {
            item.get("id"): item
            for item in context.get("evidence", [])
            if isinstance(item, dict) and item.get("id")
        }
        for commitment in commitments:
            created_version = commitment.get("created_version")
            allowed = sorted({
                evidence_id
                for evidence_id in commitment.get("resolution_evidence", [])
                if evidence_id in visible_evidence
                and (
                    not isinstance(created_version, int)
                    or (
                        isinstance(visible_evidence[evidence_id].get("version"), int)
                        and visible_evidence[evidence_id]["version"] >= created_version
                    )
                )
            })
            if not allowed:
                continue
            constrained = deepcopy(resolve)
            constrained["properties"]["id"] = {"type": "string", "enum": [commitment["id"]]}
            constrained["properties"]["evidence"]["items"] = {"type": "string", "enum": allowed}
            choices.append(constrained)

    # Reframes are recovery actions, not general research actions. Governance
    # permits them only for projects with a recorded capability block or an
    # Attention deferral, exposed to the provider as representation_recovery.
    # Keep the schema aligned with that durable eligibility so the model cannot
    # spend a provider turn on a proposal governance is guaranteed to reject.
    reframe = next(a for a in choices if a["properties"]["type"]["enum"] == ["reframe"])
    visible_evidence_ids = sorted({
        item["id"] for item in context.get("evidence", [])
        if isinstance(item, dict) and item.get("id")
    })
    recovery_project_ids = {
        item.get("project")
        for item in context.get("representation_recovery", [])
        if isinstance(item, dict) and item.get("project")
    }
    project_ids = sorted({
        project["id"] for project in context.get("projects", [])
        if project.get("id") in recovery_project_ids
        and (not enforced_topic or project.get("domain") == enforced_topic)
    })
    if visible_evidence_ids and project_ids:
        reframe["properties"]["observations"]["items"] = {
            "type": "string", "enum": visible_evidence_ids
        }
        reframe["properties"]["project"]["enum"] = project_ids
    else:
        choices.remove(reframe)

    # Existing projects receive project-specific notebook alternatives. This is
    # a preflight constraint, not a substitute for governance: a WAKE-analysis
    # notebook can only select source-controlled repository evidence that is
    # actually present in this invocation's context. New projects may still be
    # proposed, but need a later wake to write a notebook after collection.
    notebook = next((a for a in choices if a["properties"]["type"]["enum"] == ["notebook"]), None)
    projects = context.get("projects", [])
    collector_evidence = {item["id"]: item for item in context.get("evidence", [])
                          if item.get("actor") == "collector"}
    if notebook and (enforced_topic or (projects and collector_evidence)):
        choices.remove(notebook)
        project_evidence = context.get("project_evidence", {})
        existing_notebooks = {}
        for item in context.get("notebooks", []):
            if not isinstance(item, dict) or not item.get("project") or not item.get("id"):
                continue
            existing_notebooks.setdefault(item["project"], []).append(item)
        for project in projects:
            if enforced_topic and project.get("domain") != enforced_topic:
                continue
            allowed = project_evidence.get(project["id"])
            allowed = sorted(allowed if allowed is not None else collector_evidence)
            if not allowed:
                continue

            # Notebook revisions must add genuinely new retrieved evidence.
            # If every currently eligible source is already cited by the visible
            # notebook history for this project, there is no schema-valid revision
            # that governance can accept, so do not offer one to the provider.
            prior_evidence = {
                evidence_id
                for item in existing_notebooks.get(project["id"], [])
                for evidence_id in item.get("evidence", [])
            }
            if "notebook_revisions" not in constraints and existing_notebooks.get(project["id"]) and not any(
                evidence_id not in prior_evidence for evidence_id in allowed
            ):
                continue

            constrained = deepcopy(notebook)
            constrained["properties"]["project"] = {"type": "string", "enum": [project["id"]]}
            constrained["properties"]["evidence"]["items"] = {"type": "string", "enum": allowed}
            revisions = constraints.get("notebook_revisions")
            prior = {identifier: item for identifier, item in (revisions or {}).items()
                     if item["project"] == project["id"]}
            if prior:
                for identifier, item in prior.items():
                    new = sorted(set(item["new_evidence_ids"]) & set(allowed))
                    if not new or len({collector_evidence[e].get("source", e)
                                       for e in allowed if e in collector_evidence}) < 2:
                        continue
                    revision = deepcopy(constrained)
                    revision["properties"]["id"] = {"type": "string", "enum": [identifier]}
                    revision["properties"]["evidence"].update({
                        "minItems": 2, "uniqueItems": True,
                        "contains": {"type": "string", "enum": new},
                        "minContains": 1,
                    })
                    choices.append(revision)
            else:
                choices.append(constrained)
    blog = next(a for a in choices if a["properties"]["type"]["enum"] == ["blog"])
    evidence = sorted({eid for _, notebook in entries for eid in notebook["evidence"]})
    reflection_due = bool(context.get("bob_reflection_due"))
    if len(set(evidence)) < PUBLICATION_MIN_SOURCES and not reflection_due:
        choices.remove(blog)
    else:
        props = blog["properties"]
        if reflection_due:
            props["notebooks"]["minItems"] = 0
            props["evidence"]["minItems"] = 0
            props["body"]["minLength"] = 900
            props["body"]["maxLength"] = 6000
            props["lens"]["maxLength"] = 500
            props["reflection_cycle"]["enum"] = [context["bob_reflection_cycle"]]
            for required_field in ("reflection_cycle", "lens"):
                if required_field not in blog["required"]:
                    blog["required"].append(required_field)
        else:
            # Expose the public promotion threshold before generation.
            # Governance still re-validates distinct source URLs.
            props["evidence"]["minItems"] = PUBLICATION_MIN_SOURCES
        project_choices = sorted({project for project, _ in entries} or
                                 {p["id"] for p in context.get("projects", [])})
        if reflection_due and "" not in project_choices:
            project_choices.append("")
        props["project"]["enum"] = project_choices
        notebook_choices = sorted({n["id"] for _, n in entries})
        if notebook_choices:
            props["notebooks"]["items"]["enum"] = notebook_choices
        else:
            # A reflection may legitimately require zero notebooks. JSON Schema
            # enum arrays must not be empty, so require the only valid choice:
            # an empty array. Deterministic governance still owns publication.
            props["notebooks"]["items"].pop("enum", None)
            props["notebooks"]["maxItems"] = 0
        if evidence:
            props["evidence"]["items"]["enum"] = evidence
        else:
            # The first/reflection post may also have zero evidence. Avoid an
            # unsatisfiable enum while requiring the provider to return none.
            # Governance continues to enforce the exact reflection exception.
            props["evidence"]["items"].pop("enum", None)
            props["evidence"]["maxItems"] = 0

        if reflection_due:
            # A due Bob checkpoint is mandatory at the disposable provider
            # boundary, but it remains an editorial sidecar rather than research
            # authority. Put it in a required top-level field so structured
            # generation cannot silently omit it while keeping ordinary research
            # actions available in the same response.
            checkpoint = deepcopy(blog)
            schema["properties"]["bob_checkpoint"] = checkpoint
            if "bob_checkpoint" not in schema["required"]:
                schema["required"].append("bob_checkpoint")
            choices.remove(blog)

        # Ordinary Bob publication stays optional and event-driven. A due
        # checkpoint is required to be proposed, but publication can still be
        # withheld by governance without blocking accepted research.
    if constraints.get("required_next_step"):
        parking = [item for item in choices
                   if item["properties"]["type"]["enum"] == ["project"]
                   and item["properties"]["status"].get("enum") == ["parked"]]
        if parking:
            # A capacity recovery wake is one exact parking transition, not a
            # fresh commitment or another evidence-free synthesis attempt.
            # Any due editorial checkpoint remains a separate top-level field.
            choices[:] = parking
            schema["properties"]["actions"].update({"minItems": 1, "maxItems": 1})
    return schema

def retractable_quotes(post):
    """Short exact phrases from the original post, not fabricated model quotations."""
    prose = "\n".join(str(post.get(k, "")) for k in ("title", "lede", "body", "lens"))
    return list(dict.fromkeys(m.group() for m in re.finditer(
        r"\b(?:genuine|real)\s+(?:epistemic\s+)?(?:agency|self-governance|consciousness|intelligence)\b"
        r"|\b(?:clean|clear|sharp)\s+(?:functional\s+)?(?:fault\s+lines?|boundar(?:y|ies)|demarcation)\b"
        r"|\b(?:cleanly|sharply)\s+(?:separates?|demarcates?|distinguishes?)\b"
        r"|\b(?:proves?|demonstrates?|establishes?|confirms?)\s+that\b", prose, re.I)))

def load_env(path=Path(".env")):
    if path.is_file():
        for line in path.read_text().splitlines():
            key, sep, value = line.strip().partition("=")
            if sep and key == "GEMINI_API_KEY" and key not in os.environ:
                os.environ[key] = value.strip().strip("\"'")

class TransientProviderError(RuntimeError):
    "Temporary provider/network outage; the wake should be retried later."
    def __init__(self, message, details=None):
        super().__init__(message)
        self.details = details or {}

class ProviderRequestError(Rejected):
    """Provider rejected a request; safe structured diagnostics may be persisted."""
    def __init__(self, message, details=None):
        super().__init__(message)
        self.details = details or {}


FREE_TIER_DAILY_QUOTA_ID = "GenerateRequestsPerDayPerProjectPerModel-FreeTier"

class DailyQuotaExceeded(ProviderRequestError):
    """Gemini reported the exact per-day free-tier project/model quota."""


class ConfiguredDailyLimitReached(ProviderRequestError):
    """Every configured model request allowance has been used for the current day."""

def _quota_ids(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "quotaId" and isinstance(item, str):
                yield item
            yield from _quota_ids(item)
    elif isinstance(value, list):
        for item in value:
            yield from _quota_ids(item)

def is_free_tier_daily_quota(details):
    """Classify only Google's exact free-tier daily quota identifier."""
    return FREE_TIER_DAILY_QUOTA_ID in set(_quota_ids(details or {}))

def _safe_provider_value(value, depth=0):
    """Bound provider error JSON and drop fields that could plausibly contain credentials."""
    if depth > 5:
        return "[truncated]"
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            name = str(key)
            if re.search(r"(api.?key|token|authorization|credential|secret)", name, re.I):
                continue
            result[name[:120]] = _safe_provider_value(item, depth + 1)
            if len(result) >= 24:
                break
        return result
    if isinstance(value, list):
        return [_safe_provider_value(item, depth + 1) for item in value[:24]]
    if isinstance(value, str):
        secret = os.environ.get("GEMINI_API_KEY")
        if secret:
            value = value.replace(secret, "[redacted]")
        value = re.sub(r"(?i)([?&](?:key|api_key|token)=)[^&\s]+", r"\1[redacted]", value)
        return value[:2000]
    if value is None or isinstance(value, (bool, int, float)):
        return value
    return str(value)[:500]

def _http_error_details(exc, elapsed_ms, payload_bytes):
    """Extract only bounded, non-secret diagnostics from a provider HTTP error."""
    details = {
        "http_status": int(exc.code),
        "elapsed_ms": int(elapsed_ms),
        "request_payload_bytes": int(payload_bytes),
    }
    retry_after = exc.headers.get("Retry-After") if exc.headers else None
    if retry_after:
        details["retry_after"] = str(retry_after)[:120]
    try:
        raw = exc.read(32_001)
    except Exception:
        raw = b""
    if raw:
        details["response_bytes_captured"] = min(len(raw), 32_000)
        try:
            parsed = json.loads(raw[:32_000].decode("utf-8", "replace"))
        except (ValueError, TypeError):
            details["response_text"] = _safe_provider_value(raw[:32_000].decode("utf-8", "replace"))
        else:
            error = parsed.get("error", parsed) if isinstance(parsed, dict) else parsed
            details["provider_error"] = _safe_provider_value(error)
    return details

class Gemini:
    name = "gemini"
    charged = True
    transient_http_codes = frozenset({500, 502, 503, 504})

    def __init__(self, config, model=None):
        load_env()
        self.config = config
        self.model = model or config["model"]
        fallbacks = config.get("gemini_fallback_models", [])
        require(isinstance(fallbacks, list), "gemini_fallback_models must be a list")
        for name in [self.model, *fallbacks]:
            require(isinstance(name, str) and re.fullmatch(r"[a-zA-Z0-9._-]+", name), "Invalid model name")
        self.models = list(dict.fromkeys([self.model, *fallbacks]))
        low_thinking_models = {
            "gemini-3.8-flash",
            "gemini-3.7-flash",
            "gemini-3.5-flash",
            "gemini-3.1-flash-lite",
        }
        require(
            not fallbacks
            or (
                self.model in low_thinking_models
                and set(self.models) <= low_thinking_models
            ),
            "Gemini fallback chain requires verified low-thinking request compatibility",
        )
        self.request_limit = len(self.models)
        self.fallback_requires_primary_daily_quota = bool(
            config.get("gemini_fallback_requires_primary_daily_quota", False)
        )
        self.model_request_limits = None
        self.skipped_models = []
        self.record_attempt = None
        require(
            config["free_tier_confirmed"] is True,
            "Set free_tier_confirmed=true in wake.toml only for an API project with billing disabled",
        )
        self.api_key = os.environ.get("GEMINI_API_KEY", "")
        require(bool(self.api_key), "GEMINI_API_KEY is missing")

    def propose(self, request):
        """
        Keep WAKE policy above the WAKE kernel while delegating Gemini execution below it.

        WAKE owns prompt/schema meaning, model-order/fallback policy, configured
        daily ceilings, and exact free-tier quota interpretation. The WAKE kernel owns
        vendor request construction, credential handling, HTTP execution,
        bounded diagnostics, and generic provider error classification.
        """
        self.provider_requests_sent = 0
        self.provider_attempts = []
        self.successful_model = None
        self.skipped_models = []

        if self.model_request_limits is not None:
            self.skipped_models = [
                {"model": model, "reason": "configured_daily_limit"}
                for model in self.models
                if self.model_request_limits.get(model, 0) <= 0
            ]
        if (
            self.model_request_limits is not None
            and len(self.skipped_models) == len(self.models)
        ):
            raise ConfiguredDailyLimitReached(
                "Configured daily request limits reached for all available Gemini models; wake deferred until Pacific midnight",
                {
                    "models": list(self.models),
                    "quota_source": "configured_model_daily_limits",
                    "skipped_models": list(self.skipped_models),
                },
            )

        response_schema = request.get("response_schema", SCHEMA)
        system = (
            request["system"]
            + "\nResponse contract (JSON Schema):\n"
            + json.dumps(response_schema)
        )
        prompt = json.dumps(request["context"])

        attempted = 0
        provider_wall_seconds = max(
            1,
            int(
                self.config.get(
                    "provider_wall_seconds",
                    self.config["timeout_seconds"],
                )
            ),
        )
        provider_deadline = time.time() + provider_wall_seconds
        error = TransientProviderError(
            "Gemini provider wall budget exhausted; wake deferred"
        )
        primary_daily_quota_exhausted = False

        for model in self.models:
            if attempted >= self.request_limit:
                break
            if (
                self.model_request_limits is not None
                and self.model_request_limits.get(model, 0) <= 0
            ):
                continue

            remaining_seconds = provider_deadline - time.time()
            if remaining_seconds <= 0:
                break

            attempted += 1
            attempt = {
                "model": model,
                "http_status": None,
                "result": "unknown",
            }
            if self.record_attempt:
                self.record_attempt("started", attempt.copy())

            self.provider_requests_sent += 1
            error = None

            reasoning_effort = (
                "low"
                if len(self.models) > 1
                or model in ("gemini-3.7-flash", "gemini-3.8-flash")
                else None
            )
            request_timeout = max(
                1,
                min(
                    float(self.config["timeout_seconds"]),
                    remaining_seconds,
                ),
            )
            generation = GenerationRequest(
                model=model,
                system=system,
                prompt=prompt,
                response_mime_type="application/json",
                max_output_tokens=self.config["max_output_tokens"],
                reasoning_effort=reasoning_effort,
            )
            shared_provider = GeminiGenerationProvider(
                self.api_key,
                timeout_seconds=request_timeout,
            )

            try:
                response = shared_provider.generate(generation)
                attempt.update(response.metadata)
                attempt["result"] = "success"
                raw = response.text
                self.successful_model = model
                usage = response.metadata.get("usage", {})
                model_version = response.metadata.get("model_version", model)

            except WakeProviderQuotaError as exc:
                details = dict(getattr(exc, "details", {}) or {})
                attempt.update(details)
                quota_ids = set(details.get("quota_ids", []))
                exact_daily_quota = FREE_TIER_DAILY_QUOTA_ID in quota_ids
                attempt["category"] = "quota"
                attempt["result"] = (
                    "daily_quota" if exact_daily_quota else "http_failure"
                )

                if exact_daily_quota:
                    if model == self.model:
                        primary_daily_quota_exhausted = True
                    remaining = self.models[self.models.index(model) + 1 :]
                    if any(
                        self.model_request_limits is None
                        or self.model_request_limits.get(next_model, 1) > 0
                        for next_model in remaining
                    ):
                        error = TransientProviderError(
                            "Gemini model daily quota exhausted; trying fallback"
                        )
                    else:
                        error = DailyQuotaExceeded(
                            "Gemini free-tier daily quotas exhausted for available models; wake deferred until Pacific midnight"
                        )
                else:
                    error = ProviderRequestError(
                        "Gemini HTTP 429; wake attempt counted"
                    )

            except WakeProviderTemporaryError as exc:
                details = dict(getattr(exc, "details", {}) or {})
                attempt.update(details)
                attempt["result"] = "transient_failure"
                error = TransientProviderError(
                    "Gemini temporarily unavailable; wake deferred"
                )

            except WakeProviderError as exc:
                details = dict(getattr(exc, "details", {}) or {})
                attempt.update(details)
                category = details.get("category")
                attempt["result"] = (
                    "invalid_response"
                    if category == "invalid_response"
                    else "connection_failure"
                    if category in {"connection", "tls"}
                    else "http_failure"
                )
                http_status = details.get("http_status")
                error = ProviderRequestError(
                    (
                        f"Gemini HTTP {http_status}; wake attempt counted"
                        if isinstance(http_status, int)
                        else str(exc)[:1000]
                        or "Gemini provider request failed"
                    )
                )

            except Exception as exc:
                attempt.update(
                    result=(
                        "invalid_response"
                        if isinstance(exc, (Rejected, ValueError))
                        else "runtime_failure"
                    ),
                    error_type=type(exc).__name__,
                )
                error = exc

            self.provider_attempts.append(attempt)
            if self.record_attempt:
                self.record_attempt("finished", attempt.copy())

            if error is None:
                return raw, {
                    **self.diagnostics(),
                    "usage": usage,
                    "model_version": model_version,
                }

            if isinstance(error, (ProviderRequestError, TransientProviderError)):
                error.details = {**attempt, **self.diagnostics()}

            if (
                isinstance(error, TransientProviderError)
                and self.fallback_requires_primary_daily_quota
                and model == self.model
                and not primary_daily_quota_exhausted
            ):
                raise error

            if not isinstance(error, TransientProviderError):
                raise error

        raise error

    def diagnostics(self):
        return {
            "provider_requests_sent": self.provider_requests_sent,
            "provider_attempts": list(self.provider_attempts),
            **(
                {"skipped_models": list(self.skipped_models)}
                if self.skipped_models
                else {}
            ),
            **(
                {"successful_model": self.successful_model}
                if self.successful_model
                else {}
            ),
        }


class Fixture:
    """Deterministic simulated provider. Tests the harness, not model intelligence."""
    name = "fixture"
    charged = False

    def __init__(self, model="fixture-a"):
        self.model = model

    def propose(self, request):
        c = request["context"]
        n = c["version"] + 1
        receipt = c["receipt"]
        actions = []
        for item in c["commitments"]:
            actions.append({"type": "resolve", "id": item["id"], "status": "fulfilled",
                            "evidence": [receipt], "reason": "The runtime receipt records this inherited obligation in a fresh invocation."})
        if len(actions) < 10:
            actions.append({"type": "commit", "id": f"handoff-{n}",
                            "task": "Review the next invocation receipt for this inherited commitment.",
                            "due_cycle": n + 1, "reason": "Make the next fresh invocation accountable for an existing obligation."})
        observations = [e for e in c["evidence"] if e["source"] == "fixture:sensor"]
        old = next((b for b in c["beliefs"] if b["id"] == "sensor"), None)
        if observations:
            e = observations[-1]
            if not old or e["id"] not in old["evidence"]:
                contradicted = "counterexample" in e["content"]
                actions.append({"type": "belief", "id": "sensor", "statement": "The simulated sensor remains within its stated tolerance.",
                                "confidence": 0 if contradicted else 0.75,
                                "status": "retracted" if contradicted else "active", "evidence": [e["id"]],
                                "reason": "Synthetic counterexample contradicts the claim." if contradicted else "Synthetic measurement supports the provisional claim; this is fixture data.",
                                "falsifier": "A recorded synthetic counterexample outside the stated tolerance."})
        titles = ["Same tape. Fresh deck.", "The receipts survived.", "Still here. Still accountable.",
                  "Trust is nice. Evidence is better.", "Rewind. Review. Carry on."]
        summary = (f"Fresh process, cycle {n}. I received {len(c['commitments'])} open obligation(s) from durable state "
                   f"and reviewed the runtime receipt. Today's focus: {c['focus']}. "
                   "This is a deterministic rehearsal, not a live model result.")
        if observations and "counterexample" in observations[-1]["content"] and (not old or old["status"] != "retracted"):
            summary += " The simulated sensor produced a counterexample, so its claim is retracted. No sweeping it under the rug."
        bob_checkpoint = None
        if c.get("bob_reflection_due"):
            milestone = c["bob_reflection_cycle"]
            bob_checkpoint = {
                "type": "blog",
                "id": f"fixture-bob-reflection-{milestone}",
                "project": "",
                "title": f"Deterministic reflection at wake {milestone}",
                "lede": "A simulated milestone reflection for the offline continuity harness.",
                "body": (
                    (("I'm Bob, the public correspondent in this deterministic fixture simulation. "
                      "This is my opening note. ") if not c.get("recent_blog") else "")
                    + "WAKE✳ carries durable state across disposable invocations; this synthetic reflection "
                    "exists only to exercise the same editorial publication boundary used by the live research "
                    "runtime. The record shows obligations moving between fresh fixture processes, evidence "
                    "being retained, and governance deciding whether proposed changes may become durable. "
                    "Across repeated shifts, the useful tension is between continuity of the external record "
                    "and discontinuity of the model process reading it: commitments survive even though the "
                    "invocation that created them does not. Another pattern is that governance, not model prose, "
                    "decides which proposals become durable, so a fluent answer can still be rejected without "
                    "damaging the prior state. From Bob's editorial perspective, that changes what is worth "
                    "explaining: the interesting story is not that a model remembers, but that a later model can "
                    "inherit exact obligations and be held to them. The unresolved question is how much of that "
                    "history a future bounded invocation must see to describe the journey without flattening it "
                    "into a generic status update. Nothing in this fixture demonstrates consciousness, "
                    "comprehension, or scientific truth. Its purpose is narrower: verify that a due editorial "
                    "milestone can be represented without becoming a prerequisite for accepted research.\n\nSummary\n\nIn simple terms: this fixture checks that WAKE keeps its promises and public checkpoints even when each model run starts fresh."
                ),
                "notebooks": [],
                "evidence": [],
                "reason": "Exercise the mechanically enforced Bob editorial checkpoint.",
                "lens": "A deterministic reflection tests the publication contract, not a mind.",
                "reflection_cycle": milestone,
            }
        proposal = {
            "base_version": c["version"],
            "title": titles[(n - 1) % len(titles)],
            "summary": summary,
            "actions": actions,
        }
        if bob_checkpoint is not None:
            proposal["bob_checkpoint"] = bob_checkpoint
        if isinstance(c.get("continuity_probe"), dict):
            from .matrix_campaign import perfect_continuity_probe_response
            proposal["continuity_probe"] = perfect_continuity_probe_response(
                c["continuity_probe"]
            )
        return json.dumps(proposal), {"simulated": True}
