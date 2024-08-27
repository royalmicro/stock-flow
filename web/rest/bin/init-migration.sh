#!/bin/bash
set -e
export FLASK_APP=__init__.py  # Or the entry point of your Flask app

SCRIPT_DIR=$(dirname $(realpath $0))
pushd ${SCRIPT_DIR}/../
flask db init
popd