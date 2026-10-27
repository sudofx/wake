#!/usr/bin/env python3
"""Run at most eight paired evaluation requests; never open operator records."""
import argparse
import os
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from wake.knowledge_evaluation import evaluate, FixtureGeneration
from wake.kernel.generation import GeminiGenerationProvider


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--provider',choices=('fixture','gemini'),default='fixture')
    parser.add_argument('--model',default='gemini-3.5-flash-lite')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--cases',type=Path,default=Path(__file__).resolve().parents[1]/'tests/fixtures/decision_memory.json')
    args=parser.parse_args()
    provider=FixtureGeneration() if args.provider=='fixture' else GeminiGenerationProvider(os.environ.get('GEMINI_API_KEY',''),timeout_seconds=45)
    report=evaluate(args.cases,provider,args.model if args.provider=='gemini' else 'fixture',args.output,fixture=args.provider=='fixture')
    print(report['status']+': '+str(args.output))
    return 0 if report['status']=='completed' else 1


if __name__=='__main__':
    raise SystemExit(main())
