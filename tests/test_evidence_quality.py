import json
import unittest
from wake.governance import Rejected, _verify_claim_support
from wake.evidence_quality import evidence_quality
from wake.research import PlainText, source_observation_readable, source_material_text


def source(identifier, work, excerpt, scope=''):
    return dict(id=identifier, actor='collector', scope='collected', source='https://example.org/' + identifier,
                content=json.dumps(dict(source_identity=work, excerpt=excerpt, scope=scope)))


class QualityTests(unittest.TestCase):
    def test_empty_and_failed_payloads_are_not_readable_sources(self):
        for payload in ({}, {"excerpt": ""}, {"error": "ValueError", "scope": "fetch failed; no evidence obtained"}):
            self.assertFalse(source_observation_readable(payload))

    def test_publisher_menu_and_response_form_cannot_support_a_claim(self):
        chrome = ("Components of Electoral Decision\nMenu links\nBrowse\nPolitical Science\n"
                  "Institution Login\nPlease list any fees and grants from, employment by, consultancy for, "
                  "any organisation whose interests may be affected by the publication of the response.\n"
                  "Please tick the box to confirm your institutional information and research are visible.\nYes\nNo")
        self.assertFalse(source_observation_readable({"excerpt": chrome}))
        items = [source('one', 'doi:one', chrome), source('two', 'doi:two', chrome)]
        with self.assertRaises(Rejected):
            _verify_claim_support('Institutional information changes electoral decision research', items, 'Claim')
        quality = evidence_quality({'evidence': {item['id']: item for item in items},
            'notebooks': {'n': {'id': 'n', 'findings': 'Institutional information', 'evidence': ['one', 'two']}}})
        self.assertEqual(quality['notebooks'][0]['unreadable_source_ids'], ['one', 'two'])

    def test_real_prose_survives_publisher_chrome_filter(self):
        prose = 'Our experiments compare institutional information filtering across independent observers and report measurable differences in their decision making.'
        payload = {'excerpt': 'Menu links\nScience\n' + prose + '\nPlease list any fees and grants from your institution.'}
        self.assertEqual(source_material_text(payload), prose)
        self.assertTrue(source_observation_readable(payload))

    def test_navigation_labels_alone_are_not_readable_material(self):
        payload = {'excerpt': 'Menu links\nBrowse\nSubjects\nScience\nInstitutional Research\nPolitical Decision Making\nInformation'}
        self.assertFalse(source_observation_readable(payload))

    def test_html_prefers_article_and_excludes_menus_hidden_content_and_forms(self):
        prose = 'Our experiments compare institutional information filtering across independent observers and report measurable differences in their decision making.'
        parser = PlainText()
        parser.feed('<div class="menu">Science institutional information</div><main><article><p>' + prose +
            '</p><div aria-hidden="true">Invisible research claim</div><form>Institutional information form</form></article></main>')
        self.assertEqual(parser.text(), prose)

    def test_valueless_html_attributes_do_not_break_extraction(self):
        parser = PlainText()
        parser.feed('<div class id><p>Readable source text.</p></div>')
        self.assertIn('Readable source text.', parser.text())

    def test_mirrors_cannot_supply_two_supporting_works(self):
        mirrors = [source('one', 'doi:one', 'quantum entropy measurement'), source('two', 'doi:one', 'quantum entropy measurement')]
        with self.assertRaisesRegex(Rejected, 'underlying source'):
            _verify_claim_support('quantum entropy measurement', mirrors, 'Claim')
        _verify_claim_support('quantum entropy measurement', mirrors + [source('three', 'doi:two', 'quantum entropy measurement')], 'Claim')

    def test_scope_label_cannot_supply_claim_support(self):
        unrelated = [source('one', 'doi:one', 'musical perception', 'quantum entropy measurement')]
        with self.assertRaises(Rejected):
            _verify_claim_support('quantum entropy measurement', unrelated, 'Claim', minimum_sources=1)

    def test_diagnostics_expose_repeated_work_and_mismatch(self):
        evidence = {x['id']: x for x in [source('one', 'doi:one', 'entropy measurement'), source('two', 'doi:one', 'musical perception')]}
        quality = evidence_quality(dict(evidence=evidence, notebooks={
            'n': dict(id='n', findings='entropy measurement', evidence=['one', 'two']),
            'm': dict(id='m', findings='entropy measurement', evidence=['one'])}))
        self.assertEqual(quality['distinct_works'], 1)
        self.assertEqual(quality['mirror_or_repeat_observations'], 1)
        self.assertEqual(quality['reused_works'][0]['notebook_count'], 2)
        self.assertEqual(quality['notebooks'][0]['possible_mismatch_ids'], ['two'])
