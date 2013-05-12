#!/bin/bash
[ -x docs ] || mkdir docs
[ -x docs/source ] || mkdir docs/source
[ -x docs/html ] || mkdir docs/html
cd ..
sphinx-apidoc -F -f -H libuseful -A "Fox Wilson, Joshua Cotton" -o docs/source 
sphinx-build -b html docs/source docs/html
