#!/bin/bash
[ -x docs ] || mkdir docs
[ -x docs/html ] || mkdir docs/html
[ -x docs/pdf ] || mkdir docs/pdf
epydoc --html . -o docs/html -n libuseful 
epydoc --pdf . -o docs/pdf -n libuseful

