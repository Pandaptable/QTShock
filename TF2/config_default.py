import socket

PLAYER_NAME = "nemmy" # steam display name (can also be gotten from typing "name" in console)
CONSOLE_FILE = "D:\\SteamLibrary\\steamapps\\common\\Team Fortress 2\\tf\\console.log" # console.log file

CRIT_DEATH_SHOCK_STRENGTH = 40 # shock strength for crits

DEATH_SHOCK_STRENGTH = 20 # shock strength for normal deaths

# MULTISHOCKER
BEEP_SHOCKER = "" or 0 # index of your shocker for beep (if you only have 1 shocker then leave empty / put 0)

DEATH_SHOCKER = "" or 0 # index of your shocker for normal deaths (if you only have 1 shocker then leave empty / put 0)

CRIT_DEATH_SHOCKER = "" or 0 # index of your shocker for crit deaths (if you only have 1 shocker then leave empty / put 0)


# DO NOT CHANGE
QTSHOCK_IP = socket.gethostbyname("qtshock.local")
SHOCK_URL = f"http://{QTSHOCK_IP}/shock"     # http://qtshock.local/shock -> POST -> FormData
                                             # (has to have a shocker parameter, this is the index of the shocker, likely 0.
                                             # has to have a strength parameter 1 through 99)

VIBRATE_URL = f"http://{QTSHOCK_IP}/vibrate" # http://qtshock.local/vibrate  -> POST -> FormData
                                             # (has to have a shocker parameter, this is the index of the shocker, likely 0.
                                             # has to have a strength parameter 1 through 99)

BEEP_URL = f"http://{QTSHOCK_IP}/beep" # http://qtshock.local/beep  -> POST -> FormData
                                       # (has to have a shocker parameter, this is the index of the shocker likely 0.)