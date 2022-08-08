##################################
# Textadventure                  #
#                                # 
# Author: Nils aka Psychokater   #
# CoAuthor: Samo aka Samoooooooo #
#                                #
################################## 

#----------------------------
#           ToDo:  
#----------------------------
#
# -Encounter (Minor Improvements) (Nils) --- DONE
# -Inventory, Items, Merchant (Samo)
# -Stats (Fix HP Bug, add Max HP, print HP in Stats and after fights)(Nils) --- DONE
# -Encounter (add Monsters, add Merchant/Wanderer, edit Chances for Encounter)      

import random
import Helpfile
from time import sleep
import Intro
import Encounter
import Stats


# MAP:
#
#                                       The Castle
#     N                                     I
#   W + E                                   I
#     S                                 The Mountains
#                                           I        
#                                           I
#        The Town --- The Flatlands --- The Forrest --- The Islands
#                                           I
#                                           I
#                                      Starting Area
#
#

playerStatPoints = 0
playerInventoryMoney = 10
merchantInventoryMoney = 200
playerInventoryItems = {"Butterknife":[1, 0, 0, 2], "Apple":[0, 0, 2, 1], "Hat":[0, 2, 0, 2]} # {Item:[ATK,DEF,HEAL,VALUE]}
merchantInventoryItems = {"testitem":[1, 2, 3, 4]} ### maybe Random??!! Maybe add a counter for "Days" which increment with every Move()? More Days = More/Better Items (Monster Loot and Merchant)
playerName = ''
location = ''
playerStats = [1, 20, 20, 4, 5, 0] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP



### Main Game
def Main():
    global playerName
    #Intro.Intro()
    sleep(2)
    MainMenu()    
    if playerName == '':
       Start()
    IngameMenu()




### MainMENU: START/EXIT
def MainMenu():
        while True:

            userInput = int(input('\n(1) Play\t(2) Help\t(3) Exit\n'))
            match userInput:
                case 1: break                        
                case 2: Helpfile.HelpTxt()
                case 3: exit(f"\nGoodbye {playerName}")
                case _: print("\nCouldn't understand you?!")
            sleep(2)   



### PICK A NAME, GET FIRST LOCATION (One Timer)
def Start():
    global location
    global playerName
    global startLocation
    _startLocations = ["a small homestead", "a comfy cabin", "a small tent", "a cave"]
    sleep(2)
    startLocation = _startLocations[random.randint(0,len(_startLocations)-1)]
    location = startLocation
    while True:
        playerName = input("\nWhat's your name adventurer?\n").capitalize()
        if playerName.isdigit():
            print ("Enter a real warrior name you're not a number! ")
            sleep(2)
            continue
        elif playerName == "":
            print("Hey, get a name! You are not 'nothing'!")
            sleep(2)
            continue
        else:
            break
    sleep(1)
    print(f"\nWelcome to your first adventure {playerName}!")
    sleep(2)
    print(f"\nYou wake up in {location}")
    sleep(2)


### overall ingameMenu #############################
def IngameMenu():
    while True:
        userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(4) Exit to main menu\n")
        match userInput:
            case "1": Move()
            case "2": InventoryMenu()
            case "3": playerStatPoints, playerStats = Stats.StatMenu(playerStatPoints, playerStats)
            case "4": MainMenu()
            case _: print("\nCouldn't understand you?!")



def InventoryMenu():
    global playerInventoryItems
    print(f"\nInventory: {playerInventoryItems}")
    sleep(2)       


### Move() -> World()
def Move():
    temp = "x"
    global location
    print(f"\nLocation: {location}")
    sleep(2)
    while temp == "x":
        userInput = input("\nWhich direction do you want to go? \n'north' 'east' 'south' 'west'\n").lower()
        direction = userInput[:1]
        temp = World(location, direction)        
        sleep(2)        
        if temp != "x":
            location = temp
            break        
    print(f"\nYou moved to {location}\n")       
    sleep(2)
    EncounterSelection()
    if location == "the town":
        #EncounterMerchant()
        pass
    playerStats, playerStatPoints = Stats.LevelUp(playerStats, playerStatPoints)


### MOVE() -> WORLD()
def World(_location, _direction): 
   
    worldmap = [startLocation,"the town","the flatlands","the forrest","the islands","the mountains","the castle"]
    
    for i in range(0,7):
        if worldmap[i] == _location:
            break
 
    if _direction == "n":
        if i == 0:
            i += 3
        elif i == 3:
            i += 2
        elif i == 5:
            i += 1
        else:
            print("\nYou can't move there, try a different direction!")
            return "x"
      
    elif _direction == "e":
        if i == 1 or i == 2 or i == 3:
            i +=1
        else:
            print("\nYou can't move there, try a different direction!")
            return "x"

    elif _direction == "s":
        if i == 5:
            i -= 2
        elif i == 6:
            i -= 3
        elif i == 3:
            i -= 3
        else:
            print("\nYou can't move there, try a different direction!")  
            return "x"      
   
    elif _direction == "w":
        if i == 2 or i == 3 or i == 4:
            i -= 1
        else:
            print("\nYou can't move there, try a different direction!")
            return "x"
 
    else:
        print("\nCouldn't understand you?!")
        return "x"
    return worldmap[i]


def EncounterSelection():    
   global startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney 
   location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney = Encounter.Encounter(
    startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney, playerName)



def EncounterMerchant():
    while True:
        userInput = input(f"\nYour Inventory: {playerInventoryItems}\n(1) Buy\t(2) Sell\t(3) Return\n")
        match userInput:
            case "1": MerchantBuy()
            case "2": MerchantSell()
            case "3": break
            case _: print("\nCouldn't understand you?!")

def MerchantBuy():
    print("\nWhat do you want to buy?")
    sleep(2)
    print(f"Your Gold: {playerInventoryMoney}")
    print(f"Merchant Gold: {merchantInventoryMoney}")    
    print(merchantInventoryItems)
    print(playerInventoryItems)

    ### maybe print Inventory like this:
    ###                 ATK     DEF     HEAL     Value
    ### (1) "Item1"      2       0       0         2
    ### (2) "Item2"      0       0       4         5

    ### "Buy "Item": = Int User Input
    ### if Money >= Value: 
    ### playerInventoryMoney -= Value Item
    ### merchantInventoryMoney += Value Item
    ### playerInventoryItem += Item
    ### MerchantInventoryItem -= Item

    ### maybe Option for "equip" and "use" ?

def MerchantSell():
    print("\nWhat do you want to sell?")
    sleep(2)
    print(f"Your Gold: {playerInventoryMoney}")
    print(f"Merchant Gold: {merchantInventoryMoney}")
    print(merchantInventoryItems)
    print(playerInventoryItems)
    
    #see MerchantBuy()




Main()
