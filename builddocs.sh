#!/bin/bash
mkdir docs
mkdir docs/html
mkdir docs/pdf
epydoc --html . -o docs/html
epydoc --pdf . -o docs/pdf

