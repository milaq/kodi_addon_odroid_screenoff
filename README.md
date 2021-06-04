![](resources/icon.png)

# Introduction
ODROID devices with Coreelec can't do DPMS screen standby. If the attached display doesn't support CEC power management, there is only the option left to turn off the HMDI output.
This addon turns off the screen after a configurable delay when the screensaver is activated (similar to the CEC plugin but compatible with _any_ screen) and turns it back on when the screensaver is deativated..

Known compatible ODROID models: C2, C4, N2

# Requirements
This addon requires at least Kodi version 19 (Matrix) and relies on _having a Kodi screensaver enabled_.

# Installation

Go to the releases page and download an addon zip or install via my [addon repo](https://github.com/milaq/kodi_repository_milaq).

# Configuration

If enabled, the addon automatically turns off the screen by utilizing the Amlogic specific sysfs at `/sys/class/amhdmitx/amhdmitx0/phy`.

You can configure the delay to turn off the screen after screensaver activation in the addon settings dialog.
