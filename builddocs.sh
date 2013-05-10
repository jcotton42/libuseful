#!/bin/bash
mkdir docs
mkdir docs/html
mkdir docs/pdf
epydoc --html . -o docs/html -n libuseful 
epydoc --pdf . -o docs/pdf -n libuseful

