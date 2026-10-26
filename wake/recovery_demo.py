"""Governed operational adjustment on synthetic services in NEW fixture records.

No production controller imports this module. Its two settings affect only the
simulated caller below; observations come from the separate fixture service.
"""
from copy import deepcopy
import html
import json
import math
from pathlib import Path
import uuid

from .kernel import (ApplicationAction, ApplicationDecision, ApplicationDefinition,
                     ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel)
from .kernel.governance import Governance
from .kernel.models import SubmissionProvenance
from .kernel.record import Record

BASELINE = {'retry_delay_seconds': 1, 'max_concurrent_requests': 2}
RESPONSES = {'rate_limited': ('retry_delay_seconds', 4),
             'timeout': ('max_concurrent_requests', 1)}
LEASE_SECONDS = 30
COOLDOWN_SECONDS = 60


def require(value, reason):
    if not value:
        raise ValueError(reason)


def revert(state, at, reason):
    state['changes'].append({'at': at, 'status': 'reverted', 'reason': reason,
                             'before': deepcopy(state['settings']), 'after': dict(BASELINE)})
    state['settings'] = dict(BASELINE)
    state['trial'] = None
    state['failures'] = 0
    state['cooldown_until'] = at + COOLDOWN_SECONDS


def initialize(state, payload):
    if state is not None or payload != {'fixture': True}:
        return ApplicationDecision(False, reasons=('A new explicit fixture is required',))
    return ApplicationDecision(True, {'settings': dict(BASELINE), 'trial': None,
                                     'failures': 0, 'signal': None, 'observed_at': 0,
                                     'enabled': True, 'cooldown_until': 0, 'changes': []})


def observe(state, payload):
    try:
        require(state is not None and set(payload) == {'at', 'signal', 'enabled'}, 'Invalid observation fields')
        at, signal = payload['at'], payload['signal']
        require(type(at) in (int, float) and math.isfinite(at) and at >= state['observed_at'], 'Observation clock moved backward')
        require(signal in ('completed', 'rate_limited', 'timeout', 'guardrail_failure', 'no_observation'), 'Unknown observation')
        require(type(payload['enabled']) is bool, 'Operator intent must be explicit')
        result = deepcopy(state)
        result.update(observed_at=at, enabled=payload['enabled'])
        trial = result['trial']
        if trial and (not result['enabled'] or signal == 'guardrail_failure' or at >= trial['expires_at']):
            revert(result, at, 'operator_pause' if not result['enabled'] else 'lease_expired' if at >= trial['expires_at'] else signal)
        elif trial:
            if signal == 'completed':
                trial['successes'] += 1
                trial['failures'] = 0
                if trial['successes'] == 2:
                    trial['verified'] = True
                    result['changes'].append({'at': at, 'status': 'verified', 'reason': 'two_completed_fixture_requests'})
            elif signal != 'no_observation':
                trial['successes'] = 0
                trial['failures'] += 1
                if trial['failures'] >= 2:
                    revert(result, at, 'adjustment_did_not_recover_service')
        result['failures'] = result['failures'] + 1 if signal in RESPONSES and result['signal'] == signal else 1 if signal in RESPONSES else 0
        result['signal'] = signal
        return ApplicationDecision(True, result)
    except (ValueError, TypeError, KeyError) as error:
        return ApplicationDecision(False, reasons=(str(error),))


def adjust(state, payload):
    try:
        require(state is not None and set(payload) == {'setting', 'value'}, 'Invalid adjustment fields')
        require(state['enabled'] and state['trial'] is None and state['observed_at'] >= state['cooldown_until'], 'Adjustment is paused, active or cooling down')
        require(state['failures'] >= 2 and state['signal'] in RESPONSES, 'Two matching failure observations required')
        setting, value = RESPONSES[state['signal']]
        require(payload['setting'] == setting and type(payload['value']) is int and payload['value'] == value,
                'Only the installed bounded response is permitted')
        result = deepcopy(state)
        before = deepcopy(result['settings'])
        result['settings'][setting] = value
        result['trial'] = {'setting': setting, 'expires_at': state['observed_at'] + LEASE_SECONDS,
                           'successes': 0, 'failures': 0, 'verified': False}
        result['changes'].append({'at': state['observed_at'], 'status': 'applied',
                                  'reason': state['signal'], 'before': before,
                                  'after': deepcopy(result['settings']),
                                  'expires_at': result['trial']['expires_at']})
        return ApplicationDecision(True, result)
    except (ValueError, TypeError, KeyError) as error:
        return ApplicationDecision(False, reasons=(str(error),))


RECOVERY = ApplicationDefinition('wake-operational-recovery-fixture', '1', (
    ApplicationAction('initialize', initialize), ApplicationAction('observe', observe),
    ApplicationAction('adjust', adjust)), state_storage='event_log')


def fixture_host(path):
    require(not Path(path).exists(), 'Recovery fixture record must be new')
    registry = ApplicationRegistry((RECOVERY,))
    return ApplicationHost(Kernel(Record(path), Governance(application_registry=registry),
                                  receipt_location='local:operational-recovery-fixture'),
                           registry, RECOVERY.application_id)


def submit(host, action, payload):
    return host.submit(ApplicationIntent(uuid.uuid4().hex, host.context().revision, action, payload),
                       provenance=SubmissionProvenance('runtime', 'recovery-fixture',
                                                        source='wake improve recovery-demo', purpose=action))


def observe_fixture(host, at, signal, *, enabled=True):
    receipt = submit(host, 'observe', {'at': at, 'signal': signal, 'enabled': enabled})
    require(receipt.status == 'accepted', str(receipt.reasons))
    state = host.context().state
    if (state['enabled'] and state['trial'] is None and state['failures'] >= 2
            and state['signal'] in RESPONSES and at >= state['cooldown_until']):
        setting, value = RESPONSES[state['signal']]
        require(submit(host, 'adjust', {'setting': setting, 'value': value}).status == 'accepted', 'Fixture adjustment rejected')


class ServiceFixture:
    """Independent response rule: the adjustment cannot change this deadline."""
    def response(self, at):
        return 'rate_limited' if at < 3 else 'completed'


def demonstrate(output):
    root = Path(output).resolve()
    root.mkdir(parents=True, exist_ok=False)
    scenarios = {}
    service = ServiceFixture()
    baseline = [service.response(at) for at in range(5)]
    host = fixture_host(root / 'recovery.sqlite')
    require(submit(host, 'initialize', {'fixture': True}).status == 'accepted', 'Fixture initialization failed')
    observations = []
    at = 0
    for _ in range(4):
        signal = service.response(at)
        observations.append({'at': at, 'signal': signal})
        observe_fixture(host, at, signal)
        at += host.context().state['settings']['retry_delay_seconds']
    require(host.context().state['trial']['verified'], 'Recovery was not independently observed')
    observe_fixture(host, 32, 'no_observation')
    require(host.audit_context() == host.context(), 'Recovery record replay mismatch')
    scenarios['temporary_rate_limit'] = {'observations': observations, 'state': host.context().state,
                                        'baseline_rate_limited_requests': baseline.count('rate_limited'),
                                        'adjusted_rate_limited_requests': sum(x['signal'] == 'rate_limited' for x in observations),
                                        'replay_verified': True}
    for name, signal in [('persistent_failure', 'rate_limited'), ('operator_pause', 'timeout'),
                         ('guardrail_failure', 'timeout'), ('missing_observation', 'timeout')]:
        h = fixture_host(root / (name + '.sqlite'))
        submit(h, 'initialize', {'fixture': True})
        observe_fixture(h, 0, signal)
        observe_fixture(h, 1, signal)
        if name == 'persistent_failure':
            observe_fixture(h, 5, signal)
            observe_fixture(h, 9, signal)
        elif name == 'operator_pause':
            observe_fixture(h, 2, 'no_observation', enabled=False)
        elif name == 'guardrail_failure':
            observe_fixture(h, 2, 'guardrail_failure')
        else:
            observe_fixture(h, 32, 'no_observation')
        state = h.context().state
        require(state['settings'] == BASELINE and state['trial'] is None, 'Fixture did not revert')
        require(h.audit_context() == h.context(), 'Failure fixture replay mismatch')
        scenarios[name] = {'state': state, 'replay_verified': True}
    # Rejected proposals remain receipted and cannot add settings or widen limits.
    refused = submit(host, 'adjust', {'setting': 'governance_enabled', 'value': 0})
    require(refused.status == 'rejected' and host.audit_context() == host.context(), 'Forbidden setting was not rejected')
    result = {'schema': 'wake-operational-recovery-demo@1', 'fixture': True, 'model_calls': 0,
              'production_changes': 0, 'research_records_opened': 0, 'replay_verified': True,
              'baseline': BASELINE, 'lease_seconds': LEASE_SECONDS, 'cooldown_seconds': COOLDOWN_SECONDS,
              'forbidden_proposal_status': refused.status, 'scenarios': scenarios}
    (root / 'result.json').write_text(json.dumps(result, indent=2))
    rows = ''.join('<tr><td>' + html.escape(name.replace('_', ' ')) + '</td><td>' +
                   html.escape(', '.join(c['status'] for c in item['state']['changes'])) +
                   '</td><td>Verified</td></tr>' for name, item in scenarios.items())
    (root / 'recovery.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>WAKE bounded recovery</title>
<style>body{font:16px/1.6 system-ui;max-width:900px;margin:auto;padding:28px;background:#f5f4ef;color:#24372f}h1{line-height:1.15}table{border-collapse:collapse;width:100%;background:white}td,th{text-align:left;padding:12px;border-bottom:1px solid #ddd}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px}</style>
<h1>A small, reversible place to correct itself</h1><p>WAKE detected two synthetic rate-limit failures,
raised its retry delay from 1 to 4 seconds, then observed two completed fixture requests.
The independent service owns availability; the adjustment cannot change its responses.</p>
<p>The fixed baseline received three rate-limit failures; the adjusted caller received two and recovered later.
This is a tradeoff between request pressure and latency, not proof of faster recovery or production reliability.</p>
<p>Only retry delay and reduced concurrency are allowed. One change at a time, a 30-second lease,
automatic reversion, a 60-second cooldown, and operator pause. Governance, records, models,
prompts, credentials and spending ceilings are outside the allowlist.</p>
<table><tr><th>Disturbance</th><th>Recorded changes</th><th>Record replay</th></tr>''' + rows + '''</table>
<p>Zero model calls, production changes or research-record access. Each scenario uses a new native fixture record.
Missing observations cause lease expiry at the next control tick; this does not prove recovery if the controller itself stops.</p>
<details><summary>Exact fixture results</summary><pre>''' + html.escape(json.dumps(result, indent=2)) + '</pre></details></html>')
    return {**result, 'report': str(root / 'recovery.html')}
