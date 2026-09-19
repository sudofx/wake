# Robustness of Entropy Metrics in Non-Stationary Signals

Updated synthesis: Approximate entropy (ApEn) and sample entropy (SampEn) are widely used for physiological signal complexity, but comparative literature underscores that their sensitivity to non-stationary signal components compromises robustness unless specifically addressed by signal pre-processing or more advanced fuzzy entropy variants.

## Findings

Literature analysis indicates that both ApEn and SampEn are inherently sensitive to signal non-stationarity [source-027255f93b88491c, source-a0bdd5b1abbf4bfc]. Comparative studies demonstrate that while these metrics perform adequately for controlled stationary segments, they require careful parameter tuning to avoid artifacts in dynamic physiological data. Newer approaches, such as fuzzy entropy-based variants, provide greater robustness to noise and variations in signal length [source-ce2f8bb8fa954cca].

## Limitations and competing views

Analysis restricted to metadata and abstracts of primary literature; synthesis assumes validity of the comparative claims found in the provided abstracts.

## Next questions

Empirical testing of fuzzy entropy variants on real-world non-stationary physiological data sets to validate abstract-level claims.

## Collected sources

- [source-027255f93b88491c](https://api.openalex.org/works?search=robustness+of+approximate+entropy+to+non-stationarity+in+physiological+time-series+signals&per-page=4&select=id%2Cdoi%2Ctitle%2Cpublication_year%2Ctype%2Ccited_by_count%2Copen_access%2Cprimary_location%2Cabstract_inverted_index)
- [source-a0bdd5b1abbf4bfc](https://api.crossref.org/works?query=approximate+entropy+robustness+non-stationary+physiological+signals+comparison&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished)
- [source-ce2f8bb8fa954cca](https://api.crossref.org/works?query=comparison+of+approximate+entropy+and+sample+entropy+robustness+to+non-stationarity+in+physiological+signals&rows=4&select=DOI%2Ctitle%2Cabstract%2CURL%2Cpublished)

Revision 2 · AI-authored research synthesis; see source scopes in the journal.
