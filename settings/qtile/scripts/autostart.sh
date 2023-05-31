#!/bin/bash
#
image=$(find ~/Pictures/Backgrounds -type f -print0 | shuf -zn 1)
#
picom --config $HOME/.config/qtile/scripts/picom.conf &
#xrandr -s 1920x1080
#xrandr --output Virtual-1 --primary --mode 2560x1440 --rate 60.00 &
#xrandr --output LVDS1 --mode 1366x768 --rate 60.00 &
#xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#xrandr --output DP2 --primary --mode 1920x1080 --rate 60.00 --output LVDS1 --off &
#xrandr --output LVDS1 --mode 1366x768 --output DP3 --mode 1920x1080 --right-of LVDS1
#xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
#
#xrandr --output HDMI-1 --primary --mode 2560x1440 --rate 74.97 --output eDP-1 --mode 2560x1440 --rate 165.00 --gamma 0.9 --brightness 0.6
#xrandr --output DP-4 --gamma 0.9 --brightness 0.6
#
#Set your wallpaper
feh --bg-fill $image &
#
volumeicon &
sxhkd &
emacs --daemon &
solaar --window hide --battery-icons regular &
nm-applet &
xfce4-power-manager &
numlockx on &
blueberry-tray &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
thunderbird
