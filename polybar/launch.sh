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