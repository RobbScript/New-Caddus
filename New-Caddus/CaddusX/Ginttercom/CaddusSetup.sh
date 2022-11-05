#!/bin/bash
cd ~
echo 'Em qual plataforma você está?'
echo '1- Red Hat/Fedora'
echo '2- Debian/Ubuntu/Mint'
echo '3- Manjaro/Arch'
echo '4- Void linux'
echo '5- Termux (Android)'
read plata;
if [ $plata -eq 1 ];
then
   sudo dnf update
   sudo dnf install python
   sudo dnf install python-pip
elif [ $plata -eq 2 ];
then
   sudo apt-get update
   sudo apt-get install python
   sudo apt-get install python-pip
elif [ $plata -eq 3 ];
then
   sudo pacman -Syu
   sudo pacman -S python
   sudo pacman -S python-pip
elif [ $plata -eq 4 ];
then
   sudo xbps-install -Su
   sudo xbps-install python
   sudo xbps-install python-pip
elif [ $plata -eq 5 ];
then
   pkg update
   pkg install python
   pkg install python-pip
else
   echo 'não temos suporte. :('
fi
pip install art
pip install termcolor
