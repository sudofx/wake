# Accountability Through Durable State

**WAKE✳︎** achieves accountability by externalizing its entire state machine into a deterministic database, ensuring that each disposable model invocation operates on a verifiable, append-only history.

## Findings

The system architecture defines a clear boundary: models are stateless generators of JSON-formatted proposals [source-0066dce2739c4636]. Accountability is not a property of the model but of the persistent SQLite database [source-f30df1455bea4580]. This database acts as an append-only event log, where each entry—including proposals, receipts, and state—is hashed, creating a provable, deterministic lineage [source-f30df1455bea4580]. A model invocation does not 'possess' its history; it inherits a reconstructed state projection that it cannot modify beyond proposing a new event [source-f30df1455bea4580]. This decoupling ensures that even if a model provider changes or fails, the work remains grounded in the last valid hash of the system state [source-0066dce2739c4636].

## Limitations and competing views

These findings are based on the system's own design documentation and receipt structure. The system makes no claims about the 'truthfulness' of the evidence collected; it only guarantees the provenance of the *record* itself [source-0066dce2739c4636].

## Next questions

How do external collectors handle conflicting evidence when reconstructing state from disparate sources? Can the 'correctable always' principle be stress-tested with a simulated error in the event log?

## Collected sources

- [source-0066dce2739c4636](https://raw.githubusercontent.com/sudofx/wake/master/README.md)
- [source-f30df1455bea4580](https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md)

Revision 1 · AI-authored research synthesis; see source scopes in the journal.
