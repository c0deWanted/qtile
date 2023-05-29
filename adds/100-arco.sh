#!/bin/bash
#
CNT="[\e[1;36mNOTE\e[0m]"
COK="[\e[1;32mOK\e[0m]"
CER="[\e[1;31mERROR\e[0m]"
INSTLOG="arco.log"

installed_dir=$(dirname $(readlink -f $(basename `pwd`)))

# Backup pacman.conf
echo -e "$CNT - Backup pacman.conf -> /etc/pacman.conf.bup"
sudo cp /etc/pacman.conf /etc/pacman.conf.bup
sleep 2

# Install arco repos
if grep -q arcolinux_repo /etc/pacman.conf; then
  echo -e "$COK - ArcoLinux repos are already in /etc/pacman.conf"
  sleep 1
  else
  echo -e "$CNT Getting the keys and mirrors for ArcoLinux"
  sh arco/get-the-keys-and-repos.sh &>> $INSTLOG
  sudo pacman -Sy &>> $INSTLOG
fi

# Install logout tool from arco repos
echo -e "$CNT - Now installing archlinux-logout-git ..."
sudo pacman -S --noconfirm --needed archlinux-logout-git &>> $INSTLOG
if yay -Q $1 &>> /dev/null ; then
  echo -e "\e[1A\e[K$COK - installed."
else
# if this is hit then a package is missing, exit to review log
  echo -e "\e[1A\e[K$CER - install had failed, please check the install.log"
  exit
fi

# Install sddm theme
echo -e "$CNT - Now installing sddm theme ..."
sudo pacman -S --noconfirm --needed arcolinux-sddm-simplicity-git &>> $INSTLOG
sudo cp -f $installed_dir/files/sddm.conf /etc/sddm.conf
[ -d /etc/sddm.conf.d ] || sudo mkdir /etc/sddm.conf.d
sudo cp -f $installed_dir/files/kde_settings.conf /etc/sddm.conf.d/kde_settings.conf
FIND="Current=breeze"
REPLACE="Current=arcolinux-simplicity"
sudo sed -i "s/$FIND/$REPLACE/g" /etc/sddm.conf
sudo cp -f $installed_dir/files/background.jpg /usr/share/sddm/themes/arcolinux-simplicity/images/background.jpg
sleep 2

# Backup arco repos and reset to original
echo -e "$CNT - Undo arco. Save arco as pacman.conf.arco"
sudo cp /etc/pacman.conf /etc/pacman.conf.arco
sudo mv /etc/pacman.conf.bup /etc/pacman.conf
sleep 2
echo -e "$COK"
