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
import Intro
import Encounter
import Stats
import Inventory
import Items
import os
import pickle



#############################################################################################################################################################################
#---------------------------------------------------------------------------------- MAP -----------------------------------------------------------------------------------#
#############################################################################################################################################################################



# MAP:
#                                         
#                                                                               The Castle
#                                  N                                                I
#                                W + E                                              I
#                                  S                                            The Mountains
#                                                                                   I        
#                                                                                   I
#                                                The Town --- The Flatlands --- The Forest --- The Islands
#                                                                                   I
#                                                                                   I
#                                                                              Starting Area
#                                         
#



#############################################################################################################################################################################
#---------------------------------------------------------------------------------- MAIN -----------------------------------------------------------------------------------#
#############################################################################################################################################################################



################################################################################# MAIN GAME #################################################################################
### Main Game
def Main():
    playerName = ""
    savePoints = []
    autoSave = 0
    dataSaveList = [autoSave, savePoints, playerName, "", "", 0.00, 0, [], {}]   
    try:
        with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
            dataSaveList[1] = pickle.load(loadAllHandler)
    except FileNotFoundError:        
        with open(f'Savepoint_Status.pickle', 'wb') as manSaveHandler:
            pickle.dump(savePoints, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
    Intro.Intro()
    # sleep(2)
    dataSaveList = MainMenu(dataSaveList)    
    if dataSaveList[2] == '':
       dataSaveList = Start(dataSaveList)
    IngameMenu(dataSaveList)

################################################################################## MAIN MENU #################################################################################
### MainMENU: START/EXIT
def MainMenu(dataSaveList): 
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]      

    while True:
        if dataSaveList[2] == "" and len(dataSaveList[1]) == 0 and dataSaveList[0] == 0:
            userInput = input('\n(1) New Game\t(2) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": break                                          
                case "2": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        elif dataSaveList[2] == "" and len(dataSaveList[1]) == 1:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": break
                case "2": dataSaveList = LoadAutosave(dataSaveList); break                                        
                case "3": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        elif dataSaveList[2] == "" and len(dataSaveList[1]) > 1:
            userInput = input('\n(1) New Game\t(2) Load\t(3) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": break
                case "2": dataSaveList = Load(dataSaveList); break                                        
                case "3": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")
        
        elif dataSaveList[2] != "" and len(dataSaveList[1]) == 1:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Save\t(4) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": break
                case "2": dataSaveList = LoadAutosave(dataSaveList); break
                case "3": dataSaveList = Save(dataSaveList)       
                case "4": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        else:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Save\t(4) Load\t(5) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": dataSaveList[2] = ""; break
                case "2": dataSaveList = LoadAutosave(dataSaveList); break
                case "3": dataSaveList = Save(dataSaveList)                        
                case "4": dataSaveList = Load(dataSaveList); break
                case "5": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye {dataSaveList[2]}")
                case _: print("\nCouldn't understand you?!")
        # sleep(2)
        dataSaveList[0] = 1
    return dataSaveList       


################################################################################## START (only once) ##################################################################################
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

################################################################################## MENU (MOVE...) ##################################################################################
### Move, Inventory, Stats
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
    dataSaveList[8] = itemsDict

    while True:  # >>>>>>>>>> MAIN GAME LOOP <<<<<<<<<<<
        itemAddStats = []
        itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict) 
        playerStats, playerStatPoints, itemsDict = Stats.LevelUp(playerStats, playerStatPoints, playerName, itemsDict)
        itemsDict = Items.Items(itemsDict)
        dataSaveList[0] = 0
        dataSaveList = Save(dataSaveList)
        dataSaveList[0] = 1

        userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(0) Exit to main menu\n")
        os.system('cls')
        match userInput:
            case "1": startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Move(
                    startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)

            case "2": itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)

            case "3": playerStats, playerStatPoints = Stats.StatMenu(
                    playerStats, playerStatPoints, playerName, itemsDict)

            case "0": dataSaveList = MainMenu(dataSaveList)
            case _: print("\nCouldn't understand you?!")
        


#############################################################################################################################################################################
#---------------------------------------------------------------------------------- MOVING ---------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################# DIRECTION TO MOVE ##############################################################################
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


################################################################################## THE WORLD ##################################################################################
### Move() <- World()
def World(startLocation, location, direction): 
   
    compass = ["n","e","s","w"] 

    worldmap = {
    # Location                    North        East       South        West
    startLocation   :   [   "the forest",       0,          0,          0           ],
    "the town"      :   [           0,   "the flatlands",   0,          0           ],
    "the flatlands" :   [           0,     "the forest",    0,       "the town"     ],
    "the forest"    :   ["the mountains","the islands",startLocation,"the flatlands"],
    "the mountains" :   [   "the castle",       0,    "the forest",     0           ],
    "the castle"    :   [           0,          0,    "the mountains",  0           ],
    "the islands"   :   [           0,          0,          0,        "the forest"  ]
    }

    for i in range(0,4):
        if compass[i] == direction:
            if worldmap[location][i] != 0:
                return worldmap[location][i]
        
    
    print("\nYou can't move there, try a different direction!")
    return "x"  
        


#############################################################################################################################################################################
#-------------------------------------------------------------------------------- SAVE/LOAD --------------------------------------------------------------------------------#
#############################################################################################################################################################################



#################################################################################### SAVE ####################################################################################
def Save(dataSaveList):    
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    if dataSaveList[0] == 0:
        with open(f"SaveFile_Autosafe.pickle", 'wb') as autoSaveHandler:
            pickle.dump(dataSaveList, autoSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
            dataSaveList[1][0] = "Autosave"                                                 #Add AutoSave to savePoints[0]        
    elif dataSaveList[0] == 1:
        while True:
            saveFileID = 1
            print(' Nr.\t\tSavefile'\
                '\n------------------------------------------------------------------------')
            for i in range(0, len(dataSaveList[1])):
                print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                saveFileID += 1
            print('------------------------------------------------------------------------\n')
            userInput = input(f"\n(1) Save\t(2) Delete\t (0) Return\n")
            if userInput == "1": 
                while True:
                    saveFileID = 1
                    print(' Nr.\t\tSavefile'\
                        '\n------------------------------------------------------------------------')
                    for i in range(0, len(dataSaveList[1])):
                        print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                        saveFileID += 1
                    print(f" {saveFileID}\t-\t<new slot>")
                    print('------------------------------------------------------------------------\n')
                    
                    userInputOverwrite = input("Choose slot for saving:\t\t(0) Abort\n")
                    os.system('cls')
                    if userInputOverwrite == "0":
                        break
                    elif userInputOverwrite == str(saveFileID):
                        
                        userInputFileName = input("\nName your slot:\t\t(0) Abort\n")
                        os.system('cls')                       
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
                    elif userInputOverwrite == "1":
                        print("You can't overwrite 'Autosave'!\n")
                    elif userInputOverwrite < str(saveFileID):
                        
                        userInputChoose = input("overwrite Slot? (1) Yes\t(2) No\n")
                        os.system('cls')
                        if userInputChoose == "1":
                            saveFileID = int(userInputOverwrite)                
                            
                            userInputFileName = input("\nName your slot:\t\t(0) Abort\n")
                            os.system('cls')
                            if userInputFileName != "0":    
                                with open(f'SaveFile_{userInputFileName}.pickle', 'wb') as manSaveHandler:
                                    pickle.dump(dataSaveList, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
                                    dataSaveList[1][saveFileID-1] = (userInputFileName)
                                with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                                    pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                        
                                break
                            else:
                                print("Couldn't understand you?\n") 
                                continue
                        elif userInputChoose == "2":
                            continue
                        else:
                            print("Couldn't understand you?\n") 
                            continue   
                    else:
                        print("Couldn't understand you?\n") 
                        continue   
            elif userInput == "2":
                saveFileID = 1
                print(' Nr.\t\tSavefile'\
                    '\n------------------------------------------------------------------------')
                for i in range(0, len(dataSaveList[1])):
                    print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                    saveFileID += 1
                print('------------------------------------------------------------------------\n')
                userInputDelete = input("\nChoose file to delete:\t\t(0) Abort\n")
                os.system('cls')
                if userInputDelete != "0":
                    dataSaveList[1][int(userInputDelete)-1]
                    break
                else:
                    print("Couldn't understand you?\n") 
                    continue  
            elif userInput == "0":
                break
            else:
                print("\nCouldn't understand you?\n")
                continue

    return dataSaveList


################################################################################## LOAD ##################################################################################
def Load(dataSaveList):
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    while True: 
        saveFileID = 1
        print(' Nr.\t\tSavefile'\
            '\n------------------------------------------------------------------------')
        for i in range(0, len(dataSaveList[1])):
            print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
            saveFileID += 1
        print('------------------------------------------------------------------------\n')        
        userInputNumber = int(input("\nChoose number to load:\t\t(0) Abort\n"))
        os.system('cls')        
        if userInputNumber != "0":
            if userInputNumber > len(dataSaveList[1]):
                print("Selected slot is empty")
                continue

            with open(f'SaveFile_{dataSaveList[1][userInputNumber-1]}.pickle', 'rb') as loadHandler: 
                dataSaveList = pickle.load(loadHandler)
            with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
                dataSaveList[1] = pickle.load(loadAllHandler)
            break
        else:
            break
    
    return dataSaveList    

def LoadAutosave(dataSaveList):
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]

    saveFileID = 0 
    with open(f'SaveFile_{dataSaveList[1][saveFileID]}.pickle', 'rb') as loadHandler: 
        dataSaveList = pickle.load(loadHandler)
    with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
        dataSaveList[1] = pickle.load(loadAllHandler)
    
    return dataSaveList                                         

Main()
