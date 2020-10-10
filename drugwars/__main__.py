from drugwars.classes import Player
from drugwars.events import *
import requests
import os

def main():
    clear()
    try:
        logo = '''\
           ___  ___  __  _______  
          / _ \/ _ \/ / / / ___/  
         / // / , _/ /_/ / (_ /   
        /____/_/|_|\____/\___/  ____
           | | /| / / _ | / _ \/ __/
           | |/ |/ / __ |/ , _/\ \  
           |__/|__/_/ |_/_/|_/___/'''

        title_screen = [
            [logo],
            ["        Created by Max Bridgland"],
            ["     Based on the DOS Game of the 80s"],
            [""],
            ["   Press ENTER to Play or Ctrl+C to Quit"],
            [""],
            ["   Version: 1.1.7  Report Bugs on GitHub"],
            ["https://github.com/M4cs/Drugwars/issues/new"]
        ]
        print(SingleTable(title_screen).table)
        input()
        p = Player()
        clear()
        main_screen(p)
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()