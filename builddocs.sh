#!/bin/bash
[ -x docs ] || mkdir docs
[ -x docs/source ] || mkdir docs/source
[ -x docs/html ] || mkdir docs/html
cd ..
sphinx-apidoc -F -f -H libuseful -A "Fox Wilson, Joshua Cotton" -o docs/source workspace
sphinx-build -b html workspace/docs/source workspace/docs/html
