# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"

terminal = "alacritty"                  # Mod + Return
browser = "google-chrome-stable"        # Mod + B
main_code_ide = "code"                  # Mod + C
messaging_app = "discord"               # Mod + D
file_manager = "nautilus"               # Mod + F
music_player = "spotify"                # Mod + M
minecraft_launcher = "multimc"          # Mod + Shift + M
steam = "steam"                         # Mod + S
text_editor = "gedit"                   # Mod + T

keys = [
    # Switch between windows
    Key([mod], "Left",
        lazy.layout.left(),
        desc="Move focus to left"),

    Key([mod], "Right",
        lazy.layout.right(),
        desc="Move focus to right"),

    Key([mod], "Down",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "Up",
        lazy.layout.up(),
        desc="Move focus up"),

    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left",
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"),

    Key([mod, "shift"], "Right", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"),

    Key([mod, "shift"], "Down", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"),

    Key([mod, "shift"], "Up", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"),


    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),

    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),

    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        desc="Grow window down"),

    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        desc="Grow window up"),

    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return",
        lazy.spawn("alacritty"),
        desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    Key(["control", "shift"], "c",
        lazy.window.kill(),
        desc="Kill focused window"),
        
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"),

    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),

    # ///////////
    # LAUNCH APPS
    # ///////////
    
    Key([mod], "b", 
        lazy.spawn(browser), 
        desc="Launch google chrome"),

    Key([mod], "c", 
        lazy.spawn(main_code_ide), 
        desc="Launch VScode"),

    Key([mod], "d", 
        lazy.spawn(messaging_app), 
        desc="Launches discord"),

    Key([mod, "shift"], "d", 
        lazy.spawn("/home/humberto/Documents/Custom System Files/load audio.sh"), 
        desc="Audio"),

    Key([mod], "f", 
        lazy.spawn(file_manager), 
        desc="Launch file manager"),

    Key([mod], "t", 
        lazy.spawn(text_editor), 
        desc="Launches text editor"),

    Key([mod], "s", 
        lazy.spawn(steam), 
        desc="Launches steam"),

    Key([mod, "shift"], "m", 
        lazy.spawn(minecraft_launcher), 
        desc="Launches MultiMinecraft"),

    Key([mod], "m", 
        lazy.spawn(music_player), 
        desc="Launches Spotify"),
        
    Key([mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [
    Group("0. HOME", exclusive=False, layout = 'monadtall'),
    Group("1. CODE", matches=[Match(wm_class=("code"))], exclusive=False, layout = 'monadtall'),
    Group("2. COMS", matches=[Match(wm_class=("discord"))], exclusive=False, layout = 'monadtall'),
    Group("3. INTR", matches=[Match(wm_class=("google-chrome"))], exclusive=False, layout = 'monadtall'),
    Group("4. GAME", matches=[Match(wm_class=("Steam"))], exclusive=False, layout = 'max'),
    Group("5. MINE", matches=[Match(wm_class=("MultiMC5"))], exclusive=False, layout = 'max'),
    Group("6. SPOT", matches=[Match(wm_class=("spotify"))], exclusive=False, layout = 'monadwide')
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name[0], lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name[0], lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

border_focus = '#ffffff'
border_normal = '#000000'
border_width = 2

layouts = [
    layout.Max(),
    layout.MonadTall(
        ratio = 0.55,
        border_width = 0,
        margin = 10
    ),
    layout.MonadWide(
        ratio = 0.6,
        border_width = 0,
        margin = 10
    ),
    
    # layout.Matrix(),
    # layout.Columns(border_width=2, border_focus = '#ffffff', border_normal='#000000'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Source Code Pro Semi-Bold',
    fontsize=12,
    padding=3
)
extension_defaults = widget_defaults.copy()

def betterWindowNames(text):
    return text[text.rfind('-') + 1 ::] + ' '

def betterNotifications(text):
    return text[0:text.find('(') - 1] + ':' + text[text.rfind('-') + 1::] + ' '

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(' '),
                
                widget.GroupBox(
                    active = '#aa88ff',
                    inactive = '#666666',
                    block_highlight_text_color = '#000000',

                    background = '#303442',
                    foreground = '#FFFFFF',

                    this_current_screen_border = '#FFFFFF',
                    this_screen_border = '#999999',

                    other_current_screen_border = '#FFFFFF',
                    other_screen_border = '#999999',

                    rounded = True,
                    highlight_method = 'block',
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.CurrentLayout(
                    background = '#303442',
                    foreground = '#ffaa88',
                    padding = 25
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.Prompt(
                    background = '#FFFFFF',
                    foreground = '#000000'
                ),

                widget.WindowName(
                    background = '#303442',
                    empty_group_string = 'Open Something!',
                    for_current_screen = True,
                    format = '{name}',
                    parse_text = betterWindowNames
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.CheckUpdates(
                    distro = 'Arch',

                    colour_have_updates = '#ff4444',
                    colour_no_updates = '#44ff44',

                    execute = 'sudo pacman -Syu',

                    no_update_string = 'Up to date!',
                    display_format = 'Updates: {updates}',

                    update_interval = 3600
                ),
                
                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.CPU(
                    background = '#303442',
                    foreground = '#ff6666',
                    update_interval = 5.0,
                    format = ' CPU: {load_percent}% '
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.Memory(
                    background = '#303442',
                    foreground = '#66ff66',
                    measure_mem = 'M',
                    format = ' Mem:{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} '
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.Net(
                    background = '#303442',
                    foreground = '#6666ff',
                    interface = "enp42s0",
                    format = ' ▼ {down} | ▲ {up} '
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),
                
                widget.Systray(
                    background = '#303442',
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.Volume(
                    
                ),

                widget.Sep(
                    background = '#303442',
                    foreground = '#707482'
                ),

                widget.Clock(
                    background = '#303442',
                    format=' %Y-%m-%d %a %I:%M %p '
                    ),
            ],
            24,
            background = '#303442',
            opacity = 0.75,
            margin = 5,
        ),
    ),
    Screen(
        top = bar.Bar(
            [
                widget.TextBox(' '),
                widget.Mpris2(
                    name='spotify',
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    stop_pause_text=' No music playing ',
                    scroll_wait_intervals = 0,
                    scroll_interval = 0
                ),
                widget.TextBox(' '),

                widget.Sep(),

                widget.TextBox(' '),

                widget.Notify(),
            ],
            24,
            background = '#303442',
            opacity = 0.75,
            margin = 5,
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
