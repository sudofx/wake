"""Read a pinned public farm observation for editorial context only.

No model instructions, credentials, file writes, colony controls or native evidence
are exposed here. The deterministic caretaker remains a separate writer.
"""
from datetime import datetime
import hashlib
import json
import os
import re
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

SCHEMA = 'bob-farm-observation@1'
MAX_BYTES = 2_097_152


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise ValueError('Farm observation redirects are not allowed')


def read_json(url, limit):
    opener = build_opener(ProxyHandler({}), NoRedirect())
    with opener.open(Request(url, headers={'Accept': 'application/json', 'User-Agent': 'WAKE-Bob-observer/1'}), timeout=5) as response:
        raw = response.read(limit + 1)
    if len(raw) > limit:
        raise ValueError('Farm observation exceeds its reading limit')
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def _count(value):
    if type(value) is not int or not 0 <= value <= 10**12:
        raise ValueError('Invalid farm observation count')
    return value


def _metrics(state, recorded):
    if not isinstance(state, dict) or not isinstance(recorded, dict):
        raise ValueError('Invalid farm metrics')
    if not isinstance(state.get('ants'), list) or len(state['ants']) > 128 or not isinstance(state.get('brood'), list) or len(state['brood']) > 128:
        raise ValueError('Invalid farm population')
    queen_state = state.get('queen')
    if not isinstance(queen_state, dict):
        raise ValueError('Invalid farm queen observation')
    queen = queen_state.get('alive')
    if type(queen) is not bool:
        raise ValueError('Invalid farm queen observation')
    result = {'ants': len(state['ants']), 'dug': _count(state['dug']),
              'delivered': _count(state['delivered']), 'food_reserve': _count(state['foodReserve']),
              'protein_reserve': _count(state['proteinReserve']), 'queen_alive': queen}
    if any(recorded.get(key) != value for key, value in result.items()):
        raise ValueError('Farm metrics disagree with the checkpoint')
    result['brood'] = len(state['brood'])
    return result


def farm_observation(repository=None, *, reader=read_json):
    """Two bounded public GETs; unavailable observations never become invented facts."""
    repository = repository or os.environ.get('GITHUB_REPOSITORY')
    if not repository:
        return {'schema': SCHEMA, 'status': 'unavailable', 'reason': 'No farm repository is bound'}
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Invalid farm repository')
    try:
        ref, _ = reader('https://api.github.com/repos/' + repository + '/git/ref/heads/bob-ant-farm', 32768)
        revision = ref['object']['sha']
        if not re.fullmatch(r'[a-f0-9]{40}', revision):
            raise ValueError('Invalid farm revision')
        url = 'https://raw.githubusercontent.com/' + repository + '/' + revision + '/farm.json'
        packet, fingerprint = reader(url, MAX_BYTES)
        if not isinstance(packet, dict):
            raise ValueError('Invalid farm packet')
        if (packet.get('schema') != 'wake-bob-ant-farm@1' or packet.get('colony_id') != 'bobs-ant-farm'
                or packet.get('model') != 'pellet-tunnels@9'
                or not re.fullmatch(r'[a-f0-9]{40}', packet.get('source_revision', ''))):
            raise ValueError('Unsupported farm identity')
        captured = packet['updated_at']
        if not isinstance(captured, str) or len(captured)>60 or datetime.fromisoformat(captured.replace('Z', '+00:00')).tzinfo is None:
            raise ValueError('Farm observation needs an explicit time zone')
        start, end, observation = packet['replay']['start'], packet['checkpoint'], packet['observation']
        if not isinstance(start, dict) or not isinstance(end, dict) or not isinstance(observation, dict):
            raise ValueError('Invalid farm replay')
        if (start.get('schema') != 'wake-ant-colony@4' or end.get('schema') != 'wake-ant-colony@4'
                or observation.get('scope') != 'simulation-only'
                or start['ticks'] != observation['from_tick'] or end['ticks'] != observation['to_tick']
                or not 0 <= _count(end['ticks']) - _count(start['ticks']) <= 6000
                or end['ticks'] - start['ticks'] != packet['replay']['ticks']):
            raise ValueError('Farm interval disagrees with the replay')
        before, after = _metrics(start, observation['before']), _metrics(end, observation['after'])
        care = packet['replay']['care']
        feedings, units = _count(observation['feedings']), _count(observation['food_added'])
        if (not isinstance(care, list) or len(care) > 120 or feedings != len(care) or units != 100 * feedings
                or _count(end['addedFood']) - _count(start['addedFood']) != units
                or any(not isinstance(row, dict) or row.get('action') != 'feed' or row.get('units') != 100
                       or not start['ticks'] <= _count(row.get('tick')) < end['ticks'] for row in care)):
            raise ValueError('Farm feeding record disagrees with the interval')
        history = []
        notes = packet.get('notes', [])
        if not isinstance(notes, list) or len(notes) > 48:
            raise ValueError('Farm history exceeds its reading bound')
        for note in notes[-4:]:
            row = {key: _count(note[key]) for key in
                   ('from_tick', 'to_tick', 'workers', 'deliveries', 'new_tunnels', 'feedings')}
            if not row['from_tick'] <= row['to_tick'] <= end['ticks']:
                raise ValueError('Invalid farm history interval')
            history.append(row)
        return {'schema': SCHEMA, 'status': 'available', 'scope': 'programmed-simulation-only',
                'source': url, 'revision': revision, 'sha256': fingerprint, 'captured_at': captured,
                'model': packet['model'], 'model_source_revision': packet['source_revision'],
                'interval': {'from_tick': start['ticks'], 'to_tick': end['ticks']},
                'before': before, 'after': after, 'feedings': feedings, 'food_added': units,
                'recent_intervals': history}
    except (OSError, ValueError, KeyError, TypeError) as error:
        return {'schema': SCHEMA, 'status': 'unavailable', 'reason': type(error).__name__}
