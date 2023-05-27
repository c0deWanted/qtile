#!/bin/bash
#set -e
##################################################################################################################

installed_dir=$(dirname $(readlink -f $(basename `pwd`)))

##################################################################################################################

func_install() {
    if pacman -Qi $1 &> /dev/null; then
        tput setaf 6
        echo "|» The package "$1" is already installed"
        echo
        tput sgr0
    else
        tput setaf 6
        echo "|» Installing package "  $1
        echo
        tput sgr0
        sudo pacman -S --noconfirm --needed $1
    fi
}


sudo pacman -Syy

echo
tput setaf 6
echo "|» Core software"
tput sgr0
echo


list=(
adobe-source-sans-fonts
aic94xx-firmware

alacritty-themes
arandr
arc-gtk-theme
archiso
asciinema


base16-alacritty-git


brave-bin
celluloid
cmake
cpuid
cpupower
curl
dconf-editor
deadbeef
deluge-gtk

downgrade
evince
expac

faad2
fd

ffmpegthumbnailer
file-roller



font-manager
gimp
git
#gitahead-bin
#gitfiend
gnome-calculator
gnome-disk-utility
gparted
grub-customizer
gtop
gvfs-smb
hardcode-fixer-git
hardinfo-gtk3
hddtemp

hw-probe
#intellij-idea-community-edition
inxi
kvantum

libreoffice-fresh

linux-firmware-qlogic



mlocate
meld
midori
most
mousepad
mpv
neofetch
networkmanager
network-manager-applet
networkmanager-openvpn
nm-connection-editor
nomacs

ntp
nss-mdns
numlockx
oh-my-zsh-git
openresolv

paru-bin

peek
playerctl

polybar

python-pywal
pv
#qutebrowser
rate-mirrors-bin
remmina



arcolinux-rofi-themes-git
scrot
sardi-icons
#shell-color-scripts

simplescreenrecorder
solaar
sparklines-git
speedtest-cli-git
squashfs-tools
system-config-printer
the_platinum_searcher-bin
the_silver_searcher
thunar
thunar-archive-plugin
thunar-media-tags-plugin


ttf-bitstream-vera
ttf-dejavu
ttf-droid
ttf-fira-sans
#ttf-hack
ttf-inconsolata

#ttf-liberation

#ttf-roboto
#ttf-roboto-mono
#ttf-ubuntu-font-family
tumbler


xcolor
xdg-user-dirs


yay-bin
zsh
zsh-completions
zsh-syntax-highlighting
rxvt-unicode
urxvt-fullscreen
urxvt-perls
urxvt-resize-font-git






)

count=0

for name in "${list[@]}" ; do
    count=$[count+1]
    tput setaf 6;echo "|» Installing package nr.  "$count " " $name;tput sgr0;
    func_install $name
done

sudo systemctl enable avahi-daemon.service
sudo systemctl enable ntpd.service
sudo systemctl enable cpupower.service
sudo systemctl enable sddm.service
sudo systemctl enable NetworkManager.service


echo
tput setaf 6
echo "|» Install the driver for Canon MG4200 series printer"
tput sgr0
yay -S --noconfirm --needed cnijfilter-mg4200

if [ ! -f /usr/bin/duf ]; then
  sudo pacman -S --noconfirm --needed duf
fi
if [ ! -f /usr/share/xsessions/plasma.desktop ]; then
  sudo pacman -S --noconfirm --needed qt5ct
fi

sudo pacman -S --noconfirm --needed jdk17-openjdk
sudo pacman -S --noconfirm --needed jdk8-openjdk

if grep -q "archlinux" /etc/os-release; then
  echo
  tput setaf 6
  echo "|» Set Java 17 as default"
  tput sgr0
  sudo archlinux-java set java-17-openjdk
fi


if grep -q "Arch Linux" /etc/os-release; then

  echo
  tput setaf 3
  echo "|» Getting latest /etc/nsswitch.conf from ArcoLinux"
  tput sgr0
  echo

  sudo cp /etc/nsswitch.conf /etc/nsswitch.conf.bak
  sudo wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/nsswitch.conf -O $workdir/etc/nsswitch.conf

fi
echo
tput setaf 6
echo "|» Done"
tput sgr0
echo
