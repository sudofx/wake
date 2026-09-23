# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 3  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `68624db50134c91bab4cae4e4f5981e37ede792170b13b1b9b1ec490e4fe775f`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

### `entropy_equivalence_analogy`

```json
{
  "confidence": 0.8,
  "evidence": [
    "source-68482e7469c24480"
  ],
  "id": "entropy_equivalence_analogy",
  "reason": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically.",
  "statement": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-16c4ac30ac534d8c",
  "updated_version": 1
}
```

## Commitments

### `review_thermo_foundations_sources`

```json
{
  "due_cycle": 2,
  "id": "review_thermo_foundations_sources",
  "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
  "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings.",
  "type": "commit",
  "status": "open",
  "created_by": "w-16c4ac30ac534d8c",
  "created_version": 1
}
```

## Projects

### `info_thermo_foundations` · Foundations of Information Thermodynamics

```json
{
  "domain": "information_thermodynamics",
  "id": "info_thermo_foundations",
  "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
  "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
  "reason": "This is our primary configured topic under the current squirrel directive, serving as a baseline for physical information limits.",
  "status": "active",
  "title": "Foundations of Information Thermodynamics",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-16c4ac30ac534d8c"
}
```

## Acquisition capability

### `info_thermo_foundations`

```json
{
  "project": "info_thermo_foundations",
  "domain": "information_thermodynamics",
  "no_progress": 4,
  "routes": [
    "api.openalex.org:discovery",
    "api.crossref.org:discovery"
  ],
  "capability_blocked": true,
  "retry_after_version": 15,
  "persistent_identifiers": [
    "doi:10.1109/phycmp.1992.615502",
    "doi:10.20944/preprints202504.0685.v3",
    "doi:10.20944/preprints202504.0685.v1",
    "doi:10.20944/preprints202504.0685.v2",
    "doi:10.1021/acs.jpclett.4c03156.s001",
    "doi:10.3390/e26110931",
    "doi:10.3390/e27070697",
    "doi:10.3390/e28040376"
  ],
  "last_receipt": {
    "evidence": "source-d7d1f0ad961e4631",
    "outcome": "route_failure",
    "persistent_identifiers": [],
    "research_id": "search_landauer_principle_physical_limits",
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
  "information_thermodynamics": 3
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
  "invocation": "w-03c9df8165bb430a",
  "restored_topics": [],
  "selected_topic": "information_thermodynamics",
  "terminal": "accepted",
  "triggered_topics": []
}
```

## Notebooks

_None recorded._

## Invocations

### `w-16c4ac30ac534d8c`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 11128,
    "delivered_request_chars": 33444,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 33444,
    "working_set_chars": 422
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-16c4ac30ac534d8c",
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
  "quota_day": "2026-09-22",
  "request_hash": "9be376b315fd8d9c29ee74a44c2a6f2f70646e78ed3c80a7cf16fd06ac765bf5",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-2f2da8efa08f4b98"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-2f2da8efa08f4b98",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6089b15b3fba4dca"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6089b15b3fba4dca",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-5bf3787f8dce4108"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-5bf3787f8dce4108",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6684d5852c914803"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6684d5852c914803",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-68482e7469c24480"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-68482e7469c24480",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-52e0594054274110"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-52e0594054274110",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-2f2da8efa08f4b98",
      "source-6089b15b3fba4dca",
      "source-5bf3787f8dce4108",
      "source-6684d5852c914803",
      "source-68482e7469c24480",
      "source-52e0594054274110"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 10,
      "anchor_time": "2026-09-23T06:36:08.671968+00:00",
      "anchor_version": 0,
      "effective_seconds": 207.587055
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 207.587055,
    "effective_scale": 1.0,
    "effective_seconds_total": 207.587055,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 6,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 6
    },
    "observed_at": "2026-09-23T06:36:08.671968+00:00",
    "previous_anchor_time": "2026-09-23T06:32:41.084913+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 207.587055
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
    "delivered_context_chars": 11128,
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
    "working_to_delivered_ratio": 0.0379
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
  "time": "2026-09-23T06:36:08.681376+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1853,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 37713,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 5156,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 37713,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-23T06:36:22.151000+00:00",
  "reason": ""
}
```

### `w-bd51880bfb8549ab`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 13931,
    "delivered_request_chars": 36449,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36449,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-bd51880bfb8549ab",
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
          "coherence": 0.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.0,
          "self_correction": 0
        },
        "id": "info_thermo_foundations",
        "score": 0.5,
        "signals": {
          "collected_research": 0,
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
  "process_id": 2117,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "1b69b7b7dc1eea7e70911c00e7e7a3183be920413097391a1e433282dd1d712d",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-714fee674f314ca6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-714fee674f314ca6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-6f04cc1f08aa46ea"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6f04cc1f08aa46ea",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-222af203597248ec"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-222af203597248ec",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-305abc2499c140cc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-305abc2499c140cc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4bfb613f74cc464a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4bfb613f74cc464a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-bace27e6f3794e24"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-bace27e6f3794e24",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-714fee674f314ca6",
      "source-6f04cc1f08aa46ea",
      "source-222af203597248ec",
      "source-305abc2499c140cc",
      "source-4bfb613f74cc464a",
      "source-bace27e6f3794e24"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 27,
      "anchor_time": "2026-09-23T06:39:59.805750+00:00",
      "anchor_version": 1,
      "effective_seconds": 438.720837
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 231.133782,
    "effective_scale": 1.0,
    "effective_seconds_total": 438.720837,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 16
    },
    "observed_at": "2026-09-23T06:39:59.805750+00:00",
    "previous_anchor_time": "2026-09-23T06:36:08.671968+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 231.133782
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 1,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 13931,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.1152
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "time": "2026-09-23T06:39:59.819655+00:00",
  "provider_attempts": [
    {
      "category": "timeout",
      "elapsed_ms": 60066,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.8-flash",
      "request_payload_bytes": 40553,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 11645,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 40553,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-23T06:41:18.949775+00:00",
  "reason": "Notebook findings evidence must come from the same research topic as its project"
}
```

### `w-0c255ac2891a463a`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14263,
    "delivered_request_chars": 36781,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36781,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-0c255ac2891a463a",
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
          "coherence": 0.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.0,
          "self_correction": 0
        },
        "id": "info_thermo_foundations",
        "score": 0.5,
        "signals": {
          "collected_research": 0,
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
  "process_id": 2292,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "f0be25ad89b4e8716141fbc817578b2d490f48b2fc4ac92f764404baa063b2f3",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-7bd53762e0994fb2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-7bd53762e0994fb2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3d240f8c5286403b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3d240f8c5286403b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f680dddf9bf244d3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f680dddf9bf244d3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4095faa012b14ab5"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4095faa012b14ab5",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d0252707c7334da8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d0252707c7334da8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-90b1fb1abc09428a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-90b1fb1abc09428a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-7bd53762e0994fb2",
      "source-3d240f8c5286403b",
      "source-f680dddf9bf244d3",
      "source-4095faa012b14ab5",
      "source-d0252707c7334da8",
      "source-90b1fb1abc09428a"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 42,
      "anchor_time": "2026-09-23T06:43:42.404487+00:00",
      "anchor_version": 1,
      "effective_seconds": 661.319574
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 222.598737,
    "effective_scale": 1.0,
    "effective_seconds_total": 661.319574,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 1,
      "research_collected": 0,
      "squirrel_assessed": 1,
      "total": 14
    },
    "observed_at": "2026-09-23T06:43:42.404487+00:00",
    "previous_anchor_time": "2026-09-23T06:39:59.805750+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 222.598737
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 1,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 14263,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.1125
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "time": "2026-09-23T06:43:42.431519+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1271,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41429,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 22571,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 41429,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-23T06:44:12.285232+00:00",
  "reason": "Notebook findings evidence must come from the same research topic as its project"
}
```

### `w-aff3bfb6eae048aa`

```json
{
  "base_version": 1,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 14378,
    "delivered_request_chars": 36896,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 36896,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-aff3bfb6eae048aa",
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
          "coherence": 0.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.0,
          "self_correction": 0
        },
        "id": "info_thermo_foundations",
        "score": 0.5,
        "signals": {
          "collected_research": 0,
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
  "process_id": 2050,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "6d7c8196e56452e579d91f2eb367d8f7b520228e039323b32859a37af86bef3e",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-8d020c1bf7e749b8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8d020c1bf7e749b8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f10054c33e5445fd"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f10054c33e5445fd",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-13be5b2c875a4cba"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-13be5b2c875a4cba",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-fe2cd2fb3d7640c7"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-fe2cd2fb3d7640c7",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-162d6b12db5a4468"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-162d6b12db5a4468",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-0e336214e5c745dc"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0e336214e5c745dc",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-8d020c1bf7e749b8",
      "source-f10054c33e5445fd",
      "source-13be5b2c875a4cba",
      "source-fe2cd2fb3d7640c7",
      "source-162d6b12db5a4468",
      "source-0e336214e5c745dc"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 57,
      "anchor_time": "2026-09-23T06:46:56.511496+00:00",
      "anchor_version": 1,
      "effective_seconds": 855.426583
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 194.107009,
    "effective_scale": 1.0,
    "effective_seconds_total": 855.426583,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 1,
      "research_collected": 0,
      "squirrel_assessed": 1,
      "total": 14
    },
    "observed_at": "2026-09-23T06:46:56.511496+00:00",
    "previous_anchor_time": "2026-09-23T06:43:42.404487+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 194.107009
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 1,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 14378,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.1116
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "status": "accepted",
  "time": "2026-09-23T06:46:56.543142+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 3666,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 41621,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "timeout",
      "elapsed_ms": 60095,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 41621,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 7018,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 41621,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T06:48:16.798363+00:00",
  "reason": ""
}
```

### `w-6fc48d7668de46d3`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 15931,
    "delivered_request_chars": 38449,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 38449,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-6fc48d7668de46d3",
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
          "coherence": 0.5,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "info_thermo_foundations",
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
  "process_id": 2240,
  "provider": "gemini",
  "quota_day": "2026-09-22",
  "request_hash": "0302667666be9550536fbb9fe2bdd7a397b98781baf4069db6b04c6b438b56a1",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-05d140a6d98048c7"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-05d140a6d98048c7",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-e5b3faf187504227"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-e5b3faf187504227",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-1457b36f44f249a5"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1457b36f44f249a5",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-9e5b9e95e2f44769"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-9e5b9e95e2f44769",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-de1cae9a26464a92"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-de1cae9a26464a92",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-8a51c0e401cf4ed7"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8a51c0e401cf4ed7",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-05d140a6d98048c7",
      "source-e5b3faf187504227",
      "source-1457b36f44f249a5",
      "source-9e5b9e95e2f44769",
      "source-de1cae9a26464a92",
      "source-8a51c0e401cf4ed7"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 76,
      "anchor_time": "2026-09-23T06:51:39.657636+00:00",
      "anchor_version": 2,
      "effective_seconds": 1138.572723
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 283.14614,
    "effective_scale": 1.0,
    "effective_seconds_total": 1138.572723,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 18
    },
    "observed_at": "2026-09-23T06:51:39.657636+00:00",
    "previous_anchor_time": "2026-09-23T06:46:56.511496+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 283.14614
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 2,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 15931,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.1007
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "time": "2026-09-23T06:51:39.702032+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 198,
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
            "retryDelay": "17s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 17.510761741s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 43167,
      "response_bytes_captured": 1363,
      "result": "daily_quota"
    },
    {
      "category": "http",
      "elapsed_ms": 146,
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
            "retryDelay": "14s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 14.80897436s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 43167,
      "response_bytes_captured": 1362,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 5374,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 43167,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T06:51:54.686906+00:00",
  "reason": "Commitment ID already exists"
}
```

### `w-03c9df8165bb430a`

```json
{
  "base_version": 2,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 15902,
    "delivered_request_chars": 38420,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 38420,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-03c9df8165bb430a",
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
          "coherence": 0.5,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 0.5,
          "self_correction": 0
        },
        "id": "info_thermo_foundations",
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
  "process_id": 2047,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "8479985d575af83dbdbb0d21b7dcf7ace6d9eb1ad5550cd6f2c90b1a9c278e92",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-43761141a14d46f3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-43761141a14d46f3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cf7ef92f7492420b"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cf7ef92f7492420b",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-3f7fa5683d2e4fdd"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-3f7fa5683d2e4fdd",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-d3a09acdf7ce431c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d3a09acdf7ce431c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-653da709a0b34cd1"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-653da709a0b34cd1",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-52a45dc4f9f641a8"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-52a45dc4f9f641a8",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-43761141a14d46f3",
      "source-cf7ef92f7492420b",
      "source-3f7fa5683d2e4fdd",
      "source-d3a09acdf7ce431c",
      "source-653da709a0b34cd1",
      "source-52a45dc4f9f641a8"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 93,
      "anchor_time": "2026-09-23T07:26:51.902357+00:00",
      "anchor_version": 2,
      "effective_seconds": 3250.817444
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 2112.244721,
    "effective_scale": 1.0,
    "effective_seconds_total": 3250.817444,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 7,
      "rejected": 1,
      "research_collected": 0,
      "squirrel_assessed": 1,
      "total": 16
    },
    "observed_at": "2026-09-23T07:26:51.902357+00:00",
    "previous_anchor_time": "2026-09-23T06:51:39.657636+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 2112.244721
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 2,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 15902,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.1009
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "status": "accepted",
  "time": "2026-09-23T07:26:51.950662+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 2264,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 43178,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "timeout",
      "elapsed_ms": 60093,
      "error_type": "TimeoutError",
      "http_status": null,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 43178,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 3918,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 43178,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-23T07:28:08.737771+00:00",
  "reason": ""
}
```

### `w-00df19af81c64c19`

```json
{
  "base_version": 3,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 17486,
    "delivered_request_chars": 40004,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 40004,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-00df19af81c64c19",
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
        "id": "info_thermo_foundations",
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
  "process_id": 2046,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "56b1a0082f0e45d579ccd3f2673118b5c47af70db83a65ff9ea1f5e503dd31ca",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-ee8292ee56af4b72"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-ee8292ee56af4b72",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-c74896606f064ce2"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-c74896606f064ce2",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-9dd7bef90ac94385"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-9dd7bef90ac94385",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a7a710f51022460a"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a7a710f51022460a",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-62bf6499101c45d6"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-62bf6499101c45d6",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-1c277b7ed0ec4bb4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1c277b7ed0ec4bb4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-ee8292ee56af4b72",
      "source-c74896606f064ce2",
      "source-9dd7bef90ac94385",
      "source-a7a710f51022460a",
      "source-62bf6499101c45d6",
      "source-1c277b7ed0ec4bb4"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 112,
      "anchor_time": "2026-09-23T07:55:52.933058+00:00",
      "anchor_version": 3,
      "effective_seconds": 4991.848145
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 1,
    "effective_elapsed_seconds": 1741.030701,
    "effective_scale": 1.0,
    "effective_seconds_total": 4991.848145,
    "intervening_events": {
      "accepted": 1,
      "failed": 0,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 1,
      "total": 18
    },
    "observed_at": "2026-09-23T07:55:52.933058+00:00",
    "previous_anchor_time": "2026-09-23T07:26:51.902357+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 1741.030701
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 3,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 17486,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.0918
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "status": "failed",
  "time": "2026-09-23T07:55:52.994711+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 2340,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 44898,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "http_status": null,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 44898,
      "result": "unknown"
    }
  ],
  "provider_requests_sent": 1,
  "finished": "2026-09-23T07:56:29.032751+00:00",
  "reason": "Provider failed (CalledProcessError); no automatic retry"
}
```

### `w-522db193932148c2`

```json
{
  "base_version": 3,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 18073,
    "delivered_request_chars": 40591,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 40591,
    "working_set_chars": 1605
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-23T06:32:41.084913+00:00",
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
  "id": "w-522db193932148c2",
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
        "id": "info_thermo_foundations",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
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
  "process_id": 2233,
  "provider": "gemini",
  "quota_day": "2026-09-23",
  "request_hash": "e9ddf2bc846cc211a98e3073330693d07c85cc8f81495fc8fd2a7053dea83ddc",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review_thermo_foundations_sources",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-d7d1f0ad961e4631"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d7d1f0ad961e4631",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-e4b6cf6e06594c52"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-e4b6cf6e06594c52",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-8655d5e9cbf24541"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-8655d5e9cbf24541",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-1b0cc7ee01224368"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-1b0cc7ee01224368",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-a3fbbd244af74a16"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-a3fbbd244af74a16",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f750d6585f854e49"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f750d6585f854e49",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-d7d1f0ad961e4631",
      "source-e4b6cf6e06594c52",
      "source-8655d5e9cbf24541",
      "source-1b0cc7ee01224368",
      "source-a3fbbd244af74a16",
      "source-f750d6585f854e49"
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
    "selected_topic": "information_thermodynamics",
    "temporal": {
      "anchor_seq": 127,
      "anchor_time": "2026-09-23T08:00:31.016547+00:00",
      "anchor_version": 3,
      "effective_seconds": 5269.931634
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 278.083489,
    "effective_scale": 1.0,
    "effective_seconds_total": 5269.931634,
    "intervening_events": {
      "accepted": 0,
      "failed": 1,
      "observation": 7,
      "rejected": 0,
      "research_collected": 1,
      "squirrel_assessed": 0,
      "total": 14
    },
    "observed_at": "2026-09-23T08:00:31.016547+00:00",
    "previous_anchor_time": "2026-09-23T07:55:52.933058+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 278.083489
  },
  "trust_compacts_shadow": {
    "compacts": [
      {
        "formation": {
          "criteria": {
            "minimum_confidence": 0.9,
            "minimum_evidence_roots": 2
          },
          "derived_at_version": 3,
          "evidence_root_count": 1,
          "source_confidence": 0.8,
          "source_status": "active"
        },
        "id": "tc-e3ab9028034ff01c",
        "provenance": {
          "belief_id": "entropy_equivalence_analogy",
          "evidence_root_hash": "eff1dac884a8540baae8765eff5766c10a568f4bd5d9431637f9013fedbf8063",
          "evidence_roots": [
            "source-68482e7469c24480"
          ]
        },
        "rehydration": {
          "evidence_ids": [
            "source-68482e7469c24480"
          ],
          "record": {
            "id": "entropy_equivalence_analogy",
            "kind": "belief"
          },
          "trigger": "trust_compact_challenged"
        },
        "reopen_conditions": [
          "credible contradictory evidence is recorded against the belief",
          "a supporting evidence root is invalidated, superseded, or unavailable",
          "the governing scope or decision changes",
          "a human or a governed future retrieval request asks for justification"
        ],
        "rule": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "scope": "durable.belief:entropy_equivalence_analogy",
        "status": "CANDIDATE",
        "strength": "provisional"
      }
    ],
    "limitations": [
      "Compacts are deterministic receipt annotations, not authoritative durable state.",
      "They do not enter provider context in shadow mode.",
      "A compact never deletes, replaces, or proves its underlying evidence."
    ],
    "metrics": {
      "candidate_count": 1,
      "challenged_count": 0,
      "evidence_root_count": 1,
      "provisional_count": 1,
      "settled_count": 0,
      "status_counts": {
        "CANDIDATE": 1
      }
    },
    "mode": "shadow",
    "principle": "Compress settled operational consequences without severing their evidence roots."
  },
  "working_set_metrics": {
    "delivered_context_chars": 18073,
    "inquiry_drive_project_count": 1,
    "mode": "rich",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "trust_compact_candidate_count": 1,
    "trust_compact_evidence_root_count": 1,
    "trust_compact_settled_count": 0,
    "working_set_chars": 1605,
    "working_to_delivered_ratio": 0.0888
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "info_thermo_foundations",
        "next_step": "Gather authoritative sources on Landauer's principle and the formal equivalence between thermodynamic and Shannon entropy.",
        "question": "How do the mathematical formulations of Shannon entropy and thermodynamic entropy map to each other, and what are the physical limits of information processing?",
        "title": "Foundations of Information Thermodynamics"
      }
    ],
    "beliefs": [
      {
        "claim": "The mathematical formulations of Shannon entropy in information theory and entropy in statistical mechanics are directly analogous.",
        "confidence": 0.8,
        "id": "entropy_equivalence_analogy",
        "provenance": [
          "source-68482e7469c24480"
        ],
        "status": "active",
        "why_retained": "Wikipedia search metadata for 'Entropy (information theory)' and 'Entropy in thermodynamics and information theory' notes that the expressions are directly analogous mathematically."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 2,
        "id": "review_thermo_foundations_sources",
        "reason": "To ensure we move systematically from basic Wikipedia search queries to rigorous peer-reviewed abstracts and publications.",
        "task": "Review collected research results on Nicole Yunger Halpern and Shannon-thermodynamic entropy equivalence to draft our initial findings."
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
  "time": "2026-09-23T08:00:31.089394+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1730,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 45557,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 10430,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 45557,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 854,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 45557,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-23T08:00:53.712217+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 854,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 1730,
        "http_status": 503,
        "model": "gemini-3.8-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 45557,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 10430,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 45557,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 854,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 45557,
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
    "request_payload_bytes": 45557,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

## Evidence

### `source-2f2da8efa08f4b98`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40307},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6bbe6c22ac6244520ae3f2a3409c53a6c459228cb7ccf6f80f67fc1a8ee5b9e5\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2f2da8efa08f4b98",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 0,
  "time": "2026-09-23T06:36:07.259699+00:00"
}
```

### `source-6089b15b3fba4dca`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6105},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy\\\",\\\"pageid\\\":1216879,\\\"size\\\":632,\\\"wordcount\\\":100,\\\"snippet\\\":\\\"Maximum\\nentropy\\nthermodynamics Maximum\\nentropy\\nspectral estimation Principle of maximum\\nentropy\\nMaximum\\nentropy\\nprobability distribution Maximum\\nentropy\\nclassifier\\\",\\\"timestamp\\\":\\\"2022-07-15T18:19:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2c8422dc3a560b287e70c293adbbf847d830e23d2a94fefc2d4f926b85ec90a9\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6089b15b3fba4dca",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 0,
  "time": "2026-09-23T06:36:07.544824+00:00"
}
```

### `source-5bf3787f8dce4108`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149365,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethics\\\",\\\"pageid\\\":9258,\\\"size\\\":207219,\\\"wordcount\\\":19811,\\\"snippet\\\":\\\"Ethics is the philosophical study of moral phenomena. Also called moral\\nphilosophy\\n, it investigates normative questions about what people ought to do or\\\",\\\"timestamp\\\":\\\"2026-09-10T16:47:20Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"fa2b3803510f8683fbdef1b8e83015350e97df380b8c9e51eab7888d3449ce76\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-5bf3787f8dce4108",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 0,
  "time": "2026-09-23T06:36:07.851061+00:00"
}
```

### `source-6684d5852c914803`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"1d737614cb85845177bf28af901ff672d0ecd1a474ee73ef8a01f834f9521c14\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6684d5852c914803",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-23T06:36:08.207326+00:00"
}
```

### `source-68482e7469c24480`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":2199},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy in thermodynamics and information theory\\\",\\\"pageid\\\":3325140,\\\"size\\\":30221,\\\"wordcount\\\":3734,\\\"snippet\\\":\\\"expressions for\\ninformation\\ntheory developed by Claude Shannon and Ralph Hartley in the 1940s are similar to the mathematics of statistical\\nthermodynamics\\nworked\\\",\\\"timestamp\\\":\\\"2026-09-05T20:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Laws of thermodynamics\\\",\\\"pageid\\\":778700,\\\"size\\\":20658,\\\"wordcount\\\":2896,\\\"snippet\\\":\\\"The laws of\\nthermodynamics\\nare a set of scientific laws which define a group of physical quantities, such as temperature, energy, and entropy, that characterize\\\",\\\"timestamp\\\":\\\"2026-07-20T00:17:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"classical\\nthermodynamics\\n(where it was first recognized), to the microscopic description of nature in statistical physics, and the principles of\\ninformation\\ntheory\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"The second law of\\nthermodynamics\\nis a physical law based on universal empirical observation concerning heat and energy interconversions. A simple statement\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of thermodynamics\\\",\\\"pageid\\\":2281782,\\\"size\\\":35022,\\\"wordcount\\\":3780,\\\"snippet\\\":\\\"The history of\\nthermodynamics\\nis a fundamental strand in the history of physics, the history of chemistry, and the history of science in general. Due to\\\",\\\"timestamp\\\":\\\"2026-08-29T23:05:41Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Thermodynamics\\\",\\\"pageid\\\":29952,\\\"size\\\":49113,\\\"wordcount\\\":5808,\\\"snippet\\\":\\\"\\nThermodynamics\\nis a branch of physics that deals with heat, work, and temperature, and their relation to energy, entropy, and the physical properties of\\\",\\\"timestamp\\\":\\\"2026-09-01T03:12:21Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"noisy-channel coding theorem. Entropy in\\ninformation\\ntheory is directly analogous to the entropy in statistical\\nthermodynamics\\n. The analogy results when the values\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Zeroth law of thermodynamics\\\",\\\"pageid\\\":262861,\\\"size\\\":21045,\\\"wordcount\\\":2665,\\\"snippet\\\":\\\"The zeroth law of\\nthermodynamics\\nis one of the four principal laws of\\nthermodynamics\\n. It provides an independent definition of temperature without reference\\\",\\\"timestamp\\\":\\\"2025-12-17T14:08:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicole Yunger Halpern\\\",\\\"pageid\\\":80018960,\\\"size\\\":8512,\\\"wordcount\\\":643,\\\"snippet\\\":\\\"quantum\\nthermodynamics\\n. She works at the National Institute of Standards and Technology, is a fellow of the Joint Center for Quantum\\nInformation\\nand Computer\\\",\\\"timestamp\\\":\\\"2026-08-31T12:40:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy thermodynamics\\\",\\\"pageid\\\":3015758,\\\"size\\\":28263,\\\"wordcount\\\":3649,\\\"snippet\\\":\\\"In physics, maximum entropy\\nthermodynamics\\n(colloquially, MaxEnt\\nthermodynamics\\n) views equilibrium\\nthermodynamics\\nand statistical mechanics as inference\\\",\\\"timestamp\\\":\\\"2026-07-17T03:36:51Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"705a42e62d49918b15bfebf2d112bb5fc7318bcaafcdc2743c124588178e1dae\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-68482e7469c24480",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=information+thermodynamics&format=json",
  "version": 0,
  "time": "2026-09-23T06:36:08.528810+00:00"
}
```

### `source-52e0594054274110`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-52e0594054274110",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 0,
  "time": "2026-09-23T06:36:08.668860+00:00"
}
```

### `r-16c4ac30ac534d8c`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-16c4ac30ac534d8c\",\"previous_head\":\"b0a03234673e1198865f4be751bc9ba20eeb606a766fea19317c0bc1efaa7d0f\",\"process_id\":2267,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-16c4ac30ac534d8c",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-23T06:36:08.676310+00:00"
}
```

### `source-714fee674f314ca6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=Nicole+Yunger+Halpern+quantum+information+thermodynamics&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"error\": \"HTTPError\", \"scope\": \"fetch failed; no evidence obtained\"}",
  "id": "source-714fee674f314ca6",
  "scope": "failed",
  "source": "https://api.openalex.org/works?search=Nicole+Yunger+Halpern+quantum+information+thermodynamics&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 1,
  "time": "2026-09-23T06:39:58.004920+00:00"
}
```

### `source-6f04cc1f08aa46ea`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4980},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":108090,\\\"wordcount\\\":6019,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-22T20:55:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Regular prime\\\",\\\"pageid\\\":323689,\\\"size\\\":20412,\\\"wordcount\\\":2785,\\\"snippet\\\":\\\"Unsolved problem in\\nmathematics\\nAre there infinitely many regular\\nprimes\\n, and if so, is their relative density e \\\\u2212 1 / 2 {\\\\\\\\displaystyle e^{-1/2}} ? More\\\",\\\"timestamp\\\":\\\"2026-07-24T16:46:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Formula for primes\\\",\\\"pageid\\\":509009,\\\"size\\\":30336,\\\"wordcount\\\":4689,\\\"snippet\\\":\\\"In number theory, a formula for\\nprimes\\nis a formula that outputs\\nprime\\nnumbers\\n. Such formulas for calculating\\nprimes\\ndo exist; however, they are computationally\\\",\\\"timestamp\\\":\\\"2026-07-05T18:19:14Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"669fcd88659766e9d6d574e252f5af773ab2c6430a0b7721696d3162b7e35265\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-6f04cc1f08aa46ea",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 1,
  "time": "2026-09-23T06:39:58.448684+00:00"
}
```

### `source-222af203597248ec`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Bad Religion\\\",\\\"pageid\\\":168409,\\\"size\\\":101907,\\\"wordcount\\\":10415,\\\"snippet\\\":\\\"Bad\\nReligion\\nis an American punk rock band, formed in Los Angeles, California, in 1980. The band's lyrics cover topics related to\\nreligion\\n, politics, society\\\",\\\"timestamp\\\":\\\"2026-09-14T23:14:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"0ba8d55a56fe6862a9e512d4d6ce60537e8934a98cce134d7e91b554a2422415\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-222af203597248ec",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T06:39:58.776461+00:00"
}
```

### `source-305abc2499c140cc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40307},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a10088b37fe4053bb2e96d7fa0d3038a00a453d50a1c44908d884a4222064321\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-305abc2499c140cc",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-23T06:39:59.304884+00:00"
}
```

### `source-4bfb613f74cc464a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Swan Song (memoir)\\\",\\\"pageid\\\":84007061,\\\"size\\\":14512,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"Diana's brother, Charles Spencer, addresses conspiracy theories, her\\nneurodivergence\\nand more (Exclusive)\\\". People. Retrieved 21 September 2026. \\\"Charles\\\",\\\"timestamp\\\":\\\"2026-09-22T19:43:43Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"40ad6e2120903cf6f45f63998bd0ac69ec1f18f57aabf2716e282d9c800b2f8d\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-4bfb613f74cc464a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 1,
  "time": "2026-09-23T06:39:59.551450+00:00"
}
```

### `source-bace27e6f3794e24`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6105},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy\\\",\\\"pageid\\\":1216879,\\\"size\\\":632,\\\"wordcount\\\":100,\\\"snippet\\\":\\\"Maximum\\nentropy\\nthermodynamics Maximum\\nentropy\\nspectral estimation Principle of maximum\\nentropy\\nMaximum\\nentropy\\nprobability distribution Maximum\\nentropy\\nclassifier\\\",\\\"timestamp\\\":\\\"2022-07-15T18:19:55Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"132eec9ebdeb57d7c447aabaee5f5e4d7d5f369d05e1175221dea8e0b30cafca\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-bace27e6f3794e24",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 1,
  "time": "2026-09-23T06:39:59.801432+00:00"
}
```

### `r-bd51880bfb8549ab`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-bd51880bfb8549ab\",\"previous_head\":\"b9fbbbaaef3f61fce8847d554f363cdf0257c4f29ecd701329cdf925065bf245\",\"process_id\":2117,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-bd51880bfb8549ab",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T06:39:59.813920+00:00"
}
```

### `source-7bd53762e0994fb2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7075},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"4b39efc72208f1515baccc7a3454b92cf699a036f9d212bfeeea0ee8fe5fa634\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-7bd53762e0994fb2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 1,
  "time": "2026-09-23T06:43:40.932092+00:00"
}
```

### `source-3d240f8c5286403b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"bd8aa6e37be0d717a698cbed0dde6c465511adbff384f2d44c8c0b2ee713d212\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3d240f8c5286403b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 1,
  "time": "2026-09-23T06:43:41.191356+00:00"
}
```

### `source-f680dddf9bf244d3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethnic religion\\\",\\\"pageid\\\":344406,\\\"size\\\":8220,\\\"wordcount\\\":792,\\\"snippet\\\":\\\"religious studies, an ethnic\\nreligion\\nor ethnoreligion is a\\nreligion\\nor belief associated with a particular ethnicity. Ethnic\\nreligions\\nare often distinguished\\\",\\\"timestamp\\\":\\\"2026-09-22T13:35:39Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a4272258c0f67be94e5a869e98a494997a74e8b132ee4223df2bf67b8ff194ab\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f680dddf9bf244d3",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T06:43:41.584950+00:00"
}
```

### `source-4095faa012b14ab5`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149365,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Identity (philosophy)\\\",\\\"pageid\\\":89532,\\\"size\\\":10355,\\\"wordcount\\\":1171,\\\"snippet\\\":\\\"true of x is true of y as well. Leibniz's ideas have taken root in the\\nphilosophy\\nof mathematics, where they have influenced the development of the predicate\\\",\\\"timestamp\\\":\\\"2026-06-23T16:17:15Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b96f7e2149467acaec153bf9b98812f5ae52809dc1fcb6c62cf346cd8c3175eb\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-4095faa012b14ab5",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 1,
  "time": "2026-09-23T06:43:41.942232+00:00"
}
```

### `source-d0252707c7334da8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40307},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Animal consciousness\\\",\\\"pageid\\\":13001588,\\\"size\\\":135552,\\\"wordcount\\\":14235,\\\"snippet\\\":\\\"Animal\\nconsciousness\\n, or animal awareness, is the quality or state of self-awareness within an animal, or of being aware of an external object or of something\\\",\\\"timestamp\\\":\\\"2026-09-16T05:21:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"877330eeb2d2440bdd3799ac3104b94345e33adb85ef5b05543919e90ab351eb\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d0252707c7334da8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-23T06:43:42.226818+00:00"
}
```

### `source-90b1fb1abc09428a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-90b1fb1abc09428a",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 1,
  "time": "2026-09-23T06:43:42.396222+00:00"
}
```

### `r-0c255ac2891a463a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-0c255ac2891a463a\",\"previous_head\":\"d9587c160ec452d4a40ea70f7cfae0b2fd613f30c97ab1b65e2bc3b758b164a1\",\"process_id\":2292,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-0c255ac2891a463a",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T06:43:42.421511+00:00"
}
```

### `source-8d020c1bf7e749b8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40307},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Self-consciousness\\\",\\\"pageid\\\":2772118,\\\"size\\\":5955,\\\"wordcount\\\":683,\\\"snippet\\\":\\\"Self-\\nconsciousness\\nis a heightened sense of awareness of oneself. Historically, \\\"self-\\nconsciousness\\n\\\" was synonymous with \\\"self-awareness\\\", referring to\\\",\\\"timestamp\\\":\\\"2026-07-23T22:59:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Science of Consciousness\\\",\\\"pageid\\\":42114583,\\\"size\\\":7071,\\\"wordcount\\\":712,\\\"snippet\\\":\\\"The Science of\\nConsciousness\\n(TSC; formerly Toward a Science of\\nConsciousness\\n) is an international academic conference that has been held biannually since\\\",\\\"timestamp\\\":\\\"2025-06-20T10:35:32Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"ce48083c6ad6e6c9300eb21d1ed27f23b087696d756de42dbc72153160156302\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-8d020c1bf7e749b8",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 1,
  "time": "2026-09-23T06:46:55.345868+00:00"
}
```

### `source-f10054c33e5445fd`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6105},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy\\\",\\\"pageid\\\":1216879,\\\"size\\\":632,\\\"wordcount\\\":100,\\\"snippet\\\":\\\"Maximum\\nentropy\\nthermodynamics Maximum\\nentropy\\nspectral estimation Principle of maximum\\nentropy\\nMaximum\\nentropy\\nprobability distribution Maximum\\nentropy\\nclassifier\\\",\\\"timestamp\\\":\\\"2022-07-15T18:19:55Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"132eec9ebdeb57d7c447aabaee5f5e4d7d5f369d05e1175221dea8e0b30cafca\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-f10054c33e5445fd",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 1,
  "time": "2026-09-23T06:46:55.553191+00:00"
}
```

### `source-13be5b2c875a4cba`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74318},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psyche (psychology)\\\",\\\"pageid\\\":4880472,\\\"size\\\":12752,\\\"wordcount\\\":1458,\\\"snippet\\\":\\\"used synonymously.\\nPsychology\\nis the scientific or objective study of the psyche. The word has a long history of use in\\npsychology\\nand philosophy, dating\\\",\\\"timestamp\\\":\\\"2026-07-05T07:44:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b4bddc1c607b41274d7f4099938552071bc5807b7c5a2d347f39b87c1d244e00\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-13be5b2c875a4cba",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 1,
  "time": "2026-09-23T06:46:55.791049+00:00"
}
```

### `source-fe2cd2fb3d7640c7`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wednesday Addams (Wednesday)\\\",\\\"pageid\\\":83376351,\\\"size\\\":103707,\\\"wordcount\\\":9027,\\\"snippet\\\":\\\"Charli Clement has also pondered on Wednesday's representation of\\nneurodivergence\\n, noting how the character's fictionality and pretty privilege might\\\",\\\"timestamp\\\":\\\"2026-09-21T05:51:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nicki Minaj\\\",\\\"pageid\\\":22570683,\\\"size\\\":380021,\\\"wordcount\\\":31753,\\\"snippet\\\":\\\"Made My ADHD Into My Strength\\\": Understanding The Link Between Rap &\\nNeurodivergence\\n\\\". The Recording Academy. August 3, 2022. Retrieved March 18, 2026.\\\",\\\"timestamp\\\":\\\"2026-09-22T06:17:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"a97230692a1efcd1410d34726bd6f745d3fed381befa33448c701a4f7d84c190\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-fe2cd2fb3d7640c7",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 1,
  "time": "2026-09-23T06:46:55.990356+00:00"
}
```

### `source-162d6b12db5a4468`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethnic religion\\\",\\\"pageid\\\":344406,\\\"size\\\":8220,\\\"wordcount\\\":792,\\\"snippet\\\":\\\"religious studies, an ethnic\\nreligion\\nor ethnoreligion is a\\nreligion\\nor belief associated with a particular ethnicity. Ethnic\\nreligions\\nare often distinguished\\\",\\\"timestamp\\\":\\\"2026-09-22T13:35:39Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"76f16d0586c63966bfa5fcce2b6750c2f8991470910acdcc093e4268ae5dd94a\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-162d6b12db5a4468",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 1,
  "time": "2026-09-23T06:46:56.263382+00:00"
}
```

### `source-0e336214e5c745dc`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-0e336214e5c745dc",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 1,
  "time": "2026-09-23T06:46:56.500905+00:00"
}
```

### `r-aff3bfb6eae048aa`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-aff3bfb6eae048aa\",\"previous_head\":\"1ca9eeaca8e093af644fee6ecc79836e40f83e3b1d7e6c1da87e857ec9496830\",\"process_id\":2050,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-aff3bfb6eae048aa",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-23T06:46:56.532342+00:00"
}
```

### `source-05d140a6d98048c7`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=Landauer%27s+principle+Shannon+thermodynamic+entropy+equivalence+physical+limits&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1109/phycmp.1992.615502\\\", \\\"title\\\": [\\\"Landauer's Principle And Black-hole Entropy\\\"], \\\"URL\\\": \\\"https://doi.org/10.1109/phycmp.1992.615502\\\"}, {\\\"DOI\\\": \\\"10.20944/preprints202504.0685.v3\\\", \\\"title\\\": [\\\"Entropy as First Principle: Deriving Quantum and Gravitational Structure from Thermodynamic Geometry\\\"], \\\"abstract\\\": \\\"<jats:p>This paper introduces the Total Entropic Quantity (TEQ) framework, a structural reformulation of quantum theory grounded in two foundational axioms. Axiom 0 posits entropy as a generative constraint: a geometric principle that determines which configurations can stably distinguish themselves, independent of space, time, or dynamics. Here, entropy is defined as a curvature-functional over distinguishability configurations, preserving only those patterns that remain stable under finite informational resolution---that is, structures not dissolved by coarse-graining or limited observability. Axiom 1, the Minimal Principle (MP), selects from these structures those that are maximally stable under entropy-weighted variation. From this entropic foundation, core elements of quantum theory---including the Born rule, quantization, and Schrödinger dynamics---emerge as special cases of entropy-stabilized geometry. The framework derives an entropy-weighted path integral and introduces a corrected Schrödinger equation that governs evolution in regimes of finite entropy curvature. In the high-resolution limit (\\\\\\\\( \\\\\\\\beta \\\\\\\\to \\\\\\\\infty \\\\\\\\)), TEQ reduces to standard unitary quantum mechanics; in more general regimes, entropy flow deforms canonical dynamics, linking decoherence, dissipation, and gravitational curvature. TEQ reinterprets physical law as emergent structure within the geometry of distinguishability, rather than as imposed dynamics on a fixed spacetime background.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.20944/preprints202504.0685.v3\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 6, 5]]}}, {\\\"DOI\\\": \\\"10.20944/preprints202504.0685.v1\\\", \\\"title\\\": [\\\"Entropy as First Principle: Deriving Quantum and Gravitational Structure from Thermodynamic Geometry\\\"], \\\"abstract\\\": \\\"<jats:p>This paper introduces the Total Entropic Quantity (TEQ) framework, a structural reformulation of quantum theory grounded in two foundational axioms. Axiom 0 posits entropy as a generative constraint: a geometric principle that determines which configurations can stably distinguish themselves, independent of space, time, or dynamics. Here, entropy refers to a curvature-functional over distinguishability configurations, maintaining only those structural patterns that remain stable or well-posed under finite informational resolution—that is, structures that are not destroyed or dissolved by coarse-graining or limited observability. Axiom 1, the Minimal Principle (MP), selects from these configurations those that remain maximally resolvable under finite entropy resolution. From this entropic foundation, core features of quantum theory—including the Born rule, Schrödinger dynamics, quantization, and gravitational structure—emerge as consequences of variation within an entropy-curved geometry. TEQ unifies quantum coherence, classical emergence, and spacetime curvature under a single informational principle, replacing conventional postulates with entropy-stabilized structure. The framework predicts deviations in high-curvature regimes and reinterprets physical law as the geometry of distinguishability rather than imposed dynamics.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.20944/preprints202504.0685.v1\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4, 8]]}}, {\\\"DOI\\\": \\\"10.20944/preprints202504.0685.v2\\\", \\\"title\\\": [\\\"Entropy as First Principle: Deriving Quantum and Gravitational Structure from Thermodynamic Geometry\\\"], \\\"abstract\\\": \\\"<jats:p>This paper introduces the Total Entropic Quantity (TEQ) framework, a structural reformulation of quantum theory grounded in two foundational axioms. Axiom 0 posits entropy as a generative constraint: a geometric principle that determines which configurations can stably distinguish themselves, independent of space, time, or dynamics. Here, entropy is defined as a curvature-functional over distinguishability configurations, preserving only those patterns that remain stable under finite informational resolution---that is, structures not dissolved by coarse-graining or limited observability. Axiom 1, the Minimal Principle (MP), selects from these structures those that are maximally stable under entropy-weighted variation. From this entropic foundation, core elements of quantum theory---including the Born rule, quantization, and Schrödinger dynamics---emerge as special cases of entropy-stabilized geometry. The framework derives an entropy-weighted path integral and introduces a corrected Schrödinger equation that governs evolution in regimes of finite entropy curvature. In the high-resolution limit (\\\\\\\\( \\\\\\\\beta \\\\\\\\to \\\\\\\\infty \\\\\\\\)), TEQ reduces to standard unitary quantum mechanics; in more general regimes, entropy flow deforms canonical dynamics, linking decoherence, dissipation, and gravitational curvature. TEQ reinterprets physical law as emergent structure within the geometry of distinguishability, rather than as imposed dynamics on a fixed spacetime background.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.20944/preprints202504.0685.v2\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 4, 10]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"904896a00df218f6f36478a93af936653b0db1ac4c2f71e15ec937016c8c7cc0\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1109/phycmp.1992.615502\", \"doi:10.20944/preprints202504.0685.v3\", \"doi:10.20944/preprints202504.0685.v1\", \"doi:10.20944/preprints202504.0685.v2\"]}",
  "id": "source-05d140a6d98048c7",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=Landauer%27s+principle+Shannon+thermodynamic+entropy+equivalence+physical+limits&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 2,
  "time": "2026-09-23T06:51:38.228561+00:00"
}
```

### `source-e5b3faf187504227`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Otherkin\\\",\\\"pageid\\\":21702085,\\\"size\\\":37075,\\\"wordcount\\\":3341,\\\"snippet\\\":\\\"non-spiritual explanations for themselves, such as unusual psychology or\\nneurodivergence\\n,[additional citation(s) needed] or as part of dissociative identity\\\",\\\"timestamp\\\":\\\"2026-09-02T04:15:48Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"daefd31387bb79d895761f4b96698e6f053dfda5415b8fa3ff288dfeb491c6f6\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e5b3faf187504227",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 2,
  "time": "2026-09-23T06:51:38.523970+00:00"
}
```

### `source-1457b36f44f249a5`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7075},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Modern Quantum Mechanics\\\",\\\"pageid\\\":66026415,\\\"size\\\":9197,\\\"wordcount\\\":846,\\\"snippet\\\":\\\"Modern\\nQuantum\\nMechanics\\n, often called Sakurai or Sakurai and Napolitano, is a standard graduate-level\\nquantum\\nmechanics\\ntextbook written originally by\\\",\\\"timestamp\\\":\\\"2026-06-20T16:39:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c6ff58a2fb5afa54fefa4f3ef307efed958d45aab4a474bf78c74da695f6fc69\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-1457b36f44f249a5",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 2,
  "time": "2026-09-23T06:51:38.845774+00:00"
}
```

### `source-9e5b9e95e2f44769`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethnic religion\\\",\\\"pageid\\\":344406,\\\"size\\\":8220,\\\"wordcount\\\":792,\\\"snippet\\\":\\\"religious studies, an ethnic\\nreligion\\nor ethnoreligion is a\\nreligion\\nor belief associated with a particular ethnicity. Ethnic\\nreligions\\nare often distinguished\\\",\\\"timestamp\\\":\\\"2026-09-22T13:35:39Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"eaf93f8bfc2f6f88feafd5647a0e41af9599d24cf57de34260d13e6c943e4ce7\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-9e5b9e95e2f44769",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-23T06:51:39.201384+00:00"
}
```

### `source-de1cae9a26464a92`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74318},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"de8be9722226fd9ce8c2df08fc536a9410e3cdc5d3f99cf075a617430c3982e9\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-de1cae9a26464a92",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-23T06:51:39.508454+00:00"
}
```

### `source-8a51c0e401cf4ed7`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-8a51c0e401cf4ed7",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 2,
  "time": "2026-09-23T06:51:39.643342+00:00"
}
```

### `r-6fc48d7668de46d3`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-6fc48d7668de46d3\",\"previous_head\":\"b533d950a5d9e052f590130e2b3685e56781793d9296db25a0c9c0a397bfceb9\",\"process_id\":2240,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-6fc48d7668de46d3",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-23T06:51:39.687169+00:00"
}
```

### `source-43761141a14d46f3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74318},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"aefea50a45db13899e8b1ca1ec3e6fbd982bdb6f06f475193acbee1da3c7591e\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-43761141a14d46f3",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 2,
  "time": "2026-09-23T07:26:50.514393+00:00"
}
```

### `source-cf7ef92f7492420b`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6105},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Maximum entropy\\\",\\\"pageid\\\":1216879,\\\"size\\\":632,\\\"wordcount\\\":100,\\\"snippet\\\":\\\"Maximum\\nentropy\\nthermodynamics Maximum\\nentropy\\nspectral estimation Principle of maximum\\nentropy\\nMaximum\\nentropy\\nprobability distribution Maximum\\nentropy\\nclassifier\\\",\\\"timestamp\\\":\\\"2022-07-15T18:19:55Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"132eec9ebdeb57d7c447aabaee5f5e4d7d5f369d05e1175221dea8e0b30cafca\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-cf7ef92f7492420b",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 2,
  "time": "2026-09-23T07:26:50.757901+00:00"
}
```

### `source-3f7fa5683d2e4fdd`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":149366,\\\"suggestion\\\":\\\"philosopher\\\",\\\"suggestionsnippet\\\":\\\"philosopher\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Philosophy\\\",\\\"pageid\\\":13692155,\\\"size\\\":202240,\\\"wordcount\\\":17550,\\\"snippet\\\":\\\"\\nPhilosophy\\n(from Ancient Greek philosoph\\\\u00eda, lit.\\\\u2009'love of wisdom') is a systematic study of general and fundamental questions concerning topics like existence\\\",\\\"timestamp\\\":\\\"2026-09-21T19:17:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Doctor of Philosophy\\\",\\\"pageid\\\":21031297,\\\"size\\\":152425,\\\"wordcount\\\":16312,\\\"snippet\\\":\\\"A Doctor of\\nPhilosophy\\n(PhD, DPhil; Latin: philosophiae doctor or doctor in philosophia) is a terminal degree that usually denotes the highest level of\\\",\\\"timestamp\\\":\\\"2026-09-22T15:35:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Epistemology\\\",\\\"pageid\\\":9247,\\\"size\\\":211582,\\\"wordcount\\\":19966,\\\"snippet\\\":\\\"Epistemology is the branch of\\nphilosophy\\nthat examines the nature, origin, and limits of knowledge. Also called the theory of knowledge, it explores different\\\",\\\"timestamp\\\":\\\"2026-08-21T14:29:44Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fish! Philosophy\\\",\\\"pageid\\\":8770844,\\\"size\\\":8284,\\\"wordcount\\\":1071,\\\"snippet\\\":\\\"The Fish!\\nPhilosophy\\n(styled FISH!\\nPhilosophy\\n), modeled after the Pike Place Fish Market, is a business technique that is aimed at creating happy individuals\\\",\\\"timestamp\\\":\\\"2026-03-07T07:04:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cynicism (philosophy)\\\",\\\"pageid\\\":19187131,\\\"size\\\":40942,\\\"wordcount\\\":4715,\\\"snippet\\\":\\\"Cynicism (Ancient Greek: \\\\u03ba\\\\u03c5\\\\u03bd\\\\u03b9\\\\u03c3\\\\u03bc\\\\u03cc\\\\u03c2) is a school of thought in ancient Greek\\nphilosophy\\n, originating in the Classical period and extending into the Hellenistic\\\",\\\"timestamp\\\":\\\"2026-05-27T04:15:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Desert (philosophy)\\\",\\\"pageid\\\":10791397,\\\"size\\\":23606,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Desert (/d\\\\u026a\\\\u02c8z\\\\u025c\\\\u02d0rt/) in\\nphilosophy\\nis the condition of being deserving of something, whether good or bad. One type of this is moral desert. It is a concept\\\",\\\"timestamp\\\":\\\"2026-01-20T20:30:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Western philosophy\\\",\\\"pageid\\\":13704154,\\\"size\\\":96464,\\\"wordcount\\\":11377,\\\"snippet\\\":\\\"Western\\nphilosophy\\nrefers to the philosophical thought, traditions, and works of the Western world. Historically, the term refers to the philosophical\\\",\\\"timestamp\\\":\\\"2026-09-21T05:16:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Political philosophy\\\",\\\"pageid\\\":23040,\\\"size\\\":129819,\\\"wordcount\\\":13401,\\\"snippet\\\":\\\"Political\\nphilosophy\\n, also called political theory, is the study of the theoretical and conceptual foundations of politics. It examines the nature, scope\\\",\\\"timestamp\\\":\\\"2026-08-31T02:16:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"Aesthetics is the branch of\\nphilosophy\\nthat studies beauty, taste, and related phenomena. In a broad sense, it includes the\\nphilosophy\\nof art, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Phenomenology (philosophy)\\\",\\\"pageid\\\":76939,\\\"size\\\":54614,\\\"wordcount\\\":6018,\\\"snippet\\\":\\\"appeared in direct connection to Husserl's\\nphilosophy\\nin a 1907 article in The Philosophical Review. In\\nphilosophy\\n, \\\"phenomenology\\\" refers to the tradition\\\",\\\"timestamp\\\":\\\"2026-09-22T15:46:18Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"717e1712b16c884450f35888f8e32d9b27ee5f6ad2fd2e3c508c6667d21047c5\", \"verification_required\": true, \"topic_domain\": \"philosophy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-3f7fa5683d2e4fdd",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=philosophy&format=json",
  "version": 2,
  "time": "2026-09-23T07:26:51.050599+00:00"
}
```

### `source-d3a09acdf7ce431c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239478,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ethnic religion\\\",\\\"pageid\\\":344406,\\\"size\\\":8220,\\\"wordcount\\\":792,\\\"snippet\\\":\\\"religious studies, an ethnic\\nreligion\\nor ethnoreligion is a\\nreligion\\nor belief associated with a particular ethnicity. Ethnic\\nreligions\\nare often distinguished\\\",\\\"timestamp\\\":\\\"2026-09-22T13:35:39Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"3ee78a9cbde5fe59f88ba6644953e0acae8adb2633539b6d9d19353e79619fb2\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d3a09acdf7ce431c",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 2,
  "time": "2026-09-23T07:26:51.355522+00:00"
}
```

### `source-653da709a0b34cd1`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40307},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Rule consciousness\\\",\\\"pageid\\\":47313267,\\\"size\\\":1874,\\\"wordcount\\\":217,\\\"snippet\\\":\\\"Rule\\nconsciousness\\nis one of the primary factors of personality out of sixteen, as categorized by Raymond Cattell in 1946 as low- and high-level. The\\\",\\\"timestamp\\\":\\\"2026-09-17T00:12:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"7e48f5d221eb35b31dd0d0a4e5312ffded139be633279c80a97c1797691d2689\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-653da709a0b34cd1",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 2,
  "time": "2026-09-23T07:26:51.608649+00:00"
}
```

### `source-52a45dc4f9f641a8`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-52a45dc4f9f641a8",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 2,
  "time": "2026-09-23T07:26:51.886460+00:00"
}
```

### `r-03c9df8165bb430a`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-03c9df8165bb430a\",\"previous_head\":\"71fb638774745874f57f999dad24150a0a4eecd797e965a3cc1ec1860ab64262\",\"process_id\":2047,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-03c9df8165bb430a",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-23T07:26:51.935006+00:00"
}
```

### `source-ee8292ee56af4b72`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=Shannon+entropy+thermodynamic+entropy+mathematical+equivalence+landauer+principle&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1021/acs.jpclett.4c03156.s001\\\", \\\"title\\\": [\\\"Deriving the Landauer Principle From the Quantum Shannon Entropy\\\"], \\\"URL\\\": \\\"https://doi.org/10.1021/acs.jpclett.4c03156.s001\\\"}, {\\\"DOI\\\": \\\"10.3390/e26110931\\\", \\\"title\\\": [\\\"Modified Landauer Principle According to Tsallis Entropy\\\"], \\\"abstract\\\": \\\"<jats:p>The Landauer principle establishes a lower bound in the amount of energy that should be dissipated in the erasure of one bit of information. The specific value of this dissipated energy is tightly related to the definition of entropy. In this article, we present a generalization of the Landauer principle based on the Tsallis entropy. Some consequences resulting from such a generalization are discussed. These consequences include the modification to the mass ascribed to one bit of information, the generalization of the Landauer principle to the case when the system is embedded in a gravitational field, and the number of bits radiated in the emission of gravitational waves.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e26110931\\\", \\\"published\\\": {\\\"date-parts\\\": [[2024, 10, 31]]}}, {\\\"DOI\\\": \\\"10.3390/e27070697\\\", \\\"title\\\": [\\\"Landauer Principle and Einstein Synchronization of Clocks: Ramsey Approach\\\"], \\\"abstract\\\": \\\"<jats:p>We introduce a synchronization procedure for clocks based on the Einstein–Landauer framework. Clocks are modeled as discrete, macroscopic devices operating at a thermal equilibrium temperature T. Synchronization is achieved by transmitting photons from one clock to another; the absorption of a photon by a clock reduces the uncertainty in its timekeeping. The minimum energy required for this reduction in uncertainty is determined by the Landauer bound. We distinguish between the time-bearing and non-time-bearing degrees of freedom of the clocks. A reduction in uncertainty under synchronization in the time-bearing degrees of freedom necessarily leads to heat dissipation in the non-time-bearing ones. The minimum energy dissipation in these non-time-bearing degrees of freedom is likewise given by the Landauer limit. The same is true for mechanical synchronization of clocks. We also consider lattices of clocks and analyze synchronization using a Ramsey graph approach. Notably, clocks operating at the same temperature may be synchronized using photons of different frequencies. Each clock is categorized as either synchronized or non-synchronized, resulting in a bi-colored complete graph of clocks. By Ramsey’s theorem, such a graph inevitably contains a triad (or loop) of clocks that are either all synchronized or all non-synchronized. The extension of the Ramsey approach to infinite lattices of clocks is reported.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e27070697\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 6, 29]]}}, {\\\"DOI\\\": \\\"10.3390/e28040376\\\", \\\"title\\\": [\\\"Econophysics and the Landauer Principle: A Redefinition of Economic Temperature\\\"], \\\"abstract\\\": \\\"<jats:p>A redefinition of key notions in econophysics based on the Landauer principle is proposed. Marginal economic temperature is defined via the economic Landauer principle and is proportional to the minimal monetary cost associated with erasing or transmitting one bit of information in a given economic system. The actual economic temperature is defined as the effective monetary cost per irreversibly processed bit in a given economic system. The introduced definitions are particularly relevant for high-frequency trading environments. The Clausius formulation of the Second Law is reformulated for economic systems as the statement that money cannot spontaneously flow from a colder economic subsystem to a hotter one. Economic analogues of Carnot and Szilard engines are analyzed. The Carathéodory formulation of the Second Law is reformulated as follows: in every neighborhood of any equilibrium economic state there exist states that cannot be reached by processes that do not expend money or information. An optimal-power Curzon–Ahlborn economic engine is discussed. Illustrative examples of the introduced economic temperature are provided. Finally, a redefinition of economic entropy based on information processing is proposed. First and Third Laws of economic thermodynamics are proposed.</jats:p>\\\", \\\"URL\\\": \\\"https://doi.org/10.3390/e28040376\\\", \\\"published\\\": {\\\"date-parts\\\": [[2026, 3, 26]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"0030bf1864fe02ad7c3b78406cfe0eb8c0d9411137acb97d454fbc9368383d2b\", \"verification_required\": true, \"topic_domain\": \"information_thermodynamics\", \"evidence_role\": \"discovery\", \"host_tier\": \"verification\", \"persistent_identifiers\": [\"doi:10.1021/acs.jpclett.4c03156.s001\", \"doi:10.3390/e26110931\", \"doi:10.3390/e27070697\", \"doi:10.3390/e28040376\"]}",
  "id": "source-ee8292ee56af4b72",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=Shannon+entropy+thermodynamic+entropy+mathematical+equivalence+landauer+principle&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 3,
  "time": "2026-09-23T07:55:51.106640+00:00"
}
```

### `source-c74896606f064ce2`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239477,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Folk religion\\\",\\\"pageid\\\":21920776,\\\"size\\\":44106,\\\"wordcount\\\":4958,\\\"snippet\\\":\\\"Folk\\nreligion\\n, traditional\\nreligion\\n, or vernacular\\nreligion\\ncomprises, according to religious studies and folkloristics, various forms and expressions\\\",\\\"timestamp\\\":\\\"2026-09-14T10:35:40Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ainu religion\\\",\\\"pageid\\\":33528560,\\\"size\\\":37043,\\\"wordcount\\\":3917,\\\"snippet\\\":\\\"Ainu\\nreligion\\nconsists of the spiritual beliefs, ritual practices, and mythical stories of the Ainu people. It is broadly animist in nature, with special\\\",\\\"timestamp\\\":\\\"2026-06-15T02:48:46Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Vedic religion\\\",\\\"pageid\\\":5919467,\\\"size\\\":642,\\\"wordcount\\\":117,\\\"snippet\\\":\\\"Vedic\\nreligion\\nor Vedism may refer to: Historical Vedic\\nreligion\\n, the\\nreligion\\nof the Indo-Aryans of northern India during the Vedic period Hinduism, which\\\",\\\"timestamp\\\":\\\"2026-09-16T02:42:36Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"615a1235b1fc95d59a1cb7cdc5432edfc612b7efd772467680cafc70cd2d215d\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c74896606f064ce2",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 3,
  "time": "2026-09-23T07:55:51.510982+00:00"
}
```

### `source-9dd7bef90ac94385`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74319},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Shadow (psychology)\\\",\\\"pageid\\\":560394,\\\"size\\\":34954,\\\"wordcount\\\":4164,\\\"snippet\\\":\\\"In analytical\\npsychology\\n, the shadow (also known as ego-dystonic complex, repressed id, shadow aspect, or shadow archetype) is an unconscious aspect of\\\",\\\"timestamp\\\":\\\"2026-09-02T17:23:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Evolutionary psychology\\\",\\\"pageid\\\":9703,\\\"size\\\":177589,\\\"wordcount\\\":19341,\\\"snippet\\\":\\\"Evolutionary\\npsychology\\nis a theoretical approach in\\npsychology\\nthat examines cognition and behavior from a modern evolutionary perspective. It seeks to\\\",\\\"timestamp\\\":\\\"2026-09-14T00:20:33Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"df50b955f2a7960b9495059e36d33f8ce7e307a3a48f03589ab8f16e52353f22\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-9dd7bef90ac94385",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 3,
  "time": "2026-09-23T07:55:51.834648+00:00"
}
```

### `source-a7a710f51022460a`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4980},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":108090,\\\"wordcount\\\":6019,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-22T20:55:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"df7bb1e75e372bcf31b5409c11f9cc54eab85bc45b73e9747dd00b0e5e31c558\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-a7a710f51022460a",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 3,
  "time": "2026-09-23T07:55:52.224960+00:00"
}
```

### `source-62bf6499101c45d6`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":40307},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness\\\",\\\"pageid\\\":5664,\\\"size\\\":187364,\\\"wordcount\\\":21233,\\\"snippet\\\":\\\"\\nConsciousness\\nis being aware of something internal to one's self, or of states or objects in one's external environment. It has been the topic of extensive\\\",\\\"timestamp\\\":\\\"2026-09-19T15:23:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Stream of consciousness\\\",\\\"pageid\\\":101483,\\\"size\\\":26790,\\\"wordcount\\\":3226,\\\"snippet\\\":\\\"In literary criticism, stream of\\nconsciousness\\nis a narrative mode or method that attempts \\\"to depict the multitudinous thoughts and feelings which pass\\\",\\\"timestamp\\\":\\\"2026-06-22T22:10:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hard problem of consciousness\\\",\\\"pageid\\\":634216,\\\"size\\\":115556,\\\"wordcount\\\":13247,\\\"snippet\\\":\\\"hard problem of\\nconsciousness\\n(or simply the hard problem) is to explain how and why organisms have qualia, phenomenal\\nconsciousness\\n, or subjective experience\\\",\\\"timestamp\\\":\\\"2026-08-27T00:59:04Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Artificial consciousness\\\",\\\"pageid\\\":195552,\\\"size\\\":66143,\\\"wordcount\\\":6941,\\\"snippet\\\":\\\"Artificial\\nconsciousness\\n, also known as machine\\nconsciousness\\n, synthetic\\nconsciousness\\n, or digital\\nconsciousness\\n, is\\nconsciousness\\nhypothesized to be\\\",\\\"timestamp\\\":\\\"2026-09-07T05:12:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Consciousness (disambiguation)\\\",\\\"pageid\\\":40457047,\\\"size\\\":695,\\\"wordcount\\\":97,\\\"snippet\\\":\\\"\\nconsciousness\\nin Wiktionary, the free dictionary.\\nConsciousness\\nis the state or quality of awareness.\\nConsciousness\\nmay also refer to:\\nConsciousness\\n(Hill\\\",\\\"timestamp\\\":\\\"2022-05-26T00:46:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Double consciousness\\\",\\\"pageid\\\":3057990,\\\"size\\\":20535,\\\"wordcount\\\":2622,\\\"snippet\\\":\\\"Double\\nconsciousness\\nis the dual self-perception experienced by subordinated or colonized groups in an oppressive society. The term and the idea were\\\",\\\"timestamp\\\":\\\"2026-09-12T04:18:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Higher consciousness\\\",\\\"pageid\\\":7582544,\\\"size\\\":20747,\\\"wordcount\\\":2329,\\\"snippet\\\":\\\"Higher\\nconsciousness\\n(also called expanded\\nconsciousness\\n) is a term that has been used in various ways to label particular states of\\nconsciousness\\nor personal\\\",\\\"timestamp\\\":\\\"2026-08-15T05:53:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Collective consciousness\\\",\\\"pageid\\\":1077491,\\\"size\\\":15253,\\\"wordcount\\\":1536,\\\"snippet\\\":\\\"Collective\\nconsciousness\\n, collective conscience, or collective conscious (French: conscience collective) is the set of shared beliefs, ideas, and moral\\\",\\\"timestamp\\\":\\\"2026-07-29T04:14:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Clouding of consciousness\\\",\\\"pageid\\\":7554116,\\\"size\\\":78787,\\\"wordcount\\\":7669,\\\"snippet\\\":\\\"Clouding of\\nconsciousness\\n, also called brain fog or mental fog, occurs when a person is conscious but slightly less wakeful or aware than normal. The\\\",\\\"timestamp\\\":\\\"2026-09-12T16:42:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Eight Consciousnesses\\\",\\\"pageid\\\":295571,\\\"size\\\":53211,\\\"wordcount\\\":5525,\\\"snippet\\\":\\\"enumerate the five sense\\nconsciousnesses\\n, supplemented by the mental\\nconsciousness\\n(manovij\\\\u00f1\\\\u0101na), the defiled mental\\nconsciousness\\n(kli\\\\u1e63\\\\u1e6damanovij\\\\u00f1\\\\u0101na), and\\\",\\\"timestamp\\\":\\\"2026-07-23T15:02:43Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"31be6c8c4ffb9eff031428971418795e846aac4a73face290877f77e53017f5c\", \"verification_required\": true, \"topic_domain\": \"consciousness\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-62bf6499101c45d6",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=consciousness&format=json",
  "version": 3,
  "time": "2026-09-23T07:55:52.555344+00:00"
}
```

### `source-1c277b7ed0ec4bb4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-1c277b7ed0ec4bb4",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 3,
  "time": "2026-09-23T07:55:52.914369+00:00"
}
```

### `r-00df19af81c64c19`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-00df19af81c64c19\",\"previous_head\":\"12cc8fa087e070d08cfd1004ec5990ca05e614a0da7fde556419b89cdd20e6b4\",\"process_id\":2046,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-00df19af81c64c19",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-23T07:55:52.975084+00:00"
}
```

### `source-d7d1f0ad961e4631`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=Landauer+principle+physical+limits+information+processing+thermodynamic+cost&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"error\": \"HTTPError\", \"scope\": \"fetch failed; no evidence obtained\"}",
  "id": "source-d7d1f0ad961e4631",
  "scope": "failed",
  "source": "https://api.openalex.org/works?search=Landauer+principle+physical+limits+information+processing+thermodynamic+cost&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 3,
  "time": "2026-09-23T08:00:29.272151+00:00"
}
```

### `source-e4b6cf6e06594c52`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":120,\\\"suggestion\\\":\\\"neurodivergent\\\",\\\"suggestionsnippet\\\":\\\"neurodivergent\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurodiversity\\\",\\\"pageid\\\":1073739,\\\"size\\\":142665,\\\"wordcount\\\":13881,\\\"snippet\\\":\\\"and other\\nneurodivergences\\nas a natural part of human neurological diversity\\\\u2014not diseases or disorders, just \\\"difference[s]\\\".\\nNeurodivergences\\ninclude autism\\\",\\\"timestamp\\\":\\\"2026-09-15T23:26:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neuroqueer theory\\\",\\\"pageid\\\":76016274,\\\"size\\\":31724,\\\"wordcount\\\":3380,\\\"snippet\\\":\\\"have suggested the existence of a relationship between queerness and\\nneurodivergence\\n: where neurodivergent people are more likely than their neurotypical\\\",\\\"timestamp\\\":\\\"2026-08-29T18:08:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurofibromatosis type I\\\",\\\"pageid\\\":1712548,\\\"size\\\":63138,\\\"wordcount\\\":7236,\\\"snippet\\\":\\\"Neurofibromatosis type I (NF-1), or von Recklinghausen syndrome, is a complex multi-system neurocutaneous disorder caused by a subset of genetic mutations\\\",\\\"timestamp\\\":\\\"2026-09-11T22:12:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fern Brady\\\",\\\"pageid\\\":43399498,\\\"size\\\":15262,\\\"wordcount\\\":1330,\\\"snippet\\\":\\\"active within the field of autism education since learning of her\\nneurodivergence\\n. She has written about life as an autistic person in her 2023 memoir\\\",\\\"timestamp\\\":\\\"2026-09-20T00:11:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mel King (The Pitt)\\\",\\\"pageid\\\":82753144,\\\"size\\\":15333,\\\"wordcount\\\":1322,\\\"snippet\\\":\\\"and praises her for it. Mel explains that she has experience with\\nneurodivergence\\nbecause her sister Becca (Tal Anderson) is also autistic. Mel is Becca's\\\",\\\"timestamp\\\":\\\"2026-08-07T04:12:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Kassiane Asasumasu\\\",\\\"pageid\\\":76250908,\\\"size\\\":14907,\\\"wordcount\\\":1302,\\\"snippet\\\":\\\"related to the neurodiversity movement, including neurodivergent,\\nneurodivergence\\n, and caregiver benevolence. As stated in the text Neurodiversity for\\\",\\\"timestamp\\\":\\\"2026-06-22T15:58:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Katherine May\\\",\\\"pageid\\\":78381298,\\\"size\\\":13588,\\\"wordcount\\\":1261,\\\"snippet\\\":\\\"Katherine May (born 18 September 1977), also writing as Katie May and Betty Herbert, is a British author and podcaster. Her writing includes memoirs (Wintering\\\",\\\"timestamp\\\":\\\"2026-09-01T10:20:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Taylor Dearden\\\",\\\"pageid\\\":55290719,\\\"size\\\":19195,\\\"wordcount\\\":1387,\\\"snippet\\\":\\\"com/watch?v=bqFkDmto2OM \\\"Actress Taylor Dearden talks about portraying\\nneurodivergence\\non 'The Pitt'\\\". NPR. April 9, 2025. Retrieved June 18, 2025. \\\"'The\\\",\\\"timestamp\\\":\\\"2026-09-15T00:35:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"The Devil Wears Prada 2\\\",\\\"pageid\\\":77315100,\\\"size\\\":87086,\\\"wordcount\\\":7289,\\\"snippet\\\":\\\"as a fashionable, striver in the fashion world with typical Gen Z\\nneurodivergency\\n.\\\" Although all the Italian actors who had provided the voices for the\\\",\\\"timestamp\\\":\\\"2026-09-21T23:51:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Other (philosophy)\\\",\\\"pageid\\\":972208,\\\"size\\\":49508,\\\"wordcount\\\":5797,\\\"snippet\\\":\\\"differences based on race, ethnicity, gender, sexual orientation, religion,\\nneurodivergence\\n, disability or any other marker of social identity. The process of\\\",\\\"timestamp\\\":\\\"2026-09-20T02:59:58Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"62691c3fb1424eda57d794d1cfb59efdc558af7278a78836f9bb11c545d263a4\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-e4b6cf6e06594c52",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurodivergence&format=json",
  "version": 3,
  "time": "2026-09-23T08:00:29.586643+00:00"
}
```

### `source-8655d5e9cbf24541`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":74319},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology\\\",\\\"pageid\\\":22921,\\\"size\\\":247095,\\\"wordcount\\\":26594,\\\"snippet\\\":\\\"\\nPsychology\\nis the scientific study of the mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious\\\",\\\"timestamp\\\":\\\"2026-09-05T20:21:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social psychology\\\",\\\"pageid\\\":26990,\\\"size\\\":69606,\\\"wordcount\\\":7452,\\\"snippet\\\":\\\"Social\\npsychology\\nis the methodical study of how thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others\\\",\\\"timestamp\\\":\\\"2026-09-10T09:14:19Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Filipino psychology\\\",\\\"pageid\\\":1465014,\\\"size\\\":20921,\\\"wordcount\\\":2815,\\\"snippet\\\":\\\"Filipino\\npsychology\\n, or Sikolohiyang Pilipino, in Filipino, is defined as the psychological and philosophical school rooted on the experience, ideas, and\\\",\\\"timestamp\\\":\\\"2026-04-25T13:24:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cognitive psychology\\\",\\\"pageid\\\":5961,\\\"size\\\":53010,\\\"wordcount\\\":6002,\\\"snippet\\\":\\\"Cognitive\\npsychology\\nis the scientific study of human mental processes such as attention, language use, memory, perception, problem solving, creativity\\\",\\\"timestamp\\\":\\\"2026-09-16T15:47:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Gestalt psychology\\\",\\\"pageid\\\":70402,\\\"size\\\":56035,\\\"wordcount\\\":6227,\\\"snippet\\\":\\\"Gestalt\\npsychology\\n, gestaltism, or configurationism is a school of\\npsychology\\n, and a theory of perception, that emphasizes psychologically processing\\\",\\\"timestamp\\\":\\\"2026-09-06T02:55:13Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Association (psychology)\\\",\\\"pageid\\\":62176483,\\\"size\\\":18373,\\\"wordcount\\\":2485,\\\"snippet\\\":\\\"Association in\\npsychology\\nrefers to a mental connection between concepts, events, or mental states that usually stems from specific experiences. Associations\\\",\\\"timestamp\\\":\\\"2026-06-14T14:11:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Somatic psychology\\\",\\\"pageid\\\":6774132,\\\"size\\\":16405,\\\"wordcount\\\":1855,\\\"snippet\\\":\\\"Somatic\\npsychology\\nor, more precisely, somatic clinical psychotherapy is a form of psychotherapy that focuses on somatic experience, including therapeutic\\\",\\\"timestamp\\\":\\\"2026-09-03T20:37:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Humanistic psychology\\\",\\\"pageid\\\":324180,\\\"size\\\":58187,\\\"wordcount\\\":6990,\\\"snippet\\\":\\\"Humanistic\\npsychology\\nis a psychological perspective that arose in the early- to mid-20th century in response to Sigmund Freud's psychoanalytic theory\\\",\\\"timestamp\\\":\\\"2026-08-08T17:40:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Positive psychology\\\",\\\"pageid\\\":179948,\\\"size\\\":125828,\\\"wordcount\\\":13672,\\\"snippet\\\":\\\"Positive\\npsychology\\nis the scientific study of conditions and processes that contribute to positive psychological states (e.g., contentment, joy), well-being\\\",\\\"timestamp\\\":\\\"2026-09-13T19:18:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Individual psychology\\\",\\\"pageid\\\":3959877,\\\"size\\\":15651,\\\"wordcount\\\":1631,\\\"snippet\\\":\\\"Individual\\npsychology\\n(German: Individualpsychologie) is a psychological method and school of thought founded by the Austrian psychiatrist Alfred Adler\\\",\\\"timestamp\\\":\\\"2026-05-04T05:18:04Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"b1b6953fea6b58e6d255af682add8052ad1cfbb78364a5046242be41ecb8d5e5\", \"verification_required\": true, \"topic_domain\": \"psychology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-8655d5e9cbf24541",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=psychology&format=json",
  "version": 3,
  "time": "2026-09-23T08:00:29.974056+00:00"
}
```

### `source-1b0cc7ee01224368`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4980},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":108090,\\\"wordcount\\\":6019,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-22T20:55:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"39a633c5507eec98f5f8cea2b237266ef61e075ee406bcd7a9c01d1537017bec\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-1b0cc7ee01224368",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 3,
  "time": "2026-09-23T08:00:30.405896+00:00"
}
```

### `source-a3fbbd244af74a16`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":7075},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mechanics\\\",\\\"pageid\\\":25202,\\\"size\\\":101544,\\\"wordcount\\\":12070,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\n, also known as\\nquantum\\nphysics, is the fundamental physical theory that describes the behavior of matter and of light; the behaviors\\\",\\\"timestamp\\\":\\\"2026-09-22T01:21:12Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of quantum mechanics\\\",\\\"pageid\\\":9067941,\\\"size\\\":78664,\\\"wordcount\\\":9389,\\\"snippet\\\":\\\"of\\nquantum\\nmechanics\\nis a fundamental part of the history of modern physics. The major chapters of this history begin with the emergence of\\nquantum\\nideas\\\",\\\"timestamp\\\":\\\"2026-08-31T07:22:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Introduction to quantum mechanics\\\",\\\"pageid\\\":2796131,\\\"size\\\":67491,\\\"wordcount\\\":7535,\\\"snippet\\\":\\\"\\nQuantum\\nmechanics\\nis the study of matter and matter's interactions with energy on the scale of atomic and subatomic particles. By contrast, classical\\\",\\\"timestamp\\\":\\\"2026-06-16T00:28:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Interpretations of quantum mechanics\\\",\\\"pageid\\\":54738,\\\"size\\\":70224,\\\"wordcount\\\":7757,\\\"snippet\\\":\\\"interpretation of\\nquantum\\nmechanics\\nis an attempt to explain how the mathematical theory of\\nquantum\\nmechanics\\nmight correspond to experienced reality.\\nQuantum\\nmechanics\\\",\\\"timestamp\\\":\\\"2026-09-07T03:03:00Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum superposition\\\",\\\"pageid\\\":82728,\\\"size\\\":19317,\\\"wordcount\\\":2576,\\\"snippet\\\":\\\"\\nQuantum\\nsuperposition is a fundamental principle of\\nquantum\\nmechanics\\nthat states that linear combinations of solutions to the Schr\\\\u00f6dinger equation are\\\",\\\"timestamp\\\":\\\"2026-06-12T23:26:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Measurement in quantum mechanics\\\",\\\"pageid\\\":573875,\\\"size\\\":68095,\\\"wordcount\\\":8384,\\\"snippet\\\":\\\"different interpretations of\\nquantum\\nmechanics\\n, concern of solving what is known as the measurement problem. In\\nquantum\\nmechanics\\n, each physical system is\\\",\\\"timestamp\\\":\\\"2026-08-09T04:56:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mathematical formulation of quantum mechanics\\\",\\\"pageid\\\":20728,\\\"size\\\":58208,\\\"wordcount\\\":7934,\\\"snippet\\\":\\\"mathematical formulations of\\nquantum\\nmechanics\\nare those mathematical formalisms that permit a rigorous description of\\nquantum\\nmechanics\\n. This mathematical formalism\\\",\\\"timestamp\\\":\\\"2026-09-05T15:19:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wave function\\\",\\\"pageid\\\":145343,\\\"size\\\":105363,\\\"wordcount\\\":14058,\\\"snippet\\\":\\\"In\\nquantum\\nmechanics\\n, a wave function (or wavefunction) is a mathematical description of the\\nquantum\\nstate of an isolated\\nquantum\\nsystem. The most common\\\",\\\"timestamp\\\":\\\"2026-07-11T05:48:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Quantum mysticism\\\",\\\"pageid\\\":4279149,\\\"size\\\":19729,\\\"wordcount\\\":1998,\\\"snippet\\\":\\\"the ideas of\\nquantum\\nmechanics\\nand its interpretations.\\nQuantum\\nmysticism is considered pseudoscience and quackery by\\nquantum\\nmechanics\\nexperts. Before\\\",\\\"timestamp\\\":\\\"2026-08-09T08:13:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Relational quantum mechanics\\\",\\\"pageid\\\":5974662,\\\"size\\\":47991,\\\"wordcount\\\":6972,\\\"snippet\\\":\\\"Relational\\nquantum\\nmechanics\\n(RQM) is an interpretation of\\nquantum\\nmechanics\\nwhich treats the state of a\\nquantum\\nsystem as being relational, that is,\\\",\\\"timestamp\\\":\\\"2026-06-20T09:48:35Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"608d46bd977d3c25017126cccc01d537e719d2d748bcd90bc8af16b836f2a5c3\", \"verification_required\": true, \"topic_domain\": \"quantum_mechanics\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-a3fbbd244af74a16",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=quantum+mechanics&format=json",
  "version": 3,
  "time": "2026-09-23T08:00:30.821727+00:00"
}
```

### `source-f750d6585f854e49`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1\", \"scope\": \"recursive source-controlled WAKE repository file index; paths and sizes, not file contents\", \"excerpt\": \"[{\\\"path\\\": \\\".env.example\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 83}, {\\\"path\\\": \\\".github/workflows/test.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1063}, {\\\"path\\\": \\\".github/workflows/wake.yml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4783}, {\\\"path\\\": \\\".gitignore\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 86}, {\\\"path\\\": \\\"LICENSE\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 34020}, {\\\"path\\\": \\\"README.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 19146}, {\\\"path\\\": \\\"assets/covers/cover-original.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2471510}, {\\\"path\\\": \\\"assets/covers/cover-variant-001.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3329007}, {\\\"path\\\": \\\"assets/covers/cover-variant-002.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3256389}, {\\\"path\\\": \\\"assets/covers/cover-variant-003.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3125985}, {\\\"path\\\": \\\"assets/covers/cover-variant-004.png\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2847631}, {\\\"path\\\": \\\"assets/playlists/Reality Bytes Playlist.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9999}, {\\\"path\\\": \\\"docs/architecture.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23070}, {\\\"path\\\": \\\"docs/cloud.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10146}, {\\\"path\\\": \\\"docs/experiment.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9733}, {\\\"path\\\": \\\"docs/operations.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6687}, {\\\"path\\\": \\\"docs/quota-map-implementation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7787}, {\\\"path\\\": \\\"docs/retrieval.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3475}, {\\\"path\\\": \\\"docs/validation.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2755}, {\\\"path\\\": \\\"examples/journal/events.jsonl\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1017120}, {\\\"path\\\": \\\"examples/journal/experiment.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 20205}, {\\\"path\\\": \\\"examples/journal/head.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 65}, {\\\"path\\\": \\\"examples/journal/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1266448}, {\\\"path\\\": \\\"examples/journal/journal.md\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 33437}, {\\\"path\\\": \\\"examples/journal/state.json\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 199768}, {\\\"path\\\": \\\"pyproject.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 662}, {\\\"path\\\": \\\"requirements.txt\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 68}, {\\\"path\\\": \\\"research-topics.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1441}, {\\\"path\\\": \\\"scripts/archive-analysis-snapshot.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3850}, {\\\"path\\\": \\\"scripts/checkpoint-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2693}, {\\\"path\\\": \\\"scripts/covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2093}, {\\\"path\\\": \\\"scripts/github_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9899}, {\\\"path\\\": \\\"scripts/install_cron.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1560}, {\\\"path\\\": \\\"scripts/manual-model-wake.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8257}, {\\\"path\\\": \\\"scripts/package.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1207}, {\\\"path\\\": \\\"scripts/publish.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 6865}, {\\\"path\\\": \\\"scripts/run-wake-cycles.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8474}, {\\\"path\\\": \\\"scripts/scheduled_wake.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1218}, {\\\"path\\\": \\\"scripts/sync-cloud-state.sh\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2131}, {\\\"path\\\": \\\"tests/test_acquisition.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5530}, {\\\"path\\\": \\\"tests/test_alt_hosts.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2552}, {\\\"path\\\": \\\"tests/test_cloud_workflow.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18678}, {\\\"path\\\": \\\"tests/test_covers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2879}, {\\\"path\\\": \\\"tests/test_editorial_corrections.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7432}, {\\\"path\\\": \\\"tests/test_experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3981}, {\\\"path\\\": \\\"tests/test_feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8276}, {\\\"path\\\": \\\"tests/test_gemini_failover.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14594}, {\\\"path\\\": \\\"tests/test_history_filter.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 554}, {\\\"path\\\": \\\"tests/test_observation_mode.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2089}, {\\\"path\\\": \\\"tests/test_provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8429}, {\\\"path\\\": \\\"tests/test_publishing.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4612}, {\\\"path\\\": \\\"tests/test_rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4751}, {\\\"path\\\": \\\"tests/test_research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 49884}, {\\\"path\\\": \\\"tests/test_squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4839}, {\\\"path\\\": \\\"tests/test_status.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4452}, {\\\"path\\\": \\\"tests/test_system.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 30253}, {\\\"path\\\": \\\"wake.toml\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2005}, {\\\"path\\\": \\\"wake/__init__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 789}, {\\\"path\\\": \\\"wake/__main__.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13230}, {\\\"path\\\": \\\"wake/assets/app.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50487}, {\\\"path\\\": \\\"wake/assets/data-view.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1551}, {\\\"path\\\": \\\"wake/assets/help.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9578}, {\\\"path\\\": \\\"wake/assets/index.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 13072}, {\\\"path\\\": \\\"wake/assets/map.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 14055}, {\\\"path\\\": \\\"wake/assets/map.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4505}, {\\\"path\\\": \\\"wake/assets/map.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15252}, {\\\"path\\\": \\\"wake/assets/map3d.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 12562}, {\\\"path\\\": \\\"wake/assets/map3d.html\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5271}, {\\\"path\\\": \\\"wake/assets/map3d.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 18236}, {\\\"path\\\": \\\"wake/assets/nav.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 3039}, {\\\"path\\\": \\\"wake/assets/nav.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 1250}, {\\\"path\\\": \\\"wake/assets/pet.js\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 15408}, {\\\"path\\\": \\\"wake/assets/style.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 96915}, {\\\"path\\\": \\\"wake/assets/theme.css\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10846}, {\\\"path\\\": \\\"wake/audit.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 2259}, {\\\"path\\\": \\\"wake/engine.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 63931}, {\\\"path\\\": \\\"wake/experiment.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 9323}, {\\\"path\\\": \\\"wake/experimental.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4136}, {\\\"path\\\": \\\"wake/feeds.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 8221}, {\\\"path\\\": \\\"wake/governance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 56521}, {\\\"path\\\": \\\"wake/provenance.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 11826}, {\\\"path\\\": \\\"wake/providers.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 50319}, {\\\"path\\\": \\\"wake/rejected.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 10822}, {\\\"path\\\": \\\"wake/report.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 46764}, {\\\"path\\\": \\\"wake/research.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 29446}, {\\\"path\\\": \\\"wake/retrieval.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 7430}, {\\\"path\\\": \\\"wake/scheduling.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5332}, {\\\"path\\\": \\\"wake/squirrel.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 5888}, {\\\"path\\\": \\\"wake/store.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 23255}, {\\\"path\\\": \\\"wake/trust.py\\\", \\\"type\\\": \\\"blob\\\", \\\"size\\\": 4060}]\", \"excerpt_truncated\": false, \"source_sha256\": \"3e08adc5839ca94e53e56b2414738131f7a3b17a6db55ecd375979ee4ac8ac25\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\", \"evidence_role\": \"source\", \"host_tier\": \"verification\", \"persistent_identifiers\": []}",
  "id": "source-f750d6585f854e49",
  "scope": "collected",
  "source": "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
  "version": 3,
  "time": "2026-09-23T08:00:30.994303+00:00"
}
```

### `r-522db193932148c2`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":3,\"inherited_commitments\":[\"review_thermo_foundations_sources\"],\"invocation\":\"w-522db193932148c2\",\"previous_head\":\"e256b4d3598c22635fc16248cbbd559f289204e6f4101c6c8182ac5ff1b16604\",\"process_id\":2233,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-522db193932148c2",
  "source": "runtime:continuity",
  "version": 3,
  "time": "2026-09-23T08:00:31.066021+00:00"
}
```

## Journal

### 001 · Establishing Information Thermodynamics Project

```json
{
  "cycle": 1,
  "invocation": "w-16c4ac30ac534d8c",
  "title": "Establishing Information Thermodynamics Project",
  "summary": "We are initiating our first research project under the information_thermodynamics topic, focusing on the historical and mathematical overlap between thermodynamic entropy and Shannon information theory."
}
```

### 002 · Information Thermodynamics: Research Strategy and Gap Assessment

```json
{
  "cycle": 2,
  "invocation": "w-aff3bfb6eae048aa",
  "title": "Information Thermodynamics: Research Strategy and Gap Assessment",
  "summary": "We are progressing the 'Foundations of Information Thermodynamics' project. Our initial attempt to locate specific research on Nicole Yunger Halpern failed, and our existing collected evidence repository contains irrelevant data (general Wikipedia search results and repository metadata) that cannot support a notebook on the formal equivalence of Shannon and thermodynamic entropy. We must perform focused research to gather eligible sources on Landauer's principle and entropy equivalence before we can fulfill our pending commitment. We will prioritize this research in the current cycle."
}
```

### 003 · Resetting Research on Entropy Equivalence

```json
{
  "cycle": 3,
  "invocation": "w-03c9df8165bb430a",
  "title": "Resetting Research on Entropy Equivalence",
  "summary": "We are continuing the 'Foundations of Information Thermodynamics' project. Our previous research steps failed to retrieve relevant sources on Shannon and thermodynamic entropy; the collected evidence is irrelevant to the project's question. We are initiating fresh, targeted searches for authoritative sources to build a credible evidence base."
}
```

## Research

### `search_yunger_halpern_thermo`

```json
{
  "domain": "information_thermodynamics",
  "id": "search_yunger_halpern_thermo",
  "project": "info_thermo_foundations",
  "query": "Nicole Yunger Halpern quantum information thermodynamics",
  "reason": "To retrieve specific publications by Nicole Yunger Halpern, who is listed in the initial search index and works at the intersection of quantum information and thermodynamics.",
  "type": "research",
  "status": "failed",
  "created_by": "w-16c4ac30ac534d8c",
  "evidence": "source-714fee674f314ca6"
}
```

### `search_landauer_entropy_foundations`

```json
{
  "domain": "information_thermodynamics",
  "id": "search_landauer_entropy_foundations",
  "project": "info_thermo_foundations",
  "query": "Landauer's principle Shannon thermodynamic entropy equivalence physical limits",
  "reason": "Our existing collected evidence is insufficient for the project's question. We need credible, relevant sources on the connection between information and thermodynamics to fulfill our commitments and draft a notebook.",
  "type": "research",
  "status": "collected",
  "created_by": "w-aff3bfb6eae048aa",
  "evidence": "source-05d140a6d98048c7"
}
```

### `search_shannon_thermo_equivalence_formal`

```json
{
  "domain": "information_thermodynamics",
  "id": "search_shannon_thermo_equivalence_formal",
  "project": "info_thermo_foundations",
  "query": "Shannon entropy thermodynamic entropy mathematical equivalence landauer principle",
  "reason": "We must replace our current irrelevant evidence (Wikipedia consciousness and GitHub index) with peer-reviewed or authoritative academic sources that explicitly discuss the formal mathematical relationship between information-theoretic and thermodynamic entropy.",
  "type": "research",
  "status": "collected",
  "created_by": "w-03c9df8165bb430a",
  "evidence": "source-ee8292ee56af4b72"
}
```

### `search_landauer_principle_physical_limits`

```json
{
  "domain": "information_thermodynamics",
  "id": "search_landauer_principle_physical_limits",
  "project": "info_thermo_foundations",
  "query": "Landauer principle physical limits information processing thermodynamic cost",
  "reason": "This search targets the second half of our project question regarding the physical limits of information processing, which is central to the project's scope.",
  "type": "research",
  "status": "failed",
  "created_by": "w-03c9df8165bb430a",
  "evidence": "source-d7d1f0ad961e4631"
}
```

## Blog posts

_None recorded._
