"""Case-independent verification suite for the generic Stage-1 framework."""

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

    def test_01_schema_definitions_are_valid(self):
        Draft202012Validator.check_schema(self.structure_schema)
        Draft202012Validator.check_schema(self.manifest_schema)

    def test_02_all_supported_source_classes_have_valid_manifests(self):
        observed = {m["source_type"] for m in self.manifests}
        expected = {
            "vector_geospatial",
            "raster_geospatial",
            "tabular",
            "graph_network",
            "power_system_model",
            "transport_network",
            "time_indexed_records",
            "api_snapshot",
            "document_metadata",
            "normative_authority",
        }
        self.assertTrue(expected.issubset(observed))
        for manifest in self.manifests:
            self.manifest_validator.validate(manifest)

    def test_03_normative_source_requires_authority_metadata(self):
        normative = next(
            m for m in self.manifests if m["source_type"] == "normative_authority"
        )
        broken = copy.deepcopy(normative)
        broken.pop("authority_metadata")
        with self.assertRaises(ValidationError):
            self.manifest_validator.validate(broken)

    def test_04_valid_structural_handoff_conforms(self):
        self.structure_validator.validate(self.structure)

    def test_05_stage1_schema_rejects_causal_promotion(self):
        broken = copy.deepcopy(self.structure)
        broken["candidate_relations"][0]["causal_dependency_accepted"] = True
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_06_runtime_guard_rejects_causal_promotion(self):
        bundle = adapter_contract.CanonicalBundle(
            candidate_relations=[{"causal_dependency_accepted": True}]
        )
        with self.assertRaises(ValueError):
            adapter_contract.assert_stage1_noncausal(bundle)

    def test_07_normative_conformity_cannot_create_causality(self):
        bundle = adapter_contract.CanonicalBundle(
            candidate_relations=[
                {
                    "normative_admissibility": "PASS",
                    "causal_dependency_accepted": True,
                }
            ]
        )
        with self.assertRaises(ValueError):
            adapter_contract.assert_normative_noncausal(bundle)

    def test_08_identifier_stability(self):
        first = normalization.stable_id("power.bus", "raw-001")
        second = normalization.stable_id("power.bus", "raw-001")
        different = normalization.stable_id("transport.node", "raw-001")
        self.assertEqual(first, second)
        self.assertNotEqual(first, different)

    def test_09_provenance_sha256_round_trip(self):
        raw = b"immutable-stage1-fixture-bytes"
        digest = normalization.sha256_bytes(raw)
        self.assertEqual(len(digest), 64)
        self.assertEqual(digest, normalization.sha256_bytes(raw))

    def test_10_crs_normalization_known_origin(self):
        x, y = normalization.transform_xy(
            0.0, 0.0, source_crs="EPSG:4326", target_crs="EPSG:3857"
        )
        self.assertAlmostEqual(x, 0.0, places=8)
        self.assertAlmostEqual(y, 0.0, places=8)

    def test_11_unit_normalization(self):
        self.assertEqual(normalization.convert_unit(11.0, "kV", "V"), 11000.0)
        self.assertEqual(normalization.convert_unit(2.0, "km", "m"), 2000.0)

    def test_12_missingness_is_preserved_not_imputed(self):
        unknown = normalization.normalize_missing(None, missing_kind="unknown")
        self.assertIsNone(unknown["value"])
        self.assertEqual(unknown["missing_kind"], "unknown")
        present = normalization.normalize_missing(0)
        self.assertEqual(present, {"value": 0, "missing_kind": None})
        with self.assertRaises(ValueError):
            normalization.normalize_missing(None)

    def test_13_geometry_repair_is_explicit(self):
        bowtie = Polygon([(0, 0), (1, 1), (1, 0), (0, 1), (0, 0)])
        raw_geom, raw_qa = normalization.validate_or_repair_geometry(
            bowtie, allow_repair=False
        )
        self.assertFalse(raw_qa.original_valid)
        self.assertFalse(raw_qa.released_valid)
        self.assertFalse(raw_qa.repaired)
        fixed_geom, fixed_qa = normalization.validate_or_repair_geometry(
            bowtie, allow_repair=True
        )
        self.assertTrue(fixed_qa.repaired)
        self.assertTrue(fixed_qa.released_valid)
        self.assertTrue(fixed_geom.is_valid)
        self.assertEqual(fixed_qa.repair_operation, "shapely.make_valid")
        self.assertEqual(raw_geom.wkt, bowtie.wkt)

    def test_14_topology_direction_is_preserved(self):
        graph = normalization.directed_topology([("A", "B"), ("B", "C")])
        self.assertTrue(nx.has_path(graph, "A", "C"))
        self.assertFalse(nx.has_path(graph, "C", "A"))

    def test_15_temporal_role_is_preserved(self):
        manifest = next(
            m for m in self.manifests if m["temporal_semantics"] == "retrospective"
        )
        self.assertEqual(
            normalization.preserve_temporal_role(manifest), "retrospective"
        )

    def test_16_nonapplicable_authority_does_not_become_constraint(self):
        applicability = normalization.resolve_authority_applicability(
            case_jurisdiction="JUR-A",
            authority_jurisdiction="JUR-B",
            technical_scope_match=True,
            status="current",
        )
        self.assertEqual(applicability, "NOT_APPLICABLE")
        self.assertFalse(
            normalization.authority_becomes_model_constraint(applicability)
        )

    def test_17_current_in_scope_authority_can_be_admissible_constraint(self):
        applicability = normalization.resolve_authority_applicability(
            case_jurisdiction="JUR-A",
            authority_jurisdiction="JUR-A",
            technical_scope_match=True,
            status="current",
        )
        self.assertEqual(applicability, "APPLICABLE")
        self.assertTrue(
            normalization.authority_becomes_model_constraint(applicability)
        )

    def test_18_normative_register_and_candidate_reference_are_consistent(self):
        authority_ids = {a["authority_id"] for a in self.structure["normative_register"]}
        for relation in self.structure["candidate_relations"]:
            for authority_id in relation.get("normative_authority_ids", []):
                self.assertIn(authority_id, authority_ids)

    def test_19_entity_semantics_are_required(self):
        broken = copy.deepcopy(self.structure)
        broken["entities"][0].pop("engineering_functions")
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_20_relation_exchange_semantics_are_required(self):
        broken = copy.deepcopy(self.structure)
        broken["candidate_relations"][0].pop("exchange_semantics")
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_21_stage1_strength_estimation_is_rejected_by_schema(self):
        broken = copy.deepcopy(self.structure)
        broken["candidate_relations"][0]["strength_status"] = "ESTIMATED"
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_22_runtime_rejects_stage1_strength_estimation(self):
        relation = copy.deepcopy(self.structure["candidate_relations"][0])
        relation["strength_status"] = "ESTIMATED"
        bundle = adapter_contract.CanonicalBundle(candidate_relations=[relation])
        with self.assertRaises(ValueError):
            adapter_contract.assert_stage1_relation_semantics(bundle)

    def test_23_numeric_evidence_confidence_requires_method(self):
        broken = copy.deepcopy(self.structure)
        broken["candidate_relations"][0]["evidence_confidence"] = {
            "confidence_class": "HIGH",
            "score": 0.9,
            "method": None,
        }
        with self.assertRaises(ValidationError):
            self.structure_validator.validate(broken)

    def test_24_prior_or_normative_evidence_alone_cannot_verify_case_connection(self):
        relation = copy.deepcopy(self.structure["candidate_relations"][0])
        relation["structural_evidence"] = {
            "asset_crosswalk": False,
            "interface_hardware": True,
            "spatial_relation": False,
            "access_geometry": False,
            "geographic_coexposure": False,
        }
        relation["admission_basis"] = ["PRIOR_LITERATURE", "NORMATIVE_INTERFACE"]
        relation["case_connection_status"] = "VERIFIED_STRUCTURAL"
        bundle = adapter_contract.CanonicalBundle(candidate_relations=[relation])
        with self.assertRaises(ValueError):
            adapter_contract.assert_stage1_relation_semantics(bundle)

    def test_25_entity_function_resolution_and_evidence_runtime_guard(self):
        entity = copy.deepcopy(self.structure["entities"][0])
        bundle = adapter_contract.CanonicalBundle(entities=[entity])
        adapter_contract.assert_stage1_entity_semantics(bundle)
        for missing in ("engineering_functions", "resolution_level", "evidence_refs"):
            broken_entity = copy.deepcopy(entity)
            broken_entity.pop(missing)
            broken_bundle = adapter_contract.CanonicalBundle(entities=[broken_entity])
            with self.assertRaises(ValueError):
                adapter_contract.assert_stage1_entity_semantics(broken_bundle)

    def test_26_cross_layer_semantics_are_heterogeneous_and_strength_free(self):
        exchanges = {
            r["relation_id"]: r["exchange_semantics"]
            for r in self.structure["candidate_relations"]
        }
        self.assertEqual(
            exchanges["rel:p1-t1"], "electrical power/service availability"
        )
        self.assertEqual(
            exchanges["rel:t2-p2"], "crew accessibility / travel-time service"
        )
        for relation in self.structure["candidate_relations"]:
            self.assertEqual(
                relation["strength_status"], "NOT_ESTIMATED_STAGE1"
            )
            self.assertTrue(relation["resolution_level"])
            self.assertTrue(relation["evidence_refs"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
