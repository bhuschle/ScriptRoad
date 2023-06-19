#!/bin/bash

blocks() {
    echo -e "\n\e[0;30m${1}\e[0m\e[0;31m${1}\e[0m\e[0;32m${1}\e[0m\e[0;33m${1}\e[0m\e[0;34m${1}\e[0m\e[0;35m${1}\e[0m\e[0;36m${1}\e[0m\e[0;37m${1}\e[0m"
    echo -e " \e[1;30m${2}\e[0m\e[1;31m${2}\e[0m\e[1;32m${2}\e[0m\e[1;33m${2}\e[0m\e[1;34m${2}\e[0m\e[1;35m${2}\e[0m\e[1;36m${2}\e[0m\e[1;37m${2}\e[0m\n"
}

if [ "$1" -ge 1 ] && [ "$1" -le 20 ]; then
    case "$1" in
        1)
            iu="░▒▒▓"
            il="░▒▒▓"
            blocks "$iu" "$il"
            ;;
        2)
            iu="┌■┐ "
            il=" └■┘"
            blocks "$iu" "$il"
            ;;
        3)
            iu="GSB "
            il="GSB "
            blocks "$iu" "$il"
            ;;
        4)
            iu="┬┴┬┴"
            il="┴┬┴┬"
            blocks "$iu" "$il"
            ;;
        5)
            iu="─┬──"
            il="┴───"
            blocks "$iu" "$il"
            ;;
        6)
            iu="╭╮╭╮"
            il="╰╯╰╯"
            blocks "$iu" "$il"
            ;;
        7)
            iu="◡◠◡◠"
            il="◠◡◠◡"
            blocks "$iu" "$il"
            ;;
        8)
            iu="△▽△▽"
            il="▽△▽△"
            blocks "$iu" "$il"
            ;;
        9)
            iu="╔╗╔╗"
            il="╚╝╚╝"
            blocks "$iu" "$il"
            ;;
        10)
            iu="█ █ "
            il="█ █ "
            blocks "$iu" "$il"
            ;;
        11)
            iu="  "
            il="  "
            blocks "$iu" "$il"
            ;;
        12)
            iu="󱗼󰇙󱗼󰇙"
            il="󱗼󰇙󱗼󰇙"
            blocks "$iu" "$il"
            ;;
        13)
            iu="󰨓󰝣󰨓󱡔"
            il="󰨓󰝣󰨓󱡔"
            blocks "$iu" "$il"
            ;;
        14)
            iu=" ╭─╮"
            il="╰─╯ "
            blocks "$iu" "$il"
            ;;
    esac
else
    echo -e "\n\e[0;30mYou \e[0m\e[0;31mMust \e[0m\e[0;32mEnter \e[0m\e[0;33mAn \e[0m\e[0;34mArgument \e[0m\e[0;35mTo \e[0m\e[0;36mThe \e[0m\e[0;37mCall \e[0m\n"
fi
