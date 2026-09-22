# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 2  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `7f93217c1b725d99d779d3e9f455fe95475b0513f2ab2fee5e5456560b11aadd`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

### `com-001`

```json
{
  "due_cycle": 3,
  "id": "com-001",
  "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
  "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon",
  "type": "commit",
  "status": "open",
  "created_by": "w-ac9322a529144062",
  "created_version": 2
}
```

## Projects

### `it-001` · Foundations of Information Thermodynamics

```json
{
  "domain": "information_thermodynamics",
  "id": "it-001",
  "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
  "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
  "reason": "This topic is the current focus of the research directive and requires establishing a baseline of theoretical understanding.",
  "status": "active",
  "title": "Foundations of Information Thermodynamics",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-0ec3911b56d4467a"
}
```

## Acquisition capability

### `it-001`

```json
{
  "project": "it-001",
  "domain": "information_thermodynamics",
  "no_progress": 3,
  "routes": [
    "api.crossref.org:discovery",
    "api.openalex.org:discovery"
  ],
  "capability_blocked": false,
  "retry_after_version": null,
  "persistent_identifiers": [
    "doi:10.2139/ssrn.5982813",
    "doi:10.1088/1742-5468/2015/06/p06015",
    "doi:10.20944/preprints202506.0097.v1",
    "doi:10.1016/0039-3681(70)90010-5",
    "doi:10.1088/0957-4484/5/1/001",
    "doi:10.1088/0957-4484/5/1/001/pdf",
    "doi:10.1017/s0960129512000783",
    "doi:10.48550/arxiv.quant-ph/0411172",
    "openalex:W1987357549",
    "openalex:W2011301632",
    "openalex:W2134287462",
    "openalex:W2169642021"
  ],
  "last_receipt": {
    "evidence": "source-1a8e652505774fd3",
    "outcome": "no_progress",
    "persistent_identifiers": [
      "doi:10.1016/0039-3681(70)90010-5",
      "doi:10.1088/0957-4484/5/1/001",
      "doi:10.1088/0957-4484/5/1/001/pdf",
      "doi:10.1017/s0960129512000783",
      "doi:10.48550/arxiv.quant-ph/0411172",
      "openalex:W1987357549",
      "openalex:W2011301632",
      "openalex:W2134287462",
      "openalex:W2169642021"
    ],
    "research_id": "res-003",
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
{}
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
  "invocation": "w-ac9322a529144062",
  "restored_topics": [],
  "selected_topic": "information_thermodynamics",
  "terminal": "accepted",
  "triggered_topics": []
}
```

## Notebooks

_None recorded._

## Invocations

### `w-5720f1e969ec41de`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 10403,
    "delivered_request_chars": 32357,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 32357,
    "working_set_chars": 422
  },
  "id": "w-5720f1e969ec41de",
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
  "process_id": 2319,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "de661113b760fd42371dafc416d97cac5616b256377173b94142b7d7aec12205",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-5929557bed184f79"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-5929557bed184f79",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2d5a3108bbac4f52"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2d5a3108bbac4f52",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c4cb1d1e93304192"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c4cb1d1e93304192",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c45d70b71b2a459e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c45d70b71b2a459e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bc4b85956d2641bf"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bc4b85956d2641bf",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-009ba57f5ca5401a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-009ba57f5ca5401a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-5929557bed184f79",
      "source-2d5a3108bbac4f52",
      "source-c4cb1d1e93304192",
      "source-c45d70b71b2a459e",
      "source-bc4b85956d2641bf",
      "source-009ba57f5ca5401a"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 10403,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0406
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
  "time": "2026-09-22T15:13:40.095456+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1042,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 36560,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1823,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 36560,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 3270,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 36560,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-22T15:13:56.524745+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 3270,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 1042,
        "http_status": 503,
        "model": "gemini-3.8-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 36560,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 1823,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 36560,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 3270,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 36560,
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
    "request_payload_bytes": 36560,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-b01216df35934f5e`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 10151,
    "delivered_request_chars": 32105,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 32105,
    "working_set_chars": 422
  },
  "id": "w-b01216df35934f5e",
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
  "process_id": 2052,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "c51d91bd3b346999b2a233eff5de348be533e76aec712d75692f7169e88bb90f",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-5076cf616f0341e4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-5076cf616f0341e4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4344ba30d504471a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4344ba30d504471a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-8fa42ccbb409443b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8fa42ccbb409443b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6032bad82d8f49e9"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6032bad82d8f49e9",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3d4994727eb242b8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3d4994727eb242b8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cd9a9a757e7644f6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cd9a9a757e7644f6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-5076cf616f0341e4",
      "source-4344ba30d504471a",
      "source-8fa42ccbb409443b",
      "source-6032bad82d8f49e9",
      "source-3d4994727eb242b8",
      "source-cd9a9a757e7644f6"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 10151,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0416
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
  "time": "2026-09-22T15:19:53.866365+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 973,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 35756,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 681,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 35756,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 572,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 35756,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-22T15:20:06.509566+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 572,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 973,
        "http_status": 503,
        "model": "gemini-3.8-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 35756,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 681,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 35756,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 572,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 35756,
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
    "request_payload_bytes": 35756,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-f428af6ac2984cc0`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 10410,
    "delivered_request_chars": 32364,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 32364,
    "working_set_chars": 422
  },
  "id": "w-f428af6ac2984cc0",
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
  "process_id": 2244,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "bec2dd122a88732a62d7d4607d990e746a953b29bf01e1318e7899255ed320bd",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-11ecfab297f54ff5"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-11ecfab297f54ff5",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-928bb8b464934645"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-928bb8b464934645",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0067a1ae69a3409c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0067a1ae69a3409c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-03eb8e60560d4584"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-03eb8e60560d4584",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-905872ec4ec84c7b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-905872ec4ec84c7b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bd01375041314499"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bd01375041314499",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-11ecfab297f54ff5",
      "source-928bb8b464934645",
      "source-0067a1ae69a3409c",
      "source-03eb8e60560d4584",
      "source-905872ec4ec84c7b",
      "source-bd01375041314499"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 10410,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0405
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
  "time": "2026-09-22T15:24:31.091256+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 236,
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
            "retryDelay": "26s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 26.211922938s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 36587,
      "response_bytes_captured": 1363,
      "result": "daily_quota"
    },
    {
      "category": "timeout",
      "elapsed_ms": 60025,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 36587,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1157,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 36587,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-22T15:25:41.693862+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 1157,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "http",
        "elapsed_ms": 236,
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
              "retryDelay": "26s"
            }
          ],
          "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 26.211922938s.",
          "status": "RESOURCE_EXHAUSTED"
        },
        "request_payload_bytes": 36587,
        "response_bytes_captured": 1363,
        "result": "daily_quota"
      },
      {
        "category": "timeout",
        "elapsed_ms": 60025,
        "error_type": "TimeoutError",
        "http_status": null,
        "model": "gemini-3.5-flash",
        "request_payload_bytes": 36587,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 1157,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 36587,
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
    "request_payload_bytes": 36587,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-1a5e9125dd5f437f`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 10148,
    "delivered_request_chars": 32102,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 32102,
    "working_set_chars": 422
  },
  "id": "w-1a5e9125dd5f437f",
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
  "process_id": 2258,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "cf0fb17f33981e173200b93731001e22e2bd77871da48819a0bc17184d188ca0",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-dc01aca9bbfb4250"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-dc01aca9bbfb4250",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f51c3be2bfdd4daf"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f51c3be2bfdd4daf",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-5610ff2ad5334c94"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-5610ff2ad5334c94",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6e5506eff61542f6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6e5506eff61542f6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-5b2539e03e944c72"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-5b2539e03e944c72",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-8d089d1b0f744f8b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8d089d1b0f744f8b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-dc01aca9bbfb4250",
      "source-f51c3be2bfdd4daf",
      "source-5610ff2ad5334c94",
      "source-6e5506eff61542f6",
      "source-5b2539e03e944c72",
      "source-8d089d1b0f744f8b"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 10148,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0416
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
  "time": "2026-09-22T15:28:34.136848+00:00",
  "provider_attempts": [
    {
      "category": "timeout",
      "elapsed_ms": 60101,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 35743,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1473,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 35743,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 2,
  "finished": "2026-09-22T15:29:42.350500+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 1473,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "timeout",
        "elapsed_ms": 60101,
        "error_type": "TimeoutError",
        "http_status": null,
        "model": "gemini-3.5-flash",
        "request_payload_bytes": 35743,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 1473,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 35743,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 2,
    "request_payload_bytes": 35743,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-16e96f5bae6e4457`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 10403,
    "delivered_request_chars": 32357,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 32357,
    "working_set_chars": 422
  },
  "id": "w-16e96f5bae6e4457",
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
  "process_id": 2051,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "a4a1e2342b56f18cb7d3535ae73447e49d5d6b54132f796ddc911b1f6803f1ac",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-03e2ffeb53ad495b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-03e2ffeb53ad495b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-527af667d6094cdb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-527af667d6094cdb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-54e747da2a4d413a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-54e747da2a4d413a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-ed3577f74ece4b97"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-ed3577f74ece4b97",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-b5e8cedbd71a47a0"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-b5e8cedbd71a47a0",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-aa3197a133b64c30"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-aa3197a133b64c30",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-03e2ffeb53ad495b",
      "source-527af667d6094cdb",
      "source-54e747da2a4d413a",
      "source-ed3577f74ece4b97",
      "source-b5e8cedbd71a47a0",
      "source-aa3197a133b64c30"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 10403,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0406
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
  "time": "2026-09-22T15:30:25.121652+00:00",
  "provider_attempts": [
    {
      "category": "timeout",
      "elapsed_ms": 60084,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 36572,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 807,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 36572,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 2,
  "finished": "2026-09-22T15:31:33.614656+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 807,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "timeout",
        "elapsed_ms": 60084,
        "error_type": "TimeoutError",
        "http_status": null,
        "model": "gemini-3.5-flash",
        "request_payload_bytes": 36572,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 807,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 36572,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      }
    ],
    "provider_error": {
      "code": 503,
      "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
      "status": "UNAVAILABLE"
    },
    "provider_requests_sent": 2,
    "request_payload_bytes": 36572,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-0ec3911b56d4467a`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 10407,
    "delivered_request_chars": 32361,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 32361,
    "working_set_chars": 422
  },
  "id": "w-0ec3911b56d4467a",
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
  "process_id": 2240,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "64fdb053c58268c15bf554c2e1ec263dde9eb65feb802fa287280c0d3484f174",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-3a27b7c8dd8248c8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3a27b7c8dd8248c8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-73d0cad95a6a4cf8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-73d0cad95a6a4cf8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2caac7ce1f1a4450"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2caac7ce1f1a4450",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bb998eaa388b4c86"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bb998eaa388b4c86",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a8a00a7c6029446c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a8a00a7c6029446c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0a17d9c43e174670"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0a17d9c43e174670",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-3a27b7c8dd8248c8",
      "source-73d0cad95a6a4cf8",
      "source-2caac7ce1f1a4450",
      "source-bb998eaa388b4c86",
      "source-a8a00a7c6029446c",
      "source-0a17d9c43e174670"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 10407,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0405
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
  "time": "2026-09-22T15:35:47.619692+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 206,
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
            "retryDelay": "9s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 9.515967348s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 36584,
      "response_bytes_captured": 1361,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 16216,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 36584,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-22T15:36:10.577501+00:00",
  "reason": ""
}
```

### `w-5b044391187a49b2`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 12554,
    "delivered_request_chars": 34587,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 34587,
    "working_set_chars": 693
  },
  "id": "w-5b044391187a49b2",
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
        "id": "it-001",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2107,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "62dcf163337cf7f3a0eaf35a7d39a0fe72e7d569a4c78e529ea33002fd6a6acc",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-acc747317c1e45fc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-acc747317c1e45fc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-41dd87eb3f524d97"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-41dd87eb3f524d97",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-068d5f24ab504338"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-068d5f24ab504338",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6d74beafdc024eff"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6d74beafdc024eff",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-593d850fad7a45b9"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-593d850fad7a45b9",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6d7d3dae7dda4541"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6d7d3dae7dda4541",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-acc747317c1e45fc",
      "source-41dd87eb3f524d97",
      "source-068d5f24ab504338",
      "source-6d74beafdc024eff",
      "source-593d850fad7a45b9",
      "source-6d7d3dae7dda4541"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 12554,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 693,
    "working_to_delivered_ratio": 0.0552
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
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
  "time": "2026-09-22T15:39:41.019433+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 462,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 39047,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:39:46.158316+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 462,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 462,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 39047,
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
    "request_payload_bytes": 39047,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-76d3b27eb08e418c`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 12301,
    "delivered_request_chars": 34334,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 34334,
    "working_set_chars": 693
  },
  "id": "w-76d3b27eb08e418c",
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
        "id": "it-001",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2301,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "6c05fc32fb2a6b7ad51ed3fd6ecbee434c74ae0a8bea6bd190e4585c2ae99995",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-95a451bd629e4fbb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-95a451bd629e4fbb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-662d96af5e7f4e05"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-662d96af5e7f4e05",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-17692c00068f4034"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-17692c00068f4034",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-49b9db1016194c44"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-49b9db1016194c44",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d8daa7b9d76e4776"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d8daa7b9d76e4776",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-623e4988a6344654"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-623e4988a6344654",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-95a451bd629e4fbb",
      "source-662d96af5e7f4e05",
      "source-17692c00068f4034",
      "source-49b9db1016194c44",
      "source-d8daa7b9d76e4776",
      "source-623e4988a6344654"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 12301,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 693,
    "working_to_delivered_ratio": 0.0563
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
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
  "time": "2026-09-22T15:41:51.109507+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 374,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 38234,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:41:55.926926+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 374,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 374,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 38234,
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
    "request_payload_bytes": 38234,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-40869f26688a483e`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 12295,
    "delivered_request_chars": 34328,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 34328,
    "working_set_chars": 693
  },
  "id": "w-40869f26688a483e",
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
        "id": "it-001",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "quota_day": "2026-09-22",
  "request_hash": "fc92e5d57dcc2d364dd23db7df11cf5e1bfba387d4328858d8430e5eee200a7c",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-0370dd8cfa6b4e81"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0370dd8cfa6b4e81",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-24355458bfc74510"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-24355458bfc74510",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d6b00bc06439405a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d6b00bc06439405a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3bef228210934ecb"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3bef228210934ecb",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d68388e6c8c845aa"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d68388e6c8c845aa",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2a5a1c2c0ca044e7"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2a5a1c2c0ca044e7",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-0370dd8cfa6b4e81",
      "source-24355458bfc74510",
      "source-d6b00bc06439405a",
      "source-3bef228210934ecb",
      "source-d68388e6c8c845aa",
      "source-2a5a1c2c0ca044e7"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 12295,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 693,
    "working_to_delivered_ratio": 0.0564
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
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
  "time": "2026-09-22T15:43:50.206169+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 465,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 38216,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:43:55.698473+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 465,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 465,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 38216,
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
    "request_payload_bytes": 38216,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-ac9322a529144062`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 12555,
    "delivered_request_chars": 34588,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 34588,
    "working_set_chars": 693
  },
  "id": "w-ac9322a529144062",
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
        "id": "it-001",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2276,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "9e168de2ce80ea097e2ee7b803bcbf76a0bb4aaab5f5b44c599fa574f2b7f06c",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-321e2884dc494a5a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-321e2884dc494a5a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-495df910edbd4dc2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-495df910edbd4dc2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-80c490f4b71d423c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-80c490f4b71d423c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-00e7519b99cf4948"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-00e7519b99cf4948",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-7d642baea76844d8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7d642baea76844d8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-04b53731fee84454"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-04b53731fee84454",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-321e2884dc494a5a",
      "source-495df910edbd4dc2",
      "source-80c490f4b71d423c",
      "source-00e7519b99cf4948",
      "source-7d642baea76844d8",
      "source-04b53731fee84454"
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
  "squirrel": {
    "active": true,
    "cooldown_other_attempts": 3,
    "deferred_topics": [],
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 12555,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 6,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 693,
    "working_to_delivered_ratio": 0.0552
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
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
  "time": "2026-09-22T15:45:48.666110+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 10802,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 39070,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-22T15:46:04.073227+00:00",
  "reason": ""
}
```

### `w-212da6aff47b4602`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14321,
    "delivered_request_chars": 36434,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36434,
    "working_set_chars": 955
  },
  "id": "w-212da6aff47b4602",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 1
        },
        "title": "Foundations of Information Thermodynamics"
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
  "quota_day": "2026-09-22",
  "request_hash": "bdd24491188bad55b4639bb75d84d13fd3fa4bd871fc8ae1b0501fbd05b69a01",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-42595ad8c3a847b6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-42595ad8c3a847b6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-58256c38582545fe"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-58256c38582545fe",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d4241a06f2b647e4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d4241a06f2b647e4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-189a2cf0754b416c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-189a2cf0754b416c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2db1564a49d44934"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2db1564a49d44934",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-2917d46f7ea9493b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2917d46f7ea9493b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-42595ad8c3a847b6",
      "source-58256c38582545fe",
      "source-d4241a06f2b647e4",
      "source-189a2cf0754b416c",
      "source-2db1564a49d44934",
      "source-2917d46f7ea9493b"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 14321,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.0667
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T15:47:03.685398+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 15229,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41101,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:47:24.365208+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 15229,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 15229,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 41101,
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
    "request_payload_bytes": 41101,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-df51e03b28ce4a70`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14403,
    "delivered_request_chars": 36516,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36516,
    "working_set_chars": 955
  },
  "id": "w-df51e03b28ce4a70",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2242,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "164c132fedd49dad0967bf10f5392a6762a8c0512b293d212ccab3fbcdb238a3",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-1a8e652505774fd3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1a8e652505774fd3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-5a8600e5ee8b4499"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-5a8600e5ee8b4499",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a40f94f6bcf94fa9"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a40f94f6bcf94fa9",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d67f0ccc8f29438f"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d67f0ccc8f29438f",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-363d6b7ea2094758"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-363d6b7ea2094758",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-61ec15ded8124452"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-61ec15ded8124452",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-1a8e652505774fd3",
      "source-5a8600e5ee8b4499",
      "source-a40f94f6bcf94fa9",
      "source-d67f0ccc8f29438f",
      "source-363d6b7ea2094758",
      "source-61ec15ded8124452"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 14403,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.0663
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T15:49:25.175709+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1520,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 40615,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:49:32.104844+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 1520,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 1520,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 40615,
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
    "request_payload_bytes": 40615,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-dfe45cf06879458b`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14689,
    "delivered_request_chars": 36802,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36802,
    "working_set_chars": 955
  },
  "id": "w-dfe45cf06879458b",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "quota_day": "2026-09-22",
  "request_hash": "f5e45692bceb82afc603e9dd21a95d025894b77201ab7e44b9d05e6d917b74a0",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-be81bfb1a8c34f09"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-be81bfb1a8c34f09",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-95b521f5de944aab"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-95b521f5de944aab",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c8e93b3070804221"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c8e93b3070804221",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f24a3bc2f8d746d4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f24a3bc2f8d746d4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-fe2349a9b3da41fc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-fe2349a9b3da41fc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-1986257039194b0b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1986257039194b0b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-be81bfb1a8c34f09",
      "source-95b521f5de944aab",
      "source-c8e93b3070804221",
      "source-f24a3bc2f8d746d4",
      "source-fe2349a9b3da41fc",
      "source-1986257039194b0b"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 14689,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.065
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T15:51:38.779613+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 906,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41517,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:51:45.974096+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 906,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 906,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 41517,
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
    "request_payload_bytes": 41517,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-20cbe953440342a9`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14412,
    "delivered_request_chars": 36525,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36525,
    "working_set_chars": 955
  },
  "id": "w-20cbe953440342a9",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2417,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "0eae11e58cf97c8ca9912788d0eef45d067c4e34e3ee1b8a8522f8e8c51685ef",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-745fe5c5ffa845f3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-745fe5c5ffa845f3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f487079c67574131"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f487079c67574131",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c79875db668e4643"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c79875db668e4643",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-98080edfe8234ef2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-98080edfe8234ef2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-851e3b9c2f924975"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-851e3b9c2f924975",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c981d2daf898439e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c981d2daf898439e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-745fe5c5ffa845f3",
      "source-f487079c67574131",
      "source-c79875db668e4643",
      "source-98080edfe8234ef2",
      "source-851e3b9c2f924975",
      "source-c981d2daf898439e"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 14412,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.0663
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T15:53:44.297043+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 5960,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 40656,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:53:55.511074+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 5960,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 5960,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 40656,
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
    "request_payload_bytes": 40656,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-3481e469793b4328`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14400,
    "delivered_request_chars": 36513,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36513,
    "working_set_chars": 955
  },
  "id": "w-3481e469793b4328",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2281,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "a8585d4d3c8c0d8d858f04786c14c56905d5d6643d54932313be12dc11f8c7bc",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-2570b37f5bbb498c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2570b37f5bbb498c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6453079c84f64023"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6453079c84f64023",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-23c93baa8a874ff4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-23c93baa8a874ff4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f7f3d2bf8e7c41f2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f7f3d2bf8e7c41f2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-efd92dfcca5145ec"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-efd92dfcca5145ec",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bbf8bf41a5174799"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bbf8bf41a5174799",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-2570b37f5bbb498c",
      "source-6453079c84f64023",
      "source-23c93baa8a874ff4",
      "source-f7f3d2bf8e7c41f2",
      "source-efd92dfcca5145ec",
      "source-bbf8bf41a5174799"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 14400,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.0663
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T15:55:59.304906+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 814,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 40602,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:56:06.681438+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 814,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 814,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 40602,
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
    "request_payload_bytes": 40602,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-85f7947f801d4787`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 11087,
    "delivered_request_chars": 33174,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 33174,
    "working_set_chars": 955
  },
  "id": "w-85f7947f801d4787",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2259,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "d0f588a32593559a5a1a6b3242469ad6b719359b8982aa0b5c1dca623401f67b",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-2fbae06476674120"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2fbae06476674120",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-acd03dd252c34ab2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-acd03dd252c34ab2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3c89b172e05e400c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3c89b172e05e400c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0f0bd1d190a1480e"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0f0bd1d190a1480e",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3e161da7b0f24144"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3e161da7b0f24144",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-47f3fa136455450d"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-47f3fa136455450d",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-2fbae06476674120",
      "source-acd03dd252c34ab2",
      "source-3c89b172e05e400c",
      "source-0f0bd1d190a1480e",
      "source-3e161da7b0f24144",
      "source-47f3fa136455450d"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 11087,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.0861
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T15:58:08.265584+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1116,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 36441,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T15:58:14.761979+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 1116,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 1116,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 36441,
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
    "request_payload_bytes": 36441,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

### `w-7b8dc20e7a264799`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14662,
    "delivered_request_chars": 36775,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36775,
    "working_set_chars": 955
  },
  "id": "w-7b8dc20e7a264799",
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
        "id": "it-001",
        "score": 0.85,
        "signals": {
          "collected_research": 3,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Foundations of Information Thermodynamics"
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
  "process_id": 2169,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "5859958a6aa136f9c9471631634b9e9e0b720f108b8f716e14d0f05bb31ad68b",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "com-001",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-2bb1042cdc214c9f"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2bb1042cdc214c9f",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-720190247411417c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-720190247411417c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6fd3fa2bd6484479"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6fd3fa2bd6484479",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-efa38f08069d4673"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-efa38f08069d4673",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-07640412affa4f67"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-07640412affa4f67",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-7cf323b6df854f13"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7cf323b6df854f13",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-2bb1042cdc214c9f",
      "source-720190247411417c",
      "source-6fd3fa2bd6484479",
      "source-efa38f08069d4673",
      "source-07640412affa4f67",
      "source-7cf323b6df854f13"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 7,
      "evidence_count": 6,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 6
      }
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
    "selected_topic": "information_thermodynamics"
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
    "delivered_context_chars": 14662,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 955,
    "working_to_delivered_ratio": 0.0651
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "it-001",
        "next_step": "Synthesize initial research on Landauer's principle and Maxwell's Demon.",
        "question": "How does the relationship between physical entropy and information entropy constrain system efficiency?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "com-001",
        "reason": "Sufficient research time is needed to collect and evaluate the requested sources before synthesis can occur.",
        "task": "Synthesize collected evidence into a foundational notebook on Landauer's principle and Maxwell's Demon"
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
  "status": "deferred",
  "time": "2026-09-22T16:00:14.889461+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 397,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41446,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-22T16:00:22.721122+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 397,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 397,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 41446,
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
    "request_payload_bytes": 41446,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

## Evidence

### `source-5929557bed184f79`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"90f74d8b093a09eeb43f99b865011863d618a0fb57d8041adc341f51b8b67414\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5929557bed184f79",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 0,
  "time": "2026-09-22T15:13:37.709239+00:00"
}
```

### `source-2d5a3108bbac4f52`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149456,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152317,\\\"wordcount\\\":16309,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T06:51:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54612,\\\"wordcount\\\":6016,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-08-15T15:53:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"dcb633161159f18bdbf7d679415402dbde17e0857bfde05e53eb52337872251f\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2d5a3108bbac4f52",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-22T15:13:38.215493+00:00"
}
```

### `source-c4cb1d1e93304192`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"73430acc31722da1ac6df3e0d2e8de0fad5f5eee96390981257cdd7475b3a9d4\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c4cb1d1e93304192",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 0,
  "time": "2026-09-22T15:13:38.814956+00:00"
}
```

### `source-c45d70b71b2a459e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ae38b994cd336d38e69783df9234f912fc55bc963abeed190c570e7eb378733c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c45d70b71b2a459e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 0,
  "time": "2026-09-22T15:13:39.319719+00:00"
}
```

### `source-bc4b85956d2641bf`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40303},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ab519ae5eb5dc244ef2456da06671c4f036f1b9c3cc988c019abefa435f52130\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bc4b85956d2641bf",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-22T15:13:39.725800+00:00"
}
```

### `source-009ba57f5ca5401a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8477}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"8ebeec2d36d0addcdd403529f6115607a25a71ffed662be1dd9811e649bbc279\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-009ba57f5ca5401a",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 0,
  "time": "2026-09-22T15:13:40.070933+00:00"
}
```

### `r-5720f1e969ec41de`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-5720f1e969ec41de\",\"previous_head\":\"104a6644c7392f9de107deccc6aaa85693e1b47fb33248c4966db2bbc2ea1519\",\"process_id\":2319,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-5720f1e969ec41de",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-22T15:13:40.075659+00:00"
}
```

### `source-5076cf616f0341e4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":2199},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy in thermodynamics and information theory\\\",\\\"pageid\\\":3325140,\\\"size\\\":30221,\\\"wordcount\\\":3734,\\\"snippet\\\":\\\"expressions for\\ninformation\\ntheory developed by Claude Shannon and Ralph Hartley in the 1940s are similar to the mathematics of statistical\\nthermodynamics\\nworked\\\",\\\"timestamp\\\":\\\"2026-09-05T20:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"The second law of\\nthermodynamics\\nis a physical law based on universal empirical observation concerning heat and energy interconversions. A simple statement\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"classical\\nthermodynamics\\n(where it was first recognized), to the microscopic description of nature in statistical physics, and the principles of\\ninformation\\ntheory\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Laws of thermodynamics\\\",\\\"pageid\\\":778700,\\\"size\\\":20658,\\\"wordcount\\\":2896,\\\"snippet\\\":\\\"The laws of\\nthermodynamics\\nare a set of scientific laws which define a group of physical quantities, such as temperature, energy, and entropy, that characterize\\\",\\\"timestamp\\\":\\\"2026-07-20T00:17:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thermodynamics\\\",\\\"pageid\\\":29952,\\\"size\\\":49113,\\\"wordcount\\\":5808,\\\"snippet\\\":\\\"\\nThermodynamics\\nis a branch of physics that deals with heat, work, and temperature, and their relation to energy, entropy, and the physical properties of\\\",\\\"timestamp\\\":\\\"2026-09-01T03:12:21Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of thermodynamics\\\",\\\"pageid\\\":2281782,\\\"size\\\":35022,\\\"wordcount\\\":3780,\\\"snippet\\\":\\\"The history of\\nthermodynamics\\nis a fundamental strand in the history of physics, the history of chemistry, and the history of science in general. Due to\\\",\\\"timestamp\\\":\\\"2026-08-29T23:05:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"noisy-channel coding theorem. Entropy in\\ninformation\\ntheory is directly analogous to the entropy in statistical\\nthermodynamics\\n. The analogy results when the values\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicole Yunger Halpern\\\",\\\"pageid\\\":80018960,\\\"size\\\":8512,\\\"wordcount\\\":643,\\\"snippet\\\":\\\"quantum\\nthermodynamics\\n. She works at the National Institute of Standards and Technology, is a fellow of the Joint Center for Quantum\\nInformation\\nand Computer\\\",\\\"timestamp\\\":\\\"2026-08-31T12:40:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Zeroth law of thermodynamics\\\",\\\"pageid\\\":262861,\\\"size\\\":21045,\\\"wordcount\\\":2665,\\\"snippet\\\":\\\"The zeroth law of\\nthermodynamics\\nis one of the four principal laws of\\nthermodynamics\\n. It provides an independent definition of temperature without reference\\\",\\\"timestamp\\\":\\\"2025-12-17T14:08:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Black hole thermodynamics\\\",\\\"pageid\\\":339350,\\\"size\\\":26019,\\\"wordcount\\\":3050,\\\"snippet\\\":\\\"In physics, black hole\\nthermodynamics\\nis a set of physical relationships between the properties of black holes that stands in direct relationship to classical\\\",\\\"timestamp\\\":\\\"2026-09-08T17:19:17Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"86832f7fff702e036550d21769435ecd69075f96b099b5de346f9f0ce7391f91\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5076cf616f0341e4",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json",
  "version": 0,
  "time": "2026-09-22T15:19:51.659202+00:00"
}
```

### `source-4344ba30d504471a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40303},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b3c04e56f6d4d0458fd162681c2727511e63c79b4a150eae2b439d6174e65f60\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-4344ba30d504471a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-22T15:19:52.100912+00:00"
}
```

### `source-8fa42ccbb409443b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"fd97a4fa8b14e48ca3713f75b1f0e2910d233018f4ecb4ba6915f9ab386c3dbf\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-8fa42ccbb409443b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 0,
  "time": "2026-09-22T15:19:52.475591+00:00"
}
```

### `source-6032bad82d8f49e9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239448,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethnic religion\\\",\\\"pageid\\\":344406,\\\"size\\\":8220,\\\"wordcount\\\":792,\\\"snippet\\\":\\\"religious studies, an ethnic\\nreligion\\nor ethnoreligion is a\\nreligion\\nor belief associated with a particular ethnicity. Ethnic\\nreligions\\nare often distinguished\\\",\\\"timestamp\\\":\\\"2026-09-22T13:35:39Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b60dfdef4474af4bcc60a2db1d8425b192169093f2f972b80a9accca9f1ca162\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6032bad82d8f49e9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-22T15:19:53.044224+00:00"
}
```

### `source-3d4994727eb242b8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149456,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152317,\\\"wordcount\\\":16309,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T06:51:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1027c93a570643a49e4a2998ffc20d54b52ab0ded2a70ea5bbdde1ca66b2d38a\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3d4994727eb242b8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-22T15:19:53.557141+00:00"
}
```

### `source-cd9a9a757e7644f6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bd8aa6e37be0d717a698cbed0dde6c465511adbff384f2d44c8c0b2ee713d212\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-cd9a9a757e7644f6",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 0,
  "time": "2026-09-22T15:19:53.833359+00:00"
}
```

### `r-b01216df35934f5e`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-b01216df35934f5e\",\"previous_head\":\"1488d84b7228af9393290946428e32544ec4fd9ae132cb8d292cb14bc94457aa\",\"process_id\":2052,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-b01216df35934f5e",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-22T15:19:53.841860+00:00"
}
```

### `source-11ecfab297f54ff5`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40303},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Class consciousness\\\",\\\"pageid\\\":38794693,\\\"size\\\":11255,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"In sociology, class\\nconsciousness\\nis the set of beliefs that persons hold regarding their social class or economic rank in society, the structure of their\\\",\\\"timestamp\\\":\\\"2026-09-21T19:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a4bcbf54ff7428231236f41fd419ae13a69631aae56895a96f8140529976be60\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-11ecfab297f54ff5",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-22T15:24:28.797138+00:00"
}
```

### `source-928bb8b464934645`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"40f1b917c888692718f11a079c51f9044dcef595c030e793c2a604de6f71ecc5\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-928bb8b464934645",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 0,
  "time": "2026-09-22T15:24:29.304208+00:00"
}
```

### `source-0067a1ae69a3409c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":2199},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy in thermodynamics and information theory\\\",\\\"pageid\\\":3325140,\\\"size\\\":30221,\\\"wordcount\\\":3734,\\\"snippet\\\":\\\"expressions for\\ninformation\\ntheory developed by Claude Shannon and Ralph Hartley in the 1940s are similar to the mathematics of statistical\\nthermodynamics\\nworked\\\",\\\"timestamp\\\":\\\"2026-09-05T20:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Laws of thermodynamics\\\",\\\"pageid\\\":778700,\\\"size\\\":20658,\\\"wordcount\\\":2896,\\\"snippet\\\":\\\"The laws of\\nthermodynamics\\nare a set of scientific laws which define a group of physical quantities, such as temperature, energy, and entropy, that characterize\\\",\\\"timestamp\\\":\\\"2026-07-20T00:17:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"The second law of\\nthermodynamics\\nis a physical law based on universal empirical observation concerning heat and energy interconversions. A simple statement\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"classical\\nthermodynamics\\n(where it was first recognized), to the microscopic description of nature in statistical physics, and the principles of\\ninformation\\ntheory\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thermodynamics\\\",\\\"pageid\\\":29952,\\\"size\\\":49113,\\\"wordcount\\\":5808,\\\"snippet\\\":\\\"\\nThermodynamics\\nis a branch of physics that deals with heat, work, and temperature, and their relation to energy, entropy, and the physical properties of\\\",\\\"timestamp\\\":\\\"2026-09-01T03:12:21Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of thermodynamics\\\",\\\"pageid\\\":2281782,\\\"size\\\":35022,\\\"wordcount\\\":3780,\\\"snippet\\\":\\\"The history of\\nthermodynamics\\nis a fundamental strand in the history of physics, the history of chemistry, and the history of science in general. Due to\\\",\\\"timestamp\\\":\\\"2026-08-29T23:05:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"noisy-channel coding theorem. Entropy in\\ninformation\\ntheory is directly analogous to the entropy in statistical\\nthermodynamics\\n. The analogy results when the values\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicole Yunger Halpern\\\",\\\"pageid\\\":80018960,\\\"size\\\":8512,\\\"wordcount\\\":643,\\\"snippet\\\":\\\"quantum\\nthermodynamics\\n. She works at the National Institute of Standards and Technology, is a fellow of the Joint Center for Quantum\\nInformation\\nand Computer\\\",\\\"timestamp\\\":\\\"2026-08-31T12:40:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Zeroth law of thermodynamics\\\",\\\"pageid\\\":262861,\\\"size\\\":21045,\\\"wordcount\\\":2665,\\\"snippet\\\":\\\"The zeroth law of\\nthermodynamics\\nis one of the four principal laws of\\nthermodynamics\\n. It provides an independent definition of temperature without reference\\\",\\\"timestamp\\\":\\\"2025-12-17T14:08:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy thermodynamics\\\",\\\"pageid\\\":3015758,\\\"size\\\":28263,\\\"wordcount\\\":3649,\\\"snippet\\\":\\\"In physics, maximum entropy\\nthermodynamics\\n(colloquially, MaxEnt\\nthermodynamics\\n) views equilibrium\\nthermodynamics\\nand statistical mechanics as inference\\\",\\\"timestamp\\\":\\\"2026-07-17T03:36:51Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"8bb21e0b992997e66f99dc09665035c1f2ba92f1d31af908e26de49c70662d58\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-0067a1ae69a3409c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json",
  "version": 0,
  "time": "2026-09-22T15:24:29.934096+00:00"
}
```

### `source-03eb8e60560d4584`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239448,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethnic religion\\\",\\\"pageid\\\":344406,\\\"size\\\":8220,\\\"wordcount\\\":792,\\\"snippet\\\":\\\"religious studies, an ethnic\\nreligion\\nor ethnoreligion is a\\nreligion\\nor belief associated with a particular ethnicity. Ethnic\\nreligions\\nare often distinguished\\\",\\\"timestamp\\\":\\\"2026-09-22T13:35:39Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ainu religion\\\",\\\"pageid\\\":33528560,\\\"size\\\":37043,\\\"wordcount\\\":3917,\\\"snippet\\\":\\\"Ainu\\nreligion\\nconsists of the spiritual beliefs, ritual practices, and mythical stories of the Ainu people. It is broadly animist in nature, with special\\\",\\\"timestamp\\\":\\\"2026-06-15T02:48:46Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3cbe6c8d09f3b7baa82d887471f168fd60b7a21ccdd5fac556e7659924ac2229\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-03eb8e60560d4584",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-22T15:24:30.441432+00:00"
}
```

### `source-905872ec4ec84c7b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149455,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152317,\\\"wordcount\\\":16309,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T06:51:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1f801bd595e0035a54eeb35c7243b08a781514ba699c793c330d47c1f6ffb749\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-905872ec4ec84c7b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-22T15:24:30.905773+00:00"
}
```

### `source-bd01375041314499`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8476}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"57e5c127e129dcd4f6532c34d6110e94cc06b7781df30cd80e6bd351f644a60f\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-bd01375041314499",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 0,
  "time": "2026-09-22T15:24:31.065401+00:00"
}
```

### `r-f428af6ac2984cc0`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-f428af6ac2984cc0\",\"previous_head\":\"aff4f9c583c4e489926f7ca6a5211b5d94ccce9f5739f4e20e938ecd86c6d72d\",\"process_id\":2244,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-f428af6ac2984cc0",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-22T15:24:31.081961+00:00"
}
```

### `source-dc01aca9bbfb4250`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9bbddfc4f8b5af32b42252ad1f16098dd6ca47e793fa13c61fc988cf7579fe04\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-dc01aca9bbfb4250",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 0,
  "time": "2026-09-22T15:28:31.213952+00:00"
}
```

### `source-f51c3be2bfdd4daf`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a345a1b971862d31dccb9983b903e122bd77a3809254b66ca6058ccb19438695\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f51c3be2bfdd4daf",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 0,
  "time": "2026-09-22T15:28:31.665893+00:00"
}
```

### `source-5610ff2ad5334c94`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Swan Song (memoir)\\\",\\\"pageid\\\":84007061,\\\"size\\\":13974,\\\"wordcount\\\":1388,\\\"snippet\\\":\\\"Diana's brother, Charles Spencer, addresses conspiracy theories, her\\nneurodivergence\\nand more (Exclusive)\\\". People. Retrieved 21 September 2026. \\\"Charles\\\",\\\"timestamp\\\":\\\"2026-09-22T15:17:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9f56d35182672e107fd90ec5c674f0de42a4340cbd13a757b9d076f370648528\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5610ff2ad5334c94",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 0,
  "time": "2026-09-22T15:28:32.422788+00:00"
}
```

### `source-6e5506eff61542f6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239448,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ancient religion\\\",\\\"pageid\\\":7316418,\\\"size\\\":486,\\\"wordcount\\\":82,\\\"snippet\\\":\\\"Ancient\\nreligion\\nmay refer to: Prehistoric\\nreligion\\nPaleolithic\\nreligion\\nNeolithic\\nreligion\\nBronze and Iron Age\\nreligion\\n:\\nReligions\\nof the ancient Near\\\",\\\"timestamp\\\":\\\"2024-04-27T17:23:31Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"94e3312a714d6c159af38a66adfb2f10c4889c88c25bdd0e2d36dfe873273a2c\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6e5506eff61542f6",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-22T15:28:32.900596+00:00"
}
```

### `source-5b2539e03e944c72`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3a44267c61a1dc89a3aff84980587f9f9f08b15de4172202891d313d3a3e2a15\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5b2539e03e944c72",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 0,
  "time": "2026-09-22T15:28:33.366781+00:00"
}
```

### `source-8d089d1b0f744f8b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149456,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152317,\\\"wordcount\\\":16309,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T06:51:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54612,\\\"wordcount\\\":6016,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-08-15T15:53:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"7442818170981eccb48322c83e3dac9c3157362f6d5c7e8945e433f7cd637445\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-8d089d1b0f744f8b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-22T15:28:34.106922+00:00"
}
```

### `r-1a5e9125dd5f437f`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-1a5e9125dd5f437f\",\"previous_head\":\"02eebd6471279b79c731264e555201f1362d381fbc8a36055cbf9e7dabc66948\",\"process_id\":2258,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-1a5e9125dd5f437f",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-22T15:28:34.125501+00:00"
}
```

### `source-03e2ffeb53ad495b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":2199},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy in thermodynamics and information theory\\\",\\\"pageid\\\":3325140,\\\"size\\\":30221,\\\"wordcount\\\":3734,\\\"snippet\\\":\\\"expressions for\\ninformation\\ntheory developed by Claude Shannon and Ralph Hartley in the 1940s are similar to the mathematics of statistical\\nthermodynamics\\nworked\\\",\\\"timestamp\\\":\\\"2026-09-05T20:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Laws of thermodynamics\\\",\\\"pageid\\\":778700,\\\"size\\\":20658,\\\"wordcount\\\":2896,\\\"snippet\\\":\\\"The laws of\\nthermodynamics\\nare a set of scientific laws which define a group of physical quantities, such as temperature, energy, and entropy, that characterize\\\",\\\"timestamp\\\":\\\"2026-07-20T00:17:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"The second law of\\nthermodynamics\\nis a physical law based on universal empirical observation concerning heat and energy interconversions. A simple statement\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"classical\\nthermodynamics\\n(where it was first recognized), to the microscopic description of nature in statistical physics, and the principles of\\ninformation\\ntheory\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thermodynamics\\\",\\\"pageid\\\":29952,\\\"size\\\":49113,\\\"wordcount\\\":5808,\\\"snippet\\\":\\\"\\nThermodynamics\\nis a branch of physics that deals with heat, work, and temperature, and their relation to energy, entropy, and the physical properties of\\\",\\\"timestamp\\\":\\\"2026-09-01T03:12:21Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"noisy-channel coding theorem. Entropy in\\ninformation\\ntheory is directly analogous to the entropy in statistical\\nthermodynamics\\n. The analogy results when the values\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of thermodynamics\\\",\\\"pageid\\\":2281782,\\\"size\\\":35022,\\\"wordcount\\\":3780,\\\"snippet\\\":\\\"The history of\\nthermodynamics\\nis a fundamental strand in the history of physics, the history of chemistry, and the history of science in general. Due to\\\",\\\"timestamp\\\":\\\"2026-08-29T23:05:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Zeroth law of thermodynamics\\\",\\\"pageid\\\":262861,\\\"size\\\":21045,\\\"wordcount\\\":2665,\\\"snippet\\\":\\\"The zeroth law of\\nthermodynamics\\nis one of the four principal laws of\\nthermodynamics\\n. It provides an independent definition of temperature without reference\\\",\\\"timestamp\\\":\\\"2025-12-17T14:08:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicole Yunger Halpern\\\",\\\"pageid\\\":80018960,\\\"size\\\":8512,\\\"wordcount\\\":643,\\\"snippet\\\":\\\"quantum\\nthermodynamics\\n. She works at the National Institute of Standards and Technology, is a fellow of the Joint Center for Quantum\\nInformation\\nand Computer\\\",\\\"timestamp\\\":\\\"2026-08-31T12:40:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Black hole thermodynamics\\\",\\\"pageid\\\":339350,\\\"size\\\":26019,\\\"wordcount\\\":3050,\\\"snippet\\\":\\\"In physics, black hole\\nthermodynamics\\nis a set of physical relationships between the properties of black holes that stands in direct relationship to classical\\\",\\\"timestamp\\\":\\\"2026-09-08T17:19:17Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b7c2ef7f7b5ce46828accc4afa7247455aaeb24827e96c3028d23d64f1c0ad4c\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-03e2ffeb53ad495b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json",
  "version": 0,
  "time": "2026-09-22T15:30:22.730369+00:00"
}
```

### `source-527af667d6094cdb`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9859bfbb6f752deb82278c41d90294a684cc28d07ee60e16fcfe93fcf16ed6b1\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-527af667d6094cdb",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 0,
  "time": "2026-09-22T15:30:23.126754+00:00"
}
```

### `source-54e747da2a4d413a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239447,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ancient religion\\\",\\\"pageid\\\":7316418,\\\"size\\\":486,\\\"wordcount\\\":82,\\\"snippet\\\":\\\"Ancient\\nreligion\\nmay refer to: Prehistoric\\nreligion\\nPaleolithic\\nreligion\\nNeolithic\\nreligion\\nBronze and Iron Age\\nreligion\\n:\\nReligions\\nof the ancient Near\\\",\\\"timestamp\\\":\\\"2024-04-27T17:23:31Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3e10f4c01ecc3120eafdf532c5a63effff4ba42d810d38bc0b80229f2ce9aaf6\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-54e747da2a4d413a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-22T15:30:23.723100+00:00"
}
```

### `source-ed3577f74ece4b97`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"32e64b6ff62e11f70fe1ff1cd8e90991c8dd64013829ad4ce3a083e6407acdda\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-ed3577f74ece4b97",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 0,
  "time": "2026-09-22T15:30:24.292783+00:00"
}
```

### `source-b5e8cedbd71a47a0`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"202b94bc282e9e3fe3fdf6a34c94caf966550a18b7f9da00977161b0d2430de7\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-b5e8cedbd71a47a0",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 0,
  "time": "2026-09-22T15:30:24.735997+00:00"
}
```

### `source-aa3197a133b64c30`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-aa3197a133b64c30",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 0,
  "time": "2026-09-22T15:30:25.095534+00:00"
}
```

### `r-16e96f5bae6e4457`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-16e96f5bae6e4457\",\"previous_head\":\"8780b47b9a408dd5fe9046cd66072e891477c2d38070515fe8f727a30bdb5c2b\",\"process_id\":2051,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-16e96f5bae6e4457",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-22T15:30:25.111651+00:00"
}
```

### `source-3a27b7c8dd8248c8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149455,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152317,\\\"wordcount\\\":16309,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T06:51:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a2667c4a278176f61f336d1b65f3055caadebf2e892af92c2b3de0b2bc394e7e\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3a27b7c8dd8248c8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-22T15:35:45.388957+00:00"
}
```

### `source-73d0cad95a6a4cf8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":2199},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy in thermodynamics and information theory\\\",\\\"pageid\\\":3325140,\\\"size\\\":30221,\\\"wordcount\\\":3734,\\\"snippet\\\":\\\"expressions for\\ninformation\\ntheory developed by Claude Shannon and Ralph Hartley in the 1940s are similar to the mathematics of statistical\\nthermodynamics\\nworked\\\",\\\"timestamp\\\":\\\"2026-09-05T20:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"The second law of\\nthermodynamics\\nis a physical law based on universal empirical observation concerning heat and energy interconversions. A simple statement\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"classical\\nthermodynamics\\n(where it was first recognized), to the microscopic description of nature in statistical physics, and the principles of\\ninformation\\ntheory\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Laws of thermodynamics\\\",\\\"pageid\\\":778700,\\\"size\\\":20658,\\\"wordcount\\\":2896,\\\"snippet\\\":\\\"The laws of\\nthermodynamics\\nare a set of scientific laws which define a group of physical quantities, such as temperature, energy, and entropy, that characterize\\\",\\\"timestamp\\\":\\\"2026-07-20T00:17:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of thermodynamics\\\",\\\"pageid\\\":2281782,\\\"size\\\":35022,\\\"wordcount\\\":3780,\\\"snippet\\\":\\\"The history of\\nthermodynamics\\nis a fundamental strand in the history of physics, the history of chemistry, and the history of science in general. Due to\\\",\\\"timestamp\\\":\\\"2026-08-29T23:05:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thermodynamics\\\",\\\"pageid\\\":29952,\\\"size\\\":49113,\\\"wordcount\\\":5808,\\\"snippet\\\":\\\"\\nThermodynamics\\nis a branch of physics that deals with heat, work, and temperature, and their relation to energy, entropy, and the physical properties of\\\",\\\"timestamp\\\":\\\"2026-09-01T03:12:21Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"noisy-channel coding theorem. Entropy in\\ninformation\\ntheory is directly analogous to the entropy in statistical\\nthermodynamics\\n. The analogy results when the values\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicole Yunger Halpern\\\",\\\"pageid\\\":80018960,\\\"size\\\":8512,\\\"wordcount\\\":643,\\\"snippet\\\":\\\"quantum\\nthermodynamics\\n. She works at the National Institute of Standards and Technology, is a fellow of the Joint Center for Quantum\\nInformation\\nand Computer\\\",\\\"timestamp\\\":\\\"2026-08-31T12:40:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Zeroth law of thermodynamics\\\",\\\"pageid\\\":262861,\\\"size\\\":21045,\\\"wordcount\\\":2665,\\\"snippet\\\":\\\"The zeroth law of\\nthermodynamics\\nis one of the four principal laws of\\nthermodynamics\\n. It provides an independent definition of temperature without reference\\\",\\\"timestamp\\\":\\\"2025-12-17T14:08:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy thermodynamics\\\",\\\"pageid\\\":3015758,\\\"size\\\":28263,\\\"wordcount\\\":3649,\\\"snippet\\\":\\\"In physics, maximum entropy\\nthermodynamics\\n(colloquially, MaxEnt\\nthermodynamics\\n) views equilibrium\\nthermodynamics\\nand statistical mechanics as inference\\\",\\\"timestamp\\\":\\\"2026-07-17T03:36:51Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"f0ce2941e334ffc493337340e8974459518e8137ab4649f0e12938e8408d5525\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-73d0cad95a6a4cf8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json",
  "version": 0,
  "time": "2026-09-22T15:35:45.904763+00:00"
}
```

### `source-2caac7ce1f1a4450`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Modern Quantum Mechanics\\\",\\\"pageid\\\":66026415,\\\"size\\\":9197,\\\"wordcount\\\":846,\\\"snippet\\\":\\\"Modern\\nQuantum\\nMechanics\\n, often called Sakurai or Sakurai and Napolitano, is a standard graduate-level\\nquantum\\nmechanics\\ntextbook written originally by\\\",\\\"timestamp\\\":\\\"2026-06-20T16:39:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e87cbc8b1b31b3bb2e359da6b1f1ecd80b37135cf1135c57b1ead6353c496147\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2caac7ce1f1a4450",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 0,
  "time": "2026-09-22T15:35:46.466199+00:00"
}
```

### `source-bb998eaa388b4c86`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239447,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Minoan religion\\\",\\\"pageid\\\":7835879,\\\"size\\\":35247,\\\"wordcount\\\":4758,\\\"snippet\\\":\\\"Minoan\\nreligion\\nwas the\\nreligion\\nof the Bronze Age Minoan civilization of Crete. In the absence of readable texts from most of the period, modern scholars\\\",\\\"timestamp\\\":\\\"2026-07-31T08:52:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ancient religion\\\",\\\"pageid\\\":7316418,\\\"size\\\":486,\\\"wordcount\\\":82,\\\"snippet\\\":\\\"Ancient\\nreligion\\nmay refer to: Prehistoric\\nreligion\\nPaleolithic\\nreligion\\nNeolithic\\nreligion\\nBronze and Iron Age\\nreligion\\n:\\nReligions\\nof the ancient Near\\\",\\\"timestamp\\\":\\\"2024-04-27T17:23:31Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"547647dbc4f6b8bb9c94dc6c1c7f1614a6870e79df42efe881b7c4f242d6a106\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bb998eaa388b4c86",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-22T15:35:46.981301+00:00"
}
```

### `source-a8a00a7c6029446c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bea05e98b5ae88ddf78ffff15ef9b5374926b81047cfaa5fb299a21402b0fb87\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-a8a00a7c6029446c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 0,
  "time": "2026-09-22T15:35:47.349404+00:00"
}
```

### `source-0a17d9c43e174670`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-0a17d9c43e174670",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 0,
  "time": "2026-09-22T15:35:47.581534+00:00"
}
```

### `r-0ec3911b56d4467a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-0ec3911b56d4467a\",\"previous_head\":\"c7d0a9d8989639c07284b158f9edab73f2d0096974e0b578a0651c2af5497f84\",\"process_id\":2240,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-0ec3911b56d4467a",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-22T15:35:47.605426+00:00"
}
```

### `source-acc747317c1e45fc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=Landauer%27s+principle+and+Maxwell%27s+Demon+information+thermodynamics&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1887/0750307595/b1154c4\\\", \\\"title\\\": [\\\"Information erasure: Landauer's principle\\\"], \\\"URL\\\": \\\"https://doi.org/10.1887/0750307595/b1154c4\\\"}, {\\\"DOI\\\": \\\"10.2139/ssrn.5877282\\\", \\\"title\\\": [\\\"Computational Complexity Bounds for Maxwell's Demon: From Landauer's Principle to Quantum Advantage\\\"], \\\"URL\\\": \\\"https://doi.org/10.2139/ssrn.5877282\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.21203/rs.3.rs-8271063/v1\\\", \\\"title\\\": [\\\"Computational Complexity Bounds for Maxwell's Demon: From Landauer's Principle to Quantum Advantage\\\"], \\\"abstract\\\": \\\"<title>Abstract</title>\\\\n                <p>\\\\n                  <bold>Whether quantum computational speedups translate to fundamental thermodynamic energy savings remains unresolved. We establish the first rigorous connection between computational complexity and thermodynamic costs through DEMON(I,E) complexity classes that classify information-processing protocols by information complexity I(n) and erasure energy E(n). Four theorems prove: (1) any g-bit erasure dissipates &gt;= g X k_B T  ln 2, generalizing Landauer's principle; (2) measurement disturbance D reduces extractable work to (I-D)k_B T ln 2; (3) Grover-based quantum demons achieve provably optimal Theta(sqrt{N}) thermodynamic advantage over classical search, tight by the BBBV lower bound; and (4) quantum walks on d-dimensional lattices exhibit a dense hierarchy with continuous scaling exponent (d-1)/(2d). Computational validation across six orders of magnitude confirms predictions with &lt;1% error. Experimental predictions include 20.5X energy reduction for trapped-ion Grover search (N=1024, T=1 mK) and 11X effective cooling for superconducting circuit QED heat-bath protocols. This work unifies 158 years of Maxwell demon research, connects algorithmic complexity to physical energy costs, and enables experimental verification of quantum thermodynamic advantages beyond computational speedup.</bold>\\\\n                </p>\\\", \\\"URL\\\": \\\"https://doi.org/10.21203/rs.3.rs-8271063/v1\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 12, 5]]}}, {\\\"DOI\\\": \\\"10.2139/ssrn.5982813\\\", \\\"title\\\": [\\\"Complete Thermodynamics of Information Operations:\\\\\\\\\\\\\\\\Beyond Landauer's Erasure Principle\\\"], \\\"URL\\\": \\\"https://doi.org/10.2139/ssrn.5982813\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"f14fe8ccf711683a31d20204d0c70fe62c6200b6662850fc5ca767d120754860\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1887/0750307595/b1154c4\", \"doi:10.2139/ssrn.5877282\", \"doi:10.21203/rs.3.rs-8271063/v1\", \"doi:10.2139/ssrn.5982813\"]}",
  "id": "source-acc747317c1e45fc",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=Landauer%27s+principle+and+Maxwell%27s+Demon+information+thermodynamics&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-22T15:39:38.897066+00:00"
}
```

### `source-41dd87eb3f524d97`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"107a9bda3658a1e8b194291a54239832eff88261c56fc23d9e9f8ad97ea9a45d\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-41dd87eb3f524d97",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 1,
  "time": "2026-09-22T15:39:39.224700+00:00"
}
```

### `source-068d5f24ab504338`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40303},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Eight Consciousnesses\\\",\\\"pageid\\\":295571,\\\"size\\\":53211,\\\"wordcount\\\":5525,\\\"snippet\\\":\\\"enumerate the five sense\\nconsciousnesses\\n, supplemented by the mental\\nconsciousness\\n(manovij\\\\u00f1\\\\u0101na), the defiled mental\\nconsciousness\\n(kli\\\\u1e63\\\\u1e6damanovij\\\\u00f1\\\\u0101na), and\\\",\\\"timestamp\\\":\\\"2026-07-23T15:02:43Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e43e5e9e34630a4988de34a70b407a1d78b6c23f89bd11106e806b79446560cd\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-068d5f24ab504338",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-22T15:39:39.634229+00:00"
}
```

### `source-6d74beafdc024eff`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149455,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152317,\\\"wordcount\\\":16309,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T06:51:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"f1f9d2fc987777d3ecff7d3bb43aea2d00c7af6908f655b88b542287b52ab42e\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6d74beafdc024eff",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-22T15:39:40.143794+00:00"
}
```

### `source-593d850fad7a45b9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Modern Quantum Mechanics\\\",\\\"pageid\\\":66026415,\\\"size\\\":9197,\\\"wordcount\\\":846,\\\"snippet\\\":\\\"Modern\\nQuantum\\nMechanics\\n, often called Sakurai or Sakurai and Napolitano, is a standard graduate-level\\nquantum\\nmechanics\\ntextbook written originally by\\\",\\\"timestamp\\\":\\\"2026-06-20T16:39:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e87cbc8b1b31b3bb2e359da6b1f1ecd80b37135cf1135c57b1ead6353c496147\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-593d850fad7a45b9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 1,
  "time": "2026-09-22T15:39:40.683335+00:00"
}
```

### `source-6d7d3dae7dda4541`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-6d7d3dae7dda4541",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 1,
  "time": "2026-09-22T15:39:40.974288+00:00"
}
```

### `r-5b044391187a49b2`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-5b044391187a49b2\",\"previous_head\":\"3cad58e88e628996bae7933fa3fda933c5f9bf37f25bc1441bc09910bb9a3d25\",\"process_id\":2107,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-5b044391187a49b2",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-22T15:39:41.002459+00:00"
}
```

### `source-95a451bd629e4fbb`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6b553ef2709199d01d37b4eb6d73b23425cfce96f7d372f993ae920ee1bdbf1f\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-95a451bd629e4fbb",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 1,
  "time": "2026-09-22T15:41:47.380485+00:00"
}
```

### `source-662d96af5e7f4e05`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"04edc9d5a1b4eca5ffaca44849f4191feae30fac7f67ef6cdaf34232695bd085\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-662d96af5e7f4e05",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-22T15:41:47.957213+00:00"
}
```

### `source-17692c00068f4034`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239447,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"f1f7011c42b75aa6f30aa5791b9fd1520e615e39628e8e698552abfbe0c2b8ae\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-17692c00068f4034",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-22T15:41:48.586043+00:00"
}
```

### `source-49b9db1016194c44`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149455,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"4d0971631340cf86e80be8a4a875a85e66208c571214c202158666ccba0cf0db\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-49b9db1016194c44",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-22T15:41:49.259391+00:00"
}
```

### `source-d8daa7b9d76e4776`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bd8aa6e37be0d717a698cbed0dde6c465511adbff384f2d44c8c0b2ee713d212\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d8daa7b9d76e4776",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 1,
  "time": "2026-09-22T15:41:49.688904+00:00"
}
```

### `source-623e4988a6344654`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Modern Quantum Mechanics\\\",\\\"pageid\\\":66026415,\\\"size\\\":9197,\\\"wordcount\\\":846,\\\"snippet\\\":\\\"Modern\\nQuantum\\nMechanics\\n, often called Sakurai or Sakurai and Napolitano, is a standard graduate-level\\nquantum\\nmechanics\\ntextbook written originally by\\\",\\\"timestamp\\\":\\\"2026-06-20T16:39:28Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c8945d84783cc3b4172160af9ba31034d76b06eb9b6b1a1d9336b60f419481e8\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-623e4988a6344654",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 1,
  "time": "2026-09-22T15:41:51.057449+00:00"
}
```

### `r-76d3b27eb08e418c`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-76d3b27eb08e418c\",\"previous_head\":\"632eb670fc22b88110e88e14b7cb037e505efa202ca0191e8967e0bde53f04cb\",\"process_id\":2301,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-76d3b27eb08e418c",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-22T15:41:51.090508+00:00"
}
```

### `source-0370dd8cfa6b4e81`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"221c9c8b1aab799a20e0babe5c9505d0bfe728d65597824baf5b687a7cf9ff51\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-0370dd8cfa6b4e81",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-22T15:43:48.447006+00:00"
}
```

### `source-24355458bfc74510`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"cb061e436defb9e95ab5d8138f1973b3060f7fb157fdff5d5dfbc8f1fd2bc41d\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-24355458bfc74510",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 1,
  "time": "2026-09-22T15:43:48.753614+00:00"
}
```

### `source-d6b00bc06439405a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40303},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"adff6b0642333bd0a22047d630674bbb9361ee8f854d5fc2b9c1ae896c9d8d22\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d6b00bc06439405a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-22T15:43:49.043793+00:00"
}
```

### `source-3bef228210934ecb`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6fd0553d9e5598357e7d89049c929f0adc220ce0e93c94ba5d50ffb35d9fa1e0\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3bef228210934ecb",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-22T15:43:49.464556+00:00"
}
```

### `source-d68388e6c8c845aa`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3a44267c61a1dc89a3aff84980587f9f9f08b15de4172202891d313d3a3e2a15\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d68388e6c8c845aa",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 1,
  "time": "2026-09-22T15:43:49.835419+00:00"
}
```

### `source-2a5a1c2c0ca044e7`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"55bb2684833722ad32b576c6ffad78cd46432126f79f1a8accd9e109354637df\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2a5a1c2c0ca044e7",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 1,
  "time": "2026-09-22T15:43:50.148371+00:00"
}
```

### `r-40869f26688a483e`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-40869f26688a483e\",\"previous_head\":\"4307027cfa604f5d8a5a2b542b65c38cad0b3b96970be086ff35037492dd0cc5\",\"process_id\":2258,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-40869f26688a483e",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-22T15:43:50.185253+00:00"
}
```

### `source-321e2884dc494a5a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"5c449f53ed9d2f0c70faec06f6a3173bcfed25a336683de9413044a236110470\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-321e2884dc494a5a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-22T15:45:46.306371+00:00"
}
```

### `source-495df910edbd4dc2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"32e64b6ff62e11f70fe1ff1cd8e90991c8dd64013829ad4ce3a083e6407acdda\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-495df910edbd4dc2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 1,
  "time": "2026-09-22T15:45:46.746352+00:00"
}
```

### `source-80c490f4b71d423c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54612,\\\"wordcount\\\":6016,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-08-15T15:53:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"df4f058517074c6c5b2cbdc6a5967a5e074d207c61231d8337755949e6dc5aa1\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-80c490f4b71d423c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-22T15:45:47.267944+00:00"
}
```

### `source-00e7519b99cf4948`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Regular prime\\\",\\\"pageid\\\":323689,\\\"size\\\":20412,\\\"wordcount\\\":2785,\\\"snippet\\\":\\\"Unsolved problem in\\nmathematics\\nAre there infinitely many regular\\nprimes\\n, and if so, is their relative density e \\\\u2212 1 / 2 {\\\\\\\\displaystyle e^{-1/2}} ? More\\\",\\\"timestamp\\\":\\\"2026-07-24T16:46:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eeb0e77c83f773817d11febd7201d2cddfa350d165be8b037d231225ea9199e2\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-00e7519b99cf4948",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 1,
  "time": "2026-09-22T15:45:47.839424+00:00"
}
```

### `source-7d642baea76844d8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bea05e98b5ae88ddf78ffff15ef9b5374926b81047cfaa5fb299a21402b0fb87\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-7d642baea76844d8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 1,
  "time": "2026-09-22T15:45:48.404943+00:00"
}
```

### `source-04b53731fee84454`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-04b53731fee84454",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 1,
  "time": "2026-09-22T15:45:48.602712+00:00"
}
```

### `r-ac9322a529144062`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-ac9322a529144062\",\"previous_head\":\"1349183c8a54ddd5a4641ff525ac3dde2950e4496c89fd4165671b563ac76100\",\"process_id\":2276,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-ac9322a529144062",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-22T15:45:48.642859+00:00"
}
```

### `source-42595ad8c3a847b6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=Landauer%27s+principle+information+thermodynamics+physical+limits&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.2139/ssrn.5982813\\\", \\\"title\\\": [\\\"Complete Thermodynamics of Information Operations:\\\\\\\\\\\\\\\\Beyond Landauer's Erasure Principle\\\"], \\\"URL\\\": \\\"https://doi.org/10.2139/ssrn.5982813\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.1887/0750307595/b1154c4\\\", \\\"title\\\": [\\\"Information erasure: Landauer's principle\\\"], \\\"URL\\\": \\\"https://doi.org/10.1887/0750307595/b1154c4\\\"}, {\\\"DOI\\\": \\\"10.1088/1742-5468/2015/06/p06015\\\", \\\"title\\\": [\\\"Information and thermodynamics: experimental verification of Landauer's Erasure principle\\\"], \\\"URL\\\": \\\"https://doi.org/10.1088/1742-5468/2015/06/p06015\\\", \\\"published\\\": {\\\"date-parts\\\": [[2015, 6, 10]]}}, {\\\"DOI\\\": \\\"10.20944/preprints202506.0097.v1\\\", \\\"title\\\": [\\\"Limits of Landauer’s Principle and the Second Law of Thermodynamics\\\"], \\\"abstract\\\": \\\"<jats:p>Since 1857, the second law of thermodynamics has faced the challenge of Maxwell&amp;#039;s imagined demon. The widely accepted response to this challenge suggests that the demon requires a bit of information to function, and according to Landauer&amp;#039;s principle, the erasure of this bit must offset the entropy reduction achieved by the demon. Recent studies involving two-state physical systems subject to thermal fluctuations at the nanoscale have aimed to either prove Landauer&amp;#039;s principle or to demonstrate Szilard engines or Maxwell&amp;#039;s demons in practice. We developed the equations and a numerical model to simulate the evolution of these systems. The results highlight the distinction between thermodynamic entropy and information entropy. They also demonstrate that Landauer’s principle has a limited range of applicability and that, using a two-state memory, it is possible to eliminate a small amount of entropy without expending energy—challenging the second law of thermodynamics.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.20944/preprints202506.0097.v1\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 6, 2]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"9e943668dc8b19461585f80ac37c32f3ad6fc23c55fd2f40cc2fc70764db3b4c\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.2139/ssrn.5982813\", \"doi:10.1887/0750307595/b1154c4\", \"doi:10.1088/1742-5468/2015/06/p06015\", \"doi:10.20944/preprints202506.0097.v1\"]}",
  "id": "source-42595ad8c3a847b6",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=Landauer%27s+principle+information+thermodynamics+physical+limits&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 2,
  "time": "2026-09-22T15:47:00.599721+00:00"
}
```

### `source-58256c38582545fe`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Regular prime\\\",\\\"pageid\\\":323689,\\\"size\\\":20412,\\\"wordcount\\\":2785,\\\"snippet\\\":\\\"Unsolved problem in\\nmathematics\\nAre there infinitely many regular\\nprimes\\n, and if so, is their relative density e \\\\u2212 1 / 2 {\\\\\\\\displaystyle e^{-1/2}} ? More\\\",\\\"timestamp\\\":\\\"2026-07-24T16:46:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"817faffdf4ca8e741bc48f6d7d7a411e617cd98c6ef70a74b978654caa5e5519\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-58256c38582545fe",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 2,
  "time": "2026-09-22T15:47:01.375513+00:00"
}
```

### `source-d4241a06f2b647e4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40303},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Rule consciousness\\\",\\\"pageid\\\":47313267,\\\"size\\\":1874,\\\"wordcount\\\":217,\\\"snippet\\\":\\\"Rule\\nconsciousness\\nis one of the primary factors of personality out of sixteen, as categorized by Raymond Cattell in 1946 as low- and high-level. The\\\",\\\"timestamp\\\":\\\"2026-09-17T00:12:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1e61be917b50401849d9f01f12724b7a6235c602bd9e0744749f475c269c3387\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d4241a06f2b647e4",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-22T15:47:02.228092+00:00"
}
```

### `source-189a2cf0754b416c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239447,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Minoan religion\\\",\\\"pageid\\\":7835879,\\\"size\\\":35247,\\\"wordcount\\\":4758,\\\"snippet\\\":\\\"Minoan\\nreligion\\nwas the\\nreligion\\nof the Bronze Age Minoan civilization of Crete. In the absence of readable texts from most of the period, modern scholars\\\",\\\"timestamp\\\":\\\"2026-07-31T08:52:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion (disambiguation)\\\",\\\"pageid\\\":8825031,\\\"size\\\":1359,\\\"wordcount\\\":173,\\\"snippet\\\":\\\"Look up\\nreligion\\nin Wiktionary, the free dictionary.\\nReligion\\nis any cultural system of designated behaviors and practices, world views, texts, sanctified\\\",\\\"timestamp\\\":\\\"2025-02-07T03:22:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"14bf47fd51b792111641d917c33a0e9a74dba00bf49117e8f30f5e4e637b1bb3\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-189a2cf0754b416c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-22T15:47:02.751706+00:00"
}
```

### `source-2db1564a49d44934`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Modern Quantum Mechanics\\\",\\\"pageid\\\":66026415,\\\"size\\\":9197,\\\"wordcount\\\":846,\\\"snippet\\\":\\\"Modern\\nQuantum\\nMechanics\\n, often called Sakurai or Sakurai and Napolitano, is a standard graduate-level\\nquantum\\nmechanics\\ntextbook written originally by\\\",\\\"timestamp\\\":\\\"2026-06-20T16:39:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"858f3cfcebe1b316f9f60296294e7718f975b481c38813967ed353a5e7034d12\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2db1564a49d44934",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 2,
  "time": "2026-09-22T15:47:03.360811+00:00"
}
```

### `source-2917d46f7ea9493b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-2917d46f7ea9493b",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 2,
  "time": "2026-09-22T15:47:03.615767+00:00"
}
```

### `r-212da6aff47b4602`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-212da6aff47b4602\",\"previous_head\":\"068182242b72a6068fa5fed3fa443aee75ea3dda809e96d2b369630ede0cfd2b\",\"process_id\":2194,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-212da6aff47b4602",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T15:47:03.660368+00:00"
}
```

### `source-1a8e652505774fd3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=Maxwell%27s+Demon+information+theory+explanation+entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W1987357549\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/0039-3681(70)90010-5\\\", \\\"title\\\": \\\"Maxwell's demon\\\", \\\"publication_year\\\": 1970, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 43, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/0039-3681(70)90010-5\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/0039-3681(70)90010-5\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S21220828\\\", \\\"display_name\\\": \\\"Studies in History and Philosophy of Science Part A\\\", \\\"issn_l\\\": \\\"0039-3681\\\", \\\"issn\\\": [\\\"0039-3681\\\", \\\"1879-2510\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"erih-plus\\\", \\\"jufo-3\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Studies in History and Philosophy of Science Part A\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W2011301632\\\", \\\"doi\\\": \\\"https://doi.org/10.1088/0957-4484/5/1/001\\\", \\\"title\\\": \\\"Sequence logos, machine/channel capacity, Maxwell's demon, and molecular computers: a review of the theory of molecular machines\\\", \\\"publication_year\\\": 1994, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 85, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://iopscience.iop.org/article/10.1088/0957-4484/5/1/001/pdf\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1088/0957-4484/5/1/001\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1088/0957-4484/5/1/001\\\", \\\"pdf_url\\\": \\\"https://iopscience.iop.org/article/10.1088/0957-4484/5/1/001/pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S206811868\\\", \\\"display_name\\\": \\\"Nanotechnology\\\", \\\"issn_l\\\": \\\"0957-4484\\\", \\\"issn\\\": [\\\"0957-4484\\\", \\\"1361-6528\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-2\\\", \\\"medline\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320083\\\", \\\"host_organization_name\\\": \\\"IOP Publishing\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320083\\\", \\\"https://openalex.org/P4310311669\\\"], \\\"host_organization_lineage_names\\\": [\\\"IOP Publishing\\\", \\\"Institute of Physics\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Nanotechnology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Living cells contain many molecules which can make simple decisions, such as whether to bind to a particular nucleotide sequence or not. A theory describing the practical limits of these molecular machines is reviewed. Level 0 theory uses Shannon's information theory to study genetic control systems. Level 1 theory uses Shannon's channel capacity theorem to explain how these biological molecules are able to make their decisions precisely in the face of the thermal maelstrom surrounding them. Level 2 theory shows how the Second Law of Thermodynamics defines the exact extent of the choices available to a molecular machine when it dissipates a given amount of energy. Even the famous Maxwell demon must obey this result. The theory also has implications for designing molecular computers.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2134287462\\\", \\\"doi\\\": \\\"https://doi.org/10.1017/s0960129512000783\\\", \\\"title\\\": \\\"Shannon entropy: a rigorous notion at the crossroads between probability, information theory, dynamical systems and statistical physics\\\", \\\"publication_year\\\": 2014, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 227, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4A4B7B069BCF64CC595635D865317C83/S0960129512000783a.pdf/div-class-title-shannon-entropy-a-rigorous-notion-at-the-crossroads-between-probability-information-theory-dynamical-systems-and-statistical-physics-div.pdf\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1017/s0960129512000783\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1017/s0960129512000783\\\", \\\"pdf_url\\\": \\\"https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4A4B7B069BCF64CC595635D865317C83/S0960129512000783a.pdf/div-class-title-shannon-entropy-a-rigorous-notion-at-the-crossroads-between-probability-information-theory-dynamical-systems-and-statistical-physics-div.pdf\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S101766102\\\", \\\"display_name\\\": \\\"Mathematical Structures in Computer Science\\\", \\\"issn_l\\\": \\\"0960-1295\\\", \\\"issn\\\": [\\\"0960-1295\\\", \\\"1469-8072\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310311721\\\", \\\"host_organization_name\\\": \\\"Cambridge University Press\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310311721\\\", \\\"https://openalex.org/P4310311702\\\"], \\\"host_organization_lineage_names\\\": [\\\"Cambridge University Press\\\", \\\"University of Cambridge\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Mathematical Structures in Computer Science\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Statistical entropy was introduced by Shannon as a basic concept in information theory measuring the average missing information in a random source. Extended into an entropy rate, it gives bounds in coding and compression theorems. In this paper, I describe how statistical entropy and entropy rate relate to other notions of entropy that are relevant to probability theory (entropy of a discrete probability distribution measuring its unevenness), computer sciences (algorithmic complexity), the ergodic theory of dynamical systems (Kolmogorov–Sinai or metric entropy) and statistical physics (Boltzmann entropy). Their mathematical foundations and correlates (the entropy concentration, Sanov, Shannon–McMillan–Breiman, Lempel–Ziv and Pesin theorems) clarify their interpretation and offer a rigorous basis for maximum entropy principles. Although often ignored, these mathematical perspectives give a central position to entropy and relative entropy in statistical laws describing generic collective behaviours, and provide insights into the notions of randomness, typicality and disorder. The relevance of entropy beyond the realm of physics, in particular for living systems and ecosystems, is yet to be demonstrated.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2169642021\\\", \\\"doi\\\": \\\"https://doi.org/10.48550/arxiv.quant-ph/0411172\\\", \\\"title\\\": \\\"Information and Entropy in Quantum Theory\\\", \\\"publication_year\\\": 2004, \\\"type\\\": \\\"preprint\\\", \\\"cited_by_count\\\": 20, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"green\\\", \\\"oa_url\\\": \\\"https://arxiv.org/pdf/quant-ph/0411172\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"pmh:oai:arXiv.org:quant-ph/0411172\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"http://arxiv.org/abs/quant-ph/0411172\\\", \\\"pdf_url\\\": \\\"https://arxiv.org/pdf/quant-ph/0411172\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4306400194\\\", \\\"display_name\\\": \\\"arXiv (Cornell University)\\\", \\\"issn_l\\\": \\\"2331-8422\\\", \\\"issn\\\": [\\\"2331-8422\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": false, \\\"is_core\\\": false, \\\"host_organization\\\": \\\"https://openalex.org/I205783295\\\", \\\"host_organization_name\\\": \\\"Cornell University\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/I205783295\\\"], \\\"host_organization_lineage_names\\\": [], \\\"type\\\": \\\"repository\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"submittedVersion\\\", \\\"is_accepted\\\": false, \\\"is_published\\\": false, \\\"raw_source_name\\\": null, \\\"raw_type\\\": \\\"text\\\"}, \\\"abstract\\\": \\\"We look at certain thought experiments based upon the 'delayed choice' and 'quantum eraser' interference experiments, which present a complementarity between information gathered from a quantum measurement and interference effects. It has been argued that these experiments show the Bohm interpretation of quantum theory is untenable. We demonstrate that these experiments depend critically upon the assumption that a quantum optics device can operate as a measuring device, and show that, in the context of these experiments, it cannot be consistently understood in this way. By contrast, we then show how the notion of 'active information' in the Bohm interpretation provides a coherent explanation of the phenomena shown in these experiments. We then examine the relationship between information and entropy. The thought experiment connecting these two quantities is the Szilard Engine version of Maxwell's Demon, and it has been suggested that quantum measurement plays a key role in this. We provide the first complete description of the operation of the Szilard Engine as a quantum system. This enables us to demonstrate that the role of quantum measurement suggested is incorrect, and further, that the use of information theory to resolve Szilard's paradox is both unnecessary and insufficient. Finally we show that, if the concept of 'active information' is extended to cover thermal density matrices, then many of the conceptual problems raised by this paradox appear to be resolved.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"47ae3a7f46f0c9959199276ef13f171b6b8c9f45fbcaf5779d7a266368fc18cf\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1016/0039-3681(70)90010-5\", \"doi:10.1088/0957-4484/5/1/001\", \"doi:10.1088/0957-4484/5/1/001/pdf\", \"doi:10.1017/s0960129512000783\", \"doi:10.48550/arxiv.quant-ph/0411172\", \"openalex:W1987357549\", \"openalex:W2011301632\", \"openalex:W2134287462\", \"openalex:W2169642021\"]}",
  "id": "source-1a8e652505774fd3",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=Maxwell%27s+Demon+information+theory+explanation+entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 2,
  "time": "2026-09-22T15:49:22.627011+00:00"
}
```

### `source-5a8600e5ee8b4499`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bea05e98b5ae88ddf78ffff15ef9b5374926b81047cfaa5fb299a21402b0fb87\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5a8600e5ee8b4499",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 2,
  "time": "2026-09-22T15:49:23.083096+00:00"
}
```

### `source-a40f94f6bcf94fa9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54612,\\\"wordcount\\\":6016,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-08-15T15:53:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9c25e214d03b1ac03065c98783e2495454dffc23913350ea37e725463ba7b436\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-a40f94f6bcf94fa9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-22T15:49:23.677800+00:00"
}
```

### `source-d67f0ccc8f29438f`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40302},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Class consciousness\\\",\\\"pageid\\\":38794693,\\\"size\\\":11255,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"In sociology, class\\nconsciousness\\nis the set of beliefs that persons hold regarding their social class or economic rank in society, the structure of their\\\",\\\"timestamp\\\":\\\"2026-09-21T19:55:05Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"8c594c9e9c103d37eea9d61fc577a6d65161fc2e38d4233f8ac9880932833689\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d67f0ccc8f29438f",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-22T15:49:24.089648+00:00"
}
```

### `source-363d6b7ea2094758`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e5cb050e7abb5878483ee8a0052ed235a218a3f31bfe89841118f0aa64cf6c6f\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-363d6b7ea2094758",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-22T15:49:24.524306+00:00"
}
```

### `source-61ec15ded8124452`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bd8aa6e37be0d717a698cbed0dde6c465511adbff384f2d44c8c0b2ee713d212\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-61ec15ded8124452",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 2,
  "time": "2026-09-22T15:49:25.099807+00:00"
}
```

### `r-df51e03b28ce4a70`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-df51e03b28ce4a70\",\"previous_head\":\"079baee78d9e2397a138f39c9c7d7912666e8477663db0088445ef0133f974dd\",\"process_id\":2242,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-df51e03b28ce4a70",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T15:49:25.148552+00:00"
}
```

### `source-be81bfb1a8c34f09`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"9bbddfc4f8b5af32b42252ad1f16098dd6ca47e793fa13c61fc988cf7579fe04\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-be81bfb1a8c34f09",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 2,
  "time": "2026-09-22T15:51:35.311868+00:00"
}
```

### `source-95b521f5de944aab`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"e5cb050e7abb5878483ee8a0052ed235a218a3f31bfe89841118f0aa64cf6c6f\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-95b521f5de944aab",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-22T15:51:36.058471+00:00"
}
```

### `source-c8e93b3070804221`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"16cc5f4b75c16a60d6265adb4c265482126decbed87b72540f150b9c41f283a1\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c8e93b3070804221",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-22T15:51:36.778284+00:00"
}
```

### `source-f24a3bc2f8d746d4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Modern Quantum Mechanics\\\",\\\"pageid\\\":66026415,\\\"size\\\":9197,\\\"wordcount\\\":846,\\\"snippet\\\":\\\"Modern\\nQuantum\\nMechanics\\n, often called Sakurai or Sakurai and Napolitano, is a standard graduate-level\\nquantum\\nmechanics\\ntextbook written originally by\\\",\\\"timestamp\\\":\\\"2026-06-20T16:39:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a54dca77a044454474c5728577214eeece4433822b0e922738d7ddc004e1dfb7\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f24a3bc2f8d746d4",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 2,
  "time": "2026-09-22T15:51:37.391619+00:00"
}
```

### `source-fe2349a9b3da41fc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6d95ebc8c2cdd4a210ed44fcdc0c885d22fe6001f8df5d501694f544320c0ba8\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-fe2349a9b3da41fc",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 2,
  "time": "2026-09-22T15:51:37.986082+00:00"
}
```

### `source-1986257039194b0b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-1986257039194b0b",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 2,
  "time": "2026-09-22T15:51:38.407346+00:00"
}
```

### `r-dfe45cf06879458b`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-dfe45cf06879458b\",\"previous_head\":\"cb90617f836f150112bcadbf8e98c6c6fdb60d2b63755257d7ff7da70a7639a7\",\"process_id\":2051,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-dfe45cf06879458b",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T15:51:38.600701+00:00"
}
```

### `source-745fe5c5ffa845f3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"d3225d7c4778bd4b320e39c8c1e68bffe0f25d220999131ad9218dc34ce3d6d1\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-745fe5c5ffa845f3",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 2,
  "time": "2026-09-22T15:53:41.993298+00:00"
}
```

### `source-f487079c67574131`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6f419ee3c52658bdeef485c3d44518d0e8683e0521b327612dafcf67c990c2a3\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-f487079c67574131",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 2,
  "time": "2026-09-22T15:53:42.548258+00:00"
}
```

### `source-c79875db668e4643`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40302},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"025db8ded87e637b63bc083cede341ac63a5d4148e63950545dbf268e393a57e\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c79875db668e4643",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-22T15:53:42.967636+00:00"
}
```

### `source-98080edfe8234ef2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"107a9bda3658a1e8b194291a54239832eff88261c56fc23d9e9f8ad97ea9a45d\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-98080edfe8234ef2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 2,
  "time": "2026-09-22T15:53:43.342440+00:00"
}
```

### `source-851e3b9c2f924975`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Evolutionary psychology\\\",\\\"pageid\\\":9703,\\\"size\\\":177589,\\\"wordcount\\\":19341,\\\"snippet\\\":\\\"Evolutionary\\npsychology\\nis a theoretical approach in\\npsychology\\nthat examines cognition and behavior from a modern evolutionary perspective. It seeks to\\\",\\\"timestamp\\\":\\\"2026-09-14T00:20:33Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"5545e0d3852182fdd845fddb46eebfaa0f31e486347e89787d4187ed819015b7\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-851e3b9c2f924975",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-22T15:53:43.747131+00:00"
}
```

### `source-c981d2daf898439e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239447,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"No religion\\\",\\\"pageid\\\":8656279,\\\"size\\\":549,\\\"wordcount\\\":105,\\\"snippet\\\":\\\"No\\nreligion\\nmay refer to: Irreligion, absence of, or indifference towards\\nreligion\\nAtheism, the absence of belief of the existence of deities Agnosticism\\\",\\\"timestamp\\\":\\\"2026-02-05T03:10:03Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"7e7786b12236e56778792b53f5aeded5513d427976fac8ac1b02cb2bf9533a6e\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c981d2daf898439e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-22T15:53:44.210150+00:00"
}
```

### `r-20cbe953440342a9`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-20cbe953440342a9\",\"previous_head\":\"91b3b9322d0a5d01035c9607dc157799226a7201c45d6a0aec9d7706ccb69f44\",\"process_id\":2417,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-20cbe953440342a9",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T15:53:44.266125+00:00"
}
```

### `source-2570b37f5bbb498c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Regular prime\\\",\\\"pageid\\\":323689,\\\"size\\\":20412,\\\"wordcount\\\":2785,\\\"snippet\\\":\\\"Unsolved problem in\\nmathematics\\nAre there infinitely many regular\\nprimes\\n, and if so, is their relative density e \\\\u2212 1 / 2 {\\\\\\\\displaystyle e^{-1/2}} ? More\\\",\\\"timestamp\\\":\\\"2026-07-24T16:46:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"f965db7de9c814084560f305919049f0a39138e5bbc62e6c848fa0e10a9bddd6\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-2570b37f5bbb498c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 2,
  "time": "2026-09-22T15:55:56.877843+00:00"
}
```

### `source-6453079c84f64023`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40302},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Rule consciousness\\\",\\\"pageid\\\":47313267,\\\"size\\\":1874,\\\"wordcount\\\":217,\\\"snippet\\\":\\\"Rule\\nconsciousness\\nis one of the primary factors of personality out of sixteen, as categorized by Raymond Cattell in 1946 as low- and high-level. The\\\",\\\"timestamp\\\":\\\"2026-09-17T00:12:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"769187290b9e3cbcb94dc8b5e05d5f9458f85ffdf0ef812ae1e3b6763b4388ca\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6453079c84f64023",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-22T15:55:57.349751+00:00"
}
```

### `source-23c93baa8a874ff4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54614,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-09-22T15:46:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"40eaad26af3d2647fe1ae8181da35513ff0db951988d4050b6f3d525914d68cd\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-23c93baa8a874ff4",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-22T15:55:57.836900+00:00"
}
```

### `source-f7f3d2bf8e7c41f2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3e843ffb59febd6191f6f342ca0fdf168747af195af7bbeb501ebe11a37a043b\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f7f3d2bf8e7c41f2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 2,
  "time": "2026-09-22T15:55:58.229527+00:00"
}
```

### `source-efd92dfcca5145ec`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sport psychology\\\",\\\"pageid\\\":25688228,\\\"size\\\":150839,\\\"wordcount\\\":18320,\\\"snippet\\\":\\\"Sport\\npsychology\\nis defined as the study of the psychological basis, processes, and effects of sport. One definition of sport sees it as \\\"any physical\\\",\\\"timestamp\\\":\\\"2026-09-08T17:47:08Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1898595409b6f80ce63461628af44ac29b3969c1219d1a8f4f4f931e91f20c80\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-efd92dfcca5145ec",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-22T15:55:58.714726+00:00"
}
```

### `source-bbf8bf41a5174799`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"fd97a4fa8b14e48ca3713f75b1f0e2910d233018f4ecb4ba6915f9ab386c3dbf\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bbf8bf41a5174799",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 2,
  "time": "2026-09-22T15:55:59.205451+00:00"
}
```

### `r-3481e469793b4328`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-3481e469793b4328\",\"previous_head\":\"6bf6069f45b1c22cd77f1c2a51a62bd580cb35f9ebbf8cdbb66f3e8457cf81f9\",\"process_id\":2281,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-3481e469793b4328",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T15:55:59.269357+00:00"
}
```

### `source-2fbae06476674120`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4977},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":111302,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-16T14:27:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Regular prime\\\",\\\"pageid\\\":323689,\\\"size\\\":20412,\\\"wordcount\\\":2785,\\\"snippet\\\":\\\"Unsolved problem in\\nmathematics\\nAre there infinitely many regular\\nprimes\\n, and if so, is their relative density e \\\\u2212 1 / 2 {\\\\\\\\displaystyle e^{-1/2}} ? More\\\",\\\"timestamp\\\":\\\"2026-07-24T16:46:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"817faffdf4ca8e741bc48f6d7d7a411e617cd98c6ef70a74b978654caa5e5519\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-2fbae06476674120",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 2,
  "time": "2026-09-22T15:58:06.176628+00:00"
}
```

### `source-acd03dd252c34ab2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74316},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a345a1b971862d31dccb9983b903e122bd77a3809254b66ca6058ccb19438695\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-acd03dd252c34ab2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-22T15:58:06.555390+00:00"
}
```

### `source-3c89b172e05e400c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54614,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-09-22T15:46:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2b1f93e7de70f9203676860f99638fa8734391747e3af4e61a6eb3388278c124\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3c89b172e05e400c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-22T15:58:07.018541+00:00"
}
```

### `source-0f0bd1d190a1480e`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"abb4eb2b81e9c174309d84f84c88987bda822cb190b3d9d68c5e4d53fa9fbe4a\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-0f0bd1d190a1480e",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 2,
  "time": "2026-09-22T15:58:07.548858+00:00"
}
```

### `source-3e161da7b0f24144`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40302},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Class consciousness\\\",\\\"pageid\\\":38794693,\\\"size\\\":11255,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"In sociology, class\\nconsciousness\\nis the set of beliefs that persons hold regarding their social class or economic rank in society, the structure of their\\\",\\\"timestamp\\\":\\\"2026-09-21T19:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"406dd0815e2d0fea9e37d1704d9c073406dea990a07af388ab5cf18a0941539e\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3e161da7b0f24144",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-22T15:58:08.050128+00:00"
}
```

### `source-47f3fa136455450d`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"error\": \"HTTPError\", \"scope\": \"fetch failed; no evidence obtained\"}",
  "id": "source-47f3fa136455450d",
  "scope": "failed",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 2,
  "time": "2026-09-22T15:58:08.164124+00:00"
}
```

### `r-85f7947f801d4787`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-85f7947f801d4787\",\"previous_head\":\"7321de151bef89141e170c3b0899fada057868e87f8c830a9e20be887a563029\",\"process_id\":2259,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-85f7947f801d4787",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T15:58:08.229993+00:00"
}
```

### `source-2bb1042cdc214c9f`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c186fc5662378adb4846b78e3f3804b45e0eda300ad9fee4d9529bbd80d35ae7\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2bb1042cdc214c9f",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 2,
  "time": "2026-09-22T16:00:12.272355+00:00"
}
```

### `source-720190247411417c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149364,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bbb3fe35ec3e127ec22c934680e826bda3d1380dd33342999051f98728b3545f\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-720190247411417c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-22T16:00:12.931900+00:00"
}
```

### `source-6fd3fa2bd6484479`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7072},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"32e64b6ff62e11f70fe1ff1cd8e90991c8dd64013829ad4ce3a083e6407acdda\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6fd3fa2bd6484479",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 2,
  "time": "2026-09-22T16:00:13.474324+00:00"
}
```

### `source-efa38f08069d4673`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6108},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"d3225d7c4778bd4b320e39c8c1e68bffe0f25d220999131ad9218dc34ce3d6d1\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-efa38f08069d4673",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 2,
  "time": "2026-09-22T16:00:13.994140+00:00"
}
```

### `source-07640412affa4f67`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74317},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"fa7fff9edcaddb5bacf2012216dbdfb7bba6b098211e06dcf9ca2fa8c3d40c1d\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-07640412affa4f67",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-22T16:00:14.606887+00:00"
}
```

### `source-7cf323b6df854f13`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18361}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21616}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8713}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30197}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12344}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49787}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18017}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86994}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 61239}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49957}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 21875}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"ba7b5b4ec299db6a086f7b55606fb213cd2c77e166a5e22acbd975525be07888\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-7cf323b6df854f13",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 2,
  "time": "2026-09-22T16:00:14.782008+00:00"
}
```

### `r-7b8dc20e7a264799`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"com-001\"],\"invocation\":\"w-7b8dc20e7a264799\",\"previous_head\":\"5eec322ce1dada040cfa48bd17a97d59a5fecd80cfdda22cb8438b504f1066ae\",\"process_id\":2169,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-7b8dc20e7a264799",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-22T16:00:14.851451+00:00"
}
```

## Journal

### 001 · Initiating Information Thermodynamics Inquiry

```json
{
  "cycle": 1,
  "invocation": "w-0ec3911b56d4467a",
  "title": "Initiating Information Thermodynamics Inquiry",
  "summary": "WAKE✳︎ is beginning a structured examination of information thermodynamics, focusing on the conceptual and physical relationships between Shannon entropy and thermodynamic entropy. We are establishing a durable project to synthesize how information-theoretic constraints, such as Landauer's principle, interact with physical systems. This inquiry prioritizes clear differentiation between theoretical models and empirical observations."
}
```

### 002 · Establishing foundational information entropy search

```json
{
  "cycle": 2,
  "invocation": "w-ac9322a529144062",
  "title": "Establishing foundational information entropy search",
  "summary": "WAKE✳︎ is initiating targeted research into Landauer's principle and Maxwell's Demon to support the primary project 'Foundations of Information Thermodynamics'. We currently have general definitions of entropy but lack the specific literature required to address the relationship between physical and information entropy constraints. We are queueing focused inquiries to acquire this evidence."
}
```

## Research

### `res-001`

```json
{
  "domain": "information_thermodynamics",
  "id": "res-001",
  "project": "it-001",
  "query": "Landauer's principle and Maxwell's Demon information thermodynamics",
  "reason": "To retrieve foundational theoretical literature required for initial synthesis.",
  "type": "research",
  "status": "collected",
  "created_by": "w-0ec3911b56d4467a",
  "evidence": "source-acc747317c1e45fc"
}
```

### `res-002`

```json
{
  "domain": "information_thermodynamics",
  "id": "res-002",
  "project": "it-001",
  "query": "Landauer's principle information thermodynamics physical limits",
  "reason": "This is required to address the project's next step: synthesizing the role of Landauer's principle in physical efficiency.",
  "type": "research",
  "status": "collected",
  "created_by": "w-ac9322a529144062",
  "evidence": "source-42595ad8c3a847b6"
}
```

### `res-003`

```json
{
  "domain": "information_thermodynamics",
  "id": "res-003",
  "project": "it-001",
  "query": "Maxwell's Demon information theory explanation entropy",
  "reason": "This is required to understand the classical thought experiment that bridges information and physical entropy.",
  "type": "research",
  "status": "collected",
  "created_by": "w-ac9322a529144062",
  "evidence": "source-1a8e652505774fd3"
}
```

## Blog posts

_None recorded._
