#!/bin/bash

installed_dir=$(dirname $(readlink -f $(basename `pwd`)))

sudo pacman -S --noconfirm --needed openvpn

cd /etc/openvpn

sudo wget https://my.surfshark.com/vpn/api/v1/server/configurations

sudo unzip configurations

sudo cp $installed_dir/Personal/home/oh/sysctl.conf /etc/sysctl.conf

sudo sysctl -p
