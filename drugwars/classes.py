from random import randint, choice, seed, shuffle
from .helpers import round_down

class Shark():
    def __init__(self, player):
        self.player = player
        self.balance = 5500

    def interest(self):
        self.balance = int(round_down(self.balance * 1.08))

    def check_can_borrow(self, amount):
        if self.balance == 0 and amount <= int(round_down(self.player.money)):
            return True
        else:
            if amount <= int(round_down(self.balance)) and amount <= int(round_down(self.player.money)):
                return True
            else:
                return False
    
    def check_can_dep(self, amount):
        if amount <= self.player.money:
            return True
        else:
            return False

    def deposit(self, amount):
        self.player.money -= amount
        self.balance -= amount
    
    def withdraw(self, amount):
        self.player.money += amount
        self.balance += amount

class Bank:
    def __init__(self, player):
        self.player = player
        self.balance = 0

    def interest(self):
        self.balance = int(round_down(self.balance * 1.05))

    def deposit(self, amount):
        self.player.money -= amount
        self.balance += amount
    
    def withdraw(self, amount):
        self.player.money += amount
        self.balance -= amount

    def check_can_wd(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False
    
    def check_can_dep(self, amount):
        if amount <= self.player.money:
            return True
        else:
            return False

class Stash:
    def __init__(self, player):
        self.player = player
        self.cocaine = 0
        self.heroin = 0
        self.acid = 0
        self.weed = 0
        self.speed = 0
        self.ludes = 0

    def transfer(self, drug, amount):
        if drug == "cocaine":
            self.cocaine += amount
            self.player.cocaine -= amount
        elif drug == "heroin":
            self.heroin += amount
            self.player.heroin -= amount
        elif drug == "acid":
            self.acid += amount
            self.player.acid -= amount
        elif drug == "weed":
            self.weed += amount
            self.player.weed -= amount
        elif drug == "speed":
            self.speed += amount
            self.player.speed -= amount
        elif drug == "ludes":
            self.ludes += amount
            self.player.ludes -= amount
    
    def can_transfer(self, drug, amount):
        if drug == "cocaine":
            return self.player.cocaine >= amount
        elif drug == "heroin":
            return self.player.heroin >= amount
        elif drug == "acid":
            return self.player.acid >= amount
        elif drug == "weed":
            return self.player.weed >= amount
        elif drug == "speed":
            return self.player.speed >= amount
        elif drug == "ludes":
            return self.player.ludes >= amount

class Player:
    def __init__(self):
        self.is_first_round = True
        self.money = 2000
        self.guns = 0
        self.days = 0
        self.health = 20
        self.max_trench = 100
        self.cocaine = 0
        self.heroin = 0
        self.acid = 0
        self.weed = 0
        self.speed = 0
        self.ludes = 0
        self.bank = Bank(self)
        self.stash = Stash(self)
        self.shark = Shark(self)
        self.current_area = "Bronx"
    
    def buy(self, drug, amount, price):
        if drug == "cocaine":
            self.cocaine += amount
        elif drug == "heroin":
            self.heroin += amount
        elif drug == "acid":
            self.acid += amount
        elif drug == "weed":
            self.weed += amount
        elif drug == "speed":
            self.speed += amount
        elif drug == "ludes":
            self.ludes += amount
        self.money -= (amount * price)

    def len_inventory(self):
        return (self.cocaine + self.heroin + self.acid + self.weed + self.speed + self.ludes)

    def coat_space(self):
        return 100 - (self.cocaine + self.heroin + self.acid + self.weed + self.speed + self.ludes)
    
    def get_max(self, drug, price):
        return int(self.money / price)

    def can_buy(self, price, amount):
        return self.money >= (price * amount) and (self.len_inventory() + amount) <= self.max_trench

    def can_sell(self, amount, drug):
        if drug == "cocaine":
            return self.cocaine - amount >= 0
        elif drug == "heroin":
            return self.heroin - amount >= 0
        elif drug == "acid":
            return self.acid - amount >= 0
        elif drug == "weed":
            return self.weed - amount >= 0
        elif drug == "speed":
            return self.speed - amount >= 0
        elif drug == "ludes":
            return self.ludes - amount >= 0

    def get_amt(self, drug):
        if drug == "cocaine":
            return self.cocaine
        elif drug == "heroin":
            return self.heroin
        elif drug == "acid":
            return self.acid
        elif drug == "weed":
            return self.weed
        elif drug == "speed":
            return self.speed
        elif drug == "ludes":
            return self.ludes

    def sell(self, drug, amount, price):
        if drug == "cocaine":
            self.cocaine -= amount
        elif drug == "heroin":
            self.heroin -= amount
        elif drug == "acid":
            self.acid -= amount
        elif drug == "weed":
            self.weed -= amount
        elif drug == "speed":
            self.speed -= amount
        elif drug == "ludes":
            self.ludes -= amount
        self.money += (amount * price)

class Prices:
    def __init__(self, player):
        seed(randint(-10000, 10000))
        self.player = player
        self.cocaine = randint(15000, 29999)
        self.heroin = randint(5000, 13999)
        self.acid = randint(1000, 4999)
        self.weed = randint(300, 899)
        self.speed = randint(90, 249)
        self.ludes = randint(10, 89)
        self.actions = []
        events = [
            lambda self: self.cops_bust_cocaine(),
            lambda self: self.addicts_buy_coke(),
            lambda self: self.cops_bust_heroin(),
            lambda self: self.addicts_buy_herion(),
            lambda self: self.cheap_acid(),
            lambda self: self.cheap_cocaine(),
            lambda self: self.cheap_heroin(),
            lambda self: self.cheap_ludes(),
            lambda self: self.cheap_speed(),
            lambda self: self.cheap_weed(),
        ]
        shuffle(events)
        self.action = None
        self.has_done_action = False
        if not self.player.is_first_round:
            for a in events:
                if self.has_done_action:
                    break
                else:
                    a(self)
        if len(self.actions) > 0:
            self.action = self.actions[0]
    
    def cops_bust_cocaine(self):
        if 1 == randint(1, 35):
            self.cocaine *= 2
            self.actions.append("** Cops raided a coke house! Prices are rising!!! **")

    def addicts_buy_coke(self):
        if 1 == randint(1, 35):
            self.cocaine *= 4
            self.actions.append("** Cokeheads everywhere are ready to pay. Prices are skyrocketing!! **")

    def cops_bust_heroin(self):
        if 1 == randint(1, 25):
            self.heroin *= 2
            self.actions.append("** Cops raided a heroin kingpin's warehouse! Prices are rising!!! **")

    def addicts_buy_herion(self):
        if 1 == randint(1, 35):
            self.heroin *= 4
            self.actions.append("** Heroin junkies everywhere need their fix. Prices are skyrocketing!! **")
    
    def cheap_acid(self):
        if 1 == randint(1, 25):
            self.acid /= 4
            self.actions.append("** Somebody found a reliable method for making acid. It's super cheap! **")
    
    def cheap_ludes(self):
        if 1 == randint(1, 20):
            self.ludes /= 4
            self.actions.append("** The pharmacy got robbed! Ludes are extremely cheap **")
    
    def cheap_weed(self):
        if 1 == randint(1, 20):
            self.weed /= 4
            self.actions.append("** Hempfest time! Weed is basically being handed out! **")

    def cheap_heroin(self):
        if 1 == randint(1, 35):
            self.heroin /= 4
            self.actions.append("** Heroin markets are flooded! Prices have dropped!! **")

    def cheap_cocaine(self):
        if 1 == randint(1, 40):
            self.cocaine /= 4
            self.actions.append("** Holy shit! You found a time machine to the 80s. Coke is cheap! **")

    def cheap_speed(self):
        if 1 == randint(1, 20):
            self.speed /= 4
            self.actions.append("** Speed markets are flooded! Prices are dropping! **")