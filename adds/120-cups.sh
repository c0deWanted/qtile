#!/bin/bash
#
tput setaf 6
echo "|» cups"
tput sgr0

sudo pacman -S --noconfirm --needed cups
sudo pacman -S --noconfirm --needed cups-pdf
sudo pacman -S --noconfirm --needed ghostscript
sudo pacman -S --noconfirm --needed gsfonts
sudo pacman -S --noconfirm --needed gutenprint
sudo pacman -S --noconfirm --needed gtk3-print-backends
sudo pacman -S --noconfirm --needed libcups
sudo pacman -S --noconfirm --needed system-config-printer
sudo pacman -S --noconfirm --needed sane
sudo pacman -S --noconfirm --needed simple-scan

sudo systemctl enable --now cups.service

yay -S --noconfirm --needed cnijfilter-mg4200

tput setaf 6
echo "|» Done"
tput sgr0
