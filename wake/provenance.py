# =============================================================================
# PROVENANCE — the relationship layer. The map is built from explicit IDs, citations, projects, invocations and events. It should visualize recorded relationships rather than infer a more compelling story than the record supports.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# Read this file as part of a chain of custody.  WAKE✳︎ deliberately separates
# disposable cognition from durable authority.  Comments therefore explain not
# only what a function does, but why its boundary exists and what a refactor must
# not accidentally collapse.  Prefer explicit receipts, deterministic state
# transitions, and replayable facts over convenient hidden behavior.
# =============================================================================

"""Static provenance derived only from replayed events and explicit durable IDs."""

import json
from copy import deepcopy
from urllib.parse import unquote, urlsplit

from .store import empty, reduce_event

COLLECTIONS = {"belief": "beliefs", "commitment": "commitments", "project": "projects",
               "notebook": "notebooks", "research": "research", "blog": "posts", "evidence": "evidence"}
ACTIONS = {"belief": "belief", "commit": "commitment", "resolve": "commitment",
           "project": "project", "notebook": "notebook", "research": "research", "blog": "blog"}


# ---------------------------------------------------------------------------
# STEP: build_map
#
# This step exists as an explicit seam so its behavior can be
# inspected, tested, and replaced without giving a model hidden authority.
# Inputs should already belong to the layer named above; outputs remain data
# until the next boundary validates or records them. Callers may rely on this contract.


# ---------------------------------------------------------------------------


def build_map(state, events, head):
    nodes, edges, journals, blogs = {}, {}, [], []
    by_invocation = {j["invocation"]: f"journal:{j['invocation']}" for j in state["journal"]}

    # ---------------------------------------------------------------------------
    # STEP: node
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def node(key, kind, detail, title=None):
        if key not in nodes:
            summary = detail.get("statement") or detail.get("task") or ""
            if len(summary) > 110:
                summary = summary[:110] + "…"
            nodes[key] = {"id": key, "kind": kind,
                          "title": title or detail.get("title") or summary or detail.get("id", key),
                          "detail": deepcopy(detail)}
        return key

    # ---------------------------------------------------------------------------
    # STEP: edge
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def edge(source, target, relation, record):
        if source in nodes and target in nodes:
            key = (source, target, relation)
            edges[key] = {"source": source, "target": target, "relation": relation, "record": record}

    for iid, item in state["invocations"].items():
        # Full prompts and working sets remain in the raw export, outside this compact payload.
        detail = {k: v for k, v in item.items() if k not in ("working_set_shadow", "retrieval_shadow")}
        retrieval = item.get("retrieval_shadow", {})
        if retrieval:
            detail["retrieval_metrics"] = {k: v for k, v in retrieval.items()
                                           if k in ("mode", "metrics", "trigger_counts", "candidate_count", "evidence_count")}
        node(f"invocation:{iid}", "invocation", detail, iid)
    for j in state["journal"]:
        iid = j["invocation"]
        invocation = state["invocations"].get(iid, {})
        key = node(by_invocation[iid], "journal", {**j, "time": invocation.get("time"),
                   "provider": invocation.get("provider"), "model": invocation.get("successful_model") or invocation.get("model"),
                   "status": invocation.get("status"), "changes": []}, f"Cycle {j['cycle']} · {j['title']}")
        nodes[key]["expands"] = []
        journals.append(key)
        edge(key, f"invocation:{iid}", "invocation", f"journal.invocation={iid}")
    for pid, post in state.get("posts", {}).items():
        key = node(f"blog:{pid}", "blog", post)
        blogs.append(key)
        jid = by_invocation.get(post.get("created_by"))
        if jid:
            edge(key, jid, "originating wake", f"posts.{pid}.created_by")
    for pid, post in state.get("posts", {}).items():
        for field in ("supersedes", "superseded_by"):
            if post.get(field):
                edge(f"blog:{pid}", f"blog:{post[field]}", field.replace("_", " "), f"posts.{pid}.{field}")

    # ---------------------------------------------------------------------------
    # STEP: artifact
    #
    # This step exists as an explicit seam so its behavior can be
    # inspected, tested, and replaced without giving a model hidden authority.
    # Inputs should already belong to the layer named above; outputs remain data
    # until the next boundary validates or records them. Callers may rely on this contract.
    # ---------------------------------------------------------------------------

    def artifact(kind, identifier, snapshot, cycle, expanded):
        item = snapshot.get(COLLECTIONS[kind], {}).get(identifier)
        if item is None:
            return None
        key = f"{kind}:{identifier}" + ("" if kind in ("blog", "evidence") else f"@{cycle}")
        if key in expanded:
            return key
        expanded.add(key)
        detail = deepcopy(item)
        if kind not in ("blog", "evidence"):
            detail["as_of_cycle"] = cycle
        if kind == "evidence":
            try:
                parsed = json.loads(detail.get("content", ""))
            except (ValueError, TypeError):
                parsed = None
            if isinstance(parsed, dict):
                detail.pop("content", None)
                detail["collected_content"] = parsed
            if item.get("source") == "runtime:continuity" and isinstance(parsed, dict):
                node(key, kind, detail, "Continuity receipt")
                edge(f"invocation:{parsed.get('invocation')}", key, "delivery receipt", f"evidence.{identifier}.content.invocation")
        title = None
        if kind == "evidence" and item.get("source") != "runtime:continuity":
            source = urlsplit(item.get("source", ""))
            excerpt = detail.get("collected_content", {}).get("excerpt", "")
            first_line = excerpt.splitlines()[0] if excerpt else ""
            title = (first_line[7:] if first_line.startswith("title: ") else
                     (source.hostname or "Evidence") + " · " + unquote(source.path.strip("/")).replace("-", " "))
        elif kind == "research":
            title = item.get("query")
        node(key, kind, detail, title)
        for field, target_kind in (("project", "project"), ("notebooks", "notebook"), ("evidence", "evidence")):
            refs = item.get(field, [])
            if isinstance(refs, str):
                refs = [refs]
            for ref in refs:
                target = artifact(target_kind, ref, snapshot, cycle, expanded)
                if target:
                    edge(key, target, field, f"{COLLECTIONS[kind]}.{identifier}.{field} at cycle {cycle}")
        for field in ("updated_by", "created_by", "resolved_by"):
            if item.get(field) in state["invocations"]:
                edge(key, f"invocation:{item[field]}", field.replace("_", " "), f"{COLLECTIONS[kind]}.{identifier}.{field} at cycle {cycle}")
        return key

    starts = {e["payload"]["id"]: e for e in events if e["kind"] == "invocation_started"}
    replayed = empty()
    for event in events:
        before = replayed
        replayed = reduce_event(deepcopy(replayed), event, historical=True)
        if event["kind"] != "accepted":
            continue
        p = event["payload"]
        jid = by_invocation.get(p["id"])
        if not jid:
            continue
        expanded = {f"invocation:{p['id']}"}
        cycle = replayed["version"]
        for action in p["proposal"]["actions"]:
            kind = ACTIONS.get(action.get("type"))
            if not kind:
                continue
            aid = action["id"]
            key = artifact(kind, aid, replayed, cycle, expanded)
            if key:
                change = ("resolved" if action["type"] == "resolve" else "retracted" if action.get("status") == "retracted"
                          else "revised" if aid in before.get(COLLECTIONS[kind], {}) else "created")
                record = f"event {event['seq']} · {event['hash']}"
                edge(jid, key, change, record)
                if kind == "blog" and action.get("supersedes"):
                    edge(jid, f"blog:{action['supersedes']}", "superseded", record)
                nodes[jid]["detail"]["changes"].append(f"{change.capitalize()} {kind}: {aid}")
        # Receipt IDs come from the recorded request, never an ID naming convention.
        start = starts.get(p["id"])
        if start:
            receipt = start["payload"].get("request", {}).get("context", {}).get("receipt")
            if receipt:
                artifact("evidence", receipt, replayed, cycle, expanded)
        editorial = p.get("editorial")
        if editorial:
            key = node(f"editorial:{p['id']}", "editorial", editorial, "Blog withheld" if editorial["status"] == "withheld" else "Editorial decision")
            expanded.add(key)
            edge(jid, key, "editorial decision", f"event {event['seq']} · {event['hash']}")
        elif any(a.get("type") == "blog" for a in p["proposal"]["actions"]):
            key = node(f"editorial:{p['id']}", "editorial", {"status": "accepted", "reason": "Blog action accepted by governance."}, "Blog accepted")
            expanded.add(key)
            edge(jid, key, "editorial decision", f"event {event['seq']} · {event['hash']}")
        nodes[jid]["expands"] = sorted(expanded)
        nodes[jid]["detail"]["exact_record"] = f"Event {event['seq']} · {event['hash']}"
    # Legacy posts without an accepted-event link remain visible; their explicit
    # references use the current export and are labelled accordingly.
    for pid, post in state.get("posts", {}).items():
        if not any(e["source"] == f"blog:{pid}" and e["relation"] == "notebooks" for e in edges.values()):
            artifact("blog", pid, state, state["version"], set())
    return {"journals": journals, "blogs": blogs, "nodes": list(nodes.values()), "edges": list(edges.values()),
            "meta": {"head": head, "version": state["version"], "schema_version": 1,
                     "principle": "The record is auditable. The record is not thereby proven correct.",
                     "shadow_note": "Character ratios are observational instrumentation, not token savings or proof of behavioral equivalence."}}
