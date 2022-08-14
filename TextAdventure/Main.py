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
# from time import sleep
import Intro
import Encounter
import Stats
import Inventory
import Items
import os


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



### Main Game
def Main():
    playerName = ''
    #Intro.Intro()
    # sleep(2)
    MainMenu(playerName)    
    if playerName == '':
       playerName, startLocation, location = Start()
    IngameMenu(playerName, startLocation, location)




### MainMENU: START/EXIT
def MainMenu(playerName):
        while True:
            if playerName == "":
                userInput = input('\n(1) New Game\t(2) Help\t(3) Exit\n')
                os.system('cls')
            else:
                userInput = input('\n(1) Continue\t(2) Help\t(3) Exit\n')
                os.system('cls')

            match userInput:
                case "1": break                        
                case "2": Helpfile.HelpTxt()
                case "3": exit(f"\nGoodbye {playerName}")
                case _: print("\nCouldn't understand you?!")
            # sleep(2)   



### PICK A NAME, GET FIRST LOCATION (One Timer)
def Start():
    _startLocations = ["a small homestead", "a comfy cabin", "a small tent", "a cave"]
    # sleep(2)
    startLocation = _startLocations[random.randint(0,len(_startLocations)-1)]
    location = startLocation ### FOR TESTING CHANGE THIS: ## CHANGE FROM "location = startLocation" TO "location = "the flatlands"  ONLY FOR TESTING!!!!!!
    while True:
        playerName = input("\nWhat's your name adventurer?\n").capitalize()
        os.system('cls')
        if playerName.isdigit():
            print ("Enter a real warrior name you're not a number! ")
            # sleep(2)
            continue
        elif playerName == "":
            print("Hey, get a name! You are not 'nothing'!")
            # sleep(2)
            continue
        else:
            break
    # sleep(1)
    print(f"\nWelcome to your first adventure {playerName}!")
    # sleep(2)
    print(f"\nYou wake up in {location}")
    # sleep(2)

    return playerName, startLocation, location


# MAIN GAME LOOP --- MAIN DEKLARATIONS AND INITIALISATIONS!#

def IngameMenu(playerName, startLocation, location):
    playerInventoryMoney = 5.00
    playerStatPoints = 0
    playerStats = [1, 15, 15, 2, 1, 0.00] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
    itemsDict = {}

    itemsDict = Items.itemsDict(itemsDict)

    while True:  # >>>>>>>>>> MAIN GAME LOOP <<<<<<<<<<<
        itemAddStats = []
        itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict) 
        playerStats, playerStatPoints, itemsDict = Stats.LevelUp(playerStats, playerStatPoints, playerName, itemsDict)
        userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(4) Exit to main menu\n")
        os.system('cls')
        match userInput:
            case "1": startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Move(
                    startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)

            case "2": itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)

            case "3": playerStats, playerStatPoints = Stats.StatMenu(
                    playerStats, playerStatPoints, playerName, itemsDict)

            case "4": MainMenu(playerName)
            case _: print("\nCouldn't understand you?!")
        

### Move() -> World()
def Move(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
    _temp = "x"
    print(f"\nLocation: {location}")
    # sleep(1)
    while _temp == "x":
        userInput = input("\nWhich direction do you want to go? \n'north' 'east' 'south' 'west'\t\t(0) Abort\n").lower()
        if userInput == "0":
            return startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict
        os.system('cls')
        direction = userInput[:1]
        _temp = World(startLocation, location, direction)        
        # sleep(2)        
        if _temp != "x":
            location = _temp
            break        
    print(f"\nYou moved to {location}\n")       
    # sleep(2)
    
    location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Encounter.Encounter(
    startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)

    playerStats, playerStatPoints, itemsDict = Stats.LevelUp(playerStats, playerStatPoints, playerName, itemsDict)

    return startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict


### Move() <- World()
def World(startLocation, location, direction): 
   
    compass = ["n","e","s","w"] 

    worldmap = {
    # Location                    North        East       South        West
    startLocation   :   [  "the forrest",       0,          0,          0           ],
    "the town"      :   [           0,   "the flatlands",   0,          0           ],
    "the flatlands" :   [           0,    "the forrest",    0,       "the town"     ],
    "the forrest"   :   ["the mountains","the islands",startLocation,"the flatlands"],
    "the mountains" :   [   "the castle",       0,    "the forrest",    0           ],
    "the castle"    :   [           0,          0,    "the mountains",  0           ],
    "the islands"   :   [           0,          0,          0,       "the forrest"  ]
    }

    for i in range(0,4):
        if compass[i] == direction:
            if worldmap[location][i] != 0:
                return worldmap[location][i]
        
    
    print("\nYou can't move there, try a different direction!")
    return "x"  
        
                                        

Main()
