#!/bin/bash
rm -r docs
[ -x docs ] || mkdir docs
[ -x docs/source ] || mkdir docs/source
cd ..
PYTHONPATH="${PYTHONPATH}:/var/lib/jenkins/home/jobs/libuseful/"
export PYTHONPATH
python -c 'import sys; print(sys.path)'
sphinx-apidoc -F -f -H libuseful -o workspace/docs/source workspace
echo Copying docconf
cp workspace/docconf.py workspace/docs/source/conf.py
echo Done
sphinx-build -b html workspace/docs/source workspace/docs/
