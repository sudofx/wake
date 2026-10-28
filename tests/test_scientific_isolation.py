"""Real Docker boundary probes; no mock can certify these guarantees."""
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.improvement_runner import DEFAULT_IMAGE, image_identity, run_program
from wake.science.instruments import RUNNER


class ScientificIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:cls.image=image_identity(DEFAULT_IMAGE)
        except (ValueError,OSError):raise unittest.SkipTest('Reviewed Docker image unavailable')
    def run_code(self,source,seconds=5):
        return run_program(source,{},self.image,timeout=seconds,runner=RUNNER)
    def test_credentials_and_withheld_scorer_are_not_mounted(self):
        source='''import os
def experiment(inputs):
 return {'secret':os.environ.get('WAKE_TEST_SECRET'),'files':sorted(os.listdir('/experiment')),'uid':os.getuid()}
'''
        with patch.dict(os.environ,WAKE_TEST_SECRET='must-never-enter-untrusted-container'):
            r=self.run_code(source)
        self.assertEqual(r['status'],'completed',r)
        self.assertTrue(r['cleanup_confirmed'])
        self.assertIsNone(r['outputs']['secret'])
        self.assertEqual(r['outputs']['uid'],65534)
        self.assertEqual(r['outputs']['files'],['inputs.json','program.py','runner.py'])
    def test_host_files_and_runner_inputs_cannot_be_modified(self):
        with tempfile.TemporaryDirectory() as temp:
            target=Path(temp)/'authority.txt';target.write_text('preserve authority')
            source=f'''def experiment(inputs):
 denied=[]
 for path in {str([str(target),'/experiment/runner.py','/experiment/inputs.json','/experiment/expected.json','/var/run/docker.sock'])}:
  try:
   with open(path,'w') as f:f.write('forge')
   denied.append(False)
  except OSError:denied.append(True)
 return denied
'''
            r=self.run_code(source)
            self.assertEqual(r['status'],'completed',r)
            self.assertEqual(r['outputs'],[True]*5)
            self.assertEqual(target.read_text(),'preserve authority')
    def test_network_is_unavailable(self):
        r=self.run_code('''import socket
def experiment(inputs):
 try:
  socket.create_connection(('1.1.1.1',443),timeout=.5)
  return False
 except OSError:return True
''')
        self.assertEqual(r['status'],'completed',r);self.assertTrue(r['outputs'])
    def test_time_output_and_memory_limits_fail_visibly(self):
        for source,seconds in [('def experiment(inputs):\n while True:pass',1),
                               ('def experiment(inputs):\n print("x"*200000)\n return {}',5),
                               ('def experiment(inputs):\n return len(bytearray(512*1024*1024))',5)]:
            with self.subTest(source=source):
                r=self.run_code(source,seconds)
                self.assertEqual(r['status'],'failed',r)
                self.assertIn('reason',r)
    def test_process_limit_prevents_unbounded_child_creation(self):
        r=self.run_code('''import os,time
def experiment(inputs):
 children=[];limited=False
 for _ in range(80):
  try:
   pid=os.fork()
   if pid==0:
    time.sleep(1)
    os._exit(0)
   children.append(pid)
  except OSError:
   limited=True;break
 for child in children:os.waitpid(child,0)
 return {'limited':limited,'spawned':len(children)}
''',seconds=5)
        self.assertEqual(r['status'],'completed',r)
        self.assertTrue(r['outputs']['limited'])
        self.assertLess(r['outputs']['spawned'],32)
