#!/bin/bash
set -e 

SCRIPT_DIR=$(dirname $(realpath $0))
pushd ${SCRIPT_DIR}/../
    find . -name "*.py" | xargs pylint
popd