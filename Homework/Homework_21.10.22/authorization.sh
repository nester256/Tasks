#!/bin/bash
# Это скрипт авторизации 
function authorization() {
    auth=1
    user_data=0
    echo "Введите ваш логин:"
    read login
    while read line
    do 
        user_data=($line)
        if [[ ${user_data[0]} == $login ]]
        then
            for ((i=0;i<4;i++))
            do
                if [[ $i == 3 ]]
                then
                    echo Улыбнись, $USER!
                    path=/home/$USER/its_you.jpg
                    fswebcam -r 1280x720 -D -S $path
                    exit
                fi
                echo "Введите ваш пароль:"
                read -s -t 25 pass <&1
                input=$(echo -n $pass | sha512sum)
                pass=($input)
                password="${pass[0]}"
                if [[ $password == ${user_data[1]} ]]        
                then
                    echo "Авторизация успешна"
                    exit
                else
                    echo Не верный пароль. Осталось попыток $((3-($i+1)))
                fi
            done 
        else
            auth=0
        fi
    done < users_data.txt
    if [[ $auth == 0 ]]
    then
        echo "Такого логина не существует!"
        exit
    fi
}

authorization