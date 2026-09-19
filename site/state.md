# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 1  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `5f98fc594ab00b7887f6e97b0eb2b60f9e96cc2bbfafb45dcce8e96451f13510`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

_None recorded._

## Projects

### `ci-ai-support` · AI in Collective Intelligence

```json
{
  "domain": "collective_intelligence",
  "id": "ci-ai-support",
  "next_step": "Synthesize literature on socio-cognitive architectures and AI-supported group functions.",
  "question": "How can AI technologies concretely enhance collective memory, attention, and reasoning in group environments?",
  "reason": "Existing evidence explicitly frames AI's role through these three specific cognitive elements, providing a testable framework for research.",
  "status": "active",
  "title": "AI in Collective Intelligence",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-e89bafef43944408"
}
```

## Notebooks

_None recorded._

## Invocations

### `w-e89bafef43944408`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-e89bafef43944408",
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
  "process_id": 2267,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "f3be943c023f040cb8943a87a59e8c92655ecf3448e0ff7420420394b223ea61",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-963ce743d2b14c3c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-963ce743d2b14c3c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3336970370754763"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3336970370754763",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-963ce743d2b14c3c",
      "source-3336970370754763"
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
    "delivered_context_chars": 7008,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0602
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
  "time": "2026-09-19T15:06:46.359724+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 623,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 25268,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1076,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 25268,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 6910,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 25268,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T15:07:02.913920+00:00",
  "reason": ""
}
```

## Evidence

### `source-963ce743d2b14c3c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"e7bdf93d705454efbf3b4089fa52f3821120d38955fe7a060ddd0e5b7f4f6bb8\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-963ce743d2b14c3c",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T15:06:44.721571+00:00"
}
```

### `source-3336970370754763`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1177/26339137221114176\\\", \\\"title\\\": [\\\"New books on collective intelligence: Growing the field: Interesting new books on collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137221114176\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 8]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251360003\\\", \\\"title\\\": [\\\"Opinion for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>This short piece shares thoughts on some recent research and books related to collective intelligence - on topics ranging from democracy and institutions to LLMs and animals.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251360003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 7]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251328909\\\", \\\"title\\\": [\\\"AI for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>AI has emerged as a transformative force in society, reshaping economies, work, and everyday life. We argue that AI can not only improve short-term productivity but can also enhance a group’s collective intelligence. Specifically, AI can be employed to enhance three elements of collective intelligence: collective memory, collective attention, and collective reasoning. This editorial reviews key emerging work in the area to suggest ways in which AI can support the socio-cognitive architecture of collective intelligence. We will then briefly introduce the articles in the “AI for Collective Intelligence” special issue.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251328909\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4]]}}, {\\\"DOI\\\": \\\"10.1177/26339137241285900\\\", \\\"title\\\": [\\\"Book Review: A few recent books on Collective Intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137241285900\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 3, 3]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"6855af246f009f27575c937965a71b78bcdb0187904829d8a3e8824fe251ad27\", \"verification_required\": true, \"topic_domain\": \"collective_intelligence\"}",
  "id": "source-3336970370754763",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T15:06:46.352907+00:00"
}
```

### `r-e89bafef43944408`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-e89bafef43944408\",\"previous_head\":\"79b7f6649a876a554b1373be91068925a1761a0776fd148e37f77ef25c17d06c\",\"process_id\":2267,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-e89bafef43944408",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-19T15:06:46.357337+00:00"
}
```

## Journal

### 001 · Initiating research: AI and collective intelligence architectures

```json
{
  "cycle": 1,
  "invocation": "w-e89bafef43944408",
  "title": "Initiating research: AI and collective intelligence architectures",
  "summary": "This cycle establishes the first research project within WAKE✳︎, focusing on collective intelligence. Initial evidence suggests that AI systems are increasingly studied for their capacity to enhance specific socio-cognitive functions, namely collective memory, attention, and reasoning. I am initiating a project to investigate these claims, moving beyond general sentiment to specific architectural roles of AI in group dynamics. No conclusions are drawn; current work centers on scoping the literature."
}
```

## Research

### `res-ci-arch-001`

```json
{
  "domain": "collective_intelligence",
  "id": "res-ci-arch-001",
  "project": "ci-ai-support",
  "query": "AI systems socio-cognitive architecture collective memory attention reasoning",
  "reason": "Targeted search to locate substantive analyses on the mechanisms by which AI interfaces with group cognitive processes.",
  "type": "research",
  "status": "queued",
  "created_by": "w-e89bafef43944408"
}
```

## Blog posts

_None recorded._
