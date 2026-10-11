#!/usr/bin/env python3
"""Operator-only, digest-bound WAKE01 exception; never starts research.

Run inside each enrolled installation with the same reviewed publication file.
Existing history is preserved; only the introductory article is published.
"""
import argparse
import json
from pathlib import Path
from wake.authority import open_authoritative_store
from wake.event_format import digest
from wake.governance import require


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',default='/data')
    parser.add_argument('--publication',required=True)
    parser.add_argument('--confirm-wake01-exception',dest='confirm',action='store_true')
    parser.add_argument('--reason',required=True)
    args=parser.parse_args()
    require(args.confirm,'Explicit WAKE01 exception confirmation is required')
    p=json.loads(Path(args.publication).read_text())
    require(p.get('checkpoint')==1,'Only the first introduction is eligible')
    store=open_authoritative_store(args.data)
    try:
        with store.lock():
            state=store.load(); group=state.get('group_bob',{})
            if group.get('publication')==p:
                print(json.dumps({'status':'already-published','digest':digest(p)})); return
            if not group.get('exception'):
                store.append('group_bob_exception_granted',{'actor':'operator','checkpoint':1,
                    'publication_digest':digest(p),'reason':args.reason})
            store.append('group_bob_published',{'publication':p})
        print(json.dumps({'status':'published','digest':digest(p)}))
    finally:
        store.close()


if __name__=='__main__': main()
