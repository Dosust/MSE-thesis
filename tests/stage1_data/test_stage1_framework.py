"""Case-independent verification suite for the frozen-candidate Stage-1 v2 framework."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

import networkx as nx
from jsonschema import Draft202012Validator, ValidationError
from shapely.geometry import Polygon


REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "schemas"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


normalization = load_module(
    "stage1_normalization", REPO / "methods" / "stage1_data" / "normalization.py"
)
adapter_contract = load_module(
    "stage1_adapter_contract", REPO / "methods" / "stage1_data" / "adapter_contract.py"
)


class Stage1FrameworkVerification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.structure_schema = json.loads(
            (SCHEMAS / "stage1_structure.schema.json").read_text(encoding="utf-8")
        )
        cls.manifest_schema = json.loads(
            (SCHEMAS / "stage1_source_manifest.schema.json").read_text(encoding="utf-8")
        )
        cls.structure = json.loads(
            (FIXTURES / "stage1_structure_valid.json").read_text(encoding="utf-8")
        )
        cls.manifests = json.loads(
            (FIXTURES / "source_manifests.json").read_text(encoding="utf-8")
        )
        cls.structure_validator = Draft202012Validator(cls.structure_schema)
        cls.manifest_validator = Draft202012Validator(cls.manifest_schema)

    def relation(self, relation_id: str):
        return next(
            r for r in self.structure["candidate_relations"] if r["relation_id"] == relation_id
        )

    def test_01_schema_definitions_are_valid(self):
        Draft202012Validator.check_schema(self.structure_schema)
        Draft202012Validator.check_schema(self.manifest_schema)

    def test_02_structure_schema_is_v2(self):
        self.assertEqual(self.structure_schema["properties"]["version"]["const"], "2.0")
        self.assertEqual(self.structure["version"], "2.0")

    def test_03_all_supported_source_classes_have_valid_manifests(self):
        observed = {m["source_type"] for m in self.manifests}
        expected = {
            "vector_geospatial", "raster_geospatial", "tabular", "graph_network",
            "power_system_model", "transport_network", "time_indexed_records",
            "api_snapshot", "document_metadata", "normative_authority",
        }
        self.assertTrue(expected.issubset(observed))
        for manifest in self.manifests:
            self.manifest_validator.validate(manifest)

    def test_04_normative_source_requires_authority_metadata(self):
        normative = next(m for m in self.manifests if m["source_type"] == "normative_authority")
        broken = copy.deepcopy(normative)
        broken.pop("authority_metadata")
        with self.assertRaises(ValidationError):
            self.manifest_validator.validate(broken)

    def test_05_valid_v2_structural_handoff_conforms(self):
        self.structure_validator.validate(self.structure)

    def test_06_schema_rejects_causal_promotion(self):
        broken = copy.deepcopy(self.structure)
        broken["candidate_relations"][0]["causal_dependency_accepted"] = True
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_07_runtime_rejects_causal_promotion(self):
        bundle = adapter_contract.CanonicalBundle(
            candidate_relations=[{"causal_dependency_accepted": True}]
        )
        with self.assertRaises(ValueError):
            adapter_contract.assert_stage1_noncausal(bundle)

    def test_08_schema_rejects_stage1_strength_estimation(self):
        broken = copy.deepcopy(self.structure)
        broken["candidate_relations"][0]["strength_status"] = "ESTIMATED"
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_09_runtime_rejects_stage1_strength_estimation(self):
        relation = copy.deepcopy(self.relation("rel:p1-t1"))
        relation["strength_status"] = "ESTIMATED"
        with self.assertRaises(ValueError):
            adapter_contract.assert_stage1_relation_semantics(
                adapter_contract.CanonicalBundle(candidate_relations=[relation])
            )

    def test_10_template_state_is_template_only(self):
        relation = copy.deepcopy(self.relation("tpl:p-t-signal"))
        relation["structural_existence"] = "CANDIDATE"
        with self.assertRaises(ValidationError):
            self.structure_validator.validate({**self.structure, "candidate_relations": [relation]})

    def test_11_case_relation_cannot_be_template_only(self):
        relation = copy.deepcopy(self.relation("rel:p1-t1"))
        relation["structural_existence"] = "TEMPLATE_ONLY"
        with self.assertRaises(ValidationError):
            self.structure_validator.validate({**self.structure, "candidate_relations": [relation]})

    def test_12_pairwise_relation_requires_exactly_two_participants(self):
        relation = copy.deepcopy(self.relation("rel:p1-t1"))
        relation["participants"].append(
            {"entity_id": "extra", "layer": "information", "role": "extra"}
        )
        with self.assertRaises(ValidationError):
            self.structure_validator.validate({**self.structure, "candidate_relations": [relation]})

    def test_13_higher_order_relation_has_three_participants(self):
        relation = self.relation("tpl:ev-charge-higher-order")
        self.assertEqual(relation["metadata"]["arity"], "HIGHER_ORDER")
        self.assertGreaterEqual(len(relation["participants"]), 3)
        adapter_contract.assert_stage1_relation_semantics(
            adapter_contract.CanonicalBundle(candidate_relations=[copy.deepcopy(relation)])
        )

    def test_14_mediated_relation_requires_mediator_path(self):
        relation = copy.deepcopy(self.relation("rel:t2-p2"))
        relation["metadata"]["mediator_path"] = []
        with self.assertRaises(ValidationError):
            self.structure_validator.validate({**self.structure, "candidate_relations": [relation]})

    def test_15_context_relation_is_not_pt_causality(self):
        relation = self.relation("tpl:context-flood")
        self.assertEqual(relation["scope"], "CONTEXT")
        self.assertEqual(relation["mechanism_status"], "CONTEXT_ONLY")
        self.assertFalse(relation["causal_dependency_accepted"])
        adapter_contract.assert_stage1_relation_semantics(
            adapter_contract.CanonicalBundle(candidate_relations=[copy.deepcopy(relation)])
        )

    def test_16_numeric_evidence_confidence_requires_method(self):
        relation = copy.deepcopy(self.relation("rel:p1-t1"))
        relation["metadata"]["evidence_confidence"] = {
            "confidence_class": "HIGH", "score": 0.9, "method": None
        }
        with self.assertRaises(ValidationError):
            self.structure_validator.validate({**self.structure, "candidate_relations": [relation]})

    def test_17_verified_case_relation_requires_case_structural_basis(self):
        relation = copy.deepcopy(self.relation("rel:p1-t1"))
        relation["metadata"]["admission_basis"] = ["PRIOR_LITERATURE", "NORMATIVE_INTERFACE"]
        with self.assertRaises(ValueError):
            adapter_contract.assert_stage1_relation_semantics(
                adapter_contract.CanonicalBundle(candidate_relations=[relation])
            )

    def test_18_entity_semantics_are_required(self):
        entity = copy.deepcopy(self.structure["entities"][0])
        adapter_contract.assert_stage1_entity_semantics(
            adapter_contract.CanonicalBundle(entities=[entity])
        )
        for missing in ("engineering_functions", "resolution_level", "evidence_refs"):
            broken = copy.deepcopy(entity)
            broken.pop(missing)
            with self.assertRaises(ValueError):
                adapter_contract.assert_stage1_entity_semantics(
                    adapter_contract.CanonicalBundle(entities=[broken])
                )

    def test_19_pt_signal_semantics_are_explicit(self):
        relation = self.relation("rel:p1-t1")
        self.assertEqual(relation["layer_pair"], "P->T")
        self.assertIn("electrical", relation["exchange_semantics"].lower())
        self.assertEqual(relation["structural_existence"], "VERIFIED_STRUCTURAL")

    def test_20_tp_repair_access_semantics_are_explicit(self):
        relation = self.relation("rel:t2-p2")
        self.assertEqual(relation["layer_pair"], "T->P")
        self.assertIn("travel-time", relation["exchange_semantics"].lower())
        self.assertEqual(relation["metadata"]["path"], "MEDIATED")

    def test_21_intra_relation_remains_within_one_layer(self):
        relation = self.relation("tpl:pp-topology")
        layers = {p["layer"] for p in relation["participants"]}
        self.assertEqual(layers, {"power"})
        adapter_contract.assert_stage1_relation_semantics(
            adapter_contract.CanonicalBundle(candidate_relations=[copy.deepcopy(relation)])
        )

    def test_22_inter_relation_uses_multiple_layers(self):
        relation = self.relation("rel:p1-t1")
        layers = {p["layer"] for p in relation["participants"]}
        self.assertGreaterEqual(len(layers), 2)
        adapter_contract.assert_stage1_relation_semantics(
            adapter_contract.CanonicalBundle(candidate_relations=[copy.deepcopy(relation)])
        )

    def test_23_normative_conformity_cannot_create_causality(self):
        relation = copy.deepcopy(self.relation("rel:p1-t1"))
        relation["causal_dependency_accepted"] = True
        with self.assertRaises(ValueError):
            adapter_contract.assert_normative_noncausal(
                adapter_contract.CanonicalBundle(candidate_relations=[relation])
            )

    def test_24_identifier_stability(self):
        first = normalization.stable_id("power.bus", "raw-001")
        second = normalization.stable_id("power.bus", "raw-001")
        different = normalization.stable_id("transport.node", "raw-001")
        self.assertEqual(first, second)
        self.assertNotEqual(first, different)

    def test_25_provenance_sha256_round_trip(self):
        raw = b"immutable-stage1-fixture-bytes"
        digest = normalization.sha256_bytes(raw)
        self.assertEqual(len(digest), 64)
        self.assertEqual(digest, normalization.sha256_bytes(raw))

    def test_26_crs_normalization_known_origin(self):
        x, y = normalization.transform_xy(
            0.0, 0.0, source_crs="EPSG:4326", target_crs="EPSG:3857"
        )
        self.assertAlmostEqual(x, 0.0, places=8)
        self.assertAlmostEqual(y, 0.0, places=8)

    def test_27_unit_normalization(self):
        self.assertEqual(normalization.convert_unit(11.0, "kV", "V"), 11000.0)
        self.assertEqual(normalization.convert_unit(2.0, "km", "m"), 2000.0)

    def test_28_missingness_is_preserved_not_imputed(self):
        unknown = normalization.normalize_missing(None, missing_kind="unknown")
        self.assertEqual(unknown, {"value": None, "missing_kind": "unknown"})
        self.assertEqual(normalization.normalize_missing(0), {"value": 0, "missing_kind": None})
        with self.assertRaises(ValueError):
            normalization.normalize_missing(None)

    def test_29_geometry_repair_is_explicit(self):
        bowtie = Polygon([(0, 0), (1, 1), (1, 0), (0, 1), (0, 0)])
        raw_geom, raw_qa = normalization.validate_or_repair_geometry(bowtie, allow_repair=False)
        self.assertFalse(raw_qa.original_valid)
        self.assertFalse(raw_qa.repaired)
        fixed_geom, fixed_qa = normalization.validate_or_repair_geometry(bowtie, allow_repair=True)
        self.assertTrue(fixed_qa.repaired)
        self.assertTrue(fixed_geom.is_valid)
        self.assertEqual(raw_geom.wkt, bowtie.wkt)

    def test_30_topology_direction_is_preserved(self):
        graph = normalization.directed_topology([("A", "B"), ("B", "C")])
        self.assertTrue(nx.has_path(graph, "A", "C"))
        self.assertFalse(nx.has_path(graph, "C", "A"))

    def test_31_temporal_role_is_preserved(self):
        manifest = next(m for m in self.manifests if m["temporal_semantics"] == "retrospective")
        self.assertEqual(normalization.preserve_temporal_role(manifest), "retrospective")

    def test_32_nonapplicable_authority_does_not_become_constraint(self):
        applicability = normalization.resolve_authority_applicability(
            case_jurisdiction="JUR-A", authority_jurisdiction="JUR-B",
            technical_scope_match=True, status="current"
        )
        self.assertEqual(applicability, "NOT_APPLICABLE")
        self.assertFalse(normalization.authority_becomes_model_constraint(applicability))

    def test_33_current_in_scope_authority_can_be_constraint(self):
        applicability = normalization.resolve_authority_applicability(
            case_jurisdiction="JUR-A", authority_jurisdiction="JUR-A",
            technical_scope_match=True, status="current"
        )
        self.assertEqual(applicability, "APPLICABLE")
        self.assertTrue(normalization.authority_becomes_model_constraint(applicability))

    def test_34_normative_authority_reference_integrity(self):
        authority_ids = {a["authority_id"] for a in self.structure["normative_register"]}
        for relation in self.structure["candidate_relations"]:
            for authority_id in relation.get("normative_authority_ids", []):
                self.assertIn(authority_id, authority_ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)