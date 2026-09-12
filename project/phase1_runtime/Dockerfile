ARG BASE_IMAGE=python:3.11.16-slim-bookworm
FROM ${BASE_IMAGE}

ENV PYTHONHASHSEED=0 \
    OMP_NUM_THREADS=1 \
    OPENBLAS_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 \
    NUMEXPR_NUM_THREADS=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY project/requirements-phase1-v1.lock.txt /tmp/requirements-phase1-v1.lock.txt
RUN python -m pip install --no-cache-dir --require-hashes \
    -r /tmp/requirements-phase1-v1.lock.txt

COPY phase1_exec /workspace/phase1_exec
COPY tests/phase1 /workspace/tests/phase1

CMD ["pytest", "-q", "tests/phase1"]
