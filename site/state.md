# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 1  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `811080f6868787a1cab29b8342a0a76a92baccad6c429f7c65230837a75e073a`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

### `bel-ci-three-elements`

```json
{
  "confidence": 0.7,
  "evidence": [
    "source-79489f1f420142f8"
  ],
  "id": "bel-ci-three-elements",
  "reason": "The editorial metadata for 'AI for collective intelligence' explicitly outlines these three socio-cognitive dimensions as areas where AI can enhance group capabilities.",
  "statement": "Emerging frameworks partition AI's contribution to collective intelligence into collective memory, collective attention, and collective reasoning.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-3cc9a9889469416a",
  "updated_version": 1
}
```

## Commitments

_None recorded._

## Projects

### `proj-collective-intel-ai` · AI in Collective Intelligence Architectures

```json
{
  "domain": "collective_intelligence",
  "id": "proj-collective-intel-ai",
  "next_step": "Acquire a second distinct research source to analyze structural changes in collective memory and reasoning.",
  "question": "How does artificial intelligence alter or enhance socio-cognitive collective intelligence structures, specifically collective memory, attention, and reasoning?",
  "reason": "Initial source metadata indicates emerging frameworks defining AI's role in collective cognitive dimensions, requiring deeper investigation.",
  "status": "active",
  "title": "AI in Collective Intelligence Architectures",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-3cc9a9889469416a"
}
```

## Notebooks

_None recorded._

## Invocations

### `w-3cc9a9889469416a`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-3cc9a9889469416a",
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
  "process_id": 2260,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "cc72d14461d79edd9d7e2dda41040c4dabd421c00393982f7ac6d2c84add0ff0",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-e97cad0649244a6e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-e97cad0649244a6e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-79489f1f420142f8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-79489f1f420142f8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-e97cad0649244a6e",
      "source-79489f1f420142f8"
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
    "delivered_context_chars": 6852,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0616
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
  "time": "2026-09-19T00:30:41.153915+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 2115,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 24957,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 10535,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 24957,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-19T00:31:00.070257+00:00",
  "reason": ""
}
```

## Evidence

### `source-e97cad0649244a6e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"01e4b61dbe0014f7f330aa0f9e58a838932fc12afb21098a928acb172946dd2e\"}",
  "id": "source-e97cad0649244a6e",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T00:30:40.574459+00:00"
}
```

### `source-79489f1f420142f8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1177/26339137221114176\\\", \\\"title\\\": [\\\"New books on collective intelligence: Growing the field: Interesting new books on collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137221114176\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 8]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251360003\\\", \\\"title\\\": [\\\"Opinion for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>This short piece shares thoughts on some recent research and books related to collective intelligence - on topics ranging from democracy and institutions to LLMs and animals.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251360003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 7]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251328909\\\", \\\"title\\\": [\\\"AI for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>AI has emerged as a transformative force in society, reshaping economies, work, and everyday life. We argue that AI can not only improve short-term productivity but can also enhance a group’s collective intelligence. Specifically, AI can be employed to enhance three elements of collective intelligence: collective memory, collective attention, and collective reasoning. This editorial reviews key emerging work in the area to suggest ways in which AI can support the socio-cognitive architecture of collective intelligence. We will then briefly introduce the articles in the “AI for Collective Intelligence” special issue.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251328909\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4]]}}, {\\\"DOI\\\": \\\"10.1177/26339137241285900\\\", \\\"title\\\": [\\\"Book Review: A few recent books on Collective Intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137241285900\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 3, 3]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"c76b7da9235c42a5dfecdfdd1729b1a02e11631d14b89ff045bcd3a8ec431856\"}",
  "id": "source-79489f1f420142f8",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T00:30:41.147814+00:00"
}
```

### `r-3cc9a9889469416a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-3cc9a9889469416a\",\"previous_head\":\"968bee8a6cb0b5fc9facaabc86179c61fea5a273710de364935868d8493ff3c0\",\"process_id\":2260,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-3cc9a9889469416a",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-19T00:30:41.151565+00:00"
}
```

## Journal

### 001 · Initiating Socio-Cognitive Collective Intelligence Project

```json
{
  "cycle": 1,
  "invocation": "w-3cc9a9889469416a",
  "title": "Initiating Socio-Cognitive Collective Intelligence Project",
  "summary": "Beginning WAKE✳︎ research by establishing a project focused on the interaction of artificial intelligence with collective intelligence architectures. We observe initial metadata regarding AI's role in collective memory, attention, and reasoning, and are queuing targeted queries to gather sufficient distinct peer-reviewed sources for a comprehensive notebook."
}
```

## Research

### `res-ci-socio-cognitive`

```json
{
  "domain": "collective_intelligence",
  "id": "res-ci-socio-cognitive",
  "project": "proj-collective-intel-ai",
  "query": "\"collective intelligence\" AND \"socio-cognitive\" AND \"AI\"",
  "reason": "To secure a second distinct source detailing the socio-cognitive frameworks of collective intelligence when integrated with artificial agents.",
  "type": "research",
  "status": "queued",
  "created_by": "w-3cc9a9889469416a"
}
```

## Blog posts

_None recorded._
