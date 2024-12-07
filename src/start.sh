#!/bin/sh

SCRIPT_DIR=$(dirname "$0")
getopts upgrade head
python "${SCRIPT_DIR}/main.py"
