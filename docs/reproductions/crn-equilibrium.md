# Reproducing a conserved reaction network

The offline simulation matched the equilibrium prediction: five seeded trajectories had total-variation errors of 0.0153–0.0179, below the predeclared 0.04 threshold. No trajectory violated molecule conservation. This is a numerical reproduction of a simple theoretical result, not a demonstration of chemical memory or heredity.

The primary source is [Poole, Ouldridge, Gopalkrishnan and Winfree (2022)](https://arxiv.org/html/2205.06313v1), equations 6 and 7. The reproduced network is S1 ⇌ S2 ⇌ S3, with 12 total molecules, equal species energies and unit rate constants. Its reachable equilibrium distribution is multinomial with probabilities (1/3, 1/3, 1/3). The expected covariance between S1 and S2 is −12/9.

The implementation uses Gillespie's exact stochastic reaction method. It starts at (12, 0, 0), discards 100 time units, and observes 5,000 further units for each of seeds 11, 23, 37, 53 and 71. Residence times estimate probabilities; counting jumps would bias the distribution. All parameters and measurements are in [the result JSON](crn-equilibrium.json).

The comparison baseline has three independent binomial variables with exactly the same individual marginals. It ignores the shared molecule total, so it misses the joint distribution and has zero pairwise covariance. This is an explicit comparison of models with and without conservation, not a competing chemical implementation or evidence that WAKE discovered a better algorithm.

Run it without a model or network request:

```sh
python -m scripts.reproduce_crn --output /tmp/crn-equilibrium.json
```

Add `--data /data` only to append a measured operator receipt to a paused, drained installation. That receipt does not increment accepted research cycles. The reviewed protocol and exact claim are fixed; a provider cannot manufacture a tested result. Historical receipts preserve their measurements without rerunning a future simulator during replay.

This check does not reproduce the paper's complex inference figures, thermodynamic inference costs, wet experiments, learning, or heredity. The five seeds are repeated numerical trajectories, not independent biological experiments.
