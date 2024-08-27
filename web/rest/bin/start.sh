#!/bin/bash
set -e

export FLASK_APP=__init__.py  # Or the entry point of your Flask app
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
export PYTHONPATH=$(pwd)

SCRIPT_DIR=$(dirname $(realpath $0))

breakpoints=false

run_with_breakpoints() {
    python3.12 -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m flask run --host=0.0.0.0
}

run_debug(){
    flask run --host=0.0.0.0 --debug
}

pushd ${SCRIPT_DIR}/../
# Parse command line arguments
if [ $# -eq 0 ]; then
    run_debug
    exit 0
fi

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --breakpoints)
            run_with_breakpoints
            exit 0
            ;;
        *)
            echo "No valid arguments"
            exit 0
            ;;
    esac
done
popd