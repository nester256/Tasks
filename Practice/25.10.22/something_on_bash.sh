#!/bin/bash
function progress() {
    n=$1
    step=$2
    first_num=$3
    sum=0
    for ((i=0;i<$n;i++)) {
        sum=$(($sum + ($first_num + $i * $step)))
    }
    echo $sum
}

#progress 1 3 4

function find_word() {
    count=1
    flag=0
    for line in $(cat $1)
    do
        if [[ $line == *$2* ]]
        then
            echo "$count"
            flag=1 
        fi
        count=$(($count+1))
    done
    if [[ $flag -eq 0 ]]
    then
        echo -1
    fi
}

find_word test Витя