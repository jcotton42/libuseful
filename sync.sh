#!/bin/bash
shopt -u dotglob

find -type f -exec chmod 664 '{}' +
find -type d -exec chmod 775 '{}' +
for ext in sh bash
{
    find -type f -name '*.'$ext -exec chmod 775 '{}' +
}
git add *
git add .gitignore
git commit
git push
git pull
