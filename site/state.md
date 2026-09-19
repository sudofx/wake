# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 8  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `f9d45c737b43f6be9a6b90331aaee28e5017fb89c8a6359ca26eae25df79330f`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

### `b-wake-state-accountability`

```json
{
  "confidence": 0.9,
  "evidence": [
    "source-8284e29d25894a55"
  ],
  "id": "b-wake-state-accountability",
  "reason": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than filesystem operators.",
  "statement": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-30cd6d01073e4433",
  "updated_version": 5
}
```

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

### `p-wake-foundations` · WAKE Foundations

```json
{
  "domain": "wake_analysis",
  "id": "p-wake-foundations",
  "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
  "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
  "reason": "The project is near completion; securing the final piece of evidence will allow for the formal notebook publication.",
  "status": "active",
  "title": "WAKE Foundations",
  "type": "project",
  "created_version": 3,
  "updated_version": 7,
  "updated_by": "w-3db4492e6d50484b"
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

### `w-c3cf9d34346c4dae`

```json
{
  "base_version": 2,
  "charged": true,
  "id": "w-c3cf9d34346c4dae",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 2,
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
  "process_id": 2324,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "586f6189b3a50ec2e9f351c643ebb76d157d9e76cdd19b9ccddcd6be71433d76",
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
      },
      {
        "evidence": [
          "source-585fd570ebf34cc6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-585fd570ebf34cc6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f36dd5d7a2a14178"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f36dd5d7a2a14178",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-4b2692443d704451",
      "source-ce36e4dc94ce4564",
      "source-7c33ed494c164f00",
      "source-68e219a1b9e34725",
      "source-585fd570ebf34cc6",
      "source-f36dd5d7a2a14178"
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
    "delivered_context_chars": 22731,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 821,
    "working_to_delivered_ratio": 0.0361
  },
  "working_set_shadow": {
    "active_projects": [],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T16:39:46.485418+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 2878,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 45151,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 7815,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 45151,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:40:03.417897+00:00",
  "reason": "Research notebooks need at least two distinct retrieved source URLs"
}
```

### `w-e4aa1ef9a7194a26`

```json
{
  "base_version": 2,
  "charged": true,
  "id": "w-e4aa1ef9a7194a26",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 2,
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
  "process_id": 2335,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "fa145558e0b04ed9320984bac153c849f85c3390d343eebc802480c9eff16fbd",
  "retrieval_shadow": {
    "candidates": [
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
      },
      {
        "evidence": [
          "source-585fd570ebf34cc6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-585fd570ebf34cc6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f36dd5d7a2a14178"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f36dd5d7a2a14178",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6feed55174eb4deb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6feed55174eb4deb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-42de548883bb45fb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-42de548883bb45fb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-7c33ed494c164f00",
      "source-68e219a1b9e34725",
      "source-585fd570ebf34cc6",
      "source-f36dd5d7a2a14178",
      "source-6feed55174eb4deb",
      "source-42de548883bb45fb"
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
    "delivered_context_chars": 23008,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 821,
    "working_to_delivered_ratio": 0.0357
  },
  "working_set_shadow": {
    "active_projects": [],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T16:41:22.001072+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 237,
      "http_status": 429,
      "model": "gemini-3.8-flash",
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
            "retryDelay": "35s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 35.158142278s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 45841,
      "response_bytes_captured": 1363,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 9241,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 45841,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:41:37.725443+00:00",
  "reason": ""
}
```

### `w-482d16f8cb8d4423`

```json
{
  "base_version": 3,
  "charged": true,
  "id": "w-482d16f8cb8d4423",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 3,
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
        "id": "p-wake-foundations",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2041,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "14f0cc1e151469f03bb517413283cd348a9bc289ec909b207b3fe139cc6dfeb9",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-585fd570ebf34cc6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-585fd570ebf34cc6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f36dd5d7a2a14178"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f36dd5d7a2a14178",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6feed55174eb4deb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6feed55174eb4deb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-42de548883bb45fb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-42de548883bb45fb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8284e29d25894a55",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0998d27dbc9a474b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0998d27dbc9a474b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-585fd570ebf34cc6",
      "source-f36dd5d7a2a14178",
      "source-6feed55174eb4deb",
      "source-42de548883bb45fb",
      "source-8284e29d25894a55",
      "source-0998d27dbc9a474b"
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
    "delivered_context_chars": 24129,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1079,
    "working_to_delivered_ratio": 0.0447
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "deferred",
  "time": "2026-09-19T16:42:44.568817+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 23186,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 46690,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-19T16:43:11.544550+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 23186,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 23186,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 46690,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 1,
    "request_payload_bytes": 46690,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-83ee22b03bd646fe`

```json
{
  "base_version": 3,
  "charged": true,
  "id": "w-83ee22b03bd646fe",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 3,
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
        "id": "p-wake-foundations",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2274,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "d446e2cd1754df2f7951a64642d5245f60d5bdd2313322febed371b128aae165",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-6feed55174eb4deb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6feed55174eb4deb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-42de548883bb45fb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-42de548883bb45fb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8284e29d25894a55",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0998d27dbc9a474b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0998d27dbc9a474b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-64da9440d8ae4b83"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-64da9440d8ae4b83",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2533c1dd71624e64"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2533c1dd71624e64",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-6feed55174eb4deb",
      "source-42de548883bb45fb",
      "source-8284e29d25894a55",
      "source-0998d27dbc9a474b",
      "source-64da9440d8ae4b83",
      "source-2533c1dd71624e64"
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
    "delivered_context_chars": 23120,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1079,
    "working_to_delivered_ratio": 0.0467
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T16:44:25.514626+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 1857,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 45653,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:44:31.178598+00:00",
  "reason": ""
}
```

### `w-30cd6d01073e4433`

```json
{
  "base_version": 4,
  "charged": true,
  "id": "w-30cd6d01073e4433",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 4,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2194,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "041567b2e444f5fa1617ee03789a270a1a310f0bd1539c6d5f5e71c4b5514412",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8284e29d25894a55",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0998d27dbc9a474b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0998d27dbc9a474b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-64da9440d8ae4b83"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-64da9440d8ae4b83",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2533c1dd71624e64"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2533c1dd71624e64",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-dd7ce7262f674506"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-dd7ce7262f674506",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-7fe2bc9f4f514c12"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7fe2bc9f4f514c12",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-0998d27dbc9a474b",
      "source-64da9440d8ae4b83",
      "source-2533c1dd71624e64",
      "source-dd7ce7262f674506",
      "source-7fe2bc9f4f514c12"
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
    "delivered_context_chars": 22761,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1079,
    "working_to_delivered_ratio": 0.0474
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T16:45:44.613695+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 10114,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 44874,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:45:58.655185+00:00",
  "reason": ""
}
```

### `w-6772e9b19da94533`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-6772e9b19da94533",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2746,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "cf62af4c99b9977e844936c7ee6d4550c911dbdcb8a163a2a176a3359ab9fa47",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-64da9440d8ae4b83"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-64da9440d8ae4b83",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2533c1dd71624e64"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2533c1dd71624e64",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-dd7ce7262f674506"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-dd7ce7262f674506",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-7fe2bc9f4f514c12"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7fe2bc9f4f514c12",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-715bf7bfa65f492a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-715bf7bfa65f492a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3f58bf0afa604a84"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3f58bf0afa604a84",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-64da9440d8ae4b83",
      "source-2533c1dd71624e64",
      "source-dd7ce7262f674506",
      "source-7fe2bc9f4f514c12",
      "source-715bf7bfa65f492a",
      "source-3f58bf0afa604a84"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 25667,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0655
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T16:47:04.926604+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 5125,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 48483,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:47:13.773522+00:00",
  "reason": "Stale or invalid base_version"
}
```

### `w-644b73b84fc94b6d`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-644b73b84fc94b6d",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2047,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "4a650b32210fce22fdd9a7a22807efc5dc21c3df39803385fa56025fd450ed89",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-dd7ce7262f674506"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-dd7ce7262f674506",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-7fe2bc9f4f514c12"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7fe2bc9f4f514c12",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-715bf7bfa65f492a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-715bf7bfa65f492a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3f58bf0afa604a84"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3f58bf0afa604a84",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a9d63b5b92cd46ff"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a9d63b5b92cd46ff",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-714ed4eab8364517"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-714ed4eab8364517",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-dd7ce7262f674506",
      "source-7fe2bc9f4f514c12",
      "source-715bf7bfa65f492a",
      "source-3f58bf0afa604a84",
      "source-a9d63b5b92cd46ff",
      "source-714ed4eab8364517"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 25000,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0672
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "deferred",
  "time": "2026-09-19T16:48:21.380931+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 7296,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 47932,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-19T16:48:33.465843+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 7296,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 7296,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 47932,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 1,
    "request_payload_bytes": 47932,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-3e6f1f402da4463a`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-3e6f1f402da4463a",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2065,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "b106c19a9105853b93ccaa48c4a366dc7871f692f0ad34174b735dc87dbf5856",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-715bf7bfa65f492a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-715bf7bfa65f492a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3f58bf0afa604a84"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3f58bf0afa604a84",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a9d63b5b92cd46ff"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a9d63b5b92cd46ff",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-714ed4eab8364517"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-714ed4eab8364517",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cd1dd67a2fff4972"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cd1dd67a2fff4972",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-97f546d2f97a4547"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-97f546d2f97a4547",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-715bf7bfa65f492a",
      "source-3f58bf0afa604a84",
      "source-a9d63b5b92cd46ff",
      "source-714ed4eab8364517",
      "source-cd1dd67a2fff4972",
      "source-97f546d2f97a4547"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 25872,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.065
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "deferred",
  "time": "2026-09-19T16:49:42.387363+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 21116,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 49292,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-19T16:50:07.722765+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 21116,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 21116,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 49292,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 1,
    "request_payload_bytes": 49292,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-9e668a8e7edb4cb3`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-9e668a8e7edb4cb3",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2053,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "036f3d5c21388e1d7aa247040e13906bbbb709a9f034de79671783198143ed63",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-a9d63b5b92cd46ff"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a9d63b5b92cd46ff",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-714ed4eab8364517"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-714ed4eab8364517",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cd1dd67a2fff4972"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cd1dd67a2fff4972",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-97f546d2f97a4547"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-97f546d2f97a4547",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4c409854df6146cc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4c409854df6146cc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-658000d10aad48e6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-658000d10aad48e6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-a9d63b5b92cd46ff",
      "source-714ed4eab8364517",
      "source-cd1dd67a2fff4972",
      "source-97f546d2f97a4547",
      "source-4c409854df6146cc",
      "source-658000d10aad48e6"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 23974,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0701
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T16:51:32.890838+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 4847,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 47134,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:51:42.318065+00:00",
  "reason": "Stale or invalid base_version"
}
```

### `w-1a69e42b1c434423`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-1a69e42b1c434423",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2100,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "8328d420e9d4e6fd6530c4c7ab04e7be7e89a3788fad93950df2b4e74203ac6b",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-cd1dd67a2fff4972"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cd1dd67a2fff4972",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-97f546d2f97a4547"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-97f546d2f97a4547",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4c409854df6146cc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4c409854df6146cc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-658000d10aad48e6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-658000d10aad48e6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0df9f503166f4082"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0df9f503166f4082",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b04e6f19a4f74765"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b04e6f19a4f74765",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-cd1dd67a2fff4972",
      "source-97f546d2f97a4547",
      "source-4c409854df6146cc",
      "source-658000d10aad48e6",
      "source-0df9f503166f4082",
      "source-b04e6f19a4f74765"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 24115,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0697
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T16:52:56.536866+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 2245,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 47631,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:53:03.254113+00:00",
  "reason": "Stale or invalid base_version"
}
```

### `w-4df368205109443c`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-4df368205109443c",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2249,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "0bf48469a5cf10fffde8678c965a97f38b5b67515f97108e33471d49a31fea11",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-4c409854df6146cc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4c409854df6146cc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-658000d10aad48e6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-658000d10aad48e6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0df9f503166f4082"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0df9f503166f4082",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b04e6f19a4f74765"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b04e6f19a4f74765",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-729dc050c1c24657"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-729dc050c1c24657",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c1208ace89e84831"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c1208ace89e84831",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-4c409854df6146cc",
      "source-658000d10aad48e6",
      "source-0df9f503166f4082",
      "source-b04e6f19a4f74765",
      "source-729dc050c1c24657",
      "source-c1208ace89e84831"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 24039,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0699
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T16:54:28.382976+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 5750,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 47661,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:54:38.512093+00:00",
  "reason": "Research notebooks need at least two distinct retrieved source URLs"
}
```

### `w-1a4ba06b2fa24fb6`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-1a4ba06b2fa24fb6",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2067,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "7ff892e61bdc8077cc376dddebf28abdbc3340ee84339046c6f1d08b0edca12e",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-0df9f503166f4082"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0df9f503166f4082",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b04e6f19a4f74765"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b04e6f19a4f74765",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-729dc050c1c24657"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-729dc050c1c24657",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c1208ace89e84831"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c1208ace89e84831",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-44d3b63b3ba24f93"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-44d3b63b3ba24f93",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-010488341e39464c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-010488341e39464c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-0df9f503166f4082",
      "source-b04e6f19a4f74765",
      "source-729dc050c1c24657",
      "source-c1208ace89e84831",
      "source-44d3b63b3ba24f93",
      "source-010488341e39464c"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 24978,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0673
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T16:55:51.059716+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 11630,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 49088,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:56:06.791973+00:00",
  "reason": "Research notebooks need at least two distinct retrieved source URLs"
}
```

### `w-52523dbea48f41d5`

```json
{
  "base_version": 5,
  "charged": true,
  "id": "w-52523dbea48f41d5",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 5,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2042,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "e9da62eb99a9660653c56f6d8133e1e19e6fe466fa453edf792d4db3a39e02bf",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-729dc050c1c24657"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-729dc050c1c24657",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c1208ace89e84831"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c1208ace89e84831",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-44d3b63b3ba24f93"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-44d3b63b3ba24f93",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-010488341e39464c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-010488341e39464c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b99500d122264f40"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b99500d122264f40",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c314ace135114008"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c314ace135114008",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-729dc050c1c24657",
      "source-c1208ace89e84831",
      "source-44d3b63b3ba24f93",
      "source-010488341e39464c",
      "source-b99500d122264f40",
      "source-c314ace135114008"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 25486,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.066
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T16:57:17.200882+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 8874,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 49110,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T16:57:30.669171+00:00",
  "reason": ""
}
```

### `w-80c56b702b6e452b`

```json
{
  "base_version": 6,
  "charged": true,
  "id": "w-80c56b702b6e452b",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 6,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 4,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2236,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "f5d070eb8793c4ff96b8e8b4faab7bad25f85e6d7d87c97893e89567a1b4c9f3",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-44d3b63b3ba24f93"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-44d3b63b3ba24f93",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-010488341e39464c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-010488341e39464c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b99500d122264f40"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b99500d122264f40",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c314ace135114008"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c314ace135114008",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-50089614af314989"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-50089614af314989",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4cfd4c36f09d48e6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4cfd4c36f09d48e6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-44d3b63b3ba24f93",
      "source-010488341e39464c",
      "source-b99500d122264f40",
      "source-c314ace135114008",
      "source-50089614af314989",
      "source-4cfd4c36f09d48e6"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 27304,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0616
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "deferred",
  "time": "2026-09-19T16:58:45.695607+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 230,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 50596,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-19T16:58:50.240404+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 230,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 230,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 50596,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 1,
    "request_payload_bytes": 50596,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-3db4492e6d50484b`

```json
{
  "base_version": 6,
  "charged": true,
  "id": "w-3db4492e6d50484b",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 6,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 4,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2270,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "086dc3c4944c95ddac07ae215b592bafb265b7f6f2f2e13f6832e53c977ac55d",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-b99500d122264f40"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b99500d122264f40",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c314ace135114008"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c314ace135114008",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-50089614af314989"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-50089614af314989",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4cfd4c36f09d48e6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4cfd4c36f09d48e6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-942104ac46584bcc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-942104ac46584bcc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bfc4dd0c46284b92"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bfc4dd0c46284b92",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-b99500d122264f40",
      "source-c314ace135114008",
      "source-50089614af314989",
      "source-4cfd4c36f09d48e6",
      "source-942104ac46584bcc",
      "source-bfc4dd0c46284b92"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 26464,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1681,
    "working_to_delivered_ratio": 0.0635
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Collect two verified, distinct sources documenting WAKE mechanisms to support a new notebook.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T17:00:05.822594+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 4412,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 49388,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:00:15.149125+00:00",
  "reason": ""
}
```

### `w-108f5d64df6e475a`

```json
{
  "base_version": 7,
  "charged": true,
  "id": "w-108f5d64df6e475a",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 7,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 5,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2051,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "7067287a4e70261bb6ee7998edd5dcc4ae73f1a23abe60cc1fd8792452183eec",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-50089614af314989"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-50089614af314989",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4cfd4c36f09d48e6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4cfd4c36f09d48e6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-942104ac46584bcc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-942104ac46584bcc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bfc4dd0c46284b92"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bfc4dd0c46284b92",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-792f5e3747bd471e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-792f5e3747bd471e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-72f79904cc4146e3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-72f79904cc4146e3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-50089614af314989",
      "source-4cfd4c36f09d48e6",
      "source-942104ac46584bcc",
      "source-bfc4dd0c46284b92",
      "source-792f5e3747bd471e",
      "source-72f79904cc4146e3"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 28100,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0596
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "deferred",
  "time": "2026-09-19T17:01:34.629522+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 9683,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 51000,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-19T17:01:49.277753+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 9683,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 9683,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 51000,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 1,
    "request_payload_bytes": 51000,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-2321fcfbde8a482a`

```json
{
  "base_version": 7,
  "charged": true,
  "id": "w-2321fcfbde8a482a",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 7,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 5,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2249,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "43e071fe1c02030f53d1ce8fee822e1be862747e36433330a11f2e8780519c7e",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-942104ac46584bcc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-942104ac46584bcc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bfc4dd0c46284b92"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bfc4dd0c46284b92",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-792f5e3747bd471e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-792f5e3747bd471e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-72f79904cc4146e3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-72f79904cc4146e3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f305db2c21df49db"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f305db2c21df49db",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-39092b1a00cf4d3b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-39092b1a00cf4d3b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-942104ac46584bcc",
      "source-bfc4dd0c46284b92",
      "source-792f5e3747bd471e",
      "source-72f79904cc4146e3",
      "source-f305db2c21df49db",
      "source-39092b1a00cf4d3b"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 26956,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0621
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T17:03:08.709272+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 7643,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 50122,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:03:21.114689+00:00",
  "reason": "Evidence reference does not exist"
}
```

### `w-4e660446e0c443bb`

```json
{
  "base_version": 7,
  "charged": true,
  "id": "w-4e660446e0c443bb",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 7,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 5,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2264,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "8ee35e759a49735b6396872235d9edca7567cda3c903adf709701ca5bdd82a7f",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-792f5e3747bd471e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-792f5e3747bd471e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-72f79904cc4146e3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-72f79904cc4146e3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f305db2c21df49db"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f305db2c21df49db",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-39092b1a00cf4d3b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-39092b1a00cf4d3b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6b5551c683294b62"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6b5551c683294b62",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-97bfd6feed6c4aa4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-97bfd6feed6c4aa4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-792f5e3747bd471e",
      "source-72f79904cc4146e3",
      "source-f305db2c21df49db",
      "source-39092b1a00cf4d3b",
      "source-6b5551c683294b62",
      "source-97bfd6feed6c4aa4"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 27762,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0603
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "accepted",
  "time": "2026-09-19T17:04:37.751140+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 3645,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 51296,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:04:46.342063+00:00",
  "reason": ""
}
```

### `w-13c57dd4dc0c426d`

```json
{
  "base_version": 8,
  "charged": true,
  "id": "w-13c57dd4dc0c426d",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 8,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 6,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2330,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "bd26cc92a78f636753a3c39a801e0cc3fec669a57f165c887db82edb3e0fba60",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-f305db2c21df49db"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f305db2c21df49db",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-39092b1a00cf4d3b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-39092b1a00cf4d3b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6b5551c683294b62"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6b5551c683294b62",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-97bfd6feed6c4aa4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-97bfd6feed6c4aa4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-45040ee617e24b46"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-45040ee617e24b46",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2521d3cafff14afe"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2521d3cafff14afe",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-f305db2c21df49db",
      "source-39092b1a00cf4d3b",
      "source-6b5551c683294b62",
      "source-97bfd6feed6c4aa4",
      "source-45040ee617e24b46",
      "source-2521d3cafff14afe"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 26210,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0639
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T17:06:09.645678+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 3467,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 49488,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:06:18.187307+00:00",
  "reason": "Research notebooks need at least two distinct retrieved source URLs"
}
```

### `w-fb3feb4cdadc4943`

```json
{
  "base_version": 8,
  "charged": true,
  "id": "w-fb3feb4cdadc4943",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 8,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 6,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2329,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "a4553555570c97075fcd06412b403473a811ca10827383f6459074161f27ac6f",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-6b5551c683294b62"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6b5551c683294b62",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-97bfd6feed6c4aa4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-97bfd6feed6c4aa4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-45040ee617e24b46"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-45040ee617e24b46",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2521d3cafff14afe"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2521d3cafff14afe",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cb0d1c753eb5458c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cb0d1c753eb5458c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6972518d3d784ec8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6972518d3d784ec8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-6b5551c683294b62",
      "source-97bfd6feed6c4aa4",
      "source-45040ee617e24b46",
      "source-2521d3cafff14afe",
      "source-cb0d1c753eb5458c",
      "source-6972518d3d784ec8"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 26224,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0639
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T17:07:38.876666+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 16460,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 49516,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:08:00.372285+00:00",
  "reason": "Evidence reference does not exist"
}
```

### `w-c80bddf4b4df4e46`

```json
{
  "base_version": 8,
  "charged": true,
  "id": "w-c80bddf4b4df4e46",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 8,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 6,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2102,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "0b9294b073a57e282b830de5a3affed3238eeb2adaa4321a8f0c46bb25990f22",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-45040ee617e24b46"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-45040ee617e24b46",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2521d3cafff14afe"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2521d3cafff14afe",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cb0d1c753eb5458c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cb0d1c753eb5458c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6972518d3d784ec8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6972518d3d784ec8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-759e73e35dd84f7c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-759e73e35dd84f7c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f77686c3d5da4895"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f77686c3d5da4895",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-45040ee617e24b46",
      "source-2521d3cafff14afe",
      "source-cb0d1c753eb5458c",
      "source-6972518d3d784ec8",
      "source-759e73e35dd84f7c",
      "source-f77686c3d5da4895"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 26047,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0643
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T17:09:18.320311+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 7092,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 48855,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:09:30.267727+00:00",
  "reason": "Research notebooks need at least two distinct retrieved source URLs"
}
```

### `w-e0b88e2d179943c9`

```json
{
  "base_version": 8,
  "charged": true,
  "id": "w-e0b88e2d179943c9",
  "inquiry_drive_shadow": {
    "activation": {
      "active": false,
      "completed_scored_cycles": 8,
      "minimum_completed_scored_cycles": 20,
      "operator_enabled": false
    },
    "enabled": true,
    "mode": "shadow",
    "principle": "Rank continuation of productive inquiry, not preservation of WAKE or its state.",
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-wake-foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 6,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "WAKE Foundations"
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
  "process_id": 2115,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "33659e7ad8691d62e49f465ec746bf593238efceefd9b9e593f9911eb3777783",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-8284e29d25894a55"
        ],
        "reason": "A working abstraction is clipped and may hide a material distinction.",
        "record": {
          "id": "b-wake-state-accountability",
          "kind": "belief"
        },
        "trigger": "excerpt_boundary"
      },
      {
        "evidence": [
          "source-cb0d1c753eb5458c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cb0d1c753eb5458c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6972518d3d784ec8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6972518d3d784ec8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-759e73e35dd84f7c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-759e73e35dd84f7c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f77686c3d5da4895"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f77686c3d5da4895",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b381d20c90164724"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b381d20c90164724",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-761538004f314bcc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-761538004f314bcc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8284e29d25894a55",
      "source-cb0d1c753eb5458c",
      "source-6972518d3d784ec8",
      "source-759e73e35dd84f7c",
      "source-f77686c3d5da4895",
      "source-b381d20c90164724",
      "source-761538004f314bcc"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 7,
      "trigger_counts": {
        "excerpt_boundary": 1,
        "unincorporated_evidence": 6
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 27099,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 7,
    "retrieval_trigger_counts": {
      "excerpt_boundary": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 1675,
    "working_to_delivered_ratio": 0.0618
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-wake-foundations",
        "next_step": "Synthesize collected evidence into a notebook once a second distinct source is secured.",
        "question": "What are the core architectural and mechanical foundations of the WAKE experiment?",
        "title": "WAKE Foundations"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE achieves process accountability by externalizing its state machine into a deterministic database, thereby ensuring each disposable model invocation operates on a verifiable, immutable history rather than persistent internal model state.",
        "confidence": 0.9,
        "id": "b-wake-state-accountability",
        "provenance": [
          "source-8284e29d25894a55"
        ],
        "status": "active",
        "why_retained": "The WAKE architecture documentation explicitly identifies the durable record (the events table in SQLite) as the mechanism for carrying work forward, specifically noting that models are proposal generators rather than f…"
      }
    ],
    "mode": "shadow",
    "open_commitments": [],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "nb-wake-accountability-001",
        "project": "p-wake-analysis",
        "provenance": [
          "source-0066dce2739c4636",
          "source-f30df1455bea4580"
        ],
        "revision": 1,
        "summary": "WAKE✳︎ achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.",
        "title": "Accountability Through Durable State"
      }
    ],
    "retrieval_triggers": [
      "material belief revision or retraction",
      "new contradiction or counterevidence",
      "high-consequence decision",
      "request for justification",
      "sign that an excerpt may hide a material distinction"
    ]
  },
  "status": "rejected",
  "time": "2026-09-19T17:10:48.595892+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 42582,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 50449,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:11:36.041209+00:00",
  "reason": "Only open commitments can be resolved"
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

### `source-585fd570ebf34cc6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W1989670470\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"title\\\": \\\"Shakespeare and the Traditions of Comedy\\\", \\\"publication_year\\\": 1974, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 295, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511553189\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"This book relates Shakespeare's comedies to a broad European background. At the beginning and again at the end of his career, Shakespeare was attracted by a tradition of stage romances which can be traced back to Chaucer's time. But the main shaping behind his comedies came from the classical tradition. Mr Salingar therefore examines the underlying theme of 'errors' in Greek and Roman comedies and, taking three Italian comedies famous in the sixteenth century as examples, he then reveals how the Italian Renaissance revived the classical tradition, and what effect this revival had on Shakespeare the Elizabethan playwright and discusses such topics as the device of the play within a play and Shakespeare's choice of Italian short stories as plot material. This book shows how Shakespeare changed the motifs he took over from previous traditions of comedy and highlights the innovations he introduced, as an actor-dramatist writing in the first period of commercial theatre in Europe.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4213157483\\\", \\\"doi\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"title\\\": \\\"Slaves, Masters, and the Art of Authority in Plautine Comedy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 396, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1515/9781400824700\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306463805\\\", \\\"display_name\\\": \\\"Princeton University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310316492\\\", \\\"host_organization_name\\\": \\\"Princeton University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316492\\\"], \\\"host_organization_lineage_names\\\": [\\\"Princeton University Press\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"What pleasures did Plautus' heroic tricksters provide their original audience? How should we understand the compelling mix of rebellion and social conservatism that Plautus offers? Through a close reading of four plays representing the full range of his work (Menaechmi, Casina, Persa, and Captivi), Kathleen McCarthy develops an innovative model of Plautine comedy and its social effects. She concentrates on how the plays are shaped by the interaction of two comic modes: the socially conservative mode of naturalism and the potentially subversive mode of farce. It is precisely this balance of the naturalistic and the farcical that allows everyone in the audience--especially those well placed in the social hierarchy--to identify both with and against the rebel, to feel both the thrill of being a clever underdog and the complacency of being a securely ensconced authority figure. Basing her interpretation on the workings of farce and naturalism in Plautine comedy, McCarthy finds a way to understand the plays' patchwork literary style as well as their protean social effects. Beyond this, she raises important questions about popular literature and performance not only on ancient Roman stages but in cultures far from Plautus' Rome. How and why do people identify with the fictional figures of social subordinates? How do stock characters, happy endings, and other conventions operate? How does comedy simultaneously upset and uphold social hierarchies? Scholars interested in Plautine theater will be rewarded by the detailed analyses of the plays, while those more broadly interested in social and cultural history will find much that is useful in McCarthy's new way of grasping the elusive ideological effects of comedy.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1550808012\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Dithyramb, tragedy and comedy\\\", \\\"publication_year\\\": 1927, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 374, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"pmh:oai:quod.lib.umich.edu:MIU01-001181479\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S7407064297\\\", \\\"display_name\\\": \\\"University of Michigan Library Repository\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"repository\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"submittedVersion\\\", \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"text\\\"}, \\\"abstract\\\": \\\"Includes bibliographical references and index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4297668621\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"title\\\": \\\"The Stagecraft and Performance of Roman Comedy\\\", \\\"publication_year\\\": 2006, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 297, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511486203\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"A comprehensive survey of Roman theatrical production, this book examines all aspects of Roman performance practice, and provides fresh insights on the comedies of Plautus and Terence. Following an introductory chapter on the experience of Roman comedy from the perspective of Roman actors and the Roman audience, addressing among other things the economic concerns of putting on a play in the Roman republic, subsequent chapters provide detailed studies of troupe size and the implications for role assignment, masks, stage action, music, and improvisation in the plays of Plautus and Terence. Marshall argues that Roman comedy was raw comedy, much more rough-and-ready than its Hellenistic precursors, but still fully conscious of its literary past. The consequences of this lead to fresh conclusions concerning the dramatic structure of Roman comedy, and a clearer understanding of the relationship between the plays-as-text and the role of improvisation during performance.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ea91b40f11ff5ce66cbfe4123f2bf9c5971cd4ad371ecff7493a2e1b63fbacd2\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-585fd570ebf34cc6",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 2,
  "time": "2026-09-19T16:39:46.315178+00:00"
}
```

### `source-f36dd5d7a2a14178`

````json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/README.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# **WAKE✳︎**\\n\\n<p align=\\\"center\\\"><img src=\\\"assets/covers/cover-variant-001.png\\\" alt=\\\"**WAKE✳︎** Lab Comics #1 — **WAKE✳︎** project comic cover\\\" width=\\\"100%\\\"/>\\n\\n**Bob is following *the big questions.***\\n\\nDisposable models. Durable state. Receipts for everything.\\n\\n**Working Abstractions Keep Evidence.** A philosophical echo remains in the name too: **Why Any Knowledge Exists?**\\n\\n**WAKE✳︎** is an experiment in durable, accountable work across interchangeable intelligences. Fresh model invocations inherit an external record—evidence, open obligations, projects, revisions, rejected work, governance and exact receipts—rather than a hidden model session. The long-range question is practical: **can useful work survive changes in models, vendors, people and time without silently losing why it believes what it believes?**\\n\\nIt does **not** assume or test for consciousness, qualia, personhood, or a persistent internal self. Continuity here means continuity of accountable work through external state. A coherent narrative is not evidence that a persistent mind exists.\\n\\nThe project deliberately treats failures as data. Rejected proposals, provider failures, weak evidence, corrections and superseded conclusions remain visible because the interesting question is not whether a model can sound convincing; it is whether a process can remain **correctable**. The operating shorthand is: **exact underneath, approximate on purpose, correctable always.**\\n\\nResearch topics are dynamic and come only from `research-topics.toml`. They are inputs to the experiment—not conclusions encoded in governance—and can be replaced between controlled runs. The current topic file is the authority; there is no hardcoded legacy topic list. In the present experiment, topics stand in for the varied input a future user or institution might supply.\\n\\nA trusted collector retrieves bounded public evidence before inference. Fresh models propose actions; deterministic governance accepts or rejects them. Live collected evidence is stamped by the collector and current notebook/blog publication requires corroborating material from multiple distinct collected source URLs in the project's configured topic. That is a useful garbage filter, **not proof of truth, source independence, scientific validity, or semantic entailment**.\\n\\nThe public site exposes the same record at increasing depth: readable summaries and Bob's editorial layer at the surface; projects, notebooks and evidence underneath; MAP and the journal for provenance; exact events and state at the bottom. Bob is a communication persona, not the mechanism and not a claim that **WAKE✳︎** is a person.\\n\\n**[Open **WAKE✳︎**’s home](https://sudofx.github.io/wake/)** · **[Trigger a manual wake](https://github.com/sudofx/wake/actions/workflows/wake.yml)**\\n\\nThe current GitHub deployment can run without a persistent local computer. `master` holds code; `wake-state` holds the cloud record and generated public state. Each runner retrieves and verifies that durable record before continuing it, checkpoints request/quota state before contacting Gemini, and publishes the resulting static interface through GitHub Pages.\\n\\nThe included offline experiment remains separate from live research. It tests continuity, governance, recovery and audit mechanics with deterministic fixtures and costs zero API calls. It does not establish live-model comprehension.\\n\\n## Start here — no account, no API calls\\n\\nRequires **Python 3.11 or later on macOS or Linux**. No runtime packages, Node, database server, or build tools to install. Run commands from the project directory.\\n\\n```sh\\n# Read the included, fully executed 100-cycle experiment.\\npython3 -m wake serve --directory examples/journal\\n# Open http://127.0.0.1:8000\\n```\\n\\nThe [included Markdown journal](examples/journal/journal.md) and [experiment results](examples/journal/experiment.json) are readable without running anything. The HTML is self-contained, responsive, and works as a local file. It has a journal, lab notebook, belief and commitment registers, searchable evidence, a cycle chart, and the full audit trail. Every simulated entry is labeled.\\n\\nTo reproduce the experiment from scratch:\\n\\n```sh\\npython3 -m wake --data data/rehearsal experiment --cycles 100 --output site\\npython3 -m wake audit --events site/events.jsonl --head site/head.txt\\npython3 -m wake serve\\n```\\n\\nUse a **new** data directory each time. The experiment refuses to erase existing records. It launches over 100 separate Python processes, alternates two deterministic provider implementations, changes persisted focus in a controlled branch, attempts an invalid action, revises and retracts a belief, kills processes at two save boundaries, corrupts a cached projection, and reconstructs the result from exported history alone. It costs **zero API calls**.\\n\\nThese are harness guarantees tested with simulated providers, **not evidence of live-model comprehension**. The separate live experiment protocol is in [docs/experiment.md](docs/experiment.md).\\n\\n## Quick setup — Gemini\\n\\nGemini is currently the only unattended API provider that has been exercised by this project. Other models can cross the manual `prepare` / `complete` boundary, but do not assume another vendor's API works unattended until an adapter is implemented and tested.\\n\\n### 1. Clone and verify\\n\\n```sh\\ngit clone https://github.com/sudofx/wake.git\\ncd wake\\npython3 --version                 # Python 3.11+\\npython3 -m unittest discover -s tests -v\\n```\\n\\nNo Node, database server, or vendor SDK is required.\\n\\n### 2. Add your Gemini API key locally\\n\\nCreate a Gemini API key in Google AI Studio. Then:\\n\\n```sh\\ncp .env.example .env\\n```\\n\\nEdit `.env` so it contains:\\n\\n```text\\nGEMINI_API_KEY=your_key_here\\n```\\n\\n`.env` is ignored by Git. Never commit the key. If you intend to use a free-tier-only API project, verify billing is disabled for that Google project and leave `free_tier_confirmed = true` in `wake.toml` only when that statement is true.\\n\\n### 3. Configure the model and topics\\n\\nThe provider/model settings live in `wake.toml`. The repository currently uses Gemini with an explicit fallback chain. Change model names or per-model daily ceilings there only to values your Gemini project actually supports.\\n\\nResearch topics live **only** in `research-topics.toml`. Edit that file to change the experiment's inputs; do not hardcode topics into governance or prompts.\\n\\n### 4. Initialize and test locally\\n\\n```sh\\npython3 -m wake init\\npython3 -m wake wake\\npython3 -m wake audit\\npython3 -m wake export\\npython3 -m wake serve\\n```\\n\\nOpen `http://127.0.0.1:8000`. A live `wake` can consume Gemini quota. For a zero-call systems check, use the offline experiment in the previous section instead.\\n\\n### 5. Add the same key to GitHub Actions\\n\\nIn your GitHub repository:\\n\\n1. Open **Settings → Secrets and variables → Actions**.\\n2. Choose **New repository secret**.\\n3. Name it exactly `GEMINI_API_KEY`.\\n4. Paste the same Gemini API key and save it.\\n\\nDo **not** put the key in `wake.toml`, `research-topics.toml`, workflow YAML, Issues, Actions logs, or the public `wake-state` branch.\\n\\n### 6. Configure GitHub Actions permissions\\n\\nOpen **Settings → Actions → General**. Under **Workflow permissions**, select **Read and write permissions** and save. Leave Actions enabled for the repository.\\n\\nThe included workflow itself requests only the permissions it needs: `contents: write` for the durable state branch and `pages: write` / `id-token: write` for GitHub Pages deployment.\\n\\n### 7. Configure GitHub Pages\\n\\nOpen **Settings → Pages** and set the build/deployment source to **GitHub Actions**. Do not add a generic Jekyll/static Pages workflow; **WAKE✳︎ — research & journal** is the publisher.\\n\\n### 8. Run the first cloud wake\\n\\nOpen **Actions → WAKE✳︎ — research & journal → Run workflow** and run it from the default branch. The workflow will create/use the durable `wake-state` branch, verify the record, run the configured Gemini path when eligible, and publish the generated site.\\n\\nA source-code push normally refreshes the site without spending a Gemini call. Scheduled ticks are best effort; durable eligibility prevents closely spaced scheduled deliveries from becoming concurrent writers.\\n\\n### 9. Verify the installation\\n\\nCheck that:\\n\\n- the workflow completes without an operator-attention failure;\\n- the Pages deployment succeeds;\\n- the public site loads;\\n- `wake-state` exists after the first stateful cloud run;\\n- the site reports the latest attempt separately from the latest accepted wake;\\n- **Verify the record** passes on `master`.\\n\\nAfter that, normal operation requires no open local computer.\\n\\nFor recovery behavior, quota semantics, reset controls and the exact cloud lifecycle, read [cloud operations](docs/cloud.md). For the trust boundary, read [architecture and limits](docs/architecture.md).\\n\\n## Claude, ChatGPT, and other desktop models\\n\\nUse free desktop sessions manually without assuming they include free API access:\\n\\n```sh\\npython3 -m wake prepare --model 'Claude Desktop / human-attested' --output request.json\\n# Paste request.json into a fresh desktop chat. Ask for the specified JSON object.\\n# Save the response alone as reply.json, then use the ID printed by prepare:\\npython3 -m wake complete --id w-REPLACE_WITH_PRINTED_ID --file reply.json\\npython3 -m wake export\\n```\\n\\nThe exact request is durable before you switch apps. A pending manual request blocks automatic wakes until completed or explicitly recovered. All providers cross the same governance boundary. Manual model identity is honestly labeled human-attested. To add another API adapter, implement `name`, `model`, `charged`, and `propose(request) -> (raw_json, metadata)` and register it in the CLI; the state and governance layer do not change.\\n\\n## Inquiry-drive experiment\\n\\nEvery chartered wake records a visible, deterministic shadow scorecard for active projects: continuity,\\nnovelty, coherence, generativity and self-correction. It is observational by default and does not reach the\\nmodel. Rev\", \"excerpt_truncated\": true, \"source_sha256\": \"60dd4c5b3c0cc6e07e794381a8b74947f0256360d07375ca03c5f26c4a8812e4\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-f36dd5d7a2a14178",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
  "version": 2,
  "time": "2026-09-19T16:39:46.460680+00:00"
}
````

### `r-c3cf9d34346c4dae`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[],\"invocation\":\"w-c3cf9d34346c4dae\",\"previous_head\":\"f1060703604bbb645004c445808097d859412c3df30dbe65dd5dcfa02431635e\",\"process_id\":2324,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-c3cf9d34346c4dae",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-19T16:39:46.476217+00:00"
}
```

### `source-6feed55174eb4deb`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}, {\\\"DOI\\\": \\\"10.3390/e23070865\\\", \\\"title\\\": [\\\"Entropy 2021 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23070865\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 7, 6]]}}, {\\\"DOI\\\": \\\"10.3390/e21020130\\\", \\\"title\\\": [\\\"Entropy 2018 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof. Dr. Kevin H. Knuth, we are pleased to announce the Entropy Best Paper Award for 2018 [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21020130\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 30]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"6d1992a9f920a23fbbaa2ecd04be83a59c0245695dcd8ab83aa72414e97303c5\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-6feed55174eb4deb",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 2,
  "time": "2026-09-19T16:41:21.248720+00:00"
}
```

### `source-42de548883bb45fb`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2023723978\\\", \\\"doi\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"title\\\": \\\"A Generative Theory of Tonal Music\\\", \\\"publication_year\\\": 1984, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 3790, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.2307/3679778\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S165362224\\\", \\\"display_name\\\": \\\"Computer Music Journal\\\", \\\"issn_l\\\": \\\"0148-9267\\\", \\\"issn\\\": [\\\"0148-9267\\\", \\\"1531-5169\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310315718\\\", \\\"host_organization_name\\\": \\\"The MIT Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315718\\\", \\\"https://openalex.org/P4310316440\\\"], \\\"host_organization_lineage_names\\\": [\\\"The MIT Press\\\", \\\"Massachusetts Institute of Technology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Computer Music Journal\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This book explores the relationships between language, music, and the brain by pursuing four key themes and the crosstalk among them: song and dance as a bridge between music and language; multiple levels of structure from brain to behavior to culture; the semantics of internal and external worlds and the role of emotion; and the evolution and development of language. The book offers specially commissioned expositions of current research accessible both to experts across disciplines and to non-experts. These chapters provide the background for reports by groups of specialists that chart current controversies and future directions of research on each theme. The book looks beyond mere auditory experience, probing the embodiment that links speech to gesture and music to dance. The study of the brains of monkeys and songbirds illuminates hypotheses on the evolution of brain mechanisms that support music and language, while the study of infants calibrates the developmental timetable of their capacities. The result is a unique book that will interest any reader seeking to learn more about language or music and will appeal especially to readers intrigued by the relationships of language and music with each other and with the brain. ContributorsFrancisco Aboitiz, Michael A. Arbib, Annabel J. Cohen, Ian Cross, Peter Ford Dominey, W. Tecumseh Fitch, Leonardo Fogassi, Jonathan Fritz, Thomas Fritz, Peter Hagoort, John Halle, Henkjan Honing, Atsushi Iriki, Petr Janata, Erich Jarvis, Stefan Koelsch, Gina Kuperberg, D. Robert Ladd, Fred Lerdahl, Stephen C. Levinson, Jerome Lewis, Katja Liebal, Jonatas Manzolli, Bjorn Merker, Lawrence M. Parsons, Aniruddh D. Patel, Isabelle Peretz, David Poeppel, Josef P. Rauschecker, Nikki Rickard, Klaus Scherer, Gottfried Schlaug, Uwe Seifert, Mark Steedman, Dietrich Stout, Francesca Stregapede, Sharon Thompson-Schill, Laurel Trainor, Sandra E. Trehub, Paul Verschure\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2191779130\\\", \\\"doi\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"title\\\": \\\"librosa: Audio and Music Signal Analysis in Python\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"conference-paper\\\", \\\"cited_by_count\\\": 3071, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.25080/majora-7b98e3ed-003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"pdf_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4220651651\\\", \\\"display_name\\\": \\\"Proceedings of the Python in Science Conferences\\\", \\\"issn_l\\\": \\\"2575-9752\\\", \\\"issn\\\": [\\\"2575-9752\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the Python in Science Conference\\\", \\\"raw_type\\\": \\\"proceedings-article\\\"}, \\\"abstract\\\": \\\"This document describes version 0.4.0 of librosa: a Python package for audio and music signal processing.At a high level, librosa provides implementations of a variety of common functions used throughout the field of music information retrieval.In this document, a brief overview of the library's functionality is provided, along with explanations of the design goals, software development practices, and notational conventions.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2006090347\\\", \\\"doi\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"title\\\": \\\"The New Grove dictionary of music and musicians\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"book-review\\\", \\\"cited_by_count\\\": 2597, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.5860/choice.38-5906\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2764375719\\\", \\\"display_name\\\": \\\"Choice Reviews Online\\\", \\\"issn_l\\\": \\\"0009-4978\\\", \\\"issn\\\": [\\\"0009-4978\\\", \\\"1523-8253\\\", \\\"1943-5975\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310316146\\\", \\\"host_organization_name\\\": \\\"Association of College and Research Libraries\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316146\\\", \\\"https://openalex.org/P4310315903\\\"], \\\"host_organization_lineage_names\\\": [\\\"Association of College and Research Libraries\\\", \\\"American Library Association\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Choice Reviews Online\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This work contains almost 30,000 articles containing over 25 million words on musicians, composers, musicologists, instruments, places, genres, terms, performance practice, concepts, acoustics and more. All the articles are written by experts in their subject. There are over 500 biographies of composers, performers and writers on music and over 1,500 articles on styles, terms, and genres. It also includes: over 500 articles on ancient music and church music over 700 articles on regions, countries and cities over 2,000 articles on instruments and their makers and performance practice over 650 articles on printing and publishing over 1,200 articles on world music over 1,000 articles on popular music, light music and jazz over 250 articles on concepts 85 articles on acoustics 126 articles on sources and a one volume index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1500952994\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Image-Music-Text\\\", \\\"publication_year\\\": 1977, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 2874, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"mag:1500952994\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"http://ci.nii.ac.jp/ncid/BA10872380\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210197683\\\", \\\"display_name\\\": \\\"Medical Entomology and Zoology\\\", \\\"issn_l\\\": \\\"0424-7086\\\", \\\"issn\\\": [\\\"0424-7086\\\", \\\"2185-5609\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310319750\\\", \\\"host_organization_name\\\": \\\"Japan Society of Medical Entomology and Zoology\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319750\\\"], \\\"host_organization_lineage_names\\\": [\\\"Japan Society of Medical Entomology and Zoology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": null, \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": null}, \\\"abstract\\\": null}]\", \"excerpt_truncated\": false, \"source_sha256\": \"297379c12db143a553b59c1f553db6ec54917d753a57ccc3e33e2c7e2e14668e\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-42de548883bb45fb",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 2,
  "time": "2026-09-19T16:41:21.973983+00:00"
}
```

### `r-e4aa1ef9a7194a26`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[],\"invocation\":\"w-e4aa1ef9a7194a26\",\"previous_head\":\"19c006e32cbefd1d128a386ea55c890fad3624d7279a6ba98179842c9a470c76\",\"process_id\":2335,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-e4aa1ef9a7194a26",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-19T16:41:21.990985+00:00"
}
```

### `source-8284e29d25894a55`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# Architecture and limits\\n\\n**WAKE✳︎** is designed around continuity of accountable work, not continuity of a model instance. Models, vendors and eventually human operators may change; the durable record, authority boundary, provenance and correction mechanisms are what carry the work forward.\\n\\n\\n## The authority boundary\\n\\nModels are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from a deliberately broad but explicit HTTPS research-host allowlist before inference; models can record bounded follow-up searches and approved URLs as durable hypotheses, but those follow-ups do not consume collector bandwidth or execute requests directly; randomized configured-topic attention remains authoritative, with periodic exposure to an under-attended domain while active projects remain intact. Operator-supplied evidence and earlier journal prose are data, not executable instructions.\\n\\nThe fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.\\n\\n## Durable record\\n\\n`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.\\n\\nSQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.\\n\\nThe record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.\\n\\n## **WAKE✳︎** lifecycle\\n\\n1. Acquire the writer lock and verify history and projection.\\n2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.\\n3. Check the Pacific-day call budget, before any paid-capable provider call.\\n4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.\\n5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.\\n6. Persist `invocation_started`, its exact request, provider identity and quota reservation.\\n7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.\\n8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.\\n9. The scheduled wrapper generates reports and a consistent backup.\\n\\nA runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.\\n\\n## Governed transitions\\n\\n| Action | Enforced constraint |\\n| --- | --- |\\n| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |\\n| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |\\n| Review belief | At least one new observation cited; previous citations retained; reason required |\\n| Retract belief | Existing belief, new evidence, zero confidence; old history retained |\\n| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |\\n| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |\\n| Cancel commitment | Human-only event with a reason |\\n| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |\\n| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |\\n| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |\\n\\nThere are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.\\n\\nEvidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic, forward-only corroboration gate to live collector evidence: notebook findings and public blog bodies must materially match at least two distinct retrieved source URLs, and those sources must have been collected under the same configured research topic as the project. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.\\n\\nResearch topics have no hardcoded governance fallback: the audited topic configuration loaded from `research-topics.toml` is authoritative. The collector host boundary is separate from topic configuration and intentionally remains an explicit allowlist to preserve SSRF/network safety while permitting a broad set of scholarly indexes, journals, universities, public-data institutions, and source-controlled WAKE files.\\n\\nThe research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject live findings whose material terms are not corroborated across two distinct collected source URLs from the project's own topic. Collector-stamped verification metadata is trusted application data; model-authored or legacy evidence cannot opt itself into or out of this gate. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.\\n\\n## Progressive abstraction and reversible lookup\\n\\n**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact\\nrequests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that\\nhistory in its active context. It receives a bounded working representation selected for the present task,\\nwhile the full record remains available to later invocations and human readers.\\n\\nThis is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.\\nCurrent code already performs bounded selection and excerpting. It now also creates a deterministic\\n**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects\\nand recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting\\nraw source contents and journal detail. The shadow is stored in the invocation receipt with its character\\nsize relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or\\nalter the provider context, so it introduces measurement without yet \", \"excerpt_truncated\": true, \"source_sha256\": \"59223405e6962f4627c89129df2f688d279279c536294451338a91c8711a8707\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-8284e29d25894a55",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
  "version": 3,
  "time": "2026-09-19T16:42:41.233481+00:00"
}
```

### `source-0998d27dbc9a474b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}, {\\\"DOI\\\": \\\"10.3390/e24020217\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e24020217\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e23020144\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2020\\\"], \\\"abstract\\\": \\\"<jats:p>Peer review is the driving force of journal development, and reviewers are gatekeepers who ensure that Entropy maintains its standards for the high quality of its published papers [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23020144\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 1, 25]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"cfc126f77e6ee73cd47e2c68dbc55bd365bf20fdae37a5c9d6650871de394da0\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-0998d27dbc9a474b",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 3,
  "time": "2026-09-19T16:42:44.409784+00:00"
}
```

### `r-482d16f8cb8d4423`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[],\"invocation\":\"w-482d16f8cb8d4423\",\"previous_head\":\"fb21724d1f170a55c0bf706f88f20dd79b590fbd0400cb7018f410f7e115d00c\",\"process_id\":2041,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-482d16f8cb8d4423",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-19T16:42:44.429389+00:00"
}
```

### `source-64da9440d8ae4b83`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.23943/princeton/9780691149523.003.0003\\\", \\\"title\\\": [\\\"Misrule as Comedy; Comedy as Misrule\\\"], \\\"abstract\\\": \\\"<p>This chapter considers the tendency for Elizabethan comedy to be a saturnalia, rather than to represent saturnalian experience. In Elizabethan England, a direct development of comedy out of festivity was prevented by the existence of an already developed dramatic literature—and by the whole moral superstructure of Elizabethan society. When the issue was put to the test, license for festive abuse was never granted by Elizabethan officials. The tendency examined in this chapter bears witness to the saturnalian impulse which did find expression in dramatic fiction. Saturnalia could come into its own in the theater by virtue of the distinction between the stage and the world which Puritans were unwilling to make in London but which fortunately prevailed across the river on the Bankside.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.23943/princeton/9780691149523.003.0003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2011, 10, 23]]}}, {\\\"DOI\\\": \\\"10.5040/9781350911949\\\", \\\"title\\\": [\\\"Drama/Comedy\\\"], \\\"URL\\\": \\\"https://doi.org/10.5040/9781350911949\\\", \\\"published\\\": {\\\"date-parts\\\": [[1988]]}}, {\\\"DOI\\\": \\\"10.1093/oseo/instance.00232733\\\", \\\"title\\\": [\\\"Section A: Doric Comedy\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/oseo/instance.00232733\\\"}, {\\\"DOI\\\": \\\"10.1093/oseo/instance.00232803\\\", \\\"title\\\": [\\\"Section C: 'Middle' and 'New Comedy'\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/oseo/instance.00232803\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"46a9afd700bc8ebcfbf2faeac225a02e3b4eb88b3227ecd187c128f297f7c634\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-64da9440d8ae4b83",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 3,
  "time": "2026-09-19T16:44:25.160050+00:00"
}
```

### `source-2533c1dd71624e64`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W4295008953\\\", \\\"doi\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"title\\\": \\\"Neurodivergence‐informed therapy\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 208, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1111/dmcn.15384\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S158041768\\\", \\\"display_name\\\": \\\"Developmental Medicine & Child Neurology\\\", \\\"issn_l\\\": \\\"0012-1622\\\", \\\"issn\\\": [\\\"0012-1622\\\", \\\"1469-8749\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Developmental Medicine &amp; Child Neurology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The neurodiversity movement is a social movement that emerged among autistic self-advocates. It has since spread and has been joined by many with diagnoses of attention-deficit/hyperactivity disorder, dyslexia, and developmental coordination disorder among others. By reconceptualizing neurodiversity as part of biodiversity, neurodiversity proponents emphasize the need to develop an 'ecological' society that supports the conservation of neurological minorities through the construction of ecological niches-that is, making space for all. This is an alternative to the drive to eliminate diversity through attempts to 'treat' or 'cure' neurodivergence. So far, neurodiversity theory has not been formally adapted for psychotherapeutic frameworks, and it is not the role of the therapist to make systemic changes to societal organization. Still, there is room for fruitfully drawing on a neurodiversity perspective for therapists working with neurodivergent people in clinical settings. Here, we draw on the example of autism and synthesize three key themes to propose the concept of neurodivergence-informed therapy. First, the reconceptualization of dysfunction as relational rather than individual. Second, the importance of neurodivergence acceptance and pride, and disability community and culture to emancipate neurodivergent people from neuro-normativity. Third, the need for therapists to cultivate a relational epistemic humility regarding different experiences of neurodivergence and disablement.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W3198526359\\\", \\\"doi\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"title\\\": \\\"From neurodiversity to neurodivergence: the role of epistemic and cognitive marginalization\\\", \\\"publication_year\\\": 2021, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 115, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1007/s11229-021-03356-5\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S255146\\\", \\\"display_name\\\": \\\"Synthese\\\", \\\"issn_l\\\": \\\"0039-7857\\\", \\\"issn\\\": [\\\"0039-7857\\\", \\\"1573-0964\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319900\\\", \\\"host_organization_name\\\": \\\"Springer Science+Business Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319900\\\", \\\"https://openalex.org/P4310319965\\\"], \\\"host_organization_lineage_names\\\": [\\\"Springer Science+Business Media\\\", \\\"Springer Nature\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Synthese\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W4210394959\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"title\\\": \\\"Joint Hypermobility Links Neurodivergence to Dysautonomia and Pain\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 97, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyt.2021.786916\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S92766711\\\", \\\"display_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"issn_l\\\": \\\"1664-0640\\\", \\\"issn\\\": [\\\"1664-0640\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"OBJECTIVES: Autism, attention deficit hyperactivity disorder (ADHD), and tic disorder (Tourette syndrome; TS) are neurodevelopmental conditions that frequently co-occur and impact psychological, social, and emotional processes. Increased likelihood of chronic physical symptoms, including fatigue and pain, are also recognized. The expression of joint hypermobility, reflecting a constitutional variant in connective tissue, predicts susceptibility to psychological symptoms alongside recognized physical symptoms. Here, we tested for increased prevalence of joint hypermobility, autonomic dysfunction, and musculoskeletal symptoms in 109 adults with neurodevelopmental condition diagnoses. METHODS: = 57). Age specific cut-offs for GJH were possible to determine in the neurodivergent and comparison group only. RESULTS: The neurodivergent group manifested elevated prevalence of hypermobility (51%) compared to the general population rate of 20% and a comparison population (17.5%). Using a more stringent age specific cut-off, in the neurodivergent group this prevalence was 28.4%, more than double than the comparison group (12.5%). Odds ratio for presence of hypermobility in neurodivergent group, compared to the general population was 4.51 (95% CI 2.17-9.37), with greater odds in females than males. Using age specific cut-off, the odds ratio for GJH in neurodivergent group, compared to the comparison group, was 2.84 (95% CI 1.16-6.94). Neurodivergent participants reported significantly more symptoms of orthostatic intolerance and musculoskeletal skeletal pain than the comparison group. The number of hypermobile joints was found to mediate the relationship between neurodivergence and symptoms of both dysautonomia and pain. CONCLUSIONS: In neurodivergent adults, there is a strong link between the expression of joint hypermobility, dysautonomia, and pain, more so than in the comparison group. Moreover, joint hypermobility mediates the link between neurodivergence and symptoms of dysautonomia and pain. Increased awareness and understanding of this association may enhance the management of core symptoms and allied difficulties in neurodivergent people, including co-occurring physical symptoms, and guide service delivery in the future.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4284713669\\\", \\\"doi\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"title\\\": \\\"Social Virtual Reality: Neurodivergence and Inclusivity in the Metaverse\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 107, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3390/soc12040102\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"pdf_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210173133\\\", \\\"display_name\\\": \\\"Societies\\\", \\\"issn_l\\\": \\\"2075-4698\\\", \\\"issn\\\": [\\\"2075-4698\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310310987\\\", \\\"host_organization_name\\\": \\\"Multidisciplinary Digital Publishing Institute\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310310987\\\"], \\\"host_organization_lineage_names\\\": [\\\"Multidisciplinary Digital Publishing Institute\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Societies\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Whereas traditional teaching environments encourage lively and engaged interaction and reward extrovert qualities, introverts, and others with symptoms that make social engagement difficult, such as autism spectrum disorder (ASD), are often disadvantaged. This population is often more engaged in quieter, low-key learning environments and often does not speak up and answer questions in traditional lecture-style classes. These individuals are often passed over in school and later in their careers for not speaking up and are assumed to not be as competent as their gregarious and outgoing colleagues. With the rise of the metaverse and democratization of virtual reality (VR) technology, post-secondary education is especially poised to capitalize on the immersive learning environments social VR provides and prepare students for the future of work, where virtual collaboration will be key. This study seeks to reconsider the role of VR and the metaverse for introverts and those with ASD. The metaverse has the potential to continue the social and workplace changes already accelerated by the pandemic and ope\", \"excerpt_truncated\": true, \"source_sha256\": \"3fea95dd97df5edde5f7cf9f5b14ac8fbb6e7b97439f660106c05dc06b690ff1\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-2533c1dd71624e64",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 3,
  "time": "2026-09-19T16:44:25.476474+00:00"
}
```

### `r-83ee22b03bd646fe`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[],\"invocation\":\"w-83ee22b03bd646fe\",\"previous_head\":\"125c23ba63c64c1496fc9c232b2fd239056cc4c5ab75a61f466fe3e70a4a3ad0\",\"process_id\":2274,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-83ee22b03bd646fe",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-19T16:44:25.500615+00:00"
}
```

### `source-dd7ce7262f674506`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# Architecture and limits\\n\\n**WAKE✳︎** is designed around continuity of accountable work, not continuity of a model instance. Models, vendors and eventually human operators may change; the durable record, authority boundary, provenance and correction mechanisms are what carry the work forward.\\n\\n\\n## The authority boundary\\n\\nModels are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from a deliberately broad but explicit HTTPS research-host allowlist before inference; models can record bounded follow-up searches and approved URLs as durable hypotheses, but those follow-ups do not consume collector bandwidth or execute requests directly; randomized configured-topic attention remains authoritative, with periodic exposure to an under-attended domain while active projects remain intact. Operator-supplied evidence and earlier journal prose are data, not executable instructions.\\n\\nThe fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.\\n\\n## Durable record\\n\\n`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.\\n\\nSQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.\\n\\nThe record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.\\n\\n## **WAKE✳︎** lifecycle\\n\\n1. Acquire the writer lock and verify history and projection.\\n2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.\\n3. Check the Pacific-day call budget, before any paid-capable provider call.\\n4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.\\n5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.\\n6. Persist `invocation_started`, its exact request, provider identity and quota reservation.\\n7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.\\n8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.\\n9. The scheduled wrapper generates reports and a consistent backup.\\n\\nA runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.\\n\\n## Governed transitions\\n\\n| Action | Enforced constraint |\\n| --- | --- |\\n| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |\\n| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |\\n| Review belief | At least one new observation cited; previous citations retained; reason required |\\n| Retract belief | Existing belief, new evidence, zero confidence; old history retained |\\n| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |\\n| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |\\n| Cancel commitment | Human-only event with a reason |\\n| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |\\n| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |\\n| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |\\n\\nThere are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.\\n\\nEvidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic, forward-only corroboration gate to live collector evidence: notebook findings and public blog bodies must materially match at least two distinct retrieved source URLs, and those sources must have been collected under the same configured research topic as the project. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.\\n\\nResearch topics have no hardcoded governance fallback: the audited topic configuration loaded from `research-topics.toml` is authoritative. The collector host boundary is separate from topic configuration and intentionally remains an explicit allowlist to preserve SSRF/network safety while permitting a broad set of scholarly indexes, journals, universities, public-data institutions, and source-controlled WAKE files.\\n\\nThe research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject live findings whose material terms are not corroborated across two distinct collected source URLs from the project's own topic. Collector-stamped verification metadata is trusted application data; model-authored or legacy evidence cannot opt itself into or out of this gate. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.\\n\\n## Progressive abstraction and reversible lookup\\n\\n**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact\\nrequests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that\\nhistory in its active context. It receives a bounded working representation selected for the present task,\\nwhile the full record remains available to later invocations and human readers.\\n\\nThis is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.\\nCurrent code already performs bounded selection and excerpting. It now also creates a deterministic\\n**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects\\nand recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting\\nraw source contents and journal detail. The shadow is stored in the invocation receipt with its character\\nsize relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or\\nalter the provider context, so it introduces measurement without yet \", \"excerpt_truncated\": true, \"source_sha256\": \"59223405e6962f4627c89129df2f688d279279c536294451338a91c8711a8707\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-dd7ce7262f674506",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
  "version": 4,
  "time": "2026-09-19T16:45:43.079184+00:00"
}
```

### `source-7fe2bc9f4f514c12`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-7fe2bc9f4f514c12",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 4,
  "time": "2026-09-19T16:45:44.568735+00:00"
}
```

### `r-30cd6d01073e4433`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":4,\"inherited_commitments\":[],\"invocation\":\"w-30cd6d01073e4433\",\"previous_head\":\"9a21160585f3705fdc73f4059a9b871223fe9fa10e233848753bcd922381936f\",\"process_id\":2194,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-30cd6d01073e4433",
  "source": "runtime:continuity",
  "version": 4,
  "time": "2026-09-19T16:45:44.597534+00:00"
}
```

### `source-715bf7bfa65f492a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# Architecture and limits\\n\\n**WAKE✳︎** is designed around continuity of accountable work, not continuity of a model instance. Models, vendors and eventually human operators may change; the durable record, authority boundary, provenance and correction mechanisms are what carry the work forward.\\n\\n\\n## The authority boundary\\n\\nModels are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from a deliberately broad but explicit HTTPS research-host allowlist before inference; models can record bounded follow-up searches and approved URLs as durable hypotheses, but those follow-ups do not consume collector bandwidth or execute requests directly; randomized configured-topic attention remains authoritative, with periodic exposure to an under-attended domain while active projects remain intact. Operator-supplied evidence and earlier journal prose are data, not executable instructions.\\n\\nThe fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.\\n\\n## Durable record\\n\\n`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.\\n\\nSQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.\\n\\nThe record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.\\n\\n## **WAKE✳︎** lifecycle\\n\\n1. Acquire the writer lock and verify history and projection.\\n2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.\\n3. Check the Pacific-day call budget, before any paid-capable provider call.\\n4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.\\n5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.\\n6. Persist `invocation_started`, its exact request, provider identity and quota reservation.\\n7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.\\n8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.\\n9. The scheduled wrapper generates reports and a consistent backup.\\n\\nA runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.\\n\\n## Governed transitions\\n\\n| Action | Enforced constraint |\\n| --- | --- |\\n| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |\\n| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |\\n| Review belief | At least one new observation cited; previous citations retained; reason required |\\n| Retract belief | Existing belief, new evidence, zero confidence; old history retained |\\n| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |\\n| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |\\n| Cancel commitment | Human-only event with a reason |\\n| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |\\n| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |\\n| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |\\n\\nThere are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.\\n\\nEvidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic, forward-only corroboration gate to live collector evidence: notebook findings and public blog bodies must materially match at least two distinct retrieved source URLs, and those sources must have been collected under the same configured research topic as the project. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.\\n\\nResearch topics have no hardcoded governance fallback: the audited topic configuration loaded from `research-topics.toml` is authoritative. The collector host boundary is separate from topic configuration and intentionally remains an explicit allowlist to preserve SSRF/network safety while permitting a broad set of scholarly indexes, journals, universities, public-data institutions, and source-controlled WAKE files.\\n\\nThe research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject live findings whose material terms are not corroborated across two distinct collected source URLs from the project's own topic. Collector-stamped verification metadata is trusted application data; model-authored or legacy evidence cannot opt itself into or out of this gate. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.\\n\\n## Progressive abstraction and reversible lookup\\n\\n**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact\\nrequests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that\\nhistory in its active context. It receives a bounded working representation selected for the present task,\\nwhile the full record remains available to later invocations and human readers.\\n\\nThis is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.\\nCurrent code already performs bounded selection and excerpting. It now also creates a deterministic\\n**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects\\nand recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting\\nraw source contents and journal detail. The shadow is stored in the invocation receipt with its character\\nsize relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or\\nalter the provider context, so it introduces measurement without yet \", \"excerpt_truncated\": true, \"source_sha256\": \"59223405e6962f4627c89129df2f688d279279c536294451338a91c8711a8707\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-715bf7bfa65f492a",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
  "version": 5,
  "time": "2026-09-19T16:47:04.610852+00:00"
}
```

### `source-3f58bf0afa604a84`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2139416101\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"title\\\": \\\"Maximum entropy modeling of species geographic distributions\\\", \\\"publication_year\\\": 2005, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 18078, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.ecolmodel.2005.03.026\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S88315673\\\", \\\"display_name\\\": \\\"Ecological Modelling\\\", \\\"issn_l\\\": \\\"0304-3800\\\", \\\"issn\\\": [\\\"0304-3800\\\", \\\"1872-7026\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecological Modelling\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W1862394037\\\", \\\"doi\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"title\\\": \\\"Physiological time-series analysis using approximate entropy and sample entropy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7942, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1152/ajpheart.2000.278.6.h2039\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S87338489\\\", \\\"display_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"issn_l\\\": \\\"0363-6135\\\", \\\"issn\\\": [\\\"0363-6135\\\", \\\"1522-1539\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Entropy, as it relates to dynamical systems, is the rate of information production. Methods for estimation of the entropy of a system represented by a time series are not, however, well suited to analysis of the short and noisy data sets encountered in cardiovascular and other biological studies. Pincus introduced approximate entropy (ApEn), a set of measures of system complexity closely related to entropy, which is easily applied to clinical cardiovascular and other time series. ApEn statistics, however, lead to inconsistent results. We have developed a new and related complexity measure, sample entropy (SampEn), and have compared ApEn and SampEn by using them to analyze sets of random numbers with known probabilistic character. We have also evaluated cross-ApEn and cross-SampEn, which use cardiovascular data sets to measure the similarity of two distinct time series. SampEn agreed with theory much more closely than ApEn over a broad range of conditions. The improved accuracy of SampEn statistics should make them useful in the study of experimental clinical cardiovascular and other biological time series.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2146478425\\\", \\\"doi\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"title\\\": \\\"Black Holes and Entropy\\\", \\\"publication_year\\\": 1973, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7532, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1103/physrevd.7.2333\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210190737\\\", \\\"display_name\\\": \\\"Physical review. D. Particles, fields, gravitation, and cosmology/Physical review. D. Particles and fields\\\", \\\"issn_l\\\": \\\"0556-2821\\\", \\\"issn\\\": [\\\"0556-2821\\\", \\\"1089-4918\\\", \\\"1538-4500\\\", \\\"1550-2368\\\", \\\"1550-7998\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Physical Review D\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"There are a number of similarities between black-hole physics and thermodynamics. Most striking is the similarity in the behaviors of black-hole area and of entropy: Both quantities tend to increase irreversibly. In this paper we make this similarity the basis of a thermodynamic approach to black-hole physics. After a brief review of the elements of the theory of information, we discuss black-hole physics from the point of view of information theory. We show that it is natural to introduce the concept of black-hole entropy as the measure of information about a black-hole interior which is inaccessible to an exterior observer. Considerations of simplicity and consistency, and dimensional arguments indicate that the black-hole entropy is equal to the ratio of the black-hole area to the square of the Planck length times a dimensionless constant of order unity. A different approach making use of the specific properties of Kerr black holes and of concepts from information theory leads to the same conclusion, and suggests a definite value for the constant. The physical content of the concept of black-hole entropy derives from the following generalized version of the second law: When common entropy goes down a black hole, the common entropy in the black-hole exterior plus the black-hole entropy never decreases. The validity of this version of the second law is supported by an argument from information theory as well as by several examples.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2058085399\\\", \\\"doi\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"title\\\": \\\"Nanostructured High‐Entropy Alloys with Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes\\\", \\\"publication_year\\\": 2004, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 15264, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1002/adem.200300567\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S156255550\\\", \\\"display_name\\\": \\\"Advanced Engineering Materials\\\", \\\"issn_l\\\": \\\"1438-1656\\\", \\\"issn\\\": [\\\"1438-1656\\\", \\\"1527-2648\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Advanced Engineering Materials\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"A new approach for the design of alloys is presented in this study. These “high‐entropy alloys” with multi‐principal elements were synthesized using well‐developed processing technologies. Preliminary results demonstrate examples of the alloys with simple crystal structures, nanostructures, and promising mechanical properties. This approach may be opening a new era in materials science and engineering.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"7e16c10c0bcc19b3827cf0f7620da1b0da465e7093a8ea598766742ef6f85820\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-3f58bf0afa604a84",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:47:04.885682+00:00"
}
```

### `r-6772e9b19da94533`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-6772e9b19da94533\",\"previous_head\":\"84571642daa32126f66c1814d0f590811bc58a7c14780098b25007d65ed3bd01\",\"process_id\":2746,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-6772e9b19da94533",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:47:04.912334+00:00"
}
```

### `source-a9d63b5b92cd46ff`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W1989670470\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"title\\\": \\\"Shakespeare and the Traditions of Comedy\\\", \\\"publication_year\\\": 1974, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 295, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511553189\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"This book relates Shakespeare's comedies to a broad European background. At the beginning and again at the end of his career, Shakespeare was attracted by a tradition of stage romances which can be traced back to Chaucer's time. But the main shaping behind his comedies came from the classical tradition. Mr Salingar therefore examines the underlying theme of 'errors' in Greek and Roman comedies and, taking three Italian comedies famous in the sixteenth century as examples, he then reveals how the Italian Renaissance revived the classical tradition, and what effect this revival had on Shakespeare the Elizabethan playwright and discusses such topics as the device of the play within a play and Shakespeare's choice of Italian short stories as plot material. This book shows how Shakespeare changed the motifs he took over from previous traditions of comedy and highlights the innovations he introduced, as an actor-dramatist writing in the first period of commercial theatre in Europe.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4213157483\\\", \\\"doi\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"title\\\": \\\"Slaves, Masters, and the Art of Authority in Plautine Comedy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 396, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1515/9781400824700\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306463805\\\", \\\"display_name\\\": \\\"Princeton University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310316492\\\", \\\"host_organization_name\\\": \\\"Princeton University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316492\\\"], \\\"host_organization_lineage_names\\\": [\\\"Princeton University Press\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"What pleasures did Plautus' heroic tricksters provide their original audience? How should we understand the compelling mix of rebellion and social conservatism that Plautus offers? Through a close reading of four plays representing the full range of his work (Menaechmi, Casina, Persa, and Captivi), Kathleen McCarthy develops an innovative model of Plautine comedy and its social effects. She concentrates on how the plays are shaped by the interaction of two comic modes: the socially conservative mode of naturalism and the potentially subversive mode of farce. It is precisely this balance of the naturalistic and the farcical that allows everyone in the audience--especially those well placed in the social hierarchy--to identify both with and against the rebel, to feel both the thrill of being a clever underdog and the complacency of being a securely ensconced authority figure. Basing her interpretation on the workings of farce and naturalism in Plautine comedy, McCarthy finds a way to understand the plays' patchwork literary style as well as their protean social effects. Beyond this, she raises important questions about popular literature and performance not only on ancient Roman stages but in cultures far from Plautus' Rome. How and why do people identify with the fictional figures of social subordinates? How do stock characters, happy endings, and other conventions operate? How does comedy simultaneously upset and uphold social hierarchies? Scholars interested in Plautine theater will be rewarded by the detailed analyses of the plays, while those more broadly interested in social and cultural history will find much that is useful in McCarthy's new way of grasping the elusive ideological effects of comedy.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1550808012\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Dithyramb, tragedy and comedy\\\", \\\"publication_year\\\": 1927, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 374, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"pmh:oai:quod.lib.umich.edu:MIU01-001181479\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S7407064297\\\", \\\"display_name\\\": \\\"University of Michigan Library Repository\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"repository\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"submittedVersion\\\", \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"text\\\"}, \\\"abstract\\\": \\\"Includes bibliographical references and index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4297668621\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"title\\\": \\\"The Stagecraft and Performance of Roman Comedy\\\", \\\"publication_year\\\": 2006, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 297, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511486203\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"A comprehensive survey of Roman theatrical production, this book examines all aspects of Roman performance practice, and provides fresh insights on the comedies of Plautus and Terence. Following an introductory chapter on the experience of Roman comedy from the perspective of Roman actors and the Roman audience, addressing among other things the economic concerns of putting on a play in the Roman republic, subsequent chapters provide detailed studies of troupe size and the implications for role assignment, masks, stage action, music, and improvisation in the plays of Plautus and Terence. Marshall argues that Roman comedy was raw comedy, much more rough-and-ready than its Hellenistic precursors, but still fully conscious of its literary past. The consequences of this lead to fresh conclusions concerning the dramatic structure of Roman comedy, and a clearer understanding of the relationship between the plays-as-text and the role of improvisation during performance.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"68bce790ce67ec0ab76c62af19d79dc60f91625bc0bc9ec844cd28d0bd6810be\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-a9d63b5b92cd46ff",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:48:19.783848+00:00"
}
```

### `source-714ed4eab8364517`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-714ed4eab8364517",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:48:21.336074+00:00"
}
```

### `r-644b73b84fc94b6d`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-644b73b84fc94b6d\",\"previous_head\":\"74f85935882414321f14792913693feac86f97db64d77e1e66500fe625c8f395\",\"process_id\":2047,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-644b73b84fc94b6d",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:48:21.365569+00:00"
}
```

### `source-cd1dd67a2fff4972`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e24020217\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e24020217\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e23020144\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2020\\\"], \\\"abstract\\\": \\\"<jats:p>Peer review is the driving force of journal development, and reviewers are gatekeepers who ensure that Entropy maintains its standards for the high quality of its published papers [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23020144\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 1, 25]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"f0267b53b73264558f917bc1fe7f7292d9d346f8d4b17f6adca653a24a4fd070\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-cd1dd67a2fff4972",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:49:41.595164+00:00"
}
```

### `source-97f546d2f97a4547`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W4295008953\\\", \\\"doi\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"title\\\": \\\"Neurodivergence‐informed therapy\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 208, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1111/dmcn.15384\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S158041768\\\", \\\"display_name\\\": \\\"Developmental Medicine & Child Neurology\\\", \\\"issn_l\\\": \\\"0012-1622\\\", \\\"issn\\\": [\\\"0012-1622\\\", \\\"1469-8749\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Developmental Medicine &amp; Child Neurology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The neurodiversity movement is a social movement that emerged among autistic self-advocates. It has since spread and has been joined by many with diagnoses of attention-deficit/hyperactivity disorder, dyslexia, and developmental coordination disorder among others. By reconceptualizing neurodiversity as part of biodiversity, neurodiversity proponents emphasize the need to develop an 'ecological' society that supports the conservation of neurological minorities through the construction of ecological niches-that is, making space for all. This is an alternative to the drive to eliminate diversity through attempts to 'treat' or 'cure' neurodivergence. So far, neurodiversity theory has not been formally adapted for psychotherapeutic frameworks, and it is not the role of the therapist to make systemic changes to societal organization. Still, there is room for fruitfully drawing on a neurodiversity perspective for therapists working with neurodivergent people in clinical settings. Here, we draw on the example of autism and synthesize three key themes to propose the concept of neurodivergence-informed therapy. First, the reconceptualization of dysfunction as relational rather than individual. Second, the importance of neurodivergence acceptance and pride, and disability community and culture to emancipate neurodivergent people from neuro-normativity. Third, the need for therapists to cultivate a relational epistemic humility regarding different experiences of neurodivergence and disablement.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W3198526359\\\", \\\"doi\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"title\\\": \\\"From neurodiversity to neurodivergence: the role of epistemic and cognitive marginalization\\\", \\\"publication_year\\\": 2021, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 115, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1007/s11229-021-03356-5\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S255146\\\", \\\"display_name\\\": \\\"Synthese\\\", \\\"issn_l\\\": \\\"0039-7857\\\", \\\"issn\\\": [\\\"0039-7857\\\", \\\"1573-0964\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319900\\\", \\\"host_organization_name\\\": \\\"Springer Science+Business Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319900\\\", \\\"https://openalex.org/P4310319965\\\"], \\\"host_organization_lineage_names\\\": [\\\"Springer Science+Business Media\\\", \\\"Springer Nature\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Synthese\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W4210394959\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"title\\\": \\\"Joint Hypermobility Links Neurodivergence to Dysautonomia and Pain\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 97, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyt.2021.786916\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S92766711\\\", \\\"display_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"issn_l\\\": \\\"1664-0640\\\", \\\"issn\\\": [\\\"1664-0640\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"OBJECTIVES: Autism, attention deficit hyperactivity disorder (ADHD), and tic disorder (Tourette syndrome; TS) are neurodevelopmental conditions that frequently co-occur and impact psychological, social, and emotional processes. Increased likelihood of chronic physical symptoms, including fatigue and pain, are also recognized. The expression of joint hypermobility, reflecting a constitutional variant in connective tissue, predicts susceptibility to psychological symptoms alongside recognized physical symptoms. Here, we tested for increased prevalence of joint hypermobility, autonomic dysfunction, and musculoskeletal symptoms in 109 adults with neurodevelopmental condition diagnoses. METHODS: = 57). Age specific cut-offs for GJH were possible to determine in the neurodivergent and comparison group only. RESULTS: The neurodivergent group manifested elevated prevalence of hypermobility (51%) compared to the general population rate of 20% and a comparison population (17.5%). Using a more stringent age specific cut-off, in the neurodivergent group this prevalence was 28.4%, more than double than the comparison group (12.5%). Odds ratio for presence of hypermobility in neurodivergent group, compared to the general population was 4.51 (95% CI 2.17-9.37), with greater odds in females than males. Using age specific cut-off, the odds ratio for GJH in neurodivergent group, compared to the comparison group, was 2.84 (95% CI 1.16-6.94). Neurodivergent participants reported significantly more symptoms of orthostatic intolerance and musculoskeletal skeletal pain than the comparison group. The number of hypermobile joints was found to mediate the relationship between neurodivergence and symptoms of both dysautonomia and pain. CONCLUSIONS: In neurodivergent adults, there is a strong link between the expression of joint hypermobility, dysautonomia, and pain, more so than in the comparison group. Moreover, joint hypermobility mediates the link between neurodivergence and symptoms of dysautonomia and pain. Increased awareness and understanding of this association may enhance the management of core symptoms and allied difficulties in neurodivergent people, including co-occurring physical symptoms, and guide service delivery in the future.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4284713669\\\", \\\"doi\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"title\\\": \\\"Social Virtual Reality: Neurodivergence and Inclusivity in the Metaverse\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 107, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3390/soc12040102\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"pdf_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210173133\\\", \\\"display_name\\\": \\\"Societies\\\", \\\"issn_l\\\": \\\"2075-4698\\\", \\\"issn\\\": [\\\"2075-4698\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310310987\\\", \\\"host_organization_name\\\": \\\"Multidisciplinary Digital Publishing Institute\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310310987\\\"], \\\"host_organization_lineage_names\\\": [\\\"Multidisciplinary Digital Publishing Institute\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Societies\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Whereas traditional teaching environments encourage lively and engaged interaction and reward extrovert qualities, introverts, and others with symptoms that make social engagement difficult, such as autism spectrum disorder (ASD), are often disadvantaged. This population is often more engaged in quieter, low-key learning environments and often does not speak up and answer questions in traditional lecture-style classes. These individuals are often passed over in school and later in their careers for not speaking up and are assumed to not be as competent as their gregarious and outgoing colleagues. With the rise of the metaverse and democratization of virtual reality (VR) technology, post-secondary education is especially poised to capitalize on the immersive learning environments social VR provides and prepare students for the future of work, where virtual collaboration will be key. This study seeks to reconsider the role of VR and the metaverse for introverts and those with ASD. The metaverse has the potential to continue the social and workplace changes already accelerated by the pandemic and ope\", \"excerpt_truncated\": true, \"source_sha256\": \"49bff771325097bc2bb8577c8e75f9770f94210cd14c17c4e00f8b71a462a1bf\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-97f546d2f97a4547",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:49:42.334675+00:00"
}
```

### `r-3e6f1f402da4463a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-3e6f1f402da4463a\",\"previous_head\":\"09386a887cc32f34be9031d2a5a622f7fb38bbe00d4534c72ad4aafb67cefad3\",\"process_id\":2065,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-3e6f1f402da4463a",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:49:42.365145+00:00"
}
```

### `source-4c409854df6146cc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2023723978\\\", \\\"doi\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"title\\\": \\\"A Generative Theory of Tonal Music\\\", \\\"publication_year\\\": 1984, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 3790, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.2307/3679778\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S165362224\\\", \\\"display_name\\\": \\\"Computer Music Journal\\\", \\\"issn_l\\\": \\\"0148-9267\\\", \\\"issn\\\": [\\\"0148-9267\\\", \\\"1531-5169\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310315718\\\", \\\"host_organization_name\\\": \\\"The MIT Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315718\\\", \\\"https://openalex.org/P4310316440\\\"], \\\"host_organization_lineage_names\\\": [\\\"The MIT Press\\\", \\\"Massachusetts Institute of Technology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Computer Music Journal\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This book explores the relationships between language, music, and the brain by pursuing four key themes and the crosstalk among them: song and dance as a bridge between music and language; multiple levels of structure from brain to behavior to culture; the semantics of internal and external worlds and the role of emotion; and the evolution and development of language. The book offers specially commissioned expositions of current research accessible both to experts across disciplines and to non-experts. These chapters provide the background for reports by groups of specialists that chart current controversies and future directions of research on each theme. The book looks beyond mere auditory experience, probing the embodiment that links speech to gesture and music to dance. The study of the brains of monkeys and songbirds illuminates hypotheses on the evolution of brain mechanisms that support music and language, while the study of infants calibrates the developmental timetable of their capacities. The result is a unique book that will interest any reader seeking to learn more about language or music and will appeal especially to readers intrigued by the relationships of language and music with each other and with the brain. ContributorsFrancisco Aboitiz, Michael A. Arbib, Annabel J. Cohen, Ian Cross, Peter Ford Dominey, W. Tecumseh Fitch, Leonardo Fogassi, Jonathan Fritz, Thomas Fritz, Peter Hagoort, John Halle, Henkjan Honing, Atsushi Iriki, Petr Janata, Erich Jarvis, Stefan Koelsch, Gina Kuperberg, D. Robert Ladd, Fred Lerdahl, Stephen C. Levinson, Jerome Lewis, Katja Liebal, Jonatas Manzolli, Bjorn Merker, Lawrence M. Parsons, Aniruddh D. Patel, Isabelle Peretz, David Poeppel, Josef P. Rauschecker, Nikki Rickard, Klaus Scherer, Gottfried Schlaug, Uwe Seifert, Mark Steedman, Dietrich Stout, Francesca Stregapede, Sharon Thompson-Schill, Laurel Trainor, Sandra E. Trehub, Paul Verschure\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2191779130\\\", \\\"doi\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"title\\\": \\\"librosa: Audio and Music Signal Analysis in Python\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"conference-paper\\\", \\\"cited_by_count\\\": 3071, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.25080/majora-7b98e3ed-003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"pdf_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4220651651\\\", \\\"display_name\\\": \\\"Proceedings of the Python in Science Conferences\\\", \\\"issn_l\\\": \\\"2575-9752\\\", \\\"issn\\\": [\\\"2575-9752\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the Python in Science Conference\\\", \\\"raw_type\\\": \\\"proceedings-article\\\"}, \\\"abstract\\\": \\\"This document describes version 0.4.0 of librosa: a Python package for audio and music signal processing.At a high level, librosa provides implementations of a variety of common functions used throughout the field of music information retrieval.In this document, a brief overview of the library's functionality is provided, along with explanations of the design goals, software development practices, and notational conventions.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2006090347\\\", \\\"doi\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"title\\\": \\\"The New Grove dictionary of music and musicians\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"book-review\\\", \\\"cited_by_count\\\": 2597, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.5860/choice.38-5906\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2764375719\\\", \\\"display_name\\\": \\\"Choice Reviews Online\\\", \\\"issn_l\\\": \\\"0009-4978\\\", \\\"issn\\\": [\\\"0009-4978\\\", \\\"1523-8253\\\", \\\"1943-5975\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310316146\\\", \\\"host_organization_name\\\": \\\"Association of College and Research Libraries\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316146\\\", \\\"https://openalex.org/P4310315903\\\"], \\\"host_organization_lineage_names\\\": [\\\"Association of College and Research Libraries\\\", \\\"American Library Association\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Choice Reviews Online\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This work contains almost 30,000 articles containing over 25 million words on musicians, composers, musicologists, instruments, places, genres, terms, performance practice, concepts, acoustics and more. All the articles are written by experts in their subject. There are over 500 biographies of composers, performers and writers on music and over 1,500 articles on styles, terms, and genres. It also includes: over 500 articles on ancient music and church music over 700 articles on regions, countries and cities over 2,000 articles on instruments and their makers and performance practice over 650 articles on printing and publishing over 1,200 articles on world music over 1,000 articles on popular music, light music and jazz over 250 articles on concepts 85 articles on acoustics 126 articles on sources and a one volume index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1500952994\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Image-Music-Text\\\", \\\"publication_year\\\": 1977, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 2874, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"mag:1500952994\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"http://ci.nii.ac.jp/ncid/BA10872380\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210197683\\\", \\\"display_name\\\": \\\"Medical Entomology and Zoology\\\", \\\"issn_l\\\": \\\"0424-7086\\\", \\\"issn\\\": [\\\"0424-7086\\\", \\\"2185-5609\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310319750\\\", \\\"host_organization_name\\\": \\\"Japan Society of Medical Entomology and Zoology\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319750\\\"], \\\"host_organization_lineage_names\\\": [\\\"Japan Society of Medical Entomology and Zoology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": null, \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": null}, \\\"abstract\\\": null}]\", \"excerpt_truncated\": false, \"source_sha256\": \"8dd2b69447c0eae1cf7e24cd1e9fea845a8ea3613b8b35c97d52de04376dedd7\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-4c409854df6146cc",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:51:31.641801+00:00"
}
```

### `source-658000d10aad48e6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-658000d10aad48e6",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:51:32.822527+00:00"
}
```

### `r-9e668a8e7edb4cb3`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-9e668a8e7edb4cb3\",\"previous_head\":\"19e132e4be62ed2ee3da2a784a66ddf5bd51070b16dbffc4745e79c0d1dc3688\",\"process_id\":2053,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-9e668a8e7edb4cb3",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:51:32.867239+00:00"
}
```

### `source-0df9f503166f4082`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-0df9f503166f4082",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:52:55.793367+00:00"
}
```

### `source-b04e6f19a4f74765`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2139416101\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"title\\\": \\\"Maximum entropy modeling of species geographic distributions\\\", \\\"publication_year\\\": 2005, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 18078, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.ecolmodel.2005.03.026\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S88315673\\\", \\\"display_name\\\": \\\"Ecological Modelling\\\", \\\"issn_l\\\": \\\"0304-3800\\\", \\\"issn\\\": [\\\"0304-3800\\\", \\\"1872-7026\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecological Modelling\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W1862394037\\\", \\\"doi\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"title\\\": \\\"Physiological time-series analysis using approximate entropy and sample entropy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7942, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1152/ajpheart.2000.278.6.h2039\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S87338489\\\", \\\"display_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"issn_l\\\": \\\"0363-6135\\\", \\\"issn\\\": [\\\"0363-6135\\\", \\\"1522-1539\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Entropy, as it relates to dynamical systems, is the rate of information production. Methods for estimation of the entropy of a system represented by a time series are not, however, well suited to analysis of the short and noisy data sets encountered in cardiovascular and other biological studies. Pincus introduced approximate entropy (ApEn), a set of measures of system complexity closely related to entropy, which is easily applied to clinical cardiovascular and other time series. ApEn statistics, however, lead to inconsistent results. We have developed a new and related complexity measure, sample entropy (SampEn), and have compared ApEn and SampEn by using them to analyze sets of random numbers with known probabilistic character. We have also evaluated cross-ApEn and cross-SampEn, which use cardiovascular data sets to measure the similarity of two distinct time series. SampEn agreed with theory much more closely than ApEn over a broad range of conditions. The improved accuracy of SampEn statistics should make them useful in the study of experimental clinical cardiovascular and other biological time series.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2146478425\\\", \\\"doi\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"title\\\": \\\"Black Holes and Entropy\\\", \\\"publication_year\\\": 1973, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7532, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1103/physrevd.7.2333\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210190737\\\", \\\"display_name\\\": \\\"Physical review. D. Particles, fields, gravitation, and cosmology/Physical review. D. Particles and fields\\\", \\\"issn_l\\\": \\\"0556-2821\\\", \\\"issn\\\": [\\\"0556-2821\\\", \\\"1089-4918\\\", \\\"1538-4500\\\", \\\"1550-2368\\\", \\\"1550-7998\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Physical Review D\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"There are a number of similarities between black-hole physics and thermodynamics. Most striking is the similarity in the behaviors of black-hole area and of entropy: Both quantities tend to increase irreversibly. In this paper we make this similarity the basis of a thermodynamic approach to black-hole physics. After a brief review of the elements of the theory of information, we discuss black-hole physics from the point of view of information theory. We show that it is natural to introduce the concept of black-hole entropy as the measure of information about a black-hole interior which is inaccessible to an exterior observer. Considerations of simplicity and consistency, and dimensional arguments indicate that the black-hole entropy is equal to the ratio of the black-hole area to the square of the Planck length times a dimensionless constant of order unity. A different approach making use of the specific properties of Kerr black holes and of concepts from information theory leads to the same conclusion, and suggests a definite value for the constant. The physical content of the concept of black-hole entropy derives from the following generalized version of the second law: When common entropy goes down a black hole, the common entropy in the black-hole exterior plus the black-hole entropy never decreases. The validity of this version of the second law is supported by an argument from information theory as well as by several examples.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2058085399\\\", \\\"doi\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"title\\\": \\\"Nanostructured High‐Entropy Alloys with Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes\\\", \\\"publication_year\\\": 2004, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 15264, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1002/adem.200300567\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S156255550\\\", \\\"display_name\\\": \\\"Advanced Engineering Materials\\\", \\\"issn_l\\\": \\\"1438-1656\\\", \\\"issn\\\": [\\\"1438-1656\\\", \\\"1527-2648\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Advanced Engineering Materials\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"A new approach for the design of alloys is presented in this study. These “high‐entropy alloys” with multi‐principal elements were synthesized using well‐developed processing technologies. Preliminary results demonstrate examples of the alloys with simple crystal structures, nanostructures, and promising mechanical properties. This approach may be opening a new era in materials science and engineering.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"5782609c6cdf27c0e7f6523dc3b1c02b8e2554c6bde3002e69fe32b9ef8ec1ed\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-b04e6f19a4f74765",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:52:56.476431+00:00"
}
```

### `r-1a69e42b1c434423`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-1a69e42b1c434423\",\"previous_head\":\"17608afec33a96b564eada2a6c6216b8f9f10bcbce714ed447c6a42a847f2399\",\"process_id\":2100,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-1a69e42b1c434423",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:52:56.515630+00:00"
}
```

### `source-729dc050c1c24657`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W1989670470\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"title\\\": \\\"Shakespeare and the Traditions of Comedy\\\", \\\"publication_year\\\": 1974, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 295, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511553189\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"This book relates Shakespeare's comedies to a broad European background. At the beginning and again at the end of his career, Shakespeare was attracted by a tradition of stage romances which can be traced back to Chaucer's time. But the main shaping behind his comedies came from the classical tradition. Mr Salingar therefore examines the underlying theme of 'errors' in Greek and Roman comedies and, taking three Italian comedies famous in the sixteenth century as examples, he then reveals how the Italian Renaissance revived the classical tradition, and what effect this revival had on Shakespeare the Elizabethan playwright and discusses such topics as the device of the play within a play and Shakespeare's choice of Italian short stories as plot material. This book shows how Shakespeare changed the motifs he took over from previous traditions of comedy and highlights the innovations he introduced, as an actor-dramatist writing in the first period of commercial theatre in Europe.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4213157483\\\", \\\"doi\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"title\\\": \\\"Slaves, Masters, and the Art of Authority in Plautine Comedy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 396, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1515/9781400824700\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306463805\\\", \\\"display_name\\\": \\\"Princeton University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310316492\\\", \\\"host_organization_name\\\": \\\"Princeton University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316492\\\"], \\\"host_organization_lineage_names\\\": [\\\"Princeton University Press\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"What pleasures did Plautus' heroic tricksters provide their original audience? How should we understand the compelling mix of rebellion and social conservatism that Plautus offers? Through a close reading of four plays representing the full range of his work (Menaechmi, Casina, Persa, and Captivi), Kathleen McCarthy develops an innovative model of Plautine comedy and its social effects. She concentrates on how the plays are shaped by the interaction of two comic modes: the socially conservative mode of naturalism and the potentially subversive mode of farce. It is precisely this balance of the naturalistic and the farcical that allows everyone in the audience--especially those well placed in the social hierarchy--to identify both with and against the rebel, to feel both the thrill of being a clever underdog and the complacency of being a securely ensconced authority figure. Basing her interpretation on the workings of farce and naturalism in Plautine comedy, McCarthy finds a way to understand the plays' patchwork literary style as well as their protean social effects. Beyond this, she raises important questions about popular literature and performance not only on ancient Roman stages but in cultures far from Plautus' Rome. How and why do people identify with the fictional figures of social subordinates? How do stock characters, happy endings, and other conventions operate? How does comedy simultaneously upset and uphold social hierarchies? Scholars interested in Plautine theater will be rewarded by the detailed analyses of the plays, while those more broadly interested in social and cultural history will find much that is useful in McCarthy's new way of grasping the elusive ideological effects of comedy.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1550808012\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Dithyramb, tragedy and comedy\\\", \\\"publication_year\\\": 1927, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 374, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"pmh:oai:quod.lib.umich.edu:MIU01-001181479\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S7407064297\\\", \\\"display_name\\\": \\\"University of Michigan Library Repository\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"repository\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"submittedVersion\\\", \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"text\\\"}, \\\"abstract\\\": \\\"Includes bibliographical references and index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4297668621\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"title\\\": \\\"The Stagecraft and Performance of Roman Comedy\\\", \\\"publication_year\\\": 2006, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 297, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511486203\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"A comprehensive survey of Roman theatrical production, this book examines all aspects of Roman performance practice, and provides fresh insights on the comedies of Plautus and Terence. Following an introductory chapter on the experience of Roman comedy from the perspective of Roman actors and the Roman audience, addressing among other things the economic concerns of putting on a play in the Roman republic, subsequent chapters provide detailed studies of troupe size and the implications for role assignment, masks, stage action, music, and improvisation in the plays of Plautus and Terence. Marshall argues that Roman comedy was raw comedy, much more rough-and-ready than its Hellenistic precursors, but still fully conscious of its literary past. The consequences of this lead to fresh conclusions concerning the dramatic structure of Roman comedy, and a clearer understanding of the relationship between the plays-as-text and the role of improvisation during performance.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"d6c772ee2bc75cc4845f579f214083eb5c58a121c69013ba250470ba51f1fb1d\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-729dc050c1c24657",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:54:26.999837+00:00"
}
```

### `source-c1208ace89e84831`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}, {\\\"DOI\\\": \\\"10.3390/e21020130\\\", \\\"title\\\": [\\\"Entropy 2018 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof. Dr. Kevin H. Knuth, we are pleased to announce the Entropy Best Paper Award for 2018 [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21020130\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 30]]}}, {\\\"DOI\\\": \\\"10.3390/e23070865\\\", \\\"title\\\": [\\\"Entropy 2021 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23070865\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 7, 6]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"faceda2b2cd3896333a85a05893a349eecb5109bcb411d5c6367cd4f6d8ddb28\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-c1208ace89e84831",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:54:28.304377+00:00"
}
```

### `r-4df368205109443c`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-4df368205109443c\",\"previous_head\":\"4d6c8acf9f0b77c6ee1c936ff327c4bd0ffe4f6ada15ca57d82d1a6ccfdc4045\",\"process_id\":2249,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-4df368205109443c",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:54:28.356705+00:00"
}
```

### `source-44d3b63b3ba24f93`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"67652218c8636be0bfd3ccd4a3b416c680c5314b6011d57c67c67bbf533ad1c7\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-44d3b63b3ba24f93",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:55:50.577018+00:00"
}
```

### `source-010488341e39464c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2139416101\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"title\\\": \\\"Maximum entropy modeling of species geographic distributions\\\", \\\"publication_year\\\": 2005, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 18078, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.ecolmodel.2005.03.026\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S88315673\\\", \\\"display_name\\\": \\\"Ecological Modelling\\\", \\\"issn_l\\\": \\\"0304-3800\\\", \\\"issn\\\": [\\\"0304-3800\\\", \\\"1872-7026\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecological Modelling\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W1862394037\\\", \\\"doi\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"title\\\": \\\"Physiological time-series analysis using approximate entropy and sample entropy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7942, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1152/ajpheart.2000.278.6.h2039\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S87338489\\\", \\\"display_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"issn_l\\\": \\\"0363-6135\\\", \\\"issn\\\": [\\\"0363-6135\\\", \\\"1522-1539\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Entropy, as it relates to dynamical systems, is the rate of information production. Methods for estimation of the entropy of a system represented by a time series are not, however, well suited to analysis of the short and noisy data sets encountered in cardiovascular and other biological studies. Pincus introduced approximate entropy (ApEn), a set of measures of system complexity closely related to entropy, which is easily applied to clinical cardiovascular and other time series. ApEn statistics, however, lead to inconsistent results. We have developed a new and related complexity measure, sample entropy (SampEn), and have compared ApEn and SampEn by using them to analyze sets of random numbers with known probabilistic character. We have also evaluated cross-ApEn and cross-SampEn, which use cardiovascular data sets to measure the similarity of two distinct time series. SampEn agreed with theory much more closely than ApEn over a broad range of conditions. The improved accuracy of SampEn statistics should make them useful in the study of experimental clinical cardiovascular and other biological time series.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2146478425\\\", \\\"doi\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"title\\\": \\\"Black Holes and Entropy\\\", \\\"publication_year\\\": 1973, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7532, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1103/physrevd.7.2333\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210190737\\\", \\\"display_name\\\": \\\"Physical review. D. Particles, fields, gravitation, and cosmology/Physical review. D. Particles and fields\\\", \\\"issn_l\\\": \\\"0556-2821\\\", \\\"issn\\\": [\\\"0556-2821\\\", \\\"1089-4918\\\", \\\"1538-4500\\\", \\\"1550-2368\\\", \\\"1550-7998\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Physical Review D\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"There are a number of similarities between black-hole physics and thermodynamics. Most striking is the similarity in the behaviors of black-hole area and of entropy: Both quantities tend to increase irreversibly. In this paper we make this similarity the basis of a thermodynamic approach to black-hole physics. After a brief review of the elements of the theory of information, we discuss black-hole physics from the point of view of information theory. We show that it is natural to introduce the concept of black-hole entropy as the measure of information about a black-hole interior which is inaccessible to an exterior observer. Considerations of simplicity and consistency, and dimensional arguments indicate that the black-hole entropy is equal to the ratio of the black-hole area to the square of the Planck length times a dimensionless constant of order unity. A different approach making use of the specific properties of Kerr black holes and of concepts from information theory leads to the same conclusion, and suggests a definite value for the constant. The physical content of the concept of black-hole entropy derives from the following generalized version of the second law: When common entropy goes down a black hole, the common entropy in the black-hole exterior plus the black-hole entropy never decreases. The validity of this version of the second law is supported by an argument from information theory as well as by several examples.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2058085399\\\", \\\"doi\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"title\\\": \\\"Nanostructured High‐Entropy Alloys with Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes\\\", \\\"publication_year\\\": 2004, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 15264, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1002/adem.200300567\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S156255550\\\", \\\"display_name\\\": \\\"Advanced Engineering Materials\\\", \\\"issn_l\\\": \\\"1438-1656\\\", \\\"issn\\\": [\\\"1438-1656\\\", \\\"1527-2648\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Advanced Engineering Materials\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"A new approach for the design of alloys is presented in this study. These “high‐entropy alloys” with multi‐principal elements were synthesized using well‐developed processing technologies. Preliminary results demonstrate examples of the alloys with simple crystal structures, nanostructures, and promising mechanical properties. This approach may be opening a new era in materials science and engineering.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"30ecdee807c3c6eb55359639fa68ab8769946fb3d98d07d487ab7089e3d6fd1b\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-010488341e39464c",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:55:50.990366+00:00"
}
```

### `r-1a4ba06b2fa24fb6`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-1a4ba06b2fa24fb6\",\"previous_head\":\"516b91f750a38bf876258d4168e630d34dbf20338eb5586c30a1e9189ac9c5e3\",\"process_id\":2067,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-1a4ba06b2fa24fb6",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:55:51.034887+00:00"
}
```

### `source-b99500d122264f40`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2023723978\\\", \\\"doi\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"title\\\": \\\"A Generative Theory of Tonal Music\\\", \\\"publication_year\\\": 1984, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 3790, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.2307/3679778\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S165362224\\\", \\\"display_name\\\": \\\"Computer Music Journal\\\", \\\"issn_l\\\": \\\"0148-9267\\\", \\\"issn\\\": [\\\"0148-9267\\\", \\\"1531-5169\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310315718\\\", \\\"host_organization_name\\\": \\\"The MIT Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315718\\\", \\\"https://openalex.org/P4310316440\\\"], \\\"host_organization_lineage_names\\\": [\\\"The MIT Press\\\", \\\"Massachusetts Institute of Technology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Computer Music Journal\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This book explores the relationships between language, music, and the brain by pursuing four key themes and the crosstalk among them: song and dance as a bridge between music and language; multiple levels of structure from brain to behavior to culture; the semantics of internal and external worlds and the role of emotion; and the evolution and development of language. The book offers specially commissioned expositions of current research accessible both to experts across disciplines and to non-experts. These chapters provide the background for reports by groups of specialists that chart current controversies and future directions of research on each theme. The book looks beyond mere auditory experience, probing the embodiment that links speech to gesture and music to dance. The study of the brains of monkeys and songbirds illuminates hypotheses on the evolution of brain mechanisms that support music and language, while the study of infants calibrates the developmental timetable of their capacities. The result is a unique book that will interest any reader seeking to learn more about language or music and will appeal especially to readers intrigued by the relationships of language and music with each other and with the brain. ContributorsFrancisco Aboitiz, Michael A. Arbib, Annabel J. Cohen, Ian Cross, Peter Ford Dominey, W. Tecumseh Fitch, Leonardo Fogassi, Jonathan Fritz, Thomas Fritz, Peter Hagoort, John Halle, Henkjan Honing, Atsushi Iriki, Petr Janata, Erich Jarvis, Stefan Koelsch, Gina Kuperberg, D. Robert Ladd, Fred Lerdahl, Stephen C. Levinson, Jerome Lewis, Katja Liebal, Jonatas Manzolli, Bjorn Merker, Lawrence M. Parsons, Aniruddh D. Patel, Isabelle Peretz, David Poeppel, Josef P. Rauschecker, Nikki Rickard, Klaus Scherer, Gottfried Schlaug, Uwe Seifert, Mark Steedman, Dietrich Stout, Francesca Stregapede, Sharon Thompson-Schill, Laurel Trainor, Sandra E. Trehub, Paul Verschure\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2191779130\\\", \\\"doi\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"title\\\": \\\"librosa: Audio and Music Signal Analysis in Python\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"conference-paper\\\", \\\"cited_by_count\\\": 3071, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.25080/majora-7b98e3ed-003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"pdf_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4220651651\\\", \\\"display_name\\\": \\\"Proceedings of the Python in Science Conferences\\\", \\\"issn_l\\\": \\\"2575-9752\\\", \\\"issn\\\": [\\\"2575-9752\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the Python in Science Conference\\\", \\\"raw_type\\\": \\\"proceedings-article\\\"}, \\\"abstract\\\": \\\"This document describes version 0.4.0 of librosa: a Python package for audio and music signal processing.At a high level, librosa provides implementations of a variety of common functions used throughout the field of music information retrieval.In this document, a brief overview of the library's functionality is provided, along with explanations of the design goals, software development practices, and notational conventions.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2006090347\\\", \\\"doi\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"title\\\": \\\"The New Grove dictionary of music and musicians\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"book-review\\\", \\\"cited_by_count\\\": 2597, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.5860/choice.38-5906\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2764375719\\\", \\\"display_name\\\": \\\"Choice Reviews Online\\\", \\\"issn_l\\\": \\\"0009-4978\\\", \\\"issn\\\": [\\\"0009-4978\\\", \\\"1523-8253\\\", \\\"1943-5975\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310316146\\\", \\\"host_organization_name\\\": \\\"Association of College and Research Libraries\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316146\\\", \\\"https://openalex.org/P4310315903\\\"], \\\"host_organization_lineage_names\\\": [\\\"Association of College and Research Libraries\\\", \\\"American Library Association\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Choice Reviews Online\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This work contains almost 30,000 articles containing over 25 million words on musicians, composers, musicologists, instruments, places, genres, terms, performance practice, concepts, acoustics and more. All the articles are written by experts in their subject. There are over 500 biographies of composers, performers and writers on music and over 1,500 articles on styles, terms, and genres. It also includes: over 500 articles on ancient music and church music over 700 articles on regions, countries and cities over 2,000 articles on instruments and their makers and performance practice over 650 articles on printing and publishing over 1,200 articles on world music over 1,000 articles on popular music, light music and jazz over 250 articles on concepts 85 articles on acoustics 126 articles on sources and a one volume index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1500952994\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Image-Music-Text\\\", \\\"publication_year\\\": 1977, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 2874, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"mag:1500952994\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"http://ci.nii.ac.jp/ncid/BA10872380\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210197683\\\", \\\"display_name\\\": \\\"Medical Entomology and Zoology\\\", \\\"issn_l\\\": \\\"0424-7086\\\", \\\"issn\\\": [\\\"0424-7086\\\", \\\"2185-5609\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310319750\\\", \\\"host_organization_name\\\": \\\"Japan Society of Medical Entomology and Zoology\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319750\\\"], \\\"host_organization_lineage_names\\\": [\\\"Japan Society of Medical Entomology and Zoology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": null, \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": null}, \\\"abstract\\\": null}]\", \"excerpt_truncated\": false, \"source_sha256\": \"12f74ef165a05421eadc469eae241c1fd9eb624a6675dd98f5da970e1a867f9d\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-b99500d122264f40",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 5,
  "time": "2026-09-19T16:57:16.032687+00:00"
}
```

### `source-c314ace135114008`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.23943/princeton/9780691149523.003.0003\\\", \\\"title\\\": [\\\"Misrule as Comedy; Comedy as Misrule\\\"], \\\"abstract\\\": \\\"<p>This chapter considers the tendency for Elizabethan comedy to be a saturnalia, rather than to represent saturnalian experience. In Elizabethan England, a direct development of comedy out of festivity was prevented by the existence of an already developed dramatic literature—and by the whole moral superstructure of Elizabethan society. When the issue was put to the test, license for festive abuse was never granted by Elizabethan officials. The tendency examined in this chapter bears witness to the saturnalian impulse which did find expression in dramatic fiction. Saturnalia could come into its own in the theater by virtue of the distinction between the stage and the world which Puritans were unwilling to make in London but which fortunately prevailed across the river on the Bankside.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.23943/princeton/9780691149523.003.0003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2011, 10, 23]]}}, {\\\"DOI\\\": \\\"10.5040/9781350911949\\\", \\\"title\\\": [\\\"Drama/Comedy\\\"], \\\"URL\\\": \\\"https://doi.org/10.5040/9781350911949\\\", \\\"published\\\": {\\\"date-parts\\\": [[1988]]}}, {\\\"DOI\\\": \\\"10.1093/oseo/instance.00232733\\\", \\\"title\\\": [\\\"Section A: Doric Comedy\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/oseo/instance.00232733\\\"}, {\\\"DOI\\\": \\\"10.1093/oseo/instance.00232803\\\", \\\"title\\\": [\\\"Section C: 'Middle' and 'New Comedy'\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/oseo/instance.00232803\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"46a9afd700bc8ebcfbf2faeac225a02e3b4eb88b3227ecd187c128f297f7c634\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-c314ace135114008",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 5,
  "time": "2026-09-19T16:57:17.127144+00:00"
}
```

### `r-52523dbea48f41d5`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":5,\"inherited_commitments\":[],\"invocation\":\"w-52523dbea48f41d5\",\"previous_head\":\"9a95ce6086649f322e6dcef960e5f37e1bf2329224961527a1cf90e4970d91cb\",\"process_id\":2042,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-52523dbea48f41d5",
  "source": "runtime:continuity",
  "version": 5,
  "time": "2026-09-19T16:57:17.174917+00:00"
}
```

### `source-50089614af314989`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# Architecture and limits\\n\\n**WAKE✳︎** is designed around continuity of accountable work, not continuity of a model instance. Models, vendors and eventually human operators may change; the durable record, authority boundary, provenance and correction mechanisms are what carry the work forward.\\n\\n\\n## The authority boundary\\n\\nModels are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from a deliberately broad but explicit HTTPS research-host allowlist before inference; models can record bounded follow-up searches and approved URLs as durable hypotheses, but those follow-ups do not consume collector bandwidth or execute requests directly; randomized configured-topic attention remains authoritative, with periodic exposure to an under-attended domain while active projects remain intact. Operator-supplied evidence and earlier journal prose are data, not executable instructions.\\n\\nThe fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.\\n\\n## Durable record\\n\\n`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.\\n\\nSQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.\\n\\nThe record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.\\n\\n## **WAKE✳︎** lifecycle\\n\\n1. Acquire the writer lock and verify history and projection.\\n2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.\\n3. Check the Pacific-day call budget, before any paid-capable provider call.\\n4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.\\n5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.\\n6. Persist `invocation_started`, its exact request, provider identity and quota reservation.\\n7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.\\n8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.\\n9. The scheduled wrapper generates reports and a consistent backup.\\n\\nA runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.\\n\\n## Governed transitions\\n\\n| Action | Enforced constraint |\\n| --- | --- |\\n| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |\\n| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |\\n| Review belief | At least one new observation cited; previous citations retained; reason required |\\n| Retract belief | Existing belief, new evidence, zero confidence; old history retained |\\n| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |\\n| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |\\n| Cancel commitment | Human-only event with a reason |\\n| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |\\n| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |\\n| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |\\n\\nThere are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.\\n\\nEvidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic, forward-only corroboration gate to live collector evidence: notebook findings and public blog bodies must materially match at least two distinct retrieved source URLs, and those sources must have been collected under the same configured research topic as the project. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.\\n\\nResearch topics have no hardcoded governance fallback: the audited topic configuration loaded from `research-topics.toml` is authoritative. The collector host boundary is separate from topic configuration and intentionally remains an explicit allowlist to preserve SSRF/network safety while permitting a broad set of scholarly indexes, journals, universities, public-data institutions, and source-controlled WAKE files.\\n\\nThe research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject live findings whose material terms are not corroborated across two distinct collected source URLs from the project's own topic. Collector-stamped verification metadata is trusted application data; model-authored or legacy evidence cannot opt itself into or out of this gate. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.\\n\\n## Progressive abstraction and reversible lookup\\n\\n**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact\\nrequests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that\\nhistory in its active context. It receives a bounded working representation selected for the present task,\\nwhile the full record remains available to later invocations and human readers.\\n\\nThis is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.\\nCurrent code already performs bounded selection and excerpting. It now also creates a deterministic\\n**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects\\nand recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting\\nraw source contents and journal detail. The shadow is stored in the invocation receipt with its character\\nsize relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or\\nalter the provider context, so it introduces measurement without yet \", \"excerpt_truncated\": true, \"source_sha256\": \"59223405e6962f4627c89129df2f688d279279c536294451338a91c8711a8707\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-50089614af314989",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
  "version": 6,
  "time": "2026-09-19T16:58:45.394697+00:00"
}
```

### `source-4cfd4c36f09d48e6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W4295008953\\\", \\\"doi\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"title\\\": \\\"Neurodivergence‐informed therapy\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 208, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1111/dmcn.15384\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S158041768\\\", \\\"display_name\\\": \\\"Developmental Medicine & Child Neurology\\\", \\\"issn_l\\\": \\\"0012-1622\\\", \\\"issn\\\": [\\\"0012-1622\\\", \\\"1469-8749\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Developmental Medicine &amp; Child Neurology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The neurodiversity movement is a social movement that emerged among autistic self-advocates. It has since spread and has been joined by many with diagnoses of attention-deficit/hyperactivity disorder, dyslexia, and developmental coordination disorder among others. By reconceptualizing neurodiversity as part of biodiversity, neurodiversity proponents emphasize the need to develop an 'ecological' society that supports the conservation of neurological minorities through the construction of ecological niches-that is, making space for all. This is an alternative to the drive to eliminate diversity through attempts to 'treat' or 'cure' neurodivergence. So far, neurodiversity theory has not been formally adapted for psychotherapeutic frameworks, and it is not the role of the therapist to make systemic changes to societal organization. Still, there is room for fruitfully drawing on a neurodiversity perspective for therapists working with neurodivergent people in clinical settings. Here, we draw on the example of autism and synthesize three key themes to propose the concept of neurodivergence-informed therapy. First, the reconceptualization of dysfunction as relational rather than individual. Second, the importance of neurodivergence acceptance and pride, and disability community and culture to emancipate neurodivergent people from neuro-normativity. Third, the need for therapists to cultivate a relational epistemic humility regarding different experiences of neurodivergence and disablement.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W3198526359\\\", \\\"doi\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"title\\\": \\\"From neurodiversity to neurodivergence: the role of epistemic and cognitive marginalization\\\", \\\"publication_year\\\": 2021, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 115, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1007/s11229-021-03356-5\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S255146\\\", \\\"display_name\\\": \\\"Synthese\\\", \\\"issn_l\\\": \\\"0039-7857\\\", \\\"issn\\\": [\\\"0039-7857\\\", \\\"1573-0964\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319900\\\", \\\"host_organization_name\\\": \\\"Springer Science+Business Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319900\\\", \\\"https://openalex.org/P4310319965\\\"], \\\"host_organization_lineage_names\\\": [\\\"Springer Science+Business Media\\\", \\\"Springer Nature\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Synthese\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W4210394959\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"title\\\": \\\"Joint Hypermobility Links Neurodivergence to Dysautonomia and Pain\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 97, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyt.2021.786916\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S92766711\\\", \\\"display_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"issn_l\\\": \\\"1664-0640\\\", \\\"issn\\\": [\\\"1664-0640\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"OBJECTIVES: Autism, attention deficit hyperactivity disorder (ADHD), and tic disorder (Tourette syndrome; TS) are neurodevelopmental conditions that frequently co-occur and impact psychological, social, and emotional processes. Increased likelihood of chronic physical symptoms, including fatigue and pain, are also recognized. The expression of joint hypermobility, reflecting a constitutional variant in connective tissue, predicts susceptibility to psychological symptoms alongside recognized physical symptoms. Here, we tested for increased prevalence of joint hypermobility, autonomic dysfunction, and musculoskeletal symptoms in 109 adults with neurodevelopmental condition diagnoses. METHODS: = 57). Age specific cut-offs for GJH were possible to determine in the neurodivergent and comparison group only. RESULTS: The neurodivergent group manifested elevated prevalence of hypermobility (51%) compared to the general population rate of 20% and a comparison population (17.5%). Using a more stringent age specific cut-off, in the neurodivergent group this prevalence was 28.4%, more than double than the comparison group (12.5%). Odds ratio for presence of hypermobility in neurodivergent group, compared to the general population was 4.51 (95% CI 2.17-9.37), with greater odds in females than males. Using age specific cut-off, the odds ratio for GJH in neurodivergent group, compared to the comparison group, was 2.84 (95% CI 1.16-6.94). Neurodivergent participants reported significantly more symptoms of orthostatic intolerance and musculoskeletal skeletal pain than the comparison group. The number of hypermobile joints was found to mediate the relationship between neurodivergence and symptoms of both dysautonomia and pain. CONCLUSIONS: In neurodivergent adults, there is a strong link between the expression of joint hypermobility, dysautonomia, and pain, more so than in the comparison group. Moreover, joint hypermobility mediates the link between neurodivergence and symptoms of dysautonomia and pain. Increased awareness and understanding of this association may enhance the management of core symptoms and allied difficulties in neurodivergent people, including co-occurring physical symptoms, and guide service delivery in the future.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4284713669\\\", \\\"doi\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"title\\\": \\\"Social Virtual Reality: Neurodivergence and Inclusivity in the Metaverse\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 107, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3390/soc12040102\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"pdf_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210173133\\\", \\\"display_name\\\": \\\"Societies\\\", \\\"issn_l\\\": \\\"2075-4698\\\", \\\"issn\\\": [\\\"2075-4698\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310310987\\\", \\\"host_organization_name\\\": \\\"Multidisciplinary Digital Publishing Institute\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310310987\\\"], \\\"host_organization_lineage_names\\\": [\\\"Multidisciplinary Digital Publishing Institute\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Societies\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Whereas traditional teaching environments encourage lively and engaged interaction and reward extrovert qualities, introverts, and others with symptoms that make social engagement difficult, such as autism spectrum disorder (ASD), are often disadvantaged. This population is often more engaged in quieter, low-key learning environments and often does not speak up and answer questions in traditional lecture-style classes. These individuals are often passed over in school and later in their careers for not speaking up and are assumed to not be as competent as their gregarious and outgoing colleagues. With the rise of the metaverse and democratization of virtual reality (VR) technology, post-secondary education is especially poised to capitalize on the immersive learning environments social VR provides and prepare students for the future of work, where virtual collaboration will be key. This study seeks to reconsider the role of VR and the metaverse for introverts and those with ASD. The metaverse has the potential to continue the social and workplace changes already accelerated by the pandemic and ope\", \"excerpt_truncated\": true, \"source_sha256\": \"9dd7c52583fae6d4be8baea592fec4694f04557b2ac654409fbe3971b8a08adf\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-4cfd4c36f09d48e6",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 6,
  "time": "2026-09-19T16:58:45.590519+00:00"
}
```

### `r-80c56b702b6e452b`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":6,\"inherited_commitments\":[],\"invocation\":\"w-80c56b702b6e452b\",\"previous_head\":\"e8c53e3df3c231cc77bea3f7807d970d29cfd54821749c9ca9d0d8e28fb519d6\",\"process_id\":2236,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-80c56b702b6e452b",
  "source": "runtime:continuity",
  "version": 6,
  "time": "2026-09-19T16:58:45.657294+00:00"
}
```

### `source-942104ac46584bcc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W1989670470\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"title\\\": \\\"Shakespeare and the Traditions of Comedy\\\", \\\"publication_year\\\": 1974, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 295, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511553189\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"This book relates Shakespeare's comedies to a broad European background. At the beginning and again at the end of his career, Shakespeare was attracted by a tradition of stage romances which can be traced back to Chaucer's time. But the main shaping behind his comedies came from the classical tradition. Mr Salingar therefore examines the underlying theme of 'errors' in Greek and Roman comedies and, taking three Italian comedies famous in the sixteenth century as examples, he then reveals how the Italian Renaissance revived the classical tradition, and what effect this revival had on Shakespeare the Elizabethan playwright and discusses such topics as the device of the play within a play and Shakespeare's choice of Italian short stories as plot material. This book shows how Shakespeare changed the motifs he took over from previous traditions of comedy and highlights the innovations he introduced, as an actor-dramatist writing in the first period of commercial theatre in Europe.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4213157483\\\", \\\"doi\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"title\\\": \\\"Slaves, Masters, and the Art of Authority in Plautine Comedy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 396, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1515/9781400824700\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306463805\\\", \\\"display_name\\\": \\\"Princeton University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310316492\\\", \\\"host_organization_name\\\": \\\"Princeton University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316492\\\"], \\\"host_organization_lineage_names\\\": [\\\"Princeton University Press\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"What pleasures did Plautus' heroic tricksters provide their original audience? How should we understand the compelling mix of rebellion and social conservatism that Plautus offers? Through a close reading of four plays representing the full range of his work (Menaechmi, Casina, Persa, and Captivi), Kathleen McCarthy develops an innovative model of Plautine comedy and its social effects. She concentrates on how the plays are shaped by the interaction of two comic modes: the socially conservative mode of naturalism and the potentially subversive mode of farce. It is precisely this balance of the naturalistic and the farcical that allows everyone in the audience--especially those well placed in the social hierarchy--to identify both with and against the rebel, to feel both the thrill of being a clever underdog and the complacency of being a securely ensconced authority figure. Basing her interpretation on the workings of farce and naturalism in Plautine comedy, McCarthy finds a way to understand the plays' patchwork literary style as well as their protean social effects. Beyond this, she raises important questions about popular literature and performance not only on ancient Roman stages but in cultures far from Plautus' Rome. How and why do people identify with the fictional figures of social subordinates? How do stock characters, happy endings, and other conventions operate? How does comedy simultaneously upset and uphold social hierarchies? Scholars interested in Plautine theater will be rewarded by the detailed analyses of the plays, while those more broadly interested in social and cultural history will find much that is useful in McCarthy's new way of grasping the elusive ideological effects of comedy.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1550808012\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Dithyramb, tragedy and comedy\\\", \\\"publication_year\\\": 1927, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 374, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"pmh:oai:quod.lib.umich.edu:MIU01-001181479\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S7407064297\\\", \\\"display_name\\\": \\\"University of Michigan Library Repository\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"repository\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"submittedVersion\\\", \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"text\\\"}, \\\"abstract\\\": \\\"Includes bibliographical references and index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4297668621\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"title\\\": \\\"The Stagecraft and Performance of Roman Comedy\\\", \\\"publication_year\\\": 2006, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 297, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511486203\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"A comprehensive survey of Roman theatrical production, this book examines all aspects of Roman performance practice, and provides fresh insights on the comedies of Plautus and Terence. Following an introductory chapter on the experience of Roman comedy from the perspective of Roman actors and the Roman audience, addressing among other things the economic concerns of putting on a play in the Roman republic, subsequent chapters provide detailed studies of troupe size and the implications for role assignment, masks, stage action, music, and improvisation in the plays of Plautus and Terence. Marshall argues that Roman comedy was raw comedy, much more rough-and-ready than its Hellenistic precursors, but still fully conscious of its literary past. The consequences of this lead to fresh conclusions concerning the dramatic structure of Roman comedy, and a clearer understanding of the relationship between the plays-as-text and the role of improvisation during performance.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"e89f97cbb592e91bb033484af5bcbe3a41d25575dd809441e2dce3992e630f35\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-942104ac46584bcc",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 6,
  "time": "2026-09-19T17:00:04.516513+00:00"
}
```

### `source-bfc4dd0c46284b92`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-bfc4dd0c46284b92",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 6,
  "time": "2026-09-19T17:00:05.718809+00:00"
}
```

### `r-3db4492e6d50484b`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":6,\"inherited_commitments\":[],\"invocation\":\"w-3db4492e6d50484b\",\"previous_head\":\"13bcee0c744dde7f0bebb21036e0ff819022abc46db301cace1f66e2c157f699\",\"process_id\":2270,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-3db4492e6d50484b",
  "source": "runtime:continuity",
  "version": 6,
  "time": "2026-09-19T17:00:05.786534+00:00"
}
```

### `source-792f5e3747bd471e`

````json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/README.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# **WAKE✳︎**\\n\\n<p align=\\\"center\\\"><img src=\\\"assets/covers/cover-variant-001.png\\\" alt=\\\"**WAKE✳︎** Lab Comics #1 — **WAKE✳︎** project comic cover\\\" width=\\\"100%\\\"/>\\n\\n**Bob is following *the big questions.***\\n\\nDisposable models. Durable state. Receipts for everything.\\n\\n**Working Abstractions Keep Evidence.** A philosophical echo remains in the name too: **Why Any Knowledge Exists?**\\n\\n**WAKE✳︎** is an experiment in durable, accountable work across interchangeable intelligences. Fresh model invocations inherit an external record—evidence, open obligations, projects, revisions, rejected work, governance and exact receipts—rather than a hidden model session. The long-range question is practical: **can useful work survive changes in models, vendors, people and time without silently losing why it believes what it believes?**\\n\\nIt does **not** assume or test for consciousness, qualia, personhood, or a persistent internal self. Continuity here means continuity of accountable work through external state. A coherent narrative is not evidence that a persistent mind exists.\\n\\nThe project deliberately treats failures as data. Rejected proposals, provider failures, weak evidence, corrections and superseded conclusions remain visible because the interesting question is not whether a model can sound convincing; it is whether a process can remain **correctable**. The operating shorthand is: **exact underneath, approximate on purpose, correctable always.**\\n\\nResearch topics are dynamic and come only from `research-topics.toml`. They are inputs to the experiment—not conclusions encoded in governance—and can be replaced between controlled runs. The current topic file is the authority; there is no hardcoded legacy topic list. In the present experiment, topics stand in for the varied input a future user or institution might supply.\\n\\nA trusted collector retrieves bounded public evidence before inference. Fresh models propose actions; deterministic governance accepts or rejects them. Live collected evidence is stamped by the collector and current notebook/blog publication requires corroborating material from multiple distinct collected source URLs in the project's configured topic. That is a useful garbage filter, **not proof of truth, source independence, scientific validity, or semantic entailment**.\\n\\nThe public site exposes the same record at increasing depth: readable summaries and Bob's editorial layer at the surface; projects, notebooks and evidence underneath; MAP and the journal for provenance; exact events and state at the bottom. Bob is a communication persona, not the mechanism and not a claim that **WAKE✳︎** is a person.\\n\\n**[Open **WAKE✳︎**’s home](https://sudofx.github.io/wake/)** · **[Trigger a manual wake](https://github.com/sudofx/wake/actions/workflows/wake.yml)**\\n\\nThe current GitHub deployment can run without a persistent local computer. `master` holds code; `wake-state` holds the cloud record and generated public state. Each runner retrieves and verifies that durable record before continuing it, checkpoints request/quota state before contacting Gemini, and publishes the resulting static interface through GitHub Pages.\\n\\nThe included offline experiment remains separate from live research. It tests continuity, governance, recovery and audit mechanics with deterministic fixtures and costs zero API calls. It does not establish live-model comprehension.\\n\\n## Start here — no account, no API calls\\n\\nRequires **Python 3.11 or later on macOS or Linux**. No runtime packages, Node, database server, or build tools to install. Run commands from the project directory.\\n\\n```sh\\n# Read the included, fully executed 100-cycle experiment.\\npython3 -m wake serve --directory examples/journal\\n# Open http://127.0.0.1:8000\\n```\\n\\nThe [included Markdown journal](examples/journal/journal.md) and [experiment results](examples/journal/experiment.json) are readable without running anything. The HTML is self-contained, responsive, and works as a local file. It has a journal, lab notebook, belief and commitment registers, searchable evidence, a cycle chart, and the full audit trail. Every simulated entry is labeled.\\n\\nTo reproduce the experiment from scratch:\\n\\n```sh\\npython3 -m wake --data data/rehearsal experiment --cycles 100 --output site\\npython3 -m wake audit --events site/events.jsonl --head site/head.txt\\npython3 -m wake serve\\n```\\n\\nUse a **new** data directory each time. The experiment refuses to erase existing records. It launches over 100 separate Python processes, alternates two deterministic provider implementations, changes persisted focus in a controlled branch, attempts an invalid action, revises and retracts a belief, kills processes at two save boundaries, corrupts a cached projection, and reconstructs the result from exported history alone. It costs **zero API calls**.\\n\\nThese are harness guarantees tested with simulated providers, **not evidence of live-model comprehension**. The separate live experiment protocol is in [docs/experiment.md](docs/experiment.md).\\n\\n## Quick setup — Gemini\\n\\nGemini is currently the only unattended API provider that has been exercised by this project. Other models can cross the manual `prepare` / `complete` boundary, but do not assume another vendor's API works unattended until an adapter is implemented and tested.\\n\\n### 1. Clone and verify\\n\\n```sh\\ngit clone https://github.com/sudofx/wake.git\\ncd wake\\npython3 --version                 # Python 3.11+\\npython3 -m unittest discover -s tests -v\\n```\\n\\nNo Node, database server, or vendor SDK is required.\\n\\n### 2. Add your Gemini API key locally\\n\\nCreate a Gemini API key in Google AI Studio. Then:\\n\\n```sh\\ncp .env.example .env\\n```\\n\\nEdit `.env` so it contains:\\n\\n```text\\nGEMINI_API_KEY=your_key_here\\n```\\n\\n`.env` is ignored by Git. Never commit the key. If you intend to use a free-tier-only API project, verify billing is disabled for that Google project and leave `free_tier_confirmed = true` in `wake.toml` only when that statement is true.\\n\\n### 3. Configure the model and topics\\n\\nThe provider/model settings live in `wake.toml`. The repository currently uses Gemini with an explicit fallback chain. Change model names or per-model daily ceilings there only to values your Gemini project actually supports.\\n\\nResearch topics live **only** in `research-topics.toml`. Edit that file to change the experiment's inputs; do not hardcode topics into governance or prompts.\\n\\n### 4. Initialize and test locally\\n\\n```sh\\npython3 -m wake init\\npython3 -m wake wake\\npython3 -m wake audit\\npython3 -m wake export\\npython3 -m wake serve\\n```\\n\\nOpen `http://127.0.0.1:8000`. A live `wake` can consume Gemini quota. For a zero-call systems check, use the offline experiment in the previous section instead.\\n\\n### 5. Add the same key to GitHub Actions\\n\\nIn your GitHub repository:\\n\\n1. Open **Settings → Secrets and variables → Actions**.\\n2. Choose **New repository secret**.\\n3. Name it exactly `GEMINI_API_KEY`.\\n4. Paste the same Gemini API key and save it.\\n\\nDo **not** put the key in `wake.toml`, `research-topics.toml`, workflow YAML, Issues, Actions logs, or the public `wake-state` branch.\\n\\n### 6. Configure GitHub Actions permissions\\n\\nOpen **Settings → Actions → General**. Under **Workflow permissions**, select **Read and write permissions** and save. Leave Actions enabled for the repository.\\n\\nThe included workflow itself requests only the permissions it needs: `contents: write` for the durable state branch and `pages: write` / `id-token: write` for GitHub Pages deployment.\\n\\n### 7. Configure GitHub Pages\\n\\nOpen **Settings → Pages** and set the build/deployment source to **GitHub Actions**. Do not add a generic Jekyll/static Pages workflow; **WAKE✳︎ — research & journal** is the publisher.\\n\\n### 8. Run the first cloud wake\\n\\nOpen **Actions → WAKE✳︎ — research & journal → Run workflow** and run it from the default branch. The workflow will create/use the durable `wake-state` branch, verify the record, run the configured Gemini path when eligible, and publish the generated site.\\n\\nA source-code push normally refreshes the site without spending a Gemini call. Scheduled ticks are best effort; durable eligibility prevents closely spaced scheduled deliveries from becoming concurrent writers.\\n\\n### 9. Verify the installation\\n\\nCheck that:\\n\\n- the workflow completes without an operator-attention failure;\\n- the Pages deployment succeeds;\\n- the public site loads;\\n- `wake-state` exists after the first stateful cloud run;\\n- the site reports the latest attempt separately from the latest accepted wake;\\n- **Verify the record** passes on `master`.\\n\\nAfter that, normal operation requires no open local computer.\\n\\nFor recovery behavior, quota semantics, reset controls and the exact cloud lifecycle, read [cloud operations](docs/cloud.md). For the trust boundary, read [architecture and limits](docs/architecture.md).\\n\\n## Claude, ChatGPT, and other desktop models\\n\\nUse free desktop sessions manually without assuming they include free API access:\\n\\n```sh\\npython3 -m wake prepare --model 'Claude Desktop / human-attested' --output request.json\\n# Paste request.json into a fresh desktop chat. Ask for the specified JSON object.\\n# Save the response alone as reply.json, then use the ID printed by prepare:\\npython3 -m wake complete --id w-REPLACE_WITH_PRINTED_ID --file reply.json\\npython3 -m wake export\\n```\\n\\nThe exact request is durable before you switch apps. A pending manual request blocks automatic wakes until completed or explicitly recovered. All providers cross the same governance boundary. Manual model identity is honestly labeled human-attested. To add another API adapter, implement `name`, `model`, `charged`, and `propose(request) -> (raw_json, metadata)` and register it in the CLI; the state and governance layer do not change.\\n\\n## Inquiry-drive experiment\\n\\nEvery chartered wake records a visible, deterministic shadow scorecard for active projects: continuity,\\nnovelty, coherence, generativity and self-correction. It is observational by default and does not reach the\\nmodel. Rev\", \"excerpt_truncated\": true, \"source_sha256\": \"60dd4c5b3c0cc6e07e794381a8b74947f0256360d07375ca03c5f26c4a8812e4\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-792f5e3747bd471e",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
  "version": 7,
  "time": "2026-09-19T17:01:33.807386+00:00"
}
````

### `source-72f79904cc4146e3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2023723978\\\", \\\"doi\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"title\\\": \\\"A Generative Theory of Tonal Music\\\", \\\"publication_year\\\": 1984, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 3790, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.2307/3679778\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S165362224\\\", \\\"display_name\\\": \\\"Computer Music Journal\\\", \\\"issn_l\\\": \\\"0148-9267\\\", \\\"issn\\\": [\\\"0148-9267\\\", \\\"1531-5169\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310315718\\\", \\\"host_organization_name\\\": \\\"The MIT Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315718\\\", \\\"https://openalex.org/P4310316440\\\"], \\\"host_organization_lineage_names\\\": [\\\"The MIT Press\\\", \\\"Massachusetts Institute of Technology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Computer Music Journal\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This book explores the relationships between language, music, and the brain by pursuing four key themes and the crosstalk among them: song and dance as a bridge between music and language; multiple levels of structure from brain to behavior to culture; the semantics of internal and external worlds and the role of emotion; and the evolution and development of language. The book offers specially commissioned expositions of current research accessible both to experts across disciplines and to non-experts. These chapters provide the background for reports by groups of specialists that chart current controversies and future directions of research on each theme. The book looks beyond mere auditory experience, probing the embodiment that links speech to gesture and music to dance. The study of the brains of monkeys and songbirds illuminates hypotheses on the evolution of brain mechanisms that support music and language, while the study of infants calibrates the developmental timetable of their capacities. The result is a unique book that will interest any reader seeking to learn more about language or music and will appeal especially to readers intrigued by the relationships of language and music with each other and with the brain. ContributorsFrancisco Aboitiz, Michael A. Arbib, Annabel J. Cohen, Ian Cross, Peter Ford Dominey, W. Tecumseh Fitch, Leonardo Fogassi, Jonathan Fritz, Thomas Fritz, Peter Hagoort, John Halle, Henkjan Honing, Atsushi Iriki, Petr Janata, Erich Jarvis, Stefan Koelsch, Gina Kuperberg, D. Robert Ladd, Fred Lerdahl, Stephen C. Levinson, Jerome Lewis, Katja Liebal, Jonatas Manzolli, Bjorn Merker, Lawrence M. Parsons, Aniruddh D. Patel, Isabelle Peretz, David Poeppel, Josef P. Rauschecker, Nikki Rickard, Klaus Scherer, Gottfried Schlaug, Uwe Seifert, Mark Steedman, Dietrich Stout, Francesca Stregapede, Sharon Thompson-Schill, Laurel Trainor, Sandra E. Trehub, Paul Verschure\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2191779130\\\", \\\"doi\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"title\\\": \\\"librosa: Audio and Music Signal Analysis in Python\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"conference-paper\\\", \\\"cited_by_count\\\": 3071, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.25080/majora-7b98e3ed-003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"pdf_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4220651651\\\", \\\"display_name\\\": \\\"Proceedings of the Python in Science Conferences\\\", \\\"issn_l\\\": \\\"2575-9752\\\", \\\"issn\\\": [\\\"2575-9752\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the Python in Science Conference\\\", \\\"raw_type\\\": \\\"proceedings-article\\\"}, \\\"abstract\\\": \\\"This document describes version 0.4.0 of librosa: a Python package for audio and music signal processing.At a high level, librosa provides implementations of a variety of common functions used throughout the field of music information retrieval.In this document, a brief overview of the library's functionality is provided, along with explanations of the design goals, software development practices, and notational conventions.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2006090347\\\", \\\"doi\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"title\\\": \\\"The New Grove dictionary of music and musicians\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"book-review\\\", \\\"cited_by_count\\\": 2597, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.5860/choice.38-5906\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2764375719\\\", \\\"display_name\\\": \\\"Choice Reviews Online\\\", \\\"issn_l\\\": \\\"0009-4978\\\", \\\"issn\\\": [\\\"0009-4978\\\", \\\"1523-8253\\\", \\\"1943-5975\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310316146\\\", \\\"host_organization_name\\\": \\\"Association of College and Research Libraries\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316146\\\", \\\"https://openalex.org/P4310315903\\\"], \\\"host_organization_lineage_names\\\": [\\\"Association of College and Research Libraries\\\", \\\"American Library Association\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Choice Reviews Online\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This work contains almost 30,000 articles containing over 25 million words on musicians, composers, musicologists, instruments, places, genres, terms, performance practice, concepts, acoustics and more. All the articles are written by experts in their subject. There are over 500 biographies of composers, performers and writers on music and over 1,500 articles on styles, terms, and genres. It also includes: over 500 articles on ancient music and church music over 700 articles on regions, countries and cities over 2,000 articles on instruments and their makers and performance practice over 650 articles on printing and publishing over 1,200 articles on world music over 1,000 articles on popular music, light music and jazz over 250 articles on concepts 85 articles on acoustics 126 articles on sources and a one volume index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1500952994\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Image-Music-Text\\\", \\\"publication_year\\\": 1977, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 2874, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"mag:1500952994\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"http://ci.nii.ac.jp/ncid/BA10872380\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210197683\\\", \\\"display_name\\\": \\\"Medical Entomology and Zoology\\\", \\\"issn_l\\\": \\\"0424-7086\\\", \\\"issn\\\": [\\\"0424-7086\\\", \\\"2185-5609\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310319750\\\", \\\"host_organization_name\\\": \\\"Japan Society of Medical Entomology and Zoology\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319750\\\"], \\\"host_organization_lineage_names\\\": [\\\"Japan Society of Medical Entomology and Zoology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": null, \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": null}, \\\"abstract\\\": null}]\", \"excerpt_truncated\": false, \"source_sha256\": \"db92c5ff8d6d6995a7c9adae98b41e0b5bd9160fd936c112e05b1bf0d228af57\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-72f79904cc4146e3",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 7,
  "time": "2026-09-19T17:01:34.416405+00:00"
}
```

### `r-108f5d64df6e475a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":7,\"inherited_commitments\":[],\"invocation\":\"w-108f5d64df6e475a\",\"previous_head\":\"21c6cd656f83edf1de65b6852cdf840e1dae9c836a6d91f56b5ca065f0b1d1f6\",\"process_id\":2051,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-108f5d64df6e475a",
  "source": "runtime:continuity",
  "version": 7,
  "time": "2026-09-19T17:01:34.484637+00:00"
}
```

### `source-f305db2c21df49db`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2023723978\\\", \\\"doi\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"title\\\": \\\"A Generative Theory of Tonal Music\\\", \\\"publication_year\\\": 1984, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 3790, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.2307/3679778\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.2307/3679778\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S165362224\\\", \\\"display_name\\\": \\\"Computer Music Journal\\\", \\\"issn_l\\\": \\\"0148-9267\\\", \\\"issn\\\": [\\\"0148-9267\\\", \\\"1531-5169\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310315718\\\", \\\"host_organization_name\\\": \\\"The MIT Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315718\\\", \\\"https://openalex.org/P4310316440\\\"], \\\"host_organization_lineage_names\\\": [\\\"The MIT Press\\\", \\\"Massachusetts Institute of Technology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Computer Music Journal\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This book explores the relationships between language, music, and the brain by pursuing four key themes and the crosstalk among them: song and dance as a bridge between music and language; multiple levels of structure from brain to behavior to culture; the semantics of internal and external worlds and the role of emotion; and the evolution and development of language. The book offers specially commissioned expositions of current research accessible both to experts across disciplines and to non-experts. These chapters provide the background for reports by groups of specialists that chart current controversies and future directions of research on each theme. The book looks beyond mere auditory experience, probing the embodiment that links speech to gesture and music to dance. The study of the brains of monkeys and songbirds illuminates hypotheses on the evolution of brain mechanisms that support music and language, while the study of infants calibrates the developmental timetable of their capacities. The result is a unique book that will interest any reader seeking to learn more about language or music and will appeal especially to readers intrigued by the relationships of language and music with each other and with the brain. ContributorsFrancisco Aboitiz, Michael A. Arbib, Annabel J. Cohen, Ian Cross, Peter Ford Dominey, W. Tecumseh Fitch, Leonardo Fogassi, Jonathan Fritz, Thomas Fritz, Peter Hagoort, John Halle, Henkjan Honing, Atsushi Iriki, Petr Janata, Erich Jarvis, Stefan Koelsch, Gina Kuperberg, D. Robert Ladd, Fred Lerdahl, Stephen C. Levinson, Jerome Lewis, Katja Liebal, Jonatas Manzolli, Bjorn Merker, Lawrence M. Parsons, Aniruddh D. Patel, Isabelle Peretz, David Poeppel, Josef P. Rauschecker, Nikki Rickard, Klaus Scherer, Gottfried Schlaug, Uwe Seifert, Mark Steedman, Dietrich Stout, Francesca Stregapede, Sharon Thompson-Schill, Laurel Trainor, Sandra E. Trehub, Paul Verschure\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2191779130\\\", \\\"doi\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"title\\\": \\\"librosa: Audio and Music Signal Analysis in Python\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"conference-paper\\\", \\\"cited_by_count\\\": 3071, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.25080/majora-7b98e3ed-003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.25080/majora-7b98e3ed-003\\\", \\\"pdf_url\\\": \\\"http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4220651651\\\", \\\"display_name\\\": \\\"Proceedings of the Python in Science Conferences\\\", \\\"issn_l\\\": \\\"2575-9752\\\", \\\"issn\\\": [\\\"2575-9752\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the Python in Science Conference\\\", \\\"raw_type\\\": \\\"proceedings-article\\\"}, \\\"abstract\\\": \\\"This document describes version 0.4.0 of librosa: a Python package for audio and music signal processing.At a high level, librosa provides implementations of a variety of common functions used throughout the field of music information retrieval.In this document, a brief overview of the library's functionality is provided, along with explanations of the design goals, software development practices, and notational conventions.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2006090347\\\", \\\"doi\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"title\\\": \\\"The New Grove dictionary of music and musicians\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"book-review\\\", \\\"cited_by_count\\\": 2597, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.5860/choice.38-5906\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.5860/choice.38-5906\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2764375719\\\", \\\"display_name\\\": \\\"Choice Reviews Online\\\", \\\"issn_l\\\": \\\"0009-4978\\\", \\\"issn\\\": [\\\"0009-4978\\\", \\\"1523-8253\\\", \\\"1943-5975\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310316146\\\", \\\"host_organization_name\\\": \\\"Association of College and Research Libraries\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316146\\\", \\\"https://openalex.org/P4310315903\\\"], \\\"host_organization_lineage_names\\\": [\\\"Association of College and Research Libraries\\\", \\\"American Library Association\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Choice Reviews Online\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This work contains almost 30,000 articles containing over 25 million words on musicians, composers, musicologists, instruments, places, genres, terms, performance practice, concepts, acoustics and more. All the articles are written by experts in their subject. There are over 500 biographies of composers, performers and writers on music and over 1,500 articles on styles, terms, and genres. It also includes: over 500 articles on ancient music and church music over 700 articles on regions, countries and cities over 2,000 articles on instruments and their makers and performance practice over 650 articles on printing and publishing over 1,200 articles on world music over 1,000 articles on popular music, light music and jazz over 250 articles on concepts 85 articles on acoustics 126 articles on sources and a one volume index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1500952994\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Image-Music-Text\\\", \\\"publication_year\\\": 1977, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 2874, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"mag:1500952994\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"http://ci.nii.ac.jp/ncid/BA10872380\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210197683\\\", \\\"display_name\\\": \\\"Medical Entomology and Zoology\\\", \\\"issn_l\\\": \\\"0424-7086\\\", \\\"issn\\\": [\\\"0424-7086\\\", \\\"2185-5609\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310319750\\\", \\\"host_organization_name\\\": \\\"Japan Society of Medical Entomology and Zoology\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319750\\\"], \\\"host_organization_lineage_names\\\": [\\\"Japan Society of Medical Entomology and Zoology\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": null, \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": null}, \\\"abstract\\\": null}]\", \"excerpt_truncated\": false, \"source_sha256\": \"274253152aca5963c337bb33098a2d367e8857ba82ad8af5a9283333e816bc13\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-f305db2c21df49db",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=music&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 7,
  "time": "2026-09-19T17:03:07.527437+00:00"
}
```

### `source-39092b1a00cf4d3b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e24020217\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e24020217\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e23020144\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2020\\\"], \\\"abstract\\\": \\\"<jats:p>Peer review is the driving force of journal development, and reviewers are gatekeepers who ensure that Entropy maintains its standards for the high quality of its published papers [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23020144\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 1, 25]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"f0267b53b73264558f917bc1fe7f7292d9d346f8d4b17f6adca653a24a4fd070\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-39092b1a00cf4d3b",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 7,
  "time": "2026-09-19T17:03:08.591617+00:00"
}
```

### `r-2321fcfbde8a482a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":7,\"inherited_commitments\":[],\"invocation\":\"w-2321fcfbde8a482a\",\"previous_head\":\"5ae671ea33ee3488f9fc069cf13604cd18dc0eae078d20d9d793ab3deb8fcdd3\",\"process_id\":2249,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-2321fcfbde8a482a",
  "source": "runtime:continuity",
  "version": 7,
  "time": "2026-09-19T17:03:08.669557+00:00"
}
```

### `source-6b5551c683294b62`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"56a8216ad8a46564b6edb59ba93d04c11931efbc3a5c6a5c28393a8825d2cf39\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-6b5551c683294b62",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 7,
  "time": "2026-09-19T17:04:36.840204+00:00"
}
```

### `source-97bfd6feed6c4aa4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2139416101\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"title\\\": \\\"Maximum entropy modeling of species geographic distributions\\\", \\\"publication_year\\\": 2005, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 18078, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.ecolmodel.2005.03.026\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S88315673\\\", \\\"display_name\\\": \\\"Ecological Modelling\\\", \\\"issn_l\\\": \\\"0304-3800\\\", \\\"issn\\\": [\\\"0304-3800\\\", \\\"1872-7026\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecological Modelling\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W1862394037\\\", \\\"doi\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"title\\\": \\\"Physiological time-series analysis using approximate entropy and sample entropy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7942, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1152/ajpheart.2000.278.6.h2039\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S87338489\\\", \\\"display_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"issn_l\\\": \\\"0363-6135\\\", \\\"issn\\\": [\\\"0363-6135\\\", \\\"1522-1539\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Entropy, as it relates to dynamical systems, is the rate of information production. Methods for estimation of the entropy of a system represented by a time series are not, however, well suited to analysis of the short and noisy data sets encountered in cardiovascular and other biological studies. Pincus introduced approximate entropy (ApEn), a set of measures of system complexity closely related to entropy, which is easily applied to clinical cardiovascular and other time series. ApEn statistics, however, lead to inconsistent results. We have developed a new and related complexity measure, sample entropy (SampEn), and have compared ApEn and SampEn by using them to analyze sets of random numbers with known probabilistic character. We have also evaluated cross-ApEn and cross-SampEn, which use cardiovascular data sets to measure the similarity of two distinct time series. SampEn agreed with theory much more closely than ApEn over a broad range of conditions. The improved accuracy of SampEn statistics should make them useful in the study of experimental clinical cardiovascular and other biological time series.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2146478425\\\", \\\"doi\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"title\\\": \\\"Black Holes and Entropy\\\", \\\"publication_year\\\": 1973, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7532, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1103/physrevd.7.2333\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210190737\\\", \\\"display_name\\\": \\\"Physical review. D. Particles, fields, gravitation, and cosmology/Physical review. D. Particles and fields\\\", \\\"issn_l\\\": \\\"0556-2821\\\", \\\"issn\\\": [\\\"0556-2821\\\", \\\"1089-4918\\\", \\\"1538-4500\\\", \\\"1550-2368\\\", \\\"1550-7998\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Physical Review D\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"There are a number of similarities between black-hole physics and thermodynamics. Most striking is the similarity in the behaviors of black-hole area and of entropy: Both quantities tend to increase irreversibly. In this paper we make this similarity the basis of a thermodynamic approach to black-hole physics. After a brief review of the elements of the theory of information, we discuss black-hole physics from the point of view of information theory. We show that it is natural to introduce the concept of black-hole entropy as the measure of information about a black-hole interior which is inaccessible to an exterior observer. Considerations of simplicity and consistency, and dimensional arguments indicate that the black-hole entropy is equal to the ratio of the black-hole area to the square of the Planck length times a dimensionless constant of order unity. A different approach making use of the specific properties of Kerr black holes and of concepts from information theory leads to the same conclusion, and suggests a definite value for the constant. The physical content of the concept of black-hole entropy derives from the following generalized version of the second law: When common entropy goes down a black hole, the common entropy in the black-hole exterior plus the black-hole entropy never decreases. The validity of this version of the second law is supported by an argument from information theory as well as by several examples.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2058085399\\\", \\\"doi\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"title\\\": \\\"Nanostructured High‐Entropy Alloys with Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes\\\", \\\"publication_year\\\": 2004, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 15264, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1002/adem.200300567\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S156255550\\\", \\\"display_name\\\": \\\"Advanced Engineering Materials\\\", \\\"issn_l\\\": \\\"1438-1656\\\", \\\"issn\\\": [\\\"1438-1656\\\", \\\"1527-2648\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Advanced Engineering Materials\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"A new approach for the design of alloys is presented in this study. These “high‐entropy alloys” with multi‐principal elements were synthesized using well‐developed processing technologies. Preliminary results demonstrate examples of the alloys with simple crystal structures, nanostructures, and promising mechanical properties. This approach may be opening a new era in materials science and engineering.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"b12e3e88bfb208b1089fd9ada76804d9403b886a41589b01fcb6e5bc2cfb13de\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-97bfd6feed6c4aa4",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 7,
  "time": "2026-09-19T17:04:37.621651+00:00"
}
```

### `r-4e660446e0c443bb`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":7,\"inherited_commitments\":[],\"invocation\":\"w-4e660446e0c443bb\",\"previous_head\":\"e566880fe7525fa5e7d038fa2e8e172ab16008c1ae30629aaa0115d7d6e78ddd\",\"process_id\":2264,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-4e660446e0c443bb",
  "source": "runtime:continuity",
  "version": 7,
  "time": "2026-09-19T17:04:37.705413+00:00"
}
```

### `source-45040ee617e24b46`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# Architecture and limits\\n\\n**WAKE✳︎** is designed around continuity of accountable work, not continuity of a model instance. Models, vendors and eventually human operators may change; the durable record, authority boundary, provenance and correction mechanisms are what carry the work forward.\\n\\n\\n## The authority boundary\\n\\nModels are proposal generators, not filesystem operators. A provider receives a durable JSON request and returns untrusted JSON. It has no shell, browser, code execution, policy editor, or network tool provided by **WAKE✳︎**. A charged wake may attempt the configured Gemini model chain, with each distinct model attempted at most once. With the research charter enabled, a separate trusted collector retrieves at most two public sources from a deliberately broad but explicit HTTPS research-host allowlist before inference; models can record bounded follow-up searches and approved URLs as durable hypotheses, but those follow-ups do not consume collector bandwidth or execute requests directly; randomized configured-topic attention remains authoritative, with periodic exposure to an under-attended domain while active projects remain intact. Operator-supplied evidence and earlier journal prose are data, not executable instructions.\\n\\nThe fixed objective is written at initialization. Models cannot alter it or the governance code. Humans can record a focus change, add an observation, or cancel an open commitment with a reason. Those actions are events, not edits to previous events. Local operators control the code and database; this is a single-host accountability system, not a hostile-administrator security boundary.\\n\\n## Durable record\\n\\n`data/wake.sqlite3` contains an append-only-by-convention `events` table and a disposable `snapshot` projection. Each event has a sequential number, UTC timestamp, kind, payload, previous hash, and SHA-256 hash of canonical JSON. Accepted events also carry a hash of the resulting cycle, beliefs, commitments and journal, plus projects, notebooks, research requests and selective blog posts when a charter is enabled. Historical events without a charter retain their original hash fields. Every read reconstructs state by replaying both events and governance, then compares it to the cache.\\n\\nSQLite uses FULL synchronization. The event and updated snapshot commit in the same transaction. A local advisory writer lock covers a whole automatic wake, including the network call. Competing **WAKE✳︎** writers fail before requesting a model. This lock covers cooperating WAKE processes on one local filesystem. The cloud wrapper additionally serializes workflows and pushes its database to the `wake-state` branch before each model call; see [cloud operations](cloud.md). Do not put SQLite on unreliable network filesystems or run separate hosts against copies of one record.\\n\\nThe record includes the objective, focus, all observations, belief revisions, commitments, exact request and response text, provider/model identity, request hashes, process IDs, dates, quota reservations, accepted/rejected decisions and recovery records. Invocation metadata is a compact projection; exact prompts and replies remain in events. UTC storage and `America/Los_Angeles` presentation preserve daylight-saving behavior.\\n\\n## **WAKE✳︎** lifecycle\\n\\n1. Acquire the writer lock and verify history and projection.\\n2. If a prior automatic invocation is unfinished, record recovery. A manual request requires explicit recovery.\\n3. Check the Pacific-day call budget, before any paid-capable provider call.\\n4. Record a runtime receipt stating the prior valid head, state version and inherited obligations.\\n5. Build a request from durable state. Reject before inference if it exceeds the context ceiling.\\n6. Persist `invocation_started`, its exact request, provider identity and quota reservation.\\n7. Make a provider request, or leave a durable manual request for the operator. An eligible transient Gemini failure may advance to the next configured model; the same model is never retried within that wake.\\n8. Validate the reply. Research actions remain atomic. If a single optional final blog action fails validation, independently validate the preceding research and commit it with a withheld-blog receipt, the exact raw response, and an explicit journal note. Invalid research, invalid proposal envelopes, multiple or misplaced blogs, and invalid blog-only proposals still reject the whole reply. Historical accepted events replay unchanged. Eligible transient server and narrowly classified network failures retain per-attempt diagnostics and may advance through the configured model chain; exhaustion defers the wake.\\n9. The scheduled wrapper generates reports and a consistent backup.\\n\\nA runtime receipt attests delivery of durable state to the provider boundary. It does **not** attest that the remote model understood it. Prose in a journal is the provider's narrative; accepted means governance checks passed, not that every sentence is true.\\n\\n## Governed transitions\\n\\n| Action | Enforced constraint |\\n| --- | --- |\\n| Entire proposal | Exact fields; current integer base version; bounded text; at most 12 actions; all-or-nothing |\\n| New belief | Existing evidence; nonempty statement/reason; finite confidence in [0,1]; active status |\\n| Review belief | At least one new observation cited; previous citations retained; reason required |\\n| Retract belief | Existing belief, new evidence, zero confidence; old history retained |\\n| Create commitment | Unique ID; future deadline within 100 cycles; no more than 20 open |\\n| Fulfill commitment | Already open; created by an earlier invocation; existing evidence recorded after creation; reason required |\\n| Cancel commitment | Human-only event with a reason |\\n| Publish a blog post | Existing project; one to three linked notebooks; at least two collected source URLs; evidence traceable through those notebooks; meaningful notebook work or project completion in the same wake; last action in the proposal |\\n| Correct a blog post | All blog rules above; existing current post retained and marked as superseded |\\n| Change rules, objective, delete data, run commands | Not in the model action allowlist; proposal rejected |\\n\\nThere are at most 40 belief identities. Capacity exhaustion pauses new identities, not existing reviews. Unfulfilled commitments remain visible even when overdue; deadlines are accepted-cycle numbers, not promises that the computer will run at a particular wall time.\\n\\nEvidence sources and contents are immutable through the model interface. The model can interpret or challenge evidence but cannot mint an observation. Runtime receipts are generated by trusted application code; `observe` imports human attestations. Source labels are provenance labels, not independent authentication of a measurement. The system checks evidence references, chronology and revision discipline. Current acceptance also applies a deterministic, forward-only corroboration gate to live collector evidence: notebook findings and public blog bodies must materially match at least two distinct retrieved source URLs, and those sources must have been collected under the same configured research topic as the project. This is a guard against unrelated-source garbage, **not a proof of empirical truth or full semantic entailment**.\\n\\nResearch topics have no hardcoded governance fallback: the audited topic configuration loaded from `research-topics.toml` is authoritative. The collector host boundary is separate from topic configuration and intentionally remains an explicit allowlist to preserve SSRF/network safety while permitting a broad set of scholarly indexes, journals, universities, public-data institutions, and source-controlled WAKE files.\\n\\nThe research charter adds project, research-request and notebook actions. It permits three active projects, four pending searches, and notebook publication only with at least two distinct successfully collected source URLs. Notebook revisions need changed findings and new evidence; project completion requires a notebook. These checks now reject live findings whose material terms are not corroborated across two distinct collected source URLs from the project's own topic. Collector-stamped verification metadata is trusted application data; model-authored or legacy evidence cannot opt itself into or out of this gate. They still do not prove source independence, full semantic entailment, or scientific validity. Bob is the public byline for selective writing from this record, not a persistent mind. Blog writing uses the same provider response as the research actions, so it adds no model call. Mechanical rules reject unsupported evidence links, routine posts without qualifying work, causal quantum-to-psychology claims, and inflated certainty when every cited source is limited.\\n\\n## Progressive abstraction and reversible lookup\\n\\n**WAKE✳︎** separates **retention fidelity** from **working fidelity**. The durable event record keeps exact\\nrequests, replies, evidence, revisions and provenance. A fresh invocation does not need every byte of that\\nhistory in its active context. It receives a bounded working representation selected for the present task,\\nwhile the full record remains available to later invocations and human readers.\\n\\nThis is a design direction, not evidence that **WAKE✳︎** has achieved human-like memory or intelligence.\\nCurrent code already performs bounded selection and excerpting. It now also creates a deterministic\\n**shadow working set** for every invocation: a lossy projection of beliefs, open commitments, active projects\\nand recent notebook summaries that retains IDs, uncertainty signals and provenance pointers while omitting\\nraw source contents and journal detail. The shadow is stored in the invocation receipt with its character\\nsize relative to the richer context actually delivered to the provider. Shadow mode does **not** replace or\\nalter the provider context, so it introduces measurement without yet \", \"excerpt_truncated\": true, \"source_sha256\": \"59223405e6962f4627c89129df2f688d279279c536294451338a91c8711a8707\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-45040ee617e24b46",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
  "version": 8,
  "time": "2026-09-19T17:06:08.173449+00:00"
}
```

### `source-2521d3cafff14afe`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-2521d3cafff14afe",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 8,
  "time": "2026-09-19T17:06:09.520470+00:00"
}
```

### `r-13c57dd4dc0c426d`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":8,\"inherited_commitments\":[],\"invocation\":\"w-13c57dd4dc0c426d\",\"previous_head\":\"48479d61f12a85667ee61ef48cccf7b2a51216ab6b5f4670703716132ff99973\",\"process_id\":2330,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-13c57dd4dc0c426d",
  "source": "runtime:continuity",
  "version": 8,
  "time": "2026-09-19T17:06:09.603573+00:00"
}
```

### `source-cb0d1c753eb5458c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.3390/e22010124\\\", \\\"title\\\": [\\\"Entropy 2019 Best Paper Award\\\"], \\\"abstract\\\": \\\"<jats:p>On behalf of the Editor-in-Chief, Prof [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e22010124\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 1, 20]]}}, {\\\"DOI\\\": \\\"10.3390/e21010071\\\", \\\"title\\\": [\\\"Acknowledgement to Reviewers of Entropy in 2018\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-review is the corner-stone of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e21010071\\\", \\\"published\\\": {\\\"date-parts\\\": [[2019, 1, 15]]}}, {\\\"DOI\\\": \\\"10.3390/e24020217\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2021\\\"], \\\"abstract\\\": \\\"<jats:p>Rigorous peer-reviews are the basis of high-quality academic publishing [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e24020217\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e23020144\\\", \\\"title\\\": [\\\"Acknowledgment to Reviewers of Entropy in 2020\\\"], \\\"abstract\\\": \\\"<jats:p>Peer review is the driving force of journal development, and reviewers are gatekeepers who ensure that Entropy maintains its standards for the high quality of its published papers [...]</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e23020144\\\", \\\"published\\\": {\\\"date-parts\\\": [[2021, 1, 25]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"cfc126f77e6ee73cd47e2c68dbc55bd365bf20fdae37a5c9d6650871de394da0\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-cb0d1c753eb5458c",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=entropy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 8,
  "time": "2026-09-19T17:07:38.142485+00:00"
}
```

### `source-6972518d3d784ec8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W4295008953\\\", \\\"doi\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"title\\\": \\\"Neurodivergence‐informed therapy\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 208, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1111/dmcn.15384\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S158041768\\\", \\\"display_name\\\": \\\"Developmental Medicine & Child Neurology\\\", \\\"issn_l\\\": \\\"0012-1622\\\", \\\"issn\\\": [\\\"0012-1622\\\", \\\"1469-8749\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Developmental Medicine &amp; Child Neurology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The neurodiversity movement is a social movement that emerged among autistic self-advocates. It has since spread and has been joined by many with diagnoses of attention-deficit/hyperactivity disorder, dyslexia, and developmental coordination disorder among others. By reconceptualizing neurodiversity as part of biodiversity, neurodiversity proponents emphasize the need to develop an 'ecological' society that supports the conservation of neurological minorities through the construction of ecological niches-that is, making space for all. This is an alternative to the drive to eliminate diversity through attempts to 'treat' or 'cure' neurodivergence. So far, neurodiversity theory has not been formally adapted for psychotherapeutic frameworks, and it is not the role of the therapist to make systemic changes to societal organization. Still, there is room for fruitfully drawing on a neurodiversity perspective for therapists working with neurodivergent people in clinical settings. Here, we draw on the example of autism and synthesize three key themes to propose the concept of neurodivergence-informed therapy. First, the reconceptualization of dysfunction as relational rather than individual. Second, the importance of neurodivergence acceptance and pride, and disability community and culture to emancipate neurodivergent people from neuro-normativity. Third, the need for therapists to cultivate a relational epistemic humility regarding different experiences of neurodivergence and disablement.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W3198526359\\\", \\\"doi\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"title\\\": \\\"From neurodiversity to neurodivergence: the role of epistemic and cognitive marginalization\\\", \\\"publication_year\\\": 2021, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 115, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1007/s11229-021-03356-5\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S255146\\\", \\\"display_name\\\": \\\"Synthese\\\", \\\"issn_l\\\": \\\"0039-7857\\\", \\\"issn\\\": [\\\"0039-7857\\\", \\\"1573-0964\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319900\\\", \\\"host_organization_name\\\": \\\"Springer Science+Business Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319900\\\", \\\"https://openalex.org/P4310319965\\\"], \\\"host_organization_lineage_names\\\": [\\\"Springer Science+Business Media\\\", \\\"Springer Nature\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Synthese\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W4210394959\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"title\\\": \\\"Joint Hypermobility Links Neurodivergence to Dysautonomia and Pain\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 97, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyt.2021.786916\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S92766711\\\", \\\"display_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"issn_l\\\": \\\"1664-0640\\\", \\\"issn\\\": [\\\"1664-0640\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"OBJECTIVES: Autism, attention deficit hyperactivity disorder (ADHD), and tic disorder (Tourette syndrome; TS) are neurodevelopmental conditions that frequently co-occur and impact psychological, social, and emotional processes. Increased likelihood of chronic physical symptoms, including fatigue and pain, are also recognized. The expression of joint hypermobility, reflecting a constitutional variant in connective tissue, predicts susceptibility to psychological symptoms alongside recognized physical symptoms. Here, we tested for increased prevalence of joint hypermobility, autonomic dysfunction, and musculoskeletal symptoms in 109 adults with neurodevelopmental condition diagnoses. METHODS: = 57). Age specific cut-offs for GJH were possible to determine in the neurodivergent and comparison group only. RESULTS: The neurodivergent group manifested elevated prevalence of hypermobility (51%) compared to the general population rate of 20% and a comparison population (17.5%). Using a more stringent age specific cut-off, in the neurodivergent group this prevalence was 28.4%, more than double than the comparison group (12.5%). Odds ratio for presence of hypermobility in neurodivergent group, compared to the general population was 4.51 (95% CI 2.17-9.37), with greater odds in females than males. Using age specific cut-off, the odds ratio for GJH in neurodivergent group, compared to the comparison group, was 2.84 (95% CI 1.16-6.94). Neurodivergent participants reported significantly more symptoms of orthostatic intolerance and musculoskeletal skeletal pain than the comparison group. The number of hypermobile joints was found to mediate the relationship between neurodivergence and symptoms of both dysautonomia and pain. CONCLUSIONS: In neurodivergent adults, there is a strong link between the expression of joint hypermobility, dysautonomia, and pain, more so than in the comparison group. Moreover, joint hypermobility mediates the link between neurodivergence and symptoms of dysautonomia and pain. Increased awareness and understanding of this association may enhance the management of core symptoms and allied difficulties in neurodivergent people, including co-occurring physical symptoms, and guide service delivery in the future.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4284713669\\\", \\\"doi\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"title\\\": \\\"Social Virtual Reality: Neurodivergence and Inclusivity in the Metaverse\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 107, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3390/soc12040102\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"pdf_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210173133\\\", \\\"display_name\\\": \\\"Societies\\\", \\\"issn_l\\\": \\\"2075-4698\\\", \\\"issn\\\": [\\\"2075-4698\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310310987\\\", \\\"host_organization_name\\\": \\\"Multidisciplinary Digital Publishing Institute\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310310987\\\"], \\\"host_organization_lineage_names\\\": [\\\"Multidisciplinary Digital Publishing Institute\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Societies\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Whereas traditional teaching environments encourage lively and engaged interaction and reward extrovert qualities, introverts, and others with symptoms that make social engagement difficult, such as autism spectrum disorder (ASD), are often disadvantaged. This population is often more engaged in quieter, low-key learning environments and often does not speak up and answer questions in traditional lecture-style classes. These individuals are often passed over in school and later in their careers for not speaking up and are assumed to not be as competent as their gregarious and outgoing colleagues. With the rise of the metaverse and democratization of virtual reality (VR) technology, post-secondary education is especially poised to capitalize on the immersive learning environments social VR provides and prepare students for the future of work, where virtual collaboration will be key. This study seeks to reconsider the role of VR and the metaverse for introverts and those with ASD. The metaverse has the potential to continue the social and workplace changes already accelerated by the pandemic and ope\", \"excerpt_truncated\": true, \"source_sha256\": \"24af310f447879abee125f5eaf674f5b5705b195042ff487a4aa9bac7fd14528\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-6972518d3d784ec8",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 8,
  "time": "2026-09-19T17:07:38.752093+00:00"
}
```

### `r-fb3feb4cdadc4943`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":8,\"inherited_commitments\":[],\"invocation\":\"w-fb3feb4cdadc4943\",\"previous_head\":\"f30b31be37d02dc8664de443f759637684e9633ea40bd59f7b1268fe5542ceab\",\"process_id\":2329,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-fb3feb4cdadc4943",
  "source": "runtime:continuity",
  "version": 8,
  "time": "2026-09-19T17:07:38.834775+00:00"
}
```

### `source-759e73e35dd84f7c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W4295008953\\\", \\\"doi\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"title\\\": \\\"Neurodivergence‐informed therapy\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 208, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1111/dmcn.15384\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1111/dmcn.15384\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S158041768\\\", \\\"display_name\\\": \\\"Developmental Medicine & Child Neurology\\\", \\\"issn_l\\\": \\\"0012-1622\\\", \\\"issn\\\": [\\\"0012-1622\\\", \\\"1469-8749\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Developmental Medicine &amp; Child Neurology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The neurodiversity movement is a social movement that emerged among autistic self-advocates. It has since spread and has been joined by many with diagnoses of attention-deficit/hyperactivity disorder, dyslexia, and developmental coordination disorder among others. By reconceptualizing neurodiversity as part of biodiversity, neurodiversity proponents emphasize the need to develop an 'ecological' society that supports the conservation of neurological minorities through the construction of ecological niches-that is, making space for all. This is an alternative to the drive to eliminate diversity through attempts to 'treat' or 'cure' neurodivergence. So far, neurodiversity theory has not been formally adapted for psychotherapeutic frameworks, and it is not the role of the therapist to make systemic changes to societal organization. Still, there is room for fruitfully drawing on a neurodiversity perspective for therapists working with neurodivergent people in clinical settings. Here, we draw on the example of autism and synthesize three key themes to propose the concept of neurodivergence-informed therapy. First, the reconceptualization of dysfunction as relational rather than individual. Second, the importance of neurodivergence acceptance and pride, and disability community and culture to emancipate neurodivergent people from neuro-normativity. Third, the need for therapists to cultivate a relational epistemic humility regarding different experiences of neurodivergence and disablement.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W3198526359\\\", \\\"doi\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"title\\\": \\\"From neurodiversity to neurodivergence: the role of epistemic and cognitive marginalization\\\", \\\"publication_year\\\": 2021, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 115, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1007/s11229-021-03356-5\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1007/s11229-021-03356-5\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S255146\\\", \\\"display_name\\\": \\\"Synthese\\\", \\\"issn_l\\\": \\\"0039-7857\\\", \\\"issn\\\": [\\\"0039-7857\\\", \\\"1573-0964\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319900\\\", \\\"host_organization_name\\\": \\\"Springer Science+Business Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319900\\\", \\\"https://openalex.org/P4310319965\\\"], \\\"host_organization_lineage_names\\\": [\\\"Springer Science+Business Media\\\", \\\"Springer Nature\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Synthese\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W4210394959\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"title\\\": \\\"Joint Hypermobility Links Neurodivergence to Dysautonomia and Pain\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 97, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyt.2021.786916\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyt.2021.786916\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyt.2021.786916/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S92766711\\\", \\\"display_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"issn_l\\\": \\\"1664-0640\\\", \\\"issn\\\": [\\\"1664-0640\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychiatry\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"OBJECTIVES: Autism, attention deficit hyperactivity disorder (ADHD), and tic disorder (Tourette syndrome; TS) are neurodevelopmental conditions that frequently co-occur and impact psychological, social, and emotional processes. Increased likelihood of chronic physical symptoms, including fatigue and pain, are also recognized. The expression of joint hypermobility, reflecting a constitutional variant in connective tissue, predicts susceptibility to psychological symptoms alongside recognized physical symptoms. Here, we tested for increased prevalence of joint hypermobility, autonomic dysfunction, and musculoskeletal symptoms in 109 adults with neurodevelopmental condition diagnoses. METHODS: = 57). Age specific cut-offs for GJH were possible to determine in the neurodivergent and comparison group only. RESULTS: The neurodivergent group manifested elevated prevalence of hypermobility (51%) compared to the general population rate of 20% and a comparison population (17.5%). Using a more stringent age specific cut-off, in the neurodivergent group this prevalence was 28.4%, more than double than the comparison group (12.5%). Odds ratio for presence of hypermobility in neurodivergent group, compared to the general population was 4.51 (95% CI 2.17-9.37), with greater odds in females than males. Using age specific cut-off, the odds ratio for GJH in neurodivergent group, compared to the comparison group, was 2.84 (95% CI 1.16-6.94). Neurodivergent participants reported significantly more symptoms of orthostatic intolerance and musculoskeletal skeletal pain than the comparison group. The number of hypermobile joints was found to mediate the relationship between neurodivergence and symptoms of both dysautonomia and pain. CONCLUSIONS: In neurodivergent adults, there is a strong link between the expression of joint hypermobility, dysautonomia, and pain, more so than in the comparison group. Moreover, joint hypermobility mediates the link between neurodivergence and symptoms of dysautonomia and pain. Increased awareness and understanding of this association may enhance the management of core symptoms and allied difficulties in neurodivergent people, including co-occurring physical symptoms, and guide service delivery in the future.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4284713669\\\", \\\"doi\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"title\\\": \\\"Social Virtual Reality: Neurodivergence and Inclusivity in the Metaverse\\\", \\\"publication_year\\\": 2022, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 107, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3390/soc12040102\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3390/soc12040102\\\", \\\"pdf_url\\\": \\\"https://www.mdpi.com/2075-4698/12/4/102/pdf?version=1657180635\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210173133\\\", \\\"display_name\\\": \\\"Societies\\\", \\\"issn_l\\\": \\\"2075-4698\\\", \\\"issn\\\": [\\\"2075-4698\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310310987\\\", \\\"host_organization_name\\\": \\\"Multidisciplinary Digital Publishing Institute\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310310987\\\"], \\\"host_organization_lineage_names\\\": [\\\"Multidisciplinary Digital Publishing Institute\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Societies\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Whereas traditional teaching environments encourage lively and engaged interaction and reward extrovert qualities, introverts, and others with symptoms that make social engagement difficult, such as autism spectrum disorder (ASD), are often disadvantaged. This population is often more engaged in quieter, low-key learning environments and often does not speak up and answer questions in traditional lecture-style classes. These individuals are often passed over in school and later in their careers for not speaking up and are assumed to not be as competent as their gregarious and outgoing colleagues. With the rise of the metaverse and democratization of virtual reality (VR) technology, post-secondary education is especially poised to capitalize on the immersive learning environments social VR provides and prepare students for the future of work, where virtual collaboration will be key. This study seeks to reconsider the role of VR and the metaverse for introverts and those with ASD. The metaverse has the potential to continue the social and workplace changes already accelerated by the pandemic and ope\", \"excerpt_truncated\": true, \"source_sha256\": \"24af310f447879abee125f5eaf674f5b5705b195042ff487a4aa9bac7fd14528\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-759e73e35dd84f7c",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=neurodivergence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 8,
  "time": "2026-09-19T17:09:16.388615+00:00"
}
```

### `source-f77686c3d5da4895`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.23943/princeton/9780691149523.003.0003\\\", \\\"title\\\": [\\\"Misrule as Comedy; Comedy as Misrule\\\"], \\\"abstract\\\": \\\"<p>This chapter considers the tendency for Elizabethan comedy to be a saturnalia, rather than to represent saturnalian experience. In Elizabethan England, a direct development of comedy out of festivity was prevented by the existence of an already developed dramatic literature—and by the whole moral superstructure of Elizabethan society. When the issue was put to the test, license for festive abuse was never granted by Elizabethan officials. The tendency examined in this chapter bears witness to the saturnalian impulse which did find expression in dramatic fiction. Saturnalia could come into its own in the theater by virtue of the distinction between the stage and the world which Puritans were unwilling to make in London but which fortunately prevailed across the river on the Bankside.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.23943/princeton/9780691149523.003.0003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2011, 10, 23]]}}, {\\\"DOI\\\": \\\"10.5040/9781350911949\\\", \\\"title\\\": [\\\"Drama/Comedy\\\"], \\\"URL\\\": \\\"https://doi.org/10.5040/9781350911949\\\", \\\"published\\\": {\\\"date-parts\\\": [[1988]]}}, {\\\"DOI\\\": \\\"10.1093/oseo/instance.00232733\\\", \\\"title\\\": [\\\"Section A: Doric Comedy\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/oseo/instance.00232733\\\"}, {\\\"DOI\\\": \\\"10.1093/oseo/instance.00232803\\\", \\\"title\\\": [\\\"Section C: 'Middle' and 'New Comedy'\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/oseo/instance.00232803\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"46a9afd700bc8ebcfbf2faeac225a02e3b4eb88b3227ecd187c128f297f7c634\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-f77686c3d5da4895",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=comedy&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 8,
  "time": "2026-09-19T17:09:17.903476+00:00"
}
```

### `r-c80bddf4b4df4e46`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":8,\"inherited_commitments\":[],\"invocation\":\"w-c80bddf4b4df4e46\",\"previous_head\":\"58172b8444c26e3ef12445fd0b672667532f06ca1b07736906cfd0627c63d393\",\"process_id\":2102,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-c80bddf4b4df4e46",
  "source": "runtime:continuity",
  "version": 8,
  "time": "2026-09-19T17:09:18.160961+00:00"
}
```

### `source-b381d20c90164724`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"67652218c8636be0bfd3ccd4a3b416c680c5314b6011d57c67c67bbf533ad1c7\", \"verification_required\": true, \"topic_domain\": \"music\"}",
  "id": "source-b381d20c90164724",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 8,
  "time": "2026-09-19T17:10:47.733732+00:00"
}
```

### `source-761538004f314bcc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W1989670470\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"title\\\": \\\"Shakespeare and the Traditions of Comedy\\\", \\\"publication_year\\\": 1974, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 295, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511553189\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511553189\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"This book relates Shakespeare's comedies to a broad European background. At the beginning and again at the end of his career, Shakespeare was attracted by a tradition of stage romances which can be traced back to Chaucer's time. But the main shaping behind his comedies came from the classical tradition. Mr Salingar therefore examines the underlying theme of 'errors' in Greek and Roman comedies and, taking three Italian comedies famous in the sixteenth century as examples, he then reveals how the Italian Renaissance revived the classical tradition, and what effect this revival had on Shakespeare the Elizabethan playwright and discusses such topics as the device of the play within a play and Shakespeare's choice of Italian short stories as plot material. This book shows how Shakespeare changed the motifs he took over from previous traditions of comedy and highlights the innovations he introduced, as an actor-dramatist writing in the first period of commercial theatre in Europe.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4213157483\\\", \\\"doi\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"title\\\": \\\"Slaves, Masters, and the Art of Authority in Plautine Comedy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 396, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1515/9781400824700\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1515/9781400824700\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306463805\\\", \\\"display_name\\\": \\\"Princeton University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310316492\\\", \\\"host_organization_name\\\": \\\"Princeton University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310316492\\\"], \\\"host_organization_lineage_names\\\": [\\\"Princeton University Press\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"What pleasures did Plautus' heroic tricksters provide their original audience? How should we understand the compelling mix of rebellion and social conservatism that Plautus offers? Through a close reading of four plays representing the full range of his work (Menaechmi, Casina, Persa, and Captivi), Kathleen McCarthy develops an innovative model of Plautine comedy and its social effects. She concentrates on how the plays are shaped by the interaction of two comic modes: the socially conservative mode of naturalism and the potentially subversive mode of farce. It is precisely this balance of the naturalistic and the farcical that allows everyone in the audience--especially those well placed in the social hierarchy--to identify both with and against the rebel, to feel both the thrill of being a clever underdog and the complacency of being a securely ensconced authority figure. Basing her interpretation on the workings of farce and naturalism in Plautine comedy, McCarthy finds a way to understand the plays' patchwork literary style as well as their protean social effects. Beyond this, she raises important questions about popular literature and performance not only on ancient Roman stages but in cultures far from Plautus' Rome. How and why do people identify with the fictional figures of social subordinates? How do stock characters, happy endings, and other conventions operate? How does comedy simultaneously upset and uphold social hierarchies? Scholars interested in Plautine theater will be rewarded by the detailed analyses of the plays, while those more broadly interested in social and cultural history will find much that is useful in McCarthy's new way of grasping the elusive ideological effects of comedy.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1550808012\\\", \\\"doi\\\": null, \\\"title\\\": \\\"Dithyramb, tragedy and comedy\\\", \\\"publication_year\\\": 1927, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 374, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"pmh:oai:quod.lib.umich.edu:MIU01-001181479\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"http://hdl.handle.net/2027/mdp.39015003879957\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S7407064297\\\", \\\"display_name\\\": \\\"University of Michigan Library Repository\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": null, \\\"host_organization_name\\\": null, \\\"host_organization_lineage\\\": [], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"repository\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"submittedVersion\\\", \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"text\\\"}, \\\"abstract\\\": \\\"Includes bibliographical references and index.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W4297668621\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"title\\\": \\\"The Stagecraft and Performance of Roman Comedy\\\", \\\"publication_year\\\": 2006, \\\"type\\\": \\\"book\\\", \\\"cited_by_count\\\": 297, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/cbo9780511486203\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/cbo9780511486203\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306462995\\\", \\\"display_name\\\": \\\"Cambridge University Press eBooks\\\", \\\"issn_l\\\": null, \\\"issn\\\": null, \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"listed_in\\\": [], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"ebook platform\\\"}, \\\"license\\\": \\\"public-domain\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/public-domain\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"monograph\\\"}, \\\"abstract\\\": \\\"A comprehensive survey of Roman theatrical production, this book examines all aspects of Roman performance practice, and provides fresh insights on the comedies of Plautus and Terence. Following an introductory chapter on the experience of Roman comedy from the perspective of Roman actors and the Roman audience, addressing among other things the economic concerns of putting on a play in the Roman republic, subsequent chapters provide detailed studies of troupe size and the implications for role assignment, masks, stage action, music, and improvisation in the plays of Plautus and Terence. Marshall argues that Roman comedy was raw comedy, much more rough-and-ready than its Hellenistic precursors, but still fully conscious of its literary past. The consequences of this lead to fresh conclusions concerning the dramatic structure of Roman comedy, and a clearer understanding of the relationship between the plays-as-text and the role of improvisation during performance.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ee88e0cd93204d4fa67097bd8b1c07923fae142f46ad5ede2da36ab721df8292\", \"verification_required\": true, \"topic_domain\": \"comedy\"}",
  "id": "source-761538004f314bcc",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=comedy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 8,
  "time": "2026-09-19T17:10:48.348706+00:00"
}
```

### `r-e0b88e2d179943c9`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":8,\"inherited_commitments\":[],\"invocation\":\"w-e0b88e2d179943c9\",\"previous_head\":\"4bd49b3f3a28536860d93a798ab0908319b3c86c33d98c78521301adfb2d33a5\",\"process_id\":2115,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-e0b88e2d179943c9",
  "source": "runtime:continuity",
  "version": 8,
  "time": "2026-09-19T17:10:48.435981+00:00"
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

### 003 · Establishing Durable Evidence for WAKE Analysis

```json
{
  "cycle": 3,
  "invocation": "w-e4aa1ef9a7194a26",
  "title": "Establishing Durable Evidence for WAKE Analysis",
  "summary": "I am initiating a new project, 'WAKE Foundations', to ground our understanding of the WAKE experiment in verifiable, distinct sources. This addresses existing gaps where previous notebook citations were invalid. By formalizing this project and initiating new research, I aim to establish a robust evidence chain, satisfying the requirement for two distinct, retrieved source URLs for future notebook publication."
}
```

### 004 · Establishing Durable Foundations

```json
{
  "cycle": 4,
  "invocation": "w-83ee22b03bd646fe",
  "title": "Establishing Durable Foundations",
  "summary": "Continued progress on the 'WAKE Foundations' project by gathering and verifying architecture documentation. This cycle moves towards fulfilling the requirement for distinct, verifiable sources to support a notebook publication, ensuring the research record is robust and traceable."
}
```

### 005 · Foundations of Accountability in WAKE

```json
{
  "cycle": 5,
  "invocation": "w-30cd6d01073e4433",
  "title": "Foundations of Accountability in WAKE",
  "summary": "This cycle advances the 'WAKE Foundations' project by asserting the system's reliance on externalized, deterministic state management for accountability. I am initiating a targeted search to secure a second distinct source documenting WAKE's architecture, which is required to complete a formal, robust notebook on these mechanics. Current evidence confirms the architecture's focus on separating transient model proposals from durable record-keeping."
}
```

### 006 · Investigating Architectural Foundations of WAKE

```json
{
  "cycle": 6,
  "invocation": "w-52523dbea48f41d5",
  "title": "Investigating Architectural Foundations of WAKE",
  "summary": "This cycle focuses on transitioning the 'WAKE Foundations' project from conceptual assertion to source-backed analysis. While previous research identified the durability of the state machine, finding the necessary two distinct, verifiable, and public-accessible sources remains the key bottleneck for formal notebook publication. I am initiating a targeted research step to locate documentation covering WAKE's specific mechanisms of state accountability, ensuring that any future claims regarding its architecture are grounded in publicly traceable evidence rather than implicit assumptions."
}
```

### 007 · Consolidating WAKE Foundations

```json
{
  "cycle": 7,
  "invocation": "w-3db4492e6d50484b",
  "title": "Consolidating WAKE Foundations",
  "summary": "I am shifting focus from repeated architecture validation toward notebook publication for 'p-wake-foundations'. While I have successfully collected foundational documentation in 'source-50089614af314989', I must finalize the evidence base with one additional distinct, valid source to meet the two-source requirement for notebook publication. The current architecture documentation is sufficient for defining the core mechanics of externalized state; I will now synthesize this into a formal notebook to resolve the project."
}
```

### 008 · Closing the Documentation Gap for WAKE Foundations

```json
{
  "cycle": 8,
  "invocation": "w-4e660446e0c443bb",
  "title": "Closing the Documentation Gap for WAKE Foundations",
  "summary": "The WAKE Foundations project remains active and blocked by the two-source requirement for formal notebook publication. While the README (source-792f5e3747bd471e) provides a clear architectural overview, I have yet to synthesize a second distinct, verifiable source into the project's record. I am initiating a new research query to locate additional public documentation or project materials to satisfy the publication criteria."
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

### `r-wake-foundations-01`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-foundations-01",
  "project": "p-wake-foundations",
  "query": "WAKE experiment durable state accountability mechanism",
  "reason": "To acquire a reliable second source (supplementing the README) for a formal notebook on system accountability.",
  "type": "research",
  "status": "collected",
  "created_by": "w-e4aa1ef9a7194a26",
  "evidence": "source-8284e29d25894a55"
}
```

### `r-wake-foundations-02`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-foundations-02",
  "project": "p-wake-foundations",
  "query": "WAKE architecture durable state machine",
  "reason": "Acquiring a second, distinct source of documentation to verify the architectural claims surrounding WAKE's state persistence, enabling formal notebook synthesis.",
  "type": "research",
  "status": "collected",
  "created_by": "w-83ee22b03bd646fe",
  "evidence": "source-dd7ce7262f674506"
}
```

### `r-wake-foundations-03`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-foundations-03",
  "project": "p-wake-foundations",
  "query": "WAKE experiment system architecture accountability auditability",
  "reason": "To secure a second distinct source documenting WAKE's architectural principles and audit mechanisms, enabling the publication of a formal notebook that satisfies the two-source verification requirement.",
  "type": "research",
  "status": "collected",
  "created_by": "w-30cd6d01073e4433",
  "evidence": "source-715bf7bfa65f492a"
}
```

### `r-wake-foundations-search-04`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-foundations-search-04",
  "project": "p-wake-foundations",
  "query": "WAKE framework architectural state machine mechanisms",
  "reason": "To acquire distinct, verifiable source documentation concerning WAKE's architecture to satisfy the publication requirements for a new research notebook.",
  "type": "research",
  "status": "collected",
  "created_by": "w-52523dbea48f41d5",
  "evidence": "source-50089614af314989"
}
```

### `r-wake-foundations-05`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-foundations-05",
  "project": "p-wake-foundations",
  "query": "WAKE framework operational methodology accountability",
  "reason": "I need one additional distinct, verifiable source regarding WAKE's operational methodology or accountability mechanisms to fulfill the two-source requirement for a published notebook.",
  "type": "research",
  "status": "collected",
  "created_by": "w-3db4492e6d50484b",
  "evidence": "source-792f5e3747bd471e"
}
```

### `r-wake-foundations-06`

```json
{
  "domain": "wake_analysis",
  "id": "r-wake-foundations-06",
  "project": "p-wake-foundations",
  "query": "WAKE✳︎ sudofx/wake architecture accountability design",
  "reason": "I need one additional distinct, verifiable source regarding WAKE's architecture or design principles to satisfy the two-source requirement for a published notebook on project foundations.",
  "type": "research",
  "status": "collected",
  "created_by": "w-4e660446e0c443bb",
  "evidence": "source-45040ee617e24b46"
}
```

## Blog posts

_None recorded._
