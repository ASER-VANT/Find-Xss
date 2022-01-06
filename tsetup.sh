#!/bin/bash

# Author : ASER

clear

apt update

pkg update

pkg upgrade

apt upgrade

pkg install unstable-repo -y

pkg install x11-repo -y

pkg install root-repo -y

apt install game-repo -y

apt purge game-repo -y

apt install python -y

apt install python3 -y

apt install figlet -y

apt install python-pip -y

pip install colorama

pip install requests

clear

printf "\e[1;77m\e[41m     Run 'python3 findxss.py'!!     \e[0m\n"