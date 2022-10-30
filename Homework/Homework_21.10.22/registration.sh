#!/bin/bash
# Это скрипт регистрации
function registration () {
    login_flag=true
    echo "Добро пожаловать, введите желаемый логин: "
    read login 
    for line in $(cat users_data.txt)
    do 
        if [[ $line == *$login* ]]
        then
            login_flag=false
        fi
    done
    if [[ $login_flag == false ]]
    then
        echo "К сожалению, введёный логин уже занят."
    else
        echo "Введите желаемый пароль:"
        read -s password
        password_save=$(echo -n $password | sha512sum)
        echo $login $password_save >> users_data.txt
        echo "Вы успешно зарегистрировались!"
    fi
}

registration