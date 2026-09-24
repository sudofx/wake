# **WAKE✳︎** — Human-readable event history

> A presentation layer over `events.jsonl`. The JSONL file remains the canonical audit export.

Verified head: `c43c82dc81389262c41524a1fcdb7859f050358bb59b9324751a96aa6a52751d`

[Open the HTML version](events.html) · [Raw JSONL](events.jsonl) · [Readable state](state.md)

## Event 0003 · `experimental_regime_adopted`

**Time:** 2026-09-24T23:44:02.698520+00:00  
**ID:** `reg-df573bb03399f050`  
**Hash:** `c43c82dc81389262c41524a1fcdb7859f050358bb59b9324751a96aa6a52751d`  
**Previous hash:** `28e7f7f0bbd59d2bea7480036e5443132ff5e2ef31a360e0d4766e3ca45a6f7d`

### Payload

```json
{
  "actor": "operator",
  "adopted_at": "2026-09-24T23:44:02.698340+00:00",
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

**Time:** 2026-09-24T23:44:02.696841+00:00  
**ID:** `system`  
**Hash:** `28e7f7f0bbd59d2bea7480036e5443132ff5e2ef31a360e0d4766e3ca45a6f7d`  
**Previous hash:** `7fba9fa4a1dcfb9caad739141c49871846e4ce69f7d16c55d4d870097ca6be34`

### Payload

```json
{
  "actor": "operator",
  "mission": "Independently choose small, useful research projects from the configured topics. Look for structural relationships without assuming they exist. Develop source-backed notebooks, compare explanations, preserve uncertainty, revise weak claims, finish useful work, and choose the next step without waiting for human assignments. Distinguish findings, interpretation, analogy, and speculation.",
  "pet_name": "WAKE✳︎",
  "topic_colors": {
    "comedy": "#5fcf8d",
    "complex_systems": "#7aa2f7",
    "consciousness": "#b7d36b",
    "dance": "#8aa8ff",
    "endocrinology": "#f68c65",
    "entropy": "#b25dff",
    "epistemology": "#73daca",
    "evolutionary_biology": "#46b5ff",
    "information_thermodynamics": "#e0af68",
    "music": "#ff5bb9",
    "neurodivergence": "#ff9e64",
    "neurology": "#2ac3de",
    "philosophy": "#54d4bc",
    "prime_numbers": "#ffe574",
    "psychology": "#ff757f",
    "quantum_mechanics": "#d8c25d",
    "religion": "#f0bd75",
    "storytelling": "#9d7cd8",
    "visual_art": "#c0caf5"
  },
  "topics": [
    {
      "enabled": true,
      "id": "epistemology",
      "label": "Epistemology",
      "query": "epistemology evidence justification belief uncertainty",
      "seed_question": "What makes a belief justified when evidence is incomplete, conflicting, or filtered through imperfect observers?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "entropy",
      "label": "Entropy",
      "query": "entropy",
      "seed_question": "How do thermodynamic, statistical-mechanical, and information-theoretic definitions of entropy differ, and where are they mathematically related?",
      "source_kind": "web"
    },
    {
      "enabled": true,
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
      "enabled": true,
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
      "enabled": true,
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
    },
    {
      "enabled": true,
      "id": "complex_systems",
      "label": "Complex systems",
      "query": "complex systems emergence self-organization",
      "seed_question": "How do simple local interactions produce stable large-scale patterns in complex systems, and what distinguishes genuine emergence from a useful descriptive abstraction?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "evolutionary_biology",
      "label": "Evolutionary biology",
      "query": "evolutionary biology adaptation byproduct drift constraint",
      "seed_question": "How do evolutionary explanations distinguish adaptation, byproduct, drift, and constraint when explaining complex biological or behavioral traits?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "information_thermodynamics",
      "label": "Information thermodynamics",
      "query": "information thermodynamics",
      "seed_question": "What does Landauer's principle claim about the physical cost of erasing information, and what evidence supports its interpretation?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "music",
      "label": "Music",
      "query": "music cognition structure rhythm harmony melody",
      "seed_question": "Which structural features of music appear across cultures, and which are strongly shaped by learned musical traditions?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "comedy",
      "label": "Comedy",
      "query": "comedy humor cognition timing incongruity",
      "seed_question": "What mechanisms have researchers proposed to explain why humans find incongruity, timing, surprise, and social violation funny?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "visual_art",
      "label": "Visual art",
      "query": "visual art perception aesthetics composition",
      "seed_question": "How do composition, contrast, symmetry, ambiguity, and expectation influence how people perceive and evaluate visual art?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "storytelling",
      "label": "Storytelling",
      "query": "storytelling narrative cognition literature",
      "seed_question": "What features make narratives memorable, emotionally engaging, and coherent across different cultures and artistic traditions?",
      "source_kind": "web"
    },
    {
      "enabled": true,
      "id": "dance",
      "label": "Dance",
      "query": "dance rhythm movement cognition culture",
      "seed_question": "How do rhythm, coordinated movement, imitation, and social context shape the perception and meaning of dance?",
      "source_kind": "web"
    }
  ]
}
```

## Event 0001 · `initialized`

**Time:** 2026-09-24T23:44:02.695850+00:00  
**ID:** `system`  
**Hash:** `7fba9fa4a1dcfb9caad739141c49871846e4ce69f7d16c55d4d870097ca6be34`  
**Previous hash:** `0000000000000000000000000000000000000000000000000000000000000000`

### Payload

```json
{
  "governance": 1,
  "objective": "Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process."
}
```
