#!/bin/bash
shopt -u dotglob

for ext in py txt html md sh bash
{
    files="$(find -iname '*.'$ext)"
    for file in "$files"
    {
        dos2unix "$file"
        expand -t 4 "$file" > "$file"
    }
}

git add *
git add .gitignore
git commit
git push
git pull
