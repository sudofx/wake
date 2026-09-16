# Noise Resilience and Mitigation in Adaptive VQE

Analysis of how hardware noise affects the operator selection step in ADAPT-VQE and the effectiveness of multi-layered error mitigation and AIM techniques.

## Findings

In adaptive variational quantum algorithms such as ADAPT-VQE, the operator selection step exhibits a natural resilience to low levels of noise. However, recent systematic case studies indicate that both coherent and incoherent noise channels prevent algorithmic convergence when noise rates are high, as demonstrated on a linear H3 molecule test case [source-eff925a57e3a479c]. Combining multiple error mitigation techniques—specifically dynamical decoupling, zero-noise extrapolation, and Pauli twirling—restores successful convergence profiles [source-eff925a57e3a479c]. Additionally, the standard implementation of ADAPT-VQE faces severe measurement overheads from estimating numerous commutator operators. This overhead can be mitigated without extra measurement costs by using Adaptive Informationally complete generalized Measurements (AIM) to reuse energy measurement data for commutator estimation [source-e735b67670f14093].

## Limitations and competing views

The noise resilience findings are based primarily on preprints and case studies of small molecular systems (e.g., linear H3 [source-eff925a57e3a479c] and H4 [source-e735b67670f14093]). Whether these combined mitigation strategies scale effectively to larger, chemically complex processors remains unverified under actual hardware constraints.

## Next questions

How do these error mitigation configurations scale to 20+ qubit systems under high coherent noise? Is there a formal bound on the accuracy of commutator estimation when using AIM under realistic hardware noise?

## Collected sources

- [source-eff925a57e3a479c](https://export.arxiv.org/api/query?id_list=2609.17501v1)
- [source-e735b67670f14093](https://export.arxiv.org/api/query?search_query=cat%3Aquant-ph+AND+all%3AADAPT-VQE+error+mitigation&start=0&max_results=4)

Revision 1 · AI-authored research synthesis; see source scopes in the journal.
