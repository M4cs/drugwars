from terminaltables import SingleTable
from .helpers import check_ans_yn, clear, round_down, check_ans_bsj, check_drug_inp
from .classes import Prices
from random import randint, choice

def cops_chase(player):
    if 1 == randint(1, 10):
        cops = 0
        r = randint(1, 10)
        if r >= 1 or r <= 6:
            cops = 2
        elif r >= 7 or r <= 9:
            cops = 3
        else:
            cops = 4
        print(SingleTable([["Officer Headass and " + str(cops) + " other(s) are chasing you!"]]).table)
        if player.guns >= 1:
            while True:
                print(SingleTable([["Would you like to (R)un or (F)ight?"], ["HP: " + str(player.health) + "/ 20"]]).table)
                a = input("\n> ")
                aout = check_ans_yn(a)
                if aout == 1:
                    if 1 == randint(1,3):
                        drug = choice(["cocaine", "heroin", "acid", "weed", "speed", "ludes"])
                        pdrug = player.get_amt(drug)
                        if pdrug > 0:
                            amnt = randint(1, 10)
                            pdrug -= amnt
                            clear()
                            print(SingleTable([["You got away but you dropped " + str(amnt) + " bags of " + drug.capitalize() + " while running!!"]]).table)
                        else:
                            print(SingleTable([["You got away!"]]).table)
                        input("Press ENTER to Continue")
                        break
                    else:
                        if randint(1, 6) in [1,6]:
                            player.health -= 1
                            clear()
                            print(SingleTable([["You got hit by one of their shots and lost some health!"]]).table)
                        else:
                            drug = choice(["cocaine", "heroin", "acid", "weed", "speed", "ludes"])
                            pdrug = player.get_amt(drug)
                            if pdrug > 0:
                                amnt = randint(1, 10)
                                pdrug -= amnt
                                clear()
                                print(SingleTable([["You got away but you dropped " + str(amnt) + " bags of " + drug.capitalize() + " while running!!"]]).table)
                            else:
                                print(SingleTable([["You got away!"]]).table)
                            input("Press ENTER to Continue")
                            break
                elif aout == 2:
                    if 1 == randint(1,6):
                        cops -= 1
                        if cops == 0:
                            drug = choice(["cocaine", "heroin", "acid", "weed", "speed", "ludes"])
                            pdrug = player.get_amt(drug)
                            if pdrug > 0:
                                amnt = randint(1, 10)
                                pdrug -= amnt
                                clear()
                                print(SingleTable([["You got away but you dropped " + str(amnt) + " bags of " + drug.capitalize() + " while running!!"]]).table)
                            else:
                                print(SingleTable([["You got away!"]]).table)
                            input("Press ENTER to Continue")
                            break
                        clear()
                        print(SingleTable([["You took one of them out!"]]).table)
                    else:
                        player.health -= 1
                        clear()
                        print(SingleTable([["You got hit by one of their shots and lost some health!"]]).table)
        else:
            while True:
                print(SingleTable([["Press ENTER to Try and Run"], ["HP: " + str(player.health) + "/ 20"]]).table)
                input()
                if 1 == randint(1,3):
                    drug = choice(["cocaine", "heroin", "acid", "weed", "speed", "ludes"])
                    pdrug = player.get_amt(drug)
                    if pdrug > 0:
                        amnt = randint(1, 10)
                        pdrug -= amnt
                        clear()
                        print(SingleTable([["You got away but you dropped " + str(amnt) + " bags of " + drug.capitalize() + " while running!!"]]).table)
                    else:
                        print(SingleTable([["You got away!"]]).table)
                    input("Press ENTER to Continue")
                    break
                else:
                    player.health -= 1
                    clear()
                    print(SingleTable([["You got hit by one of their shots and lost some health!"]]).table)
            clear()
            print(SingleTable([["You got away from the pigs!"]]).table)
            input("Press ENTER to Continue")


def ask_bank(player):
    clear()
    while True:
        print(SingleTable([['Would you like to visit the bank?']]).table)
        ans = input("\n> ")
        aout = check_ans_yn(ans)
        if aout == 1:
            clear()
            visit_bank(player)
            break
        elif aout == 2:
            clear()
            break

def ask_loan_shark(player):
    clear()
    while True:
        print(SingleTable([['Would you like to visit the loan shark?']]).table)
        ans = input("\n> ")
        aout = check_ans_yn(ans)
        if aout == 1:
            clear()
            visit_loan_shark(player)
            break
        elif aout == 2:
            clear()
            break

def ask_stash(player):
    clear()
    while True:
        print(SingleTable([['Would you like to stash any drugs?']]).table)
        ans = input("\n> ")
        aout = check_ans_yn(ans)
        if aout == 1:
            clear()
            visit_stash(player)
            break
        elif aout == 2:
            clear()
            break

def visit_stash(player):
    stashes = ["cocaine", "heroin", "acid", "weed", "speed", "ludes"]
    for stash in stashes:
        clear()
        while True:
            print(SingleTable([['How much ' + stash + ' would you like to deposit?'], ['Stash: ' + str(getattr(player.stash, stash)) + ' | Coat: ' + str(getattr(player, stash))]]).table)
            try:
                ans = int(input("\n> "))
                if ans == 0:
                    break
                else:
                    if player.stash.can_transfer(stash, ans):
                        player.stash.transfer(stash, ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)
        while True:
            print(SingleTable([['How much ' + stash + ' would you like to take out?'], ['Stash: ' + str(getattr(player.stash, stash)) + ' | Coat: ' + str(getattr(player, stash))]]).table)
            try:
                ans = int(input("\n> "))
                if ans == 0:
                    break
                else:
                    if player.stash.can_withdraw(stash, ans):
                        player.stash.withdraw(stash, ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much in your stash!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)

def visit_bank(player):
    clear()
    if player.money > 0:
        while True:
            print(SingleTable([['How much would you like to deposit?'], ['Bank: ' + str(player.bank.balance) + ' | Wallet: ' + str(player.money)]]).table)
            try:
                ans = input("\n> ")
                if ans.lower() == "h" or ans.lower() == "half":
                    if player.bank.check_can_dep(int(round_down(player.money / 2))):
                        player.bank.deposit(int(round_down(player.money / 2)))
                        break
                ans = int(ans)
                if ans == 0:
                    break
                else:
                    if player.bank.check_can_dep(ans):
                        player.bank.deposit(ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)
    clear()
    if player.bank.balance > 0:
        while True:
            print(SingleTable([['How much would you like to withdraw?'], ['Bank: ' + str(player.bank.balance) + ' | Wallet: ' + str(player.money)]]).table)
            try:
                ans = input("\n> ")
                if ans.lower() == "a" or ans.lower() == "all":
                    player.bank.withdraw(player.bank.balance)
                    break
                if ans.lower() == "h" or ans.lower() == "half":
                    player.bank.withdraw(int(round_down(player.shark.balance / 2)))
                    break
                ans = int(ans)
                if ans == 0:
                    break
                else:
                    if player.bank.check_can_wd(ans):
                        player.bank.withdraw(ans)
                        break
                    else:
                        clear()
                        print(SingleTable([["You don't have that much!"]]).table)
            except ValueError as e:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)

def visit_loan_shark(player):
    clear()
    while True:
        print(SingleTable([['How much would you like to repay?'], ['Debt: ' + str(player.shark.balance) + ' | Wallet: ' + str(player.money)]]).table)
        try:
            ans = input("\n> ")
            if ans.lower() == "a" or ans.lower() == "all":
                if player.shark.check_can_dep(player.shark.balance):
                    player.shark.deposit(player.shark.balance)
                    break
            if ans.lower() == "h" or ans.lower() == "half":
                if player.shark.check_can_dep(int(round_down(player.shark.balance / 2))):
                    player.shark.deposit(int(round_down(player.shark.balance / 2)))
                    break
            ans = int(ans)
            if ans == 0:
                break
            elif ans > player.shark.balance:
                clear()
                print(SingleTable([["That's more than you owe!"]]).table)
            else:
                if player.shark.check_can_dep(ans):
                    player.shark.deposit(ans)
                    break
                else:
                    clear()
                    print(SingleTable([["You don't have enough!"]]).table)
        except ValueError as e:
            clear()
            print(SingleTable([["That isn't a number!"]]).table)
    clear()
    while True:
        print(SingleTable([['How much would you like to borrow?'], ['Debt: ' + str(player.shark.balance) + ' | Wallet: ' + str(player.money)]]).table)
        try:
            ans = int(input("\n> "))
            if ans == 0:
                break
            else:
                if player.shark.check_can_borrow(ans):
                    player.shark.withdraw(ans)
                    break
                else:
                    clear()
                    print(SingleTable([["You can't take more than you owe or have already!"]]).table)
        except ValueError as e:
            clear()
            print(SingleTable([["That isn't a number!"]]).table)

def upgrade_coat(p):
    clear()
    while True:
        price = randint(150, 250)
        if p.money >= price:
            print(SingleTable([["** Would you like to buy 15 more pockets for more drugs? It's $" + str(price) + " **"], ["Wallet: ", p.money]]).table)
            a = input("\n> ")
            ao = check_ans_yn(a)
            if ao == 1:
                p.max_trench += 15
                p.money -= price
                clear()
                print(SingleTable([["You bought more trench pockets for $" + str(price)]]).table)
                input("Press ENTER to Continue")
                break
            elif ao == 2:
                break
            else:
                clear()
                print(SingleTable([["Please enter Y or N"]]).table)
                break
            input("Press ENTER to Continue")
            clear()
        else:
            break

def get_mugged(p):
    clear()
    if 1 == randint(1, 8):
        clear()
        print(SingleTable([["You got mugged!! You lost " + str(p.money - int(round_down(p.money * 0.80))) + " dollars!"]]).table)
        p.money = int(round_down(p.money * 0.80))
        input("Press ENTER to Continue")
        clear()

def find_drugs(p):
    clear()
    if 1 == randint(1, 10):
        clear()
        amnt = randint(1, 10)
        drug = randint(1, 8)
        dstr = ""
        if p.len_inventory() + amnt <= p.max_trench:
            if drug == 1:
                dstr = "Cocaine"
                p.cocaine += amnt
            if drug == 2:
                dstr = "Heroin"
                p.heroin += amnt
            if drug == 3:
                dstr = "Acid"
                p.acid += amnt
            if drug == 4:
                dstr = "Weed"
                p.weed += amnt
            if drug == 5:
                dstr = "Speed"
                p.speed += amnt
            if drug == 6:
                dstr = "Ludes"
                p.ludes += amnt
            print(SingleTable([["You found " + str(amnt) + " bags of " + dstr + " on the ground... \n FUCK YEAH"]]).table)
            input("Press ENTER to Continue")

def buy_gun(p):
    clear()
    if 1 == randint(1, 5):
        clear()
        while True:
            price = randint(200, 300)
            print(SingleTable([["** Would you like to buy a gun for $" + str(price) + "? **"], ["Wallet: ", p.money]]).table)
            a = input("\n> ")
            ao = check_ans_yn(a)
            if ao == 1:
                p.guns += 1
                p.money -= price
                clear()
                print(SingleTable([["You bought a gun for $" + str(price)]]).table)
                input("Press ENTER to Continue")
                break
            elif ao == 2:
                break
            else:
                clear()
                print(SingleTable([["Please enter Y or N"]]).table)
                break
            input("Press ENTER to Continue")

def you_win(p):
    clear()
    score = int(round_down((p.bank.balance + p.money - p.shark.balance) / 10000000 * 100))
    if score > 100:
        score = 100
    print(SingleTable([["GAME OVER", "You Reached 30 Days!"]]).table)
    print(SingleTable([["Your Total Money:", p.bank.balance + p.money - p.shark.balance]]).table)
    print(SingleTable([["Your Score:", str(score) + " out of 100"]]).table)
    if score >= 0 and score <= 30:
        print(SingleTable([["Dealer Rank", "Small Time Pusha... WEAK"]]).table)
    elif score >= 31 and score <= 50:
        print(SingleTable([["Dealer Rank", "Own The Block... NOT BAD"]]).table)
    elif score >= 51 and score <= 75:
        print(SingleTable([["Dealer Rank", "Run The Town... PRETTY GOOD"]]).table)
    elif score >= 76 and score <= 99:
        print(SingleTable([["Dealer Rank", "Kingpin... GOD DAMN"]]).table)
    else:
        print(SingleTable([["Dealer Rank", "PABLO ESCOBAR... YOU ARE A GOD"]]).table)
    exit()

def buy_menu(prices, inventory_table, pricing_table, money_table, p):
    while True:
        print(SingleTable(inventory_table()).table)
        print(SingleTable(pricing_table(), title="Prices").table)
        print(SingleTable(money_table(), title="Money").table)
        print(SingleTable([["What would you like to buy?"]]).table)
        buy = input("\n> ")
        if not check_drug_inp(buy):
            clear()
            print(SingleTable([["Enter the first letter of a drug to choose!"]]).table)
        else:
            if buy[0].lower() == "c":
                drug = prices.cocaine
            elif buy[0].lower() == "h":
                drug = prices.heroin
            elif buy[0].lower() == "a":
                drug = prices.acid
            elif buy[0].lower() == "w":
                drug = prices.weed
            elif buy[0].lower() == "s":
                drug = prices.speed
            elif buy[0].lower() == "l":
                drug = prices.ludes
            price = int(round_down(drug))
            print(SingleTable([["How much would you like to buy?"], ["Max Allowed: " + str(p.get_max(check_drug_inp(buy), drug))]]).table)
            try:
                amnt = int(input("\n> "))
                if p.can_buy(price, int(amnt)):
                    p.buy(check_drug_inp(buy), amnt, price)
                    clear()
                    print(SingleTable([["You bought " + str(amnt) + " of " + check_drug_inp(buy)]]).table)
                    break
                else:
                    clear()
                    print(SingleTable([["You don't have enough money/coat space to buy that!"]]).table)
                    break
            except ValueError:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)

def sell_menu(prices, inventory_table, pricing_table, money_table, p):
    while True:
        print(SingleTable(inventory_table()).table)
        print(SingleTable(pricing_table(), title="Prices").table)
        print(SingleTable(money_table(), title="Money").table)
        print(SingleTable([["What would you like to sell?"]]).table)
        sell = input("\n> ")
        if not check_drug_inp(sell):
            clear()
            print(SingleTable([["Enter the first letter of a drug to choose!"]]).table)
        else:
            if sell[0].lower() == "c":
                drug = prices.cocaine
            elif sell[0].lower() == "h":
                drug = prices.heroin
            elif sell[0].lower() == "a":
                drug = prices.acid
            elif sell[0].lower() == "w":
                drug = prices.weed
            elif sell[0].lower() == "s":
                drug = prices.speed
            elif sell[0].lower() == "l":
                drug = prices.ludes
            price = int(round_down(drug))
            print(SingleTable([["How much would you like to sell?"], ["You Have: " + str(p.get_amt(check_drug_inp(sell)))]]).table)
            try:
                amnt = int(input("\n> "))
                if p.can_sell(amnt, check_drug_inp(sell)):
                    p.sell(check_drug_inp(sell), amnt, price)
                    clear()
                    print(SingleTable([["You sold " + str(amnt) + " of " + check_drug_inp(sell)]]).table)
                    break
                else:
                    clear()
                    print(SingleTable([["You don't have enough to sell that many!"]]).table)
                    break
            except ValueError:
                clear()
                print(SingleTable([["That isn't a number!"]]).table)

def location_menu(p):
    while True:
        clear()
        loc_index = ['Bronx', 'Ghetto', 'Central Park', 'Manhattan', 'Coney Island', 'Brooklyn']
        location_table = [
            ['1) Bronx', '2) Ghetto', '3) Central Park'],
            ['4) Manhattan', '5) Coney Island', '6) Brooklyn']
        ]
        print(SingleTable(location_table, title="Where you gonna go? Current Location: " + p.current_area).table)
        try:
            loc = int(input("\n> ")) - 1
            if loc > 5 or loc < 0:
                clear()
                print(SingleTable([["Choose a number between 1 and 6!"]]).table)
            else:
                if loc_index[loc] == p.current_area:
                    clear()
                else:
                    loc += 1
                    if loc == 1:
                        p.current_area = "Bronx"
                    if loc == 2:
                        p.current_area = "Ghetto"
                    if loc == 3:
                        p.current_area = "Central Park"
                    if loc == 4:
                        p.current_area = "Manhattan"
                    if loc == 5:
                        p.current_area = "Coney Island"
                    if loc == 6:
                        p.current_area = "Brooklyn"
                    p.days += 1
                    break
        except ValueError:
            clear()
            print(SingleTable([["That isn't a number!"]]).table)

def difficulty_screen():
    clear()
    while True:
        diff_table = [
            ["(E)asy", "(N)ormal", "(H)ard"],
        ]
        print(SingleTable(diff_table, "Difficulty Level").table)
        print("What level of difficulty would you like to play at?")
        diff = input("\n> ")
        if diff.lower() == "e":
            return 0
        elif diff.lower() == "n":
            return 1
        elif diff.lower() == "h":
            return 2
        else:
            clear()
            print(SingleTable([["Options Are: E, N, or H!!"]]).table)
            
    

def main_screen(p):
    prices = Prices(p)
    if p.days == 30:
        you_win(p)
    if not p.is_first_round:
        achoice = choice([lambda p: cops_chase(p), lambda p: buy_gun(p), lambda p: get_mugged(p), lambda p: find_drugs(p), lambda p: upgrade_coat(p)])
        achoice(p)
    if prices.action != None and not p.is_first_round:
        print(SingleTable([[prices.action]]).table)
        input("Press ENTER to Continue")
    current_area = p.current_area
    if not p.is_first_round and current_area == "Bronx":
        clear()
        ask_loan_shark(p)
        ask_bank(p)
        ask_stash(p)
    while True:
        clear()
        inventory_table = lambda : [
            ['Inventory', 'Days Left: ' + str(30 - p.days)],
            ['Cocaine: ' + str(round_down(p.cocaine)), 'Weed: ' + str(round_down(p.weed))],
            ['Heroin: ' + str(round_down(p.heroin)), 'Speed: ' + str(round_down(p.speed))],
            ['Acid: ' + str(round_down(p.acid)), 'Ludes: ' + str(round_down(p.ludes))],
        ]
        pricing_table = lambda : [
            ['Current Area: ' + p.current_area, 'Coat Space: ' + str(p.coat_space()) + " / " + str(p.max_trench)],
            ['Cocaine: ' + str(round_down(prices.cocaine)), 'Weed: ' + str(round_down(prices.weed))],
            ['Heroin: ' + str(round_down(prices.heroin)), 'Speed: ' + str(round_down(prices.speed))],
            ['Acid: ' + str(round_down(prices.acid)), 'Ludes: ' + str(round_down(prices.ludes))]
        ]
        money_table = lambda : [
            ['Debt: ' + str(int(round_down(p.shark.balance))) ,'Guns: ' + str(p.guns), 'Bank: ' + str(int(round_down(p.bank.balance))), 'Wallet: ' + str(int(round_down(p.money)))]
        ]
        print(SingleTable(inventory_table()).table)
        print(SingleTable(pricing_table(), title="Prices").table)
        print(SingleTable(money_table(), title="Money").table)
        print(SingleTable([["Are you going to (B)uy, (S)ell, or (J)et?"]]).table)
        ans = input("\n> ")
        anout = check_ans_bsj(ans)
        clear()
        if anout == 1:
            buy_menu(prices, inventory_table, pricing_table, money_table, p)
        elif anout == 2:
            sell_menu(prices, inventory_table, pricing_table, money_table, p)
        elif anout == 3:
            location_menu(p)
        else:
            clear()
            print(SingleTable([["That isn't an option. Choose B, S, or J"]]).table)
        if p.current_area != current_area:
            break
    p.is_first_round = False
    p.bank.interest()
    p.shark.interest()
    main_screen(p)