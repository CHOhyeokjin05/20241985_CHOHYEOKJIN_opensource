#!/bin/sh

weight=${1}
height=${2}

# BMI 계산 (몸무게 / (신장 * 신장))
bmi=$(echo "scale=2; $weight * 10000 / ($height * $height)" | bc)

# BMI에 따른 비만 여부 판단
if [ $(echo "$bmi >= 18.5" | bc) -eq 1 ] && [ $(echo "$bmi < 23" | bc) -eq 1 ]; then
    result="정상체중입니다."
elif [ $(echo "$bmi < 18.5" | bc) -eq 1 ]; then
    result="저체중입니다."
else
    result="과체중입니다."
fi

# 결과 출력
echo "$result"
