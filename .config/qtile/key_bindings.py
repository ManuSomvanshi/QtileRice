from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "tor-browser"   # My browser of choice
myFM = "pcmanfm"          # file manager

def keys():
    keys = [
             ### THE ESSENTIALS ###
             Key([mod], "Return",
                 lazy.spawn(myTerm+" -e bash"),
                 desc='Launches My Terminal'
                 ),
             Key([mod, "shift"], "Return",
                 lazy.spawn("/home/isomorphism/.config/rofi/launchers/type-3/launcher.sh"),
                 desc='Run Launcher'
                 ),
             Key([mod, "control"], "Return",
                 lazy.spawn("/home/isomorphism/.config/rofi/applets/bin/powermenu.sh"),
                 desc='Run power menu'
                 ),
             Key([mod], "q",
                 lazy.spawn("/home/isomorphism/.config/rofi/applets/bin/quicklinks.sh"),
                 desc='Run quicklinks'
                 ),
             Key([mod, "shift"], "m",
                 lazy.spawn(myFM),
                 desc = 'file-manager'
                 ),
             Key([mod], "b",
                 lazy.spawn(myBrowser),
                 desc='private browser'
                 ),
             Key([mod], "Tab",
                 lazy.next_layout(),
                 desc='Toggle through layouts'
                 ),
             Key([mod, "shift"], "c",
                 lazy.window.kill(),
                 desc='Kill active window'
                 ),
             Key([mod, "shift"], "r",
                 lazy.restart(),
                 desc='Restart Qtile'
                 ),
             Key([mod, "shift"], "q",
                 lazy.shutdown(),
                 desc='Shutdown Qtile'
                 ),
             Key([mod, "shift"], "b",
                 lazy.spawn('firefox'),
                 desc='work browser'
                 ),
             Key([mod, "shift"], "p",
                 lazy.spawn("/home/isomorphism/.config/rofi/applets/bin/screenshot.sh")
                 ),
             ### WINDOW CONTROLS ###
             #focus windows
             Key([mod], "j",
                 lazy.layout.down(),
                 desc='Move focus down in current stack pane'
                 ),
             Key([mod], "k",
                 lazy.layout.up(),
                 desc='Move focus up in current stack pane'
                 ),
             Key([mod], "h",
                 lazy.layout.left(),
                 desc='moves focus left'
                 ),
             Key([mod], "l",
                 lazy.layout.right(),
                 desc='moves focus right'
                 ),
             #move windows
             Key([mod, "shift"], "j",
                 lazy.layout.shuffle_down(),
                 lazy.layout.section_down(),
                 desc='Move windows down in current stack'
                 ),
             Key([mod, "shift"], "k",
                 lazy.layout.shuffle_up(),
                 lazy.layout.section_up(),
                 desc='Move windows up in current stack'
                 ),
             Key([mod, "shift"], "h",
                 lazy.layout.shuffle_left(),
                 desc='moves window left'
                 ),
             Key([mod, "shift"], "l",
                 lazy.layout.shuffle_right(),
                 desc='moves window right'
                 ),
             #resize windows
             Key([mod], "f",
                 lazy.window.toggle_fullscreen(),
                 desc='toggle fullscreen'
                 ),
             Key([mod], "y",
                 lazy.window.toggle_minimize(),
                 desc='toggle minimize'
                 ),
             #bsp specific
             Key([mod, "control"], "j", 
                 lazy.layout.grow_down(),
                 desc='increase size down'
                 ),
             Key([mod, "control"], "k", 
                 lazy.layout.grow_up(),
                 desc='increase size up'
                 ),
             Key([mod, "control"], "h", 
                 lazy.layout.grow_left(),
                 desc='increase size left'
                 ),
             Key([mod, "control"], "l", 
                 lazy.layout.grow_right(),
                 desc='increase size right'
                 ),
             Key(["mod1", "control"], "o", 
                 lazy.spawn('/home/isomorphism/.config/qtile/picom_toggle.sh'),
                 desc='picom toggle'
                 ),
             #monadtall spcific
             Key([mod], "i", lazy.layout.grow()),
             Key([mod], "o", lazy.layout.shrink()),
             ### BRIGHTNESS ###
             Key([], "XF86MonBrightnessUp",
                 lazy.spawn('xbacklight -display eDP-1 -inc 10'),
                 desc="increase brightness"
                 ),
             Key([], "XF86MonBrightnessDown",
                 lazy.spawn('xbacklight -display eDP-1 -dec 10'),
                 desc="increase brightness"
                 ),
             ### VOLUME ###
             Key([], "XF86AudioRaiseVolume",
                 lazy.spawn('pamixer -i 2'),
                 desc="increase volume"
                 ),
             Key([], "XF86AudioLowerVolume",
                 lazy.spawn('pamixer -d 2'),
                 desc="decrease volume"
                 ),
             Key([], "XF86AudioMute",
                 lazy.spawn('pamixer -t'),
                 desc="mute"
                 )
    ]
    return keys
