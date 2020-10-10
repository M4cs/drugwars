import os, math

def check_ans_yn(a):
    if a.lower() == "y" or a.lower() == "r":
        return 1
    elif a.lower() == "n" or a.lower() == "f":
        return 2
    else:
        return 0

def check_drug_inp(a):
    if len(a) == 0:
        return None
    if a[0].lower() == "c":
        return "cocaine"
    elif a[0].lower() == "h":
        return "heroin"
    elif a[0].lower() == "a":
        return "acid"
    elif a[0].lower() == "w":
        return "weed"
    elif a[0].lower() == "s":
        return "speed"
    elif a[0].lower() == "l":
        return "ludes"
    else:
        return None

def check_ans_bsj(a):
    if a.lower() == "b":
        return 1
    elif a.lower() == "s":
        return 2
    elif a.lower() == "j":
        return 3
    else:
        return 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier) / multiplier)
