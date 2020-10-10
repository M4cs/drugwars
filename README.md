<p align="center">
  <img src="https://i.imgur.com/pvKzM9G.png">
</p>

# Drugwars
### The DOS game from the 80s re-written in Python from Scratch!

Play in your browser [Here](https://Drugwars-Online-Version.m4cs.repl.run)


# Installation

**Recommended:** Using pip

```
pip install drugwars
```

Installing from source

```
git clone https://github.com/M4cs/drugwars
cd drugwars
python3 setup.py install
drugwars
```

# How to Play

The game is played inside of your terminal and uses letters and numbers to select things and take part actions.

You start with 2000 dollars and 5500 dollars in debt to the loan shark. The goal of the game is to pay off the loan shark and get as much money as possible while avoiding cops or getting mugged. Cops can shoot at you and you have 20 hit points until you die and the game ends. 

You have 30 days to buy and sell as many drugs as possible to make a profit. Prices are randomly generated so it's all dependent on the market in the area you're at.

There are events that can happen inbetween moving areas. These can either be good for you or bad, it's all random.

You have access to a bank and stash in the Bronx which allows you to store money and drugs to keep them safe while getting mugged or caught by the cops.

**When asked yes or no questions:** Respond with `y` or `n`

**When asked to (B)uy, (S)ell, or (J)et:** Respond with `b` to buy, `s` to sell, or `j` to jet

**When asked to (R)un or (F)ight:** Respond with `r` to run, or `f` to fight

**When asked where to go:** Respond with a number `1-6`, these correspond to a location on the table

# Why did I make this?

Drugwars is a game I've been playing for a long time, well before I learned how to program. Now that I'm apt in Python I thought what the hell, why not rewrite a game I love in Python and release it. Well that's what I'm doing and here it is. Enjoy :)

# Changelog

v1.1.7

```
- Fix loan shark balance
- Fix input bugs
```

v1.1.6:

```
- Fix borrowing
```

v1.1.5:

```
- Fix actions breaking
```

v1.1.4:

```
- Remove Auto update
```

v1.1.3:

```
- Fix logic around pricing events
```

v1.1.2:

```
- Disable Actions from occuring first round
```

v1.1.1:

```
- Adds auto update check (Set DO_NOT_UPDATE to 1 to skip)
```

v1.1.0:

```
- Adds upgrade trench coat
- Changes chances of getting away from Headass
- Fixes crashing bugs
```
