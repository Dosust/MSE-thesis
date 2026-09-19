#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

GREENEVT_COMMIT="6aff1cac48869ccfa0183643979f5f04b04e1124"
UDS_SHA256="74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724"
UDS_SIZE="107778048"
SUMO_NET_SHA256="f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06"
SUMO_NET_SIZE="351967227"
IMAGE="thesis-stage3-greenevt:v1"
ART="runtime_artifacts"

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "ERROR: required command not found: $1" >&2
    exit 10
  }
}

need git
need docker
need sha256sum
need stat

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "ERROR: this qualification runner is frozen for Linux/amd64." >&2
  exit 11
fi

ARCH="$(uname -m)"
if [[ "$ARCH" != "x86_64" && "$ARCH" != "amd64" ]]; then
  echo "ERROR: expected amd64/x86_64, got $ARCH" >&2
  exit 12
fi

docker info >/dev/null

rm -rf "$ART"
mkdir -p "$ART" external

echo "==> Acquire frozen GreenEVT source"
if [[ ! -d external/GreenEVT/.git ]]; then
  GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/GreenEVT/GreenEVT.git external/GreenEVT
fi
git -C external/GreenEVT fetch --all --tags --prune
git -C external/GreenEVT checkout --detach "$GREENEVT_COMMIT"
test "$(git -C external/GreenEVT rev-parse HEAD)" = "$GREENEVT_COMMIT"

if command -v git-lfs >/dev/null 2>&1 || git lfs version >/dev/null 2>&1; then
  git -C external/GreenEVT lfs install --local || true
fi

echo "==> Materialize exact GreenEVT LFS objects"
if ! git -C external/GreenEVT lfs pull   --include='data/UDS.db,data/sumo_network/greensboro.net.xml'   --exclude=''; then
  echo "ERROR: Git-LFS materialization failed." >&2
  echo "Use the upstream fallback archive only after independently verifying the exact frozen SHA-256 values." >&2
  exit 13
fi

test "$(sha256sum external/GreenEVT/data/UDS.db | awk '{print $1}')" = "$UDS_SHA256"
test "$(stat -c '%s' external/GreenEVT/data/UDS.db)" = "$UDS_SIZE"
test "$(sha256sum external/GreenEVT/data/sumo_network/greensboro.net.xml | awk '{print $1}')" = "$SUMO_NET_SHA256"
test "$(stat -c '%s' external/GreenEVT/data/sumo_network/greensboro.net.xml)" = "$SUMO_NET_SIZE"

echo "==> Build frozen runtime"
set +e
docker build   --file project/stage3/runtime/Dockerfile.greenevt-v1   --tag "$IMAGE"   . 2>&1 | tee "$ART/docker_build.log"
BUILD_RC=${PIPESTATUS[0]}
set -e
if [[ "$BUILD_RC" -ne 0 ]]; then
  echo "BLOCKED_RUNTIME_COMPATIBILITY: Docker image build failed." >&2
  exit "$BUILD_RC"
fi

docker image inspect "$IMAGE" > "$ART/docker_image_inspect.json"
docker image inspect --format='{{.Id}}' "$IMAGE" > "$ART/docker_image_id.txt"

runq() {
  docker run --rm     -v "$PWD:/workspace"     -w /workspace     "$IMAGE" "$@"
}

run_gate() {
  local name="$1"
  shift
  echo "==> $name"
  set +e
  "$@"
  local rc=$?
  set -e
  printf "%s\t%s\n" "$name" "$rc" >> "$ART/gate_exit_codes.tsv"
  return 0
}

: > "$ART/gate_exit_codes.tsv"

run_gate G_ENV   runq python models/H1/level2/runtime/verify_environment.py     --thesis-root .     --greenevt external/GreenEVT     --out "$ART/environment.json"

run_gate G_DATA   runq python models/H1/level2/runtime/verify_source_bytes.py     --greenevt external/GreenEVT     --out "$ART/source_bytes.json"

run_gate G_DSS   runq python models/H1/level2/runtime/verify_opendss_baseline.py     --greenevt external/GreenEVT     --out "$ART/opendss_baseline.json"

run_gate G_SUMO   runq python models/H1/level2/runtime/verify_sumo_baseline.py     --greenevt external/GreenEVT     --out "$ART/sumo_baseline.json"

run_gate G_Q05_RUN1   runq python models/H1/level2/runtime/verify_q05_coupling.py     --greenevt external/GreenEVT     --out "$ART/q05_run1.json"

run_gate G_Q05_RUN2   runq python models/H1/level2/runtime/verify_q05_coupling.py     --greenevt external/GreenEVT     --out "$ART/q05_run2.json"

run_gate G_REPRO   runq python models/H1/level2/runtime/compare_replicates.py     "$ART/q05_run1.json"     "$ART/q05_run2.json"     --out "$ART/reproducibility.json"     --tol 1e-12

echo "==> Capture environment manifests"
docker run --rm "$IMAGE" python -m pip freeze > "$ART/pip_freeze.txt"
docker run --rm "$IMAGE" sh -lc "dpkg-query -W | sort" > "$ART/dpkg_manifest.tsv"
sha256sum "$ART"/* | sort > "$ART/artifact_sha256_pre_gate.txt"

run_gate G_PROV   runq python models/H1/level2/runtime/verify_provenance.py     --artifacts "$ART"     --environment "$ART/environment.json"     --out "$ART/provenance.json"

echo "==> Aggregate authoritative runtime gate"
set +e
runq python models/H1/level2/runtime/aggregate_runtime_gate.py   --environment "$ART/environment.json"   --data "$ART/source_bytes.json"   --dss "$ART/opendss_baseline.json"   --sumo "$ART/sumo_baseline.json"   --q05 "$ART/q05_run1.json"   --repro "$ART/reproducibility.json"   --provenance "$ART/provenance.json"   --out "$ART/runtime_gate.json"
AGG_RC=$?
set -e

sha256sum "$ART"/* | sort > "$ART/artifact_sha256.txt"

echo
echo "Evidence: $ROOT/$ART"
echo "Aggregate exit code: $AGG_RC"
if [[ -f "$ART/runtime_gate.json" ]]; then
  cat "$ART/runtime_gate.json"
fi

exit "$AGG_RC"
