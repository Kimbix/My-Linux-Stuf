function sync-git;
    echo "Copying" "$argv[1]" "to" "$argv[2]"
    rsync $argv[1] $argv[2]

    if [ $status -eq 0 ]
    echo "Copied" "$argv[1]" "to" "$argv[2]"
    else
    echo "Failed to copy" "$argv[1]"
    end

    echo ""
end;

function sync-github-config;
# Syncs the configuration files with the git repo
set CONF '/home/humberto/.config'
set REPO '/home/humberto/Documents/Repos/My-Linux-Stuf'

# Autolaunch script
sync-git $CONF/polybar/launch.sh $REPO/polybar/launch.sh

# Configuration for polybar
sync-git $CONF/polybar/config $REPO/polybar/config

# Fish configuration file
sync-git $CONF/fish/config.fish $REPO/fish/config.fish

# i3 configuration
sync-git $CONF/i3/config $REPO/i3/config

# Rofi configuration
sync-git $CONF/rofi/config.rasi $REPO/rofi/config.rafi

# Rofi file for launching configs
sync-git $CONF/rofi/configlauncher $REPO/rofi/configlauncher

# Rofi file for the power menu
sync-git $CONF/rofi/powermenu $REPO/rofi/powermenu

# Menu when powering off
sync-git /usr/share/rofi/themes/powerMenu.rasi         $REPO/rofi/themes/powerMenu.rasi
sync-git /usr/share/rofi/themes/powerMenumessage.rasi  $REPO/rofi/themes/powerMenumessage.rasi
sync-git /usr/share/rofi/themes/powerMenuconfirm.rasi  $REPO/rofi/themes/powerMenuconfirm.rasi

# Config files launcher
sync-git /usr/share/rofi/themes/configLauncher.rasi    $REPO/rofi/themes/configLauncher.rasi

# App launchers
sync-git /usr/share/rofi/themes/appLauncher.rasi       $REPO/rofi/themes/appLauncher.rasi
end;


if status is-interactive
    # Commands to run in interactive sessions can go here

    starship init fish | source
    alias reboot="doas REBOOT"
end

