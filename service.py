import os
import time

import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
addonid = addon.getAddonInfo('id')

displaystate = True


def log(msg, level):
    xbmc.log("%s: %s" % (addonid, msg), level=level)


def amlogic_display_power(state):
    global displaystate
    if displaystate == state:
        return
    if state:
        sysfs = '1'
        msg = 'on'
    else:
        sysfs = '0'
        msg = 'off'
    log("Turning %s display" % msg, xbmc.LOGINFO)
    os.system('echo %s > /sys/class/amhdmitx/amhdmitx0/phy' % sysfs)
    displaystate = state


class IdleMonitor(xbmc.Monitor):
    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)
        self.screensaver = False
        self.screensaver_activation_time = -1

    def onScreensaverActivated(self):
        self.screensaver = True
        self.screensaver_activation_time = time.time()

    def onScreensaverDeactivated(self):
        self.screensaver = False
        amlogic_display_power(True)


monitor = IdleMonitor()
while not monitor.abortRequested():
    if monitor.waitForAbort(1):
        break
    if monitor.screensaver:
        idletime = time.time() - monitor.screensaver_activation_time
        if displaystate and idletime >= (int(addon.getSetting('delay')) * 60):
            log("Screensaver is running for %i seconds" % idletime, xbmc.LOGDEBUG)
            if addon.getSetting('no_action_when_playing') == 'true' and xbmc.Player().isPlaying() and not xbmc.getCondVisibility("Player.Paused"):
                log("Still playing media, not taking action", xbmc.LOGDEBUG)
            else:
                amlogic_display_power(False)
