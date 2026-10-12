"""Offline numerical check of Poole et al. (2022), equations 6 and 7."""
import hashlib
import json
import math
import random
from collections import defaultdict

SOURCE = 'https://arxiv.org/html/2205.06313v1'
CLAIM = 'A conserved three-species reversible reaction simulation approximates the predicted equilibrium distribution; this does not demonstrate chemical heredity.'


def equilibrium(n):
    return {(a, b, n-a-b): math.factorial(n) / (math.factorial(a)*math.factorial(b)*math.factorial(n-a-b)) / 3**n
            for a in range(n+1) for b in range(n-a+1)}


def simulate(n, seed, duration, burn_in):
    rng = random.Random(seed)
    state = [n, 0, 0]
    time = 0.0
    residence = defaultdict(float)
    reactions = ((0, 1), (1, 0), (1, 2), (2, 1))
    jumps = 0
    while time < duration + burn_in:
        rates = [state[i] for i, _ in reactions]
        total = sum(rates)
        next_time = time + rng.expovariate(total)
        weight = max(0.0, min(next_time, duration + burn_in) - max(time, burn_in))
        residence[tuple(state)] += weight
        if next_time >= duration + burn_in:
            break
        draw = rng.random()*total
        for rate, (i, j) in zip(rates, reactions):
            draw -= rate
            if draw < 0:
                state[i] -= 1; state[j] += 1
                break
        jumps += 1
        time = next_time
    return {s: weight/duration for s, weight in residence.items()}, jumps


def reproduce(n=12, seeds=(11, 23, 37, 53, 71), duration=5000.0, burn_in=100.0):
    expected = equilibrium(n)
    rows = []
    for seed in seeds:
        empirical, jumps = simulate(n, seed, duration, burn_in)
        tv = 0.5 * sum(abs(empirical.get(s, 0)-p) for s, p in expected.items())
        mean_a = sum(s[0]*p for s, p in empirical.items())
        mean_b = sum(s[1]*p for s, p in empirical.items())
        covariance = sum(s[0]*s[1]*p for s, p in empirical.items()) - mean_a*mean_b
        rows.append({'seed': seed, 'jumps': jumps, 'total_variation_error': tv, 'covariance_a_b': covariance,
                     'conservation_violations': sum(p for s, p in empirical.items() if sum(s) != n)})
    marginal = [math.comb(n, k)*(1/3)**k*(2/3)**(n-k) for k in range(n+1)]
    # Independent variables preserve each exact marginal, but discard the joint constraint.
    baseline_on_support = {s: math.prod(marginal[k] for k in s) for s in expected}
    outside_mass = 1-sum(baseline_on_support.values())
    baseline_tv = 0.5*(sum(abs(expected[s]-baseline_on_support[s]) for s in expected)+outside_mass)
    return {'protocol': 'crn-equilibrium@1', 'source': SOURCE, 'source_equations': [6, 7],
            'status': 'measured', 'claim': CLAIM,
            'parameters': {'population': n, 'rates': [1, 1, 1, 1], 'initial_counts': [n, 0, 0],
                           'observation_seconds': duration, 'burn_in_seconds': burn_in, 'seeds': list(seeds)},
            'method': 'Exact Gillespie simulation; stationary distribution estimated by residence time, not jump frequency.',
            'runs': rows, 'expected_covariance_a_b': -n/9,
            'baseline': {'name': 'Independent binomial variables with the same exact one-species marginals',
                         'total_variation_error': baseline_tv, 'conservation_violation_probability': outside_mass,
                         'covariance_a_b': 0},
            'acceptance': {'predeclared_max_total_variation': 0.04,
                           'passed': all(r['total_variation_error'] < 0.04 and r['conservation_violations'] == 0 for r in rows)},
            'limitations': 'Numerical reproduction of a simple equilibrium result, not the paper\'s complex inference figures, wet chemistry, heredity, learning, or new research. Seeds are repeated trajectories, not independent biological experiments.'}


def result_id(report):
    encoded = json.dumps(report, sort_keys=True, separators=(',', ':')).encode()
    return 'reproduction-' + hashlib.sha256(encoded).hexdigest()[:24]


def record_result(state, payload, event, *, historical=False):
    from .governance import require
    report = payload.get('report')
    require(payload.get('actor') == 'operator', 'Measured reproductions are operator-owned')
    require(isinstance(report, dict) and report.get('protocol') == 'crn-equilibrium@1', 'Unknown reproduction protocol')
    require(report.get('source') == SOURCE and report.get('claim') == CLAIM and report.get('status') == 'measured', 'Reproduction scope mismatch')
    # Validation uses the deterministic offline protocol rather than trusting provider text.
    params = report.get('parameters', {})
    require(params == {'population': 12, 'rates': [1,1,1,1], 'initial_counts': [12,0,0], 'observation_seconds': 5000.0, 'burn_in_seconds': 100.0, 'seeds': [11,23,37,53,71]}, 'Only the reviewed reproduction parameters are supported')
    if not historical:
        require(report == reproduce(), 'Measured receipt does not match the reproducible protocol')
    identifier = result_id(report)
    require(identifier not in state.get('reproductions', {}), 'Reproduction is already recorded')
    state.setdefault('reproductions', {})[identifier] = {**report, 'id': identifier, 'time': event['time'], 'event_seq': event['seq']}
