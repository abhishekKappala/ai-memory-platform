#!/bin/sh
set -e

echo "=== RUNNING ALEMBIC ==="

alembic upgrade head

echo "=== ALEMBIC SUCCESS ==="

uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}