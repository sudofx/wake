# **WAKE✳︎** — Human-readable durable state

> A presentation layer over `state.json`. The JSON file remains the canonical state export.

**Version:** 0  
**Objective:** Test whether durable state and mechanically enforced rules can make fresh model invocations act as one accountable process.  
**Focus:** continuity  
**Verified head:** `db2537ede1a1142f1cbf54b125b142ea9c3a10e8a6c68c45f9bce7303798c546`

[Open the HTML version](state.html) · [Raw JSON](state.json) · [Readable history](events.md)

## Beliefs

_None recorded._

## Commitments

_None recorded._

## Projects

_None recorded._

## Acquisition capability

_None recorded._

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

## Notebooks

_None recorded._

## Invocations

### `w-7ca5a90625e94665`

```json
{
  "base_version": 0,
  "charged": true,
  "context_delivery": {
    "delivered_context_chars": 19299,
    "delivered_request_chars": 45214,
    "mode": "rich",
    "omitted_categories": [],
    "provenance_policy": null,
    "rich_context_chars": 45214,
    "working_set_chars": 422
  },
  "experimental_regime": {
    "actor": "operator",
    "adopted_at": "2026-09-24T16:31:28.319996+00:00",
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
  "id": "w-7ca5a90625e94665",
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
  "process_id": 2043,
  "provider": "gemini",
  "quota_day": "2026-09-24",
  "request_hash": "5d528685eb56670b8c14bfcc1609f28e3fec80e5526980c25be7f486f00ca162",
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
    "attention": {},
    "attention_saturation_threshold": 5,
    "capability_blocked_topics": [],
    "cooldown_other_attempts": 3,
    "current_topic_unconfigured": false,
    "deferred_topics": [],
    "enforce_selected_topic": false,
    "hard_rejection_threshold": 5,
    "parked": {},
    "reason": "current durable project topic remains eligible",
    "rotation_required": false,
    "saturation_release_condition": "accepted notebook or ordinary publication on another topic",
    "selected_topic": "epistemology",
    "temporal": {
      "anchor_seq": 11,
      "anchor_time": "2026-09-24T16:41:25.768712+00:00",
      "anchor_version": 0,
      "effective_seconds": 597.448716
    },
    "temporal_use": "observational; no time signal changes Squirrel eligibility yet"
  },
  "temporal": {
    "cycle_distance": 0,
    "effective_elapsed_seconds": 597.448716,
    "effective_scale": 1.0,
    "effective_seconds_total": 597.448716,
    "intervening_events": {
      "accepted": 0,
      "failed": 0,
      "observation": 6,
      "rejected": 0,
      "research_collected": 0,
      "squirrel_assessed": 0,
      "total": 7
    },
    "observed_at": "2026-09-24T16:41:25.768712+00:00",
    "previous_anchor_time": "2026-09-24T16:31:28.319996+00:00",
    "regime_id": "reg-df573bb03399f050",
    "wall_elapsed_seconds": 597.448716
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
    "delivered_context_chars": 19299,
    "inquiry_drive_project_count": 0,
    "mode": "rich",
    "retrieval_candidate_count": 0,
    "retrieval_evidence_count": 0,
    "retrieval_trigger_counts": {},
    "trust_compact_candidate_count": 0,
    "trust_compact_evidence_root_count": 0,
    "trust_compact_settled_count": 0,
    "working_set_chars": 422,
    "working_to_delivered_ratio": 0.0219
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
  "time": "2026-09-24T16:41:25.779743+00:00",
  "provider_attempts": [
    {
      "category": "server",
      "elapsed_ms": 18401,
      "http_status": 503,
      "model": "gemini-3.8-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 49790,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 1157,
      "http_status": 503,
      "model": "gemini-3.5-flash",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 49790,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    },
    {
      "category": "server",
      "elapsed_ms": 8296,
      "http_status": 503,
      "model": "gemini-3.1-flash-lite",
      "provider_error": {
        "code": 503,
        "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
        "status": "UNAVAILABLE"
      },
      "request_payload_bytes": 49790,
      "response_bytes_captured": 198,
      "result": "transient_failure"
    }
  ],
  "provider_requests_sent": 3,
  "finished": "2026-09-24T16:42:05.161971+00:00",
  "reason": "Gemini temporarily unavailable; wake deferred",
  "provider_error": {
    "category": "server",
    "elapsed_ms": 8296,
    "http_status": 503,
    "model": "gemini-3.1-flash-lite",
    "provider_attempts": [
      {
        "category": "server",
        "elapsed_ms": 18401,
        "http_status": 503,
        "model": "gemini-3.8-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 49790,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 1157,
        "http_status": 503,
        "model": "gemini-3.5-flash",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 49790,
        "response_bytes_captured": 198,
        "result": "transient_failure"
      },
      {
        "category": "server",
        "elapsed_ms": 8296,
        "http_status": 503,
        "model": "gemini-3.1-flash-lite",
        "provider_error": {
          "code": 503,
          "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
          "status": "UNAVAILABLE"
        },
        "request_payload_bytes": 49790,
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
    "request_payload_bytes": 49790,
    "response_bytes_captured": 198,
    "result": "transient_failure"
  }
}
```

## Evidence

### `source-2278e38353394608`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":6105,\\\"suggestion\\\":\\\"entry\\\",\\\"suggestionsnippet\\\":\\\"entry\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy\\\",\\\"pageid\\\":9891,\\\"size\\\":115933,\\\"wordcount\\\":14396,\\\"snippet\\\":\\\"\\nEntropy\\nis a thermodynamic state variable that quantifies the probabilistic distribution of accessible microstates in a system. The term and the concept\\\",\\\"timestamp\\\":\\\"2026-09-21T14:49:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (information theory)\\\",\\\"pageid\\\":15445,\\\"size\\\":72351,\\\"wordcount\\\":10078,\\\"snippet\\\":\\\"In information theory, the\\nentropy\\nof a random variable quantifies the average level of uncertainty or information associated with the variable's potential\\\",\\\"timestamp\\\":\\\"2026-08-01T11:28:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Second law of thermodynamics\\\",\\\"pageid\\\":133017,\\\"size\\\":119048,\\\"wordcount\\\":16416,\\\"snippet\\\":\\\"appear below. The second law of thermodynamics establishes the concept of\\nentropy\\nas a physical property of a thermodynamic system. It predicts whether processes\\\",\\\"timestamp\\\":\\\"2026-09-22T12:26:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy (disambiguation)\\\",\\\"pageid\\\":302133,\\\"size\\\":5540,\\\"wordcount\\\":726,\\\"snippet\\\":\\\"Look up\\nentropy\\nin Wiktionary, the free dictionary.\\nEntropy\\nis a fundamental scientific concept that quantifies the statistical probability of a system's\\\",\\\"timestamp\\\":\\\"2026-04-29T22:10:25Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"R\\\\u00e9nyi entropy\\\",\\\"pageid\\\":1731689,\\\"size\\\":27228,\\\"wordcount\\\":4205,\\\"snippet\\\":\\\"R\\\\u00e9nyi\\nentropy\\nis a quantity that generalizes various notions of\\nentropy\\n, including Hartley\\nentropy\\n, Shannon\\nentropy\\n, collision\\nentropy\\n, and min-\\nentropy\\n. The\\\",\\\"timestamp\\\":\\\"2026-08-13T19:55:15Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Cross-entropy\\\",\\\"pageid\\\":1735250,\\\"size\\\":19871,\\\"wordcount\\\":3496,\\\"snippet\\\":\\\"In information theory, the cross-\\nentropy\\nbetween two probability distributions p {\\\\\\\\displaystyle p} and q {\\\\\\\\displaystyle q} , over the same underlying\\\",\\\"timestamp\\\":\\\"2026-09-15T02:14:33Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Information theory\\\",\\\"pageid\\\":14773,\\\"size\\\":88576,\\\"wordcount\\\":10416,\\\"snippet\\\":\\\"theory is\\nentropy\\n. In Shannon's formulation,\\nentropy\\nis equal to the lack of information about an event. In the above coin flip example, the\\nentropy\\nin the\\\",\\\"timestamp\\\":\\\"2026-09-19T03:01:03Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Social entropy\\\",\\\"pageid\\\":12447991,\\\"size\\\":1975,\\\"wordcount\\\":200,\\\"snippet\\\":\\\"\\nentropy\\nis a sociological theory that evaluates social behaviours using a method based on the second law of thermodynamics. The equivalent of\\nentropy\\n\\\",\\\"timestamp\\\":\\\"2026-05-03T07:04:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Entropy unit\\\",\\\"pageid\\\":1886799,\\\"size\\\":521,\\\"wordcount\\\":71,\\\"snippet\\\":\\\"The\\nentropy\\nunit is a non-S.I. unit of thermodynamic\\nentropy\\n, usually denoted by \\\"e.u.\\\" or \\\"eU\\\" and equal to one calorie per kelvin per mole, or 4.184\\\",\\\"timestamp\\\":\\\"2024-11-06T04:45:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Holographic principle\\\",\\\"pageid\\\":14286,\\\"size\\\":36292,\\\"wordcount\\\":4216,\\\"snippet\\\":\\\"bound of black hole thermodynamics, which conjectures that the maximum\\nentropy\\nin any region scales with the radius squared, rather than cubed as might\\\",\\\"timestamp\\\":\\\"2026-05-16T11:15:06Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"77c9a045733efbcd677f02a982fcc62015d613dde5d5d7cdbbac6ca6afc72915\", \"verification_required\": true, \"topic_domain\": \"entropy\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-2278e38353394608",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=entropy&format=json",
  "version": 0,
  "time": "2026-09-24T16:41:22.490068+00:00"
}
```

### `source-1b9adb9815f94aed`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":239491,\\\"suggestion\\\":\\\"religious\\\",\\\"suggestionsnippet\\\":\\\"religious\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Religion\\\",\\\"pageid\\\":25414,\\\"size\\\":187367,\\\"wordcount\\\":19574,\\\"snippet\\\":\\\"\\nReligion\\nis a range of social-cultural systems, including designated behaviors and practices, ethics, morals, beliefs, worldviews, texts, sanctified places\\\",\\\"timestamp\\\":\\\"2026-09-21T06:41:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Civil religion\\\",\\\"pageid\\\":185692,\\\"size\\\":34053,\\\"wordcount\\\":3846,\\\"snippet\\\":\\\"Civil\\nreligion\\n, also referred to as a civic\\nreligion\\n, is the implicit religious values of a nation, as expressed through public rituals, symbols (such\\\",\\\"timestamp\\\":\\\"2026-06-25T16:06:42Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Abrahamic religions\\\",\\\"pageid\\\":13906453,\\\"size\\\":112861,\\\"wordcount\\\":10868,\\\"snippet\\\":\\\"The Abrahamic\\nreligions\\nare a set of monotheistic\\nreligions\\nthat respect or admire the religious figure Abraham as a patriarch and/or as a prophet, namely\\\",\\\"timestamp\\\":\\\"2026-09-18T17:21:29Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in China\\\",\\\"pageid\\\":367843,\\\"size\\\":300336,\\\"wordcount\\\":34062,\\\"snippet\\\":\\\"\\nReligion\\nin China by self-identified affiliation (Pew Research Center 2023) No\\nreligion\\n(93.0%) Buddhism (3.70%) Folk beliefs (0.20%) Christianity (1\\\",\\\"timestamp\\\":\\\"2026-09-12T03:20:45Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Yoruba religion\\\",\\\"pageid\\\":682534,\\\"size\\\":64332,\\\"wordcount\\\":4734,\\\"snippet\\\":\\\"The Yor\\\\u00f9b\\\\u00e1\\nreligion\\n(Yoruba: \\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e [\\\\u00ec\\\\u0283\\\\u025b\\\\u0300\\\\u0283\\\\u0113]), West African Orisa (\\\\u00d2r\\\\u00ec\\\\u1e63\\\\u00e0 [\\\\u00f2\\\\u027e\\\\u00ec\\\\u0283\\\\u00e0]), or Isese (\\\\u00cc\\\\u1e63\\\\u1eb9\\\\u0300\\\\u1e63e), comprises the traditional religious and spiritual\\\",\\\"timestamp\\\":\\\"2026-09-15T17:38:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Canaanite religion\\\",\\\"pageid\\\":2375688,\\\"size\\\":38557,\\\"wordcount\\\":4353,\\\"snippet\\\":\\\"The\\nreligion\\nand mythic beliefs of the people in the land of Canaan in the southern Levant during approximately the first three millennia\\\\u00a0BCE were polytheistic\\\",\\\"timestamp\\\":\\\"2026-09-08T21:35:17Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Religion in India\\\",\\\"pageid\\\":10710364,\\\"size\\\":125253,\\\"wordcount\\\":11197,\\\"snippet\\\":\\\"\\nReligion\\nin India (2011 census) Hinduism (79.8%) Islam (14.2%) Christianity (2.30%) Sikhism (1.70%) Buddhism (0.70%) Sarnaism (0.40%) Jainism (0.40%) Other\\\",\\\"timestamp\\\":\\\"2026-09-11T19:59:55Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Hellenistic religion\\\",\\\"pageid\\\":7491899,\\\"size\\\":17856,\\\"wordcount\\\":2083,\\\"snippet\\\":\\\"The concept of Hellenistic\\nreligion\\nas the late form of Ancient Greek\\nreligion\\ncovers any of the various systems of beliefs and practices of the people\\\",\\\"timestamp\\\":\\\"2026-08-19T12:26:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"State religion\\\",\\\"pageid\\\":292285,\\\"size\\\":161900,\\\"wordcount\\\":12907,\\\"snippet\\\":\\\"state\\nreligion\\n(also called official\\nreligion\\n) is a\\nreligion\\nor creed officially endorsed by a sovereign state. A state with an official\\nreligion\\n(also\\\",\\\"timestamp\\\":\\\"2026-09-20T01:30:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Comparative religion\\\",\\\"pageid\\\":186861,\\\"size\\\":39435,\\\"wordcount\\\":4234,\\\"snippet\\\":\\\"Abrahamic\\nreligions\\nand Iranian\\nreligions\\n), Indian\\nreligions\\n, East Asian\\nreligions\\n, African\\nreligions\\n, American\\nreligions\\n, Oceanic\\nreligions\\n, and classical\\\",\\\"timestamp\\\":\\\"2026-07-25T01:00:19Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"6951d22534607d8cbe5887289f422f2c3ec714d6ca885fa119311ed4633a884a\", \"verification_required\": true, \"topic_domain\": \"religion\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-1b9adb9815f94aed",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=religion&format=json",
  "version": 0,
  "time": "2026-09-24T16:41:23.150138+00:00"
}
```

### `source-d9e46c012db94a86`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":4980},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Prime number\\\",\\\"pageid\\\":23666,\\\"size\\\":128021,\\\"wordcount\\\":14786,\\\"snippet\\\":\\\"A\\nprime\\nnumber (or a\\nprime\\n) is a natural number greater than 1 that is not a product of two smaller natural\\nnumbers\\n. A natural number greater than 1 that\\\",\\\"timestamp\\\":\\\"2026-09-21T15:01:53Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of Mersenne primes and perfect numbers\\\",\\\"pageid\\\":68906231,\\\"size\\\":52386,\\\"wordcount\\\":2900,\\\"snippet\\\":\\\"Mersenne\\nprimes\\nand perfect\\nnumbers\\nare two deeply interlinked types of natural\\nnumbers\\nin number theory. Mersenne\\nprimes\\n, named after the friar Marin\\\",\\\"timestamp\\\":\\\"2026-09-17T04:54:59Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of prime numbers\\\",\\\"pageid\\\":442370,\\\"size\\\":108090,\\\"wordcount\\\":6019,\\\"snippet\\\":\\\"This is a list of articles about\\nprime\\nnumbers\\n. A\\nprime\\nnumber (or\\nprime\\n) is a natural number greater than 1 that has no divisors other than 1 and itself\\\",\\\"timestamp\\\":\\\"2026-09-22T20:55:26Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Perfect number\\\",\\\"pageid\\\":23670,\\\"size\\\":39840,\\\"wordcount\\\":5531,\\\"snippet\\\":\\\"odd Perfect\\nPrime\\nNumbers\\n\\\".\\nMathematics\\nof Computation. 27 (124): 951\\\\u2013953. doi:10.2307/2005530. JSTOR\\\\u00a02005530. Riele, H.J.J. \\\"Perfect\\nNumbers\\nand Aliquot\\\",\\\"timestamp\\\":\\\"2026-09-12T00:36:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Sexy primes\\\",\\\"pageid\\\":343116,\\\"size\\\":3815,\\\"wordcount\\\":453,\\\"snippet\\\":\\\"sexy\\nprimes\\nare\\nprime\\nnumbers\\nthat differ from another\\nprime\\nby 6. For example, the\\nnumbers\\n5 and 11 are a pair of sexy\\nprimes\\n, because both are\\nprime\\nand\\\",\\\"timestamp\\\":\\\"2026-09-18T20:27:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Wieferich prime\\\",\\\"pageid\\\":323631,\\\"size\\\":43265,\\\"wordcount\\\":4566,\\\"snippet\\\":\\\"\\nprimes\\nand various other topics in\\nmathematics\\nhave been discovered, including other types of\\nnumbers\\nand\\nprimes\\n, such as Mersenne and Fermat\\nnumbers\\n\\\",\\\"timestamp\\\":\\\"2026-08-21T10:09:34Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Number\\\",\\\"pageid\\\":21690,\\\"size\\\":111928,\\\"wordcount\\\":11702,\\\"snippet\\\":\\\"A number is a\\nmathematical\\nobject used to count, measure, and label. The most basic examples are the natural\\nnumbers\\n: 1, 2, 3, 4, 5, and so forth. Individual\\\",\\\"timestamp\\\":\\\"2026-09-21T13:55:05Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Closing the Gap: The Quest to Understand Prime Numbers\\\",\\\"pageid\\\":63087914,\\\"size\\\":5974,\\\"wordcount\\\":617,\\\"snippet\\\":\\\"Closing the Gap: The Quest to Understand\\nPrime\\nNumbers\\nis a book on\\nprime\\nnumbers\\nand\\nprime\\ngaps by Vicky Neale, published in 2017 by the Oxford University\\\",\\\"timestamp\\\":\\\"2026-09-11T00:17:48Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Fermat number\\\",\\\"pageid\\\":91127,\\\"size\\\":43237,\\\"wordcount\\\":3868,\\\"snippet\\\":\\\"(2001), \\\"Another note on the greatest\\nprime\\nfactors of Fermat\\nnumbers\\n\\\", Southeast Asian Bulletin of\\nMathematics\\n, 25 (1): 111\\\\u2013115, doi:10.1007/s10012-001-0111-4\\\",\\\"timestamp\\\":\\\"2026-09-21T16:11:11Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Mersenne prime\\\",\\\"pageid\\\":18908,\\\"size\\\":78122,\\\"wordcount\\\":6673,\\\"snippet\\\":\\\"In\\nmathematics\\n, a Mersenne\\nprime\\nis a\\nprime\\nnumber that is one less than a power of two. That is, it is a\\nprime\\nnumber of the form Mn = 2n \\\\u2212 1 for some\\\",\\\"timestamp\\\":\\\"2026-09-08T20:24:47Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"69349f29a09d3078740d0401e0e95acfb8008acdb1fae49e893cb6d3bf6a6c58\", \"verification_required\": true, \"topic_domain\": \"prime_numbers\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": [\"doi:10.2307/2005530\", \"doi:10.1007/s10012-001-0111-4\"]}",
  "id": "source-d9e46c012db94a86",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=prime+numbers+mathematics&format=json",
  "version": 0,
  "time": "2026-09-24T16:41:23.733142+00:00"
}
```

### `source-6a2eb9ec108942e9`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=storytelling+narrative+cognition+literature&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":86,\\\"suggestion\\\":\\\"storytelling narrative coalition literature\\\",\\\"suggestionsnippet\\\":\\\"storytelling narrative\\ncoalition\\nliterature\\\"},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Fiction\\\",\\\"pageid\\\":18949461,\\\"size\\\":35712,\\\"wordcount\\\":3771,\\\"snippet\\\":\\\"non-fiction.\\nStorytelling\\nhas existed in all human cultures, and each culture incorporates different elements of truth and fiction into\\nstorytelling\\n. Early\\\",\\\"timestamp\\\":\\\"2026-09-07T19:11:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Narrative identity\\\",\\\"pageid\\\":35716364,\\\"size\\\":60455,\\\"wordcount\\\":7308,\\\"snippet\\\":\\\"on the affective tone of life\\nnarrative\\nmemories: Early adolescence and older age are more negative\\\". Memory and\\nCognition\\n. 51 (6): 1265\\\\u20131286. doi:10\\\",\\\"timestamp\\\":\\\"2026-09-16T15:09:54Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Narratology\\\",\\\"pageid\\\":718763,\\\"size\\\":23172,\\\"wordcount\\\":2691,\\\"snippet\\\":\\\"Digital-media theorist and professor Janet Murray theorized a shift in\\nstorytelling\\nand\\nnarrative\\nstructure in the twentieth century as a result of scientific advancement\\\",\\\"timestamp\\\":\\\"2026-06-21T07:57:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ancient literature\\\",\\\"pageid\\\":3709305,\\\"size\\\":49644,\\\"wordcount\\\":4634,\\\"snippet\\\":\\\"Ancient\\nliterature\\ncomprises religious and scientific documents, tales, poetry and plays, royal edicts and declarations, and other forms of writing that\\\",\\\"timestamp\\\":\\\"2026-06-29T20:43:46Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Role-playing game\\\",\\\"pageid\\\":25475,\\\"size\\\":38009,\\\"wordcount\\\":4559,\\\"snippet\\\":\\\"form of interactive and collaborative\\nstorytelling\\n. Events, roles, and\\nnarrative\\nstructure give a sense of a\\nnarrative\\nexperience, and the game need not have\\\",\\\"timestamp\\\":\\\"2026-09-20T05:14:32Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Suspense\\\",\\\"pageid\\\":4450450,\\\"size\\\":10990,\\\"wordcount\\\":1207,\\\"snippet\\\":\\\"audience feels sympathy. However, suspense is not exclusive to\\nnarratives\\n. In\\nliterature\\n, films, television, and plays, suspense is a major device for\\\",\\\"timestamp\\\":\\\"2026-09-10T05:31:31Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Children's literature\\\",\\\"pageid\\\":52847,\\\"size\\\":167603,\\\"wordcount\\\":18216,\\\"snippet\\\":\\\"Machine Children's\\nliterature\\nArchived 2016-06-17 at the Wayback Machine at the British Library Children's\\nLiterature\\n, Culture, and\\nCognition\\n(CLCC) Database\\\",\\\"timestamp\\\":\\\"2026-09-21T04:25:10Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Soma (video game)\\\",\\\"pageid\\\":5649586,\\\"size\\\":41063,\\\"wordcount\\\":3882,\\\"snippet\\\":\\\"Cody (22 June 2023). \\\"Games ad Critical\\nLiterature\\n: Playing with Transhumanism, Embodied\\nCognition\\n, and\\nNarrative\\nDifference in SOMA\\\". In Ghosal, Torsa\\\",\\\"timestamp\\\":\\\"2026-07-09T19:08:06Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Immersive learning\\\",\\\"pageid\\\":64345811,\\\"size\\\":22110,\\\"wordcount\\\":2264,\\\"snippet\\\":\\\"structured by the audience's own\\ncognition\\n. Also, within Ryan's book, the cognitive immersion created by\\nnarrative\\nis categorized into three kinds: spatial\\\",\\\"timestamp\\\":\\\"2025-11-26T22:52:24Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dramatization\\\",\\\"pageid\\\":57618166,\\\"size\\\":5558,\\\"wordcount\\\":732,\\\"snippet\\\":\\\"emphasis on spontaneity,\\ncognition\\n, action, identification, dialogue and sequence of events. Greater appreciation of the\\nliterature\\nmay then occur. Children\\\",\\\"timestamp\\\":\\\"2026-03-12T01:42:08Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"c2faf4430f852c820b2f62d89753abc6a9bf74973f2d45d891e79a3817faf1a5\", \"verification_required\": true, \"topic_domain\": \"storytelling\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-6a2eb9ec108942e9",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=storytelling+narrative+cognition+literature&format=json",
  "version": 0,
  "time": "2026-09-24T16:41:24.411413+00:00"
}
```

### `source-d1f0be57fffa4038`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=visual+art+perception+aesthetics+composition&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":393},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Art\\\",\\\"pageid\\\":752,\\\"size\\\":132424,\\\"wordcount\\\":14439,\\\"snippet\\\":\\\"spiritually, or philosophically motivated\\nart\\n; to create a sense of beauty (see\\naesthetics\\n); to explore the nature of\\nperception\\n; for pleasure; or to generate strong\\\",\\\"timestamp\\\":\\\"2026-09-09T08:09:22Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Psychology of art\\\",\\\"pageid\\\":8165347,\\\"size\\\":90900,\\\"wordcount\\\":11467,\\\"snippet\\\":\\\"The psychology of\\nart\\nis the scientific study of cognitive and emotional processes precipitated by the sensory\\nperception\\nof aesthetic artefacts, such\\\",\\\"timestamp\\\":\\\"2026-09-21T20:46:36Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Aesthetics\\\",\\\"pageid\\\":2130,\\\"size\\\":149323,\\\"wordcount\\\":16275,\\\"snippet\\\":\\\"\\nAesthetics\\nis the branch of philosophy that studies beauty, taste, and related phenomena. In a broad sense, it includes the philosophy of\\nart\\n, which examines\\\",\\\"timestamp\\\":\\\"2026-09-18T11:00:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Tribal art\\\",\\\"pageid\\\":24811443,\\\"size\\\":11752,\\\"wordcount\\\":1204,\\\"snippet\\\":\\\"Tribal\\nart\\nis the\\nvisual\\narts and material culture of indigenous people. Also known as non-Western\\nart\\nor ethnographic\\nart\\n, or, controversially, primitive\\\",\\\"timestamp\\\":\\\"2025-12-21T03:03:57Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Rudolf Arnheim\\\",\\\"pageid\\\":467254,\\\"size\\\":17187,\\\"wordcount\\\":2040,\\\"snippet\\\":\\\"have included\\nVisual\\nThinking (1969), and The Power of the Center: A Study of\\nComposition\\nin the\\nVisual\\nArts (1982).\\nArt\\nand\\nVisual\\nPerception\\nwas revised\\\",\\\"timestamp\\\":\\\"2026-09-02T04:51:51Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Style (visual arts)\\\",\\\"pageid\\\":147860,\\\"size\\\":37916,\\\"wordcount\\\":4617,\\\"snippet\\\":\\\"\\nvisual\\nappearance of a work of\\nart\\nthat relates it to other works by the same artist or one from the same period, training, location, \\\"school\\\",\\nart\\nmovement\\\",\\\"timestamp\\\":\\\"2026-09-10T04:00:14Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of aesthetics\\\",\\\"pageid\\\":3376041,\\\"size\\\":78283,\\\"wordcount\\\":10808,\\\"snippet\\\":\\\"This is a history of\\naesthetics\\n. The first important contributions to aesthetic theory are usually considered to stem from philosophers in Ancient Greece\\\",\\\"timestamp\\\":\\\"2026-09-11T08:39:27Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Ma (negative space)\\\",\\\"pageid\\\":14904296,\\\"size\\\":8650,\\\"wordcount\\\":904,\\\"snippet\\\":\\\"space, ma may also refer to the\\nperception\\nof a space, gap or interval, without necessarily requiring a physical\\ncompositional\\nelement. This results in the\\\",\\\"timestamp\\\":\\\"2026-09-22T04:45:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"History of the nude in art\\\",\\\"pageid\\\":71247922,\\\"size\\\":337730,\\\"wordcount\\\":43252,\\\"snippet\\\":\\\"academic classifications of works of\\nart\\n. Nudity in\\nart\\nhas generally reflected the social standards for\\naesthetics\\nand morality of the era in which the\\\",\\\"timestamp\\\":\\\"2026-09-19T06:09:38Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Applied aesthetics\\\",\\\"pageid\\\":17741443,\\\"size\\\":28492,\\\"wordcount\\\":3644,\\\"snippet\\\":\\\"Applied\\naesthetics\\nis the application of the branch of philosophy of\\naesthetics\\nto cultural constructs. In a variety of fields, artifacts (whether physical\\\",\\\"timestamp\\\":\\\"2026-08-07T10:16:52Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"2b8f8bc5eede1ad3041cec66e068af65ce023139e574441d9453dd4f916a2a60\", \"verification_required\": true, \"topic_domain\": \"visual_art\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-d1f0be57fffa4038",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=visual+art+perception+aesthetics+composition&format=json",
  "version": 0,
  "time": "2026-09-24T16:41:25.024789+00:00"
}
```

### `source-c5a1c1a9855e4029`

```json
{
  "actor": "collector",
  "content": "{\"url\": \"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json\", \"scope\": \"extracted web-page text; may be incomplete\", \"excerpt\": \"{\\\"batchcomplete\\\":\\\"\\\",\\\"continue\\\":{\\\"sroffset\\\":10,\\\"continue\\\":\\\"-||\\\"},\\\"query\\\":{\\\"searchinfo\\\":{\\\"totalhits\\\":3371},\\\"search\\\":[{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological disorder\\\",\\\"pageid\\\":19572333,\\\"size\\\":21181,\\\"wordcount\\\":2085,\\\"snippet\\\":\\\"A\\nneurological\\ndisorder\\nis any\\ndisorder\\nof the\\nnervous\\nsystem\\n. Structural, biochemical or electrical abnormalities in the brain, spinal cord, or other\\\",\\\"timestamp\\\":\\\"2026-07-13T18:36:56Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Functional neurological symptom disorder\\\",\\\"pageid\\\":49594540,\\\"size\\\":23378,\\\"wordcount\\\":2498,\\\"snippet\\\":\\\"\\\"Functional\\nneurologic\\ndisorders\\n/conversion\\ndisorder\\n- Symptoms and causes\\\". Mayo Clinic. Retrieved 2022-01-04. \\\"Functional\\nneurological\\nsymptom\\ndisorder\\n\\\". Medicalnewstoday\\\",\\\"timestamp\\\":\\\"2026-09-13T17:05:43Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"List of neurological conditions and disorders\\\",\\\"pageid\\\":56335,\\\"size\\\":13517,\\\"wordcount\\\":1152,\\\"snippet\\\":\\\"This is a list of major and frequently observed\\nneurological\\ndisorders\\n(e.g., Alzheimer's disease), symptoms (e.g., back pain), signs (e.g., aphasia) and\\\",\\\"timestamp\\\":\\\"2026-06-20T20:53:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurology\\\",\\\"pageid\\\":21226,\\\"size\\\":28663,\\\"wordcount\\\":2752,\\\"snippet\\\":\\\"and treat\\nneurological\\ndisorders\\n. Neurologists diagnose and treat myriad\\nneurologic\\nconditions, including stroke, epilepsy, movement\\ndisorders\\nsuch as Parkinson's\\\",\\\"timestamp\\\":\\\"2026-09-24T16:30:07Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Central nervous system disease\\\",\\\"pageid\\\":17681122,\\\"size\\\":31068,\\\"wordcount\\\":3102,\\\"snippet\\\":\\\"Central\\nnervous\\nsystem\\ndiseases or central\\nnervous\\nsystem\\ndisorders\\nare a group of\\nneurological\\ndisorders\\nthat affect the structure or function of the\\\",\\\"timestamp\\\":\\\"2026-08-15T09:05:37Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Paraneoplastic syndrome\\\",\\\"pageid\\\":11520228,\\\"size\\\":29092,\\\"wordcount\\\":2366,\\\"snippet\\\":\\\"to the peripheral\\nnervous\\nsystem\\n. Symptomatic features of paraneoplastic syndrome cultivate in four ways: endocrine,\\nneurological\\n, mucocutaneous, and\\\",\\\"timestamp\\\":\\\"2026-03-07T21:14:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Dysautonomia\\\",\\\"pageid\\\":410746,\\\"size\\\":32867,\\\"wordcount\\\":2908,\\\"snippet\\\":\\\"inherited or degenerative\\nneurologic\\ndiseases (primary dysautonomia) or injury of the autonomic\\nnervous\\nsystem\\nfrom an acquired\\ndisorder\\n(secondary dysautonomia)\\\",\\\"timestamp\\\":\\\"2026-08-12T22:17:01Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Multiple system atrophy\\\",\\\"pageid\\\":861802,\\\"size\\\":57832,\\\"wordcount\\\":5875,\\\"snippet\\\":\\\"Many people affected by MSA experience dysfunction of the autonomic\\nnervous\\nsystem\\n, which commonly manifests as orthostatic hypotension, impotence, loss\\\",\\\"timestamp\\\":\\\"2026-09-10T19:21:28Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Neurological examination\\\",\\\"pageid\\\":3893700,\\\"size\\\":11559,\\\"wordcount\\\":956,\\\"snippet\\\":\\\"A\\nneurological\\nexamination is the assessment of sensory neuron and motor responses, especially reflexes, to determine whether the\\nnervous\\nsystem\\nis impaired\\\",\\\"timestamp\\\":\\\"2026-08-29T23:18:49Z\\\"},{\\\"ns\\\":0,\\\"title\\\":\\\"Nervous system disease\\\",\\\"pageid\\\":18881907,\\\"size\\\":11932,\\\"wordcount\\\":1141,\\\"snippet\\\":\\\"\\nNervous\\nsystem\\ndiseases, also known as\\nnervous\\nsystem\\nor\\nneurological\\ndisorders\\n, refers to a small class of medical conditions affecting the\\nnervous\\nsystem\\\",\\\"timestamp\\\":\\\"2025-10-20T08:53:25Z\\\"}]}}\", \"excerpt_truncated\": false, \"source_sha256\": \"56f7a58d6f5bcbcf78619182dc12ff07e1c0d06baf1de076dbb72262b1e91d51\", \"verification_required\": true, \"topic_domain\": \"neurology\", \"evidence_role\": \"discovery\", \"host_tier\": \"discovery\", \"persistent_identifiers\": []}",
  "id": "source-c5a1c1a9855e4029",
  "scope": "collected",
  "source": "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=neurology+nervous+system+neurological+disorders&format=json",
  "version": 0,
  "time": "2026-09-24T16:41:25.765089+00:00"
}
```

### `r-7ca5a90625e94665`

```json
{
  "actor": "runtime",
  "content": "{\"base_version\":0,\"inherited_commitments\":[],\"invocation\":\"w-7ca5a90625e94665\",\"previous_head\":\"7b3a0f07a407e001c8f3dd339175d094ccaa458f2947a13998308e50e7c339c8\",\"process_id\":2043,\"scope\":\"Receipt proves state delivery to the provider boundary, not model comprehension.\"}",
  "id": "r-7ca5a90625e94665",
  "source": "runtime:continuity",
  "version": 0,
  "time": "2026-09-24T16:41:25.774121+00:00"
}
```

## Journal

_None recorded._

## Research

_None recorded._

## Blog posts

_None recorded._
