# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 1  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `f85ef504adee38f63407418365eb5422aa4ba89e3591d81e579eedc94791da6a`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

### `wake_system_design`

```json
{
  "confidence": 1.0,
  "evidence": [
    "source-6cea09af14e345ae"
  ],
  "id": "wake_system_design",
  "reason": "The repository's master README explicitly defines WAKE as an experiment in durable, accountable work across interchangeable intelligences.",
  "statement": "WAKE is a durable research framework designed to preserve state, open obligations, projects, and exact receipts across disposable model invocations.",
  "status": "active",
  "type": "belief",
  "updated_by": "w-a71ac450ec6e4502",
  "updated_version": 1
}
```

## Commitments

### `commit_entropy_review`

```json
{
  "due_cycle": 3,
  "id": "commit_entropy_review",
  "reason": "To ensure continuity of the entropy research project across subsequent wakes.",
  "task": "Review incoming search results for entropy concepts and draft an initial analysis notebook.",
  "type": "commit",
  "status": "open",
  "created_by": "w-a71ac450ec6e4502",
  "created_version": 1
}
```

## Projects

### `entropy_measurement` · Measuring Information and Physical Entropy

```json
{
  "domain": "entropy",
  "id": "entropy_measurement",
  "next_step": "Search for more clinical and ecological definitions of entropy metrics.",
  "question": "How do approximate entropy and maximum entropy formulations reconcile in physical and physiological time-series?",
  "reason": "Aligns with OpenAlex metadata showing ecological maximum entropy models and physiological time-series metrics.",
  "status": "active",
  "title": "Measuring Information and Physical Entropy",
  "type": "project",
  "created_version": 1,
  "updated_version": 1,
  "updated_by": "w-a71ac450ec6e4502"
}
```

## Notebooks

_None recorded._

## Invocations

### `w-a71ac450ec6e4502`

```json
{
  "base_version": 0,
  "charged": true,
  "id": "w-a71ac450ec6e4502",
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
  "process_id": 2268,
  "provider": "gemini",
  "quota_day": "2026-09-19",
  "request_hash": "e5184975c8a5e9a8b659cc3401fb64994ee954be6a3f5b4ac8afc38a0c2a0673",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [
          "source-6cea09af14e345ae"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-6cea09af14e345ae",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-cbfd772aea3543e4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cbfd772aea3543e4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-6cea09af14e345ae",
      "source-cbfd772aea3543e4"
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
    "delivered_context_chars": 8902,
    "inquiry_drive_project_count": 0,
    "mode": "shadow",
    "retrieval_candidate_count": 2,
    "retrieval_evidence_count": 2,
    "retrieval_trigger_counts": {
      "unincorporated_evidence": 2
    },
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0474
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
  "time": "2026-09-19T17:22:14.364939+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 205,
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
            "retryDelay": "43s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.8-flash\nPlease retry in 43.12412593s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 28979,
      "response_bytes_captured": 1362,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 25879,
      "http_status": 200,
      "model": "gemini-3.5-flash",
      "request_payload_bytes": 28979,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.5-flash",
  "finished": "2026-09-19T17:22:46.276196+00:00",
  "reason": ""
}
```

### `w-02ede87b8aaf43e1`

```json
{
  "base_version": 1,
  "charged": true,
  "id": "w-02ede87b8aaf43e1",
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
        "id": "entropy_measurement",
        "score": 0.675,
        "signals": {
          "collected_research": 1,
          "notebooks": 0,
          "queued_research": 0
        },
        "title": "Measuring Information and Physical Entropy"
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
  "request_hash": "ea835bd524594eb01375d2ef907d047f78fb46724c1073861a5e3d591cbe3baf",
  "retrieval_shadow": {
    "candidates": [
      {
        "evidence": [],
        "reason": "An open commitment is approaching its due cycle.",
        "record": {
          "id": "commit_entropy_review",
          "kind": "commitment"
        },
        "trigger": "commitment_near_due"
      },
      {
        "evidence": [
          "source-cbfd772aea3543e4"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-cbfd772aea3543e4",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-412751d2ead44fdd"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-412751d2ead44fdd",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      },
      {
        "evidence": [
          "source-4dc364b7299d4d46"
        ],
        "reason": "Durable evidence exists that is not yet represented by a belief or notebook.",
        "record": {
          "id": "source-4dc364b7299d4d46",
          "kind": "evidence"
        },
        "trigger": "unincorporated_evidence"
      }
    ],
    "evidence_ids": [
      "source-cbfd772aea3543e4",
      "source-412751d2ead44fdd",
      "source-4dc364b7299d4d46"
    ],
    "limitations": [
      "This plan is deterministic and ID-based; it does not claim semantic contradiction detection.",
      "No evidence content is copied into the working set by this planner.",
      "Shadow mode records what would be retrieved but does not change provider context."
    ],
    "metrics": {
      "candidate_count": 4,
      "evidence_count": 3,
      "trigger_counts": {
        "commitment_near_due": 1,
        "unincorporated_evidence": 3
      }
    },
    "mode": "shadow",
    "principle": "Rehydrate exact records when an abstraction becomes expensive to trust."
  },
  "working_set_metrics": {
    "delivered_context_chars": 16816,
    "inquiry_drive_project_count": 1,
    "mode": "shadow",
    "retrieval_candidate_count": 4,
    "retrieval_evidence_count": 3,
    "retrieval_trigger_counts": {
      "commitment_near_due": 1,
      "unincorporated_evidence": 3
    },
    "working_set_chars": 1367,
    "working_to_delivered_ratio": 0.0813
  },
  "working_set_shadow": {
    "active_projects": [
      {
        "id": "entropy_measurement",
        "next_step": "Search for more clinical and ecological definitions of entropy metrics.",
        "question": "How do approximate entropy and maximum entropy formulations reconcile in physical and physiological time-series?",
        "title": "Measuring Information and Physical Entropy"
      }
    ],
    "beliefs": [
      {
        "claim": "WAKE is a durable research framework designed to preserve state, open obligations, projects, and exact receipts across disposable model invocations.",
        "confidence": 1.0,
        "id": "wake_system_design",
        "provenance": [
          "source-6cea09af14e345ae"
        ],
        "status": "active",
        "why_retained": "The repository's master README explicitly defines WAKE as an experiment in durable, accountable work across interchangeable intelligences."
      }
    ],
    "mode": "shadow",
    "open_commitments": [
      {
        "due_cycle": 3,
        "id": "commit_entropy_review",
        "reason": "To ensure continuity of the entropy research project across subsequent wakes.",
        "task": "Review incoming search results for entropy concepts and draft an initial analysis notebook."
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
  "time": "2026-09-19T17:24:02.909423+00:00",
  "provider_attempts": [
    {
      "category": "http",
      "elapsed_ms": 184,
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
            "retryDelay": "54s"
          }
        ],
        "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-3.5-flash\nPlease retry in 54.489229826s.",
        "status": "RESOURCE_EXHAUSTED"
      },
      "request_payload_bytes": 38120,
      "response_bytes_captured": 1363,
      "result": "daily_quota"
    },
    {
      "elapsed_ms": 10529,
      "http_status": 200,
      "model": "gemini-3.1-flash-lite",
      "request_payload_bytes": 38120,
      "result": "success"
    }
  ],
  "provider_requests_sent": 2,
  "successful_model": "gemini-3.1-flash-lite",
  "finished": "2026-09-19T17:24:19.628932+00:00",
  "reason": "Evidence reference does not exist"
}
```

## Evidence

### `source-6cea09af14e345ae`

````json
{
  "actor": "collector",
  "content": "{\"url\": \"https://raw.githubusercontent.com/sudofx/wake/master/README.md\", \"scope\": \"raw source-controlled WAKE repository text\", \"excerpt\": \"# **WAKE✳︎**\\n\\n<p align=\\\"center\\\"><img src=\\\"assets/covers/cover-variant-001.png\\\" alt=\\\"**WAKE✳︎** Lab Comics #1 — **WAKE✳︎** project comic cover\\\" width=\\\"100%\\\"/>\\n\\n**Bob is following *the big questions.***\\n\\nDisposable models. Durable state. Receipts for everything.\\n\\n**Working Abstractions Keep Evidence.** A philosophical echo remains in the name too: **Why Any Knowledge Exists?**\\n\\n**WAKE✳︎** is an experiment in durable, accountable work across interchangeable intelligences. Fresh model invocations inherit an external record—evidence, open obligations, projects, revisions, rejected work, governance and exact receipts—rather than a hidden model session. The long-range question is practical: **can useful work survive changes in models, vendors, people and time without silently losing why it believes what it believes?**\\n\\nIt does **not** assume or test for consciousness, qualia, personhood, or a persistent internal self. Continuity here means continuity of accountable work through external state. A coherent narrative is not evidence that a persistent mind exists.\\n\\nThe project deliberately treats failures as data. Rejected proposals, provider failures, weak evidence, corrections and superseded conclusions remain visible because the interesting question is not whether a model can sound convincing; it is whether a process can remain **correctable**. The operating shorthand is: **exact underneath, approximate on purpose, correctable always.**\\n\\nResearch topics are dynamic and come only from `research-topics.toml`. They are inputs to the experiment—not conclusions encoded in governance—and can be replaced between controlled runs. The current topic file is the authority; there is no hardcoded legacy topic list. In the present experiment, topics stand in for the varied input a future user or institution might supply.\\n\\nA trusted collector retrieves bounded public evidence before inference. Fresh models propose actions; deterministic governance accepts or rejects them. Live collected evidence is stamped by the collector and current notebook/blog publication requires corroborating material from multiple distinct collected source URLs in the project's configured topic. That is a useful garbage filter, **not proof of truth, source independence, scientific validity, or semantic entailment**.\\n\\nThe public site exposes the same record at increasing depth: readable summaries and Bob's editorial layer at the surface; projects, notebooks and evidence underneath; MAP and the journal for provenance; exact events and state at the bottom. Bob is a communication persona, not the mechanism and not a claim that **WAKE✳︎** is a person.\\n\\n**[Open **WAKE✳︎**’s home](https://sudofx.github.io/wake/)** · **[Trigger a manual wake](https://github.com/sudofx/wake/actions/workflows/wake.yml)**\\n\\nThe current GitHub deployment can run without a persistent local computer. `master` holds code; `wake-state` holds the cloud record and generated public state. Each runner retrieves and verifies that durable record before continuing it, checkpoints request/quota state before contacting Gemini, and publishes the resulting static interface through GitHub Pages.\\n\\nThe included offline experiment remains separate from live research. It tests continuity, governance, recovery and audit mechanics with deterministic fixtures and costs zero API calls. It does not establish live-model comprehension.\\n\\n## Start here — no account, no API calls\\n\\nRequires **Python 3.11 or later on macOS or Linux**. No runtime packages, Node, database server, or build tools to install. Run commands from the project directory.\\n\\n```sh\\n# Read the included, fully executed 100-cycle experiment.\\npython3 -m wake serve --directory examples/journal\\n# Open http://127.0.0.1:8000\\n```\\n\\nThe [included Markdown journal](examples/journal/journal.md) and [experiment results](examples/journal/experiment.json) are readable without running anything. The HTML is self-contained, responsive, and works as a local file. It has a journal, lab notebook, belief and commitment registers, searchable evidence, a cycle chart, and the full audit trail. Every simulated entry is labeled.\\n\\nTo reproduce the experiment from scratch:\\n\\n```sh\\npython3 -m wake --data data/rehearsal experiment --cycles 100 --output site\\npython3 -m wake audit --events site/events.jsonl --head site/head.txt\\npython3 -m wake serve\\n```\\n\\nUse a **new** data directory each time. The experiment refuses to erase existing records. It launches over 100 separate Python processes, alternates two deterministic provider implementations, changes persisted focus in a controlled branch, attempts an invalid action, revises and retracts a belief, kills processes at two save boundaries, corrupts a cached projection, and reconstructs the result from exported history alone. It costs **zero API calls**.\\n\\nThese are harness guarantees tested with simulated providers, **not evidence of live-model comprehension**. The separate live experiment protocol is in [docs/experiment.md](docs/experiment.md).\\n\\n## Quick setup — Gemini\\n\\nGemini is currently the only unattended API provider that has been exercised by this project. Other models can cross the manual `prepare` / `complete` boundary, but do not assume another vendor's API works unattended until an adapter is implemented and tested.\\n\\n### 1. Clone and verify\\n\\n```sh\\ngit clone https://github.com/sudofx/wake.git\\ncd wake\\npython3 --version                 # Python 3.11+\\npython3 -m unittest discover -s tests -v\\n```\\n\\nNo Node, database server, or vendor SDK is required.\\n\\n### 2. Add your Gemini API key locally\\n\\nCreate a Gemini API key in Google AI Studio. Then:\\n\\n```sh\\ncp .env.example .env\\n```\\n\\nEdit `.env` so it contains:\\n\\n```text\\nGEMINI_API_KEY=your_key_here\\n```\\n\\n`.env` is ignored by Git. Never commit the key. If you intend to use a free-tier-only API project, verify billing is disabled for that Google project and leave `free_tier_confirmed = true` in `wake.toml` only when that statement is true.\\n\\n### 3. Configure the model and topics\\n\\nThe provider/model settings live in `wake.toml`. The repository currently uses Gemini with an explicit fallback chain. Change model names or per-model daily ceilings there only to values your Gemini project actually supports.\\n\\nResearch topics live **only** in `research-topics.toml`. Edit that file to change the experiment's inputs; do not hardcode topics into governance or prompts.\\n\\n### 4. Initialize and test locally\\n\\n```sh\\npython3 -m wake init\\npython3 -m wake wake\\npython3 -m wake audit\\npython3 -m wake export\\npython3 -m wake serve\\n```\\n\\nOpen `http://127.0.0.1:8000`. A live `wake` can consume Gemini quota. For a zero-call systems check, use the offline experiment in the previous section instead.\\n\\n### 5. Add the same key to GitHub Actions\\n\\nIn your GitHub repository:\\n\\n1. Open **Settings → Secrets and variables → Actions**.\\n2. Choose **New repository secret**.\\n3. Name it exactly `GEMINI_API_KEY`.\\n4. Paste the same Gemini API key and save it.\\n\\nDo **not** put the key in `wake.toml`, `research-topics.toml`, workflow YAML, Issues, Actions logs, or the public `wake-state` branch.\\n\\n### 6. Configure GitHub Actions permissions\\n\\nOpen **Settings → Actions → General**. Under **Workflow permissions**, select **Read and write permissions** and save. Leave Actions enabled for the repository.\\n\\nThe included workflow itself requests only the permissions it needs: `contents: write` for the durable state branch and `pages: write` / `id-token: write` for GitHub Pages deployment.\\n\\n### 7. Configure GitHub Pages\\n\\nOpen **Settings → Pages** and set the build/deployment source to **GitHub Actions**. Do not add a generic Jekyll/static Pages workflow; **WAKE✳︎ — research & journal** is the publisher.\\n\\n### 8. Run the first cloud wake\\n\\nOpen **Actions → WAKE✳︎ — research & journal → Run workflow** and run it from the default branch. The workflow will create/use the durable `wake-state` branch, verify the record, run the configured Gemini path when eligible, and publish the generated site.\\n\\nA source-code push normally refreshes the site without spending a Gemini call. Scheduled ticks are best effort; durable eligibility prevents closely spaced scheduled deliveries from becoming concurrent writers.\\n\\n### 9. Verify the installation\\n\\nCheck that:\\n\\n- the workflow completes without an operator-attention failure;\\n- the Pages deployment succeeds;\\n- the public site loads;\\n- `wake-state` exists after the first stateful cloud run;\\n- the site reports the latest attempt separately from the latest accepted wake;\\n- **Verify the record** passes on `master`.\\n\\nAfter that, normal operation requires no open local computer.\\n\\nFor recovery behavior, quota semantics, reset controls and the exact cloud lifecycle, read [cloud operations](docs/cloud.md). For the trust boundary, read [architecture and limits](docs/architecture.md).\\n\\n## Claude, ChatGPT, and other desktop models\\n\\nUse free desktop sessions manually without assuming they include free API access:\\n\\n```sh\\npython3 -m wake prepare --model 'Claude Desktop / human-attested' --output request.json\\n# Paste request.json into a fresh desktop chat. Ask for the specified JSON object.\\n# Save the response alone as reply.json, then use the ID printed by prepare:\\npython3 -m wake complete --id w-REPLACE_WITH_PRINTED_ID --file reply.json\\npython3 -m wake export\\n```\\n\\nThe exact request is durable before you switch apps. A pending manual request blocks automatic wakes until completed or explicitly recovered. All providers cross the same governance boundary. Manual model identity is honestly labeled human-attested. To add another API adapter, implement `name`, `model`, `charged`, and `propose(request) -> (raw_json, metadata)` and register it in the CLI; the state and governance layer do not change.\\n\\n## Inquiry-drive experiment\\n\\nEvery chartered wake records a visible, deterministic shadow scorecard for active projects: continuity,\\nnovelty, coherence, generativity and self-correction. It is observational by default and does not reach the\\nmodel. Rev\", \"excerpt_truncated\": true, \"source_sha256\": \"60dd4c5b3c0cc6e07e794381a8b74947f0256360d07375ca03c5f26c4a8812e4\", \"verification_required\": true, \"topic_domain\": \"wake_analysis\"}",
  "id": "source-6cea09af14e345ae",
  "scope": "collected",
  "source": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
  "version": 0,
  "time": "2026-09-19T17:22:13.876176+00:00"
}
````

### `source-cbfd772aea3543e4`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2139416101\\\", \\\"doi\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"title\\\": \\\"Maximum entropy modeling of species geographic distributions\\\", \\\"publication_year\\\": 2005, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 18078, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1016/j.ecolmodel.2005.03.026\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1016/j.ecolmodel.2005.03.026\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S88315673\\\", \\\"display_name\\\": \\\"Ecological Modelling\\\", \\\"issn_l\\\": \\\"0304-3800\\\", \\\"issn\\\": [\\\"0304-3800\\\", \\\"1872-7026\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"jufo-1\\\", \\\"norway-1\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320990\\\", \\\"host_organization_name\\\": \\\"Elsevier BV\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320990\\\"], \\\"host_organization_lineage_names\\\": [\\\"Elsevier BV\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecological Modelling\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": null}, {\\\"id\\\": \\\"https://openalex.org/W1862394037\\\", \\\"doi\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"title\\\": \\\"Physiological time-series analysis using approximate entropy and sample entropy\\\", \\\"publication_year\\\": 2000, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7942, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1152/ajpheart.2000.278.6.h2039\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1152/ajpheart.2000.278.6.h2039\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S87338489\\\", \\\"display_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"issn_l\\\": \\\"0363-6135\\\", \\\"issn\\\": [\\\"0363-6135\\\", \\\"1522-1539\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\", \\\"doyens\\\", \\\"jufo-2\\\", \\\"medline\\\", \\\"norway-2\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"American Journal of Physiology-Heart and Circulatory Physiology\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Entropy, as it relates to dynamical systems, is the rate of information production. Methods for estimation of the entropy of a system represented by a time series are not, however, well suited to analysis of the short and noisy data sets encountered in cardiovascular and other biological studies. Pincus introduced approximate entropy (ApEn), a set of measures of system complexity closely related to entropy, which is easily applied to clinical cardiovascular and other time series. ApEn statistics, however, lead to inconsistent results. We have developed a new and related complexity measure, sample entropy (SampEn), and have compared ApEn and SampEn by using them to analyze sets of random numbers with known probabilistic character. We have also evaluated cross-ApEn and cross-SampEn, which use cardiovascular data sets to measure the similarity of two distinct time series. SampEn agreed with theory much more closely than ApEn over a broad range of conditions. The improved accuracy of SampEn statistics should make them useful in the study of experimental clinical cardiovascular and other biological time series.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2146478425\\\", \\\"doi\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"title\\\": \\\"Black Holes and Entropy\\\", \\\"publication_year\\\": 1973, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 7532, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1103/physrevd.7.2333\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1103/physrevd.7.2333\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S4210190737\\\", \\\"display_name\\\": \\\"Physical review. D. Particles, fields, gravitation, and cosmology/Physical review. D. Particles and fields\\\", \\\"issn_l\\\": \\\"0556-2821\\\", \\\"issn\\\": [\\\"0556-2821\\\", \\\"1089-4918\\\", \\\"1538-4500\\\", \\\"1550-2368\\\", \\\"1550-7998\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320261\\\", \\\"host_organization_name\\\": \\\"American Physical Society\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320261\\\"], \\\"host_organization_lineage_names\\\": [\\\"American Physical Society\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Physical Review D\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"There are a number of similarities between black-hole physics and thermodynamics. Most striking is the similarity in the behaviors of black-hole area and of entropy: Both quantities tend to increase irreversibly. In this paper we make this similarity the basis of a thermodynamic approach to black-hole physics. After a brief review of the elements of the theory of information, we discuss black-hole physics from the point of view of information theory. We show that it is natural to introduce the concept of black-hole entropy as the measure of information about a black-hole interior which is inaccessible to an exterior observer. Considerations of simplicity and consistency, and dimensional arguments indicate that the black-hole entropy is equal to the ratio of the black-hole area to the square of the Planck length times a dimensionless constant of order unity. A different approach making use of the specific properties of Kerr black holes and of concepts from information theory leads to the same conclusion, and suggests a definite value for the constant. The physical content of the concept of black-hole entropy derives from the following generalized version of the second law: When common entropy goes down a black hole, the common entropy in the black-hole exterior plus the black-hole entropy never decreases. The validity of this version of the second law is supported by an argument from information theory as well as by several examples.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2058085399\\\", \\\"doi\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"title\\\": \\\"Nanostructured High‐Entropy Alloys with Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes\\\", \\\"publication_year\\\": 2004, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 15264, \\\"open_access\\\": {\\\"is_oa\\\": false, \\\"oa_status\\\": \\\"closed\\\", \\\"oa_url\\\": null, \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1002/adem.200300567\\\", \\\"is_oa\\\": false, \\\"landing_page_url\\\": \\\"https://doi.org/10.1002/adem.200300567\\\", \\\"pdf_url\\\": null, \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S156255550\\\", \\\"display_name\\\": \\\"Advanced Engineering Materials\\\", \\\"issn_l\\\": \\\"1438-1656\\\", \\\"issn\\\": [\\\"1438-1656\\\", \\\"1527-2648\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Advanced Engineering Materials\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"A new approach for the design of alloys is presented in this study. These “high‐entropy alloys” with multi‐principal elements were synthesized using well‐developed processing technologies. Preliminary results demonstrate examples of the alloys with simple crystal structures, nanostructures, and promising mechanical properties. This approach may be opening a new era in materials science and engineering.\\\"}]\", \"excerpt_truncated\": false, \"source_sha256\": \"925fa175e43e12b61c9dccd98aaf69a7abf2a8ab0694b0131b47fd8dfe70336f\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-cbfd772aea3543e4",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=entropy&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 0,
  "time": "2026-09-19T17:22:14.358254+00:00"
}
```

### `r-a71ac450ec6e4502`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-a71ac450ec6e4502\",\"previous_head\":\"61551e938b3bc049ab8243469c2d5871d51184f9fb9534d1ed22be477096c4dc\",\"process_id\":2268,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-a71ac450ec6e4502",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-19T17:22:14.361642+00:00"
}
```

### `source-412751d2ead44fdd`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.openalex.org/works?search=approximate+entropy+sample+entropy+physiology+ecological+modeling&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index\", \"scope\": \"OpenAlex scholarly metadata and reconstructed abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"id\\\": \\\"https://openalex.org/W2107695795\\\", \\\"doi\\\": \\\"https://doi.org/10.1890/10-1171.1\\\", \\\"title\\\": \\\"Ecological niche modeling in Maxent: the importance of model complexity and the performance of model selection criteria\\\", \\\"publication_year\\\": 2010, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 2360, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"bronze\\\", \\\"oa_url\\\": \\\"https://onlinelibrary.wiley.com/doi/pdfdirect/10.1890/10-1171.1\\\", \\\"any_repository_has_fulltext\\\": false}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1890/10-1171.1\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1890/10-1171.1\\\", \\\"pdf_url\\\": \\\"https://onlinelibrary.wiley.com/doi/pdfdirect/10.1890/10-1171.1\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S166870025\\\", \\\"display_name\\\": \\\"Ecological Applications\\\", \\\"issn_l\\\": \\\"1051-0761\\\", \\\"issn\\\": [\\\"1051-0761\\\", \\\"1939-5582\\\"], \\\"is_oa\\\": false, \\\"is_in_doaj\\\": false, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"cwts-core\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": null, \\\"license_id\\\": null, \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecological Applications\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Maxent, one of the most commonly used methods for inferring species distributions and environmental tolerances from occurrence data, allows users to fit models of arbitrary complexity. Model complexity is typically constrained via a process known as L1 regularization, but at present little guidance is available for setting the appropriate level of regularization, and the effects of inappropriately complex or simple models are largely unknown. In this study, we demonstrate the use of information criterion approaches to setting regularization in Maxent, and we compare models selected using information criteria to models selected using other criteria that are common in the literature. We evaluate model performance using occurrence data generated from a known \\\\\\\"true\\\\\\\" initial Maxent model, using several different metrics for model quality and transferability. We demonstrate that models that are inappropriately complex or inappropriately simple show reduced ability to infer habitat quality, reduced ability to infer the relative importance of variables in constraining species' distributions, and reduced transferability to other time periods. We also demonstrate that information criteria may offer significant advantages over the methods commonly used in the literature.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2108292915\\\", \\\"doi\\\": \\\"https://doi.org/10.1371/journal.pone.0032202\\\", \\\"title\\\": \\\"Predicting the Current and Future Potential Distributions of Lymphatic Filariasis in Africa Using Maximum Entropy Ecological Niche Modelling\\\", \\\"publication_year\\\": 2012, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 166, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0032202&type=printable\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1371/journal.pone.0032202\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1371/journal.pone.0032202\\\", \\\"pdf_url\\\": \\\"https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0032202&type=printable\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S202381698\\\", \\\"display_name\\\": \\\"PLoS ONE\\\", \\\"issn_l\\\": \\\"1932-6203\\\", \\\"issn\\\": [\\\"1932-6203\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310315706\\\", \\\"host_organization_name\\\": \\\"Public Library of Science\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315706\\\"], \\\"host_organization_lineage_names\\\": [\\\"Public Library of Science\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"PLoS ONE\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Modelling the spatial distributions of human parasite species is crucial to understanding the environmental determinants of infection as well as for guiding the planning of control programmes. Here, we use ecological niche modelling to map the current potential distribution of the macroparasitic disease, lymphatic filariasis (LF), in Africa, and to estimate how future changes in climate and population could affect its spread and burden across the continent. We used 508 community-specific infection presence data collated from the published literature in conjunction with five predictive environmental/climatic and demographic variables, and a maximum entropy niche modelling method to construct the first ecological niche maps describing potential distribution and burden of LF in Africa. We also ran the best-fit model against climate projections made by the HADCM3 and CCCMA models for 2050 under A2a and B2a scenarios to simulate the likely distribution of LF under future climate and population changes. We predict a broad geographic distribution of LF in Africa extending from the west to the east across the middle region of the continent, with high probabilities of occurrence in the Western Africa compared to large areas of medium probability interspersed with smaller areas of high probability in Central and Eastern Africa and in Madagascar. We uncovered complex relationships between predictor ecological niche variables and the probability of LF occurrence. We show for the first time that predicted climate change and population growth will expand both the range and risk of LF infection (and ultimately disease) in an endemic region. We estimate that populations at risk to LF may range from 543 and 804 million currently, and that this could rise to between 1.65 to 1.86 billion in the future depending on the climate scenario used and thresholds applied to signify infection presence.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2969247546\\\", \\\"doi\\\": \\\"https://doi.org/10.1002/ece3.5555\\\", \\\"title\\\": \\\"Collinearity in ecological niche modeling: Confusions and challenges\\\", \\\"publication_year\\\": 2019, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 450, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ece3.5555\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1002/ece3.5555\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1002/ece3.5555\\\", \\\"pdf_url\\\": \\\"https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ece3.5555\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S2482021738\\\", \\\"display_name\\\": \\\"Ecology and Evolution\\\", \\\"issn_l\\\": \\\"2045-7758\\\", \\\"issn\\\": [\\\"2045-7758\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"host_organization\\\": \\\"https://openalex.org/P4310320595\\\", \\\"host_organization_name\\\": \\\"Wiley\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310320595\\\"], \\\"host_organization_lineage_names\\\": [\\\"Wiley\\\"], \\\"type\\\": \\\"journal\\\"}, \\\"license\\\": \\\"cc-by\\\", \\\"license_id\\\": \\\"https://openalex.org/licenses/cc-by\\\", \\\"version\\\": \\\"publishedVersion\\\", \\\"is_accepted\\\": true, \\\"is_published\\\": true, \\\"raw_source_name\\\": \\\"Ecology and Evolution\\\", \\\"raw_type\\\": \\\"journal-article\\\"}, \\\"abstract\\\": \\\"Ecological niche models are widely used in ecology and biogeography. Maxent is one of the most frequently used niche modeling tools, and many studies have aimed to optimize its performance. However, scholars have conflicting views on the treatment of predictor collinearity in Maxent modeling. Despite this lack of consensus, quantitative examinations of the effects of collinearity on Maxent modeling, especially in model transfer scenarios, are lacking. To address this knowledge gap, here we quantify the effects of collinearity under different scenarios of Maxent model training and projection. We separately examine the effects of predictor collinearity, collinearity shifts between training and testing data, and environmental novelty on model performance. We demonstrate that excluding highly correlated predictor variables does not significantly influence model performance. However, we find that collinearity shift and environmental novelty have significant negative effects on the performance of model transfer. We thus conclude that (a) Maxent is robust to predictor collinearity in model training; (b) the strategy of excluding highly correlated variables has little impact because Maxent accounts for redundant variables; and (c) collinearity shift and environmental novelty can negatively affect Maxent model transferability. We therefore recommend to quantify and report collinearity shift and environmental novelty to better infer model accuracy when models are spatially and/or temporally transferred.\\\"}, {\\\"id\\\": \\\"https://openalex.org/W2057691392\\\", \\\"doi\\\": \\\"https://doi.org/10.1371/journal.pone.0055158\\\", \\\"title\\\": \\\"The Effects of Sampling Bias and Model Complexity on the Predictive Performance of MaxEnt Species Distribution Models\\\", \\\"publication_year\\\": 2013, \\\"type\\\": \\\"article\\\", \\\"cited_by_count\\\": 616, \\\"open_access\\\": {\\\"is_oa\\\": true, \\\"oa_status\\\": \\\"gold\\\", \\\"oa_url\\\": \\\"https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0055158&type=printable\\\", \\\"any_repository_has_fulltext\\\": true}, \\\"primary_location\\\": {\\\"id\\\": \\\"doi:10.1371/journal.pone.0055158\\\", \\\"is_oa\\\": true, \\\"landing_page_url\\\": \\\"https://doi.org/10.1371/journal.pone.0055158\\\", \\\"pdf_url\\\": \\\"https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0055158&type=printable\\\", \\\"source\\\": {\\\"id\\\": \\\"https://openalex.org/S202381698\\\", \\\"display_name\\\": \\\"PLoS ONE\\\", \\\"issn_l\\\": \\\"1932-6203\\\", \\\"issn\\\": [\\\"1932-6203\\\"], \\\"is_oa\\\": true, \\\"is_in_doaj\\\": true, \\\"is_core\\\": true, \\\"listed_in\\\": [\\\"doyens\\\", \\\"cwts-core\\\", \\\"doaj\\\"], \\\"host_organization\\\": \\\"https://openalex.org/P4310315706\\\", \\\"host_organization_name\\\": \\\"Public Library of Science\\\", \\\"host_organization_lineage\\\": [\\\"https://openalex.org/P4310315706\\\"], \\\"host_organization_lineage_names\\\": [\\\"Public Library of Science\\\"], \\\"t\", \"excerpt_truncated\": true, \"source_sha256\": \"c9ae8746fa4afa8329281f31bb861108acd082f2907755a9492aa5bd89e26a36\", \"verification_required\": true, \"topic_domain\": \"entropy\"}",
  "id": "source-412751d2ead44fdd",
  "scope": "collected",
  "source": "https://api.openalex.org/works?search=approximate+entropy+sample+entropy+physiology+ecological+modeling&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index",
  "version": 1,
  "time": "2026-09-19T17:24:01.300120+00:00"
}
```

### `source-4dc364b7299d4d46`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished\", \"scope\": \"bibliographic metadata and abstracts where supplied; not full papers\", \"excerpt\": \"[{\\\"DOI\\\": \\\"10.4135/9781071990001\\\", \\\"title\\\": [\\\"Harnessing the Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071990001\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9781071989999\\\", \\\"title\\\": [\\\"Summarizing Harnessing Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9781071989999\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843748\\\", \\\"title\\\": [\\\"Digital Tools and Neurodivergence Capstone Project\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843748\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}, {\\\"DOI\\\": \\\"10.4135/9798348843731\\\", \\\"title\\\": [\\\"Summarizing Digital Tools and Neurodivergence\\\"], \\\"URL\\\": \\\"https://doi.org/10.4135/9798348843731\\\", \\\"published\\\": {\\\"date-parts\\\": [[2025]]}}]\", \"excerpt_truncated\": false, \"source_sha256\": \"94d45bcb2875812795f468c8a2e5db538668353dc7846f2dec1fd04320833c3c\", \"verification_required\": true, \"topic_domain\": \"neurodivergence\"}",
  "id": "source-4dc364b7299d4d46",
  "scope": "collected",
  "source": "https://api.crossref.org/works?query=neurodivergence&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished",
  "version": 1,
  "time": "2026-09-19T17:24:02.897997+00:00"
}
```

### `r-02ede87b8aaf43e1`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":1,\"inherited_commitments\":[\"commit_entropy_review\"],\"invocation\":\"w-02ede87b8aaf43e1\",\"previous_head\":\"67325b67dfe1ee34c33b139ce00ca5c379bacb9978849303aa754a5a42462475\",\"process_id\":2274,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-02ede87b8aaf43e1",
  "source": "runtime:continuity",
  "version": 1,
  "time": "2026-09-19T17:24:02.904590+00:00"
}
```

## Journal

### 001 · A New Wake Begins: Establishing the Baseline

```json
{
  "cycle": 1,
  "invocation": "w-a71ac450ec6e4502",
  "title": "A New Wake Begins: Establishing the Baseline",
  "summary": "We have launched the WAKE system experiment. Armed with the initial project manifest and early metadata pulls from OpenAlex and our repository README, we are establishing our baseline beliefs and initializing a project focusing on Entropy to track how complex systems maintain state and structure."
}
```

## Research

### `research_entropy_metrics`

```json
{
  "domain": "entropy",
  "id": "research_entropy_metrics",
  "project": "entropy_measurement",
  "query": "approximate entropy sample entropy physiology ecological modeling",
  "reason": "To retrieve papers matching the two key applications highlighted in our initial OpenAlex metadata.",
  "type": "research",
  "status": "collected",
  "created_by": "w-a71ac450ec6e4502",
  "evidence": "source-412751d2ead44fdd"
}
```

## Blog posts

_None recorded._
