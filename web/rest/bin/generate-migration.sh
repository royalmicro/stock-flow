#!/bin/bash
set -e

export FLASK_APP=__init__.py

SCRIPT_DIR=$(dirname $(realpath $0))
pushd ${SCRIPT_DIR}/../
if [ "$#" -gt 0 ]; then
    flask db migrate -m $1
else
    flask db migrate
fi
popd