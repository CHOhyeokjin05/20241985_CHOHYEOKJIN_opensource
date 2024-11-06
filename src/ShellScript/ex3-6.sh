#!/bin/sh

folder_name=${1}

# 작업할 폴더가 없으면 생성
if [ ! -d "${folder_name}" ]; then
  mkdir "${folder_name}"
fi

# 5개의 파일 생성
for i in 1 2 3 4 5; do
  touch "${folder_name}/file$i.txt"
done

# 현재 폴더에서 압축 파일 생성
tar -cvf "${folder_name}.tar" "$folder_name"

# files 폴더 생성 (압축 해제용 폴더)
if [ ! -d "$folder_name" ]; then
  mkdir "$folder_name"
fi

# files 폴더에 압축 해제
tar -xvf "${folder_name}.tar" -C "files"
