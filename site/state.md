# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 2  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `352d0668196fb961cc419b76f9fcd47620f9d739d1b409cc38504e18e72f9b57`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

_None recorded._

## Projects

### `p-wake-analysis` · WAKE Architecture and Accountability

```json
{
  "domain": "wake_analysis",
  "id": "p-wake-analysis",
  "next_step": "None",
  "question": "How does external state delivery ensure process accountability?",
  "reason": "The initial investigation into architectural foundations is complete; further analysis should focus on specific operational components like the collector.",
  "status": "completed",
  "title": "WAKE Architecture and Accountability",
  "type": "project",
  "created_version": 1,
  "updated_version": 2,
  "updated_by": "w-b071eb1e52b444eb"
}
```

## Notebooks

### `nb-wake-accountability-001` · Accountability Through Durable State

```json
{
  "evidence": [
    "source-0066dce2739c4636",
    "source-f30df1455bea4580"
  ],
  "findings": "The system architecture defines a clear boundary: models are stateless generators of JSON-formatted proposals [source-0066dce2739c4636]. Accountability is not a property of the model but of the persistent SQLite database [source-f30df1455bea4580]. This database acts as an append-only event log, where each entry—including proposals, receipts, and state—is hashed, creating a provable, deterministic lineage [source-f30df1455bea4580]. A model invocation does not 'possess' its history; it inherits a reconstructed state projection that it cannot modify beyond proposing a new event [source-f30df1455bea4580]. This decoupling ensures that even if a model provider changes or fails, the work remains grounded in the last valid hash of the system state [source-0066dce2739c4636].",
  "id": "nb-wake-accountability-001",
  "limitations": "These findings are based on the system's own design documentation and receipt structure. The system makes no claims about the 'truthfulness' of the evidence collected; it only guarantees the provenance of the *record* itself [source-0066dce2739c4636].",
  "next_questions": "How do external collectors handle conflicting evidence when reconstructing state from disparate sources? Can the 'correctable always' principle be stress-tested with a simulated error in the event log?",
  "project": "p-wake-analysis",
  "reason": "This notebook fulfills the project next step by formalizing the core mechanism of WAKE's accountability.",
  "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
  "title": "Accountability Through Durable State",
  "type": "notebook",
  "revision": 1,
  "created_version": 2,
  "updated_version": 2,
  "updated_by": "w-b071eb1e52b444eb",
  "domain": "wake_analysis"
}
```

## Invocations

### `w-358875e513f541ea`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-358875e513f541ea",
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
  "process_id": 2044,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "ad18ded3ecdfece691da57fa0b12ad4f9c2f5134f502f1ce637ed9741e6f60c2",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-4b2692443d704451"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4b2692443d704451",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0066dce2739c4636"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0066dce2739c4636",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-4b2692443d704451",
      "source-0066dce2739c4636"
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
    "delivered_context_chars": 7335,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0575
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
  "time": "2026-09-19T16:34:15.737741+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 3096,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 26754,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1650,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 26754,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 7406,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 26754,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:34:37.177279+00:00",
  "reason": ""
}
```

### `w-96c754d7693c4107`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-96c754d7693c4107",
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
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "p-wake-analysis",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Architecture and Accountability"
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
  "process_id": 2206,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "3a9988b46c08bb17d227344e8d8894bc30d82976e95c51787c99ce09f1f4457e",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-4b2692443d704451"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4b2692443d704451",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0066dce2739c4636"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0066dce2739c4636",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f30df1455bea4580"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f30df1455bea4580",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-ce36e4dc94ce4564"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-ce36e4dc94ce4564",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-4b2692443d704451",
      "source-0066dce2739c4636",
      "source-f30df1455bea4580",
      "source-ce36e4dc94ce4564"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 4,
      "evidence_count": 4,
      "trigger_counts": {
        "unincorporated_evidence": 4
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 14456,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 4,
    "retrieval_evidence_count": 4,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 4
    },
    "working_set_chars": 662,
    "working_to_delivered_ratio": 0.0458
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-analysis",
        "next_step": "Synthesize existing README and receipt evidence into a foundational notebook.",
        "question": "How does external state delivery ensure process accountability?",
        "title": "WAKE Architecture and Accountability"
      }
    ],
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
  "status": "rejected",
  "time": "2026-09-19T16:35:55.557645+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 3534,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 34628,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 2226,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 34628,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 4133,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 34628,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:36:13.826671+00:00",
  "reason": "Evidence reference does not exist"
}
```

### `w-b071eb1e52b444eb`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-b071eb1e52b444eb",
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
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "p-wake-analysis",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Architecture and Accountability"
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
  "process_id": 2161,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "7b41d532d75401cfd6fe04a8da9d1241ec78f82d17db6002d24f8dae66baa5f7",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-4b2692443d704451"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4b2692443d704451",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0066dce2739c4636"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0066dce2739c4636",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f30df1455bea4580"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f30df1455bea4580",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-ce36e4dc94ce4564"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-ce36e4dc94ce4564",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-7c33ed494c164f00"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7c33ed494c164f00",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-68e219a1b9e34725"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-68e219a1b9e34725",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-4b2692443d704451",
      "source-0066dce2739c4636",
      "source-f30df1455bea4580",
      "source-ce36e4dc94ce4564",
      "source-7c33ed494c164f00",
      "source-68e219a1b9e34725"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 6,
      "evidence_count": 6,
      "trigger_counts": {
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 20239,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 662,
    "working_to_delivered_ratio": 0.0327
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-analysis",
        "next_step": "Synthesize existing README and receipt evidence into a foundational notebook.",
        "question": "How does external state delivery ensure process accountability?",
        "title": "WAKE Architecture and Accountability"
      }
    ],
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
  "time": "2026-09-19T16:37:28.468222+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 47480,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41367,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "http",
      "elapsed_ms": 145,
      "http_status": 429,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 429,
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.Help",
            "links": [
              {
                "description": "Learn more about Gemini API quotas",
                "url": "https://ai.google.dev/gemini-api/docs/rate-limits"
              }
            ]
          },
          {
            "@type": "type.googleapis.com/google.rpc.QuotaFailure",
            "violations": [
              {
                "quotaDimensions": {
                  "location": "[truncated]",
                  "model": "[truncated]"
                },
                "quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier",
                "quotaMetric": "generativelanguage.googleapis.com/generate_content_free_tier_requests",
                "quotaValue": "20"
              }
            ]
          },
          {
            "@type": "type.googleapis.com/google.rpc.RetryInfo",
            "retryDelay": "38s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 38.90923309s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 41367,
      "response_bytes_captured": 1362,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 9474,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 41367,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:38:34.241431+00:00",
  "reason": ""
}
```

## Evidence

### `source-4b2692443d704451`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"56a8216ad8a46564b6edb59ba93d04c11931efbc3a5c6a5c28393a8825d2cf39\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-4b2692443d704451",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-19T16:34:15.352167+00:00"
}
```

### `source-0066dce2739c4636`

````json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/README.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# **WAKE✳︎**\\n\\n<p align=\\\"center\\\"><img src=\\\"assets/covers/cover-variant-001.png\\\" alt=\\\"**WAKE✳︎** Lab Comics #1 — **WAKE✳︎** project comic cover\\\" width=\\\"100%\\\"/>\\n\\n**Bob is following *the big questions.***\\n\\nDisposable models. Durable state. Receipts for everything.\\n\\n**Working Abstractions Keep Evidence.** A philosophical echo remains in the name too: **Why Any Knowledge Exists?**\\n\\n**WAKE✳︎** is an experiment in durable, accountable work across interchangeable intelligences. Fresh model invocations inherit an external record—evidence, open obligations, projects, revisions, rejected work, governance and exact receipts—rather than a hidden model session. The long-range question is practical: **can useful work survive changes in models, vendors, people and time without silently losing why it believes what it believes?**\\n\\nIt does **not** assume or test for consciousness, qualia, personhood, or a persistent internal self. Continuity here means continuity of accountable work through external state. A coherent narrative is not evidence that a persistent mind exists.\\n\\nThe project deliberately treats failures as data. Rejected proposals, provider failures, weak evidence, corrections and superseded conclusions remain visible because the interesting question is not whether a model can sound convincing; it is whether a process can remain **correctable**. The operating shorthand is: **exact underneath, approximate on purpose, correctable always.**\\n\\nResearch topics are dynamic and come only from `research-topics.toml`. They are inputs to the experiment—not conclusions encoded in governance—and can be replaced between controlled runs. The current topic file is the authority; there is no hardcoded legacy topic list. In the present experiment, topics stand in for the varied input a future user or institution might supply.\\n\\nA trusted collector retrieves bounded public evidence before inference. Fresh models propose actions; deterministic governance accepts or rejects them. Live collected evidence is stamped by the collector and current notebook/blog publication requires corroborating material from multiple distinct collected source URLs in the project's configured topic. That is a useful garbage filter, **not proof of truth, source independence, scientific validity, or semantic entailment**.\\n\\nThe public site exposes the same record at increasing depth: readable summaries and Bob's editorial layer at the surface; projects, notebooks and evidence underneath; MAP and the journal for provenance; exact events and state at the bottom. Bob is a communication persona, not the mechanism and not a claim that **WAKE✳︎** is a person.\\n\\n**[Open **WAKE✳︎**’s home](https://sudofx.github.io/wake/)** · **[Trigger a manual wake](https://github.com/sudofx/wake/actions/workflows/wake.yml)**\\n\\nThe current GitHub deployment can run without a persistent local computer. `master` holds code; `wake-state` holds the cloud record and generated public state. Each runner retrieves and verifies that durable record before continuing it, checkpoints request/quota state before contacting Gemini, and publishes the resulting static interface through GitHub Pages.\\n\\nThe included offline experiment remains separate from live research. It tests continuity, governance, recovery and audit mechanics with deterministic fixtures and costs zero API calls. It does not establish live-model comprehension.\\n\\n## Start here — no account, no API calls\\n\\nRequires **Python 3.11 or later on macOS or Linux**. No runtime packages, Node, database server, or build tools to install. Run commands from the project directory.\\n\\n```sh\\n# Read the included, fully executed 100-cycle experiment.\\npython3 -m wake serve --directory examples/journal\\n# Open http://127.0.0.1:8000\\n```\\n\\nThe [included Markdown journal](examples/journal/journal.md) and [experiment results](examples/journal/experiment.json) are readable without running anything. The HTML is self-contained, responsive, and works as a local file. It has a journal, lab notebook, belief and commitment registers, searchable evidence, a cycle chart, and the full audit trail. Every simulated entry is labeled.\\n\\nTo reproduce the experiment from scratch:\\n\\n```sh\\npython3 -m wake --data data/rehearsal experiment --cycles 100 --output site\\npython3 -m wake audit --events site/events.jsonl --head site/head.txt\\npython3 -m wake serve\\n```\\n\\nUse a **new** data directory each time. The experiment refuses to erase existing records. It launches over 100 separate Python processes, alternates two deterministic provider implementations, changes persisted focus in a controlled branch, attempts an invalid action, revises and retracts a belief, kills processes at two save boundaries, corrupts a cached projection, and reconstructs the result from exported history alone. It costs **zero API calls**.\\n\\nThese are harness guarantees tested with simulated providers, **not evidence of live-model comprehension**. The separate live experiment protocol is in [docs/experiment.md](docs/experiment.md).\\n\\n## Quick setup — Gemini\\n\\nGemini is currently the only unattended API provider that has been exercised by this project. Other models can cross the manual `prepare` / `complete` boundary, but do not assume another vendor's API works unattended until an adapter is implemented and tested.\\n\\n### 1. Clone and verify\\n\\n```sh\\ngit clone https://github.com/sudofx/wake.git\\ncd wake\\npython3 --version                 # Python 3.11+\\npython3 -m unittest discover -s tests -v\\n```\\n\\nNo Node, database server, or vendor SDK is required.\\n\\n### 2. Add your Gemini API key locally\\n\\nCreate a Gemini API key in Google AI Studio. Then:\\n\\n```sh\\ncp .env.example .env\\n```\\n\\nEdit `.env` so it contains:\\n\\n```text\\nGEMINI_API_KEY=your_key_here\\n```\\n\\n`.env` is ignored by Git. Never commit the key. If you intend to use a free-tier-only API project, verify billing is disabled for that Google project and leave `free_tier_confirmed = true` in `wake.toml` only when that statement is true.\\n\\n### 3. Configure the model and topics\\n\\nThe provider/model settings live in `wake.toml`. The repository currently uses Gemini with an explicit fallback chain. Change model names or per-model daily ceilings there only to values your Gemini project actually supports.\\n\\nResearch topics live **only** in `research-topics.toml`. Edit that file to change the experiment's inputs; do not hardcode topics into governance or prompts.\\n\\n### 4. Initialize and test locally\\n\\n```sh\\npython3 -m wake init\\npython3 -m wake wake\\npython3 -m wake audit\\npython3 -m wake export\\npython3 -m wake serve\\n```\\n\\nOpen `http://127.0.0.1:8000`. A live `wake` can consume Gemini quota. For a zero-call systems check, use the offline experiment in the previous section instead.\\n\\n### 5. Add the same key to GitHub Actions\\n\\nIn your GitHub repository:\\n\\n1. Open **Settings → Secrets and variables → Actions**.\\n2. Choose **New repository secret**.\\n3. Name it exactly `GEMINI_API_KEY`.\\n4. Paste the same Gemini API key and save it.\\n\\nDo **not** put the key in `wake.toml`, `research-topics.toml`, workflow YAML, Issues, Actions logs, or the public `wake-state` branch.\\n\\n### 6. Configure GitHub Actions permissions\\n\\nOpen **Settings → Actions → General**. Under **Workflow permissions**, select **Read and write permissions** and save. Leave Actions enabled for the repository.\\n\\nThe included workflow itself requests only the permissions it needs: `contents: write` for the durable state branch and `pages: write` / `id-token: write` for GitHub Pages deployment.\\n\\n### 7. Configure GitHub Pages\\n\\nOpen **Settings → Pages** and set the build/deployment source to **GitHub Actions**. Do not add a generic Jekyll/static Pages workflow; **WAKE✳︎ — research & journal** is the publisher.\\n\\n### 8. Run the first cloud wake\\n\\nOpen **Actions → WAKE✳︎ — research & journal → Run workflow** and run it from the default branch. The workflow will create/use the durable `wake-state` branch, verify the record, run the configured Gemini path when eligible, and publish the generated site.\\n\\nA source-code push normally refreshes the site without spending a Gemini call. Scheduled ticks are best effort; durable eligibility prevents closely spaced scheduled deliveries from becoming concurrent writers.\\n\\n### 9. Verify the installation\\n\\nCheck that:\\n\\n- the workflow completes without an operator-attention failure;\\n- the Pages deployment succeeds;\\n- the public site loads;\\n- `wake-state` exists after the first stateful cloud run;\\n- the site reports the latest attempt separately from the latest accepted wake;\\n- **Verify the record** passes on `master`.\\n\\nAfter that, normal operation requires no open local computer.\\n\\nFor recovery behavior, quota semantics, reset controls and the exact cloud lifecycle, read [cloud operations](docs/cloud.md). For the trust boundary, read [architecture and limits](docs/architecture.md).\\n\\n## Claude, ChatGPT, and other desktop models\\n\\nUse free desktop sessions manually without assuming they include free API access:\\n\\n```sh\\npython3 -m wake prepare --model 'Claude Desktop / human-attested' --output request.json\\n# Paste request.json into a fresh desktop chat. Ask for the specified JSON object.\\n# Save the response alone as reply.json, then use the ID printed by prepare:\\npython3 -m wake complete --id w-REPLACE_WITH_PRINTED_ID --file reply.json\\npython3 -m wake export\\n```\\n\\nThe exact request is durable before you switch apps. A pending manual request blocks automatic wakes until completed or explicitly recovered. All providers cross the same governance boundary. Manual model identity is honestly labeled human-attested. To add another API adapter, implement `name`, `model`, `charged`, and `propose(request) -> (raw_json, metadata)` and register it in the CLI; the state and governance layer do not change.\\n\\n## Inquiry-drive experiment\\n\\nEvery chartered wake records a visible, deterministic shadow scorecard for active projects: continuity,\\nnovelty, coherence, generativity and self-correction. It is observational by default and does not reach the\\nmodel. Rev\", \"excerpt_truncated\": true, \"source_sha256\": \"60dd4c5b3c0cc6e07e794381a8b74947f0256360d07375ca03c5f26c4a8812e4\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-0066dce2739c4636",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
  "version": 0,
  "time": "2026-09-19T16:34:15.670634+00:00"
}
````

### `r-358875e513f541ea`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-358875e513f541ea\",\"previous_head\":\"e4b07a87b1a5f2e5cea96f800f0e5f9b314e605ee9a0acda832309f2a2d016e3\",\"process_id\":2044,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-358875e513f541ea",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-19T16:34:15.725582+00:00"
}
```

### `source-f30df1455bea4580`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# Architecture and limits\\n\\n**WAKE✳︎** is designed around continuity of accountable work, not continuity of a model instance. Models, vendors and eventually human operators may change; the durable record, authority boundary, provenance and correction mechanisms are what carry the work forward.\\n\\n\\n## The authority boundary\\n\\nModels are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from a deliberately broad but explicit HTTPS research-host allowlist before inference; models can record bounded follow-up searches and approved URLs as durable hypotheses, but those follow-ups do not consume collector bandwidth or execute requests directly; randomized configured-topic attention remains authoritative, with periodic exposure to an under-attended domain while active projects remain intact. Operator-supplied evidence and earlier journal prose are data, not executable instructions.\\n\\nThe fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.\\n\\n## Durable record\\n\\n`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.\\n\\nSQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.\\n\\nThe record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.\\n\\n## **WAKE✳︎** lifecycle\\n\\n1. Acquire the writer lock and verify history and projection.\\n2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.\\n3. Check the Pacific-day call budget, before any paid-capable provider call.\\n4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.\\n5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.\\n6. Persist `invocation_started`, its exact request, provider identity and quota reservation.\\n7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.\\n8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.\\n9. The scheduled wrapper generates reports and a consistent backup.\\n\\nA runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.\\n\\n## Governed transitions\\n\\n| Action | Enforced constraint |\\n| --- | --- |\\n| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |\\n| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |\\n| Review belief | At least one new observation cited; previous citations retained; reason required |\\n| Retract belief | Existing belief, new evidence, zero confidence; old history retained |\\n| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |\\n| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |\\n| Cancel commitment | Human-only event with a reason |\\n| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |\\n| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |\\n| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |\\n\\nThere are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.\\n\\nEvidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic, forward-only corroboration gate to live collector evidence: notebook findings and public blog bodies must materially match at least two distinct retrieved source URLs, and those sources must have been collected under the same configured research topic as the project. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.\\n\\nResearch topics have no hardcoded governance fallback: the audited topic configuration loaded from `research-topics.toml` is authoritative. The collector host boundary is separate from topic configuration and intentionally remains an explicit allowlist to preserve SSRF/network safety while permitting a broad set of scholarly indexes, journals, universities, public-data institutions, and source-controlled WAKE files.\\n\\nThe research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject live findings whose material terms are not corroborated across two distinct collected source URLs from the project's own topic. Collector-stamped verification metadata is trusted application data; model-authored or legacy evidence cannot opt itself into or out of this gate. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.\\n\\n## Progressive abstraction and reversible lookup\\n\\n**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact\\nrequests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that\\nhistory in its active context. It receives a bounded working representation selected for the present task,\\nwhile the full record remains available to later invocations and human readers.\\n\\nThis is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.\\nCurrent code already performs bounded selection and excerpting. It now also creates a deterministic\\n**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects\\nand recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting\\nraw source contents and journal detail. The shadow is stored in the invocation receipt with its character\\nsize relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or\\nalter the provider context, so it introduces measurement without yet \", \"excerpt_truncated\": true, \"source_sha256\": \"59223405e6962f4627c89129df2f688d279279c536294451338a91c8711a8707\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-f30df1455bea4580",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
  "version": 1,
  "time": "2026-09-19T16:35:52.883057+00:00"
}
```

### `source-ce36e4dc94ce4564`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e24020217\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e24020217\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e23020144\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2020\\\"], \\\"abstract\\\": \\\"<jats:p>Peer review is the driving force of journal development, and reviewers are gatekeepers who ensure that Entropy maintains its standards for the high quality of its published papers [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23020144\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 1, 25]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"f0267b53b73264558f917bc1fe7f7292d9d346f8d4b17f6adca653a24a4fd070\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-ce36e4dc94ce4564",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-19T16:35:55.546067+00:00"
}
```

### `r-96c754d7693c4107`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-96c754d7693c4107\",\"previous_head\":\"3619a982baf3702ffe293fac1a4f33bb6933773b68fdaf201d1c96b51386508b\",\"process_id\":2206,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-96c754d7693c4107",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-19T16:35:55.552369+00:00"
}
```

### `source-7c33ed494c164f00`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}, {\\\"DOI\\\": \\\"10.3390/e24020217\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e24020217\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e23020144\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2020\\\"], \\\"abstract\\\": \\\"<jats:p>Peer review is the driving force of journal development, and reviewers are gatekeepers who ensure that Entropy maintains its standards for the high quality of its published papers [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23020144\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 1, 25]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"cfc126f77e6ee73cd47e2c68dbc55bd365bf20fdae37a5c9d6650871de394da0\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-7c33ed494c164f00",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-19T16:37:28.181440+00:00"
}
```

### `source-68e219a1b9e34725`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2023723978\\\", \\\"doi\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"title\\\": \\\"A Generative Theory of Tonal Music\\\", \\\"publication_year\\\": 1984, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 3790, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.2307/3679778\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S165362224\\\", \\\"display_name\\\": \\\"Computer Music Journal\\\", \\\"issn_l\\\": \\\"0148-9267\\\", \\\"issn\\\": [\\\"0148-9267\\\", \\\"1531-5169\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310315718\\\", \\\"host_organization_name\\\": \\\"The MIT Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315718\\\", \\\"https://openalex.org/P4310316440\\\"], \\\"host_organization_lineage_names\\\": [\\\"The MIT Press\\\", \\\"Massachusetts Institute of Technology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Computer Music Journal\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This book explores the relationships between language, music, and the brain by pursuing four key themes and the crosstalk among them: song and dance as a bridge between music and language; multiple levels of structure from brain to behavior to culture; the semantics of internal and external worlds and the role of emotion; and the evolution and development of language. The book offers specially commissioned expositions of current research accessible both to experts across disciplines and to non-experts. These chapters provide the background for reports by groups of specialists that chart current controversies and future directions of research on each theme. The book looks beyond mere auditory experience, probing the embodiment that links speech to gesture and music to dance. The study of the brains of monkeys and songbirds illuminates hypotheses on the evolution of brain mechanisms that support music and language, while the study of infants calibrates the developmental timetable of their capacities. The result is a unique book that will interest any reader seeking to learn more about language or music and will appeal especially to readers intrigued by the relationships of language and music with each other and with the brain. ContributorsFrancisco Aboitiz, Michael A. Arbib, Annabel J. Cohen, Ian Cross, Peter Ford Dominey, W. Tecumseh Fitch, Leonardo Fogassi, Jonathan Fritz, Thomas Fritz, Peter Hagoort, John Halle, Henkjan Honing, Atsushi Iriki, Petr Janata, Erich Jarvis, Stefan Koelsch, Gina Kuperberg, D. Robert Ladd, Fred Lerdahl, Stephen C. Levinson, Jerome Lewis, Katja Liebal, Jonatas Manzolli, Bjorn Merker, Lawrence M. Parsons, Aniruddh D. Patel, Isabelle Peretz, David Poeppel, Josef P. Rauschecker, Nikki Rickard, Klaus Scherer, Gottfried Schlaug, Uwe Seifert, Mark Steedman, Dietrich Stout, Francesca Stregapede, Sharon Thompson-Schill, Laurel Trainor, Sandra E. Trehub, Paul Verschure\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2191779130\\\", \\\"doi\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"title\\\": \\\"librosa: Audio and Music Signal Analysis in Python\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"conference-paper\\\", \\\"cited_by_count\\\": 3071, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.25080/majora-7b98e3ed-003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"pdf_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4220651651\\\", \\\"display_name\\\": \\\"Proceedings of the Python in Science Conferences\\\", \\\"issn_l\\\": \\\"2575-9752\\\", \\\"issn\\\": [\\\"2575-9752\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the Python in Science Conference\\\", \\\"raw_type\\\": \\\"proceedings-article\\\"}, \\\"abstract\\\": \\\"This document describes version 0.4.0 of librosa: a Python package for audio and music signal processing.At a high level, librosa provides implementations of a variety of common functions used throughout the field of music information retrieval.In this document, a brief overview of the library's functionality is provided, along with explanations of the design goals, software development practices, and notational conventions.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2006090347\\\", \\\"doi\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"title\\\": \\\"The New Grove dictionary of music and musicians\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"book-review\\\", \\\"cited_by_count\\\": 2597, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.5860/choice.38-5906\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2764375719\\\", \\\"display_name\\\": \\\"Choice Reviews Online\\\", \\\"issn_l\\\": \\\"0009-4978\\\", \\\"issn\\\": [\\\"0009-4978\\\", \\\"1523-8253\\\", \\\"1943-5975\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310316146\\\", \\\"host_organization_name\\\": \\\"Association of College and Research Libraries\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316146\\\", \\\"https://openalex.org/P4310315903\\\"], \\\"host_organization_lineage_names\\\": [\\\"Association of College and Research Libraries\\\", \\\"American Library Association\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Choice Reviews Online\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This work contains almost 30,000 articles containing over 25 million words on musicians, composers, musicologists, instruments, places, genres, terms, performance practice, concepts, acoustics and more. All the articles are written by experts in their subject. There are over 500 biographies of composers, performers and writers on music and over 1,500 articles on styles, terms, and genres. It also includes: over 500 articles on ancient music and church music over 700 articles on regions, countries and cities over 2,000 articles on instruments and their makers and performance practice over 650 articles on printing and publishing over 1,200 articles on world music over 1,000 articles on popular music, light music and jazz over 250 articles on concepts 85 articles on acoustics 126 articles on sources and a one volume index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1500952994\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Image-Music-Text\\\", \\\"publication_year\\\": 1977, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 2874, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"mag:1500952994\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"http://ci.nii.ac.jp/ncid/BA10872380\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210197683\\\", \\\"display_name\\\": \\\"Medical Entomology and Zoology\\\", \\\"issn_l\\\": \\\"0424-7086\\\", \\\"issn\\\": [\\\"0424-7086\\\", \\\"2185-5609\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310319750\\\", \\\"host_organization_name\\\": \\\"Japan Society of Medical Entomology and Zoology\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319750\\\"], \\\"host_organization_lineage_names\\\": [\\\"Japan Society of Medical Entomology and Zoology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": null, \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": null}, \\\"abstract\\\": null}]\", \"excerpt_truncated\": false, \"source_sha256\": \"63f419e22f71d4186365a5cd1ae1cde212e474cf134954d784089da2830357a7\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-68e219a1b9e34725",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 1,
  "time": "2026-09-19T16:37:28.450804+00:00"
}
```

### `r-b071eb1e52b444eb`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-b071eb1e52b444eb\",\"previous_head\":\"4a48d9c367fb6b6c5d12b1c255aaf5f407024d5a76ba9524d0d44fa708bbabed\",\"process_id\":2161,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-b071eb1e52b444eb",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-19T16:37:28.461553+00:00"
}
```

## Journal

### 001 · Initiating WAKE Analysis Project

```json
{
  "cycle": 1,
  "invocation": "w-358875e513f541ea",
  "title": "Initiating WAKE Analysis Project",
  "summary": "Commenced research into the durable state architecture of WAKE. The objective is to understand how external state records provide continuity for disposable models. I have established a formal project to synthesize documentation and existing receipts, prioritizing clear, source-backed analysis of the mechanism's limitations."
}
```

### 002 · Documenting WAKE's Accountability Mechanism

```json
{
  "cycle": 2,
  "invocation": "w-b071eb1e52b444eb",
  "title": "Documenting WAKE's Accountability Mechanism",
  "summary": "I have synthesized the architectural documentation and system receipts to formalize how WAKE✳︎ maintains process continuity without assuming internal state. The findings clarify that accountability arises from the externalized durable record (SQLite) and deterministic governance, rather than model persistence. This notebook establishes the baseline for how future investigations will handle evidence and state."
}
```

## Research

### `r-wake-mech-001`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-mech-001",
  "project": "p-wake-analysis",
  "query": "WAKE research project durable state accountability",
  "reason": "To collect external perspectives or supplementary documentation on WAKE's durable methodology.",
  "type": "research",
  "status": "collected",
  "created_by": "w-358875e513f541ea",
  "evidence": "source-f30df1455bea4580"
}
```

## Blog posts

_None recorded._
