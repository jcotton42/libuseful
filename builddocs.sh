#!/bin/bash
rm -r docs
[ -x docs ] || mkdir docs
[ -x docs/source ] || mkdir docs/source
cd ..
PYTHONPATH="${PYTHONPATH}:/var/lib/jenkins/home/jobs/libuseful/"
export PYTHONPATH
python -c 'import sys; print(sys.path)'
sphinx-apidoc -F -f -H libuseful -A "Fox Wilson, Joshua Cotton" -o workspace/docs/source workspace
sphinx-build -b html workspace/docs/source workspace/docs/
[ -x workspace/lint ] || mkdir workspace/lint
pylint -f html workspace > workspace/lint/index.html
