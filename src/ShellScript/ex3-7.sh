#!/bin/sh

folder_name=${1}

# 작업할 폴더가 없으면 생성
if [ ! -d "${folder_name}" ]; then
  mkdir "${folder_name}"
fi

# 5개의 파일 생성 및 하위 폴더에 링크
for i in 0 1 2 3 4; do
  touch "$folder_name/file$i.txt"
  mkdir -p "$folder_name/file$i"
  ln -s "$folder_name/file$i.txt" "$folder_name/file$i/file$i.txt"
done