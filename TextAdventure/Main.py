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
import pickle


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
    savePoints = ["Autosave"]
    with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
        savePoints = pickle.load(loadAllHandler)
    autoSave = 0
    playerName = ""
    dataSaveList = [autoSave, savePoints, playerName, "", "", 0.00, 0, [], {}]   
    Intro.Intro()
    # sleep(2)
    dataSaveList = MainMenu(dataSaveList)    
    if dataSaveList[2] == '':
       dataSaveList = Start(dataSaveList)
    IngameMenu(dataSaveList)

def Save(dataSaveList):    
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    if dataSaveList[0] == 0:    
        saveFileAuto = dataSaveList[1][0]
        with open(f"SaveFile_{saveFileAuto}.pickle", 'wb') as autoSaveHandler:
            pickle.dump(dataSaveList, autoSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
            dataSaveList[1][0] = saveFileAuto                                                  #Add AutoSave to savePoints[0]        
    elif dataSaveList[0] == 1:
        while True:
            userInput = input(f"\n(1) Save\t(2) Return\n")
            if userInput == "1":      
                userInputFileName = input("\nSet a name for the savefile:\t\t(0) Abort\n")
                if userInputFileName != "0":    
                    with open(f'SaveFile_{userInputFileName}.pickle', 'wb') as manSaveHandler:
                        pickle.dump(dataSaveList, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
                        dataSaveList[1].append(userInputFileName)
                    with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                        pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                        
                    break
                else:
                    print("Couldn't understand you?\n") 
                    continue
            elif userInput == "2":
                break
            else:
                print("\nCouldn't understand you?\n")
                continue

    return dataSaveList


def Load(dataSaveList):
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    saveFileID = 1
    for i in range(0, len(dataSaveList[1]-1)):
        print(f"{saveFileID} - {dataSaveList[i]}")        
    userInputNumber = input("Choose number to load: ")        
    with open(f'SaveFile_{dataSaveList[1]([userInputNumber]-1)}.pickle', 'rb') as loadHandler: 
        dataSaveList = pickle.load(loadHandler)
    
    return dataSaveList

### MainMENU: START/EXIT
def MainMenu(dataSaveList): 
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]      

    while True:
        if dataSaveList[2] == "" and dataSaveList[0] == 0:
            userInput = input('\n(1) New Game\t(2) Help\t(3) Exit\n')
            os.system('cls')
            match userInput:
                case "1": break                                          
                case "2": Helpfile.HelpTxt()
                case "3": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        elif dataSaveList[2] == "":
            userInput = input('\n(1) New Game\t(2) Load\t(3) Help\t(4) Exit\n')
            os.system('cls')
            match userInput:
                case "1": break
                case "2": dataSaveList = Load(dataSaveList)                                        
                case "3": Helpfile.HelpTxt()
                case "4": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        else:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Load\t(4) Save\t(5) Help\t(6) Exit\n')
            os.system('cls')
            match userInput:
                case "1": dataSaveList[2] = ""; break
                case "2": break
                case "3": dataSaveList = Load(dataSaveList) 
                case "4": dataSaveList = Save(
                    dataSaveList)                        
                case "5": Helpfile.HelpTxt()
                case "6": exit(f"\nGoodbye {dataSaveList[2]}")
                case _: print("\nCouldn't understand you?!")
        # sleep(2)
        dataSaveList[0] = 1
    return dataSaveList       



### PICK A NAME, GET FIRST LOCATION (One Timer)
def Start(dataSaveList):
   #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]    
    playerName = dataSaveList[2]
    startLocation = dataSaveList[3]
    location = dataSaveList[4]
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
    dataSaveList[2] = playerName
    dataSaveList[3] = startLocation
    dataSaveList[4] = location

    return dataSaveList


# MAIN GAME LOOP --- MAIN DEKLARATIONS AND INITIALISATIONS!#

def IngameMenu(dataSaveList):
   #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    playerName = dataSaveList[2]
    playerInventoryMoney = 5.00
    startLocation = dataSaveList[3]
    location = dataSaveList[4]
    dataSaveList[5] = playerInventoryMoney 
    playerStatPoints = 0
    dataSaveList[6] = playerStatPoints
    playerStats = [1, 15, 15, 2, 1, 0.00] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    dataSaveList[7] = playerStats
    itemsDict = {}    
    itemsDict = Items.Items(itemsDict)
    dataSaveList[8] = itemsDict

    while True:  # >>>>>>>>>> MAIN GAME LOOP <<<<<<<<<<<
        itemAddStats = []
        itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict) 
        playerStats, playerStatPoints, itemsDict = Stats.LevelUp(playerStats, playerStatPoints, playerName, itemsDict)
        dataSaveList[0] = 0
        dataSaveList = Save(dataSaveList)
        dataSaveList[0] = 1

        userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(4) Exit to main menu\n")
        os.system('cls')
        match userInput:
            case "1": startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Move(
                    startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)

            case "2": itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)

            case "3": playerStats, playerStatPoints = Stats.StatMenu(
                    playerStats, playerStatPoints, playerName, itemsDict)

            case "4": dataSaveList = MainMenu(dataSaveList)
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
