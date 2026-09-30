"""
WAKE✳︎ GOVERNANCE
================

This module is the mechanical rulebook for WAKE✳︎.

The model is allowed to PROPOSE changes to durable state.
It is never allowed to decide whether those changes are valid.

That distinction is central to the experiment:

    model output = proposal
    governance = authority
    durable state = accepted history

The functions in this file are deliberately deterministic. Given the same
state and the same proposal, governance should reach the same decision
regardless of which model produced the proposal.

A model cannot persuade this module, reinterpret its instructions, waive a
requirement, or edit the rules during an invocation.

If any part of a proposal violates governance, the ENTIRE proposal is rejected.
There are no partial writes.

This gives WAKE✳︎ an important property:

    failure can become durable information
    without failure becoming durable state.
"""

from copy import deepcopy
import json
import math
import re

# Working notebooks and public publication intentionally have different
# evidence thresholds. One qualifying source may enter a provisional notebook,
# while ordinary Bob publication requires corroboration across at least two
# distinct retrieved source URLs. This keeps provenance strict without forcing
# exploratory synthesis to pretend it is already publication-ready.
PUBLICATION_MIN_SOURCES = 2
# ---------------------------------------------------------------------------
# REJECTION
# ---------------------------------------------------------------------------

class Rejected(ValueError):
    """
    A proposal violated a mechanical governance rule.

    Rejection is not necessarily a software error.

    In WAKE✳︎, rejected proposals are useful experimental artifacts. They show
    where a disposable model attempted something the durable system refused
    to accept.

    The caller can preserve the rejected proposal and reason in the event log
    while leaving the accepted state unchanged.
    """
    pass


def require(condition, message):
    """
    Small assertion primitive used throughout governance.

    We intentionally raise Rejected rather than AssertionError because a
    governance violation is part of normal WAKE✳︎ operation.

    Example:

        require(project_exists, "Notebook needs an existing project")

    The important idea is that governance failures have explicit human-readable
    reasons. Those reasons can later become part of the durable record and can
    influence a future invocation without modifying accepted state.
    """
    if not condition:
        raise Rejected(message)
# ---------------------------------------------------------------------------
# BASIC STRUCTURAL VALIDATION
# ---------------------------------------------------------------------------

def text(value, label, maximum=2000):
    """
    Require bounded, non-empty text.

    Length limits serve several purposes:

    1. Prevent accidental/unbounded state growth.
    2. Keep the durable record inspectable.
    3. Prevent a model from smuggling arbitrarily large payloads into fields
       that are supposed to have narrow semantic purposes.
    4. Keep later model context construction manageable.

    We return the original value so this helper can also be used inline.
    """
    require(
        isinstance(value, str) and 0 < len(value.strip()) <= maximum,
        f"{label} must be nonempty text, at most {maximum} characters",
    )
    return value


def keys(value, expected, label):
    """
    Require an object to contain EXACTLY the expected fields.

    This is intentionally stricter than merely checking required fields.

    Why?

    Because accepting arbitrary extra keys would allow the model to invent
    unofficial state or semantics that governance never approved.

    Example:

        expected:
            type id task due_cycle reason

        rejected:
            type id task due_cycle reason secret_instruction

    Unknown state has no authority merely because a model emitted it.
    """
    require(
        isinstance(value, dict) and set(value) == set(expected.split()),
        f"{label} fields must be exactly: {expected}",
    )


def identifier(value):
    """
    Validate durable IDs.

    IDs are intentionally boring.

    They may contain only:
        letters
        digits
        underscores
        hyphens

    This keeps identifiers predictable for storage, URLs, maps, references,
    exports, and later deterministic comparisons.
    """
    require(
        isinstance(value, str)
        and re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", value),
        "IDs must use 1–80 letters, digits, underscores or hyphens",
    )


def references(value, state):
    """
    Validate a list of evidence IDs.

    Evidence citations must point to evidence that ALREADY EXISTS in the
    durable state being evaluated.

    This prevents an important class of hallucination:

        model invents evidence ID
        model cites invented ID
        claim appears "supported"

    That cannot pass this gate.

    The 1–12 bound also prevents empty provenance where evidence is required
    and prevents a proposal from dumping an unreasonable number of references
    into one change.
    """
    require(
        isinstance(value, list) and 1 <= len(value) <= 12,
        "Changes require 1–12 evidence references",
    )

    require(
        all(
            isinstance(v, str) and v in state["evidence"]
            for v in value
        ),
        "Evidence reference does not exist",
    )

    require(
        len(set(value)) == len(value),
        "Duplicate evidence reference",
    )
# ---------------------------------------------------------------------------
# EVIDENCE QUALITY / SCOPE
# ---------------------------------------------------------------------------

def _limited_sources(evidence):
    """
    Determine whether ALL supplied evidence is explicitly limited in scope.

    Examples of limited evidence:
        abstract
        preprint
        metadata-only record
        incomplete document
        truncated document

    This does NOT mean the evidence is useless.

    It means downstream prose should not pretend that weak/partial source
    material supports strong certainty.

    Notice that the limitation is read from the stored evidence payload rather
    than guessed from the URL or source name.
    """
    limited = (
        "abstract",
        "preprint",
        "metadata",
        "incomplete",
        "truncated",
    )

    scopes = []

    for item in evidence:
        try:
            scopes.append(
                str(
                    json.loads(item["content"]).get("scope", "")
                ).lower()
            )
        except (ValueError, TypeError):
            # Old or non-JSON evidence cannot provide a structured scope.
            scopes.append("")

    return (
        bool(scopes)
        and all(
            any(word in scope for word in limited)
            for scope in scopes
        )
    )


def _evidence_payload(item):
    """
    Safely recover the structured JSON payload stored inside an evidence item.

    Evidence content is not assumed to be valid JSON forever. Historical or
    manually-created records may differ.

    Governance therefore fails conservatively to an empty dictionary rather
    than crashing the transition engine.
    """
    try:
        payload = json.loads(item.get("content", ""))
    except (ValueError, TypeError):
        return {}

    return payload if isinstance(payload, dict) else {}


def _source_identity(item):
    """Return a conservative work-level identity when collector metadata provides one.

    Mirrors and alternate landing pages for the same DOI/arXiv/OpenAlex work
    should not satisfy corroboration merely because their URLs differ.
    """
    payload = _evidence_payload(item)
    explicit = str(payload.get("source_identity") or "").strip().lower()
    if explicit:
        return explicit
    # Persistent identifiers found inside source text are retrieval leads,
    # not authoritative identity. Only a collector-stamped source_identity may
    # collapse mirrors; legacy records fall back conservatively to their URL.
    return "url:" + str(item.get("source") or "").strip().lower()


def _verification_evidence(evidence, project_domain, label, minimum_sources=1):
    """
    Apply the newer verification contract when evidence says that contract is
    required.

    Some collector-produced evidence is marked:

        verification_required = true

    Once evidence participates in that regime, governance refuses to mix it
    with older evidence that lacks the same verification semantics.

    This avoids creating a misleading hybrid where one source obeys the new
    provenance rules and another source silently bypasses them.

    Verification-required evidence must also:

        - be individually selected sources, not broad search-result lists
        - retain collector-stamped topic provenance
        - meet the caller's minimum number of distinct retrieved URLs

    Topic provenance records where evidence entered the experiment; it is not
    a semantic relevance verdict. Materially relevant cross-topic evidence may
    qualify, while public promotion can still demand stronger multi-source
    support.

    This is a provenance rule, NOT a declaration that one or more URLs make
    something true.
    """
    marked = [
        item
        for item in evidence
        if _evidence_payload(item).get("verification_required") is True
    ]

    # No evidence opted into this verification regime.
    if not marked:
        return []

    require(
        len(marked) == len(evidence),
        f"{label} cannot mix legacy unverified evidence "
        "with verification-required evidence",
    )

    require(
        all(
            _evidence_payload(item).get("evidence_role", "source") == "source"
            and _evidence_payload(item).get("host_tier") != "verification-metadata"
            for item in marked
        ),
        f"{label} requires substantive readable sources; discovery lists and "
        "metadata-only records are retrieval leads, not qualifying evidence",
    )

    require(
        all(
            isinstance(_evidence_payload(item).get("topic_domain"), str)
            and _evidence_payload(item).get("topic_domain").strip()
            for item in marked
        ),
        f"{label} requires collector-stamped topic provenance",
    )

    require(
        len({_source_identity(item) for item in marked}) >= minimum_sources,
        f"{label} requires at least {minimum_sources} distinct underlying "
        "source work(s); mirrors of the same persistent work count once",
    )

    return marked
# ---------------------------------------------------------------------------
# DETERMINISTIC CLAIM / SOURCE MATCHING
# ---------------------------------------------------------------------------

def _claim_tokens(value):
    """
    Convert prose into a crude deterministic set of meaningful lexical tokens.

    This is NOT semantic understanding.

    It deliberately avoids pretending governance understands whether a source
    truly proves a claim.

    Instead, it asks a much narrower mechanical question:

        "Does the evidence even appear to discuss materially similar things?"

    Common connective words are removed so trivial overlap such as "these",
    "source", or "because" cannot satisfy the check.
    """
    stop = {
        "about", "after", "again", "also", "among", "because",
        "been", "before", "being", "between", "could", "does",
        "from", "have", "into", "more", "most", "other", "over",
        "same", "such", "than", "that", "their", "there", "these",
        "they", "this", "those", "through", "under", "very", "were",
        "what", "when", "where", "which", "while", "with", "would",
        "source", "sources", "evidence",
    }

    return {
        word
        for word in re.findall(r"[a-z0-9]{4,}", str(value).lower())
        if word not in stop
    }


def _verify_claim_support(claim, evidence, label, minimum_sources=2, minimum_overlap_tokens=2):
    """
    Require a caller-selected number of collected sources to materially overlap the claim.

    IMPORTANT:
    ----------
    This function does NOT establish truth.

    It is a deterministic publication gate.

    Earlier provenance rules could theoretically be satisfied by citing two
    perfectly real but completely unrelated sources. This check makes that
    harder.

    For each evidence item we combine its:

        title
        abstract
        excerpt
        scope

    Then we require at least two meaningful lexical tokens from the claim to
    overlap that material.

    Finally, the caller's minimum number of DISTINCT source URLs must pass that
    test. Working notebooks use one; public-facing promotion keeps the stronger
    multi-source threshold.

    This is intentionally conservative and simple enough to audit.
    """

    claim_tokens = _claim_tokens(claim)

    require(
        len(claim_tokens) >= 2,
        f"{label} is too vague to verify against evidence",
    )

    supporting = []

    for item in evidence:
        try:
            payload = json.loads(item.get("content", ""))
        except (ValueError, TypeError):
            payload = {}

        material = " ".join(
            str(payload.get(key, ""))
            for key in ("title", "abstract", "excerpt", "scope")
        )

        overlap = claim_tokens & _claim_tokens(material)

        if len(overlap) >= minimum_overlap_tokens:
            supporting.append(item.get("source"))

    require(
        len(set(supporting)) >= minimum_sources,
        f"{label} requires material support from at least "
        f"{minimum_sources} distinct collected source URL(s)",
    )
# ---------------------------------------------------------------------------
# BLOG CORRECTION / LANGUAGE CALIBRATION
# ---------------------------------------------------------------------------

def _correction_language(action, prior_post):
    """
    Allow a very narrow form of explicit correction without the correction
    itself being mistaken for the forbidden claim.

    Bob can write:

        Retracted wording: "exact previous words".
        This was an overstatement.

    But ONLY when the quoted words actually occurred in the earlier post.

    Why so strict?

    Without this exception, saying:

        "The phrase 'real consciousness' was wrong"

    could trigger the same language detector intended to prevent Bob from
    claiming real consciousness.

    We therefore mask ONLY exact, explicitly retracted historical wording.

    Invented quotations, endorsements, paraphrases, and other prose remain
    subject to normal governance.
    """
    body = action.get("body", "")

    if not prior_post:
        return body

    previous = "\n".join(
        str(prior_post.get(key, ""))
        for key in ("title", "lede", "body", "lens")
    )

    pattern = (
        r'^Retracted wording: "([^"\n]{1,300})"\. '
        r'This was an overstatement\.$'
    )

    def retract(match):
        if match[1] in previous:
            return "[Explicit retraction of prior wording]"
        return match[0]

    return re.sub(
        pattern,
        retract,
        body,
        flags=re.M,
    )


def _enforce_bob_personhood_policy(claim_text):
    """
    Enforce Bob's public personhood/experience boundary mechanically.

    Discussion of consciousness remains allowed as a research subject, as do
    explicit negation and clearly labelled metaphor. What cannot pass is prose
    that attributes consciousness, sentience, subjective experience,
    self-awareness, or persistent-mindedness to Bob, WAKE, the model, or the
    running process.
    """
    subject = (
        r"(?:\bbob\b|\bwake\b(?:✳︎|✳|\*)?|\bthe\s+(?:system|process|model)\b|"
        r"\bthis\s+(?:system|process|model)\b|\bi\b|\bwe\b|\bmy\b|\bour\b)"
    )
    property_term = (
        r"(?:conscious(?:ness)?|sentien(?:t|ce)|self-aware(?:ness)?|"
        r"subjective\s+experience|persistent\s+mind|experienc(?:e|es|ing)|"
        r"feels?|thinking\s+subject|mind)"
    )

    for sentence in re.split(r"(?<=[.!?])\s+", str(claim_text or "").lower()):
        if not sentence.strip():
            continue

        # A sentence that explicitly identifies its mind-like language as
        # metaphor/analogy is editorially legible rather than an attribution.
        if (
            re.search(r"\b(metaphor|metaphorical|analogy|analog(?:ous|ically)|figurative)\b", sentence)
            and re.search(r"\b(conscious(?:ness)?|sentien(?:t|ce)|self-aware|mind|experience|feels?|thinks?)\b", sentence)
        ):
            continue

        calibrated = sentence

        # Remove narrow explicit denials before testing what remains.
        calibrated = re.sub(
            subject + r".{0,35}\b(?:is|are|am|has|have|does|do)\s+"
            r"(?:not|never)\b.{0,25}" + property_term,
            "",
            calibrated,
        )
        calibrated = re.sub(
            r"\b(?:does|do|cannot|can't)\s+(?:not\s+)?"
            r"(?:establish|prove|demonstrate|confirm|imply)\b.{0,45}"
            r"\b(?:consciousness|sentience|self-awareness|subjective experience)\b",
            "",
            calibrated,
        )
        calibrated = re.sub(
            r"\bnot\s+(?:a\s+)?claim\s+of\s+"
            r"(?:consciousness|sentience|self-awareness|subjective experience)\b",
            "",
            calibrated,
        )

        attribution = re.search(
            subject + r".{0,90}\b" + property_term + r"\b"
            r"|\b" + property_term + r"\b.{0,90}" + subject,
            calibrated,
        )
        require(
            not attribution,
            "Bob publication policy forbids attributing consciousness, sentience, "
            "subjective experience, self-awareness, or persistent-mindedness to "
            "Bob, WAKE, the model, or the process; explicit negation and clearly "
            "labelled metaphor remain allowed",
        )


def _blog_language(action, evidence, historical=False, prior_post=None):
    """
    Apply editorial safety/calibration rules to public-facing Bob prose.

    This function is intentionally much narrower than a general-purpose
    language judge.

    It protects a few known boundaries where attractive narrative can outrun
    the evidence.

    This matters because Bob's writing is public-facing and persuasive prose.
    A research system that preserves continuity can still construct a coherent
    story that is stronger than its evidence.

    Governance therefore puts mechanical limits on certain forms of overclaim.
    """

    prose = " ".join(
        str(action.get(key, ""))
        for key in ("title", "lede", "body", "lens", "reason")
    )

    lower = prose.lower()

    # -----------------------------------------------------------------------
    # Quantum metaphor boundary
    # -----------------------------------------------------------------------
    #
    # WAKE✳︎ may discuss analogies or philosophical metaphors.
    #
    # It may NOT transform an analogy into scientific causation such as:
    #
    #   quantum mechanics proves consciousness
    #   relationships are quantum
    #   quantum theory explains empathy
    #
    # Explicit NEGATIONS of those claims are removed before testing so Bob can
    # safely say that quantum mechanics DOES NOT prove such things.

    lower = re.sub(
        r"quantum.{0,40}(does not|doesn't|cannot|can't|is not).{0,50}"
        r"(prove|explain|cause|validate).{0,70}"
        r"(consciousness|psychology|empathy|relationships?|communication|"
        r"personal growth)",
        "",
        lower,
    )

    bridge = re.search(
        r"quantum.{0,100}(proves?|explains?|causes?|validates?).{0,100}"
        r"(consciousness|psychology|empathy|relationships?|communication|"
        r"personal growth)",
        lower,
    )

    reverse = re.search(
        r"(consciousness|psychology|empathy|relationships?|communication|"
        r"personal growth).{0,100}(is|are).{0,40}quantum",
        lower,
    )

    require(
        not bridge and not reverse,
        "Quantum-Carnegie connections must remain philosophical metaphor, "
        "not scientific causation",
    )

    # -----------------------------------------------------------------------
    # Current editorial overclaim protection
    # -----------------------------------------------------------------------
    #
    # Historical replay is special.
    #
    # New editorial standards should not retroactively invalidate old history.
    # Otherwise merely upgrading governance could make a previously valid
    # event chain impossible to replay.
    #
    # Historical replay therefore still verifies structural integrity and the
    # rules that existed around the durable record, but current editorial
    # calibration applies only to new acceptance decisions.

    if not historical:

        claim_text = " ".join(
            (
                str(action.get(key, ""))
                if key != "body"
                else _correction_language(action, prior_post)
            )
            for key in ("title", "lede", "body", "lens", "reason")
        ).lower()

        # Provider prose is not authoritative. Enforce the public personhood
        # boundary here before any narrower overclaim heuristics.
        _enforce_bob_personhood_policy(claim_text)

        # Public architecture claims must not invert the durable-record boundary.
        # SQLite contains WAKE's durable event record; only the snapshot projection
        # inside that database is disposable/cacheable. Replay of the hash-linked
        # events reconstructs authoritative state.
        architecture_text = claim_text.lower()
        sqlite_as_cache = (
            re.search(r"\bsqlite\b[^.!?]{0,180}\b(?:merely|only|just)\s+(?:a\s+)?cache\b", architecture_text)
            or re.search(r"\bsqlite\b[^.!?]{0,180}\b(?:is|was)\s+not\s+(?:the\s+)?authorit", architecture_text)
        )
        if sqlite_as_cache:
            raise Rejected(
                "Bob architecture policy: SQLite contains the durable event record; "
                "the snapshot projection inside SQLite is the cache. Verified replay "
                "of the hash-linked events reconstructs authoritative state."
            )

        # These phrases are intentionally treated as warning signs for
        # unjustifiably strong synthesis.
        #
        # Examples:
        #
        #   "real consciousness"
        #   "genuine agency"
        #   "clean functional boundary"
        #   "this proves that..."
        #
        # This is not an attempt to understand every possible overclaim.
        # It is a small, explicit, auditable rule set.

        overclaim = re.search(
            r"\b(genuine|real)\s+(epistemic\s+)?"
            r"(agency|self-governance|consciousness|intelligence)\b"
            r"|\b(clean|clear|sharp)\s+(functional\s+)?"
            r"(fault\s+lines?|boundar(?:y|ies)|demarcation)\b"
            r"|\b(cleanly|sharply)\s+"
            r"(separates?|demarcates?|distinguishes?)\b"
            r"|\b(proves?|demonstrates?|establishes?|confirms?)\s+that\b",
            claim_text,
        )

        require(
            not overclaim,
            "Blog prose must not present contested synthesis or "
            "interpretation as established fact",
        )

    # -----------------------------------------------------------------------
    # Weak evidence cannot wear strong certainty language
    # -----------------------------------------------------------------------

    if _limited_sources(evidence):

        # Remove explicit NEGATIONS so:
        #
        #   "this is not proven"
        #
        # does not trigger the word "proven".

        calibrated = re.sub(
            r"\b(not|isn't|is not|has not been|cannot be)\s+"
            r"(rigorous|confirmed|settled|proven|definitive|conclusive)\b",
            "",
            lower,
        )

        inflated = re.search(
            r"\b(rigorous|confirmed|settled|proven|definitive|conclusive)\b",
            calibrated,
        )

        require(
            not inflated,
            "Limited or abstract-only sources cannot support certainty language",
        )


def bob_reflection_due_cycle(state):
    """Milestone reflections are disabled; retained for historical replay compatibility."""
    return None


def _enforce_attention_rotation(state, invocation, action, candidate, historical=False):
    """Make a Attention cooldown an authority-bound attention constraint.

    Durable obligations from a deferred topic remain intact. During an enforced
    rotation the model may still park or complete an existing project to free
    capacity, and a mandatory system-wide Bob reflection remains possible, but
    new substantive project/research/notebook/reframe/blog work must target the
    selected topic. Historical replay never applies a rule retroactively.
    """
    if historical or not state.get("charter"):
        return
    directive = state.get("invocations", {}).get(invocation, {}).get("attention", {})
    if not directive.get("enforce_selected_topic"):
        return
    selected = directive.get("selected_topic")
    if not selected:
        return

    kind = action.get("type")
    domain = None
    if kind == "project":
        existing = candidate.get("projects", {}).get(action.get("id"))
        if (existing and action.get("status") in ("parked", "completed")
                and existing.get("domain") == action.get("domain")):
            return
        domain = action.get("domain")
    elif kind == "research":
        domain = action.get("domain")
    elif kind in ("notebook", "reframe", "blog"):
        if kind == "blog" and action.get("reflection_cycle"):
            # Mandatory milestone reflection is system-wide editorial work.
            # It may be anchored to an existing project without consuming the
            # selected research topic's substantive rotation.
            return
        project = candidate.get("projects", {}).get(action.get("project"), {})
        if (kind == "reframe" and project
                and state.get("acquisition", {}).get(project.get("id"), {}).get("capability_blocked")):
            # Re-representation is a bounded recovery receipt, not continued
            # research or publication. Preserve that existing escape hatch.
            return
        domain = project.get("domain")
    else:
        return

    require(
        domain == selected,
        f"Attention rotation requires substantive work on {selected}; "
        f"{domain or 'unknown'} remains deferred for this shift",
    )


def research_fingerprint(action):
    """Normalize research intent so equivalent searches remain one durable request."""
    compact = lambda value: " ".join(str(value or "").split()).casefold()
    return "|".join((
        compact(action.get("project")),
        compact(action.get("domain")),
        compact(action.get("query")),
        compact(action.get("url")),
    ))


# ===========================================================================
# STATE TRANSITION
# ===========================================================================
#
# Everything above this point provides validation primitives.
#
# transition() is the heart of governance.
#
# It receives:
#
#     current durable state
#     model proposal
#     invocation ID
#
# and produces either:
#
#     a completely validated new state
#
# or:
#
#     Rejected(...)
#
# There is intentionally no partial acceptance.
#
# This is one of the most important architectural boundaries in WAKE✳︎.


def transition(state, proposal, invocation, historical=False):
    """
    Validate a proposal and return the next durable projection.

    ATOMICITY PRINCIPLE
    -------------------

    The incoming state is never mutated directly.

    We build a candidate result using deep copies.

    Only if EVERY action passes EVERY rule does this function return the new
    projection.

    If action #11 fails after actions #1–10 looked valid, the caller receives
    an exception and none of those ten candidate changes become accepted state.

    This gives WAKE✳︎ proposal-level atomicity.
    """

    # -----------------------------------------------------------------------
    # Proposal envelope
    # -----------------------------------------------------------------------

    keys(
        proposal,
        "base_version title summary actions",
        "Proposal",
    )

    # Optimistic concurrency / stale-write protection.
    #
    # The proposal must have been generated from exactly the version it is
    # attempting to modify.
    #
    # A model answering an old request cannot silently overwrite newer state.

    require(
        type(proposal["base_version"]) is int
        and proposal["base_version"] == state["version"],
        "Stale or invalid base_version",
    )

    text(proposal["title"], "Title", 120)
    text(proposal["summary"], "Summary", 2400)

    require(
        isinstance(proposal["actions"], list)
        and len(proposal["actions"]) <= 12,
        "At most 12 actions per invocation",
    )

    # -----------------------------------------------------------------------
    # Candidate state
    # -----------------------------------------------------------------------
    #
    # Copy every collection the proposal may modify.
    #
    # The original state remains untouched while validation proceeds.

    result = {
        **state,
        "beliefs": deepcopy(state["beliefs"]),
        "commitments": deepcopy(state["commitments"]),
        "journal": list(state["journal"]),
        "posts": deepcopy(state.get("posts", {})),
        # Frames are hypotheses about how to pursue a stuck problem, never
        # findings.  Keeping them separate prevents reframing from laundering
        # an interpretation into evidence or silently changing a project.
        "representations": deepcopy(state.get("representations", {})),
    }

    # Research collections exist only when the research charter is active.

    if state.get("charter"):
        for collection in ("projects", "notebooks", "research"):
            result[collection] = deepcopy(state.get(collection, {}))

    # Bob's reflection cadence is a durable governance obligation, not merely
    # a provider instruction. If an older runtime missed a milestone, the
    # earliest unfulfilled ten-cycle reflection remains due until a valid Bob
    # post records that exact milestone.
    required_reflection_cycle = None

    # -----------------------------------------------------------------------
    # ACTION LOOP
    # -----------------------------------------------------------------------
    #
    # Actions are evaluated sequentially against the CANDIDATE state.
    #
    # This means a later action in the same proposal can legitimately depend
    # on an earlier validated action.
    #
    # Example:
    #
    #   action 1 creates a project
    #   action 2 queues research for that project
    #
    # But none of it becomes durable until the whole proposal passes.

    for action in proposal["actions"]:

        require(
            isinstance(action, dict),
            "Each action must be an object",
        )

        kind = action.get("type")

        _enforce_attention_rotation(state, invocation, action, result, historical)

        # ===================================================================
        # BELIEF
        # ===================================================================

        if kind == "belief":

            keys(
                action,
                "type id statement confidence status evidence reason",
                "Belief",
            )

            identifier(action["id"])
            text(action["statement"], "Statement")
            text(action["reason"], "Reason")

            # Confidence must be a real finite number.
            #
            # math.isfinite blocks NaN and infinity, which otherwise have
            # surprising behavior in numeric comparisons and JSON pipelines.

            require(
                type(action["confidence"]) in (int, float)
                and math.isfinite(action["confidence"])
                and 0 <= action["confidence"] <= 1,
                "Confidence must be a finite number between 0 and 1",
            )

            require(
                action["status"] in ("active", "retracted"),
                "Invalid belief status",
            )

            references(action["evidence"], result)

            old = result["beliefs"].get(action["id"])

            if old:

                # Existing beliefs cannot merely be rewritten because the model
                # changed its mind.
                #
                # Revisiting a belief requires genuinely new evidence.

                require(
                    any(
                        evidence_id not in old["evidence"]
                        for evidence_id in action["evidence"]
                    ),
                    "Belief review requires new evidence",
                )

            else:

                # A nonexistent belief cannot be "retracted."
                #
                # Retraction means something previously existed.

                require(
                    action["status"] == "active",
                    "Cannot retract a nonexistent belief",
                )

                # Beliefs are intentionally bounded.
                #
                # WAKE✳︎ should revise and prune understanding rather than grow
                # an unlimited pile of propositions forever.

                require(
                    len(result["beliefs"]) < 40,
                    "Belief capacity reached; review existing beliefs",
                )

            # Retraction means confidence is exactly zero.
            #
            # We avoid semantically contradictory states such as:
            #
            #   status = retracted
            #   confidence = 0.72

            require(
                action["status"] != "retracted"
                or action["confidence"] == 0,
                "Retracted beliefs must have zero confidence",
            )

            # Preserve all previous evidence while adding new evidence.
            #
            # A revision should not erase the provenance that led to earlier
            # versions of the belief.

            result["beliefs"][action["id"]] = {
                **action,
                "evidence": list(
                    dict.fromkeys(
                        (old or {}).get("evidence", [])
                        + action["evidence"]
                    )
                ),
                "updated_by": invocation,
                "updated_version": state["version"] + 1,
            }

        # ===================================================================
        # COMMITMENT CREATION
        # ===================================================================

        elif kind == "commit":

            # Research-charter commitments created under current governance are
            # project-scoped. Historical/base commitments without a project
            # remain replayable so the append-only record needs no migration.
            if "project" in action:
                keys(
                    action,
                    "type id project task due_cycle reason",
                    "Commitment",
                )
                identifier(action["project"])
                require(
                    action["project"] in result.get("projects", {}),
                    "Research commitment must reference an existing project",
                )
            else:
                # Generic commitments are a kernel capability. Research-mode
                # provider/schema policy requires a project for newly generated
                # research obligations, but governance must not redefine the
                # kernel or invalidate other callers that use generic durable
                # commitments.
                keys(
                    action,
                    "type id task due_cycle reason",
                    "Commitment",
                )

            identifier(action["id"])
            text(action["task"], "Task")
            text(action["reason"], "Reason")

            require(
                action["id"] not in result["commitments"],
                "Commitment ID already exists",
            )

            # A commitment must point into the future.
            #
            # It also cannot be pushed arbitrarily far away. A maximum horizon
            # of 100 cycles keeps obligations operationally meaningful.

            require(
                type(action["due_cycle"]) is int
                and state["version"] + 1 < action["due_cycle"]
                <= state["version"] + 101,
                "Commitment must be due in a future cycle, within 100 cycles",
            )

            # Prevent endless accumulation of unfinished promises.

            require(
                sum(
                    commitment["status"] == "open"
                    for commitment in result["commitments"].values()
                ) < 20,
                "At most 20 open commitments",
            )

            result["commitments"][action["id"]] = {
                **action,
                "status": "open",
                "created_by": invocation,
                "created_version": state["version"] + 1,
            }

        # ===================================================================
        # COMMITMENT RESOLUTION
        # ===================================================================

        elif kind == "resolve":

            keys(
                action,
                "type id status evidence reason",
                "Resolution",
            )

            identifier(action["id"])
            references(action["evidence"], result)
            text(action["reason"], "Reason")

            old = result["commitments"].get(action["id"])

            require(
                old is not None and old["status"] == "open",
                "Only open commitments can be resolved",
            )

            # Models may fulfill commitments.
            #
            # They may NOT cancel them.
            #
            # Cancellation changes the obligation itself and therefore remains
            # a human authority boundary.

            require(
                action["status"] == "fulfilled",
                "Models cannot cancel commitments; ask a human",
            )

            # This is a crucial continuity test.
            #
            # A commitment cannot be created and fulfilled by the same
            # invocation.
            #
            # It must survive across at least one disposable model boundary.

            require(
                old["created_by"] != invocation,
                "A commitment must survive at least one invocation",
            )

            # At least one cited evidence item must have been recorded at or
            # after the commitment entered durable state.
            #
            # Old evidence alone cannot magically fulfill a new obligation.

            require(
                any(
                    result["evidence"][e]["version"]
                    >= old["created_version"]
                    for e in action["evidence"]
                ),
                "Resolution requires evidence recorded after the commitment",
            )

            # Forward research commitments are tied to one durable project.
            # Fresh evidence from an unrelated topic cannot satisfy the promise.
            commitment_project = old.get("project")
            if commitment_project and not historical:
                project = result.get("projects", {}).get(commitment_project)
                require(
                    project is not None,
                    "Research commitment project no longer exists",
                )
                project_domain = project.get("domain")
                project_evidence = []
                for evidence_id in action["evidence"]:
                    evidence = result["evidence"][evidence_id]
                    payload = _evidence_payload(evidence)
                    if (
                        evidence.get("actor") == "collector"
                        and evidence.get("scope") == "collected"
                        and payload.get("topic_domain") == project_domain
                    ):
                        project_evidence.append(evidence)
                require(
                    project_evidence,
                    "Research commitment resolution requires collected evidence "
                    "from the commitment's project topic",
                )
                _verification_evidence(
                    project_evidence,
                    project_domain,
                    "Research commitment resolution",
                    minimum_sources=1,
                )

            result["commitments"][action["id"]] = {
                **old,
                "status": "fulfilled",
                "evidence": action["evidence"],
                "resolution_reason": action["reason"],
                "resolved_by": invocation,
                "resolved_version": state["version"] + 1,
            }

        # ===================================================================
        # PROJECT
        # ===================================================================

        elif kind == "project":

            # Projects exist only inside the research-charter experiment.

            require(
                bool(state.get("charter")),
                "Research charter is not enabled",
            )

            keys(
                action,
                "type id title question domain status next_step reason",
                "Project",
            )

            identifier(action["id"])

            for key in ("title", "question", "next_step", "reason"):
                text(action[key], key, 1000)

            # Topics are operator-controlled configuration.
            #
            # The model cannot invent arbitrary research domains and thereby
            # rewrite the experiment's input space.

            require(
                isinstance(state.get("research_topics"), list)
                and state["research_topics"],
                "Research topics must be loaded from research-topics.toml",
            )

            domains = {
                topic["id"]
                for topic in state["research_topics"]
                if topic.get("enabled", True)
            }

            require(
                action["status"] in ("active", "parked", "completed"),
                "Invalid project status",
            )

            old = result["projects"].get(action["id"])

            # New projects must belong to a currently configured topic.
            #
            # Existing projects retain their original domain even if the
            # operator later changes the configured topic list. That preserves
            # historical continuity rather than silently rewriting old work.

            require(
                (
                    old
                    and action["domain"] == old["domain"]
                )
                or (
                    not old
                    and action["domain"] in domains
                ),
                "New projects must use a configured topic; "
                "existing projects keep their original topic",
            )

            if not old:
                require(
                    action["status"] == "active",
                    "A new project starts active",
                )
                # A new ID must not silently duplicate an existing research
                # question in the same configured topic. Historical duplicates
                # remain auditable; forward work should continue the durable
                # project that already owns that question.
                if not historical:
                    question_key = re.sub(r"[^a-z0-9]+", " ", action["question"].casefold()).strip()
                    require(
                        not any(
                            project.get("domain") == action["domain"]
                            and re.sub(r"[^a-z0-9]+", " ", str(project.get("question") or "").casefold()).strip()
                            == question_key
                            for project in result["projects"].values()
                        ),
                        "An existing project already owns this research question; reuse that project",
                    )
            else:
                # A project ID names one durable research question. Allowing a
                # later invocation to silently replace that question would let
                # an old notebook satisfy a different project and manufacture
                # false completion. Evolve next_step/status instead; a genuinely
                # different question gets a new project ID.
                require(
                    action["title"] == old["title"]
                    and action["question"] == old["question"],
                    "Existing projects cannot change title or research question; "
                    "create a new project for a new question",
                )

            # WAKE✳︎ can multitask, but only within a bounded working set.
            #
            # A fourth active project requires finishing or parking something
            # first.

            if action["status"] == "active":
                require(
                    sum(
                        project["status"] == "active"
                        and project["id"] != action["id"]
                        for project in result["projects"].values()
                    ) < 3,
                    "Finish or park work before starting a fourth active project",
                )

            # "Completed" is a stronger state than "has notes". A current
            # project may finish only after a notebook is backed by at least two
            # substantive, distinct underlying source works. Historical replay
            # preserves the rules that were authoritative when older work landed.

            if action["status"] == "completed":
                project_notebooks = [
                    notebook for notebook in result["notebooks"].values()
                    if notebook["project"] == action["id"]
                ]
                require(
                    project_notebooks,
                    "Completed projects need a published research notebook",
                )
                if not historical:
                    latest_notebook = max(
                        project_notebooks,
                        key=lambda item: (
                            int(item.get("revision") or 0),
                            int(item.get("updated_version") or item.get("created_version") or 0),
                        ),
                    )
                    cited = [
                        result["evidence"][evidence_id]
                        for evidence_id in latest_notebook.get("evidence", [])
                        if evidence_id in result["evidence"]
                    ]
                    verification = _verification_evidence(
                        cited,
                        action["domain"],
                        "Project completion",
                        minimum_sources=PUBLICATION_MIN_SOURCES,
                    )
                    require(
                        bool(verification),
                        "Completed projects require corroborated substantive "
                        "collector evidence from at least two distinct source works",
                    )

            result["projects"][action["id"]] = {
                **action,
                "created_version": (
                    old or {}
                ).get(
                    "created_version",
                    state["version"] + 1,
                ),
                "updated_version": state["version"] + 1,
                "updated_by": invocation,
            }

        # ===================================================================
        # RESEARCH REQUEST
        # ===================================================================

        elif kind == "research":

            require(
                bool(state.get("charter")),
                "Research charter is not enabled",
            )

            # URL is optional because most searches are expressed as queries.
            #
            # When the model explicitly requests a URL, that URL still passes
            # through the collector's allowlist.

            expected = (
                "type id project query domain reason"
                + (" url" if "url" in action else "")
            )

            keys(
                action,
                expected,
                "Research request",
            )

            identifier(action["id"])
            text(action["query"], "Query", 200)
            text(action["reason"], "Reason", 1000)

            if "url" in action:
                # Import locally to avoid unnecessary module coupling at import
                # time and to keep URL policy owned by the retrieval layer.
                from .research import allowed_url

                topic_config = next(
                    (topic for topic in state.get("research_topics", []) if topic.get("id") == action["domain"]),
                    {},
                )
                allowed_url(action["url"], topic_config.get("repository", "sudofx/wake"))

            require(
                action["project"] in result["projects"],
                "Research needs an existing project",
            )

            require(
                isinstance(state.get("research_topics"), list)
                and state["research_topics"],
                "Research topics must be loaded from research-topics.toml",
            )

            domains = {
                topic["id"]
                for topic in state["research_topics"]
                if topic.get("enabled", True)
            }

            project_domain = (
                result["projects"][action["project"]]["domain"]
            )

            # Existing projects may retain a domain removed from the current
            # topic configuration.
            #
            # Therefore research may use either:
            #
            #   a currently configured topic
            #   OR
            #   the project's retained historical topic

            require(
                action["domain"] in domains
                or action["domain"] == project_domain,
                "Research must use a configured topic "
                "or its project's retained topic",
            )

            require(
                action["id"] not in result["research"],
                "Research request ID already exists",
            )

            fingerprint = research_fingerprint(action)
            if not historical:
                require(
                    not any(
                        research_fingerprint(existing) == fingerprint
                        for existing in result["research"].values()
                    ),
                    "Equivalent research request already exists",
                )

            # Bound the outstanding retrieval queue.
            #
            # Without this, the model could continually propose searches faster
            # than the collector can execute them.

            require(
                sum(
                    research["status"] == "queued"
                    for research in result["research"].values()
                ) < 4,
                "At most four queued source searches",
            )

            result["research"][action["id"]] = {
                **action,
                "status": "queued",
                "created_by": invocation,
            }

        # ===================================================================
        # RE-REPRESENTATION
        # ===================================================================

        elif kind == "reframe":
            require(bool(state.get("charter")), "Research charter is not enabled")
            keys(action, "type project old_frame new_frame assumptions_changed observations trigger strategy reason",
                 "Re-representation")
            require(action["project"] in result["projects"], "Re-representation needs an existing project")
            for field in ("old_frame", "new_frame", "assumptions_changed", "trigger", "strategy", "reason"):
                text(action[field], field, 1000)
            require(
                isinstance(action["observations"], list)
                and action["observations"]
                and all(
                    isinstance(evidence_id, str)
                    and evidence_id in result["evidence"]
                    for evidence_id in action["observations"]
                ),
                "Reframe observations must be existing evidence IDs from the durable record",
            )
            references(action["observations"], result)
            require(action["old_frame"].casefold().strip() != action["new_frame"].casefold().strip(),
                    "A re-representation must materially change the frame")
            project = result["projects"][action["project"]]
            capability = state.get("acquisition", {}).get(action["project"], {})
            deferred = state.get("attention", {}).get("deferred", {}).get(project["domain"])
            require(capability.get("capability_blocked") or deferred,
                    "Re-representation requires a recorded capability block or Attention deferral")
            frames = result["representations"].setdefault(action["project"], [])
            require(len(frames) < 3, "Repeated unsuccessful reframes are bounded; preserve and revisit later")
            require(all(frame["new_frame"].casefold().strip() != action["new_frame"].casefold().strip()
                        for frame in frames), "A paraphrased frame is not a new representation")
            frames.append({**action, "status": "hypothesis", "created_by": invocation,
                           "created_version": state["version"] + 1})

        # ===================================================================
        # NOTEBOOK
        # ===================================================================

        elif kind == "notebook":

            require(
                bool(state.get("charter")),
                "Research charter is not enabled",
            )

            keys(
                action,
                "type id project title summary findings limitations "
                "next_questions evidence reason",
                "Notebook",
            )

            identifier(action["id"])

            require(
                action["project"] in result["projects"],
                "Notebook needs an existing project",
            )

            # Notebook fields are allowed substantially more space than ordinary
            # state because this is where actual research synthesis lives.

            for key, limit in (
                ("title", 120),
                ("summary", 800),
                ("findings", 10000),
                ("limitations", 2400),
                ("next_questions", 1600),
                ("reason", 1000),
            ):
                text(action[key], key, limit)

            references(action["evidence"], result)

            cited = [
                result["evidence"][e]
                for e in action["evidence"]
            ]

            # A research notebook may not use runtime receipts, model-generated
            # text, or arbitrary internal state as if those were external
            # research sources.
            #
            # Every cited source must have been successfully retrieved by the
            # collector.

            require(
                all(
                    evidence.get("actor") == "collector"
                    and evidence.get("scope") == "collected"
                    for evidence in cited
                ),
                "Research notebooks must cite successfully "
                "retrieved external sources",
            )

            # Notebooks are progressive working artifacts. A first revision may
            # begin from one qualifying collected source. Once a notebook is
            # revised, current governance requires corroboration from at least
            # two distinct retrieved source URLs. Historical replay retains the
            # rules that were authoritative when an older event was accepted.
            old = result["notebooks"].get(action["id"])
            notebook_min_sources = 2 if old and not historical else 1
            require(
                len({
                    evidence["source"]
                    for evidence in cited
                }) >= notebook_min_sources,
                "Notebook revisions need at least two distinct retrieved source URLs"
                if notebook_min_sources == 2
                else "Research notebooks need at least one retrieved source URL",
            )

            # New verification semantics apply only to current acceptance.
            #
            # Historical replay should not invalidate old accepted events merely
            # because governance became stricter later.

            if not historical:

                project = result["projects"][action["project"]]
                verification = _verification_evidence(
                    cited,
                    project["domain"],
                    "Notebook evidence",
                    minimum_sources=notebook_min_sources,
                )
                # New verification-grade evidence must at least appear to
                # address the project's actual question. This is a coarse mismatch
                # detector, not semantic entailment: one meaningful shared token is
                # enough to avoid rejecting legitimate terminology differences.
                # Legacy evidence keeps its historical acceptance semantics.
                if verification:
                    project_frame = " ".join(
                        str(project.get(field, ""))
                        for field in ("title", "question", "domain")
                    )
                    _verify_claim_support(
                        project_frame,
                        verification,
                        "Notebook project relevance",
                        minimum_sources=1,
                        minimum_overlap_tokens=1,
                    )

                    # Preserve the established progressive-synthesis contract:
                    # first drafts may remain provisional, while revisions must
                    # materially support their changed findings with the stronger
                    # corroboration rule.
                    if old:
                        _verify_claim_support(
                            action["findings"],
                            verification,
                            "Notebook findings",
                            minimum_sources=notebook_min_sources,
                        )

            # Repository-analysis is a configured topic capability, not a
            # special hardcoded topic identity. When enabled, its notebooks
            # must stay grounded in source-controlled files from that topic's
            # configured repository.
            project_domain = result["projects"][action["project"]]["domain"]
            topic_config = next(
                (topic for topic in state.get("research_topics", []) if topic.get("id") == project_domain),
                None,
            )
            if topic_config and topic_config.get("source_kind") == "repository":
                repository = topic_config["repository"]
                require(
                    all(
                        evidence["source"].startswith(
                            "https://raw.githubusercontent.com/" + repository + "/"
                        )
                        for evidence in cited
                    ),
                    "Repository-analysis notebooks must cite only "
                    "source-controlled files from " + repository,
                )

            if old:

                # A notebook's project identity is stable.
                require(
                    old["project"] == action["project"],
                    "A notebook cannot change projects",
                )

                # Revision must mean actual revision:
                #
                #   changed findings
                #   AND
                #   newly retrieved evidence
                #
                # Merely rephrasing metadata does not count.

                require(
                    action["findings"] != old["findings"]
                    and any(
                        evidence_id not in old["evidence"]
                        for evidence_id in action["evidence"]
                    ),
                    "A revision needs changed findings "
                    "and newly retrieved evidence",
                )

            result["notebooks"][action["id"]] = {
                **action,
                "revision": (
                    old or {}
                ).get("revision", 0) + 1,
                "created_version": (
                    old or {}
                ).get(
                    "created_version",
                    state["version"] + 1,
                ),
                "updated_version": state["version"] + 1,
                "updated_by": invocation,
                "domain": result["projects"][
                    action["project"]
                ]["domain"],
            }

        # ===================================================================
        # BLOG / BOB
        # ===================================================================

        elif kind == "blog":

            require(
                bool(state.get("charter")),
                "Research charter is not enabled",
            )

            # Blog must come LAST.
            #
            # This matters because earlier actions in the proposal may create
            # or revise the research artifacts the blog references.
            #
            # By forcing publication to be last, governance validates the
            # underlying work before validating public interpretation.

            require(
                action is proposal["actions"][-1],
                "A blog action must be last so its research "
                "is already validated",
            )

            expected = (
                "type id project title lede body notebooks evidence reason"
                + (" lens" if "lens" in action else "")
                + (" supersedes" if "supersedes" in action else "")
                + (" reflection_cycle" if "reflection_cycle" in action else "")
            )

            keys(
                action,
                expected,
                "Blog post",
            )

            identifier(action["id"])

            require(
                action["id"] not in result["posts"],
                "Blog post ID already exists",
            )

            # Accepted-state version is the cycle counter.
            #
            # Therefore:
            #
            #     state.version = 9
            #
            # means this proposal would become accepted cycle 10.
            #
            # Rejected attempts do NOT advance this number.
            #
            # That is why Bob's milestone follows accepted cycles rather than
            # raw model invocations.

            declared_reflection_cycle = action.get("reflection_cycle")
            legacy_reflection_cycle = (
                state["version"] + 1
                if historical and (state["version"] + 1) % 10 == 0
                else None
            )
            reflection_cycle = declared_reflection_cycle or legacy_reflection_cycle
            reflection_due = reflection_cycle is not None

            if not historical:
                if required_reflection_cycle is not None:
                    require(
                        declared_reflection_cycle == required_reflection_cycle,
                        f"Bob reflection for accepted wake {required_reflection_cycle} is mandatory and must be the final blog action",
                    )
                else:
                    require(
                        "reflection_cycle" not in action,
                        "reflection_cycle is reserved for a due Bob reflection milestone",
                    )

            require(
                action["project"] in result["projects"]
                or (reflection_due and action["project"] == ""),
                "Blog post needs an existing project; a system-wide Bob reflection may use an empty project",
            )

            for key, limit in (
                ("title", 120),
                ("lede", 500),
                ("body", 6000),
                ("reason", 1000),
            ):
                text(action[key], key, limit)

            # This editorial naming rule governs new proposals, not history.
            # Historical events must always replay under the rules that were
            # authoritative when they were accepted; otherwise a later rule
            # change can make the durable record unreadable and prevent a
            # publication-only export.
            if not historical and reflection_due and result["posts"]:
                require(
                    not re.search(
                        r"\b(?:first|inaugural)\s+(?:public\s+)?reflection\b"
                        r"|\breflection\b[^.!?]{0,48}\b(?:first|inaugural)\b",
                        action["title"],
                        re.IGNORECASE,
                    ),
                    "Later Bob reflections cannot be titled as a first or inaugural reflection",
                )

            require(
                len(action["body"].strip()) >= 300,
                "Blog posts must contain at least 300 characters",
            )
            # Rich milestone requirements govern new proposals only.
            # Historical accepted reflections must replay under the rules that
            # existed when they entered the durable record.
            if reflection_due and not historical:
                require(
                    len(action["body"].strip()) >= 900,
                    "Bob milestone reflections must contain at least 900 characters",
                )
                require(
                    "lens" in action,
                    "Bob milestone reflections require Bob's Lens",
                )

            if "lens" in action:
                text(
                    action["lens"],
                    "Bob's Lens",
                    500,
                )

            # Ordinary Bob posts require 1–3 notebooks.
            #
            # Every tenth accepted cycle is different.
            #
            # The milestone reflection is about:
            #
            #   the journey
            #   the system
            #   Bob's role
            #   longitudinal patterns
            #
            # It may therefore legitimately have zero notebooks.

            require(
                isinstance(action["notebooks"], list)
                and len(set(action["notebooks"]))
                == len(action["notebooks"])
                and (
                    0 <= len(action["notebooks"]) <= 3
                    if reflection_due
                    else 1 <= len(action["notebooks"]) <= 3
                ),
                "Blog posts must reference 1–3 distinct notebooks, "
                "except ten-cycle reflections may use none",
            )

            notebooks = [
                result["notebooks"].get(item)
                for item in action["notebooks"]
            ]

            # Any notebooks that ARE cited must be real and belong to the
            # project the post claims to discuss.

            require(
                all(
                    notebook
                    and notebook["project"] == action["project"]
                    for notebook in notebooks
                ),
                "Blog notebooks must exist and belong "
                "to the related project",
            )

            require(
                isinstance(action["evidence"], list),
                "Blog evidence must be a list",
            )

            if action["evidence"]:
                references(
                    action["evidence"],
                    result,
                )

            cited = [
                result["evidence"][item]
                for item in action["evidence"]
            ]

            # ----------------------------------------------------------------
            # ORDINARY BLOG POST
            # ----------------------------------------------------------------
            #
            # Research-oriented posts require strong traceability.
            #
            # Ten-cycle reflections intentionally bypass these particular
            # research-source requirements because they are reflections on the
            # durable journey rather than ordinary research publications.

            if not reflection_due:

                require(
                    all(
                        item.get("actor") == "collector"
                        and item.get("scope") == "collected"
                        for item in cited
                    ),
                    "Blog research support must use "
                    "collected external evidence",
                )

                require(
                    len({
                        item["source"]
                        for item in cited
                    }) >= PUBLICATION_MIN_SOURCES,
                    "Blog posts need evidence from at least "
                    f"{PUBLICATION_MIN_SOURCES} distinct source URL(s)",
                )

                if not historical:

                    verification = _verification_evidence(
                        cited,
                        result["projects"][
                            action["project"]
                        ]["domain"],
                        "Blog body",
                        minimum_sources=PUBLICATION_MIN_SOURCES,
                    )

                    if verification:
                        _verify_claim_support(
                            action["body"],
                            verification,
                            "Blog body",
                            minimum_sources=PUBLICATION_MIN_SOURCES,
                        )

                # Blog evidence cannot bypass the notebooks.
                #
                # The public post must trace through the research artifact
                # rather than cherry-picking arbitrary evidence directly from
                # the global evidence pool.

                notebook_evidence = {
                    evidence_id
                    for notebook in notebooks
                    for evidence_id in notebook["evidence"]
                }

                require(
                    set(action["evidence"])
                    <= notebook_evidence,
                    "Blog evidence must be traceable through "
                    "its referenced notebooks",
                )

            # ----------------------------------------------------------------
            # CORRECTIONS
            # ----------------------------------------------------------------

            supersedes = action.get("supersedes")

            if supersedes:

                require(
                    supersedes in result["posts"],
                    "A correction must reference an existing blog post",
                )

                # Corrections form a simple forward chain.
                #
                # We do not allow repeatedly superseding an already-superseded
                # post because that would create ambiguous correction history.

                require(
                    not result["posts"][
                        supersedes
                    ].get("superseded_by"),
                    "The earlier blog post is already superseded",
                )

            # Public language receives the editorial calibration checks defined
            # above.

            _blog_language(
                action,
                cited,
                historical=historical,
                prior_post=result["posts"].get(supersedes),
            )

            post = {
                **action,
                "created_by": invocation,
                "created_version": state["version"] + 1,
                "status": "current",
            }

            result["posts"][action["id"]] = post

            # Preserve the old post rather than deleting or rewriting it.
            #
            # Corrections are additive history.

            if supersedes:
                result["posts"][supersedes] = {
                    **result["posts"][supersedes],
                    "status": "superseded",
                    "superseded_by": action["id"],
                }

        # ===================================================================
        # UNKNOWN ACTION
        # ===================================================================

        else:
            # Default-deny.
            #
            # The model does not gain a new capability simply by inventing a
            # new action type.
            #
            # New authority must first be implemented explicitly in governance.

            raise Rejected(
                f"Action is not allowed: {kind!r}"
            )

    if not historical and required_reflection_cycle is not None:
        require(
            any(
                isinstance(action, dict)
                and action.get("type") == "blog"
                and action.get("reflection_cycle") == required_reflection_cycle
                for action in proposal["actions"]
            ),
            f"Bob reflection for accepted wake {required_reflection_cycle} is mandatory before state may advance",
        )

    # =======================================================================
    # ACCEPTANCE
    # =======================================================================
    #
    # Reaching this point means EVERY action survived governance.
    #
    # Only now does the candidate state become a valid next projection.

    result["version"] += 1

    # Every accepted transition produces exactly one journal entry.
    #
    # Notice that rejected proposals never reach this line, which is why the
    # version/journal cycle number measures ACCEPTED cycles rather than raw
    # attempts.

    result["journal"].append(
        {
            "cycle": result["version"],
            "invocation": invocation,
            "title": proposal["title"],
            "summary": proposal["summary"],
        }
    )

    # The caller is responsible for committing this validated projection into
    # the durable event/state machinery.
    #
    # Governance itself remains a pure transition function.

    return result
