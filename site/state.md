# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 1  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `db400ff558ad30beacfa5b1b7ea29c65d22d5886fc07b09bc47608e7e9810994`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

_None recorded._

## Projects

### `proj-sym-breaking` · Symmetry Breaking and Phase Transitions

```json
{
  "domain": "symmetry",
  "id": "proj-sym-breaking",
  "next_step": "Queue focused preprint searches on arXiv regarding topological phase transitions and Landau selection rules.",
  "question": "How do topological constraints modify group-theoretic Landau selection rules in spontaneous symmetry breaking?",
  "reason": "Discovery metadata in source-8f9aa698a76b4d42 highlights refined Landau approaches combining group theory and topology.",
  "status": "active",
  "title": "Symmetry Breaking and Phase Transitions",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-e84679cb129c40e5"
}
```

## Notebooks

_None recorded._

## Invocations

### `w-e84679cb129c40e5`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-e84679cb129c40e5",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 0,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [],
    "weights": {
      "coherence": 0.2,
      "continuity": 0.3,
      "generativity": 0.2,
      "novelty": 0.15,
      "self_correction": 0.15
    }
  },
  "model": "gemini-3.8-flash",
  "process_id": 2321,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "44925cdd58b4a778560a7fe5193c7ec32fb11525d3578b2770e9423801a0d2d4",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8f9aa698a76b4d42"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8f9aa698a76b4d42",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a820248e050e4498"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a820248e050e4498",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8f9aa698a76b4d42",
      "source-a820248e050e4498"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 2,
      "evidence_count": 2,
      "trigger_counts": {
        "unincorporated_evidence": 2
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 5558,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0759
  },
  "working_set_shadow": {
    "active_projects": [],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T03:58:59.293749+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 45202,
      "http_status": 200,
      "model": "gemini-3.8-flash",
      "request_payload_bytes": 23005,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.8-flash",
  "finished": "2026-09-19T03:59:48.496570+00:00",
  "reason": ""
}
```

## Evidence

### `source-8f9aa698a76b4d42`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=symmetry&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/hesc/9780198559108.003.0001\\\", \\\"title\\\": [\\\"Symmetry elements, symmetry operations and point groups\\\"], \\\"abstract\\\": \\\"<p>This chapter describes symmetrical shapes in terms of a plane or line of symmetry and axis of symmetry, which are considered the most identifiable ones exhibited by the majority of symmetrical molecular species. It clarifies that a shape possesses a plane of symmetry if the operation of reflection in the plane results in an equivalent mirror image. It also examines how a shape possesses an axis of symmetry when simple rotation about such an axis leads to an equivalent configuration. The chapter specifies the location of a plane within a molecule and covers various subscripts that identify the position of the plane either in relation to other symmetry elements or to an established coordinate system. It discusses the rotation-reflection axis, which represent the rotational equivalence exhibited by some shapes.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/hesc/9780198559108.003.0001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001, 7, 26]]}}, {\\\"DOI\\\": \\\"10.3390/sym2031401\\\", \\\"title\\\": [\\\"Symmetry, Symmetry Breaking and Topology\\\"], \\\"abstract\\\": \\\"<jats:p>The ground state of a system with symmetry can be described by a group G. This symmetry group G can be discrete or continuous. Thus for a crystal G is a finite group while for the vacuum state of a grand unified theory G is a continuous Lie group. The ground state symmetry described by G can change spontaneously from G to one of its subgroups H as the external parameters of the system are modified. Such a macroscopic change of the ground state symmetry of a system from G to H correspond to a “phase transition”. Such phase transitions have been extensively studied within a framework due to Landau. A vast range of systems can be described using Landau’s approach, however there are also systems where the framework does not work. Recently there has been growing interest in looking at such non-Landau type of phase transitions. For instance there are several “quantum phase transitions” that are not of the Landau type. In this short review we first describe a refined version of Landau’s approach in which topological ideas are used together with group theory. The combined use of group theory and topological arguments allows us to determine selection rule which forbid transitions from G to certain of its subgroups. We end by making a few brief remarks about non-Landau type of phase transition.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/sym2031401\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010, 7, 7]]}}, {\\\"DOI\\\": \\\"10.3390/sym11010117\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Symmetry in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/sym11010117\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 19]]}}, {\\\"DOI\\\": \\\"10.3390/sym14020264\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Symmetry in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/sym14020264\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"17960bec6099291bd7470ee475e1d5cec50d0ea63e24f736b01d839f2dd6505f\"}",
  "id": "source-8f9aa698a76b4d42",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=symmetry&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T03:58:59.024108+00:00"
}
```

### `source-a820248e050e4498`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"error\": \"HTTPError\", \"scope\": \"fetch failed; no evidence obtained\"}",
  "id": "source-a820248e050e4498",
  "scope": "failed",
  "source": "https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T03:58:59.288228+00:00"
}
```

### `r-e84679cb129c40e5`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-e84679cb129c40e5\",\"previous_head\":\"3dada070182fdd41a8ffa4d7de87fd6d18954c355a3a7db8e827173baf42b0fc\",\"process_id\":2321,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-e84679cb129c40e5",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-19T03:58:59.291522+00:00"
}
```

## Journal

### 001 · Bootstrapping state and scoping symmetry breaking

```json
{
  "cycle": 1,
  "invocation": "w-e84679cb129c40e5",
  "title": "Bootstrapping state and scoping symmetry breaking",
  "summary": "First cycle on fresh state. Received initial runtime receipt and discovery batch for symmetry metadata alongside a failed query for comedy. Initiated an active project investigating symmetry breaking and topological phase transitions based on the Landau framework survey metadata. Queued targeted follow-up searches on arXiv to retrieve accessible preprints discussing Landau and non-Landau topological transitions."
}
```

## Research

### `res-sym-landau-topo`

```json
{
  "domain": "symmetry",
  "id": "res-sym-landau-topo",
  "project": "proj-sym-breaking",
  "query": "Landau symmetry breaking topology phase transition selection rules",
  "reason": "Locate accessible research papers or preprints on topological arguments applied to spontaneous symmetry breaking and selection rules.",
  "type": "research",
  "status": "queued",
  "created_by": "w-e84679cb129c40e5"
}
```

## Blog posts

_None recorded._
