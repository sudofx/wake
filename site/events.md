# **WAKE✳︎** — Human-readable event history

> A presentation layer over `events.jsonl`. The JSONL file remains the canonical audit export.

Verified head: `86e35aed3a20137f6deb0451ae64189d63e5e7a7559002f6fe7d49a9d8f2821e`

[Open the HTML version](events.html) · [Raw JSONL](events.jsonl) · [Readable state](state.md)

## Event 0002 · `charter_adopted`

**Time:** 2026-09-17T16:05:32.452246+00:00  
**ID:** `system`  
**Hash:** `86e35aed3a20137f6deb0451ae64189d63e5e7a7559002f6fe7d49a9d8f2821e`  
**Previous hash:** `605cb78574c3726a33c4ee27e6679959350b35cf526b26443b4a400adb4d7ba6`

### Payload

```json
{
  "actor": "operator",
  "mission": "Independently choose small, useful research projects from the configured topics. Look for structural relationships without assuming they exist. Develop source-backed notebooks, compare explanations, preserve uncertainty, revise weak claims, finish useful work, and choose the next step without waiting for human assignments. Distinguish findings, interpretation, analogy, and speculation.",
  "pet_name": "WAKE✳︎",
  "topics": [
    {
      "id": "cellular_automata",
      "label": "Cellular automata",
      "query": "cellular automata"
    },
    {
      "id": "symmetry",
      "label": "Symmetry",
      "query": "symmetry"
    },
    {
      "id": "error_correction",
      "label": "Error correction",
      "query": "error correction"
    },
    {
      "id": "ant_colonies",
      "label": "Ant colonies",
      "query": "ant colonies"
    },
    {
      "id": "compression",
      "label": "Compression",
      "query": "information compression"
    },
    {
      "id": "entropy",
      "label": "Entropy",
      "query": "entropy"
    },
    {
      "id": "wake_analysis",
      "label": "WAKE✳︎",
      "query": "WAKE"
    }
  ]
}
```

## Event 0001 · `initialized`

**Time:** 2026-09-17T16:05:32.339903+00:00  
**ID:** `system`  
**Hash:** `605cb78574c3726a33c4ee27e6679959350b35cf526b26443b4a400adb4d7ba6`  
**Previous hash:** `0000000000000000000000000000000000000000000000000000000000000000`

### Payload

```json
{
  "governance": 1,
  "objective": "Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process."
}
```
