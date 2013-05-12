#!/bin/bash
[ -x docs ] || mkdir docs
[ -x docs/source] || mkdir docs/source
[ -x docs/html ] || mkdir docs/html
sphinx-apidoc -F -f -o docs/source .
sphinx-build -b html docs/source docs/html
