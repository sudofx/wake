# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 2  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `14a034ede46613281d226faa8ee96bdcb787be23e54de808cbb5912242a145c0`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

### `ci-structure-three-factor`

```json
{
  "confidence": 0.8,
  "evidence": [
    "source-1ba654396b7a4c16"
  ],
  "id": "ci-structure-three-factor",
  "reason": "The meta-analysis meta-analyzed 22 studies and found strong empirical support for this three-factor model over other alternatives, particularly in established groups.",
  "statement": "Collective intelligence (CI) can be structurally modeled as a hierarchical system comprised of collective memory, collective attention, and collective reasoning.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-a8003593ddd64a29",
  "updated_version": 2
}
```

## Commitments

_None recorded._

## Projects

### `ci-ai-foundations` · AI and Collective Intelligence

```json
{
  "domain": "collective_intelligence",
  "id": "ci-ai-foundations",
  "next_step": "Conduct literature search on AI-assisted collective cognition",
  "question": "How does AI intervene in collective memory, attention, and reasoning?",
  "reason": "To move beyond bibliographic citations and investigate specific structural mechanisms of AI intervention in group cognition.",
  "status": "active",
  "title": "AI and Collective Intelligence",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-3fd5a721413845e4"
}
```

## Notebooks

_None recorded._

## Invocations

### `w-3fd5a721413845e4`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-3fd5a721413845e4",
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
  "process_id": 2383,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "eb79da06f63a19766baafce465bb072f5b6f7021fad1fff8eb907562b7619465",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-49f19aec89e64836"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-49f19aec89e64836",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3e60dc5bebe44c74"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3e60dc5bebe44c74",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-49f19aec89e64836",
      "source-3e60dc5bebe44c74"
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
  "time": "2026-09-18T16:41:24.180985+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 14644,
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
      "category": "server",
      "elapsed_ms": 1606,
      "http_status": 503,
      "model": "gemini-3.5-flash",
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
      "elapsed_ms": 10298,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 24957,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-18T16:41:59.311753+00:00",
  "reason": ""
}
```

### `w-c6f273ca72ff4837`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-c6f273ca72ff4837",
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
        "id": "ci-ai-foundations",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "AI and Collective Intelligence"
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
  "process_id": 2044,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "d8d7f524523e32137f4383c02d08a02b48464cfbcbaa36c5352f4fb62dc74306",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-49f19aec89e64836"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-49f19aec89e64836",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3e60dc5bebe44c74"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3e60dc5bebe44c74",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-1ba654396b7a4c16"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1ba654396b7a4c16",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c23d5ed899ba4958"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c23d5ed899ba4958",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-49f19aec89e64836",
      "source-3e60dc5bebe44c74",
      "source-1ba654396b7a4c16",
      "source-c23d5ed899ba4958"
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
    "delivered_context_chars": 14757,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 4,
    "retrieval_evidence_count": 4,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 4
    },
    "working_set_chars": 648,
    "working_to_delivered_ratio": 0.0439
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "ci-ai-foundations",
        "next_step": "Conduct literature search on AI-assisted collective cognition",
        "question": "How does AI intervene in collective memory, attention, and reasoning?",
        "title": "AI and Collective Intelligence"
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
  "status": "deferred",
  "time": "2026-09-18T16:42:41.036156+00:00",
  "provider_attempts": [
    {
      "category": "timeout",
      "elapsed_ms": 60106,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.8-flash",
      "request_payload_bytes": 33687,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 2050,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 33687,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 10245,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 33687,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-18T16:44:03.419404+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 10245,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "timeout",
        "elapsed_ms": 60106,
        "error_type": "TimeoutError",
        "http_status": null,
        "model": "gemini-3.8-flash",
        "request_payload_bytes": 33687,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 2050,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 33687,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 10245,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 33687,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 3,
    "request_payload_bytes": 33687,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-a8003593ddd64a29`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-a8003593ddd64a29",
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
        "id": "ci-ai-foundations",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "AI and Collective Intelligence"
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
  "process_id": 2077,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "da06dcda54dba7780c57347b0cbbd5e3964a3140dc0e38f1f2a5f90dabfdbb99",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-49f19aec89e64836"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-49f19aec89e64836",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3e60dc5bebe44c74"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3e60dc5bebe44c74",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-1ba654396b7a4c16"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1ba654396b7a4c16",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c23d5ed899ba4958"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c23d5ed899ba4958",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-95bd13c86b1044c2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-95bd13c86b1044c2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4e03a34d1ef84a0c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4e03a34d1ef84a0c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-49f19aec89e64836",
      "source-3e60dc5bebe44c74",
      "source-1ba654396b7a4c16",
      "source-c23d5ed899ba4958",
      "source-95bd13c86b1044c2",
      "source-4e03a34d1ef84a0c"
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
    "delivered_context_chars": 18656,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "working_set_chars": 648,
    "working_to_delivered_ratio": 0.0347
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "ci-ai-foundations",
        "next_step": "Conduct literature search on AI-assisted collective cognition",
        "question": "How does AI intervene in collective memory, attention, and reasoning?",
        "title": "AI and Collective Intelligence"
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
  "time": "2026-09-18T16:44:46.279203+00:00",
  "provider_attempts": [
    {
      "category": "timeout",
      "elapsed_ms": 60108,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.8-flash",
      "request_payload_bytes": 38016,
      "result": "transient_failure"
    },
    {
      "category": "http",
      "elapsed_ms": 189,
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
            "retryDelay": "8s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 8.150466762s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 38016,
      "response_bytes_captured": 1361,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 10730,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 38016,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-18T16:46:06.411311+00:00",
  "reason": ""
}
```

## Evidence

### `source-49f19aec89e64836`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.47215\\\", \\\"title\\\": [\\\"Dance music (popular music genre)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.47215\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.a2258723\\\", \\\"title\\\": [\\\"Women’s music [womyn’s music]\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.a2258723\\\", \\\"published\\\": {\\\"date-parts\\\": [[2014, 1, 31]]}}, {\\\"DOI\\\": \\\"10.7763/ijcee.2010.v2.168\\\", \\\"title\\\": [\\\"Angular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithmsAngular Accuracy of ML, MUSIC, ROOT-MUSIC and spatially smoothed version of MUSIC algorithms\\\"], \\\"URL\\\": \\\"https://doi.org/10.7763/ijcee.2010.v2.168\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010]]}}, {\\\"DOI\\\": \\\"10.1093/gmo/9781561592630.article.42753\\\", \\\"title\\\": [\\\"Warner Bros. Music (music publisher)\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/gmo/9781561592630.article.42753\\\", \\\"published\\\": {\\\"date-parts\\\": [[2001]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"6b1069af06922b760ae859cbcbe63c740e2e0a8e3518d0b61223bde4eb339a35\"}",
  "id": "source-49f19aec89e64836",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=music&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-18T16:41:23.418228+00:00"
}
```

### `source-3e60dc5bebe44c74`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1177/26339137221114176\\\", \\\"title\\\": [\\\"New books on collective intelligence: Growing the field: Interesting new books on collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137221114176\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 8]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251360003\\\", \\\"title\\\": [\\\"Opinion for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>This short piece shares thoughts on some recent research and books related to collective intelligence - on topics ranging from democracy and institutions to LLMs and animals.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251360003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 7]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251328909\\\", \\\"title\\\": [\\\"AI for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>AI has emerged as a transformative force in society, reshaping economies, work, and everyday life. We argue that AI can not only improve short-term productivity but can also enhance a group’s collective intelligence. Specifically, AI can be employed to enhance three elements of collective intelligence: collective memory, collective attention, and collective reasoning. This editorial reviews key emerging work in the area to suggest ways in which AI can support the socio-cognitive architecture of collective intelligence. We will then briefly introduce the articles in the “AI for Collective Intelligence” special issue.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251328909\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4]]}}, {\\\"DOI\\\": \\\"10.1177/26339137241285900\\\", \\\"title\\\": [\\\"Book Review: A few recent books on Collective Intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137241285900\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 3, 3]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"a1264fd23b16fc37b0cd17c724c2040c742cde41b827560996478785e63e3b7a\"}",
  "id": "source-3e60dc5bebe44c74",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 0,
  "time": "2026-09-18T16:41:24.175353+00:00"
}
```

### `r-3fd5a721413845e4`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-3fd5a721413845e4\",\"previous_head\":\"e92923e1c7507638d215ef57b74908a20364e478f20e1a410fe4d19b7da6b0e8\",\"process_id\":2383,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-3fd5a721413845e4",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-18T16:41:24.178778+00:00"
}
```

### `source-1ba654396b7a4c16`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=AI+collective+intelligence+collective+memory+attention+reasoning&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.31234/osf.io/4sqfx_v1\\\", \\\"title\\\": [\\\"The Structure of Collective Intelligence: Evidence for Collective Memory, Attention, and Reasoning\\\"], \\\"abstract\\\": \\\"<p>The ability for groups to effectively collaborate is important for both economic and societal progress. Extant research has demonstrated that group performance can be explained by a general \\\\\\\"collective intelligence\\\\\\\" (CI) factor, but there is ongoing debate about the components of CI with important implications for our understanding of how it develops or can be enhanced. We conduct a meta-analysis with data from 22 studies and 5,279 individuals in 1,356 groups to investigate the structure of collective intelligence using factor analysis. Our analysis yields strong support for a hierarchical three-factor model, supporting a theory that collective intelligence emerges from collective memory, attention, and reasoning. The model explains the data better than other plausible alternatives, especially in established groups who had the opportunity to develop their collective cognition over time. Our findings provide new insights into the formation of collective intelligence and have important implications for the design and evaluation of interventions that aim to increase it.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.31234/osf.io/4sqfx_v1\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 11, 27]]}}, {\\\"DOI\\\": \\\"10.1177/17456916231191534\\\", \\\"title\\\": [\\\"Understanding Collective Intelligence: Investigating the Role of Collective Memory, Attention, and Reasoning Processes\\\"], \\\"abstract\\\": \\\"<jats:p>As society has come to rely on groups and technology to address many of its most challenging problems, there is a growing need to understand how technology-enabled, distributed, and dynamic collectives can be designed to solve a wide range of problems over time in the face of complex and changing environmental conditions—an ability we define as “collective intelligence.” We describe recent research on the Transaction Systems Model of Collective Intelligence (TSM-CI) that integrates literature from diverse areas of psychology to conceptualize the underpinnings of collective intelligence. The TSM-CI articulates the development and mutual adaptation of transactive memory, transactive attention, and transactive reasoning systems that together support the emergence and maintenance of collective intelligence. We also review related research on computational indicators of transactive-system functioning based on collaborative process behaviors that enable agent-based teammates to diagnose and potentially intervene to address developing issues. We conclude by discussing future directions in developing the TSM-CI to support research on developing collective human-machine intelligence and to identify ways to design technology to enhance it.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/17456916231191534\\\", \\\"published\\\": {\\\"date-parts\\\": [[2023, 8, 29]]}}, {\\\"DOI\\\": \\\"10.1177/26339137261429497\\\", \\\"title\\\": [\\\"Incorporating memory into bounded confidence models of probabilistic social learning\\\"], \\\"abstract\\\": \\\"<jats:p>In social learning models, truth-seeking agents learn both individually from direct evidence and socially by pooling beliefs with others. That learning can be undermined by two types of unreliable agents: zealots, who do not learn and promote the same fixed opinion and free riders, who lack access to evidence yet still influence others. In this paper, we explore how learning rules that incorporate memory can mitigate the effects of unreliable agents. To do so, we construct an agent-based model of social learning in which agents apply a probabilistic bounded confidence (BC) model that evaluates the similarity between themselves and others based on samples of recent beliefs rather than current beliefs only. When compared to a memoryless BC benchmark, BC with memory proves significantly less sensitive to the choice of similarity threshold governing agent interactions, to the extent that a fixed threshold is effective for avoiding all types of zealots. It is also less susceptible to high levels of distrust in evidence. The BC with memory model is then extended to social learning about multiple hypotheses, and we show that the robustness results generalise to the case in which beliefs are multi-dimensional probability distributions.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137261429497\\\", \\\"published\\\": {\\\"date-parts\\\": [[2026, 4]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251328909\\\", \\\"title\\\": [\\\"AI for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>AI has emerged as a transformative force in society, reshaping economies, work, and everyday life. We argue that AI can not only improve short-term productivity but can also enhance a group’s collective intelligence. Specifically, AI can be employed to enhance three elements of collective intelligence: collective memory, collective attention, and collective reasoning. This editorial reviews key emerging work in the area to suggest ways in which AI can support the socio-cognitive architecture of collective intelligence. We will then briefly introduce the articles in the “AI for Collective Intelligence” special issue.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251328909\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"4eed098edcf0496e06ae1f2aa9fd32a1d1aac55fdfc6d1345bb533d5c241811d\"}",
  "id": "source-1ba654396b7a4c16",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=AI+collective+intelligence+collective+memory+attention+reasoning&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T16:42:40.503802+00:00"
}
```

### `source-c23d5ed899ba4958`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1177/26339137221114176\\\", \\\"title\\\": [\\\"New books on collective intelligence: Growing the field: Interesting new books on collective intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137221114176\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 8]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251360003\\\", \\\"title\\\": [\\\"Opinion for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>This short piece shares thoughts on some recent research and books related to collective intelligence - on topics ranging from democracy and institutions to LLMs and animals.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251360003\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 7]]}}, {\\\"DOI\\\": \\\"10.1177/26339137251328909\\\", \\\"title\\\": [\\\"AI for collective intelligence\\\"], \\\"abstract\\\": \\\"<jats:p>AI has emerged as a transformative force in society, reshaping economies, work, and everyday life. We argue that AI can not only improve short-term productivity but can also enhance a group’s collective intelligence. Specifically, AI can be employed to enhance three elements of collective intelligence: collective memory, collective attention, and collective reasoning. This editorial reviews key emerging work in the area to suggest ways in which AI can support the socio-cognitive architecture of collective intelligence. We will then briefly introduce the articles in the “AI for Collective Intelligence” special issue.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1177/26339137251328909\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4]]}}, {\\\"DOI\\\": \\\"10.1177/26339137241285900\\\", \\\"title\\\": [\\\"Book Review: A few recent books on Collective Intelligence\\\"], \\\"URL\\\": \\\"https://doi.org/10.1177/26339137241285900\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 3, 3]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"a1264fd23b16fc37b0cd17c724c2040c742cde41b827560996478785e63e3b7a\"}",
  "id": "source-c23d5ed899ba4958",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T16:42:41.022662+00:00"
}
```

### `r-c6f273ca72ff4837`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-c6f273ca72ff4837\",\"previous_head\":\"f04d47d99fc72e59016d9329bbe1fd299b043dc50e29bf3362ea2ab6829b8c80\",\"process_id\":2044,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-c6f273ca72ff4837",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-18T16:42:41.031931+00:00"
}
```

### `source-95bd13c86b1044c2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=climate+change&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/wentk/9780197647127.003.0007\\\", \\\"title\\\": [\\\"Climate Change and You\\\"], \\\"abstract\\\": \\\"<p>\\\\n                  <italic>This chapter will explore some of the more personal questions that climate change raises for individuals and their families.</italic>\\\\n               </p>\\\\n               <p>How will climate change impact you and your family in the coming decades?</p>\\\\n               <p>The transition to a low-carbon economy is inevitable this century, and indeed it...</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/wentk/9780197647127.003.0007\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 9]]}}, {\\\"DOI\\\": \\\"10.1093/hesc/9780198807506.003.0005\\\", \\\"title\\\": [\\\"Climate Change and Agriculture\\\"], \\\"abstract\\\": \\\"<p>This chapter discusses how climate change affects agriculture, which plays a major role in providing food for a growing global population. Climate has an impact on agriculture through the effects of such variables as solar radiation, temperature, and rainfall. Moreover, extreme events such as heatwaves, frosts, wind storms, floods, and droughts can have catastrophic effects on agriculture. The chapter also looks into the process of achieving optimal climatic conditions for crops and livestock. It provides an overview of the impacts of climate change in line with the development of climate change adaptation strategies dedicated to agriculture, particularly the wine sector.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/hesc/9780198807506.003.0005\\\", \\\"published\\\": {\\\"date-parts\\\": [[2023, 11, 21]]}}, {\\\"DOI\\\": \\\"10.1332/policypress/9781529203950.003.0005\\\", \\\"title\\\": [\\\"Climate change victims\\\"], \\\"abstract\\\": \\\"<p>This chapter discusses the notion of victimhood as this pertains to climate change. Each section deals with a specific victim category — non-human environmental entities, children and young people, and Indigenous communities. Each grouping has its own specific histories, stories, and issues. What perhaps unites the discussion is an underlying emphasis on adopting an ecocentric perspective that incorporates social and ecological justice. From a human perspective, ecocentrism attempts to strike a balance between the need to utilise resources for human survival and the need to develop rules that facilitate the benign use of the ecosphere. Thus, for example, ensuring the preservation of biocentric values becomes integral to maintaining long-term human needs. To do this means minimising the victimisation of both the human and the non-human — in essence, to assert a form of <italic>ecological citizenship</italic>.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1332/policypress/9781529203950.003.0005\\\", \\\"published\\\": {\\\"date-parts\\\": [[2018, 10, 3]]}}, {\\\"DOI\\\": \\\"10.1093/wentk/9780197647127.003.0002\\\", \\\"title\\\": [\\\"Extreme Weather and Climate Change\\\"], \\\"abstract\\\": \\\"<p>\\\\n                    <italic>Extreme weather is the earliest manifestation of climate change that most people will be exposed to. This chapter will focus on what science tells us about the remarkable spate of once-in-a-century (and rarer) extreme weather events we have observed in the last few years. It...</italic>\\\\n                  </p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/wentk/9780197647127.003.0002\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 9]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"dc6520ab404af002fe01079ee4370b1fe7d5b75e2cfd089cb8a2ed04a5118008\"}",
  "id": "source-95bd13c86b1044c2",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=climate+change&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T16:44:46.147164+00:00"
}
```

### `source-4e03a34d1ef84a0c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=symmetry&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"error\": \"HTTPError\", \"scope\": \"fetch failed; no evidence obtained\"}",
  "id": "source-4e03a34d1ef84a0c",
  "scope": "failed",
  "source": "https://api.crossref.org/works?query=symmetry&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T16:44:46.263188+00:00"
}
```

### `r-a8003593ddd64a29`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-a8003593ddd64a29\",\"previous_head\":\"2b6e450ea422cf434b9cd36327fe51504ace364efe8eaf965e52c4c7f65631c3\",\"process_id\":2077,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-a8003593ddd64a29",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-18T16:44:46.274517+00:00"
}
```

## Journal

### 001 · Initiating inquiry into collective intelligence

```json
{
  "cycle": 1,
  "invocation": "w-3fd5a721413845e4",
  "title": "Initiating inquiry into collective intelligence",
  "summary": "This journal entry marks the start of the WAKE✳︎ research process. We are prioritizing the investigation of collective intelligence, specifically the interaction between AI and group cognitive architectures. The initial bibliographic scan highlights recent work on AI's potential to scaffold collective memory, attention, and reasoning. The immediate goal is to transition from bibliographic metadata to substantive analysis of these mechanisms."
}
```

### 002 · Inquiry into the structural foundations of collective intelligence

```json
{
  "cycle": 2,
  "invocation": "w-a8003593ddd64a29",
  "title": "Inquiry into the structural foundations of collective intelligence",
  "summary": "I am initiating a belief regarding the hierarchical structure of collective intelligence based on the initial meta-analysis collected. I am also queuing a targeted search to secure a distinct second source, which will enable the eventual publication of a substantive notebook on this topic."
}
```

## Research

### `search-ci-mechanisms`

```json
{
  "domain": "collective_intelligence",
  "id": "search-ci-mechanisms",
  "project": "ci-ai-foundations",
  "query": "AI collective intelligence collective memory attention reasoning",
  "reason": "To identify foundational papers and analysis regarding how AI technologies specifically support or augment collective cognitive processes.",
  "type": "research",
  "status": "collected",
  "created_by": "w-3fd5a721413845e4",
  "evidence": "source-1ba654396b7a4c16"
}
```

### `search-ci-paper-2`

```json
{
  "domain": "collective_intelligence",
  "id": "search-ci-paper-2",
  "project": "ci-ai-foundations",
  "query": "10.1177/17456916231191534",
  "reason": "To independently fetch bibliographic metadata for the Transactive Systems Model paper cited in the recent meta-analysis, satisfying the two-source requirement for notebook publication.",
  "type": "research",
  "status": "queued",
  "created_by": "w-a8003593ddd64a29"
}
```

## Blog posts

_None recorded._
