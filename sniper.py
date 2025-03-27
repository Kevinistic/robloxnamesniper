# MAJOR CREDIT TO ocuz FOR THE ORIGINAL SNIPE CODE
# https://github.com/ocuz/Roblox-Name-Sniper
# This version has been modified for better support and to be run continuously
# Be sure to first download python and pip, then install the required libraries
# PLEASE USE AT YOUR OWN RISK, I AM NOT RESPONSIBLE FOR ANY BANS OR ISSUES THAT MAY OCCUR

import random
import time
import string
import requests
from colorama import Fore, Style, init
import sys
import os

init()

def check_username(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        response = requests.get(url)
        response_data = response.json()

        code = response_data.get("code")
        if code == 0:
            sys.stdout.write('\a')  # ASCII bell character
            sys.stdout.flush()
            print(Fore.GREEN + f"VALID: {username}" + Style.RESET_ALL)
            with open("usernames.txt", "a") as f: # write to usernames.txt
                f.write(f"{username}\n")
        elif code == 1:
            print(Fore.LIGHTBLACK_EX + f"TAKEN: {username}" + Style.RESET_ALL)
        elif code == 2:
            print(Fore.RED + f"CENSORED: {username}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"Wtf ({code}): {username}" + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"ERROR {username}: {e}" + Style.RESET_ALL)

def main():
    allowed_chars = string.ascii_lowercase + string.digits + '_'

    print(Fore.CYAN + "Roblox 4-character username checker running..." + Style.RESET_ALL)
    print(Fore.CYAN + "Valid usernames will be saved to usernames.txt in the same folder as script" + Style.RESET_ALL)
    print(Fore.CYAN + "Press Ctrl+C to stop\n" + Style.RESET_ALL)

    try:
        while True:
            username = ''.join(random.choice(allowed_chars) for _ in range(4)) # generate 4-character username
            if not (username.startswith('_') or username.endswith('_')): # no underscore at start or end
                check_username(username)
                time.sleep(0.5) # adjust delay
    except KeyboardInterrupt:
        print(Fore.CYAN + "\nStopped. Valid usernames saved to usernames.txt" + Style.RESET_ALL)
        print(Fore.CYAN + "\nThank you!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()