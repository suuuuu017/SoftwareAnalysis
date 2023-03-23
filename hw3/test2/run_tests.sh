#!/bin/bash

while IFS=',' read -ra array; do
  test+=("${array[0]}")
  result+=("${array[1]}")
done < tests.csv

mkdir pdir
mkdir fdir
gcc -Wall -fprofile-arcs -ftest-coverage -o tcas$1 tcas$1.c

for i in `seq 1 ${#test[@]}`
do
    if ./tcas$1  ${test[$i-1]} | grep -q "${result[$i-1]/ /}"; then
        gcov tcas$1.c
        mv tcas$1.c.gcov tcas$1.c.gcov.$i
        mv tcas$1.c.gcov.$i ./pdir
        echo $i:P
        :
    else
        gcov tcas$1.c
        mv tcas$1.c.gcov tcas$1.c.gcov.$i
        mv tcas$1.c.gcov.$i ./fdir
        echo $i:F
        #echo $i:F   ---  `./tcas  ${test[$i-1]}` --- ${result[$i-1]} ----------- ${test[$i-1]}
    fi
    rm tcas$1.gcda


done
