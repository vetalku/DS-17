#!/bin/sh

echo $0 $1
git add .
git commit -m " $1 "
git push origin 