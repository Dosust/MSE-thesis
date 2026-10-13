"""Structural regression tests only: they do not verify rights, physical truth or renders."""
import copy
import json
import unittest
from pathlib import Path
from validate_deck3_visual_manifest import InvalidManifest, check

BASE = json.loads((Path(__file__).parent / 'deck3_visual_asset_example.json').read_text())

class VisualManifestTests(unittest.TestCase):
    def bad(self, update):
        d = copy.deepcopy(BASE)
        update(d)
        with self.assertRaises(InvalidManifest):
            check(d)

    def test_accept_valid_abstract_asset(self):
        self.assertEqual(check(BASE)['decision'], 'STRUCTURE_ACCEPTED_NOT_SCIENCE_OR_RIGHTS_VERIFIED')

    def test_reject_whole_slide(self):
        self.bad(lambda d: d.update(asset_only=False, whole_slide_screenshot=True))

    def test_reject_collage(self):
        self.bad(lambda d: d.update(collage=True))

    def test_reject_wrong_slide_variant(self):
        self.bad(lambda d: d.update(presentation_variant='CANONICAL_EIGHT_SLIDE'))

    def test_reject_incomplete_three_bullets(self):
        self.bad(lambda d: d['three_bullets'].pop())

    def test_reject_wrong_filename(self):
        self.bad(lambda d: d['outputs'].update(png='combined_10_slides.png'))

    def test_reject_unlicensed_embedded_photo(self):
        self.bad(lambda d: d.update(source_mode='EMBED_REAL_PHOTO', embedded_real_photo_count=1))

    def test_reject_original_grounded_no_sources(self):
        self.bad(lambda d: d.update(source_mode='ORIGINAL_SOURCE_GROUNDED'))

    def test_reject_off_palette(self):
        self.bad(lambda d: d['style']['authored_colors'].append('#FACADE'))

    def test_reject_gold_decorative(self):
        self.bad(lambda d: d['style']['authored_colors'].append('#FFC627'))

    def test_reject_colored_panel(self):
        self.bad(lambda d: d['style'].update(panel='#0072B2'))

    def test_reject_invented_cross_heat_flow(self):
        def change(d):
            d['nodes'].extend([{'id':'P1','system':'POWER'},{'id':'T1','system':'TRANSPORT'}])
            d['arrows'].append({'id':'A05','type':'HEAT_TRANSFER','source':'T1','target':'P1','evidence_status':'ESTABLISHED_GENERIC','label':'Invented thermal transmission'})
        self.bad(change)

    def test_reject_unqualified_candidate_misrepresented(self):
        def change(d):
            d['nodes'].extend([{'id':'P1','system':'POWER'},{'id':'T1','system':'TRANSPORT'}])
            d['arrows'].append({'id':'A05','type':'CANDIDATE_T_TO_P','source':'T1','target':'P1','evidence_status':'MEASURED','label':'I2 measured','hypothesis':'I2/H1'})
        self.bad(change)

    def test_reject_wrong_causality_orientation(self):
        def change(d):
            d['nodes'].extend([{'id':'P1','system':'POWER'},{'id':'T1','system':'TRANSPORT'}])
            d['arrows'].append({'id':'A05','type':'CANDIDATE_P_TO_T','source':'T1','target':'P1','evidence_status':'CANDIDATE_UNQUALIFIED','label':'I3 not yet qualified','hypothesis':'I3/H2'})
        self.bad(change)

    def test_accept_qualified_candidate_only_structurally(self):
        d = copy.deepcopy(BASE)
        d['nodes'].extend([{'id':'P1','system':'POWER'},{'id':'T1','system':'TRANSPORT'}])
        d['arrows'].append({'id':'A05','type':'CANDIDATE_T_TO_P','source':'T1','target':'P1','evidence_status':'CANDIDATE_UNQUALIFIED','label':'I2 NOT YET QUALIFIED','hypothesis':'I2/H1'})
        self.assertEqual(check(d)['arrows'], 5)

    def test_reject_wrong_power_direction(self):
        def change(d):
            d['nodes'].extend([{'id':'P1','system':'POWER'},{'id':'P2','system':'POWER'}])
            d['arrows'].append({'id':'A05','type':'AC_POWER','source':'P2','target':'P1','evidence_status':'ESTABLISHED_GENERIC','label':'Wrong'})
        self.bad(change)

    def test_reject_missing_no_photo_justification(self):
        self.bad(lambda d: d.update(no_photo_reason=''))

if __name__ == '__main__':
    unittest.main()
