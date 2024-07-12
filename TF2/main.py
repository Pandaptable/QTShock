import re
import time
import os
import requests
from config_default import CONSOLE_FILE, PLAYER_NAME, QTSHOCK_IP, SHOCK_URL, BEEP_URL, BEEP_SHOCKER, DEATH_SHOCKER, CRIT_DEATH_SHOCKER, CRIT_DEATH_SHOCK_STRENGTH, DEATH_SHOCK_STRENGTH

def listen(log_file):
    log_file.seek(0, os.SEEK_END)
    last_size = log_file.tell()

    while True:
        current_size = os.stat(log_file.name).st_size
        if current_size < last_size:
            log_file.seek(0, os.SEEK_SET)
            last_size = current_size

        line = log_file.readline()
        if not line:
            time.sleep(0.1)
            continue

        print(line.strip())
        parse(line)
        last_size = log_file.tell()

def parse(line):

    if killfeed_match := re.match(
            """\d\d\/\d\d\/\d\d\d\d - \d\d:\d\d:\d\d: ([^\n]{0,32}) killed ([^\n]{0,32}) with (\w+)\. ?(\(crit\))?""",
            line):

        if killfeed_match[1] == PLAYER_NAME:
            print("Beeped for kill.")
            requests.post(BEEP_URL, data={"shocker": {BEEP_SHOCKER}})
        if killfeed_match[2] == PLAYER_NAME and killfeed_match[4] is not None:
            print(f"Shocked for {CRIT_DEATH_SHOCK_STRENGTH} strength from dying a crit.")
            requests.post(SHOCK_URL, data={"shocker": {CRIT_DEATH_SHOCKER}, "strength": {CRIT_DEATH_SHOCK_STRENGTH}})
        elif killfeed_match[2] == PLAYER_NAME:
            print(f"Shocked for {DEATH_SHOCK_STRENGTH} strength from dying.")
            requests.post(SHOCK_URL, data={"shocker": {DEATH_SHOCKER}, "strength": {DEATH_SHOCK_STRENGTH}})
        else:
            return


if __name__ == '__main__':
    print(f"QTSHOCK IP: {QTSHOCK_IP}")
    log_file = open(CONSOLE_FILE,"r", encoding="utf-8")
    try:
        while True:
            listen(log_file)
    except KeyboardInterrupt:
        print("Stopped")