#!/bin/sh

list_files() {
  echo "함수 안으로 들어왔음"
  ls $1
}

echo "프로그램을 시작합니다."
option=${1}
list_files "$option"
echo "프로그램을 종료합니다."