#!/bin/bash

tput setaf 6
echo "|» Install Qogir GTK Theme"
tput sgr0

yay -S --noconfirm --needed qogir-gtk-theme

tput setaf 6
echo "|» Install Kvantum Theme Qogir Git"
tput sgr0

yay -S --noconfirm --needed kvantum-theme-qogir-git

tput setaf 6
echo "|» Install Nordzy Icon Theme"
tput sgr0

yay -S --noconfirm --needed nordzy-icon-theme-git

tput setaf 6
echo "|» Install Vimix Cursors"
tput sgr0

yay -S --noconfirm --needed vimix-cursors

tput setaf 6
echo "|» Install Kali Themes"
tput sgr0

yay -S --noconfirm --needed kali-themes

tput setaf 6
echo "|» Done"
tput sgr0
