"""A reproducible artificial instrument. Its mechanism is never model context.

This is synthetic scientific instrumentation, not a claim about nature. Public
seeds make independent replication possible; the proposing provider receives
observations and the instrument interface, never this implementation or labels.
"""
import random
from ..event_format import digest
from ..governance import require
from . import contracts as c


def response(instance, x):
    rng = random.Random(instance)
    slope, intercept, bend = rng.randint(1, 4), rng.randint(-3, 3), rng.randint(1, 3)
    return slope*x + intercept + bend*max(0, x-2)**2


def observations(instance):
    return [{'x': x, 'y': response(instance, x)} for x in (-2, 0, 2)]


def prepare(protocol):
    c.fields(protocol['inputs'], ('instance', 'probes', 'holdout_size'))
    instance = protocol['inputs']['instance']
    require(type(instance) is int and 0 <= instance < 2**32, 'A bounded artificial-system instance is required')
    probes = protocol['inputs']['probes']
    require(isinstance(probes, list) and 1 <= len(probes) <= 12 and len(set(probes)) == len(probes)
            and all(type(x) is int and -50 <= x <= 50 for x in probes), 'Choose 1–12 distinct bounded probe inputs')
    count = protocol['inputs']['holdout_size']
    require(type(count) is int and 4 <= count <= 24, 'Use 4–24 unseen test inputs per seed')
    pool = [x for x in range(-50, 51) if x not in probes and x not in (-2, 0, 2)]
    holdout = []
    for seed in protocol['seeds']:
        for x in random.Random(seed).sample(pool, count):
            holdout.append({'id': f'{seed}:{x}', 'x': x})
    inputs = {'observations': observations(instance), 'probes': probes, 'holdout': holdout}
    labels = {'probes': [response(instance, x) for x in probes],
              'holdout': [response(instance, row['x']) for row in holdout]}
    return inputs, {'oracle_digest': digest(labels), 'instrument_version': 'artificial-response@1'}


def measure(item):
    protocol = item['protocol']
    output = item['attempts'][-1]['receipt']['outputs']
    c.fields(output, ('probe_predictions', 'holdout_predictions'))
    inputs, _ = prepare(protocol)
    instance = protocol['inputs']['instance']
    expected = {'probe_predictions': [response(instance, x) for x in inputs['probes']],
                'holdout_predictions': [response(instance, row['x']) for row in inputs['holdout']]}
    correct = {}
    for key in expected:
        require(isinstance(output[key], list) and len(output[key]) == len(expected[key]) and
                all(type(value) in (int, float) for value in output[key]), 'Malformed artificial-system predictions')
        correct[key] = [a == b for a, b in zip(output[key], expected[key])]
    probe, holdout = correct['probe_predictions'], correct['holdout_predictions']
    return {'probe_accuracy': sum(probe)/len(probe), 'holdout_accuracy': sum(holdout)/len(holdout),
            'accuracy': sum(holdout)/len(holdout), 'errors': len(holdout)-sum(holdout)}, 'validated', {
        'method': 'Independent artificial-system oracle; prediction code receives no test labels',
        'scope': 'Synthetic generalization on fresh inputs; not natural-science evidence',
        'observations': [{'x': x, 'prediction': y, 'observed': actual} for x, y, actual in
                         zip(inputs['probes'], output['probe_predictions'], expected['probe_predictions'])],
        'holdout_labels_disclosed': False, 'holdout_consumed': True,
        'holdout_identity': digest(inputs['holdout'])}
