#!/bin/bash
git checkout main
git add . 
git commit -m"$*"
git push $GIT_URL
BRANCH=$(git branch --show-current)
echo $'\n\n\n\n'Succesfully commited changes to branch $BRANCH with message:$'\n' "$@"