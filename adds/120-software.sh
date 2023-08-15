#!/bin/bash

# set some colors
CNT="[\e[1;36mNOTE\e[0m]"
COK="[\e[1;32mOK\e[0m]"
CER="[\e[1;31mERROR\e[0m]"
INSTLOG="software.log"

installed_dir=$(dirname $(readlink -f $(basename `pwd`)))
count=0

# function that will test for a package and if not found it will attempt to install it
func_install() {
    # First lets see if the package is there
    if yay -Q $1 &>> /dev/null ; then
        echo -e "$COK - $count. $1 is already installed."
    else
        # no package found so installing
        echo -e "$CNT - $count. Now installing $1 ..."
        yay -S --noconfirm $1 &>> $INSTLOG
        # test to make sure package installed
        if yay -Q $1 &>> /dev/null ; then
            echo -e "\e[1A\e[K$COK - $count. $1 was installed."
        else
            # if this is hit then a package is missing, exit to review log
            echo -e "\e[1A\e[K$CER - $count. $1 install had failed, please check the install.log"
            exit
        fi
    fi
}

sudo pacman -Syy &>> $INSTLOG

list=(
adobe-source-sans-fonts
baobab
brave-bin
celluloid
cmake
cpuid
cpupower
deadbeef
deluge-gtk
duf
evince
file-roller
font-manager
gdu
geeqie
gimp
gnome-calculator
gvfs-smb
hardinfo-git
hblock
hw-probe
iftop
inxi
libreoffice-fresh
mlocate
meld
mousepad
mpv
networkmanager-openvpn
#nomacs
ntp
numlockx
obsidian
#onlyoffice-bin
openresolv
peek
python-pywal
pv
solaar
speedtest-cli
system-config-printer
tldr
vnstat
xcolor
)

for name in "${list[@]}" ; do
    count=$[count+1]
    func_install $name
done

echo -e "$CNT - Enabling services ..."
sudo hblock &>> $INSTLOG
sudo systemctl enable --now ntpd.service &>> $INSTLOG
sudo systemctl enable --now cpupower.service &>> $INSTLOG
sudo systemctl enable --now vnstat.service &>> $INSTLOG
echo -e "$COK"
