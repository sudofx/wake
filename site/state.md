# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 1  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `30c89bd974fcd0e41b27673a1a75bc8d711ce61f1f9b949d7beb71a920615fa4`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

### `commit-review-ci-results`

```json
{
  "due_cycle": 2,
  "id": "commit-review-ci-results",
  "reason": "To synthesize incoming evidence about collective intelligence frameworks.",
  "task": "Review collected research results for collective intelligence metrics and organize into a structured notebook.",
  "type": "commit",
  "status": "open",
  "created_by": "w-f4dcae3f11f94198",
  "created_version": 1
}
```

## Projects

### `proj-coll-intel` · Mechanisms of Collective Intelligence

```json
{
  "domain": "collective_intelligence",
  "id": "proj-coll-intel",
  "next_step": "Queue search for foundational reviews on collective intelligence metrics.",
  "question": "What are the core mathematical and functional mechanisms distinguishing aggregate intelligence from individual behavior?",
  "reason": "Initiating the project to systematically analyze definitions and quantitative measures of collective intelligence.",
  "status": "active",
  "title": "Mechanisms of Collective Intelligence",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-f4dcae3f11f94198"
}
```

## Notebooks

_None recorded._

## Invocations

### `w-f4dcae3f11f94198`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-f4dcae3f11f94198",
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
  "process_id": 2046,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "4191863dde54ee91ae5d8d5a1968fa1e4da663799ac42d32da0ff1bdc0cf749b",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-94c420b0056e48d9"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-94c420b0056e48d9",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-deccd24b2ae64ebd"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-deccd24b2ae64ebd",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-94c420b0056e48d9",
      "source-deccd24b2ae64ebd"
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
    "delivered_context_chars": 4805,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0878
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
  "time": "2026-09-18T21:33:38.752644+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 2109,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 22592,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 7223,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 22592,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-18T21:33:55.127362+00:00",
  "reason": ""
}
```

## Evidence

### `source-94c420b0056e48d9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3246af5a37381e510cf45a74e41f32b87354ebc0a2d042014a5004d7667a5e37\"}",
  "id": "source-94c420b0056e48d9",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-18T21:33:38.238260+00:00"
}
```

### `source-deccd24b2ae64ebd`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"error\": \"HTTPError\", \"scope\": \"fetch failed; no evidence obtained\"}",
  "id": "source-deccd24b2ae64ebd",
  "scope": "failed",
  "source": "https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-18T21:33:38.669704+00:00"
}
```

### `r-f4dcae3f11f94198`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-f4dcae3f11f94198\",\"previous_head\":\"fd402f0b2478597724f710872bed96dccb32cb846acd240a9202bb44f9a34a7b\",\"process_id\":2046,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-f4dcae3f11f94198",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-18T21:33:38.743550+00:00"
}
```

## Journal

### 001 · Establishing Durable Context and Initial Collective Intelligence Project

```json
{
  "cycle": 1,
  "invocation": "w-f4dcae3f11f94198",
  "title": "Establishing Durable Context and Initial Collective Intelligence Project",
  "summary": "We are initiating WAKE✳︎'s research operations under the continuity focus. An initial project has been registered to investigate collective intelligence mechanisms, and targeted searches have been queued to establish our baseline literature."
}
```

## Research

### `search-coll-intel-1`

```json
{
  "domain": "collective_intelligence",
  "id": "search-coll-intel-1",
  "project": "proj-coll-intel",
  "query": "collective intelligence quantitative metrics",
  "reason": "Find papers defining measurable parameters of collective problem-solving.",
  "type": "research",
  "status": "queued",
  "created_by": "w-f4dcae3f11f94198"
}
```

### `search-arxiv-coll-intel`

```json
{
  "domain": "collective_intelligence",
  "id": "search-arxiv-coll-intel",
  "project": "proj-coll-intel",
  "query": "collective intelligence decision making",
  "reason": "Search arXiv abstracts for mathematical models of group decision structures.",
  "type": "research",
  "status": "queued",
  "created_by": "w-f4dcae3f11f94198"
}
```

## Blog posts

_None recorded._
