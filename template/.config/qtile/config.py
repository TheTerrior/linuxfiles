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

import os
import subprocess
from typing import List

from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command import lazy


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.run([home + "/.autorun"], shell=True)
    
#@hook.subscribe.startup_once
#def autostart():
#    processes = [
#        ['/usr/bin/setxkbmap', '-option', 'caps:swapescape'],
#        ['feh', '--bg-scale', '/home/user/Pictures/wallpaper/archfoil.jpg'],
#        ['blueman-applet'],
#        ['nextcloud']
#    ]
#
#    for p in processes:
#        subprocess.Popen(p)

mod = "mod4"
alt = "mod1"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Open programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("dmenu_run -nb '#282828' -sf '#FF5555' -sb '#464646' -nf '#bbbbbb'"), desc="Run dmenu"),
    Key([mod, alt], "n", lazy.spawn("nemo"), desc="Run nemo"),
    Key([mod, alt], "f", lazy.spawn("firefox"), desc="Run firefox"),
    Key([mod, alt], "b", lazy.spawn("brave"), desc="Run brave"),
    Key([mod, alt], "l", lazy.spawn("librewolf"), desc="Run librewolf"),
    Key([mod, alt], "v", lazy.spawn("code"), desc="Run code"),
    Key([mod, alt], "d", lazy.spawn("discord"), desc="Run discord"),
    Key([mod, alt], "m", lazy.spawn("alacritty --command lf"), desc="Run lf"),
    Key([mod, alt], "s", lazy.spawn("spotify"), desc="Run spotify"),
    Key([mod, alt], "t", lazy.spawn("steam"), desc="Run steam"),
    
    # Restart Applications
    Key([mod, "shift"], "b", lazy.spawn("nitrogen --restore"), desc="Restart background"),
    #Key([mod, "shift"], "p", lazy.spawn("./.config/polybar/launch.sh"), desc="Restart polybar"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),

    # Lighting
    Key([mod], "KP_Up", lazy.spawn("brightnessctl set 10%+"), desc="Brightness up"),
    Key([mod, "shift"], "KP_Up", lazy.spawn("brightnessctl set 1%+"), desc="Brightness slight up"),
    Key([mod], "KP_Down", lazy.spawn("brightnessctl set 10%-"), desc="Brightness down"),
    Key([mod, "shift"], "KP_Down", lazy.spawn("brightnessctl set 1%-"), desc="Brightness slight down"),
    Key([mod, "control"], "KP_Down", lazy.spawn("redshift -P -O 6500"), desc="Redshift 0"),
    Key([mod, "control"], "KP_Up", lazy.spawn("redshift -P -O 3500"), desc="Redshift 1"),
    Key([mod, "control"], "KP_Left", lazy.spawn("redshift -P -O 2500"), desc="Redshift 2"),
    Key([mod, "control"], "KP_Right", lazy.spawn("redshift -P -O 1500"), desc="Redshift 3"),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -M set Master 5%+"), desc="Volume up"),
    Key(["shift"], "XF86AudioRaiseVolume", lazy.spawn("amixer -M set Master 1%+"), desc="Volume slight up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -M set Master 5%-"), desc="Volume down"),
    Key(["shift"], "XF86AudioLowerVolume", lazy.spawn("amixer -M set Master 1%-"), desc="Volume slight down"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -M set Master toggle"), desc="Volume toggle mute"),

    # Power
    Key([mod], "F1", lazy.spawn("systemctl shutoff"), desc="Shutdown"),
    Key([mod], "F2", lazy.spawn("systemctl reboot"), desc="Restart"),
    Key([mod], "F3", lazy.shutdown(), desc="Logout / Shutdown Qtile"),

    # Close window
    Key([mod, "shift"], "z", lazy.window.kill(), desc="Kill focused window"),

    #Spawn prompt
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Miscellaneous
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #xdotool key U00D1
    #xdotool key shift+U00D1
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="Move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"