#!/bin/bash
exec 2> log_error_registration
database=./database.txt

compliance_flag=0
echo -n "Введите логин: "
read login
if [ -z $login ]
    then
    compliance_flag=1
fi
if [ -f $database ] && [ $compliance_flag == 0]
then
    while read line
        do
        if [[ $login == $line ]]
            then
            compliance_flag=1
        fi
    done < database
fi

if [[ $compliance_flag == 1 ]]
    then
    echo "Вы ничего не ввели, либо данный логин занят другим пользователем"
elif [[ $compliance_flag == 0 ]]
    then
    echo -n "Введите пароль:"
    read -s password
    
    if [ -z $pass ]
            then
            echo "Пароль не валидный"
            break
    fi
    pass=$(echo -n $password | sha512sum)
    echo $login $pass >> $database
    echo "Вы зарегистрировались"
fi