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
from libqtile import qtile
from libqtile import hook, bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#from qtile_extras import widget
#from qtile_extras.widget.decorations import PowerLineDecoration
#from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod9 = "shift"
home = os.path.expanduser('~')

terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "n", lazy.layout.next()),
    Key([mod], "s", lazy.next_screen()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left(), lazy.layout.shrink().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "l", lazy.layout.grow_right(), lazy.layout.grow().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "j", lazy.layout.grow_down(), lazy.layout.maximize().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "k", lazy.layout.grow_up(), lazy.layout.normalize().when(layout=["monadtall", "monadwide"])),
    #Key([mod, "cuntrol"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod9], "Shift_R",  lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]

#MOVE WINDOW TO NEXT SCREEN
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])

def init_group_names():
    return [("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            ("", {'layout': 'MonadTall'}),
            #("MAX", {'layout': 'max'}),
            #("MEDIA", {'layout': 'columns'}),
            #("MAIL", {'layout': 'columns'}),
            #("MON", {'layout': 'bsp'}),
            ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# COLORS FOR THE BAR
#Theme name : RavenDark
def init_colors():
    return [
        ["#111416", "#111416"], # 0 : black
        ["#1e1e20", "#1e1e20"], # 1 : secondary background : dark
        ["#376bc3", "#376bc3"], # 2 : blue
        ["#F7B232", "#F7B232"], # 3 : yellow
        ["#C2D5EA", "#C2D5EA"], # 4 : active : light blue-grey
        ["#6F88A4", "#6F88A4"], # 5 : inactiv : grey blue
        ["#E5E9F0", "#E5E9F0"], # 6 : main text color : pale grey
        ["#aa5cff", "#aa5cff"], # 7 : purple
        ["#f20202", "#f20202"], # 8 : red alert
        ["#7cec3c", "#7cec3c"], # 9 : green
        ["#ea1b52", "#ea1b52"], # 10 : pink
        ["#ec743c", "#ec743c"], # 11 : peach

    ]
colors = init_colors()

# def init_layout_theme():
#     return {"margin":7,
#             "border_width":2,
#             "border_focus": colors[2],
#             "border_normal": colors[0]
#             }

# layout_theme = init_layout_theme()

layouts = [
    #layout.Columns(margin=10, border_width=2, border_focus=colors[0], border_normal=colors[1]),
    layout.MonadTall(margin=6, border_width=1, border_focus=colors[3], border_normal=colors[0]),
    #layout.Bsp(margin=0, border_width=0),
    #layout.Floating(border_width=1, border_focus=colors[2], border_normal=colors[3]),
    layout.Max(margin=18, border_width=0),
]

screens = [
    Screen(
        top=bar.Bar(
            [
# --------------- LEFT SIDE -------------------------------------------------
                widget.ThermalSensor(
                    font="Noto Sans medium",
                    fontsize = 18,
                    tag_sensor = 'Package id 0',
                    foreground = colors[6],
                    foreground_alert = colors[8],
                    threshold = 85,
                    fmt = '{}',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
                    update_interval = 1,
                    padding = 10,
                ),
                widget.ThermalSensor(
                    font="Noto Sans medium",
                    fontsize = 18,
                    foreground = colors[6],
                    foreground_alert = colors[8],
                    threshold = 85,
                    fmt = '{}',
                    padding = 10,
                    update_interval = 1,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('hardinfo')},
                ),
                widget.NvidiaSensors(
                    font="Noto Sans medium",
                    fontsize = 18,
                    foreground = colors[6],
                    foreground_alert = colors[8],
                    threshold = 85,
                    padding = 10,
                    format = '{temp}°C',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nvidia-settings')},
                ),
                widget.CheckUpdates(
                    font="FontAwesome",
                    fontsize = 18,
                    foreground = colors[11],
                    colour_have_updates = colors[11],
                    colour_no_updates = colors[11],
                    update_interval = 600,
                    distro = "Arch_checkupdates",
                    display_format = " {updates} ",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e yay')},
                    padding = 30,
                ),
                widget.TextBox(
                    font="FontAwesome",
                    text="",
                    foreground=colors[9],
                    fontsize=24,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty')},
                ),
                # widget.Net(
                #     font="FontAwesome",
                #     fontsize = 20,
                #     interface = "enp46s0",
                #     format=' {down}',
                #     foreground = colors[9],
                #     padding = 10,
                #     update_interval = 1,
                # ),
                # widget.Net(
                #     font="FontAwesome",
                #     fontsize = 20,
                #     interface = "enp46s0",
                #     format=' {up}',
                #     foreground = colors[3],
                #     padding = 10,
                #     update_interval = 1,
                # ),
# --------------- MIDDLE -------------------------------------------------
                widget.WindowName(
                    font="Noto Sans medium",
                    fontsize = 16,
                    foreground = colors[4],
                    for_current_screen=True,
                    format = '',
                ),
                widget.GroupBox(
                    font="FontAwesome",
                    fontsize = 24,
                    borderwidth = 2,
                    disable_drag = True,
                    active = colors[5],
                    inactive = colors[1],
                    rounded = True,
                    highlight_method = "text",
                    this_current_screen_border = colors[3],
                    other_current_screen_border = colors[3],
                    this_screen_border = colors[5],
                    other_screen_border = colors [5],
                    block_highlight_text_color = colors[0],
                    hide_unused = True,
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                #widget.Clock(format="%Y-%m-%d %a %I:%M %p"),

# --------------- LEFT SIDE -------------------------------------------------
                widget.WindowName(
                    format = '',
                ),
                widget.Systray(
                    font="FontAwesome",
                    icon_size = 25,
                ),
                widget.Spacer(
                    length=30,
                ),
                widget.Clock(
                    font="Noto Sans medium",
                    fontsize = 18,
                    foreground=colors[6],
                    format="%d.%m.%y",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e calcurse')},
                ),
                widget.KeyboardLayout(
                    font="FontAwesome",
                    fontsize = 24,
                    foreground = colors[3],
                    configured_keyboards = ['de', 'ru'],
                    display_map = {'de':'', 'ru':''},
                    padding = 15,
                ),
                widget.Clock(
                    font="Noto Sans medium",
                    fontsize = 18,
                    foreground=colors[6],
                    format="%H:%M:%S",
                ),
            ],
            size = 32,
            opacity = 0.8
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),

    # Screen(
    #     bottom=bar.Bar(
    #         [
    #         ],
    #         size = 24,
    #         opacity = 0.8
    #     ),
    # ),
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
#wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
