# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2023 c0deWanted
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
    return [("1", {'layout': 'MonadTall'}),
            ("2", {'layout': 'MonadTall'}),
            ("3", {'layout': 'MonadTall'}),
            ("4", {'layout': 'MonadTall'}),
            ("5", {'layout': 'MonadTall'}),
            ("6", {'layout': 'MonadTall'}),
            ("7", {'layout': 'MonadTall'}),
            ("8", {'layout': 'MonadTall'}),
            ("9", {'layout': 'MonadTall'}),
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
        #["#282C34", "#282C34"], # 0 : main background : dark grey - doom one
        ["#282a33", "#282a33"], # 0 : main background : dark grey - Qogir-dark
        ["#3B4252", "#3B4252"], # 1 : secondary background : dark
        ["#2674CF", "#2674CF"], # 2 : blue background : mid blue
        ["#F7B232", "#F7B232"], # 3 : yellow background : nice yellow
        ["#C2D5EA", "#C2D5EA"], # 4 : active : light blue-grey
        ["#6F88A4", "#6F88A4"], # 5 : inactiv : grey blue
        ["#E5E9F0", "#E5E9F0"], # 6 : main text color : pale grey
        ["#0B0B17", "#0B0B17"], # 7 : raven balck
        ["#a73020", "#a73020"], # 8 : red alert
        ["#a3aab2", "#a3aab2"], # 9 : another background : light grey
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
    layout.MonadTall(margin=6, border_width=2, border_focus=colors[1], border_normal=colors[0]),
    #layout.Bsp(margin=0, border_width=0),
    #layout.Floating(border_width=1, border_focus=colors[2], border_normal=colors[3]),
    layout.Max(margin=18, border_width=0),
]

# powerline = {
#     "decorations": [
#         PowerLineDecoration(
#             path = 'forward_slash')
#     ]
# }


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
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),


# screens = [
# # Primary screen
#     Screen(
#          top=bar.Bar(
#              [
#                 widget.Sep(
#                     linewidth = 0,
#                     background = colors[0],
#                     padding = 20,
#                 ),
#                 widget.GroupBox(
#                     font="Noto Sans bold",
#                     fontsize = 14,
#                     borderwidth = 2,
#                     disable_drag = True,
#                     active = colors[6],
#                     inactive = colors[5],
#                     rounded = True,
#                     highlight_method = "block",
#                     this_current_screen_border = colors[2],
#                     other_current_screen_border = colors[2],
#                     this_screen_border = colors[5],
#                     other_screen_border = colors [5],
#                     background = colors[0],
#                     block_highlight_text_color = colors[6],
#                     hide_unused = True,
#                 ),
#                 widget.Spacer(
#                     background=colors[0],
#                     length=100,
#                 ),
#                 widget.WindowName(
#                     font="Noto Sans medium",
#                     fontsize = 20,
#                     padding = 30,
#                     foreground = colors[4],
#                     background = colors[0],
#                     for_current_screen=True,
#                 ),
#                 widget.CheckUpdates(
#                     font="Noto Sans bold",
#                     fontsize = 14,
#                     update_interval = 3600,
#                     distro = "Arch_checkupdates",
#                     display_format = "Upd.  {updates} ",
#                     foreground = colors[3],
#                     background = colors[0],
#                     #**powerline,
#                     colour_have_updates = colors[3],
#                     colour_no_updates = colors[1],
#                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')},
#                     padding = 10,
#                 ),
#                 widget.KeyboardLayout(
#                     font="Mononoki Nerd Font Mono bold",
#                     fontsize = 20,
#                     foreground = colors[3],
#                     background= colors[0],
#                     configured_keyboards = ['de', 'ru'],
#                     display_map = {'de':'D', 'ru':'R'},
#                     padding = 5,
#                 ),
#                 widget.Sep(
#                     linewidth = 0,
#                     background = colors[0],
#                     padding = 20,
#                 ),
#                 widget.Systray(
#                     padding = 10,
#                     icon_size = 21,
#                     background = colors[0],
#                 ),
#                 widget.Sep(
#                     linewidth = 0,
#                     padding = 20,
#                     background = colors[0],
#                 ),
#                 widget.Clock(
#                     font = "Noto Sans bold",
#                     foreground = colors[6],
#                     background = colors[0],
#                     fontsize = 16,
#                     padding = 15,
#                     format="%Y.%m.%d",
#                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e calcurse')},
#                 ),
#                 widget.Clock(
#                     font = "Noto Sans bold",
#                     foreground = colors[6],
#                     background = colors[0],
#                     fontsize = 16,
#                     padding = 15,
#                     format="%H:%M:%S",
#                ),
#             ],
#             size = 32,
#             opacity = 0.7
#         ),
#     ),
# Secondary screen
    # Screen(
    #     top=bar.Bar(
    #         [
    #             widget.Sep(
    #                 linewidth = 0,
    #                 background = colors[0],
    #                 padding = 10,
    #             ),
    #             widget.TextBox(
    #                 font="FontAwesome",
    #                 text="",
    #                 foreground=colors[3],
    #                 background=colors[0],
    #                 fontsize=18,
    #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e vim /home/oh/.config/qtile/config.py')},
    #             ),
    #             widget.Sep(
    #                     linewidth = 0,
    #                     background = colors[0],
    #                     padding = 15,
    #             ),
    #             widget.TextBox(
    #                 font="FontAwesome",
    #                 text="",
    #                 foreground=colors[3],
    #                 background=colors[0],
    #                 fontsize=18,
    #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e vim /home/oh/.config/qtile/scripts/autostart.sh')},
    #             ),
    #             widget.Sep(
    #                 linewidth = 0,
    #                 background = colors[0],
    #                 padding = 15,
    #             ),
    #             widget.TextBox(
    #                 font="FontAwesome",
    #                 text="",
    #                 foreground=colors[3],
    #                 background=colors[0],
    #                 fontsize=18,
    #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e vim /home/oh/.config/sxhkd/sxhkdrc')},
    #             ),
    #             widget.Sep(
    #                     linewidth = 0,
    #                     background = colors[0],
    #                     padding = 25,
    #             ),
    #             widget.GroupBox(
    #                 font="Noto Sans bold",
    #                 fontsize = 18,
    #                 borderwidth = 2,
    #                 disable_drag = True,
    #                 active = colors[6],
    #                 inactive = colors[5],
    #                 rounded = True,
    #                 highlight_method = "block",
    #                 this_current_screen_border = colors[3],
    #                 other_current_screen_border = colors[3],
    #                 this_screen_border = colors[5],
    #                 other_screen_border = colors [5],
    #                 background = colors[0],
    #                 block_highlight_text_color = colors[7],
    #             ),
    #             widget.Sep(
    #                 linewidth = 0,
    #                 background = colors[0],
    #                 padding = 25,
    #                 **powerline,
    #             ),
    #             widget.TextBox(
    #                 font="FontAwesome",
    #                 text="",
    #                 foreground=colors[3],
    #                 background=colors[0],
    #                 fontsize=14,
    #             ),
    #             widget.WindowName(
    #                 font="Mononoki Nerd Font Mono bold",
    #                 fontsize = 20,
    #                 padding = 30,
    #                 foreground = colors[6],
    #                 background = colors[0],
    #             ),
    #             # widget.CurrentLayout(
    #             #     font="Mononoki Nerd Font Mono bold",
    #             #     fontsize = 22,
    #             #     padding = 10,
    #             #     foreground = colors[7],
    #             #     background = colors[3],
    #             #     **powerline,
    #             # ),
    #             widget.ThermalSensor(
    #                 font = "Mononoki Nerd Font Mono bold",
    #                 fontsize = 22,
    #                 tag_sensor = 'Package id 0',
    #                 foreground = colors[6],
    #                 background = colors[0],
    #                 threshold = 90,
    #                 fmt = 'C {}',
    #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('hardinfo')},
    #                 update_interval = 1,
    #                 padding = 10,
    #             ),
    #             widget.ThermalSensor(
    #                 font = "Mononoki Nerd Font Mono bold",
    #                 fontsize = 22,
    #                 foreground = colors[6],
    #                 background = colors[0],
    #                 threshold = 90,
    #                 fmt = 'P {}',
    #                 padding = 25,
    #                 update_interval = 1,
    #             ),
    #             widget.NvidiaSensors(
    #                 font = "Mononoki Nerd Font Mono bold",
    #                 fontsize = 22,
    #                 foreground = colors[6],
    #                 foreground_alert = colors[8],
    #                 background = colors[0],
    #                 padding = 10,
    #                 format = 'G {temp}°C'
    #             ),
    #             widget.KeyboardLayout(
    #                 font = "Noto Sans bold",
    #                 fontsize = 20,
    #                 foreground = colors[3],
    #                 background= colors[0],
    #                 configured_keyboards = ['de', 'ru'],
    #                 padding = 25,
    #             ),
    #             # widget.Clock(
    #             #     font = "Noto Sans bold",
    #             #     foreground = colors[6],
    #             #     background = colors[0],
    #             #     fontsize = 18,
    #             #     padding = 15,
    #             #     format="%Y.%m.%d "
    #             # ),
    #             widget.Clock(
    #                 font = "Noto Sans bold",
    #                 foreground = colors[6],
    #                 background = colors[0],
    #                 fontsize = 22,
    #                 padding = 15,
    #                 format="%H:%M:%S",
    #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e calcurse')},
    #            ),
    #             widget.TextBox(
    #                 font="FontAwesome",
    #                 text="",
    #                 foreground=colors[3],
    #                 background=colors[0],
    #                 fontsize=22,
    #                 padding = 15,
    #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('archlinux-logout')},
    #             ),
    #         ],
    #         size = 28,
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
