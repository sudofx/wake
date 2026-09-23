# **WAKE✳︎** — Human-readable event history

> A presentation layer over `events.jsonl`. The JSONL file remains the canonical audit export.

Verified head: `da993730ebe447b5e4bd1170995b185cd11b990811149d4bff9071474d528653`

[Open the HTML version](events.html) · [Raw JSONL](events.jsonl) · [Readable state](state.md)

## Event 0004 · `research_topics_changed`

**Time:** 2026-09-23T17:30:33.494704+00:00  
**ID:** `system`  
**Hash:** `da993730ebe447b5e4bd1170995b185cd11b990811149d4bff9071474d528653`  
**Previous hash:** `bea2cc4e272243c1ed191848c8577c869e1768bf068be8df306df822694deedf`

### Payload

```json
{
  "actor": "operator",
  "topic_colors": {
    "consciousness": "#73daca",
    "endocrinology": "#93ff74",
    "neurology": "#46b5ff",
    "philosophy": "#9d7cd8",
    "psychology": "#c0caf5",
    "religion": "#c099ff"
  },
  "topics": [
    {
      "enabled": true,
      "id": "consciousness",
      "label": "Consciousness",
      "query": "consciousness",
      "seed_question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "psychology",
      "label": "Psychology",
      "query": "psychology",
      "seed_question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "philosophy",
      "label": "Philosophy",
      "query": "philosophy",
      "seed_question": "How do falsifiability, verification, and inference to the best explanation differ as approaches to evaluating claims?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "religion",
      "label": "Religion",
      "query": "religion",
      "seed_question": "What explanations have researchers proposed for the recurrence of similar religious practices across otherwise different human societies?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "neurology",
      "label": "Neurology",
      "query": "neurology nervous system neurological disorders",
      "seed_question": "How do metabolic, hormonal, and systemic physiological changes influence neurological function and neurological disease?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "endocrinology",
      "label": "Endocrinology",
      "query": "endocrinology hormones endocrine disorders",
      "seed_question": "How do endocrine disorders and hormonal signaling affect the nervous system, and which neurological findings can arise from endocrine dysfunction?",
      "source_kind": "web"
    }
  ]
}
```

## Event 0003 · `experimental_regime_adopted`

**Time:** 2026-09-23T17:25:51.321389+00:00  
**ID:** `reg-df573bb03399f050`  
**Hash:** `bea2cc4e272243c1ed191848c8577c869e1768bf068be8df306df822694deedf`  
**Previous hash:** `f8a07eb2e0cb5536b87bedc352eafa8d43852dc7064be8674de50cbb5d5e04b8`

### Payload

```json
{
  "actor": "operator",
  "adopted_at": "2026-09-23T17:25:51.321126+00:00",
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
}
```

## Event 0002 · `charter_adopted`

**Time:** 2026-09-23T17:25:51.319266+00:00  
**ID:** `system`  
**Hash:** `f8a07eb2e0cb5536b87bedc352eafa8d43852dc7064be8674de50cbb5d5e04b8`  
**Previous hash:** `1ad431e4832edc30673f28fba670364b0d33664746551afd53f8d0db6f5f9ba5`

### Payload

```json
{
  "actor": "operator",
  "mission": "Independently choose small, useful research projects from the configured topics. Look for structural relationships without assuming they exist. Develop source-backed notebooks, compare explanations, preserve uncertainty, revise weak claims, finish useful work, and choose the next step without waiting for human assignments. Distinguish findings, interpretation, analogy, and speculation.",
  "pet_name": "WAKE✳︎",
  "topic_colors": {
    "consciousness": "#ff9e64",
    "endocrinology": "#ff757f",
    "entropy": "#e0af68",
    "information_thermodynamics": "#8aa8ff",
    "neurodivergence": "#46b5ff",
    "neurology": "#c099ff",
    "philosophy": "#9ece6a",
    "prime_numbers": "#b25dff",
    "psychology": "#2ac3de",
    "quantum_mechanics": "#93ff74",
    "religion": "#d8c25d",
    "wake_analysis": "#54d4bc"
  },
  "topics": [
    {
      "enabled": false,
      "id": "wake_analysis",
      "label": "WAKE✳︎",
      "query": "WAKE✳︎ sudofx/wake",
      "repository": "sudofx/wake",
      "seed_question": "How does WAKE✳︎ preserve useful continuity across disposable model invocations, and where does that continuity fail?",
      "source_kind": "repository"
    },
    {
      "enabled": false,
      "id": "information_thermodynamics",
      "label": "Information thermodynamics",
      "query": "information thermodynamics",
      "seed_question": "What does Landauer's principle claim about the physical cost of erasing information, and what evidence supports its interpretation?",
      "source_kind": "web"
    },
    {
      "enabled": false,
      "id": "entropy",
      "label": "Entropy",
      "query": "entropy",
      "seed_question": "How do thermodynamic, statistical-mechanical, and information-theoretic definitions of entropy differ, and where are they mathematically related?",
      "source_kind": "web"
    },
    {
      "enabled": false,
      "id": "neurodivergence",
      "label": "Neurodivergence",
      "query": "neurodivergence",
      "seed_question": "How does the neurodiversity paradigm differ from clinical pathology models, and where do the two frameworks overlap?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "consciousness",
      "label": "Consciousness",
      "query": "consciousness",
      "seed_question": "What empirical observations are major scientific theories of consciousness attempting to explain, and where do their predictions differ?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "psychology",
      "label": "Psychology",
      "query": "psychology",
      "seed_question": "How do working memory and short-term memory differ in major psychological models, and what experimental evidence motivated that distinction?",
      "source_kind": "web"
    },
    {
      "enabled": false,
      "id": "quantum_mechanics",
      "label": "Quantum mechanics",
      "query": "quantum mechanics",
      "seed_question": "What experimental observations motivated the development of quantum mechanics, and which features could classical physics not adequately explain?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "philosophy",
      "label": "Philosophy",
      "query": "philosophy",
      "seed_question": "How do falsifiability, verification, and inference to the best explanation differ as approaches to evaluating claims?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "religion",
      "label": "Religion",
      "query": "religion",
      "seed_question": "What explanations have researchers proposed for the recurrence of similar religious practices across otherwise different human societies?",
      "source_kind": "web"
    },
    {
      "enabled": false,
      "id": "prime_numbers",
      "label": "Prime numbers",
      "query": "prime numbers mathematics",
      "seed_question": "What does the prime number theorem tell us about how prime numbers become distributed as numbers grow larger, and what does it not tell us?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "neurology",
      "label": "Neurology",
      "query": "neurology nervous system neurological disorders",
      "seed_question": "How do metabolic, hormonal, and systemic physiological changes influence neurological function and neurological disease?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "endocrinology",
      "label": "Endocrinology",
      "query": "endocrinology hormones endocrine disorders",
      "seed_question": "How do endocrine disorders and hormonal signaling affect the nervous system, and which neurological findings can arise from endocrine dysfunction?",
      "source_kind": "web"
    }
  ]
}
```

## Event 0001 · `initialized`

**Time:** 2026-09-23T17:25:51.318071+00:00  
**ID:** `system`  
**Hash:** `1ad431e4832edc30673f28fba670364b0d33664746551afd53f8d0db6f5f9ba5`  
**Previous hash:** `0000000000000000000000000000000000000000000000000000000000000000`

### Payload

```json
{
  "governance": 1,
  "objective": "Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process."
}
```
