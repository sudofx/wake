# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 1  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `ce8e3db377b699d2a3b11c117bdaed0ee5ce35bd0e089c76e334734db25e6a66`

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

### `w-8af03f63baaa498f`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-8af03f63baaa498f",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 1,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 0.5,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "proj-coll-intel",
        "score": 0.75,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 1
        },
        "title": "Mechanisms of Collective Intelligence"
      }
    ],
    "weights": {
      "coherence": 0.2,
      "continuity": 0.3,
      "generativity": 0.2,
      "novelty": 0.15,
      "self_correction": 0.15
    }
  },
  "model": "gemini-3.8-flash",
  "process_id": 2256,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "aad37e4cd5022be3e59e76e83d06f27de2a3d099de3406893a99a4d3ceb19124",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "commit-review-ci-results",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
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
      },
      {
        "evidence": [
          "source-f19497248e1047b4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f19497248e1047b4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-e12c7e8fa8db4893"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-e12c7e8fa8db4893",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-94c420b0056e48d9",
      "source-deccd24b2ae64ebd",
      "source-f19497248e1047b4",
      "source-e12c7e8fa8db4893"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 5,
      "evidence_count": 4,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 4
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 12861,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 5,
    "retrieval_evidence_count": 4,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 4
    },
    "working_set_chars": 968,
    "working_to_delivered_ratio": 0.0753
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "proj-coll-intel",
        "next_step": "Queue search for foundational reviews on collective intelligence metrics.",
        "question": "What are the core mathematical and functional mechanisms distinguishing aggregate intelligence from individual behavior?",
        "title": "Mechanisms of Collective Intelligence"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "commit-review-ci-results",
        "reason": "To synthesize incoming evidence about collective intelligence frameworks.",
        "task": "Review collected research results for collective intelligence metrics and organize into a structured notebook."
      }
    ],
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
  "status": "rejected",
  "time": "2026-09-18T21:34:47.834258+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 2539,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 31724,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 993,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 31724,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 7604,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 31724,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-18T21:35:08.782783+00:00",
  "reason": "Evidence reference does not exist"
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

### `source-f19497248e1047b4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence+quantitative+metrics&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1162/qss_a_00280\\\", \\\"title\\\": [\\\"The rise of responsible metrics as a professional reform movement: A collective action frames account\\\"], \\\"abstract\\\": \\\"<jats:title>Abstract</jats:title>\\\\n                  <jats:p>Recent years have seen a rise in awareness around “responsible metrics” and calls for research assessment reforms internationally. Yet within the field of quantitative science studies and in research policy contexts, concerns about the limitations of evaluative bibliometrics are almost as old as the tools themselves. Given that many of the concerns articulated in recent reform movements go back decades, why has momentum for change grown only in the past 10 years? In this paper, we draw on analytical insights from the sociology of social movements on collective action frames to chart the emergence, development, and expansion of “responsible metrics” as a professional reform movement. Through reviewing important texts that have shaped reform efforts, we argue that hitherto, three framings have underpinned the responsible metrics reform agenda: the metrics skepticism framing, the professional-expert framing, and the reflexivity framing. We suggest that although these three framings have coexisted within the responsible metrics movement to date, cohabitation between these framings may not last indefinitely, especially as the responsible metrics movement extends into wider research assessment reform movements.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1162/qss_a_00280\\\", \\\"published\\\": {\\\"date-parts\\\": [[2023]]}}, {\\\"DOI\\\": \\\"10.1145/1865909.1865963\\\", \\\"title\\\": [\\\"Collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1145/1865909.1865963\\\", \\\"published\\\": {\\\"date-parts\\\": [[2009, 9, 21]]}}, {\\\"DOI\\\": \\\"10.1007/978-3-030-30241-2_58\\\", \\\"title\\\": [\\\"Benchmarking Collective Perception: New Task Difficulty Metrics for Collective Decision-Making\\\"], \\\"URL\\\": \\\"https://doi.org/10.1007/978-3-030-30241-2_58\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019]]}}, {\\\"DOI\\\": \\\"10.1177/26339137221114176\\\", \\\"title\\\": [\\\"New books on collective intelligence: Growing the field: Interesting new books on collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137221114176\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 8]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"d1c1a0d6e3a9c1580ec9f831296e3b4a852c1e94aaecdd99356c304c7825b630\"}",
  "id": "source-f19497248e1047b4",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence+quantitative+metrics&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T21:34:47.275557+00:00"
}
```

### `source-e12c7e8fa8db4893`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1177/26339137221114176\\\", \\\"title\\\": [\\\"New books on collective intelligence: Growing the field: Interesting new books on collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137221114176\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 8]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251360003\\\", \\\"title\\\": [\\\"Opinion for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>This short piece shares thoughts on some recent research and books related to collective intelligence - on topics ranging from democracy and institutions to LLMs and animals.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251360003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 7]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251328909\\\", \\\"title\\\": [\\\"AI for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>AI has emerged as a transformative force in society, reshaping economies, work, and everyday life. We argue that AI can not only improve short-term productivity but can also enhance a group’s collective intelligence. Specifically, AI can be employed to enhance three elements of collective intelligence: collective memory, collective attention, and collective reasoning. This editorial reviews key emerging work in the area to suggest ways in which AI can support the socio-cognitive architecture of collective intelligence. We will then briefly introduce the articles in the “AI for Collective Intelligence” special issue.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251328909\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4]]}}, {\\\"DOI\\\": \\\"10.1177/26339137241285900\\\", \\\"title\\\": [\\\"Book Review: A few recent books on Collective Intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137241285900\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 3, 3]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"58b2fc75bdb9c736cb0720e6df0e4beee2c846e78e9ce07f300ec86caa615266\"}",
  "id": "source-e12c7e8fa8db4893",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T21:34:47.823336+00:00"
}
```

### `r-8af03f63baaa498f`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[\"commit-review-ci-results\"],\"invocation\":\"w-8af03f63baaa498f\",\"previous_head\":\"137c00df897f68b41747e5079e46c05f5721a73f342769059d46aeaec6d749a9\",\"process_id\":2256,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-8af03f63baaa498f",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-18T21:34:47.830413+00:00"
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
  "status": "collected",
  "created_by": "w-f4dcae3f11f94198",
  "evidence": "source-f19497248e1047b4"
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
