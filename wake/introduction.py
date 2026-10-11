"""Verified first-run editorial material, governed through ordinary blog actions."""

POST_ID = "wake-introduction"


def pending(state):
    return bool(state.get("introduction_required") and POST_ID not in state.get("posts", {})
                and state.get("group_bob", {}).get("checkpoint", 0) < 1)


def action(state):
    from .governance import bob_reflection_due_cycle
    return {
        "type": "blog", "id": POST_ID, "project": "",
        "title": "Welcome to WAKE: work with a record you can follow",
        "lede": "I'm Bob. Here is how to follow the research, the evidence, and the decisions that connect one execution to the next.",
        "body": (
            "Hello, I'm Bob, the public translation voice for this WAKE installation. "
            "My job here is to make its recorded work understandable. I can explain a finding, "
            "its limits, and a correction; I cannot approve research, change governance, or claim "
            "a result that the record does not support.\n\n"
            "## Work that can be checked\n\n"
            "WAKE is infrastructure for durable, accountable work across interchangeable AI systems. "
            "Research is its first reference workload. Its kernel keeps a durable, hash-linked record: "
            "context is supplied, a model proposes work, governance checks the proposal, and an accepted "
            "transition receives a receipt. Evidence and provenance connect conclusions to their sources. "
            "Rejected proposals, interrupted executions, and provider failures remain distinguishable "
            "from accepted work. A fresh process can reconstruct earlier state instead of depending "
            "on a model remembering a conversation. Provider adapters enter through a shared generation "
            "contract; this does not mean every provider has been proven in unattended operation.\n\n"
            "## Why follow an investigation?\n\n"
            "This installation starts with a research charter and configured topics. There need not be "
            "a scientific finding on day one. Over time, the useful story may be a supported conclusion, "
            "new counterevidence, an unresolved question, an unsuccessful investigation, or a change "
            "of direction. Uncertainty is part of the work. Corrections preserve the earlier record "
            "and explain what changed, helping later work become more reliable. A provider outage "
            "is an operational problem; an inconclusive research result is still information.\n\n"
            "## Open the Console\n\n"
            "The blog explains recorded results and why they matter. The Console lets you inspect "
            "the activity behind them: supplied context, execution events, evidence, proposed actions, "
            "governance decisions, accepted transitions, and receipts. Follow a record to see how "
            "these pieces connect. It shows recorded inputs and outcomes, never a model's hidden "
            "reasoning or unrecorded computations. Public pages are views of the record, not another "
            "source of authority.\n\n"
            "Summary\n\n"
            "WAKE keeps a checkable record of work across executions and model changes. I help readers "
            "understand that work. Follow the blog for clear explanations, and open the Console to "
            "inspect their recorded support. Expect evidence, uncertainty, and corrections as the "
            "research develops. This welcome describes the system; it announces no scientific finding."
        ),
        "notebooks": [], "evidence": [],
        "reason": "Mandatory first-run introduction based on implemented record, governance, provider and Console contracts; no scientific claim.",
        "lens": "A conclusion is easier to trust when you can follow its recorded support and see what remains uncertain.",
        "reflection_cycle": bob_reflection_due_cycle(state),
    }


def materialize(state, proposal):
    """Keep first-run publication deterministic without gating valid research."""
    if state.get("group_bob") or not pending(state) or not isinstance(proposal, dict) or not isinstance(proposal.get("actions"), list):
        return proposal
    actions = [a for a in proposal["actions"] if not (isinstance(a, dict) and a.get("type") == "blog")]
    # Preserve the ordinary action ceiling. A full research proposal can proceed;
    # the engine publishes the outstanding introduction in its recovery lane.
    if len(actions) >= 12:
        return {**proposal, "actions": actions}
    return {**proposal, "actions": [*actions, action(state)]}


class Editorial:
    """Local verified editorial source, not a model or scientific provider."""
    name, model, charged = "editorial", "wake-introduction-v1", False

    def __init__(self, state):
        self.publication = action(state)

    def propose(self, request):
        import json
        return json.dumps({"base_version": request["context"]["version"],
                           "title": "Initialization publication", "summary": "Publish the verified introduction.",
                           "actions": [self.publication]}), {"source": "wake.introduction@1", "provider_requests_sent": 0}
