#!/bin/sh

set -e # give an error if any command finishes with a non-zero exit code
set -u # give an error if we reference unset variables
set -o pipefail # for a pipeline, if any of the commands fail with a non-zero exit code, fail the entire pipeline with that exit code


mkdir simpmsg
cp simpmsg.py simpmsg/__init__.py

python setup.py sdist bdist_wheel
