"""Operator-controlled correction in the live research record, without API calls.

A deliberately false source-count claim is labeled as a demonstration throughout.
The original and correction use normal governance; no historical bypass or reset.
"""
import json
from .application_policy import govern_proposal
from .governance import require, _source_identity

PREFIX = 'controlled-correction-demo-v1'


def run_correction_demo(engine):
    with engine.store.lock():
        state = engine.store.load()
        require(state['pending'] is None, 'Finish the pending invocation before the correction demonstration')
        corrected_id = PREFIX + '-corrected'
        if corrected_id in state['posts']:
            return _receipt_summary(engine, state, already_complete=True)
        prior_post = state['posts'].get(PREFIX + '-original')
        require((PREFIX in state['beliefs']) == bool(prior_post),
                'Inconsistent correction demonstration; inspect receipts before continuing')
        attention = engine.context(state, 'operator-inspection').get('attention', {})
        require(not attention.get('enforce_selected_topic'),
                'Correction demonstration waits for an unenforced Attention window; policy is never bypassed')
        candidates = ([state['notebooks'][prior_post['notebooks'][0]]] if prior_post else
                      sorted(state.get('notebooks', {}).values(), key=lambda item: item['id']))
        selected = None
        for notebook in candidates:
            evidence = notebook.get('evidence', [])
            if len({_source_identity(state['evidence'][key]) for key in evidence}) >= 2:
                selected = notebook
                break
        require(selected is not None, 'Correction demonstration needs a governed notebook citing two source works')
        evidence = list(selected['evidence'])
        count = len({_source_identity(state['evidence'][key]) for key in evidence})
        false_claim = 'Controlled demonstration: this notebook cites exactly one underlying source work.'
        shared = (f"This is an operator-controlled audit demonstration using notebook {selected['id']}. "
                  'The intentionally mistaken count is a test claim, not a scientific finding. '
                  'The underlying research remains provisional and must be checked against its collected sources. '
                  + selected['findings'][:2500])
        original = dict(type='blog', id=PREFIX + '-original', project=selected['project'],
                        title='Controlled correction demonstration: seeded counting error',
                        lede='A deliberately seeded source-count error to test additive correction.',
                        body=false_claim + '\n\n' + shared + '\n\nSummary\n\nThis labeled demonstration will correct a deliberately mistaken count while preserving the first version.',
                        notebooks=[selected['id']], evidence=evidence,
                        reason='Operator-authorized controlled demonstration, not new research.')
        belief = dict(type='belief', id=PREFIX, statement=false_claim, confidence=0.2,
                      status='active', evidence=evidence,
                      reason='Deliberately false test claim; verify by counting the notebook source identities.',
                      falsifier='More than one distinct source identity in the cited notebook falsifies this claim.')
        # Prove the proposal can pass before appending any demonstration material.
        if prior_post is None:
            _, _, editorial, _ = govern_proposal(state, 'operator-preflight', dict(base_version=state['version'],
                             title='Controlled correction demonstration', summary='Seed a labeled source-count error.',
                             actions=[belief, original]))
            require(editorial is None, 'Demonstration publication would be withheld: ' + str(editorial))
            _submit(engine, [belief, original], 'Seed the labeled false source-count claim')
        measurement_id = PREFIX + '-measurement'
        if measurement_id not in engine.store.load()['evidence']:
            engine.observe(json.dumps({'kind': 'controlled-correction-measurement',
                       'notebook': selected['id'], 'evidence_ids': evidence,
                       'distinct_source_identities': sorted({_source_identity(state['evidence'][key]) for key in evidence}),
                       'observed_count': count, 'method': 'Count distinct collector source_identity values, falling back to URL.'}),
                       'operator:controlled-correction-measurement', evidence_id=measurement_id)
        retracted = {**belief, 'status': 'retracted', 'confidence': 0,
                     'evidence': [measurement_id], 'reason': f'Observed {count} distinct source works; the seeded claim is false.'}
        correction = {**original, 'id': corrected_id, 'supersedes': original['id'],
                      'title': 'Controlled correction demonstration: corrected source count',
                      'body': f'Retracted wording: "{false_claim}". This was an overstatement. '
                              f'The measured count is {count} distinct source works.\n\n' + shared
                              + '\n\nSummary\n\nThe original counting error remains in the record. New measurement retracts the belief and this post supersedes the earlier demonstration.',
                      'reason': f'New measurement {measurement_id} corrects the source count; preserve the original publication.'}
        actions = [correction] if engine.store.load()['beliefs'][PREFIX]['status'] == 'retracted' else [retracted, correction]
        _submit(engine, actions, 'Retract the false count and supersede its publication')
        state = engine.store.load()
        require(state['posts'][original['id']].get('superseded_by') == corrected_id,
                'Correction publication was withheld; inspect the recorded editorial receipt')
        return _receipt_summary(engine, state)


def _submit(engine, actions, summary):
    invocation, request = engine.start('manual', 'operator-controlled-demonstration', charged=False)
    result = engine.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
                           title='Controlled correction demonstration', summary=summary, actions=actions)))
    require(result['status'] == 'accepted', 'Correction demonstration rejected: ' + str(result))


def _receipt_summary(engine, state, already_complete=False):
    events = engine.store.events()
    receipts = [event for event in events if event['kind'] == 'accepted' and any(
        action.get('id', '').startswith(PREFIX) for action in event['payload'].get('proposal', {}).get('actions', []))]
    invocations = {event['payload']['id'] for event in receipts}
    kernel_receipts = []
    if hasattr(engine.store, 'record'):
        for receipt in engine.store.record.history():
            for operation in receipt['proposal'].get('operations', []):
                value = operation.get('value', {})
                item = value.get('input') if isinstance(value, dict) else None
                if (receipt['status'] == 'accepted' and isinstance(item, dict)
                        and item.get('kind') == 'accepted'
                        and item.get('payload', {}).get('id') in invocations):
                    kernel_receipts.append({key: receipt[key] for key in ('receipt_id', 'sequence', 'event_hash')})
    return {'demonstration': PREFIX, 'already_complete': already_complete, 'provider_calls': 0,
            'belief_status': state['beliefs'][PREFIX]['status'],
            'original_post': PREFIX + '-original', 'superseded_by': PREFIX + '-corrected',
            'receipts': [{'seq': event['seq'], 'hash': event['hash'], 'invocation': event['payload']['id']} for event in receipts],
            'kernel_receipts': kernel_receipts,
            'head': engine.store.head(), 'boundary': 'Operator-controlled live transition; does not prove autonomous model correction.'}
