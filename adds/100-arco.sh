#!/bin/bash
#
installed_dir=$(dirname $(readlink -f $(basename `pwd`)))

echo "|» ArcoLinux Software to install"

if grep -q arcolinux_repo /etc/pacman.conf; then

  echo "|» ArcoLinux repos are already in /etc/pacman.conf "
  else
  echo "|» Getting the keys and mirrors for ArcoLinux"
  sh arco/get-the-keys-and-repos.sh
  sudo pacman -Sy
fi

sudo pacman -S --noconfirm --needed archlinux-logout-git
sudo pacman -S --noconfirm --needed cpuid

tput setaf 6
echo "|» Done"
tput sgr0
