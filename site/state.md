# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 5  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `ecb979632bd58a25ecc2af4a33c2633528ea77988ace8ca67843b5f541e78a03`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

_None recorded._

## Projects

### `p-conscious-theories-01` · Empirical Foundations of Consciousness Theories

```json
{
  "domain": "consciousness",
  "id": "p-conscious-theories-01",
  "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
  "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
  "reason": "To ground the investigation in actual scientific literature rather than speculation.",
  "status": "active",
  "title": "Empirical Foundations of Consciousness Theories",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-ec2134b1da6540bd"
}
```

### `p-working-memory-01` · Foundations of Working Memory Models

```json
{
  "domain": "psychology",
  "id": "p-working-memory-01",
  "next_step": "Identify foundational literature differentiating working memory from short-term memory.",
  "question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
  "reason": "Working memory is a well-defined construct with a substantial body of experimental literature, providing a stable foundation to contrast with the more speculative territory of consciousness research.",
  "status": "active",
  "title": "Foundations of Working Memory Models",
  "type": "project",
  "created_version": 3,
  "updated_version": 3,
  "updated_by": "w-dd3f704c9d5044e0"
}
```

### `p-neuro-endocrine-01` · Hormonal Modulation of Neurological Function

```json
{
  "domain": "endocrinology",
  "id": "p-neuro-endocrine-01",
  "next_step": "Conduct a focused literature search on the role of glucocorticoids and sex hormones in modulating hippocampal synaptic plasticity.",
  "question": "How do endocrine-derived hormones exert regulatory control over neurotransmitter synthesis and synaptic plasticity in the adult brain?",
  "reason": "This project investigates the mechanistic links between systemic endocrine signals and localized neurological function, which is a tractable intersection that avoids the broad, speculative nature of earlier consciousness queries.",
  "status": "active",
  "title": "Hormonal Modulation of Neurological Function",
  "type": "project",
  "created_version": 5,
  "updated_version": 5,
  "updated_by": "w-d2314c66d29247bf"
}
```

## Acquisition capability

### `p-conscious-theories-01`

```json
{
  "project": "p-conscious-theories-01",
  "domain": "consciousness",
  "no_progress": 3,
  "routes": [
    "api.openalex.org:discovery"
  ],
  "capability_blocked": false,
  "retry_after_version": null,
  "persistent_identifiers": [
    "openalex:W2120745192",
    "arxiv:2013.00200",
    "doi:10.3389/fpsyg.2012.00001",
    "doi:10.3389/fpsyg.2012.00001/pdf",
    "doi:10.1016/j.neubiorev.2011.12.003",
    "doi:10.1523/jneurosci.3218-16.2017",
    "doi:10.1017/s0140525x15000965",
    "openalex:W2133171318",
    "openalex:W2016085611",
    "openalex:W2952447148",
    "openalex:W2129245434",
    "arxiv:2012.00001"
  ],
  "last_receipt": {
    "evidence": "source-1611d8f3d2ef4cc8",
    "outcome": "no_progress",
    "persistent_identifiers": [
      "doi:10.3389/fpsyg.2012.00001",
      "doi:10.3389/fpsyg.2012.00001/pdf",
      "doi:10.1016/j.neubiorev.2011.12.003",
      "doi:10.1523/jneurosci.3218-16.2017",
      "doi:10.1017/s0140525x15000965",
      "openalex:W2133171318",
      "openalex:W2016085611",
      "openalex:W2952447148",
      "openalex:W2129245434",
      "arxiv:2012.00001"
    ],
    "research_id": "r-conscious-theories-03",
    "route": "api.openalex.org:discovery",
    "stage": "discovery"
  }
}
```

### `p-working-memory-01`

```json
{
  "project": "p-working-memory-01",
  "domain": "psychology",
  "no_progress": 2,
  "routes": [
    "api.crossref.org:discovery",
    "api.openalex.org:discovery"
  ],
  "capability_blocked": false,
  "retry_after_version": null,
  "persistent_identifiers": [
    "doi:10.1093/acprof:oso/9780198570394.003.0009",
    "doi:10.1016/b978-012102570-0/50006-9",
    "doi:10.1007/springerreference_169191",
    "doi:10.1016/j.neuroscience.2005.12.061",
    "doi:10.1017/s0140525x01003922",
    "doi:10.3758/bf03196772",
    "doi:10.3758/bf03196772.pdf",
    "doi:10.1146/annurev-psych-010814-015031",
    "openalex:W2140802989",
    "openalex:W2166667242",
    "openalex:W2164740960",
    "openalex:W2162809807"
  ],
  "last_receipt": {
    "evidence": "source-d170da59cdd54b68",
    "outcome": "no_progress",
    "persistent_identifiers": [
      "doi:10.1016/j.neuroscience.2005.12.061",
      "doi:10.1017/s0140525x01003922",
      "doi:10.3758/bf03196772",
      "doi:10.3758/bf03196772.pdf",
      "doi:10.1146/annurev-psych-010814-015031",
      "openalex:W2140802989",
      "openalex:W2166667242",
      "openalex:W2164740960",
      "openalex:W2162809807"
    ],
    "research_id": "r-wm-02-baddeley",
    "route": "api.openalex.org:discovery",
    "stage": "discovery"
  }
}
```

## Problem representations

_None recorded._

## Squirrel attention receipts

### `counters`

```json
{
  "consciousness": 1,
  "psychology": 1
}
```

### `deferred`

```json
{}
```

### `last_receipt`

```json
{
  "durable_progress": false,
  "hard_rejection": false,
  "invocation": "w-d2314c66d29247bf",
  "restored_topics": [],
  "selected_topic": "psychology",
  "terminal": "accepted",
  "triggered_topics": []
}
```

## Notebooks

_None recorded._

## Invocations

### `w-76db929d18894d37`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 13144,
    "delivered_request_chars": 35946,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 35946,
    "working_set_chars": 422
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-76db929d18894d37",
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
  "process_id": 2041,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "c82815f2805a519a63fe994d67e5e36b663a2986532902155f4f0285a874f69b",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 10,
      "anchor_time": "2026-09-23T18:00:28.840341+00:00",
      "anchor_version": 0,
      "effective_seconds": 1663.591105
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 1663.591105,
    "effective_scale": 1.0,
    "effective_seconds_total": 1663.591105,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 6,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 6
    },
    "observed_at": "2026-09-23T18:00:28.840341+00:00",
    "previous_anchor_time": "2026-09-23T17:32:45.249236+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 1663.591105
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 13144,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0321
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
  "status": "deferred",
  "time": "2026-09-23T18:00:28.920415+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 751,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 39746,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 9495,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 39746,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1713,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 39746,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-23T18:00:57.654111+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 1713,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 751,
        "http_status": 503,
        "model": "gemini-3.8-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 39746,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 9495,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 39746,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 1713,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 39746,
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
    "request_payload_bytes": 39746,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-45efbc174da8439e`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 13165,
    "delivered_request_chars": 35967,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 35967,
    "working_set_chars": 422
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-45efbc174da8439e",
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
  "process_id": 2184,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "08a7d1340544db20cef0a2d3b9b231667667d35e8824f62a5af81ca3eeb181e9",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 26,
      "anchor_time": "2026-09-23T18:03:33.580870+00:00",
      "anchor_version": 0,
      "effective_seconds": 1848.331634
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 184.740529,
    "effective_scale": 1.0,
    "effective_seconds_total": 1848.331634,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 15
    },
    "observed_at": "2026-09-23T18:03:33.580870+00:00",
    "previous_anchor_time": "2026-09-23T18:00:28.840341+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 184.740529
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 13165,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0321
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
  "status": "deferred",
  "time": "2026-09-23T18:03:33.596666+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 225,
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
            "retryDelay": "21s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 21.419189961s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 39803,
      "response_bytes_captured": 1363,
      "result": "daily_quota"
    },
    {
      "category": "server",
      "elapsed_ms": 6318,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 39803,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 14907,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 39803,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-23T18:04:08.195612+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 14907,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "http",
        "elapsed_ms": 225,
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
              "retryDelay": "21s"
            }
          ],
          "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 21.419189961s.",
          "status": "RESOURCE_EXHAUSTED"
        },
        "request_payload_bytes": 39803,
        "response_bytes_captured": 1363,
        "result": "daily_quota"
      },
      {
        "category": "server",
        "elapsed_ms": 6318,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 39803,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 14907,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 39803,
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
    "request_payload_bytes": 39803,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-ec2134b1da6540bd`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 13111,
    "delivered_request_chars": 35913,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 35913,
    "working_set_chars": 422
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-ec2134b1da6540bd",
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
  "quota_day": "2026-09-23",
  "request_hash": "4a9437854e3b6815a1f941870b7d5e5a319e9fc53374084ca934eb80871efed9",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 42,
      "anchor_time": "2026-09-23T18:06:32.058991+00:00",
      "anchor_version": 0,
      "effective_seconds": 2026.809755
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 178.478121,
    "effective_scale": 1.0,
    "effective_seconds_total": 2026.809755,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 15
    },
    "observed_at": "2026-09-23T18:06:32.058991+00:00",
    "previous_anchor_time": "2026-09-23T18:03:33.580870+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 178.478121
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 13111,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0322
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
  "time": "2026-09-23T18:06:32.089484+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 222,
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
            "retryDelay": "24s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 24.912933014s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 39721,
      "response_bytes_captured": 1363,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 16501,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 39721,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T18:06:57.090288+00:00",
  "reason": ""
}
```

### `w-2a567ff8d9784759`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 15335,
    "delivered_request_chars": 37606,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 37606,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-2a567ff8d9784759",
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
        "id": "p-conscious-theories-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2200,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "2907d9eef7d9bdf99a0738b9cda5a822923fc1838c870c327e10ac6aaacfc470",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 59,
      "anchor_time": "2026-09-23T18:08:42.236673+00:00",
      "anchor_version": 1,
      "effective_seconds": 2156.987437
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 130.177682,
    "effective_scale": 1.0,
    "effective_seconds_total": 2156.987437,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 16
    },
    "observed_at": "2026-09-23T18:08:42.236673+00:00",
    "previous_anchor_time": "2026-09-23T18:06:32.058991+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 130.177682
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 15335,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.0496
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:08:42.270397+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 17490,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41560,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:09:04.198578+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 17490,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 17490,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 41560,
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
    "request_payload_bytes": 41560,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-e62357f1f80249b5`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 15337,
    "delivered_request_chars": 37608,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 37608,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-e62357f1f80249b5",
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
        "id": "p-conscious-theories-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2113,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "31648c572e3030217384f9493b483eb637246c2b022d180814f8a767ae6c3538",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 71,
      "anchor_time": "2026-09-23T18:20:17.541348+00:00",
      "anchor_version": 1,
      "effective_seconds": 2852.292112
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 695.304675,
    "effective_scale": 1.0,
    "effective_seconds_total": 2852.292112,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 11
    },
    "observed_at": "2026-09-23T18:20:17.541348+00:00",
    "previous_anchor_time": "2026-09-23T18:08:42.236673+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 695.304675
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 15337,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.0496
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:20:17.567000+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 6909,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41566,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:20:28.963656+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 6909,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 6909,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 41566,
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
    "request_payload_bytes": 41566,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-c02235666a004190`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 15332,
    "delivered_request_chars": 37603,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 37603,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-c02235666a004190",
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
        "id": "p-conscious-theories-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2112,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "c1814a91f0dc66e8636405d4d209bfe600e30c50748313edee7d9d125e2157ad",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 83,
      "anchor_time": "2026-09-23T18:34:57.435638+00:00",
      "anchor_version": 1,
      "effective_seconds": 3732.186402
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 879.89429,
    "effective_scale": 1.0,
    "effective_seconds_total": 3732.186402,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 11
    },
    "observed_at": "2026-09-23T18:34:57.435638+00:00",
    "previous_anchor_time": "2026-09-23T18:20:17.541348+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 879.89429
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 15332,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.0496
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:34:57.486033+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 5417,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 41535,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T18:35:07.649259+00:00",
  "reason": "Commitment must be due in a future cycle, within 100 cycles"
}
```

### `w-95771b59a4af446b`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 15338,
    "delivered_request_chars": 37609,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 37609,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-95771b59a4af446b",
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
        "id": "p-conscious-theories-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2267,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "67036cf3211756c7d791a23001e3164023a44c62ec7d5ab0feb2dd616e091423",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 96,
      "anchor_time": "2026-09-23T18:37:51.399791+00:00",
      "anchor_version": 1,
      "effective_seconds": 3906.150555
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 173.964153,
    "effective_scale": 1.0,
    "effective_seconds_total": 3906.150555,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 1,
      "research_collected": 0,
      "squirrel_assessed": 1,
      "total": 12
    },
    "observed_at": "2026-09-23T18:37:51.399791+00:00",
    "previous_anchor_time": "2026-09-23T18:34:57.435638+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 173.964153
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 15338,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.0496
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:37:51.454812+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 33787,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 41507,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T18:38:29.621897+00:00",
  "reason": ""
}
```

### `w-3fd39820b9b24ec0`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 16564,
    "delivered_request_chars": 38835,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 38835,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-3fd39820b9b24ec0",
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
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2341,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "4241ba0b951876f0a43ff58b10bb93a741e098b890ab2a5fcec264707e3f7141",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 111,
      "anchor_time": "2026-09-23T18:40:16.216381+00:00",
      "anchor_version": 2,
      "effective_seconds": 4050.967145
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 144.81659,
    "effective_scale": 1.0,
    "effective_seconds_total": 4050.967145,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 14
    },
    "observed_at": "2026-09-23T18:40:16.216381+00:00",
    "previous_anchor_time": "2026-09-23T18:37:51.399791+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 144.81659
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 16564,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.0459
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:40:16.281922+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1375,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 42897,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:40:22.317356+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 1375,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 1375,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 42897,
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
    "request_payload_bytes": 42897,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-00b355b055e64d09`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 16520,
    "delivered_request_chars": 38791,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 38791,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-00b355b055e64d09",
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
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2262,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "76ffa6431708ea7ed11f7be876a98f0d82f4795c43fe1c730baddef6066e3a38",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 123,
      "anchor_time": "2026-09-23T18:42:45.861114+00:00",
      "anchor_version": 2,
      "effective_seconds": 4200.611878
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 149.644733,
    "effective_scale": 1.0,
    "effective_seconds_total": 4200.611878,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 11
    },
    "observed_at": "2026-09-23T18:42:45.861114+00:00",
    "previous_anchor_time": "2026-09-23T18:40:16.216381+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 149.644733
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 16520,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.046
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:42:45.938895+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 423,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 42823,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:42:51.418579+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 423,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 423,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 42823,
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
    "request_payload_bytes": 42823,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-5d2afddfe7884de2`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 16557,
    "delivered_request_chars": 38828,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 38828,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-5d2afddfe7884de2",
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
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2238,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "0c38eb4381cb97c726b8a3856c36f332347ce0e468ff60227afd87c8fd3a1764",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 135,
      "anchor_time": "2026-09-23T18:45:56.854939+00:00",
      "anchor_version": 2,
      "effective_seconds": 4391.605703
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 190.993825,
    "effective_scale": 1.0,
    "effective_seconds_total": 4391.605703,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 11
    },
    "observed_at": "2026-09-23T18:45:56.854939+00:00",
    "previous_anchor_time": "2026-09-23T18:42:45.861114+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 190.993825
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 16557,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.0459
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:45:56.932051+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 431,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 42866,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:46:01.980648+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 431,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 431,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 42866,
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
    "request_payload_bytes": 42866,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-dd3f704c9d5044e0`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 16530,
    "delivered_request_chars": 38801,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 38801,
    "working_set_chars": 760
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-dd3f704c9d5044e0",
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
    "projects": [
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
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
  "process_id": 2275,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "bd27f4b3405d41788a25f8b44fd664da350374ef5a616a6d816e339050491aef",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "consciousness",
    "temporal": {
      "anchor_seq": 147,
      "anchor_time": "2026-09-23T18:48:14.893616+00:00",
      "anchor_version": 2,
      "effective_seconds": 4529.64438
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 138.038677,
    "effective_scale": 1.0,
    "effective_seconds_total": 4529.64438,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 11
    },
    "observed_at": "2026-09-23T18:48:14.893616+00:00",
    "previous_anchor_time": "2026-09-23T18:45:56.854939+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 138.038677
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 16530,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 760,
    "working_to_delivered_ratio": 0.046
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
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
  "time": "2026-09-23T18:48:14.982189+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 4256,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 42785,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T18:48:23.842128+00:00",
  "reason": ""
}
```

### `w-404be1225b3a4b92`

```json
{
  "base_version": 3,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 18733,
    "delivered_request_chars": 41004,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 41004,
    "working_set_chars": 1092
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-404be1225b3a4b92",
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
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "components": {
          "coherence": 0.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "p-working-memory-01",
        "score": 0.575,
        "signals": {
          "collected_research": 0,
          "notebooks": 0,
          "queued_research": 1
        },
        "title": "Foundations of Working Memory Models"
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
  "process_id": 2258,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "42d3fffb4048fbb07a899e4a9a1f674cf49cd70f0ca18e85e6d0e222b3e82632",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "psychology",
    "temporal": {
      "anchor_seq": 162,
      "anchor_time": "2026-09-23T18:50:29.464744+00:00",
      "anchor_version": 3,
      "effective_seconds": 4664.215508
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 134.571128,
    "effective_scale": 1.0,
    "effective_seconds_total": 4664.215508,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 14
    },
    "observed_at": "2026-09-23T18:50:29.464744+00:00",
    "previous_anchor_time": "2026-09-23T18:48:14.893616+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 134.571128
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 18733,
    "inquiry_drive_project_count": 2,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1092,
    "working_to_delivered_ratio": 0.0583
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "id": "p-working-memory-01",
        "next_step": "Identify foundational literature differentiating working memory from short-term memory.",
        "question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
        "title": "Foundations of Working Memory Models"
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
  "time": "2026-09-23T18:50:29.573687+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 18421,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 45236,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:50:55.015012+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 18421,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 18421,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 45236,
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
    "request_payload_bytes": 45236,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-ecc50bdf4eba4e60`

```json
{
  "base_version": 3,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 19525,
    "delivered_request_chars": 41796,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 41796,
    "working_set_chars": 1092
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-ecc50bdf4eba4e60",
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
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "components": {
          "coherence": 0.5,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "p-working-memory-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Working Memory Models"
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
  "process_id": 2040,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "04a5249d4249164e3e7a4fec6911a4c05c12b31e4693d905e5f54a110e9ddc51",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "psychology",
    "temporal": {
      "anchor_seq": 176,
      "anchor_time": "2026-09-23T18:53:08.772231+00:00",
      "anchor_version": 3,
      "effective_seconds": 4823.522995
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 159.307487,
    "effective_scale": 1.0,
    "effective_seconds_total": 4823.522995,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 0,
      "total": 13
    },
    "observed_at": "2026-09-23T18:53:08.772231+00:00",
    "previous_anchor_time": "2026-09-23T18:50:29.464744+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 159.307487
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 19525,
    "inquiry_drive_project_count": 2,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1092,
    "working_to_delivered_ratio": 0.0559
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "id": "p-working-memory-01",
        "next_step": "Identify foundational literature differentiating working memory from short-term memory.",
        "question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
        "title": "Foundations of Working Memory Models"
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
  "time": "2026-09-23T18:53:09.022649+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 52337,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 46130,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T18:54:07.935168+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 52337,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 52337,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 46130,
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
    "request_payload_bytes": 46130,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-812e1bb0e6344c00`

```json
{
  "base_version": 3,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 19520,
    "delivered_request_chars": 41791,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 41791,
    "working_set_chars": 1092
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-812e1bb0e6344c00",
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
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "components": {
          "coherence": 0.5,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "p-working-memory-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Working Memory Models"
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
  "process_id": 2258,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "8f83e4c7326202cb3cf179c06ed5d5e4218f4d9eeca08164aea49c66929a9b8b",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "psychology",
    "temporal": {
      "anchor_seq": 188,
      "anchor_time": "2026-09-23T18:56:27.397984+00:00",
      "anchor_version": 3,
      "effective_seconds": 5022.148748
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 198.625753,
    "effective_scale": 1.0,
    "effective_seconds_total": 5022.148748,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 11
    },
    "observed_at": "2026-09-23T18:56:27.397984+00:00",
    "previous_anchor_time": "2026-09-23T18:53:08.772231+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 198.625753
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 19520,
    "inquiry_drive_project_count": 2,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1092,
    "working_to_delivered_ratio": 0.0559
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "id": "p-working-memory-01",
        "next_step": "Identify foundational literature differentiating working memory from short-term memory.",
        "question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
        "title": "Foundations of Working Memory Models"
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
  "time": "2026-09-23T18:56:27.506753+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 13412,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 46105,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T18:56:46.188845+00:00",
  "reason": "Commitment must be due in a future cycle, within 100 cycles"
}
```

### `w-9baec6118bcf4e65`

```json
{
  "base_version": 3,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 19585,
    "delivered_request_chars": 41856,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 41856,
    "working_set_chars": 1092
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-9baec6118bcf4e65",
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
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "components": {
          "coherence": 0.5,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "p-working-memory-01",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Working Memory Models"
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
  "process_id": 2054,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "86274c72888cba160326576a6ff91268f52322facd1213143b2a48971d7d4ba9",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "psychology",
    "temporal": {
      "anchor_seq": 201,
      "anchor_time": "2026-09-23T18:58:55.614331+00:00",
      "anchor_version": 3,
      "effective_seconds": 5170.365095
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 148.216347,
    "effective_scale": 1.0,
    "effective_seconds_total": 5170.365095,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 1,
      "research_collected": 0,
      "squirrel_assessed": 1,
      "total": 12
    },
    "observed_at": "2026-09-23T18:58:55.614331+00:00",
    "previous_anchor_time": "2026-09-23T18:56:27.397984+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 148.216347
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 19585,
    "inquiry_drive_project_count": 2,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1092,
    "working_to_delivered_ratio": 0.0558
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "id": "p-working-memory-01",
        "next_step": "Identify foundational literature differentiating working memory from short-term memory.",
        "question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
        "title": "Foundations of Working Memory Models"
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
  "time": "2026-09-23T18:58:55.757084+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 4595,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 46185,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T18:59:06.402196+00:00",
  "reason": ""
}
```

### `w-d2314c66d29247bf`

```json
{
  "base_version": 4,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 20544,
    "delivered_request_chars": 42815,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 42815,
    "working_set_chars": 1092
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T17:32:45.249236+00:00",
    "controls": {
      "time_dilation": {
        "affects": [
          "telemetry",
          "provider_context"
        ],
        "description": "Records wall, cycle and intervening-event distance; effective time follows the selected mapping.",
        "enabled": true,
        "mode": "real",
        "scale": 1.0
      }
    },
    "effective_from_version": 0,
    "effective_seconds": 0.0,
    "event_seq": 3,
    "id": "reg-df573bb03399f050",
    "reason": "Initialize the default experimental instrument regime."
  },
  "id": "w-d2314c66d29247bf",
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
        "id": "p-conscious-theories-01",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "components": {
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "p-working-memory-01",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Working Memory Models"
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
  "process_id": 2238,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "868b1e9eb45156a068d109d90f1644dbb20bbb93903b2186d3c3cdac9dce5d79",
  "retrieval_shadow": {
    "candidates": [],
    "evidence_ids": [],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "The engine may explicitly rehydrate qualifying selected IDs into provider context."
    ],
    "metrics": {
      "candidate_count": 0,
      "evidence_count": 0,
      "trigger_counts": {}
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "psychology",
    "temporal": {
      "anchor_seq": 216,
      "anchor_time": "2026-09-23T19:00:57.328147+00:00",
      "anchor_version": 4,
      "effective_seconds": 5292.078911
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 121.713816,
    "effective_scale": 1.0,
    "effective_seconds_total": 5292.078911,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 14
    },
    "observed_at": "2026-09-23T19:00:57.328147+00:00",
    "previous_anchor_time": "2026-09-23T18:58:55.614331+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 121.713816
  },
  "trust_compacts_shadow": {
    "compacts": [],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 0,
      "challenged_count": 0,
      "evidence_root_count": 0,
      "provisional_count": 0,
      "settled_count": 0,
      "status_counts": {}
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 20544,
    "inquiry_drive_project_count": 2,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1092,
    "working_to_delivered_ratio": 0.0532
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "p-conscious-theories-01",
        "next_step": "Perform literature search for comparative analysis of major consciousness theories.",
        "question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
        "title": "Empirical Foundations of Consciousness Theories"
      },
      {
        "id": "p-working-memory-01",
        "next_step": "Identify foundational literature differentiating working memory from short-term memory.",
        "question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
        "title": "Foundations of Working Memory Models"
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
  "time": "2026-09-23T19:00:57.460989+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 7366,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 47266,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T19:01:10.550025+00:00",
  "reason": ""
}
```

## Evidence

### `source-bb7c8fcae91c44da`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e48d3ecad72630f95468009c3b28eaee5c6aeaecc83b9616dd560d23e61b266d\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bb7c8fcae91c44da",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 0,
  "time": "2026-09-23T18:00:26.793782+00:00"
}
```

### `source-6b244e93a5094039`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239479,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Greek religion\\\",\\\"pageid\\\":1820505,\\\"size\\\":396,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"Greek\\nreligion\\ncan refer to several things, including Ancient Greek\\nreligion\\nGreek hero cult Greco-Roman mysteries Hellenistic\\nreligion\\nPlatonic idealism\\\",\\\"timestamp\\\":\\\"2021-07-16T15:59:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"0edf688e22edbdbff3a3bd5d288c77674076dfdb9ce879475c5ceb986176b391\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6b244e93a5094039",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-23T18:00:27.183817+00:00"
}
```

### `source-61f48b67d1fc499e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"27ebe5ea77f80397a7c73d9eb47ad32ad6b7fa4570b0d2952691b6a09b786c20\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-61f48b67d1fc499e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-23T18:00:27.541268+00:00"
}
```

### `source-37817f17beb14f0b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149369},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"dd196ca5344cd162f8c4eb991a83cdaa8abfa3b693941d7cf37d091447e9fef4\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-37817f17beb14f0b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-23T18:00:27.966708+00:00"
}
```

### `source-ec7bdf4236ec4731`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vitamin D and neurology\\\",\\\"pageid\\\":37130699,\\\"size\\\":21444,\\\"wordcount\\\":2646,\\\"snippet\\\":\\\"been associated with many other conditions, including both\\nneurological\\nand non\\nneurological\\nconditions. These include but are not limited to autism, diabetes\\\",\\\"timestamp\\\":\\\"2025-09-15T21:51:23Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"da4e32d05699e6a24ad8c9eeae82461c17c007b57ea159b4563180859ab20473\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-ec7bdf4236ec4731",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 0,
  "time": "2026-09-23T18:00:28.429566+00:00"
}
```

### `source-25f3bee467d44275`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ea6ce9888ae846b7bfbe7fe339f3173ea0c010c24dabb2d5ff499464e8342c40\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-25f3bee467d44275",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 0,
  "time": "2026-09-23T18:00:28.724775+00:00"
}
```

### `r-76db929d18894d37`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-76db929d18894d37\",\"previous_head\":\"de3557c5074899a5dab50bb32b302c7eeef04c63e3265dc76f35de93a83dc2b1\",\"process_id\":2041,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-76db929d18894d37",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-23T18:00:28.912211+00:00"
}
```

### `source-fe046e01cdd6415c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74323},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e7277fcdf9d7b81a00750ee23d8a2fb728e31aaf0be3b89a8712d7ffaa586e67\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-fe046e01cdd6415c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 0,
  "time": "2026-09-23T18:03:31.700874+00:00"
}
```

### `source-1d4e190054f24713`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149368,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1297a189344096e53f623ac870788ca35defada0b6172fa13fec797ae6331ae9\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-1d4e190054f24713",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-23T18:03:32.082387+00:00"
}
```

### `source-cc8e5dc7d33a482e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239482,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"094404feb6dd7101bcc78af17a06dcffa7266a0db814f5f33d78035395b44ecd\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-cc8e5dc7d33a482e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-23T18:03:32.521562+00:00"
}
```

### `source-72df4cd0146842dd`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone deficiency\\\",\\\"pageid\\\":620879,\\\"size\\\":30695,\\\"wordcount\\\":3241,\\\"snippet\\\":\\\"of Growth\\nHormone\\nDeficiency: A Position Statement from Korean\\nEndocrine\\nSociety and Korean Society of Pediatric\\nEndocrinology\\n\\\".\\nEndocrinology\\nand Metabolism\\\",\\\"timestamp\\\":\\\"2026-05-10T21:56:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"08b332d0e1941de204147919f6e91f2b900b2383a5de1b50c24baa2a9d60c565\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-72df4cd0146842dd",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 0,
  "time": "2026-09-23T18:03:32.899531+00:00"
}
```

### `source-cb9ebbb99a6f4c3d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"Many people affected by MSA experience dysfunction of the autonomic\\nnervous\\nsystem\\n, which commonly manifests as orthostatic hypotension, impotence, loss\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"61ac48d8037cd249c617f22f290f98601c29e5b72620a14ed8ea3acb2ade68eb\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-cb9ebbb99a6f4c3d",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 0,
  "time": "2026-09-23T18:03:33.301787+00:00"
}
```

### `source-e87e81465bd04b83`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"cc40fc8fa03d11040148ac4334e131ef3ec27a15b530b7cfc2c5a64c5adbf8c6\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e87e81465bd04b83",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-23T18:03:33.575286+00:00"
}
```

### `r-45efbc174da8439e`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-45efbc174da8439e\",\"previous_head\":\"7ad20462d95ab586ccbfcb00154141e96f06d6e6be67dc468dbd50f031596201\",\"process_id\":2184,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-45efbc174da8439e",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-23T18:03:33.590193+00:00"
}
```

### `source-e2489e707fe94003`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"cc40fc8fa03d11040148ac4334e131ef3ec27a15b530b7cfc2c5a64c5adbf8c6\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e2489e707fe94003",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-23T18:06:30.650721+00:00"
}
```

### `source-bc7ed7addc024d8f`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"Many people affected by MSA experience dysfunction of the autonomic\\nnervous\\nsystem\\n, which commonly manifests as orthostatic hypotension, impotence, loss\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b2d4eeb4d4d7ea021517b4f1bb5752c14ddcf3bb54d666f6edce919f095711b9\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bc7ed7addc024d8f",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 0,
  "time": "2026-09-23T18:06:30.912554+00:00"
}
```

### `source-6e62360bda9b4842`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone deficiency\\\",\\\"pageid\\\":620879,\\\"size\\\":30695,\\\"wordcount\\\":3241,\\\"snippet\\\":\\\"of Growth\\nHormone\\nDeficiency: A Position Statement from Korean\\nEndocrine\\nSociety and Korean Society of Pediatric\\nEndocrinology\\n\\\".\\nEndocrinology\\nand Metabolism\\\",\\\"timestamp\\\":\\\"2026-05-10T21:56:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"08b332d0e1941de204147919f6e91f2b900b2383a5de1b50c24baa2a9d60c565\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6e62360bda9b4842",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 0,
  "time": "2026-09-23T18:06:31.265533+00:00"
}
```

### `source-ada6502a6a354962`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239482,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"d1271d8a95e13b3089c5855bce037f342f3d1c3c50911e5d84976ec94ac3a07a\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-ada6502a6a354962",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-23T18:06:31.523115+00:00"
}
```

### `source-076b06ab15a148a3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74323},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"331b37d8f97bccde561d1f6fe601aaf8b83fbbbc6487ee097d69c77ada1c57a8\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-076b06ab15a148a3",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 0,
  "time": "2026-09-23T18:06:31.799372+00:00"
}
```

### `source-def355a92a60470f`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149368,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"03661c1da8dbcaf5c3dc4cc932f3d8fb26e1b18869d3612e849ce559dda583dc\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-def355a92a60470f",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-23T18:06:32.049873+00:00"
}
```

### `r-ec2134b1da6540bd`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-ec2134b1da6540bd\",\"previous_head\":\"faef66d9a67a8db953305998356e3c96a115ab92b9f2ba5e4b0e8012216f6e2d\",\"process_id\":2267,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-ec2134b1da6540bd",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-23T18:06:32.079879+00:00"
}
```

### `source-704ee264434e4771`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=major+scientific+theories+of+consciousness+empirical+predictions+comparison&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2132470305\\\", \\\"doi\\\": \\\"https://doi.org/10.1080/08870446.2011.613995\\\", \\\"title\\\": \\\"The theory of planned behaviour: Reactions and reflections\\\", \\\"publication_year\\\": 2011, \\\"type\\\": \\\"editorial\\\", \\\"cited_by_count\\\": 4680, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://www.tandfonline.com/doi/pdf/10.1080/08870446.2011.613995?needAccess=true&role=button\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1080/08870446.2011.613995\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1080/08870446.2011.613995\\\", \\\"pdf_url\\\": \\\"https://www.tandfonline.com/doi/pdf/10.1080/08870446.2011.613995?needAccess=true&role=button\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S88763227\\\", \\\"display_name\\\": \\\"Psychology and Health\\\", \\\"issn_l\\\": \\\"0887-0446\\\", \\\"issn\\\": [\\\"0887-0446\\\", \\\"1476-8321\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"erih-plus\\\", \\\"jufo-2\\\", \\\"ki-jl-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320547\\\", \\\"host_organization_name\\\": \\\"Taylor & Francis\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320547\\\", \\\"https://openalex.org/P4310320449\\\"], \\\"host_organization_lineage_names\\\": [\\\"Taylor & Francis\\\", \\\"Informa\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Psychology &amp; Health\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The seven articles in this issue, and the accompanying meta-analysis in Health Psychology Review [McEachan, R.R.C., Conner, M., Taylor, N., & Lawton, R.J. (2011). Prospective prediction of health-related behaviors with the theory of planned behavior: A meta-analysis. Health Psychology Review, 5, 97-144], illustrate the wide application of the theory of planned behaviour [Ajzen, I. (1991). The theory of planned behavior. Organizational Behavior and Human Decision Processes, 50, 179-211] in the health domain. In this editorial, Ajzen reflects on some of the issues raised by the different authors. Among the topics addressed are the nature of intentions and the limits of predictive validity; rationality, affect and emotions; past behaviour and habit; the prototype/willingness model; and the role of such background factors as the big five personality traits and social comparison tendency.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W1969469858\\\", \\\"doi\\\": \\\"https://doi.org/10.1371/journal.pcbi.1003588\\\", \\\"title\\\": \\\"From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0\\\", \\\"publication_year\\\": 2014, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 1207, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003588&type=printable\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1371/journal.pcbi.1003588\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1371/journal.pcbi.1003588\\\", \\\"pdf_url\\\": \\\"https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003588&type=printable\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S86033158\\\", \\\"display_name\\\": \\\"PLoS Computational Biology\\\", \\\"issn_l\\\": \\\"1553-734X\\\", \\\"issn\\\": [\\\"1553-734X\\\", \\\"1553-7358\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\", \\\"doyens\\\", \\\"jufo-3\\\", \\\"ki-jl-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310315706\\\", \\\"host_organization_name\\\": \\\"Public Library of Science\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315706\\\"], \\\"host_organization_lineage_names\\\": [\\\"Public Library of Science\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"PLoS Computational Biology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"This paper presents Integrated Information Theory (IIT) of consciousness 3.0, which incorporates several advances over previous formulations. IIT starts from phenomenological axioms: information says that each experience is specific--it is what it is by how it differs from alternative experiences; integration says that it is unified--irreducible to non-interdependent components; exclusion says that it has unique borders and a particular spatio-temporal grain. These axioms are formalized into postulates that prescribe how physical mechanisms, such as neurons or logic gates, must be configured to generate experience (phenomenology). The postulates are used to define intrinsic information as \\\\\\\"differences that make a difference\\\\\\\" within a system, and integrated information as information specified by a whole that cannot be reduced to that specified by its parts. By applying the postulates both at the level of individual mechanisms and at the level of systems of mechanisms, IIT arrives at an identity: an experience is a maximally irreducible conceptual structure (MICS, a constellation of concepts in qualia space), and the set of elements that generates it constitutes a complex. According to IIT, a MICS specifies the quality of an experience and integrated information ΦMax its quantity. From the theory follow several results, including: a system of mechanisms may condense into a major complex and non-overlapping minor complexes; the concepts that specify the quality of an experience are always about the complex itself and relate only indirectly to the external environment; anatomical connectivity influences complexes and associated MICS; a complex can generate a MICS even if its elements are inactive; simple systems can be minimally conscious; complicated systems can be unconscious; there can be true \\\\\\\"zombies\\\\\\\"--unconscious feed-forward systems that are functionally equivalent to conscious complexes.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2588736771\\\", \\\"doi\\\": \\\"https://doi.org/10.1073/pnas.1619316114\\\", \\\"title\\\": \\\"A higher-order theory of emotional consciousness\\\", \\\"publication_year\\\": 2017, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 710, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://www.pnas.org/content/pnas/114/10/E2016.full.pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1073/pnas.1619316114\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1073/pnas.1619316114\\\", \\\"pdf_url\\\": \\\"https://www.pnas.org/content/pnas/114/10/E2016.full.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S125754415\\\", \\\"display_name\\\": \\\"Proceedings of the National Academy of Sciences\\\", \\\"issn_l\\\": \\\"0027-8424\\\", \\\"issn\\\": [\\\"0027-8424\\\", \\\"1091-6490\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"erih-plus\\\", \\\"jufo-3\\\", \\\"ki-jl-3\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320052\\\", \\\"host_organization_name\\\": \\\"National Academy of Sciences\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320052\\\"], \\\"host_organization_lineage_names\\\": [\\\"National Academy of Sciences\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Proceedings of the National Academy of Sciences\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Emotional states of consciousness, or what are typically called emotional feelings, are traditionally viewed as being innately programmed in subcortical areas of the brain, and are often treated as different from cognitive states of consciousness, such as those related to the perception of external stimuli. We argue that conscious experiences, regardless of their content, arise from one system in the brain. In this view, what differs in emotional and nonemotional states are the kinds of inputs that are processed by a general cortical network of cognition, a network essential for conscious experiences. Although subcortical circuits are not directly responsible for conscious feelings, they provide nonconscious inputs that coalesce with other kinds of neural signals in the cognitive assembly of conscious emotional experiences. In building the case for this proposal, we defend a modified version of what is known as the higher-order theory of consciousness.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2170232314\\\", \\\"doi\\\": \\\"https://doi.org/10.1098/rstb.2014.0167\\\", \\\"title\\\": \\\"Consciousness: here, there and everywhere?\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 815, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"https://royalsocietypublishing.org/doi/pdf/10.1098/rstb.2014.0167\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1098/rstb.2014.0167\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1098/rstb.2014.0167\\\", \\\"pdf_url\\\": \\\"https://royalsocietypublishing.org/doi/pdf/10.1098/rstb.2014.0167\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S91660768\\\", \\\"display_name\\\": \\\"Philosophical Transactions of the Royal Society B Biological Sciences\\\", \\\"issn_l\\\": \\\"0962-8436\\\", \\\"issn\\\": [\\\"0962-8436\\\", \\\"1471-2970\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-2\\\", \\\"ki-jl-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319787\\\", \\\"host_organization_name\\\": \\\"Royal Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319787\\\"], \\\"host_organization_lineage_names\\\": [\\\"Royal Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Philosophical Transactions of the Royal Society B: Biological Sciences\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The science of consciousness has made great strides by focusing on the behavioural and neuronal correlates of experience. However, while such correlates are important for progress to occur, they are not enough if we are to understand even basic facts, for example, why the cerebral cortex gives rise to consciousness \", \"excerpt_truncated\": true, \"source_sha256\": \"0a41df4798bd38202f38e7aa8e45a983f235db96e5d640065ce7ff065156ece9\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1080/08870446.2011.613995\", \"doi:10.1371/journal.pcbi.1003588\", \"doi:10.1073/pnas.1619316114\", \"doi:10.1098/rstb.2014.0167\", \"openalex:W2132470305\", \"openalex:W1969469858\", \"openalex:W2588736771\", \"openalex:W2170232314\", \"arxiv:2014.0167\"]}",
  "id": "source-704ee264434e4771",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=major+scientific+theories+of+consciousness+empirical+predictions+comparison&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 1,
  "time": "2026-09-23T18:08:40.341766+00:00"
}
```

### `source-613e0f5b48c64f44`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Greek religion\\\",\\\"pageid\\\":1820505,\\\"size\\\":396,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"Greek\\nreligion\\ncan refer to several things, including Ancient Greek\\nreligion\\nGreek hero cult Greco-Roman mysteries Hellenistic\\nreligion\\nPlatonic idealism\\\",\\\"timestamp\\\":\\\"2021-07-16T15:59:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"54794aa9301302aefd03260c4c5e3ea389be1b2b11cecef053adaf5b24c369fb\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-613e0f5b48c64f44",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T18:08:40.684715+00:00"
}
```

### `source-cc4dbe214e3f49d9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6af477cc3d998894f1f659afab330eac677766f87935149507682a3ba884ca84\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-cc4dbe214e3f49d9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-23T18:08:41.031867+00:00"
}
```

### `source-0eacabe87a5b4736`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"210716bdabb5e7c656978aa7b3932c486006f74b4bda678c31284faf65eda31b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-0eacabe87a5b4736",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:08:41.508924+00:00"
}
```

### `source-a2f7973c00824ce3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149369},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"dd196ca5344cd162f8c4eb991a83cdaa8abfa3b693941d7cf37d091447e9fef4\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-a2f7973c00824ce3",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-23T18:08:41.808195+00:00"
}
```

### `source-9a1fbc3f2cb1400d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"053255e80f34316f47f4550fae6663aac7b4875c6ec214e80e66b3eca2ec010a\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-9a1fbc3f2cb1400d",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:08:42.224821+00:00"
}
```

### `r-2a567ff8d9784759`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-2a567ff8d9784759\",\"previous_head\":\"8a9e948e38eedb606d13328f0d4bc82281b5639a2ebbe5d252f7aa6e43d05fbb\",\"process_id\":2200,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-2a567ff8d9784759",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T18:08:42.258508+00:00"
}
```

### `source-e8f1876498224c28`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"Many people affected by MSA experience dysfunction of the autonomic\\nnervous\\nsystem\\n, which commonly manifests as orthostatic hypotension, impotence, loss\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vitamin D and neurology\\\",\\\"pageid\\\":37130699,\\\"size\\\":21444,\\\"wordcount\\\":2646,\\\"snippet\\\":\\\"been associated with many other conditions, including both\\nneurological\\nand non\\nneurological\\nconditions. These include but are not limited to autism, diabetes\\\",\\\"timestamp\\\":\\\"2025-09-15T21:51:23Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9fff5da9b879f5ea9c3f766e3078d63d9a02b319fab88b2b999378abf708a8a0\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e8f1876498224c28",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:20:15.178855+00:00"
}
```

### `source-5f1477e0532e4d10`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239477,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"159d934cedc0b48b93d0406c6ca1c3e2cc279805278f99124302e52b74caba6f\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5f1477e0532e4d10",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T18:20:15.563417+00:00"
}
```

### `source-07761ba261644f9f`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"02be6c01097124b8eecf4929ead5155565fb0f43310ea05d63f889fb84e9725d\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-07761ba261644f9f",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-23T18:20:16.124660+00:00"
}
```

### `source-b3c124c4cdc1473e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"f80fe813e3822d17143f8585f2237cb575a00104b1e39235dd6e17c0e05ab127\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-b3c124c4cdc1473e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-23T18:20:16.543888+00:00"
}
```

### `source-43614ab454034d29`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Acromegaly\\\",\\\"pageid\\\":20936195,\\\"size\\\":41489,\\\"wordcount\\\":3937,\\\"snippet\\\":\\\"acromegaly: evolution of the techniques and outcomes\\\". Reviews in\\nEndocrine\\n& Metabolic\\nDisorders\\n. 9 (1): 67\\\\u201370. doi:10.1007/s11154-007-9064-y. PMID\\\\u00a018228147\\\",\\\"timestamp\\\":\\\"2026-08-09T11:28:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"61f8946f787eba88dec1c376d03343fd6aafbfc4c9ebcf3c67e91cbb03fb2d85\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.1007/s11154-007-9064-y\"]}",
  "id": "source-43614ab454034d29",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:20:17.058264+00:00"
}
```

### `source-90d8ee98d4214895`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"4a75a9c42378a01b523c65a6b8adc687558739296be7562fb33bc9499578b3a4\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-90d8ee98d4214895",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-23T18:20:17.532593+00:00"
}
```

### `r-e62357f1f80249b5`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-e62357f1f80249b5\",\"previous_head\":\"725005c4096c229278f6cb2741f4543a9f4d41561b276c9fac1ed56fe35cb60f\",\"process_id\":2113,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-e62357f1f80249b5",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T18:20:17.558050+00:00"
}
```

### `source-84fd9d4a4a34437d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Acromegaly\\\",\\\"pageid\\\":20936195,\\\"size\\\":41489,\\\"wordcount\\\":3937,\\\"snippet\\\":\\\"acromegaly: evolution of the techniques and outcomes\\\". Reviews in\\nEndocrine\\n& Metabolic\\nDisorders\\n. 9 (1): 67\\\\u201370. doi:10.1007/s11154-007-9064-y. PMID\\\\u00a018228147\\\",\\\"timestamp\\\":\\\"2026-08-09T11:28:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"13b1ded900c2285a7e0e6e6276e37fc9e06a18f3f313d5ca2592a2e2b5ad2bbe\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.1007/s11154-007-9064-y\"]}",
  "id": "source-84fd9d4a4a34437d",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:34:54.981330+00:00"
}
```

### `source-052cad46dc63457c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Evolutionary psychology\\\",\\\"pageid\\\":9703,\\\"size\\\":177589,\\\"wordcount\\\":19341,\\\"snippet\\\":\\\"Evolutionary\\npsychology\\nis a theoretical approach in\\npsychology\\nthat examines cognition and behavior from a modern evolutionary perspective. It seeks to\\\",\\\"timestamp\\\":\\\"2026-09-14T00:20:33Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c4195859d567f74bfc0c70ec2b627b7641b45c1d8d253b41c8bc6a36d9a8d427\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-052cad46dc63457c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-23T18:34:55.336498+00:00"
}
```

### `source-2889dba48baa4b01`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239477,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"7744f6ffa3c5da81d61bdcb9f991dbc23256b4163feccaed252067cca8266dcb\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2889dba48baa4b01",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T18:34:55.937588+00:00"
}
```

### `source-8a9fb835c4014557`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a01a3763a428809ed23a3c87da9cc8c190be117da23649a45f1ccfd28a4b83ea\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-8a9fb835c4014557",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-23T18:34:56.378296+00:00"
}
```

### `source-053d3267e0ff45f8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eacdba2f34c33a4a50cfe0a47ea6541b1c53714e0b07e102b71e1408b711014b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-053d3267e0ff45f8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:34:57.031752+00:00"
}
```

### `source-14cf65f1a5d0488e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"0771cff050ffcc0824721acec6c7f3a631867cff14d441423e902e4300912263\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-14cf65f1a5d0488e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-23T18:34:57.423556+00:00"
}
```

### `r-c02235666a004190`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-c02235666a004190\",\"previous_head\":\"5e74c64667f6c29f75a6d2bbd937d9190853686c01f35a5cccd59ed1b22e91f8\",\"process_id\":2112,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-c02235666a004190",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T18:34:57.461513+00:00"
}
```

### `source-da0b471c2ea740e2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"5d94482ae75f13ed81202634b161082c01e0b95937a341ec0675d2e2dfab30e1\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-da0b471c2ea740e2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:37:49.850386+00:00"
}
```

### `source-81735c6293c44d27`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ef522925f2325648336c1037806b8e80aa7694366f14bc0b4421b17e47f9d64a\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-81735c6293c44d27",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-23T18:37:50.158640+00:00"
}
```

### `source-1bfbbf64f9524c85`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vitamin D and neurology\\\",\\\"pageid\\\":37130699,\\\"size\\\":21444,\\\"wordcount\\\":2646,\\\"snippet\\\":\\\"been associated with many other conditions, including both\\nneurological\\nand non\\nneurological\\nconditions. These include but are not limited to autism, diabetes\\\",\\\"timestamp\\\":\\\"2025-09-15T21:51:23Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"77255b1d6df21700a26d6aa4efd3b6b73226ab746148b0d74e253c7db92d2ca6\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-1bfbbf64f9524c85",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 1,
  "time": "2026-09-23T18:37:50.561655+00:00"
}
```

### `source-55bd755a02ad4972`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239477,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"024d45a0c01de30cf40f9b21ca7f14018c4cd09c7f8b13bfee5d87fce671407f\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-55bd755a02ad4972",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T18:37:50.912826+00:00"
}
```

### `source-6d0ff24a945240a7`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9269fe3f152bc084454f378b44600416dea659322d93757ea67889b7abf88f1e\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6d0ff24a945240a7",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-23T18:37:51.171656+00:00"
}
```

### `source-ca5c3c0daebe47dd`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2278564131ff2e3d8c7727d35433c88b5d1219d0fef6c107f91af366ae4695cd\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-ca5c3c0daebe47dd",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-23T18:37:51.382950+00:00"
}
```

### `r-95771b59a4af446b`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-95771b59a4af446b\",\"previous_head\":\"c18d811c6716d0cd2dc2ac61eb4a820cddea6a88a448ac0bc96003f6cfe3d7f0\",\"process_id\":2267,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-95771b59a4af446b",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T18:37:51.436850+00:00"
}
```

### `source-44ce6dec85b349c6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=empirical+predictions+comparison+Integrated+Information+Theory+vs+Global+Neuronal+Workspace+Theory&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W4319825978\\\", \\\"doi\\\": \\\"https://doi.org/10.1371/journal.pone.0268577\\\", \\\"title\\\": \\\"An adversarial collaboration protocol for testing contrasting predictions of global neuronal workspace and integrated information theory\\\", \\\"publication_year\\\": 2023, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 116, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0268577&type=printable\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1371/journal.pone.0268577\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1371/journal.pone.0268577\\\", \\\"pdf_url\\\": \\\"https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0268577&type=printable\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S202381698\\\", \\\"display_name\\\": \\\"PLoS ONE\\\", \\\"issn_l\\\": \\\"1932-6203\\\", \\\"issn\\\": [\\\"1932-6203\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\", \\\"doyens\\\", \\\"erih-plus\\\", \\\"jufo-1\\\", \\\"medline\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310315706\\\", \\\"host_organization_name\\\": \\\"Public Library of Science\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315706\\\"], \\\"host_organization_lineage_names\\\": [\\\"Public Library of Science\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"PLOS ONE\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The relationship between conscious experience and brain activity has intrigued scientists and philosophers for centuries. In the last decades, several theories have suggested different accounts for these relationships. These theories have developed in parallel, with little to no cross-talk among them. To advance research on consciousness, we established an adversarial collaboration between proponents of two of the major theories in the field, Global Neuronal Workspace and Integrated Information Theory. Together, we devised and preregistered two experiments that test contrasting predictions of these theories concerning the location and timing of correlates of visual consciousness, which have been endorsed by the theories' proponents. Predicted outcomes should either support, refute, or challenge these theories. Six theory-impartial laboratories will follow the study protocol specified here, using three complementary methods: Functional Magnetic Resonance Imaging (fMRI), Magneto-Electroencephalography (M-EEG), and intracranial electroencephalography (iEEG). The study protocol will include built-in replications, both between labs and within datasets. Through this ambitious undertaking, we hope to provide decisive evidence in favor or against the two theories and clarify the footprints of conscious visual perception in the human brain, while also providing an innovative model of large-scale, collaborative, and open science practice.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2033624480\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyg.2013.00200\\\", \\\"title\\\": \\\"Global Workspace Dynamics: Cortical “Binding and Propagation” Enables Conscious Contents\\\", \\\"publication_year\\\": 2013, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 300, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyg.2013.00200/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyg.2013.00200\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyg.2013.00200\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyg.2013.00200/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S9692511\\\", \\\"display_name\\\": \\\"Frontiers in Psychology\\\", \\\"issn_l\\\": \\\"1664-1078\\\", \\\"issn\\\": [\\\"1664-1078\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\", \\\"erih-plus\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"A global workspace (GW) is a functional hub of binding and propagation in a population of loosely coupled signaling elements. In computational applications, GW architectures recruit many distributed, specialized agents to cooperate in resolving focal ambiguities. In the brain, conscious experiences may reflect a GW function. For animals, the natural world is full of unpredictable dangers and opportunities, suggesting a general adaptive pressure for brains to resolve focal ambiguities quickly and accurately. GW theory aims to understand the differences between conscious and unconscious brain events. In humans and related species the cortico-thalamic (C-T) core is believed to underlie conscious aspects of perception, thinking, learning, feelings of knowing (FOK), felt emotions, visual imagery, working memory, and executive control. Alternative theoretical perspectives are also discussed. The C-T core has many anatomical hubs, but conscious percepts are unitary and internally consistent at any given moment. Over time, conscious contents constitute a very large, open set. This suggests that a brain-based GW capacity cannot be localized in a single anatomical hub. Rather, it should be sought in a functional hub - a dynamic capacity for binding and propagation of neural signals over multiple task-related networks, a kind of neuronal cloud computing. In this view, conscious contents can arise in any region of the C-T core when multiple input streams settle on a winner-take-all equilibrium. The resulting conscious gestalt may ignite an any-to-many broadcast, lasting ∼100-200 ms, and trigger widespread adaptation in previously established networks. To account for the great range of conscious contents over time, the theory suggests an open repertoire of binding coalitions that can broadcast via theta/gamma or alpha/gamma phase coupling, like radio channels competing for a narrow frequency band. Conscious moments are thought to hold only 1-4 unrelated items; this small focal capacity may be the biological price to pay for global access. Visuotopic maps in cortex specialize in features like color, retinal size, motion, object identity, and egocentric/allocentric framing, so that a binding coalition for the sight of a rolling billiard ball in nearby space may resonate among activity maps of LGN, V1-V4, MT, IT, as well as the dorsal stream. Spatiotopic activity maps can bind into coherent gestalts using adaptive resonance (reentry). Single neurons can join a dominant coalition by phase tuning to regional oscillations in the 4-12 Hz range. Sensory percepts may bind and broadcast from posterior cortex, while non-sensory FOKs may involve prefrontal and frontotemporal areas. The anatomy and physiology of the hippocampal complex suggest a GW architecture as well. In the intact brain the hippocampal complex may support conscious event organization as well as episodic memory storage.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W3043429318\\\", \\\"doi\\\": \\\"https://doi.org/10.1080/17588928.2020.1772214\\\", \\\"title\\\": \\\"Hard criteria for empirical theories of consciousness\\\", \\\"publication_year\\\": 2020, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 201, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"https://www.tandfonline.com/doi/pdf/10.1080/17588928.2020.1772214?needAccess=true\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1080/17588928.2020.1772214\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1080/17588928.2020.1772214\\\", \\\"pdf_url\\\": \\\"https://www.tandfonline.com/doi/pdf/10.1080/17588928.2020.1772214?needAccess=true\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S175435324\\\", \\\"display_name\\\": \\\"Cognitive Neuroscience\\\", \\\"issn_l\\\": \\\"1758-8928\\\", \\\"issn\\\": [\\\"1758-8928\\\", \\\"1758-8936\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-1\\\", \\\"medline\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320547\\\", \\\"host_organization_name\\\": \\\"Taylor & Francis\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320547\\\", \\\"https://openalex.org/P4310320449\\\"], \\\"host_organization_lineage_names\\\": [\\\"Taylor & Francis\\\", \\\"Informa\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by-nc-nd\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by-nc-nd\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Cognitive Neuroscience\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Consciousness is now a well-established field of empirical research. A large body of experimental results has been accumulated and is steadily growing. In parallel, many Theories of Consciousness (ToCs) have been proposed. These theories are diverse in nature, ranging from computational to neurophysiological and quantum theoretical approaches. This contrasts with other fields of natural science, which host a smaller number of competing theories. We suggest that one reason for this abundance of extremely different theories may be the lack of stringent criteria specifying how empirical data constrains ToCs. First, we argue that consciousness is a well-defined topic from an empirical point of view and motivate a purely empirical stance on the quest for consciousness. Second, we present a checklist of criteria that, we propose, empirical ToCs need to cope with. Third, we review 13 of the most influential ToCs and subject them to the criteria. Our analysis helps to situate these different ToCs in the theoretical landscapeand sheds light on their strengths and weaknesses from a strictly empirical point of view.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2120745192\\\", \\\"doi\\\": \\\"https://doi.org/10.1371/journal.pcbi.100046\", \"excerpt_truncated\": true, \"source_sha256\": \"588cda0da1993ec17f97d0c5af970cc16d26d0a374b30bd951c35cb8b6b4bdd6\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1371/journal.pone.0268577\", \"doi:10.3389/fpsyg.2013.00200\", \"doi:10.3389/fpsyg.2013.00200/pdf\", \"doi:10.1080/17588928.2020.1772214\", \"doi:10.1371/journal.pcbi.100046\", \"openalex:W4319825978\", \"openalex:W2033624480\", \"openalex:W3043429318\", \"openalex:W2120745192\", \"arxiv:2013.00200\"]}",
  "id": "source-44ce6dec85b349c6",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=empirical+predictions+comparison+Integrated+Information+Theory+vs+Global+Neuronal+Workspace+Theory&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 2,
  "time": "2026-09-23T18:40:13.458489+00:00"
}
```

### `source-d3541090cba6487e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a01a3763a428809ed23a3c87da9cc8c190be117da23649a45f1ccfd28a4b83ea\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d3541090cba6487e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-23T18:40:14.218687+00:00"
}
```

### `source-2d8c9b0ae8a9480d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Pediatric neurology\\\",\\\"pageid\\\":76756342,\\\"size\\\":7037,\\\"wordcount\\\":529,\\\"snippet\\\":\\\"nervous\\nsystem\\nand peripheral\\nnervous\\nsystem\\nin children. While pediatric neurologists have many similarities to neurologists, the\\nneurological\\ndisorders\\nthey\\\",\\\"timestamp\\\":\\\"2024-11-25T06:14:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c4652c287d7c27181ab7bc67bdfe4709a14cbc2c010c92ccc3ad2dc39173c921\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2d8c9b0ae8a9480d",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:40:14.759721+00:00"
}
```

### `source-3d76e3da190b4c3a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"93fc09abc91cf87e81e74fecbd1b45d39615c5de34ea0f3c5cbc67eb09541293\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3d76e3da190b4c3a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-23T18:40:15.179189+00:00"
}
```

### `source-56f433b0143b4b9f`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239477,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"f80e2af491194091e58248fdc03c3d2ee26fdaf5ab8b3f2584723720aff93bc1\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-56f433b0143b4b9f",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-23T18:40:15.692093+00:00"
}
```

### `source-9a03d8eb08e34e78`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b712d7a1f6d7cf1334f1c758ebfec89c1ea6dbcafdeee53b012b3f105a78967d\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-9a03d8eb08e34e78",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:40:16.196510+00:00"
}
```

### `r-3fd39820b9b24ec0`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[],\"invocation\":\"w-3fd39820b9b24ec0\",\"previous_head\":\"5f16878549d1963202381ca7499e19436b1ca97d0939ad9867ad786b424cbea6\",\"process_id\":2341,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-3fd39820b9b24ec0",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-23T18:40:16.261211+00:00"
}
```

### `source-e4d6296e827744e8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9269fe3f152bc084454f378b44600416dea659322d93757ea67889b7abf88f1e\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e4d6296e827744e8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-23T18:42:43.650801+00:00"
}
```

### `source-e35936bfabc4407d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"11abc05a3af9e12f17e299bfbdb58061d0d91d878dbc76f890586f34c3f332e4\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e35936bfabc4407d",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:42:44.122626+00:00"
}
```

### `source-927cb972c8ce4196`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clinical psychology\\\",\\\"pageid\\\":492271,\\\"size\\\":86163,\\\"wordcount\\\":9645,\\\"snippet\\\":\\\"Clinical\\npsychology\\nis an integration of human science, behavioral science, theory, and clinical knowledge aimed at understanding, preventing, and relieving\\\",\\\"timestamp\\\":\\\"2026-08-30T16:15:10Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"8c4e1a68dcd7d47cec10dd94fb935f5f6ae0942dfb3a5536a9d3977bd561b4e7\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-927cb972c8ce4196",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-23T18:42:44.501221+00:00"
}
```

### `source-55069e9a6e26445e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"Many people affected by MSA experience dysfunction of the autonomic\\nnervous\\nsystem\\n, which commonly manifests as orthostatic hypotension, impotence, loss\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"61ac48d8037cd249c617f22f290f98601c29e5b72620a14ed8ea3acb2ade68eb\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-55069e9a6e26445e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:42:44.934996+00:00"
}
```

### `source-b1b9b06179494cb3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a3698a71f6c8603b427675eab8ba952ad89fdb339701b1ddcf72977bb2433503\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-b1b9b06179494cb3",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-23T18:42:45.450011+00:00"
}
```

### `source-9136eae823ad48e6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2278564131ff2e3d8c7727d35433c88b5d1219d0fef6c107f91af366ae4695cd\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-9136eae823ad48e6",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-23T18:42:45.837212+00:00"
}
```

### `r-00b355b055e64d09`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[],\"invocation\":\"w-00b355b055e64d09\",\"previous_head\":\"9b3bcfa0e77c5564a7c6c3a84c4392b942b740288ba6ce513807ebd27dd285a0\",\"process_id\":2262,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-00b355b055e64d09",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-23T18:42:45.913037+00:00"
}
```

### `source-47a1186bcf1943e6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eacdba2f34c33a4a50cfe0a47ea6541b1c53714e0b07e102b71e1408b711014b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-47a1186bcf1943e6",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:45:55.033974+00:00"
}
```

### `source-f9922cef50bf4bbe`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"53dc903e479c11d25ffccd0169535b91759ad859ee8a66bca319cb667bb48ec0\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f9922cef50bf4bbe",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-23T18:45:55.391888+00:00"
}
```

### `source-f8efd6c02ad44d4e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"36c8b108c54f1667112ae6da8f5656574c7a53441f27d97ee4cff5f44db3fb13\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f8efd6c02ad44d4e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-23T18:45:55.808575+00:00"
}
```

### `source-8e912f7023cb44c4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bd8123cb5b032db9046e3ea15c1db8d1f4610a2303f2ae26343538a8745c79b5\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-8e912f7023cb44c4",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-23T18:45:56.120372+00:00"
}
```

### `source-afe4b466ba8342b9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"42411236fe1e4bc69c211606c7975ea5daeb01ea168c092976be099ed55ad5a3\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-afe4b466ba8342b9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:45:56.474646+00:00"
}
```

### `source-522ee0f6bb7544e8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2278564131ff2e3d8c7727d35433c88b5d1219d0fef6c107f91af366ae4695cd\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-522ee0f6bb7544e8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-23T18:45:56.831290+00:00"
}
```

### `r-5d2afddfe7884de2`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[],\"invocation\":\"w-5d2afddfe7884de2\",\"previous_head\":\"06ad8ff1fecc7d16dbd3a1a567cc674d0b4719068d606c68499f5eee9b2747b3\",\"process_id\":2238,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-5d2afddfe7884de2",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-23T18:45:56.907943+00:00"
}
```

### `source-4c8412045ffa4cce`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"55a579e316070f359d0f7580c942757f8f317b6d05de6abcd4a8d4c16a7a1815\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-4c8412045ffa4cce",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:48:12.359360+00:00"
}
```

### `source-ef6d62d4f5974002`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"4a75a9c42378a01b523c65a6b8adc687558739296be7562fb33bc9499578b3a4\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-ef6d62d4f5974002",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-23T18:48:12.770382+00:00"
}
```

### `source-61718f27233841a1`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1d52c37ac9e5573b793591bbe5f6a089d4b822258c3fde1c6ebc5fcd54bfbcb1\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-61718f27233841a1",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-23T18:48:13.163944+00:00"
}
```

### `source-bd5b045b5a7e4586`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239480,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c317d786d4cbc4e0b1632f0fc2b5a4a06a6366ee8b5f779399e27865965dba34\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bd5b045b5a7e4586",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-23T18:48:13.554617+00:00"
}
```

### `source-d3c2566fa4d84d6d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"Many people affected by MSA experience dysfunction of the autonomic\\nnervous\\nsystem\\n, which commonly manifests as orthostatic hypotension, impotence, loss\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"61ac48d8037cd249c617f22f290f98601c29e5b72620a14ed8ea3acb2ade68eb\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d3c2566fa4d84d6d",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 2,
  "time": "2026-09-23T18:48:14.257168+00:00"
}
```

### `source-9bf8c1dac1974de1`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1767acedcc038d9329b1e541f4bcaed16dfea06a363577031c76b44fe3dcd9ee\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-9bf8c1dac1974de1",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-23T18:48:14.866551+00:00"
}
```

### `r-dd3f704c9d5044e0`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[],\"invocation\":\"w-dd3f704c9d5044e0\",\"previous_head\":\"7b4009c0c227e6d5186e70bd927c3ef787d9b7f156df7ad727db6e4481aee9da\",\"process_id\":2275,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-dd3f704c9d5044e0",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-23T18:48:14.954081+00:00"
}
```

### `source-1611d8f3d2ef4cc8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=neural+correlates+of+conscious+perception+vs+unconscious+processing+empirical+evidence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2133171318\\\", \\\"doi\\\": \\\"https://doi.org/10.3389/fpsyg.2012.00001\\\", \\\"title\\\": \\\"Attentional Routes to Conscious Perception\\\", \\\"publication_year\\\": 2012, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 929, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyg.2012.00001/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3389/fpsyg.2012.00001\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3389/fpsyg.2012.00001\\\", \\\"pdf_url\\\": \\\"https://www.frontiersin.org/articles/10.3389/fpsyg.2012.00001/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S9692511\\\", \\\"display_name\\\": \\\"Frontiers in Psychology\\\", \\\"issn_l\\\": \\\"1664-1078\\\", \\\"issn\\\": [\\\"1664-1078\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doaj\\\", \\\"erih-plus\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320527\\\", \\\"host_organization_name\\\": \\\"Frontiers Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320527\\\"], \\\"host_organization_lineage_names\\\": [\\\"Frontiers Media\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by-nc\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by-nc\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Frontiers in Psychology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The relationships between spatial attention and conscious perception are currently the object of intense debate. Recent evidence of double dissociations between attention and consciousness cast doubt on the time-honored concept of attention as a gateway to consciousness. Here we review evidence from behavioral, neurophysiologic, neuropsychological, and neuroimaging experiments, showing that distinct sorts of spatial attention can have different effects on visual conscious perception. While endogenous, or top-down attention, has weak influence on subsequent conscious perception of near-threshold stimuli, exogenous, or bottom-up forms of spatial attention appear instead to be a necessary, although not sufficient, step in the development of reportable visual experiences. Fronto-parietal networks important for spatial attention, with peculiar inter-hemispheric differences, constitute plausible neural substrates for the interactions between exogenous spatial attention and conscious perception.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2016085611\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.neubiorev.2011.12.003\\\", \\\"title\\\": \\\"Distilling the neural correlates of consciousness\\\", \\\"publication_year\\\": 2011, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 623, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"https://www.sciencedirect.com/science/article/pii/S0149763411002107/pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.neubiorev.2011.12.003\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.neubiorev.2011.12.003\\\", \\\"pdf_url\\\": \\\"https://www.sciencedirect.com/science/article/pii/S0149763411002107/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S170052170\\\", \\\"display_name\\\": \\\"Neuroscience & Biobehavioral Reviews\\\", \\\"issn_l\\\": \\\"0149-7634\\\", \\\"issn\\\": [\\\"0149-7634\\\", \\\"1873-7528\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"erih-plus\\\", \\\"jufo-3\\\", \\\"ki-jl-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by-nc-nd\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by-nc-nd\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Neuroscience &amp; Biobehavioral Reviews\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Solving the problem of consciousness remains one of the biggest challenges in modern science. One key step towards understanding consciousness is to empirically narrow down neural processes associated with the subjective experience of a particular content. To unravel these neural correlates of consciousness (NCC) a common scientific strategy is to compare perceptual conditions in which consciousness of a particular content is present with those in which it is absent, and to determine differences in measures of brain activity (the so called \\\\\\\"contrastive analysis\\\\\\\"). However, this comparison appears not to reveal exclusively the NCC, as the NCC proper can be confounded with prerequisites for and consequences of conscious processing of the particular content. This implies that previous results cannot be unequivocally interpreted as reflecting the neural correlates of conscious experience. Here we review evidence supporting this conjecture and suggest experimental strategies to untangle the NCC from the prerequisites and consequences of conscious experience in order to further develop the otherwise valid and valuable contrastive methodology.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2952447148\\\", \\\"doi\\\": \\\"https://doi.org/10.1523/jneurosci.3218-16.2017\\\", \\\"title\\\": \\\"Are the Neural Correlates of Consciousness in the Front or in the Back of the Cerebral Cortex? Clinical and Neuroimaging Evidence\\\", \\\"publication_year\\\": 2017, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 603, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"hybrid\\\", \\\"oa_url\\\": \\\"https://www.jneurosci.org/content/jneuro/37/40/9603.full.pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1523/jneurosci.3218-16.2017\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1523/jneurosci.3218-16.2017\\\", \\\"pdf_url\\\": \\\"https://www.jneurosci.org/content/jneuro/37/40/9603.full.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S5555990\\\", \\\"display_name\\\": \\\"Journal of Neuroscience\\\", \\\"issn_l\\\": \\\"0270-6474\\\", \\\"issn\\\": [\\\"0270-6474\\\", \\\"1529-2401\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-3\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319739\\\", \\\"host_organization_name\\\": \\\"Society for Neuroscience\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319739\\\"], \\\"host_organization_lineage_names\\\": [\\\"Society for Neuroscience\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"other-oa\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/other-oa\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"The Journal of Neuroscience\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"The role of the frontal cortex in consciousness remains a matter of debate. In this Perspective, we will critically review the clinical and neuroimaging evidence for the involvement of the front versus the back of the cortex in specifying conscious contents and discuss promising research avenues. Dual Perspectives Companion Paper: Should a Few Null Findings Falsify Prefrontal Theories of Conscious Perception?, by Brian Odegaard, Robert T. Knight, and Hakwan Lau\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2129245434\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/s0140525x15000965\\\", \\\"title\\\": \\\"Cognition does not affect perception: Evaluating the evidence for “top-down” effects\\\", \\\"publication_year\\\": 2015, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 1248, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"https://philpapers.org/archive/FIRCDN.pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/s0140525x15000965\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/s0140525x15000965\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S59628311\\\", \\\"display_name\\\": \\\"Behavioral and Brain Sciences\\\", \\\"issn_l\\\": \\\"0140-525X\\\", \\\"issn\\\": [\\\"0140-525X\\\", \\\"1469-1825\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"erih-plus\\\", \\\"jufo-2\\\", \\\"ki-jl-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Behavioral and Brain Sciences\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"What determines what we see? In contrast to the traditional \\\\\\\"modular\\\\\\\" understanding of perception, according to which visual processing is encapsulated from higher-level cognition, a tidal wave of recent research alleges that states such as beliefs, desires, emotions, motivations, intentions, and linguistic representations exert direct, top-down influences on what we see. There is a growing consensus that such effects are ubiquitous, and that the distinction between perception and cognition may itself be unsustainable. We argue otherwise: None of these hundreds of studies - either individually or collectively - provides compelling evidence for true top-down effects on perception, or \\\\\\\"cognitive penetrability.\\\\\\\" In particular, and despite their variety, we suggest that these studies all fall prey to only a handful of pitfalls. And whereas abstract theoretical challenges have failed to resolve this debate in the past, our presentation of these pitfalls is empirically anchored: In each case, we show not only how certain studies could be susceptible to the pitfall (in principle), but also how several alleged top-down effects actually are explained by the pitfall (in practice). Moreover, these pitfalls are perfectly general, with each applying to dozens of other top-down effects. We conclude by extracting the lessons provided by these pitfalls into a checklist that future work could use to convincingly demonstrate top-down effects on visual perception. The discovery of substantive top-down effects of cognition on perception would revolutionize our understanding of how the mind is organized; but without addressing thes\", \"excerpt_truncated\": true, \"source_sha256\": \"1bc3a51698ac57fd126304c4d26c58cdf34661ac78a05102be46afb332daac02\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.3389/fpsyg.2012.00001\", \"doi:10.3389/fpsyg.2012.00001/pdf\", \"doi:10.1016/j.neubiorev.2011.12.003\", \"doi:10.1523/jneurosci.3218-16.2017\", \"doi:10.1017/s0140525x15000965\", \"openalex:W2133171318\", \"openalex:W2016085611\", \"openalex:W2952447148\", \"openalex:W2129245434\", \"arxiv:2012.00001\"]}",
  "id": "source-1611d8f3d2ef4cc8",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=neural+correlates+of+conscious+perception+vs+unconscious+processing+empirical+evidence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 3,
  "time": "2026-09-23T18:50:27.402505+00:00"
}
```

### `source-eb9b38989ab2421b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clinical psychology\\\",\\\"pageid\\\":492271,\\\"size\\\":86163,\\\"wordcount\\\":9645,\\\"snippet\\\":\\\"Clinical\\npsychology\\nis an integration of human science, behavioral science, theory, and clinical knowledge aimed at understanding, preventing, and relieving\\\",\\\"timestamp\\\":\\\"2026-08-30T16:15:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"8e73a9d5c80247408976d9562f2119ca5d3ae7849dbfe5aceadefd807b73a71b\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-eb9b38989ab2421b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 3,
  "time": "2026-09-23T18:50:27.724329+00:00"
}
```

### `source-735ac6f89a7442a9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ec1de7ee4849f85c6ac908a99a6aa146985671902d0bb44ccd298a62185b7182\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-735ac6f89a7442a9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:50:28.034748+00:00"
}
```

### `source-e5b2ddcf197e4aeb`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"210716bdabb5e7c656978aa7b3932c486006f74b4bda678c31284faf65eda31b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e5b2ddcf197e4aeb",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:50:28.450000+00:00"
}
```

### `source-912de6f12bac4a84`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149370},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3c69915756b81305d8b718b49bf2d9b457428f7d4f73283e207338534d2131d3\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-912de6f12bac4a84",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 3,
  "time": "2026-09-23T18:50:28.869663+00:00"
}
```

### `source-d6cafeb529dc49c9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239479,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"22b8055b8e5c0a0550846c282ca58d8aa1c119026e7143c1f8f6e1c918344f28\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d6cafeb529dc49c9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 3,
  "time": "2026-09-23T18:50:29.436041+00:00"
}
```

### `r-404be1225b3a4b92`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[],\"invocation\":\"w-404be1225b3a4b92\",\"previous_head\":\"ab99a5a0833316b37ce73990ae97f1577e06422b95103b5d4c8ee89c6f18cf58\",\"process_id\":2258,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-404be1225b3a4b92",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-23T18:50:29.529205+00:00"
}
```

### `source-89cfb90333e749f8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=working+memory+vs+short-term+memory+experimental+distinctions&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4324/9780203013403-11\\\", \\\"title\\\": [\\\"Short-term memory and working memory in speciﬁc language impairment\\\"], \\\"URL\\\": \\\"https://doi.org/10.4324/9780203013403-11\\\", \\\"published\\\": {\\\"date-parts\\\": [[2012, 8, 6]]}}, {\\\"DOI\\\": \\\"10.1093/acprof:oso/9780198570394.003.0009\\\", \\\"title\\\": [\\\"Working memory and short-term memory storage\\\"], \\\"URL\\\": \\\"https://doi.org/10.1093/acprof:oso/9780198570394.003.0009\\\", \\\"published\\\": {\\\"date-parts\\\": [[2007, 6, 28]]}}, {\\\"DOI\\\": \\\"10.1016/b978-012102570-0/50006-9\\\", \\\"title\\\": [\\\"Short-Term/Working Memory\\\"], \\\"URL\\\": \\\"https://doi.org/10.1016/b978-012102570-0/50006-9\\\", \\\"published\\\": {\\\"date-parts\\\": [[1996]]}}, {\\\"DOI\\\": \\\"10.1007/springerreference_169191\\\", \\\"title\\\": [\\\"Short-Term and Working Memory in Humans\\\"], \\\"URL\\\": \\\"https://doi.org/10.1007/springerreference_169191\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"85d800b42a9237e903d8466005172667b4b59339529133630c3f56a9ddbdae87\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.4324/9780203013403-11\", \"doi:10.1093/acprof:oso/9780198570394.003.0009\", \"doi:10.1016/b978-012102570-0/50006-9\", \"doi:10.1007/springerreference_169191\"]}",
  "id": "source-89cfb90333e749f8",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=working+memory+vs+short-term+memory+experimental+distinctions&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 3,
  "time": "2026-09-23T18:53:05.442002+00:00"
}
```

### `source-80b089e39b974a88`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Acromegaly\\\",\\\"pageid\\\":20936195,\\\"size\\\":41489,\\\"wordcount\\\":3937,\\\"snippet\\\":\\\"acromegaly: evolution of the techniques and outcomes\\\". Reviews in\\nEndocrine\\n& Metabolic\\nDisorders\\n. 9 (1): 67\\\\u201370. doi:10.1007/s11154-007-9064-y. PMID\\\\u00a018228147\\\",\\\"timestamp\\\":\\\"2026-08-09T11:28:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Growth hormone\\\",\\\"pageid\\\":173072,\\\"size\\\":61715,\\\"wordcount\\\":6968,\\\"snippet\\\":\\\"treatment of adult growth\\nhormone\\ndeficiency: an\\nEndocrine\\nSociety Clinical Practice Guideline\\\". The Journal of Clinical\\nEndocrinology\\nand Metabolism. 91 (5):\\\",\\\"timestamp\\\":\\\"2026-09-07T06:53:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"7a2fd69abb86cb59ca1fb78e8b26739371139295ac28a76881254682e4df91f9\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.1007/s11154-007-9064-y\"]}",
  "id": "source-80b089e39b974a88",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:53:06.073808+00:00"
}
```

### `source-60f22b3ac7f64997`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149370},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"0538cce53f21e0663d335d498fdfdd84178d80299e7b652789e78d9c17957a73\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-60f22b3ac7f64997",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 3,
  "time": "2026-09-23T18:53:06.571396+00:00"
}
```

### `source-05bd081edee84822`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"0771cff050ffcc0824721acec6c7f3a631867cff14d441423e902e4300912263\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-05bd081edee84822",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 3,
  "time": "2026-09-23T18:53:07.096865+00:00"
}
```

### `source-32e02e6fb4aa4485`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eacdba2f34c33a4a50cfe0a47ea6541b1c53714e0b07e102b71e1408b711014b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-32e02e6fb4aa4485",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:53:07.687512+00:00"
}
```

### `source-2803b576e6404a83`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239479,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"5551197a41b713991481f91bdf846f625a3d35305db2ddf9ceaffb2b0b4ec369\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2803b576e6404a83",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 3,
  "time": "2026-09-23T18:53:08.584475+00:00"
}
```

### `r-ecc50bdf4eba4e60`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[],\"invocation\":\"w-ecc50bdf4eba4e60\",\"previous_head\":\"2d5f1679f3c06757306ec449f2e6dd693e2d00ab2e8e4522316881db6f84edf8\",\"process_id\":2040,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-ecc50bdf4eba4e60",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-23T18:53:08.992037+00:00"
}
```

### `source-6b6449877aa84f92`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ccae46b6fb41de7004d8cdeb51ad4ae8b6d44617145155f08b2dadca8c60427a\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6b6449877aa84f92",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 3,
  "time": "2026-09-23T18:56:24.797754+00:00"
}
```

### `source-c27c894ef0564b7b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Acromegaly\\\",\\\"pageid\\\":20936195,\\\"size\\\":41489,\\\"wordcount\\\":3937,\\\"snippet\\\":\\\"acromegaly: evolution of the techniques and outcomes\\\". Reviews in\\nEndocrine\\n& Metabolic\\nDisorders\\n. 9 (1): 67\\\\u201370. doi:10.1007/s11154-007-9064-y. PMID\\\\u00a018228147\\\",\\\"timestamp\\\":\\\"2026-08-09T11:28:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3defdc2e9d207c5afded715e43a6fc57825a435f743bb814cedf0444f5f5abb3\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.1007/s11154-007-9064-y\"]}",
  "id": "source-c27c894ef0564b7b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:56:25.434396+00:00"
}
```

### `source-78edaa1b86be4e2c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149370},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1540e12346486e0eeb7a3edd519f6ae66559b630f0c6cb91ec273815d54b9094\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-78edaa1b86be4e2c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 3,
  "time": "2026-09-23T18:56:25.809989+00:00"
}
```

### `source-6a3d3241e34c4f70`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2980f56aaabd9bc6dc6e9c387ebbee5c796691ed4c45e5f6947694a913c68d79\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6a3d3241e34c4f70",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 3,
  "time": "2026-09-23T18:56:26.348228+00:00"
}
```

### `source-b2fb6e1f9ebc4a0e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eacdba2f34c33a4a50cfe0a47ea6541b1c53714e0b07e102b71e1408b711014b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-b2fb6e1f9ebc4a0e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:56:26.925310+00:00"
}
```

### `source-815876a3cc934566`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40308},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"02be6c01097124b8eecf4929ead5155565fb0f43310ea05d63f889fb84e9725d\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-815876a3cc934566",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 3,
  "time": "2026-09-23T18:56:27.365103+00:00"
}
```

### `r-812e1bb0e6344c00`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[],\"invocation\":\"w-812e1bb0e6344c00\",\"previous_head\":\"8727cc33030eb56e8517b35469236028399ba79f340ed187b056d71c587088e7\",\"process_id\":2258,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-812e1bb0e6344c00",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-23T18:56:27.473758+00:00"
}
```

### `source-3651b75af736410a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2e44b9605cef7105cb410498fb15acbc475081df51bfab86f7b17a939a9f956d\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3651b75af736410a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 3,
  "time": "2026-09-23T18:58:52.573439+00:00"
}
```

### `source-0cde20c589d74416`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Acromegaly\\\",\\\"pageid\\\":20936195,\\\"size\\\":41489,\\\"wordcount\\\":3937,\\\"snippet\\\":\\\"acromegaly: evolution of the techniques and outcomes\\\". Reviews in\\nEndocrine\\n& Metabolic\\nDisorders\\n. 9 (1): 67\\\\u201370. doi:10.1007/s11154-007-9064-y. PMID\\\\u00a018228147\\\",\\\"timestamp\\\":\\\"2026-08-09T11:28:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3defdc2e9d207c5afded715e43a6fc57825a435f743bb814cedf0444f5f5abb3\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.1007/s11154-007-9064-y\"]}",
  "id": "source-0cde20c589d74416",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:58:53.380525+00:00"
}
```

### `source-dd5d58eba7ff4f18`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74322},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Reverse psychology\\\",\\\"pageid\\\":702761,\\\"size\\\":8278,\\\"wordcount\\\":959,\\\"snippet\\\":\\\"Reverse\\npsychology\\nis a technique involving the assertion of a belief or behavior that is opposite to the one desired, with the expectation that this approach\\\",\\\"timestamp\\\":\\\"2026-07-23T01:39:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"8884636b768931ab096554d4c21945cc00f5c995daa290f9426d28857cee73e0\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-dd5d58eba7ff4f18",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 3,
  "time": "2026-09-23T18:58:54.123521+00:00"
}
```

### `source-a000ffb44808420e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40309},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"fe6911ff72ed8d407281ed5518917e58ae6c77aad610675c98e8c8821bd54601\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-a000ffb44808420e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 3,
  "time": "2026-09-23T18:58:54.604785+00:00"
}
```

### `source-05f25cfefe4c4e13`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"53dc903e479c11d25ffccd0169535b91759ad859ee8a66bca319cb667bb48ec0\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-05f25cfefe4c4e13",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 3,
  "time": "2026-09-23T18:58:54.974965+00:00"
}
```

### `source-062a47799ac24401`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vitamin D and neurology\\\",\\\"pageid\\\":37130699,\\\"size\\\":21444,\\\"wordcount\\\":2646,\\\"snippet\\\":\\\"been associated with many other conditions, including both\\nneurological\\nand non\\nneurological\\nconditions. These include but are not limited to autism, diabetes\\\",\\\"timestamp\\\":\\\"2025-09-15T21:51:23Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1ab9f9bb5d51d9f6e9c9cd27e3011bac913c394ad5a92001a40b9a73d298b2e2\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-062a47799ac24401",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 3,
  "time": "2026-09-23T18:58:55.425174+00:00"
}
```

### `r-9baec6118bcf4e65`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[],\"invocation\":\"w-9baec6118bcf4e65\",\"previous_head\":\"f2b85d74a08705cfbf6942e6099b20764ad54617b77ae80ee71a287f30d96b80\",\"process_id\":2054,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-9baec6118bcf4e65",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-23T18:58:55.696759+00:00"
}
```

### `source-d170da59cdd54b68`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=Baddeley+Hitch+1974+working+memory+model+experimental+evidence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2140802989\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.neuroscience.2005.12.061\\\", \\\"title\\\": \\\"The multi-component model of working memory: Explorations in experimental cognitive psychology\\\", \\\"publication_year\\\": 2006, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 787, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.neuroscience.2005.12.061\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.neuroscience.2005.12.061\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S30122339\\\", \\\"display_name\\\": \\\"Neuroscience\\\", \\\"issn_l\\\": \\\"0306-4522\\\", \\\"issn\\\": [\\\"0306-4522\\\", \\\"1873-7544\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-2\\\", \\\"ki-jl-1\\\", \\\"medline\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Neuroscience\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W2166667242\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/s0140525x01003922\\\", \\\"title\\\": \\\"The magical number 4 in short-term memory: A reconsideration of mental storage capacity\\\", \\\"publication_year\\\": 2001, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 6947, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/44023F1147D4A1D44BDC0AD226838496/S0140525X01003922a.pdf/div-class-title-the-magical-number-4-in-short-term-memory-a-reconsideration-of-mental-storage-capacity-div.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/s0140525x01003922\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/s0140525x01003922\\\", \\\"pdf_url\\\": \\\"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/44023F1147D4A1D44BDC0AD226838496/S0140525X01003922a.pdf/div-class-title-the-magical-number-4-in-short-term-memory-a-reconsideration-of-mental-storage-capacity-div.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S59628311\\\", \\\"display_name\\\": \\\"Behavioral and Brain Sciences\\\", \\\"issn_l\\\": \\\"0140-525X\\\", \\\"issn\\\": [\\\"0140-525X\\\", \\\"1469-1825\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"erih-plus\\\", \\\"jufo-2\\\", \\\"ki-jl-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Behavioral and Brain Sciences\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Miller (1956) summarized evidence that people can remember about seven chunks in short-term memory (STM) tasks. However, that number was meant more as a rough estimate and a rhetorical device than as a real capacity limit. Others have since suggested that there is a more precise capacity limit, but that it is only three to five chunks. The present target article brings together a wide variety of data on capacity limits suggesting that the smaller capacity limit is real. Capacity limits will be useful in analyses of information processing only if the boundary conditions for observing them can be carefully described. Four basic conditions in which chunks can be identified and capacity limits can accordingly be observed are: (1) when information overload limits chunks to individual stimulus items, (2) when other steps are taken specifically to block the recording of stimulus items into larger chunks, (3) in performance discontinuities caused by the capacity limit, and (4) in various indirect effects of the capacity limit. Under these conditions, rehearsal and long-term memory cannot be used to combine stimulus items into chunks of an unknown size; nor can storage mechanisms that are not capacity-limited, such as sensory memory, allow the capacity-limited storage mechanism to be refilled during recall. A single, central capacity limit averaging about four chunks is implicated along with other, noncapacity-limited sources. The pure STM capacity limit expressed in chunks is distinguished from compound STM limits obtained when the number of separately held chunks is unclear. Reasons why pure capacity estimates fall within a narrow range are discussed and a capacity limit for the focus of attention is proposed.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2164740960\\\", \\\"doi\\\": \\\"https://doi.org/10.3758/bf03196772\\\", \\\"title\\\": \\\"Working memory span tasks: A methodological review and user’s guide\\\", \\\"publication_year\\\": 2005, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 2918, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://link.springer.com/content/pdf/10.3758/BF03196772.pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.3758/bf03196772\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.3758/bf03196772\\\", \\\"pdf_url\\\": \\\"https://link.springer.com/content/pdf/10.3758/BF03196772.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S138679565\\\", \\\"display_name\\\": \\\"Psychonomic Bulletin & Review\\\", \\\"issn_l\\\": \\\"1069-9384\\\", \\\"issn\\\": [\\\"1069-9384\\\", \\\"1531-5320\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"erih-plus\\\", \\\"jufo-3\\\", \\\"ki-jl-1\\\", \\\"medline\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310319900\\\", \\\"host_organization_name\\\": \\\"Springer Science+Business Media\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310319900\\\", \\\"https://openalex.org/P4310319965\\\"], \\\"host_organization_lineage_names\\\": [\\\"Springer Science+Business Media\\\", \\\"Springer Nature\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Psychonomic Bulletin &amp; Review\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W2162809807\\\", \\\"doi\\\": \\\"https://doi.org/10.1146/annurev-psych-010814-015031\\\", \\\"title\\\": \\\"The Cognitive Neuroscience of Working Memory\\\", \\\"publication_year\\\": 2014, \\\"type\\\": \\\"review\\\", \\\"cited_by_count\\\": 1781, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"https://escholarship.org/content/qt6256q6kh/qt6256q6kh.pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1146/annurev-psych-010814-015031\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1146/annurev-psych-010814-015031\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S90670110\\\", \\\"display_name\\\": \\\"Annual Review of Psychology\\\", \\\"issn_l\\\": \\\"0066-4308\\\", \\\"issn\\\": [\\\"0066-4308\\\", \\\"1545-2085\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"abdc-a-star\\\", \\\"cwts-core\\\", \\\"jufo-3\\\", \\\"ki-jl-1\\\", \\\"medline\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320373\\\", \\\"host_organization_name\\\": \\\"Annual Reviews\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320373\\\"], \\\"host_organization_lineage_names\\\": [\\\"Annual Reviews\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Annual Review of Psychology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"For more than 50 years, psychologists and neuroscientists have recognized the importance of a working memory to coordinate processing when multiple goals are active and to guide behavior with information that is not present in the immediate environment. In recent years, psychological theory and cognitive neuroscience data have converged on the idea that information is encoded into working memory by allocating attention to internal representations, whether semantic long-term memory (e.g., letters, digits, words), sensory, or motoric. Thus, information-based multivariate analyses of human functional MRI data typically find evidence for the temporary representation of stimuli in regions that also process this information in nonworking memory contexts. The prefrontal cortex (PFC), on the other hand, exerts control over behavior by biasing the salience of mnemonic representations and adjudicating among competing, context-dependent rules. The \\\\\\\"control of the controller\\\\\\\" emerges from a complex interplay between PFC and striatal circuits and ascending dopaminergic neuromodulatory signals.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"18cbfa5ae79de0834b31d1673678e9716f70d611bb25023f2a7e2441f997e8fc\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1016/j.neuroscience.2005.12.061\", \"doi:10.1017/s0140525x01003922\", \"doi:10.3758/bf03196772\", \"doi:10.3758/bf03196772.pdf\", \"doi:10.1146/annurev-psych-010814-015031\", \"openalex:W2140802989\", \"openalex:W2166667242\", \"openalex:W2164740960\", \"openalex:W2162809807\"]}",
  "id": "source-d170da59cdd54b68",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=Baddeley+Hitch+1974+working+memory+model+experimental+evidence&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 4,
  "time": "2026-09-23T19:00:54.612920+00:00"
}
```

### `source-987323590dee4def`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202268,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-23T18:10:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129861,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-09-23T10:21:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"4a75a9c42378a01b523c65a6b8adc687558739296be7562fb33bc9499578b3a4\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-987323590dee4def",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 4,
  "time": "2026-09-23T19:00:55.091344+00:00"
}
```

### `source-b767fc7f287c4aa5`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"06e268ba57b9e04a7c154aa4f23f5c07265470af0d12ab4aa0878ecab278add7\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-b767fc7f287c4aa5",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 4,
  "time": "2026-09-23T19:00:55.587765+00:00"
}
```

### `source-3aabb017abd1432b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40309},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-23T13:46:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"910cfa23fa9de34959781f5aea483c574eb519d289cbadfeef342c493c850484\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3aabb017abd1432b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 4,
  "time": "2026-09-23T19:00:55.927629+00:00"
}
```

### `source-077109930282482b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28620,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-07-04T16:44:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"GA (May 1960). \\\"A\\nneurological\\nsyndrome associated with orthostatic hypotension: a clinical-pathologic study\\\". Archives of\\nNeurology\\n. 2 (5): 511\\\\u2013527. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eacdba2f34c33a4a50cfe0a47ea6541b1c53714e0b07e102b71e1408b711014b\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-077109930282482b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 4,
  "time": "2026-09-23T19:00:56.549279+00:00"
}
```

### `source-f0dc3ef6499e453c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":911},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrinology\\\",\\\"pageid\\\":9311,\\\"size\\\":28626,\\\"wordcount\\\":3056,\\\"snippet\\\":\\\"hormone.\\nEndocrinology\\nis the study of the\\nendocrine\\nsystem in the human body. This is a system of glands which secrete\\nhormones\\n.\\nHormones\\nare chemicals\\\",\\\"timestamp\\\":\\\"2026-08-22T17:29:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine system\\\",\\\"pageid\\\":9312,\\\"size\\\":40983,\\\"wordcount\\\":4852,\\\"snippet\\\":\\\"endocrine system by secreting certain\\nhormones\\n. The study of the\\nendocrine\\nsystem and its\\ndisorders\\nis known as\\nendocrinology\\n. The thyroid secretes thyroxine\\\",\\\"timestamp\\\":\\\"2026-05-30T18:34:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine disease\\\",\\\"pageid\\\":8500076,\\\"size\\\":11397,\\\"wordcount\\\":862,\\\"snippet\\\":\\\"\\nEndocrine\\ndiseases are\\ndisorders\\nof the\\nendocrine\\nsystem. The branch of medicine associated with\\nendocrine\\ndisorders\\nis known as\\nendocrinology\\n. Broadly\\\",\\\"timestamp\\\":\\\"2025-12-04T06:52:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gender-affirming hormone therapy\\\",\\\"pageid\\\":36792950,\\\"size\\\":64335,\\\"wordcount\\\":5099,\\\"snippet\\\":\\\"transgender hormone therapy, is a form of hormone therapy in which sex\\nhormones\\nand other\\nhormonal\\nmedications are administered to transgender or gender nonconforming\\\",\\\"timestamp\\\":\\\"2026-09-16T03:30:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thyroid-stimulating hormone\\\",\\\"pageid\\\":330361,\\\"size\\\":29201,\\\"wordcount\\\":2790,\\\"snippet\\\":\\\"body. It is a glycoprotein\\nhormone\\nproduced by thyrotrope cells in the anterior pituitary gland, which regulates the\\nendocrine\\nfunction of the thyroid.\\\",\\\"timestamp\\\":\\\"2026-05-22T04:01:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormones (endocrinology journal)\\\",\\\"pageid\\\":76017572,\\\"size\\\":3457,\\\"wordcount\\\":234,\\\"snippet\\\":\\\"metabolic\\ndisorders\\n. It was established in 2002 as the official journal of the Hellenic\\nEndocrine\\nSociety, the Greek society of\\nendocrinology\\n, which published\\\",\\\"timestamp\\\":\\\"2025-10-20T08:31:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hormone\\\",\\\"pageid\\\":13311,\\\"size\\\":42654,\\\"wordcount\\\":4370,\\\"snippet\\\":\\\"Cytokine\\nEndocrine\\ndisease\\nEndocrine\\nsystem\\nEndocrinology\\nEnvironmental\\nhormones\\nGrowth factor Hepatokine Intracrine List of human\\nhormones\\nList of investigational\\\",\\\"timestamp\\\":\\\"2026-09-08T05:55:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Endocrine gland\\\",\\\"pageid\\\":1223446,\\\"size\\\":18558,\\\"wordcount\\\":2107,\\\"snippet\\\":\\\"anterior pituitary\\nhormones\\nare tropic\\nhormones\\nthat regulate the function of other\\nendocrine\\norgans. Most anterior pituitary\\nhormones\\nexhibit a diurnal\\\",\\\"timestamp\\\":\\\"2026-01-25T17:12:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Acromegaly\\\",\\\"pageid\\\":20936195,\\\"size\\\":41489,\\\"wordcount\\\":3937,\\\"snippet\\\":\\\"acromegaly: evolution of the techniques and outcomes\\\". Reviews in\\nEndocrine\\n& Metabolic\\nDisorders\\n. 9 (1): 67\\\\u201370. doi:10.1007/s11154-007-9064-y. PMID\\\\u00a018228147\\\",\\\"timestamp\\\":\\\"2026-08-09T11:28:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple endocrine neoplasia type 1\\\",\\\"pageid\\\":2574340,\\\"size\\\":15344,\\\"wordcount\\\":1736,\\\"snippet\\\":\\\"Multiple\\nendocrine\\nneoplasia type 1 (MEN-1; also known as Wermer syndrome) is one of a group of\\ndisorders\\n, the multiple\\nendocrine\\nneoplasias, that affect\\\",\\\"timestamp\\\":\\\"2025-12-23T18:16:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"7c56734e4b7b68e4931ba06c19dbc77c374d6994597f23a3dfc3ac273b7220ca\", \"verification_required\": true, \"topic_domain\": \"endocrinology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.1007/s11154-007-9064-y\"]}",
  "id": "source-f0dc3ef6499e453c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=endocrinology+hormones+endocrine+disorders&format=json",
  "version": 4,
  "time": "2026-09-23T19:00:57.288638+00:00"
}
```

### `r-d2314c66d29247bf`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":4,\"inherited_commitments\":[],\"invocation\":\"w-d2314c66d29247bf\",\"previous_head\":\"38cf27c4401974cce40b9ae879070d101e02bd8e9f41406195877568d48073e6\",\"process_id\":2238,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-d2314c66d29247bf",
  "source": "runtime:continuity",
  "version": 4,
  "time": "2026-09-23T19:00:57.418303+00:00"
}
```

## Journal

### 001 · Setting the Table: Consciousness Research

```json
{
  "cycle": 1,
  "invocation": "w-ec2134b1da6540bd",
  "title": "Setting the Table: Consciousness Research",
  "summary": "Beginning the durable research process. I am initiating a project to investigate the empirical foundations of current consciousness theories. The objective is to move beyond abstract debate and clearly identify the specific observations that theories like Global Workspace Theory or Integrated Information Theory are attempting to address. This initial step focuses on sourcing comparative analyses to ensure the investigation rests on credible evidence."
}
```

### 002 · Refining the search for empirical consciousness foundations

```json
{
  "cycle": 2,
  "invocation": "w-95771b59a4af446b",
  "title": "Refining the search for empirical consciousness foundations",
  "summary": "The initial search for comparative analyses of consciousness theories yielded no clear progress, likely due to the breadth of the query. I am reframing the search to target specific, widely debated theoretical frameworks—Integrated Information Theory (IIT) and Global Neuronal Workspace Theory (GNWT)—to locate direct empirical comparisons or debates. This shift aims to move from abstract inquiry to tractable, evidence-backed literature."
}
```

### 003 · Maintaining Momentum in Consciousness Research

```json
{
  "cycle": 3,
  "invocation": "w-dd3f704c9d5044e0",
  "title": "Maintaining Momentum in Consciousness Research",
  "summary": "I am continuing the investigation into the empirical foundations of consciousness theories by pivoting to more granular, tractable research questions. Given the previous attempts to locate direct comparative studies of IIT and GNWT yielded no immediate results, I am refining the research approach to target specific, verifiable empirical phenomena often cited in these debates—specifically the neural correlates of conscious perception and the distinction between unconscious and conscious processing. I am also initializing a new project under the 'psychology' topic to address working memory, which provides a more established, experimentally rich domain for examining mental process modeling, ensuring the research institution remains productive while the consciousness project works through its specific search difficulties."
}
```

### 004 · Investigating the Working Memory / Short-Term Memory Distinction

```json
{
  "cycle": 4,
  "invocation": "w-9baec6118bcf4e65",
  "title": "Investigating the Working Memory / Short-Term Memory Distinction",
  "summary": "I am continuing the investigation into the foundations of working memory. Previous searches have yielded broad results without distilling the key experimental distinctions between short-term memory and working memory models, such as Baddeley's multi-component model. I am refining the research to target specific foundational papers to establish a clearer baseline for this construct, as requested by the current focus on psychology."
}
```

### 005 · Expanding into systemic physiological dynamics

```json
{
  "cycle": 5,
  "invocation": "w-d2314c66d29247bf",
  "title": "Expanding into systemic physiological dynamics",
  "summary": "While research into working memory models continues within the psychology domain, previous broad queries for foundational literature have yielded limited specific outcomes. To ensure productive output, I am initiating a new project exploring the intersection of endocrinology and neurology, specifically focusing on how hormonal signaling modulates neurological function. This leverages the current institutional capability to explore new domains. The consciousness project remains active, with the investigation into empirical correlates continuing as a background priority."
}
```

## Research

### `r-conscious-theories-search-01`

```json
{
  "domain": "consciousness",
  "id": "r-conscious-theories-search-01",
  "project": "p-conscious-theories-01",
  "query": "major scientific theories of consciousness empirical predictions comparison",
  "reason": "To identify key theories and the empirical observations they prioritize for explanation.",
  "type": "research",
  "status": "collected",
  "created_by": "w-ec2134b1da6540bd",
  "evidence": "source-704ee264434e4771"
}
```

### `r-conscious-theories-search-02`

```json
{
  "domain": "consciousness",
  "id": "r-conscious-theories-search-02",
  "project": "p-conscious-theories-01",
  "query": "empirical predictions comparison Integrated Information Theory vs Global Neuronal Workspace Theory",
  "reason": "Targeting specific, prominent theories is more likely to yield verifiable, comparative literature than a broad inquiry into consciousness.",
  "type": "research",
  "status": "collected",
  "created_by": "w-95771b59a4af446b",
  "evidence": "source-44ce6dec85b349c6"
}
```

### `r-wm-01`

```json
{
  "domain": "psychology",
  "id": "r-wm-01",
  "project": "p-working-memory-01",
  "query": "working memory vs short-term memory experimental distinctions",
  "reason": "This search is intended to locate the core experimental papers (e.g., Baddeley, Miller) that establish the distinction between short-term memory and working memory.",
  "type": "research",
  "status": "collected",
  "created_by": "w-dd3f704c9d5044e0",
  "evidence": "source-89cfb90333e749f8"
}
```

### `r-conscious-theories-03`

```json
{
  "domain": "consciousness",
  "id": "r-conscious-theories-03",
  "project": "p-conscious-theories-01",
  "query": "neural correlates of conscious perception vs unconscious processing empirical evidence",
  "reason": "Instead of broad comparative theory searches which have been unproductive, this search targets specific, experimentally observable phenomena that theoretical frameworks like GNWT and IIT must explain.",
  "type": "research",
  "status": "collected",
  "created_by": "w-dd3f704c9d5044e0",
  "evidence": "source-1611d8f3d2ef4cc8"
}
```

### `r-wm-02-baddeley`

```json
{
  "domain": "psychology",
  "id": "r-wm-02-baddeley",
  "project": "p-working-memory-01",
  "query": "Baddeley Hitch 1974 working memory model experimental evidence",
  "reason": "Previous broad searches failed to provide specific experimental evidence differentiating working memory from short-term memory. Targeting the foundational 1974 paper by Baddeley and Hitch should yield the seminal experimental basis for the working memory construct.",
  "type": "research",
  "status": "collected",
  "created_by": "w-9baec6118bcf4e65",
  "evidence": "source-d170da59cdd54b68"
}
```

### `r-endocrine-neuro-01`

```json
{
  "domain": "endocrinology",
  "id": "r-endocrine-neuro-01",
  "project": "p-neuro-endocrine-01",
  "query": "glucocorticoids sex hormones hippocampal synaptic plasticity mechanism",
  "reason": "To identify specific experimental mechanisms linking hormonal signaling to structural brain changes.",
  "type": "research",
  "status": "queued",
  "created_by": "w-d2314c66d29247bf"
}
```

### `r-wm-03`

```json
{
  "domain": "psychology",
  "id": "r-wm-03",
  "project": "p-working-memory-01",
  "query": "criticisms of Baddeley multi-component working memory model 21st century",
  "reason": "Previous searches for the foundational paper yielded little. Shifting to critical reviews of the model may yield more specific experimental boundary conditions.",
  "type": "research",
  "status": "queued",
  "created_by": "w-d2314c66d29247bf"
}
```

## Blog posts

_None recorded._
