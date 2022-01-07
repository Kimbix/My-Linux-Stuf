#!/usr/bin/env bash

## HELLO this is my launch script have fun

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use 
# polybar-msg cmd quit

## For spotifyc
cd /home/humberto/Documents/System/spotifyc && export PATH="$PATH:$PWD"
cd /home/humberto

# Launches bars for both of my monitors
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar top 2>&1 | tee -a /tmp/polybar1.log & disown
polybar top_second 2>&1 | tee -a /tmp/polybar2.log & disown


## Launch the keyboard layout changer
setxkbmap -layout us,es
setxkbmap -option 'grp:alt_space_toggle'

## Syncs the configuration files with the git repo
CONF='/home/humberto/.config'
REPO='/home/humberto/Documents/Repos/My-Linux-Stuf'
rsync $CONF/polybar/config $REPO/polybar/config
rsync $CONF/polybar/launch.sh $REPO/polybar/launch.sh

rsync $CONF/i3/config $REPO/i3/config

rsync $CONF/rofi/config.rasi $REPO/rofi/config.rafi
rsync $CONF/rofi/configlauncher $REPO/rofi/configlauncher
rsync $CONF/rofi/powermenu $REPO/rofi/powermenu