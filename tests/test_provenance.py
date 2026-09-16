"""Provenance must survive revisions without manufacturing relationships."""
import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import Engine, DEFAULTS
from wake.provenance import build_map
from wake.report import export


def project():
    return dict(type="project", id="p", title="A question", question="What distinguishes these accounts?",
                domain="cellular_automata", status="active", next_step="Read more", reason="Compare sources")


def notebook(evidence, findings="A bounded comparison of two sources."):
    return dict(type="notebook", id="n", project="p", title="A question", summary="Source comparison",
                findings=findings, limitations="Synthetic fixtures", next_questions="Collect more sources",
                evidence=evidence, reason="Keep source provenance")


def blog(identifier="post", **changes):
    action = dict(type="blog", id=identifier, project="p", title="A question", lede="A comparison of sources.",
                  body="The sources describe different aspects of the question. Their disagreement suggests a useful next comparison. " * 4,
                  notebooks=["n"], evidence=["s1", "s2"], reason="Share a source-backed comparison")
    return {**action, **changes}


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / "data", {**DEFAULTS, "mission": "Compare sources."})
        with self.engine.store.lock():
            self.engine.initialize()
            for sid in ("s1", "s2", "s3", "unrelated"):
                self.engine.store.append("observation", dict(id=sid, actor="collector", scope="collected",
                    source="https://example.org/" + sid,
                    content=json.dumps({"excerpt": "A question", "scope": "synthetic", "truncated": False})))

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def propose(self, actions):
        with self.engine.store.lock():
            iid, request = self.engine.start("fixture", "test")
            result = self.engine.finish(iid, json.dumps(dict(base_version=request["context"]["version"],
                title="A question", summary="A bounded fixture", actions=actions)))
        self.assertEqual(result["status"], "accepted", result)
        return iid

    def graph(self):
        state = self.engine.store.load()
        events = self.engine.store.events()
        serialized = json.dumps([state, events], sort_keys=True)
        graph = build_map(state, events, self.engine.store.replay()[1])
        self.assertEqual(json.dumps([state, events], sort_keys=True), serialized)
        return graph, {n["id"]: n for n in graph["nodes"]}

    def test_revisions_preserve_selected_cycle_evidence_and_explicit_changes(self):
        first = self.propose([project(), notebook(["s1", "s2"]), dict(type="belief", id="b", statement="A question",
            confidence=.5, status="active", evidence=["s1"], reason="Provisional"), blog()])
        second = self.propose([notebook(["s2", "s3"], "Changed findings"), blog("correction", supersedes="post", evidence=["s2", "s3"])])
        graph, nodes = self.graph()
        self.assertEqual(len(graph["journals"]), 2)
        self.assertEqual(len(graph["blogs"]), 2)
        self.assertEqual(nodes['notebook:n@1']['detail']['evidence'], ['s1', 's2'])
        self.assertEqual(nodes['notebook:n@2']['detail']['evidence'], ['s2', 's3'])
        triples = {(e['source'], e['target'], e['relation']) for e in graph['edges']}
        self.assertIn((f'journal:{first}', 'notebook:n@1', 'created'), triples)
        self.assertIn((f'journal:{second}', 'notebook:n@2', 'revised'), triples)
        self.assertIn(('blog:post', f'journal:{first}', 'originating wake'), triples)
        self.assertIn(('blog:correction', 'blog:post', 'supersedes'), triples)
        self.assertIn(('blog:post', 'blog:correction', 'superseded by'), triples)
        self.assertIn(('belief:b@1', 'evidence:s1', 'evidence'), triples)
        self.assertNotIn(('notebook:n@1', 'evidence:s3', 'evidence'), triples)
        self.assertNotIn('evidence:unrelated', nodes)
        self.assertEqual(nodes['blog:post']['detail']['status'], 'superseded')
        self.assertTrue(all(e['record'] and e['source'] in nodes and e['target'] in nodes for e in graph['edges']))
        self.assertIn('working_set_metrics', nodes[f'invocation:{first}']['detail'])
        self.assertNotIn('working_set_shadow', nodes[f'invocation:{first}']['detail'])
        self.assertEqual(nodes['evidence:s1']['detail']['collected_content']['excerpt'], 'A question')

    def test_withheld_blog_is_only_an_editorial_record(self):
        iid = self.propose([project(), notebook(["s1", "s2"]), blog(evidence=["s1", "missing"])])
        graph, nodes = self.graph()
        self.assertEqual(graph['blogs'], [])
        self.assertEqual(nodes[f'editorial:{iid}']['detail']['status'], 'withheld')
        self.assertNotIn('blog:post', nodes)

    def test_no_origin_link_is_inferred_from_matching_text_or_version(self):
        iid = self.propose([project(), notebook(["s1", "s2"]), blog()])
        state = self.engine.store.load()
        state['posts']['post'].pop('created_by')
        graph = build_map(state, self.engine.store.events(), self.engine.store.replay()[1])
        self.assertFalse(any(e['source']=='blog:post' and e['relation']=='originating wake' for e in graph['edges']))
        self.assertIn('blog:post', graph['blogs'])

    def test_export_is_static_safe_and_reproducible(self):
        self.propose([project(), notebook(["s1", "s2"], '</script><script>alert("no")</script>'), blog()])
        export(self.engine.store, self.root/'site')
        page = (self.root/'site/map.html').read_text()
        graph = json.loads((self.root/'site/map-data.json').read_text())
        embedded = json.loads(page.split('<script id="map-data" type="application/json">')[1].split('</script>')[0])
        self.assertEqual(embedded, graph)
        self.assertNotIn('</script><script>alert("no")</script>', page)
        self.assertIn('href="map.html"', (self.root/'site/index.html').read_text())
        self.assertIn('aria-label="Record details"', page)
        self.assertIn('prefers-reduced-motion', page)
        self.assertIn('<strong>WAKE✳︎</strong>', page)
        self.assertNotIn('fetch(', page)
        self.assertNotIn('working_set_shadow', page)
        self.assertEqual(graph, self.graph()[0])
        self.assertTrue(all('expands' in n for n in graph['nodes'] if n['kind']=='journal'))
        self.assertNotIn('data-node=', page.split('<script id="map-data"')[0])

    def test_empty_export_and_missing_shadow_metrics(self):
        graph, _ = self.graph()
        self.assertEqual(graph['journals'], [])
        iid = self.propose([project()])
        state = self.engine.store.load()
        state['invocations'][iid].pop('working_set_metrics')
        state['invocations'][iid].pop('retrieval_shadow')
        graph = build_map(state, self.engine.store.events(), self.engine.store.replay()[1])
        invocation = next(n for n in graph['nodes'] if n['id']==f'invocation:{iid}')
        self.assertNotIn('working_set_metrics', invocation['detail'])
        self.assertNotIn('retrieval_metrics', invocation['detail'])
