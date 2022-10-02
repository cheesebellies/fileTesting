#!/bin/bash
git checkout main
git add $1
git commit -m"add file"
git push $GIT_URL