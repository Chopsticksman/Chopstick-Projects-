from tkinter import *
import time

master = Tk()

def uiPrint():
    info()
    print("")
    print ("Found Pebbles!")
    print(click)

def info():
    print("You can buy Double Pebbles for Pebbles!")


info()
DoubleClicksCost = 50
click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(0):
        print("")

def purchaseDoubleClicksCommand():
    global click
    global mult
    global DoubleClicksCost    
    if click%2== 0:
        if click < DoubleClicksCost:
            print("Not enough pebbles!")
            blankLine()
        elif click >= DoubleClicksCost:
            mult = mult*2
            click = click - DoubleClicksCost
            print("Double Clicks Purchased!")
            DoubleClicksCost = DoubleClicksCost * 2
            blankLine()
    else:
        print("Please acquire an even number of pebbles.")
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

purchaseDoubleClickButton = Button(master, text='''Purchase Pebble Collector
ᕕ( ᐛ )ᕗ''', command = purchaseDoubleClicksCommand)
purchaseDoubleClickButton.pack()

master.title("Pebble Collector")
master.geometry("%sx%s+%s+%s" % (200,70,512,512))
mainloop()

