"""Operational request admission, not scientific authority or provider quota proof."""
from datetime import datetime, timedelta
import math
from zoneinfo import ZoneInfo

PACIFIC=ZoneInfo('America/Los_Angeles')


class CallPacing:
    def __init__(self,policy,limits):
        if not isinstance(policy,dict) or set(policy)!={'enabled','target_hours','reserve_calls'}:
            raise ValueError('provider_pacing requires enabled, target_hours, reserve_calls')
        if type(policy['enabled']) is not bool:
            raise ValueError('Provider pacing enabled must be boolean')
        if type(policy['target_hours']) not in (int,float) or not math.isfinite(policy['target_hours']) or not 1<=policy['target_hours']<=24:
            raise ValueError('Provider pacing target_hours must be 1–24')
        if not isinstance(limits,dict) or not limits or any(not isinstance(k,str) or not k or type(v) is not int or v<1 for k,v in limits.items()):
            raise ValueError('Provider pacing requires explicit positive per-model daily limits')
        total=sum(limits.values())
        if type(policy['reserve_calls']) is not int or not 0<=policy['reserve_calls']<total:
            raise ValueError('Provider pacing reserve must leave a routine research allowance')
        self.policy=dict(policy);self.limits=dict(limits);self.total=total
        self.research_budget=total-policy['reserve_calls']
        self.interval=policy['target_hours']*3600/self.research_budget
        self.day=None;self.usage={};self.research_used=0;self.feature_used=0;self.next_at=0

    def _roll(self,now):
        day=datetime.fromtimestamp(now,PACIFIC).date().isoformat()
        if self.day!=day:
            self.day=day;self.usage={};self.research_used=0;self.feature_used=0
            # Keep spacing through midnight. Unused allowance never bursts.

    def check(self,model,purpose,now):
        self._roll(now)
        if not self.policy['enabled']:return True,0,'ready'
        tomorrow=(datetime.fromtimestamp(now,PACIFIC).replace(hour=0,minute=0,second=0,microsecond=0)+timedelta(days=1)).timestamp()
        if model not in self.limits:return False,300,'access_blocked'
        feature=purpose in ('reader','experiment')
        if self.usage.get(model,0)>=self.limits[model]:return False,tomorrow-now,'research_budget'
        if feature:
            if self.feature_used>=self.policy['reserve_calls']:return False,tomorrow-now,'research_budget'
        elif self.research_used>=self.research_budget:
            return False,tomorrow-now,'research_budget'
        elif self.next_at>now:return False,self.next_at-now,'pacing'
        return True,0,'ready'

    def consume(self,model,purpose,now):
        self._roll(now)
        self.usage[model]=self.usage.get(model,0)+1
        if purpose in ('reader','experiment'):self.feature_used+=1
        else:
            self.research_used+=1
            self.next_at=now+self.interval

    def seed(self,day,usage):
        """Conservatively include known native attempts before this policy existed."""
        if day!=self.day:return
        for model,count in usage.items():
            if model in self.limits and type(count) is int and count>=0:
                difference=max(0,count-self.usage.get(model,0))
                self.usage[model]=max(count,self.usage.get(model,0))
                self.research_used+=difference

    def dump(self):
        return {'day':self.day,'usage':dict(self.usage),'research_used':self.research_used,
                'feature_used':self.feature_used,'next_at':self.next_at}

    def restore(self,state):
        if not isinstance(state,dict) or set(state)!={'day','usage','research_used','feature_used','next_at'}:
            raise ValueError('Invalid persisted pacing state')
        if state['day'] is not None:
            if not isinstance(state['day'],str):raise ValueError('Invalid pacing day')
            datetime.strptime(state['day'],'%Y-%m-%d')
        if not isinstance(state['usage'],dict) or any(not isinstance(k,str) or type(v) is not int or v<0 for k,v in state['usage'].items()):
            raise ValueError('Invalid pacing usage')
        if any(type(state[k]) is not int or state[k]<0 for k in ('research_used','feature_used')):
            raise ValueError('Invalid pacing counters')
        if type(state['next_at']) not in (int,float) or not math.isfinite(state['next_at']) or state['next_at']<0:
            raise ValueError('Invalid pacing deadline')
        if sum(state['usage'].values())!=state['research_used']+state['feature_used']:
            raise ValueError('Pacing counts do not reconcile')
        self.day=state['day'];self.usage=dict(state['usage']);self.research_used=state['research_used']
        self.feature_used=state['feature_used'];self.next_at=state['next_at']

    def status(self,now):
        self._roll(now)
        return {**self.dump(),'enabled':self.policy['enabled'],'target_hours':self.policy['target_hours'],
                'configured_daily_calls':self.total,'routine_daily_calls':self.research_budget,
                'reserved_daily_calls':self.policy['reserve_calls'],'minimum_research_spacing_seconds':self.interval,
                'next_research_in_seconds':max(0,self.next_at-now)}
