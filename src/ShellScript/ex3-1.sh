#!/bin/sh

num=${1:-11}

i=0
while [ $i -lt $num ]
do
  echo "hello world"
  i=$((i + 1))
done
