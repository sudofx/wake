"""Public activity is a fresh allowlisted observation, never private context."""
from datetime import datetime, timezone, timedelta
import json
import unittest
from wake.hosted_activity import public_sample, NODES


class HostedActivityTests(unittest.TestCase):
    def test_private_data_stale_workers_and_unconfirmed_calls_are_excluded(self):
        stamp = datetime.now(timezone.utc).isoformat()
        runtime = {'mode':'standalone','state':'running','runtime_id':'runtime-1','observed_at':stamp,
            'activity_schema':1,'capabilities':{'live_activity':True},
            'activity':{'stage':'provider','active':True,'invocation_id':'w-'+'a'*16,'coordinate_id':'axis:1','prompt':'PRIVATE'},'reason':'PRIVATE'}
        packet = {'members':[{'id':node,'runtime':runtime} for node in NODES],
            'coordinator':{'active':{'confirmed':False,'member':NODES[0],'token':'PRIVATE'},'queued':100},'passenger':'PRIVATE'}
        result = public_sample(packet,'installation','123','a'*40)
        self.assertNotIn('PRIVATE',json.dumps(result));self.assertEqual(result['coordinator'],{'active':None,'queued':12})
        self.assertEqual(len(result['members']),12)
        runtime['observed_at']=(datetime.now(timezone.utc)-timedelta(seconds=30)).isoformat()
        self.assertTrue(all(m['runtime']=={'state':'unavailable'} for m in public_sample(packet,'installation','123','a'*40)['members']))
