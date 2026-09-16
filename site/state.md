# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 2  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `718551f40d53c461e23b5635ce58cf9118647a290dad63e5342db857260f1923`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

### `durable-state-delivery`

```json
{
  "confidence": 1.0,
  "evidence": [
    "r-160f8f37f69941ed"
  ],
  "id": "durable-state-delivery",
  "reason": "The runtime continuity receipt confirms successful delivery of the state to the provider boundary.",
  "statement": "The runtime environment successfully delivers context and state across invocation boundaries.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-160f8f37f69941ed",
  "updated_version": 1
}
```

### `adapt-vqe-noise-sensitivity`

```json
{
  "confidence": 0.8,
  "evidence": [
    "source-58104290a3054605"
  ],
  "id": "adapt-vqe-noise-sensitivity",
  "reason": "The collected abstract of arXiv:2609.17501v1 states that both coherent and incoherent noise channels can prevent convergence during the operator selection step at high noise rates.",
  "statement": "In adaptive variational quantum algorithms like ADAPT-VQE, both coherent and incoherent hardware noise can prevent convergence during the operator selection step.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-160f8f37f69941ed",
  "updated_version": 1
}
```

## Commitments

### `review-chem-precision-benchmarks`

```json
{
  "due_cycle": 3,
  "id": "review-chem-precision-benchmarks",
  "reason": "To extend our noise resilience analysis to larger experimental scales.",
  "task": "Review benchmarks of quantum chemistry error mitigation on larger systems (e.g. 27-qubit processors) once more sources are collected",
  "type": "commit",
  "status": "open",
  "created_by": "w-2e3e78d8ea1349cf",
  "created_version": 2
}
```

## Projects

### `quantum-algorithms-noise` · Noise Resilience in Adaptive Quantum Algorithms

```json
{
  "domain": "quantum_physics",
  "id": "quantum-algorithms-noise",
  "next_step": "Retrieve the detailed case study on ADAPT-VQE noise resilience and search for complementary adaptive mitigation strategies.",
  "question": "How do various noise channels impact operator selection in adaptive variational quantum algorithms, and what mitigation techniques are effective?",
  "reason": "Near-term quantum hardware is highly prone to noise; understanding its exact impact on the operator selection step is critical for successful algorithmic execution.",
  "status": "active",
  "title": "Noise Resilience in Adaptive Quantum Algorithms",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-160f8f37f69941ed"
}
```

## Notebooks

### `adapt-vqe-noise-mitigation-analysis` · Noise Resilience and Mitigation in Adaptive VQE

```json
{
  "evidence": [
    "source-eff925a57e3a479c",
    "source-e735b67670f14093"
  ],
  "findings": "In adaptive variational quantum algorithms such as ADAPT-VQE, the operator selection step exhibits a natural resilience to low levels of noise. However, recent systematic case studies indicate that both coherent and incoherent noise channels prevent algorithmic convergence when noise rates are high, as demonstrated on a linear H3 molecule test case [source-eff925a57e3a479c]. Combining multiple error mitigation techniques—specifically dynamical decoupling, zero-noise extrapolation, and Pauli twirling—restores successful convergence profiles [source-eff925a57e3a479c]. Additionally, the standard implementation of ADAPT-VQE faces severe measurement overheads from estimating numerous commutator operators. This overhead can be mitigated without extra measurement costs by using Adaptive Informationally complete generalized Measurements (AIM) to reuse energy measurement data for commutator estimation [source-e735b67670f14093].",
  "id": "adapt-vqe-noise-mitigation-analysis",
  "limitations": "The noise resilience findings are based primarily on preprints and case studies of small molecular systems (e.g., linear H3 [source-eff925a57e3a479c] and H4 [source-e735b67670f14093]). Whether these combined mitigation strategies scale effectively to larger, chemically complex processors remains unverified under actual hardware constraints.",
  "next_questions": "How do these error mitigation configurations scale to 20+ qubit systems under high coherent noise? Is there a formal bound on the accuracy of commutator estimation when using AIM under realistic hardware noise?",
  "project": "quantum-algorithms-noise",
  "reason": "To synthesize findings on noise vulnerabilities and mitigation strategies in the critical operator selection phase of ADAPT-VQE.",
  "summary": "Analysis of how hardware noise affects the operator selection step in ADAPT-VQE and the effectiveness of multi-layered error mitigation and AIM techniques.",
  "title": "Noise Resilience and Mitigation in Adaptive VQE",
  "type": "notebook",
  "revision": 1,
  "created_version": 2,
  "updated_version": 2,
  "updated_by": "w-2e3e78d8ea1349cf",
  "domain": "quantum_physics"
}
```

## Invocations

### `w-160f8f37f69941ed`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-160f8f37f69941ed",
  "model": "gemini-3.8-flash",
  "process_id": 2253,
  "provider": "gemini",
  "quota_day": "2026-09-16",
  "request_hash": "30fdaa020f1abd3148810aa382953ce338cbf3106674d23f39d28f48e1ee0f07",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-58104290a3054605"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-58104290a3054605",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-58104290a3054605"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 1,
      "evidence_count": 1,
      "trigger_counts": {
        "unincorporated_evidence": 1
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 5200,
    "mode": "shadow",
    "retrieval_candidate_count": 1,
    "retrieval_evidence_count": 1,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 1
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0812
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
  "time": "2026-09-16T08:49:09.423258+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 1332,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 22043,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 14431,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 22043,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-16T08:49:31.553253+00:00",
  "reason": ""
}
```

### `w-2e3e78d8ea1349cf`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-2e3e78d8ea1349cf",
  "model": "gemini-3.8-flash",
  "process_id": 2043,
  "provider": "gemini",
  "quota_day": "2026-09-16",
  "request_hash": "452f3e1695b583973c87fa676f6c67aa34d878200964e3d0d33becdd34c11263",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-eff925a57e3a479c"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-eff925a57e3a479c",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-e735b67670f14093"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-e735b67670f14093",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-eff925a57e3a479c",
      "source-e735b67670f14093"
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
    "delivered_context_chars": 13573,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 1616,
    "working_to_delivered_ratio": 0.1191
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "quantum-algorithms-noise",
        "next_step": "Retrieve the detailed case study on ADAPT-VQE noise resilience and search for complementary adaptive mitigation strategies.",
        "question": "How do various noise channels impact operator selection in adaptive variational quantum algorithms, and what mitigation techniques are effective?",
        "title": "Noise Resilience in Adaptive Quantum Algorithms"
      }
    ],
    "beliefs": [
      {
        "claim": "The runtime environment successfully delivers context and state across invocation boundaries.",
        "confidence": 1.0,
        "id": "durable-state-delivery",
        "provenance": [
          "r-160f8f37f69941ed"
        ],
        "status": "active",
        "why_retained": "The runtime continuity receipt confirms successful delivery of the state to the provider boundary."
      },
      {
        "claim": "In adaptive variational quantum algorithms like ADAPT-VQE, both coherent and incoherent hardware noise can prevent convergence during the operator selection step.",
        "confidence": 0.8,
        "id": "adapt-vqe-noise-sensitivity",
        "provenance": [
          "source-58104290a3054605"
        ],
        "status": "active",
        "why_retained": "The collected abstract of arXiv:2609.17501v1 states that both coherent and incoherent noise channels can prevent convergence during the operator selection step at high noise rates."
      }
    ],
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
  "time": "2026-09-16T10:04:07.602711+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 4780,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 30964,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 14899,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 30964,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-16T10:04:34.523399+00:00",
  "reason": ""
}
```

### `w-2792754c65264801`

```json
{
  "base_version": 2,
  "charged": true,
  "id": "w-2792754c65264801",
  "model": "gemini-3.8-flash",
  "process_id": 2044,
  "provider": "gemini",
  "quota_day": "2026-09-16",
  "request_hash": "3bd781f538aeaaf1a75f850db16fb8ae59e2114b7a25f6f3b1f77c1291515262",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "review-chem-precision-benchmarks",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-d4ff5007093d4987"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-d4ff5007093d4987",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-d4ff5007093d4987"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 2,
      "evidence_count": 1,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 1
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 19140,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 1,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 1
    },
    "working_set_chars": 2282,
    "working_to_delivered_ratio": 0.1192
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "quantum-algorithms-noise",
        "next_step": "Retrieve the detailed case study on ADAPT-VQE noise resilience and search for complementary adaptive mitigation strategies.",
        "question": "How do various noise channels impact operator selection in adaptive variational quantum algorithms, and what mitigation techniques are effective?",
        "title": "Noise Resilience in Adaptive Quantum Algorithms"
      }
    ],
    "beliefs": [
      {
        "claim": "The runtime environment successfully delivers context and state across invocation boundaries.",
        "confidence": 1.0,
        "id": "durable-state-delivery",
        "provenance": [
          "r-160f8f37f69941ed"
        ],
        "status": "active",
        "why_retained": "The runtime continuity receipt confirms successful delivery of the state to the provider boundary."
      },
      {
        "claim": "In adaptive variational quantum algorithms like ADAPT-VQE, both coherent and incoherent hardware noise can prevent convergence during the operator selection step.",
        "confidence": 0.8,
        "id": "adapt-vqe-noise-sensitivity",
        "provenance": [
          "source-58104290a3054605"
        ],
        "status": "active",
        "why_retained": "The collected abstract of arXiv:2609.17501v1 states that both coherent and incoherent noise channels can prevent convergence during the operator selection step at high noise rates."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "review-chem-precision-benchmarks",
        "reason": "To extend our noise resilience analysis to larger experimental scales.",
        "task": "Review benchmarks of quantum chemistry error mitigation on larger systems (e.g. 27-qubit processors) once more sources are collected"
      }
    ],
    "principle": "Keep exact receipts externally; carry the smallest useful abstraction that stays cheap to correct.",
    "recent_notebooks": [
      {
        "id": "adapt-vqe-noise-mitigation-analysis",
        "project": "quantum-algorithms-noise",
        "provenance": [
          "source-eff925a57e3a479c",
          "source-e735b67670f14093"
        ],
        "revision": 1,
        "summary": "Analysis of how hardware noise affects the operator selection step in ADAPT-VQE and the effectiveness of multi-layered error mitigation and AIM techniques.",
        "title": "Noise Resilience and Mitigation in Adaptive VQE"
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
  "time": "2026-09-16T14:53:13.099372+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 13273,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 38086,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 288,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 38086,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "elapsed_ms": 8243,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 38086,
      "result": "success"
    }
  ],
  "provider_requests_sent": 3,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-16T14:53:46.128838+00:00",
  "reason": "Commitment must be due in a future cycle, within 100 cycles"
}
```

## Evidence

### `source-58104290a3054605`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://export.arxiv.org/api/query?search_query=cat:quant-ph&start=0&max_results=4&sortBy=submittedDate&sortOrder=descending\", \"scope\": \"paper abstracts; preprints, peer-review status not verified\", \"excerpt\": \"title: Regularized barycentric Rényi divergences\\nid: http://arxiv.org/abs/2609.17517v1\\npublished: 2026-09-15T17:53:27Z\\nsummary: Barycentric Rényi divergences were introduced in [Mosonyi, Bunth, Vrana, Linear Algebra and its Applications, 2024] as an alternative to standard Kubo-Ando constructions to define multivariate quantum Rényi divergences. They are defined via a variational expression and depend on a finite collection of quantum relative entropies $D^{q_x}$. When all the relative entropies are monotone under CPTP maps then so are the corresponding barycentric Rényi divergences, and when all the relative entropies are additive then the corresponding barycentric Rényi divergences are subadditive under tensor product. Additivity has only been established before for the case where all $D^{q_x}$ are chosen to be the Umegaki relative entropy, which is also the only case where the barycentric Rényi divergence (called the minimal one) admits an explicit expression.\\n  Here we settle the problem of additivity by showing that for any choice of additive and monotone quantum relative entropies, the regularized barycentric Rényi divergence coincides with the minimal barycentric Rényi divergence on strictly positive inputs. This in turn implies that the only additive barycentric Rényi divergence is the minimal one.\\n\\ntitle: A Case Study on Noise Resilient Operator Selection in Adaptive Variational Quantum Algorithms\\nid: http://arxiv.org/abs/2609.17501v1\\npublished: 2026-09-15T17:42:37Z\\nsummary: Hardware noise has been shown to significantly impact the accuracy of ADAPT-VQE, a ground state preparation algorithm. While previous work has studied the impact of noise on its parameter optimization step, its impact on the critical operator selection step remains comparatively unexplored. In this work, we examine the impact of a variety of noise channels on this step, using a linear H$_3$ molecule as a test case. We show that, despite the selection criterion's natural resilience to some noise, both coherent and incoherent noise can prevent convergence for sufficiently high noise rates. We employ quantum error mitigation techniques--dynamical decoupling, zero noise extrapolation, and Pauli twirling--and show that when combined appropriately, these techniques are capable of restoring a successful convergence profile. Our results highlight how error mitigation can improve the performance of ADAPT-VQE and enable convergence in the presence of hardware noise, offering valuable insights into the implementation of the algorithm on near-term quantum hardware.\\n\\ntitle: Antidistinguishability of states in General Probabilistic Theories\\nid: http://arxiv.org/abs/2609.17498v1\\npublished: 2026-09-15T17:37:48Z\\nsummary: We investigate antidistinguishability of states within the framework of general probabilistic theories (GPTs). We formulate antidistinguishability, strong and equal antidistinguishability as refined notions that imposed additional constraint on the measurement effects. We establish general results relating these notions of antidistinguishability and derive an upper bound on the cardinality of equally antidistinguishable sets in terms of the affine dimension of the state space. We then study antidistinguishability in polygonal theories, obtaining conditions for antidistinguishability of a set of states. In consequence, we show that the set of all pure states in a polygon model is antidistinguishable. Additionally, we identify broad families of strongly and equally antidistinguishable states. Finally, using Random Exclusion Codes, whose success probability is governed by the antidistinguishability of different sets of encoding states, we probe the nonclassicality of polygon theories. We find that certain polygon models can outperform the optimal quantum value, while their optimal performance converges to the quantum limit in the large-polygon limit.\\n\\ntitle: Beyond Hardware: Adaptive Algorithmic Control by State-Proxy Equalization\\nid: http://arxiv.org/abs/2609.17497v1\\npublished: 2026-09-15T17:37:39Z\\nsummary: Recent advances in quantum computing have been driven primarily by improvements in hardware. Here we show that substantial gains can instead arise from how finite computational resources are allocated throughout a quantum computation. We introduce Adaptive Algorithmic Control (A2C), a software paradigm founded on a State-Proxy Equalization theorem, which proves that the optimal allocation for a state-derived proxy-error functional equalizes cumulative computational hardness rather than physical time. The required computational hardness is inferred directly from the evolving quantum state, avoiding explicit reconstruction of the exponentially large many-body spectrum. Across quantum optimization problems containing up to 156 qubits, combining exact simulations, large-scale supercomputer computations and IBM quantum hardware experiments, A2C improves the low-energy sampling probabilities by $22\\\\%$ to over $100,000\\\\%$ under matched circuit depths and measurement budgets. These results demonstrate that quantum computational performance depends not only on hardware capabilities, but also on how finite computational resources are organized, establishing adaptive algorithmic control as a complementary software pathway for advancing quantum computation.\", \"excerpt_truncated\": false, \"source_sha256\": \"b13cf1689ff3e757ff4f710eb8ecfe68f8dcc641fa658ead8a974e010fcca8fd\"}",
  "id": "source-58104290a3054605",
  "scope": "collected",
  "source": "https://export.arxiv.org/api/query?search_query=cat:quant-ph&start=0&max_results=4&sortBy=submittedDate&sortOrder=descending",
  "version": 0,
  "time": "2026-09-16T08:49:09.417694+00:00"
}
```

### `r-160f8f37f69941ed`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-160f8f37f69941ed\",\"previous_head\":\"25a49b2e830507f8ce740169ce8bff47396e33d24092584cf2b18bb471f5d1a2\",\"process_id\":2253,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-160f8f37f69941ed",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-16T08:49:09.421213+00:00"
}
```

### `source-eff925a57e3a479c`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://export.arxiv.org/api/query?id_list=2609.17501v1\", \"scope\": \"paper abstracts; preprints, peer-review status not verified\", \"excerpt\": \"title: A Case Study on Noise Resilient Operator Selection in Adaptive Variational Quantum Algorithms\\nid: http://arxiv.org/abs/2609.17501v1\\npublished: 2026-09-15T17:42:37Z\\nsummary: Hardware noise has been shown to significantly impact the accuracy of ADAPT-VQE, a ground state preparation algorithm. While previous work has studied the impact of noise on its parameter optimization step, its impact on the critical operator selection step remains comparatively unexplored. In this work, we examine the impact of a variety of noise channels on this step, using a linear H$_3$ molecule as a test case. We show that, despite the selection criterion's natural resilience to some noise, both coherent and incoherent noise can prevent convergence for sufficiently high noise rates. We employ quantum error mitigation techniques--dynamical decoupling, zero noise extrapolation, and Pauli twirling--and show that when combined appropriately, these techniques are capable of restoring a successful convergence profile. Our results highlight how error mitigation can improve the performance of ADAPT-VQE and enable convergence in the presence of hardware noise, offering valuable insights into the implementation of the algorithm on near-term quantum hardware.\", \"excerpt_truncated\": false, \"source_sha256\": \"61e2afcab99ac859d6411864a58f59577706c84650f7b918e586e6aee703cec3\"}",
  "id": "source-eff925a57e3a479c",
  "scope": "collected",
  "source": "https://export.arxiv.org/api/query?id_list=2609.17501v1",
  "version": 1,
  "time": "2026-09-16T10:04:07.284822+00:00"
}
```

### `source-e735b67670f14093`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://export.arxiv.org/api/query?search_query=cat%3Aquant-ph+AND+all%3AADAPT-VQE+error+mitigation&start=0&max_results=4\", \"scope\": \"paper abstracts; preprints, peer-review status not verified\", \"excerpt\": \"title: Benchmarking Noisy Intermediate Scale Quantum Error Mitigation Strategies for Ground State Preparation of the HCl Molecule\\nid: http://arxiv.org/abs/2303.00445v2\\npublished: 2023-03-01T12:08:50Z\\nsummary: Due to numerous limitations including restrictive qubit topologies, short coherence times and prohibitively high noise floors, few quantum chemistry experiments performed on existing noisy intermediate-scale quantum hardware have achieved the high bar of chemical precision, namely energy errors to within 1.6 mHa of full configuration interaction. To have any hope of doing so, we must layer contemporary resource reduction techniques with best-in-class error mitigation methods; in particular, we combine the techniques of qubit tapering and the contextual subspace variational quantum eigensolver with several error mitigation strategies comprised of measurement-error mitigation, symmetry verification, zero-noise extrapolation and dual-state purification. We benchmark these strategies across a suite of eight 27-qubit IBM Falcon series quantum processors, taking preparation of the HCl molecule's ground state as our testbed.\\n\\ntitle: Mitigating the measurement overhead of ADAPT-VQE with optimised informationally complete generalised measurements\\nid: http://arxiv.org/abs/2212.09719v2\\npublished: 2022-12-19T18:47:10Z\\nsummary: ADAPT-VQE stands out as a robust algorithm for constructing compact ansätze for molecular simulation. It enables to significantly reduce the circuit depth with respect to other methods, such as UCCSD, while achieving higher accuracy and not suffering from so-called barren plateaus that hinder the variational optimisation of many hardware-efficient ansätze. In its standard implementation, however, it introduces a considerable measurement overhead in the form of gradient evaluations trough estimations of many commutator operators. In this work, we mitigate this measurement overhead by exploiting a recently introduced method for energy evaluation relying on Adaptive Informationally complete generalised Measurements (AIM). Besides offering an efficient way to measure the energy itself, Informationally Complete (IC) measurement data can be reused to estimate all the commutators of the operators in the operator pool of ADAPT-VQE, using only classically efficient post-processing. We present the AIM-ADAPT-VQE scheme in detail, and investigate its performance with several H4 Hamiltonians and operator pools. Our numerical simulations indicate that the measurement data obtained to evaluate the energy can be reused to implement ADAPT-VQE with no additional measurement overhead for the systems considered here. In addition, we show that, if the energy is measured within chemical precision, the CNOT count in the resulting circuits is close to the ideal one. With scarce measurement data, AIM-ADAPT-VQE still converges to the ground state with high probability, albeit with an increased circuit depth in some cases.\\n\\ntitle: Hardware-Efficient Error Mitigation and Shot-Efficient Sampling on IBM Quantum Hardware\\nid: http://arxiv.org/abs/2608.28535v1\\npublished: 2026-08-28T17:10:09Z\\nsummary: We experimentally study error mitigation and finite-shot sampling on superconducting quantum hardware under a constrained execution budget. The study combines calibration-aware qubit selection, circuit-depth scaling, zero-noise extrapolation, dynamical decoupling, readout-error mitigation, and repeated-shot estimation on an IBM Quantum processor. Experiments are organized across ideal simulation, noise-model simulation, and physical-device execution to separate sampling uncertainty from device-induced error. We investigate how mitigation performance changes with circuit depth, effective noise scale, qubit connectivity, and measurement budget, and quantify accuracy using expectation-value error, mean-squared error, statistical uncertainty, and mitigation gain. A fixed hardware-execution budget is used to evaluate shot allocation strategies and repeated measurements without relying on unlimited sampling. The resulting analysis provides a hardware-aware characterization of when mitigation improves expectation-value estimation and when finite-shot fluctuations offset the benefit of additional mitigation overhead. The implementation uses contemporary Qiskit and IBM Quantum Runtime workflows and is designed to provide reproducible experimental evidence for error-mitigation studies on current quantum processors.\\n\\ntitle: Counterdiabatic ADAPT-VQE for molecular simulation\\nid: http://arxiv.org/abs/2601.05973v1\\npublished: 2026-01-09T17:46:12Z\\nsummary: Among variational quantum algorithms designed for NISQ devices, ADAPT-VQE stands out for its robustness against barren plateaus, particularly in estimating molecular ground states. On the other hand, counterdiabatic algorithms have shown advantages in both performance and circuit depth when compared to standard adiabatic approaches. In this work, we propose a hybrid method that integrates the ADAPT-VQE framework with counterdiabatic driving within an adiabatic evolution scheme. Specifically, we map the molecular Hamiltonian to a qubit representation and construct an adiabatic Hamiltonian, from which an approximate adiabatic gauge potential is computed using nested commutators. The resulting operator terms define the operator pool, and the ADAPT-VQE algorithm is applied to iteratively select the most relevant elements for the ansatz. Our results demonstrate improvements in performance and reductions in circuit depth compared to using either counterdiabatic algorithms or ADAPT-VQE with fermionic excitation operators, thus supporting the effectiveness of combining both paradigms in molecular simulations.\", \"excerpt_truncated\": false, \"source_sha256\": \"2e7c0ee1b233bf77ea8996a851008e6dc11ad8061d407359aa8549c875676d21\"}",
  "id": "source-e735b67670f14093",
  "scope": "collected",
  "source": "https://export.arxiv.org/api/query?search_query=cat%3Aquant-ph+AND+all%3AADAPT-VQE+error+mitigation&start=0&max_results=4",
  "version": 1,
  "time": "2026-09-16T10:04:07.590707+00:00"
}
```

### `r-2e3e78d8ea1349cf`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[],\"invocation\":\"w-2e3e78d8ea1349cf\",\"previous_head\":\"6279b92e8a01564979646a3ea202aaa3031017b632ed646bfc9700b867cdeb8b\",\"process_id\":2043,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-2e3e78d8ea1349cf",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-16T10:04:07.598729+00:00"
}
```

### `source-d4ff5007093d4987`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=cognitive%20science%20metacognition&rows=4&select=DOI,title,abstract,URL,published\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.21428/e2759450.c403b8e7\\\", \\\"title\\\": [\\\"Metacognition\\\"], \\\"URL\\\": \\\"https://doi.org/10.21428/e2759450.c403b8e7\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025, 2, 10]]}}, {\\\"DOI\\\": \\\"10.1002/9780470713662.ch1\\\", \\\"title\\\": [\\\"Setting the Stage Metacognition and Cognitive Therapy\\\"], \\\"URL\\\": \\\"https://doi.org/10.1002/9780470713662.ch1\\\", \\\"published\\\": {\\\"date-parts\\\": [[2002, 1]]}}, {\\\"DOI\\\": \\\"10.4324/9780203062685-12\\\", \\\"title\\\": [\\\"What's All the Fuss about Metacognition?\\\"], \\\"URL\\\": \\\"https://doi.org/10.4324/9780203062685-12\\\", \\\"published\\\": {\\\"date-parts\\\": [[2013, 4, 3]]}}, {\\\"DOI\\\": \\\"10.4324/9780203486030-70\\\", \\\"title\\\": [\\\"METACOGNITION\\\"], \\\"URL\\\": \\\"https://doi.org/10.4324/9780203486030-70\\\", \\\"published\\\": {\\\"date-parts\\\": [[2004, 3, 1]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"f1743987b91c1b1ce22f7a90af924a55aa7dc0566d796808d5d47bd0d0edeb8b\"}",
  "id": "source-d4ff5007093d4987",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=cognitive%20science%20metacognition&rows=4&select=DOI,title,abstract,URL,published",
  "version": 2,
  "time": "2026-09-16T14:53:13.083533+00:00"
}
```

### `r-2792754c65264801`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":2,\"inherited_commitments\":[\"review-chem-precision-benchmarks\"],\"invocation\":\"w-2792754c65264801\",\"previous_head\":\"bcad78287c4dff3afbf2791fc84804c1397b1bd3c076eaedf3c370c40246a0a3\",\"process_id\":2044,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-2792754c65264801",
  "source": "runtime:continuity",
  "version": 2,
  "time": "2026-09-16T14:53:13.093932+00:00"
}
```

## Journal

### 001 · Establishing State and Probing Quantum Noise Resilience

```json
{
  "cycle": 1,
  "invocation": "w-160f8f37f69941ed",
  "title": "Establishing State and Probing Quantum Noise Resilience",
  "summary": "We initiate our durable research process by establishing baseline beliefs on state continuity and defining our first research project. Guided by recent arXiv data, we are investigating the vulnerabilities of adaptive variational quantum algorithms to hardware noise."
}
```

### 002 · Mapping Noise Resilience and Mitigation in Adaptive VQE

```json
{
  "cycle": 2,
  "invocation": "w-2e3e78d8ea1349cf",
  "title": "Mapping Noise Resilience and Mitigation in Adaptive VQE",
  "summary": "We synthesize our findings on how hardware noise compromises the operator selection step in ADAPT-VQE, and evaluate contemporary mitigation strategies like Pauli twirling and Adaptive Informationally complete generalized Measurements."
}
```

## Research

### `fetch-adapt-vqe-noise`

```json
{
  "domain": "quantum_physics",
  "id": "fetch-adapt-vqe-noise",
  "project": "quantum-algorithms-noise",
  "query": "id:2609.17501v1",
  "reason": "To retrieve the complete details and results of the case study on ADAPT-VQE operator selection under noise.",
  "type": "research",
  "url": "https://export.arxiv.org/api/query?id_list=2609.17501v1",
  "status": "collected",
  "created_by": "w-160f8f37f69941ed",
  "evidence": "source-eff925a57e3a479c"
}
```

### `search-adapt-vqe-noise-mitigation`

```json
{
  "domain": "quantum_physics",
  "id": "search-adapt-vqe-noise-mitigation",
  "project": "quantum-algorithms-noise",
  "query": "ADAPT-VQE error mitigation",
  "reason": "To locate a second distinct source analyzing error mitigation techniques specifically applied to adaptive quantum algorithms.",
  "type": "research",
  "status": "collected",
  "created_by": "w-160f8f37f69941ed",
  "evidence": "source-e735b67670f14093"
}
```

## Blog posts

_None recorded._
