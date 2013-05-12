#!/bin/bash
[ -x docs ] || mkdir docs
[ -x docs/source ] || mkdir docs/source
[ -x docs/html ] || mkdir docs/html
cd ..
python -c 'import sys; sys.path.append("/var/lib/jenkins/home/jobs/libuseful")'
python -c 'import sys; print(sys.path)'
sphinx-apidoc -F -f -H libuseful -A "Fox Wilson, Joshua Cotton" -o docs/source workspace
sphinx-build -b html workspace/docs/source workspace/docs/html
