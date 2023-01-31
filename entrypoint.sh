#!/bin/sh

set -e

echo "${0}: Waiting for Postgres DB..."
./wait-for-it.sh postgres:5432

echo "${0}: Running script ..."
python -u /src/main_pool.py  # or main_pool.py

exec "$@"
