#!/bin/bash
set -e

export FLASK_APP=__init__.py

SCRIPT_DIR=$(dirname $(realpath $0))
pushd ${SCRIPT_DIR}/../
if [ -z "$1" ]; then
    echo "Error: No argument provided."
    echo "Usage: $0 --upgrade | --downgrade"
    exit 1
fi

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --upgrade)
            flask db upgrade
            exit 0
            ;;
        --downgrade)
            flask db downgrade
            exit 0
            ;;
        *)
            echo "No valid arguments"
            exit 0
            ;;
    esac
done
popd