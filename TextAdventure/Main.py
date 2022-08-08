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
# -Inventory, Items, Merchant, Loot(?!) (Samo)
# -Stats (Fix HP Bug, add Max HP, print HP in Stats and after fights)(Nils) --- DONE
# -Encounter (add Monsters, add Merchant/Wanderer, edit Chances for Encounter, Chances for Gold) (Nils)     

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


### overall ingameMenu #############################
def IngameMenu(playerName, startLocation, location):
    playerStatPoints = 0
    playerStats = [1, 20, 20, 4, 5, 0] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    playerInventoryMoney = 10
    playerInventoryItems = {"Make a":[1, 1, 1, 1, 1], "Fuckin":[1, 1, 1, 1, 1], "Inventory!!!":[1, 1, 1, 1, 1]} # Items =: 1 ATK, 2 DEF, 3 HEAL, 4 VALUE, 5 QUANTITY

    while True:
        userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(4) Exit to main menu\n")
        match userInput:
            case "1": startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney = Move(
                    startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney, playerName)

            case "2": playerInventoryItems, playerInventoryMoney = Inventory.InventoryMenu(
                    playerInventoryItems, playerInventoryMoney, playerName)

            case "3": playerStats, playerStatPoints = Stats.StatMenu(
                    playerStats, playerStatPoints, playerName)

            case "4": MainMenu(playerName)
            case _: print("\nCouldn't understand you?!")



    


### Move() -> World()
def Move(startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney, playerName):
    _temp = "x"
    print(f"\nLocation: {location}")
    sleep(2)
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
    
    location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney = Encounter.Encounter(
    startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney, playerName)
    
    if location == "the town":
        #Inventory.EncounterMerchant()
        pass
    playerStats, playerStatPoints = Stats.LevelUp(playerStats, playerStatPoints, playerName)

    return startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney


### Move() -> World()
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
