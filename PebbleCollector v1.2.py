## Made by a Kid (ﾉ◕ヮ◕)ﾉ*:・ﾟ✧
## July 9th, 2019
from tkinter import *
import time

DoubleClicksCost = 50
AutoClickerCost = 75
click = 0
mult = 1
autoclickers = 0

    
master = Tk()

def uiPrint():
    info()
    print("")
    print ("Found Pebbles!")
    print(click)

def info():
    print("You can buy a two times larger Pebble scoop for " + str(DoubleClicksCost) + " Pebbles!")
    print("You can buy an Auto Clicker for " + str(AutoClickerCost) + " Pebbles!")

def blankLine():
    for i in range(0):
        print("")

def purchaseDoubleClicksCommand():
    global click
    global mult
    global DoubleClicksCost
    if click < DoubleClicksCost:
        print("Not enough pebbles!")
        blankLine()
    elif click >= DoubleClicksCost:
        mult = mult*2
        click = click - DoubleClicksCost
        print("Pebble Scoop Purchased!")
        DoubleClicksCost = DoubleClicksCost * 2
        blankLine()
        
def purchaseAutoClickerCommand():
    global click
    global mult
    global AutoClickerCost
    global autoclickers
    if click < AutoClickerCost:
        print("Not enough pebbles!")
        blankLine()
    elif click >= AutoClickerCost:
        click = click - AutoClickerCost
        print("AutoClicker Purchased!")
        AutoClickerCost = AutoClickerCost * 2
        autoclickers += 1
        blankLine()

def autoclick():
    global master
    global click
    global autoclickers
    click += autoclickers
    master.after(1000,autoclick)

autoclick()

def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()

    if click == 100:
        print('''Achievement Unlocked: Pebble!
        BONUS 100 Pebbles!''')
        click += 100
        
    elif click == 400:
        print ('''Achievement Unlocked: Rock!
        BONUS 300 Pebbles!''')
        click += 300
     
    elif click == 1500:
        print ('''Achievement Unlocked: Boulder!
        Quadrebble Pebbles!''')
        mult = mult * 4
        
    elif click == 3000:
        print ('''Achievement Unlocked:  Mountain!
        Octubble Pebbles!!!!!!!!!''')
        mult = mult * 8
        
    elif click == 6000:
        print ('''Achievement Unlocked:  Mountain Range!
        SO MANY PEBBLES!!!!!!!!!!!!!!''')
        mult = mult * 16
        
    elif click == 100000:
        print ('''Achievement Unlocked:  Planet!
        If you are still playing , you deserve a reward... 100 times the amount of PEBBLES!!!!!!!!!!!!!!!''')
        mult = mult * 16
        
    elif click == 1000000:
        print ('''Achievement Unlocked:  Rock Star!
        Well, now you have technically beat the game...  Have fun getting to Infinity!''')
        mult = mult * 100000000000000000000000000

    
mainClickButton = Button(master, text='''Pebble!
•''', command = buttonCommand)
mainClickButton.pack()

purchaseDoubleClickButton = Button(master, text='''Purchase Pebble Scoop
ᕕ( ᐛ )ᕗ''', command = purchaseDoubleClicksCommand)
purchaseDoubleClickButton.pack()

purchaseAutoClickerButton = Button(master, text='''Purchase Auto Clicker
･｡ﾟ[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]｡ﾟ.*''', command = purchaseAutoClickerCommand)
purchaseAutoClickerButton.pack()

master.title("Pebble Collector")
master.geometry("%sx%s+%s+%s" % (200,70,512,512))
mainloop()

