####################################
#                                  #
#     ~~~ TEXTADVENTURE ~~~        #
#                                  # 
#  Author: Nils aka Psychokater    #
#  CoAuthor: Samo aka Samoooooooo  #
#                                  #
#################################### 

#----------------------------
#           ToDo:  
#----------------------------
#
# -Encounter (Minor Improvements) (Nils) --- DONE
# -Inventory, Items, Merchant, Loot(?!) (Samo) half DONE
# -Stats (Fix HP Bug, add Max HP, print HP in Stats and after fights)(Nils) --- DONE
# -Encounter (add Monsters, add Merchant/Wanderer, edit Chances for Encounter, Chances for Gold) (Nils and Samo)     

import random
import Helpfile
from time import sleep
#import Intro
import Encounter
import Stats
import Inventory


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


merchantInventoryMoney = 200

merchantInventoryItems = {"testitem":[1, 2, 3, 4]} ### maybe Random??!! Maybe add a counter for "Days" which increment with every Move()? More Days = More/Better Items (Monster Loot and Merchant)


### Main Game
def Main():
    playerName = ''
    #Intro.Intro()
    sleep(2)
    MainMenu(playerName)    
    if playerName == '':
       playerName, startLocation, location = Start()
    IngameMenu(playerName, startLocation, location)




### MainMENU: START/EXIT
def MainMenu(playerName):
        while True:
            if playerName == "":
                userInput = input('\n(1) New Game\t(2) Help\t(3) Exit\n')
            else:
                userInput = input('\n(1) Continue\t(2) Help\t(3) Exit\n')

            match userInput:
                case "1": break                        
                case "2": Helpfile.HelpTxt()
                case "3": exit(f"\nGoodbye {playerName}")
                case _: print("\nCouldn't understand you?!")
            sleep(2)   



### PICK A NAME, GET FIRST LOCATION (One Timer)
def Start():
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

    return playerName, startLocation, location


# MAIN GAME LOOP --- MAIN DEKLARATIONS AND INITIALISATIONS!#

def IngameMenu(playerName, startLocation, location):
    playerInventoryMoney = 0.00
    playerStatPoints = 1
    playerStats = [1, 20, 20, 4, 5, 0.00] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP

    itemsDict = {
    #      0   1        2          3     4       5      6         7        8       9       10     11
    #                            atk    def     hp      val      qnt      qnt      ID      ID_ON  use/eq                        Quantity Merchant resets every lvlUp (qnt Max / 2 - qnt P)
    #                                                            Max       P                                                    qnt Max = Max qnt in Game
    1001:[(0),(0),"Apple    ",   (0),   (0),    (4),    (1),    (100),    (5),    (10),   (10),  (0)],                          # ID (row 9 and 10)
    1002:[(0),(0),"Fish",        (9),   (8),    (1),    (6),     (10),    (5),    (1),    (1)    (0)],                          # 1, 2, 3 = Merchant Inv lvl 5, 10, 20+
    1003:[(0),(0),"Cabbage",     (9),   (8),    (1),    (6),      (2),    (0),    (4),    (4),   (0)],                          # 4, 5, 6 = Wizard Inv lvl 5, 10, 20+   
    1004:[(0),(0),"Sword",       (9),   (8),    (1),    (6),      (4),    (0),    (6),    (0),   (2)],                          # 7, 8, 9 = Loot Inv lvl 5, 10, 20+                          
    1005:[(0),(0),"Shield",      (9),   (8),    (0),    (6),      (4),    (0),    (3),    (0),   (2)],                          # 
    1006:[(0),(0),"10 HP Potion",(5),   (8),    (1),    (6),      (2),    (0),    (8),    (0),   (0)],                          # use = 0, equip = 1, equipped = 2
    1007:[(0),(0),"20 HP Potion",(9),   (8),    (0),    (6),      (2),    (1),    (10),   (10),  (0)],                          # 
    1008:[(0),(0),"ItemName7",   (9),   (8),    (0),    (6),      (2),    (0),    (11),   (0),   (0)],                          # IF lvl "x" Then itemsDict(10) = itemsDict(9)
    1009:[(0),(0),"ItemName8",   (9),   (8),    (1),    (6),      (2),    (0),    (12),   (0),   (1)],                          # IF itemsDict(10)  = Value = Item is in game!
    1010:[(0),(0),"ItemName9",   (9),   (8),    (1),    (6),      (2),    (0),    (10),   (10),  (1)]}                          # IF itemsDict(10)  = 0 = Item is NOT in game!
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON 11 used

    while True:  # >>>>>>>>>> MAIN GAME LOOP <<<<<<<<<<<
        playerStats, playerStatPoints = Stats.LevelUp(playerStats, playerStatPoints, playerName)
        userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(4) Exit to main menu\n")
        match userInput:
            case "1": startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Move(
                    startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)

            case "2": itemsDict = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney)

            case "3": playerStats, playerStatPoints = Stats.StatMenu(
                    playerStats, playerStatPoints, playerName)

            case "4": MainMenu(playerName)
            case _: print("\nCouldn't understand you?!")
        

### Move() -> World()
def Move(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
    _temp = "x"
    print(f"\nLocation: {location}")
    sleep(1)
    while _temp == "x":
        userInput = input("\nWhich direction do you want to go? \n'north' 'east' 'south' 'west'\n").lower()
        direction = userInput[:1]
        _temp = World(startLocation, location, direction)        
        sleep(2)        
        if _temp != "x":
            location = _temp
            break        
    print(f"\nYou moved to {location}\n")       
    sleep(2)
    
    location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Encounter.Encounter(
    startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)

    playerStats, playerStatPoints = Stats.LevelUp(playerStats, playerStatPoints, playerName)

    return startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict


### Move() <- World()
def World(startLocation, location, direction): 
   
    worldmap = [startLocation,"the town","the flatlands","the forrest","the islands","the mountains","the castle"]
    
    for i in range(0,7):
        if worldmap[i] == location:
            break
 
    if direction == "n":
        if i == 0:
            i += 3
        elif i == 3:
            i += 2
        elif i == 5:
            i += 1
        else:
            print("\nYou can't move there, try a different direction!")
            return "x"
      
    elif direction == "e":
        if i == 1 or i == 2 or i == 3:
            i +=1
        else:
            print("\nYou can't move there, try a different direction!")
            return "x"

    elif direction == "s":
        if i == 5:
            i -= 2
        elif i == 6:
            i -= 3
        elif i == 3:
            i -= 3
        else:
            print("\nYou can't move there, try a different direction!")  
            return "x"      
   
    elif direction == "w":
        if i == 2 or i == 3 or i == 4:
            i -= 1
        else:
            print("\nYou can't move there, try a different direction!")
            return "x"
 
    else:
        print("\nCouldn't understand you?!")
        return "x"
    return worldmap[i]



Main()
