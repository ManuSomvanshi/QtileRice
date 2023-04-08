# -*- coding: utf-8 -*- 
import os
import re
import socket
import subprocess
from libqtile import backend, qtile
from libqtile.config import Click, Drag, Group, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401
import fontawesome as fa
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

#### KEY BINDING ####
from key_bindings import mod, myTerm, myBrowser, myFM, keys
keys = keys()

groups = [Group(fa.icons["terminal"]+ ' ',  layout='bsp'),
          Group(fa.icons["firefox"] + ' ',  layout='monadtall'),
          Group(fa.icons["code"]+ ' ',      layout='monadtall'),
          Group(fa.icons["superscript"]+ ' ', layout="bsp"),
          Group(fa.icons["spray-can"]+ ' ', layout='monadtall'),
          Group(fa.icons["video"]+ ' ',     layout='monadtall'),
          Group(fa.icons["pray"]+ ' ',      layout='monadtall')
         ]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

#### LAYOUTS ####
layout_theme = {"border_width": 3,
                "margin": 8,
                "border_focus": "#076678",
                "border_normal": "1D2330"
                }

layouts = [
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme)
]

#### CHOOSING A COLOR SCHEME ####
import themes
colors = themes.gruvbox_colors()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

#DECORATE THE WIDGETS
decor_left_dark = {
    "decorations": [
        RectDecoration(colour = colors['dark0'], radius=12, filled=True, padding_y=0),
    ],
    "padding": 18,
    "foreground": colors['bright_red']
}

decor_left_light = {
    "decorations": [
        RectDecoration(colour = colors['dark0'], radius=12, filled=True, padding_y=0)
    ],
    "padding": 18,
    "foreground": colors['bright_yellow']
}

decor_right_dark = {
    "decorations": [
        RectDecoration(colour = colors['dark0'], radius=12, filled=True, padding_y=0)
    ],
    "padding": 18,
    "foreground": colors['bright_orange']
}

decor_right_light = {
    "decorations": [
        RectDecoration(colour = colors['dark0'], radius=12, filled=True, padding_y=0)
    ],
    "padding": 18,
    "foreground": colors['bright_blue']
}

decor_groupbox = {
    "decorations": [
        RectDecoration(colour = colors['dark0_hard'], radius=12, filled=True, padding_y=0, padding_x=1)
    ],
    "padding": 15,
}

##### BLUETOOTH DEVICE MAC ADDRESS   #####
from bluetooth import list_connected_devices
hci_string = list_connected_devices()

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="FantasqueSansmono Nerd Font",
    fontsize = 18,
    padding = 5,
    background='#00000000',
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Spacer(length=5),

              widget.Clock(
                       format= fa.icons["calendar"]+ '  %d/%m/%y',
                       **decor_left_dark
                       ),

              widget.Spacer(length=5),

              widget.Clock(
                       format= fa.icons['city'] + ' %H:%M',
                       **decor_left_light
                       ),

              widget.Spacer(length=5),

              widget.CurrentLayout(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       scale = 0.7,
                       **decor_left_dark
                       ),

              widget.Spacer(),

              widget.GroupBox(
                       fontsize = 18,
                       disable_drag = True,
                       margin_x = 6,
                       borderwidth = 3,
                       inactive = colors['gray_244'],
                       active = colors['neutral_yellow'],
                       rounded = True,
                       highlight_color = "#00000000",
                       highlight_method = "line",
                       this_current_screen_border = colors['neutral_blue'],
                       urgent_text = colors['neutral_red'],
                       use_mouse_wheel = False,
                       **decor_groupbox
                       ),

             widget.Spacer(),

             widget.WidgetBox(
                **decor_right_light, 
                text_closed = " " + fa.icons["wifi"] +"  " + fa.icons["bluetooth"] + " ",
                text_open = " hide ",
                widgets = [widget.Spacer(length=5),

                           widget.Wlan(
                           interface = "wlo1",
                           disconnected_message = fa.icons["times"],
                           fmt = fa.icons["wifi"] + '  {}',
                           format = '{essid}',
                           mouse_callbacks = {"Button1": lazy.spawn("nm-connection-editor")},
                           **decor_right_dark
                                    ),

                           widget.Spacer(length=5),

                           widget.Bluetooth(
                                    fmt = fa.icons["bluetooth"] + ' {}',
                                    hci = hci_string,
                                    mouse_callbacks = {"Button1": lazy.spawn("blueman-manager")},
                                    **decor_right_light
                                    ),
                           ]
                                     ),
              widget.Spacer(length = 5),

                           widget.Memory(
                                     format = '{MemUsed:.0f}{mm}',
                                     fmt = fa.icons["microchip"]+'  {}',
                                     **decor_right_dark
                                     ),

                           widget.Spacer(length = 5),

                           widget.Battery(
                                     charge_char = fa.icons["bolt"],
                                     discharge_char = fa.icons["battery-half"],
                                     full_char = fa.icons["battery-full"],
                                     format = '{char}  {percent:2.0%}',
                                     update = 15,
                                     show_short_text = False,
                                     **decor_right_light
                                   ),

                           widget.Spacer(length=5),

                           widget.PulseVolume(
                                     fmt = '  {}',
                                     update_interval = 0.1,
                                     volume_app = "pamixer",
                                     mouse_callbacks = {"Button1": lazy.spawn('pavucontrol')},
                                     **decor_right_dark
                                   ),
             widget.Spacer(length=5),
             ]
    return widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), opacity=1, size=25, background='#00000000', margin=[5,1,1,1]))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
