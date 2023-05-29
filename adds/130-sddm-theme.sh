#!/bin/bash

installed_dir=$(dirname $(readlink -f $(basename `pwd`)))

if grep -q "archlinux" /etc/os-release; then

	echo "Copying sddm files"
	sudo pacman -S --noconfirm --needed arcolinux-sddm-simplicity-git
	sudo cp -f $installed_dir/files/sddm.conf /etc/sddm.conf

	[ -d /etc/sddm.conf.d ] || sudo mkdir /etc/sddm.conf.d
	sudo cp -f $installed_dir/files/kde_settings.conf /etc/sddm.conf.d/kde_settings.conf
	FIND="Current=breeze"
	REPLACE="Current=arcolinux-simplicity"
	sudo sed -i "s/$FIND/$REPLACE/g" /etc/sddm.conf

	sudo cp -f $installed_dir/files/background.jpg /usr/share/sddm/themes/arcolinux-simplicity/images/background.jpg

	echo
	tput setaf 6
	echo "|» Done"
	tput sgr0
	echo

fi

