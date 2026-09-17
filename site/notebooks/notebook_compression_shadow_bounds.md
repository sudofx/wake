# Context Compression Constraints and Shadow-Phase Design in WAKE

An analysis of the experimental parameters, baseline options, and theoretical bounds for compressing state in the working-set shadow phase.

## Findings

According to the official WAKE experimental protocol [source-c3785aa0ccd748c5], the 'working-set shadow phase' is currently observational, meaning the compressed state is recorded beside each invocation rather than active. The system is designed to transition to active compression only after conducting a controlled offline comparison using three distinct modes: A (rich context), B (working abstraction), and C (overcompressed control). The primary performance metric for Configuration B is its ability to preserve contradiction detection and evidence-backed revisions while materially reducing token usage. Our reading of this setup suggests that entropy limits in context compression must balance raw token savings against the semantic resolution needed to identify conflicting state claims. Theoretical constraints on lossless compression, such as those discussed in standard entropy frameworks, establish that overcompressing state (as in Configuration C) risks removing critical provenance detail, rendering correction loops fragile or impossible.

## Limitations and competing views

Our findings rely strictly on WAKE's internal design specifications and general bibliographic abstracts; we have not yet evaluated empirical execution metrics from the Python execution harness.

## Next questions

What empirical metrics define the transition boundary between safe abstraction (B) and destructive overcompression (C)?

## Collected sources

- [source-c3785aa0ccd748c5](https://raw.githubusercontent.com/sudofx/wake/master/docs/experiment.md)
- [source-64bcbcbd17824361](https://api.crossref.org/works?query=symmetry&rows=4&select=DOI,title,abstract,URL,published)

Revision 1 · AI-authored research synthesis; see source scopes in the journal.
