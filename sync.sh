#!/bin/bash
shopt -u dotglob

git add *
git add .gitignore
git commit
git push
git pull
