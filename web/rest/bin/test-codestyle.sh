#!/bin/bash
set -e

SCRIPT_DIR=$(dirname $(realpath $0))
pushd ${SCRIPT_DIR}/../
    black .

    if [[ -n $(git status --porcelain) ]]; then
        echo "There are changes in the repository after running black."
        git status --porcelain
        exit 1
    else
        echo "No changes detected."
        exit 0
    fi
popd