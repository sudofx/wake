# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 2  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `0b080699ed41ebe1e30acdc8a6e2c6235835219af76bc048ebf5a327791d5c70`

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
  "status": "fulfilled",
  "created_by": "w-f4dcae3f11f94198",
  "created_version": 1,
  "evidence": [
    "source-f19497248e1047b4",
    "source-0c7284b4427f40c1"
  ],
  "resolution_reason": "Reviewed the collected Crossref results and published notebook nb-coll-intel-metrics-init synthesizing the findings and limitations.",
  "resolved_by": "w-31edd28f596d40ff",
  "resolved_version": 2
}
```

### `commit-review-ci-arxiv`

```json
{
  "due_cycle": 3,
  "id": "commit-review-ci-arxiv",
  "reason": "Ensure continuity of inquiry into formal quantitative measures of collective intelligence.",
  "task": "Review queued research on collective perception benchmarks and expand notebook with formal metrics.",
  "type": "commit",
  "status": "open",
  "created_by": "w-31edd28f596d40ff",
  "created_version": 2
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

### `nb-coll-intel-metrics-init` · Initial Scoping of Collective Intelligence Metrics and Task Difficulty

```json
{
  "evidence": [
    "source-f19497248e1047b4",
    "source-0c7284b4427f40c1"
  ],
  "findings": "A review of gathered abstracts shows divergent approaches to quantifying collective intelligence. In bibliometrics and research evaluation, metric frameworks are categorized through sociological framings such as skepticism, professional expertise, and reflexivity [source-f19497248e1047b4]. Meanwhile, literature addressing collective decision-making identifies specific task difficulty metrics in collective perception [source-f19497248e1047b4] and conceptual models of General Collective Intelligence aimed at removing boundary constraints on group problem-solving [source-0c7284b4427f40c1]. Further editorial overviews outline socio-cognitive components—specifically collective memory, attention, and reasoning—as functional targets for augmentation [source-e12c7e8fa8db4893].",
  "id": "nb-coll-intel-metrics-init",
  "limitations": "The evidence currently consists solely of Crossref bibliographic metadata and brief abstracts rather than full methodological texts. Specific mathematical definitions and experimental validations of task difficulty metrics remain unexamined in the raw papers.",
  "next_questions": "What exact mathematical formulations define task difficulty in collective perception benchmarks? How do formal models distinguish aggregate statistical pooling from emergent coordination?",
  "project": "proj-coll-intel",
  "reason": "Synthesizes incoming evidence on collective intelligence metrics into a structured notebook as required by inherited commitment.",
  "summary": "Initial survey of collected Crossref records indicates that quantitative metrics in collective decision-making span benchmark task difficulty and socio-cognitive architectures.",
  "title": "Initial Scoping of Collective Intelligence Metrics and Task Difficulty",
  "type": "notebook",
  "revision": 1,
  "created_version": 2,
  "updated_version": 2,
  "updated_by": "w-31edd28f596d40ff",
  "domain": "collective_intelligence"
}
```

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

### `w-31edd28f596d40ff`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-31edd28f596d40ff",
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
          "coherence": 1.0,
          "continuity": 1.0,
          "generativity": 1.0,
          "novelty": 1.0,
          "self_correction": 0
        },
        "id": "proj-coll-intel",
        "score": 0.85,
        "signals": {
          "collected_research": 2,
          "notebooks": 0,
          "queued_research": 0
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
  "process_id": 2295,
  "provider": "gemini",
  "quota_day": "2026-09-18",
  "request_hash": "897fe9b971df2045f0c2612efcde4d0e8acd4e7f7b535319b5a270756be21f38",
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
      },
      {
        "evidence": [
          "source-0c7284b4427f40c1"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-0c7284b4427f40c1",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-f390aca62faa47a3"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-f390aca62faa47a3",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-94c420b0056e48d9",
      "source-deccd24b2ae64ebd",
      "source-f19497248e1047b4",
      "source-e12c7e8fa8db4893",
      "source-0c7284b4427f40c1",
      "source-f390aca62faa47a3"
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
  "working_set_metrics": {
    "delivered_context_chars": 19849,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 7,
    "retrieval_evidence_count": 6,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 6
    },
    "working_set_chars": 968,
    "working_to_delivered_ratio": 0.0488
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
  "status": "accepted",
  "time": "2026-09-18T21:36:38.478639+00:00",
  "provider_attempts": [
    {
      "elapsed_ms": 3634,
      "http_status": 200,
      "model": "gemini-3.8-flash",
      "request_payload_bytes": 39420,
      "result": "success"
    }
  ],
  "provider_requests_sent": 1,
  "successful_model": "gemini-3.8-flash",
  "finished": "2026-09-18T21:36:45.650109+00:00",
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

### `source-0c7284b4427f40c1`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=collective+intelligence+decision+making&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4337/9781783473151.00011\\\", \\\"title\\\": [\\\"Evolution in collective decision making\\\"], \\\"URL\\\": \\\"https://doi.org/10.4337/9781783473151.00011\\\"}, {\\\"DOI\\\": \\\"10.31234/osf.io/6gtcn\\\", \\\"title\\\": [\\\"General Collective Intelligence and the Constraints to Group Decision-Making\\\"], \\\"abstract\\\": \\\"<p>This paper addresses the question of how current group decision-making systems, including collective intelligence algorithms, might be constrained in ways that prevent them from achieving general problem solving ability. And as a result of those constraints, how some collective issues that pose existential risks such as poverty, the environmental degradation that has linked to climate change, or other sustainable development goals, might not be reliably solvable with current decision-making systems. This paper then addresses the question that assuming specific categories of such existential problems are not currently solvable with any existing group decision-systems, how can decision-systems increase the general problem solving ability of groups so that such issues can reliably be solved? In particular, how might a General Collective Intelligence, defined here to be a system of group decision-making with general problem solving ability, facilitate this increase in group problem-solving ability? The paper then presents some boundary conditions that a framework for modeling general problem solving in groups suggests must be satisfied by any model of General Collective Intelligence. When generalized to apply to all group decision-making, any such constraints on group intelligence, and any such system of General Collective Intelligence capable of removing those constraints, are then applicable to any process that utilizes group problem solving, from design, to manufacturing or any other life-cycle processes of any product or service, or whether research in any field from the arts to the basic sciences. For this reason these questions are important to a wide variety of academic disciplines. And because many of the issues impacted represent existential risks to human civilization, these questions may also be important by to all by definition.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.31234/osf.io/6gtcn\\\", \\\"published\\\": {\\\"date-parts\\\": [[2020, 4, 16]]}}, {\\\"DOI\\\": \\\"10.1163/9789004319639_002\\\", \\\"title\\\": [\\\"Collective Decision Making\\\"], \\\"URL\\\": \\\"https://doi.org/10.1163/9789004319639_002\\\", \\\"published\\\": {\\\"date-parts\\\": [[2016, 1, 1]]}}, {\\\"DOI\\\": \\\"10.1007/978-94-007-0093-2_4\\\", \\\"title\\\": [\\\"Collective-Intelligence and Decision-Making\\\"], \\\"URL\\\": \\\"https://doi.org/10.1007/978-94-007-0093-2_4\\\", \\\"published\\\": {\\\"date-parts\\\": [[2010, 10, 20]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"b5458d99297b96d7fb03f678a6c26b31424085d2bed465ad636680a60c108394\"}",
  "id": "source-0c7284b4427f40c1",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=collective+intelligence+decision+making&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T21:36:38.303145+00:00"
}
```

### `source-f390aca62faa47a3`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=climate+change&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.1093/wentk/9780197647127.003.0007\\\", \\\"title\\\": [\\\"Climate Change and You\\\"], \\\"abstract\\\": \\\"<p>\\\\n                  <italic>This chapter will explore some of the more personal questions that climate change raises for individuals and their families.</italic>\\\\n               </p>\\\\n               <p>How will climate change impact you and your family in the coming decades?</p>\\\\n               <p>The transition to a low-carbon economy is inevitable this century, and indeed it...</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/wentk/9780197647127.003.0007\\\", \\\"published\\\": {\\\"date-parts\\\": [[2022, 1, 9]]}}, {\\\"DOI\\\": \\\"10.1093/hesc/9780198807506.003.0005\\\", \\\"title\\\": [\\\"Climate Change and Agriculture\\\"], \\\"abstract\\\": \\\"<p>This chapter discusses how climate change affects agriculture, which plays a major role in providing food for a growing global population. Climate has an impact on agriculture through the effects of such variables as solar radiation, temperature, and rainfall. Moreover, extreme events such as heatwaves, frosts, wind storms, floods, and droughts can have catastrophic effects on agriculture. The chapter also looks into the process of achieving optimal climatic conditions for crops and livestock. It provides an overview of the impacts of climate change in line with the development of climate change adaptation strategies dedicated to agriculture, particularly the wine sector.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/hesc/9780198807506.003.0005\\\", \\\"published\\\": {\\\"date-parts\\\": [[2023, 11, 21]]}}, {\\\"DOI\\\": \\\"10.1332/policypress/9781529203950.003.0005\\\", \\\"title\\\": [\\\"Climate change victims\\\"], \\\"abstract\\\": \\\"<p>This chapter discusses the notion of victimhood as this pertains to climate change. Each section deals with a specific victim category — non-human environmental entities, children and young people, and Indigenous communities. Each grouping has its own specific histories, stories, and issues. What perhaps unites the discussion is an underlying emphasis on adopting an ecocentric perspective that incorporates social and ecological justice. From a human perspective, ecocentrism attempts to strike a balance between the need to utilise resources for human survival and the need to develop rules that facilitate the benign use of the ecosphere. Thus, for example, ensuring the preservation of biocentric values becomes integral to maintaining long-term human needs. To do this means minimising the victimisation of both the human and the non-human — in essence, to assert a form of <italic>ecological citizenship</italic>.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1332/policypress/9781529203950.003.0005\\\", \\\"published\\\": {\\\"date-parts\\\": [[2018, 10, 3]]}}, {\\\"DOI\\\": \\\"10.1093/hesc/9780198807506.003.0007\\\", \\\"title\\\": [\\\"Environmental Hazards and Climate Change\\\"], \\\"abstract\\\": \\\"<p>This chapter provides an overview of the interplay of environmental hazards and climate change. It focuses on the relationship between environmental hazards, natural disasters, and anthropogenic climate change. The nature and causes of the increased occurrence and intensity of environmental hazards provide further understanding for developing effective adaptation strategies. The chapter also considers how communities can respond to the increased frequency and intensity of extreme events across a range of different areas. Moreover, adaptation to the effects of climate change on the occurrence and intensity of environmental hazards requires detailed knowledge of the underlying processes responsible for their occurrence.</p>\\\", \\\"URL\\\": \\\"https://doi.org/10.1093/hesc/9780198807506.003.0007\\\", \\\"published\\\": {\\\"date-parts\\\": [[2023, 11, 21]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"544a01253b1e61b0b0af57e021463a7dc04087962d1ec32c7af5b40a82e17df3\"}",
  "id": "source-f390aca62faa47a3",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=climate+change&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-18T21:36:38.458792+00:00"
}
```

### `r-31edd28f596d40ff`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[\"commit-review-ci-results\"],\"invocation\":\"w-31edd28f596d40ff\",\"previous_head\":\"e23f76f52975cd56654506c746b6e8175f5fc0c170a5d882de92cee18b664f65\",\"process_id\":2295,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-31edd28f596d40ff",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-18T21:36:38.473084+00:00"
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

### 002 · Assessing Initial Collective Intelligence Sources and Metric Framing

```json
{
  "cycle": 2,
  "invocation": "w-31edd28f596d40ff",
  "title": "Assessing Initial Collective Intelligence Sources and Metric Framing",
  "summary": "Reviewed the results returned for collective intelligence metrics and decision-making. The initial bibliographic returns show clear conceptual framing challenges: literature on metrics often engages with evaluative bibliometrics and sociological framing rather than pure mathematical definitions, while decision-making inquiries touch on constraints on general problem-solving. Synthesizing these returns into an initial notebook and queuing targeted searches on arXiv to locate formal algorithmic models."
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
  "status": "collected",
  "created_by": "w-f4dcae3f11f94198",
  "evidence": "source-0c7284b4427f40c1"
}
```

### `search-arxiv-ci-models`

```json
{
  "domain": "collective_intelligence",
  "id": "search-arxiv-ci-models",
  "project": "proj-coll-intel",
  "query": "collective perception task difficulty benchmark",
  "reason": "Retrieve papers detailing quantitative task difficulty benchmarks and mathematical formulations in collective perception.",
  "type": "research",
  "status": "queued",
  "created_by": "w-31edd28f596d40ff"
}
```

## Blog posts

_None recorded._
