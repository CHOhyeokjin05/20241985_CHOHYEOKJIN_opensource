#!/bin/sh

name=${1}
info=${2}

# DB.txt에 이름과 정보를 추가 (파일이 없으면 자동 생성)
echo "$name $info" >> DB.txt
