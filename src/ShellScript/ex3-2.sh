#!/bin/sh

num1=${1}

operator=${2}

num2=${3}

# Perform the calculation based on the operator
if [ "$operator" = "+" ]; then
    result=`expr $num1 + $num2`
elif [ "$operator" = "-" ]; then
    result=`expr $num1 - $num2`
else
    echo "Invalid operator. Please use + or -."
    exit 1
fi

# Output the result
echo "$result"

