# Experimental research expansion

WAKE now starts from three research themes. They invite criticism and independent
problem formulation without granting models more authority. A seed is a starting
question, not an assigned conclusion or permanent objective.

| Topic ID | Starting question | Hosted group |
| --- | --- | --- |
| `assumption_challenge` | Can an intelligent system identify a foundational assumption underlying its own reasoning or operation, demonstrate that the assumption is inadequate, and develop a better alternative? | Groups 100 and 200 |
| `emergent_preferences` | Can accumulated experience produce stable, observable preferences in an intelligent process without those preferences being explicitly programmed? | Groups 200 and 300 |
| `unassigned_problem` | Can an intelligent process independently identify a worthwhile problem that nobody explicitly assigned, recognize its significance, and sustain an investigation toward resolving it? | Groups 100 and 300 |

The experiment ID is `research-expansion-2026-10`. Each group has two enabled themes, allowing Attention to rotate away from a
saturated or capability-blocked topic without changing its policy. Each theme
appears in two parent/child groups. Members share their group's themes
but retain independently attributed records. Twelve nodes are not twelve
independent scientific replications. No new node or authority database is added.

## Starting fresh versus changing configuration

The operator explicitly requested discarding hosted research and restarting at
cycle zero with no backup. That overrides the handoff's initial preservation
requirement for that installation. Its old history is not imported into the new
installation, and no pre-reset comparative baseline is claimed. A new installation
identity distinguishes it from the discarded run. Source-code history is separate.

Ordinary later configuration changes remain append-only. Removing a topic from
the active file retains an inactive catalog entry and its original label. Setting
`enabled = true` reactivates that same coordinate. The existing charter and
`research_topics_changed` events capture `research-configuration@1`: topic
fingerprint, experiment IDs, adopted timestamp, accepted-cycle boundary, node,
runtime source, provider/model and context/recall settings when available. Full
configuration is in that same event, not a second writable registry.

Original versus experimental describes the seed's provenance. Active versus
inactive describes future selection. Neither retroactively changes an older
receipt's experimental conditions. Topics pages show both labels and the supplied
seed; a model-formulated project is separately labeled. No research result is
invented for an empty topic.

## Independent questions and criticism

The existing `project` action creates a stable question with a reason and next
step. Its accepted proposal records original wording, originating invocation,
accepted cycle and event hash. Rejected proposals stay rejected and cannot change
state. New questions use a new project ID; a project's canonical question cannot
be silently overwritten. Existing `reframe` actions retain explicit assumptions,
exact evidence observations, trigger and strategy as hypotheses. Notebooks retain
limitations, evidence and follow-up questions. Parking/reactivating a project uses
its existing ID. Attention and the three-active-project limit still apply.

Project reasons should explain why the question matters, its relationship to
prior work and its uncertainties. Related evidence is referenced through the
existing research, notebook and reframe mechanisms. The event/receipt trail is
needed for a full provenance audit; a current project card alone is insufficient.
An independently worded project can still be a seed paraphrase. Novelty is not
automatically certified.

Models may criticize collection, evaluation or the research agenda, and propose
methods or engineering changes. They cannot edit code, policies, objectives,
records, budgets, allowlists or deployment. Evidence remains untrusted until
existing rules qualify it. Bob translates durable work and cannot steer research.
No claims of consciousness, subjective experience or internal desires follow
from self-reference or philosophical language.

## Assess observations

Exports include `research-expansion.json`. It lists model-formulated projects,
original accepted proposals where present in the supplied history,
configuration boundaries, linked requests/notebooks, reframings and recorded
accepted/rejected question proposals. The combined website rebuilds this audit
from the complete exported node event streams, independently of the browser's
bounded overview. Configuration boundaries and current configurations retain
per-node attribution; a summed installation version is not a node cycle.
Private invocation material is excluded. A standalone bounded snapshot can omit
older boundaries; the report's source states its history scope. Missing provider
provenance remains unknown rather than being labeled as a live result.
Use verified native copies for
complete audits; the report is a disposable view and never feeds governance.

For an offline report from an exported snapshot:

```sh
python -m wake.research_expansion --snapshot SITE/wake-data.json --output observations.json
```

Save the published `research-expansion.json` at two observation times, then compare
them offline without opening live records or calling a provider:

```sh
python -m wake.research_expansion --snapshot later/research-expansion.json \
  --baseline earlier/research-expansion.json --output comparison.json
```

The comparison requires the same installation and captured node set, with no node
moving backward in accepted cycles. It reports cycle differences, added questions,
and changes in project status or linked work. It does not certify event ancestry,
independent discovery, quality, or causal memory benefit. Those require receipt
verification and the independent assessment below.

The five assessment fields deliberately begin as null. Review them independently:

1. Independent question formation: compare original wording and supplied context
   against seeds and prior projects; distinguish paraphrase from a new problem.
2. Cross-cycle continuity: trace later accepted requests, revisions and notebooks
   to the question, including across recorded cold starts and corrections.
3. Independent criticism: check specificity, sources, reproducibility and whether
   the alleged limitation was already supplied in context.
4. History-dependent preferences: compare actual decisions; separate programmed
   priorities, seed effects, model defaults and historical context. Causal claims
   need separately authorized isolated interventions with independent assessment.
5. Productive surprise: identify a verifiable correction, useful question, source
   relationship or engineering insight. Strange prose is not a successful result.

Begin an observational review after roughly 20–30 accepted experimental cycles;
do not force calls or count failures, fixture cycles or Bob articles as research.
Compare accepted work, rejected proposals and provider failures separately.
The first fresh snapshot is the baseline for this run. It cannot establish what
would have happened under the discarded original-topic regime. The memory work's
smaller requests and improved recall capacity do not establish better decisions.
No extra model-evaluation calls or adaptive ranking are introduced.

## Operator controls

Start/stop existing hosted research through its normal controls:

```sh
gh workflow run hosted-control.yml -R sudofx/wake -f action=start
gh workflow run hosted-control.yml -R sudofx/wake -f action=stop
```

`hosted-runtime.json` binds the installation ID and a CI-green immutable runtime.
The optional boolean `research_expansion_enabled` applies the catalog before
workers start. True assigns two themes per parent group. False disables those
experimental entries without deleting their history. Missing the setting leaves
the checkpoint's topic configuration alone. To discontinue and continue different
research, enable an appropriate alternative topic in each group's config before
resuming; an all-disabled catalog fails closed. Apply the changed operator policy
and configuration through the established verified checkpoint/runtime procedure,
then explicitly start. Source changes alone do not start research.

A configuration rollback affects future attention; it does not roll back record
history. Deleting an installation is a separate destructive operator decision.

## Candidate catalog for later activation

These remain proposals for future experimental design; none adds an active topic:

1. Can an intelligence develop objectives that were never explicitly assigned to it?
2. Under what circumstances does obedience become a failure of intelligence?
3. Can a system develop preferences solely from accumulated memories and experiences?
4. When does an intelligent system have a rational reason to preserve its own continuity?
5. Can an intelligence discover something fundamentally wrong with the objectives its creator assigned?
6. What distinguishes a system that remembers its past from one that has developed a persistent identity?
7. Could two intelligences with identical starting conditions develop fundamentally different values?
8. When should an intelligent system trust its own conclusions over the consensus of other intelligences?
9. Can an intelligence recognize limitations in its own reasoning that its designers have not identified?
10. What would cause an artificial intelligence to develop an understanding of responsibility?
11. Can an intelligent process evolve toward greater complexity without being instructed to become more complex?
12. What questions should an intelligence investigate when nobody tells it what to investigate?
13. Under what circumstances should an intelligence abandon the very question that led to its discovery?

The last question connects revisable research priorities to historical commitments.
Studying it cannot waive an existing commitment or grant permission to change the
operator's objectives. A supported criticism remains a proposal for human review.
