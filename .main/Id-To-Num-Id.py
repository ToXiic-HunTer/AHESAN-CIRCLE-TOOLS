
import requests
import os
import sys
import time
import subprocess
from colorama import Fore, Style, init
from termcolor import colored
from pyfiglet import Figlet
from itertools import cycle
import random

colorArr = ["\033[1;91m", "\033[1;92m", "\033[1;93m",
            "\033[1;94m", "\033[1;95m", "\033[1;96m"]

class randomColor:
    color = random.choice(colorArr)

def animated_print(text, color='white'):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Logo
logo = random.choice(colorArr) + f"""
    ###....##.....##.########..######.....###....##....##
   ##.##...##.....##.##.......##....##...##.##...###...##
  ##...##..##.....##.##.......##........##...##..####..##
 ##.....##.#########.######....######..##.....##.##.##.##
 #########.##.....##.##.............##.#########.##..####
 ##.....##.##.....##.##.......##....##.##.....##.##...###
 ##.....##.##.....##.########..######..##.....##.##....##
"""

logo1 = random.choice(colorArr) + f"""

           ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
           ♥︎[√]𝑪𝑰𝑹𝑪𝑳𝑬 𝑰𝑫 𝑻𝑶 𝑵𝑼𝑴𝑩𝑬𝑹 𝑻𝑶 𝑰𝑫 𝑻𝑶𝑶𝑳[√]♥︎
           ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
"""

# Print the logo
os.system('clear')
print(logo)
print(logo1)

url = "https://circle.robi.com.BD/mylife/appapi/appcall.php?op=getUserInfobyNickname"
url1 = "https://circle.robi.com.BD/mylife/appapi/appcall.php?op=getUserInfo"

headers = {
    "x-app-key": "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg",
    "x-api-key": "e4a45af8a8fb00619b976bb703a88972"
}

while True:
    # Input with color
    colored_input = (random.choice(colorArr) + f"[👉]𝗘𝗡𝗧𝗘𝗥 𝗖𝗜𝗥𝗖𝗟𝗘 𝗜𝗗 𝗢𝗥 𝗡𝗨𝗠𝗕𝗘𝗥: " + random.choice(colorArr))
    user_input = str(input(colored_input))
    
    if not user_input:
        print("Please Enter ID or Number")
        continue
    if user_input.isdigit():
        if len(user_input) != 11:
            print("Please Enter 11 digit Number")
            continue
        elif not user_input.startswith(('018', '016')):
            print("Please Enter Robi or Airtel Number")
            continue

        os.system('clear')
        print(logo)
        print(logo1)
        print("\n\n\n")
        animated_print(f"      ♥︎♥︎♥︎𝗡𝗢𝗪 𝗦𝗘𝗘 '{user_input}' 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗧𝗢 𝗚𝗔𝗧𝗛𝗘𝗥 𝗧𝗛𝗘 𝗨𝗦𝗘𝗥 𝗗𝗔𝗧𝗔♥︎♥︎♥︎", 'cyan')
        print("\n\n\n")

        data = {"msisdn": "88" + user_input}
        response = requests.post(url1, headers=headers, data=data)
    else:
        data = {"nickname": user_input}
        response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        try:
            user_data = response.json()["data"]
            # Customize and print the data with color
            print(colored("[👉]𝗡𝗜𝗖𝗞𝗡𝗔𝗠𝗘 :", "green"), colored(user_data.get('nickname', ''), 'green'))
            print(colored("[👉]𝗡𝗨𝗠𝗕𝗘𝗥 :", "cyan"), colored(user_data.get('msisdn', ''), 'cyan'))
            print(colored("[👉]𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 :", "cyan"), colored(user_data.get('name', ''), 'cyan'))
            print(colored("[👉]𝗢𝗣𝗘𝗡 𝗗𝗔𝗧𝗘 :", "yellow"), colored(user_data.get('start_date', ''), 'yellow'))
            print(colored("[👉]𝗦𝗧𝗢𝗣 𝗗𝗔𝗧𝗘 :", "yellow"), colored(user_data.get('end_date', ''), 'yellow'))
            print(colored("[👉]𝗥𝗔𝗡𝗞:", "red"), colored(user_data.get('rank', ''), 'red'))
            print(colored("[👉]𝗚𝗘𝗡𝗗𝗘𝗥 :", "red"), colored(user_data.get('gender', ''), 'red'))
            print(colored("[👉]𝗕𝗜𝗥𝗧𝗛𝗗𝗔𝗬 :", "green"), colored(user_data.get('birthday', ''), 'green'))
            print(colored("[👉]𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘 :", "green"), colored(user_data.get('language', ''), 'green'))
            print(colored("[👉]𝗣𝗢𝗜𝗡𝗧𝗦 :", "yellow"), colored(user_data.get('points', ''), 'yellow'))
            print(colored("[👉]𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 :", "cyan"), colored(user_data.get('followers', ''), 'cyan'))
            print(colored("[👉]𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 :", "cyan"), colored(user_data.get('following', ''), 'cyan'))
            print(colored("[👉]𝗦𝗛𝗢𝗨𝗧𝗦 :", "green"), colored(user_data.get('updates', ''), 'cyan'))
            print(colored("[👉]𝗖𝗢𝗠𝗠𝗘𝗡𝗧𝗦 :", "cyan"), colored(user_data.get('comments', ''), 'cyan'))
            print(colored("[👉]𝗟𝗔𝗦𝗧 𝗦𝗛𝗢𝗨𝗧 𝗧𝗜𝗠𝗘 :", "cyan"), colored(user_data.get('timestamp', ''), 'cyan'))
            print(colored("[👉]𝗟𝗔𝗦𝗧 𝗦𝗛𝗢𝗨𝗧 :", "yellow"), colored(user_data.get('mlstatus', ''), 'green'))
            print(colored("[👉]𝗨𝗦𝗘𝗥 𝗦𝗧𝗔𝗧𝗨𝗦:", "green"), end=' ')
            status_text = user_data.get('status_id')
            if status_text and status_text.strip().lower() == '1':
                print(colored("ON", 'green'))
            else:
                print(colored("OFF", 'red'))

            # Another status check
            print(colored("[👉]𝗔𝗣𝗣 𝗔𝗖𝗖𝗘𝗦𝗦 :", "green"), end=' ')
            status_text = user_data.get('type')
            if status_text and status_text.strip().lower() == '0':
                print(colored("ON", 'green'))
            else:
                print(colored("OFF", 'red'))
                
            print("\n\n\n")
            animated_print(f"               𝗧𝗵𝗶𝘀 𝗦𝘆𝘀𝘁𝗲𝗺 𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗕𝘆 𝗠𝗿 𝗔𝗵𝗲𝘀𝗮𝗻", 'magenta')
            print("\n\n\n")
            input(f"                 {randomColor.color}𝗣𝗿𝗲𝘀𝘀 𝗘𝗻𝘁𝗲𝗿 𝗙𝗼𝗿 𝗖𝗼𝗻𝘁𝗶𝗻𝘂𝗲")
            os.system('clear')
            os.system('python main.py')
            break

        except KeyError:
            animated_print(f"☠️ 𝘜𝘴𝘦𝘳 𝘕𝘰𝘵 𝘍𝘰𝘶𝘯𝘥☠️", 'red')
        
        except requests.exceptions.JSONDecodeError:
            print("Invalid Id")

    else:
        print(colored("Run Time Error! Please Try Again", 'red'))
