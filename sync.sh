#!/bin/bash
shopt -u dotglob

for ext in py txt html md sh bash
{
    find -iname '*.'$ext -print0 | xargs -0 dos2unix
    find -iname '*.'$ext -print0 | xargs -0 -I'{}' expand -t 4 '{}' > '{}'
}

git add *
git add .gitignore
git commit
git push
git pull
