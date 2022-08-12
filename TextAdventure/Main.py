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
            else:
                userInput = input('\n(1) Continue\t(2) Help\t(3) Exit\n')

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
    location = "the flatlands"                                                                                                      # !!!!!!!!!!!!! CHANGE "the flatlands" TO "startLocation" FOR RELEASE!!!!!!!!!!!! ONLY FOR TESTING!!!!!!!!!!
    while True:
        playerName = input("\nWhat's your name adventurer?\n").capitalize()
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
    playerInventoryMoney = 50.00
    playerStatPoints = 1
    playerStats = [1, 20, 20, 4, 5, 0.00] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP

    itemsDict = {
    #      0   1        2            3     4       5      6         7        8       9       10     11
    #                  Name         atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                           Quantity Merchant resets every lvlUp (qnt Max / 2 - qnt P)
    #                                                                Max       P                                                     qnt Max = Max qnt in Game
    1001:[(0),(0),"Apple\t",        (0),   (0),    (2),    (1),     (20),    (2),    (7),    (7),   (0)],                          # ID (row 9 and 10)
    1002:[(0),(0),"Fish\t",         (0),   (0),    (5),    (3),     (20),    (0),    (7),    (7),   (0)],                          # 1, 2, 3 = Merchant Inv lvl 5, 10, 20+
    1003:[(0),(0),"Cabbage\t",      (0),   (0),    (4),    (2),     (10),    (0),    (7),    (7),   (0)],                          # 4, 5, 6 = Wizard Inv lvl 5, 10, 20+   
    1004:[(0),(0),"Rusty Sword",    (5),   (0),    (0),    (5),     (2),     (0),    (1),    (1),   (1)],                          # 7, 8, 9 = Loot Inv lvl 5, 10, 20+                          
    1005:[(0),(0),"Shield\t",       (0),   (5),    (0),    (8),     (2),     (0),    (1),    (1),   (2)],                          # 
    1006:[(0),(0),"10 HP Potion",   (0),   (0),    (10),   (5),     (10),    (0),    (4),    (4),   (0)],                          # For Index 11: Use = 0, Weapon = 1, Secondary = 2, Head = 3, Breast = 4, Feet = 5, Hands = 6, Special = 7 -- if equipped: +10
    1007:[(0),(0),"20 HP Potion",   (0),   (0),    (20),   (10),    (10),    (0),    (5),    (0),   (0)],                          # 
    1008:[(0),(0),"30 HP Potion",   (0),   (0),    (30),   (15),    (10),    (0),    (6),    (0),   (0)],                          # IF lvl "x" Then itemsDict(10) = itemsDict(9)
    1009:[(0),(0),"Bandage\t",      (0),   (0),    (5),    (3),     (5),     (2),    (4),    (4),   (0)],                        
    1010:[(0),(0),"Bullwark",       (0),   (15),   (0),    (17),    (1),     (0),    (9),    (0),   (2)],                         
    1011:[(0),(0),"Steel Plates",   (0),   (12),   (0),    (20),    (1),     (0),    (3),    (0),   (3)],                        
    1012:[(0),(0),"Steel Gloves",   (0),   (5),    (0),    (7),     (1),     (0),    (3),    (0),   (6)],                        
    1013:[(0),(0),"Steel Shoes",    (0),   (3),    (0),    (5),     (1),     (0),    (3),    (0),   (5)],                        # IF itemsDict(10)  = Value = Item is in game
    1014:[(0),(0),"Steel Helmet",   (0),   (8),    (0),    (12),    (1),     (0),    (3),    (0),   (3)],                        
    1015:[(0),(0),"Steel Shield",   (0),   (10),   (0),    (15),    (1),     (0),    (3),    (0),   (2)],                         # IF itemsDict(10)  = 0 = Item is NOT in game!  
    1016:[(0),(0),"Steel Axe",      (10),  (0),    (0),    (15),    (1),     (0),    (3),    (0),   (1)],                        
    1017:[(0),(0),"Blueberries",    (0),   (0),    (4),    (2),     (10),    (0),    (7),    (7),   (0)],                        
    1018:[(0),(0),"Dark Dagger",    (12),  (0),    (0),    (18),    (1),     (0),    (8),    (0),   (1)], 
    1019:[(0),(0),"Bone Knife",     (10),  (0),    (0),    (16),    (1),     (0),    (8),    (0),   (1)],                        
    1020:[(0),(0),"Trousers",       (0),   (2),    (0),    (4),     (4),     (1),    (1),    (1),   (14)],                        
    1021:[(0),(0),"Butcher Knife",  (3),   (0),    (0),    (6),     (3),     (0),    (7),    (7),   (1)],                        
    1022:[(0),(0),"Broken Staff",   (2),   (0),    (0),    (1),     (3),     (1),    (7),    (7),   (11)],                       
    1023:[(0),(0),"Kings Sword",    (25),  (0),    (0),    (50),    (1),     (0),    (9),    (0),   (1)],                          #ItemKeys: 1234 
    1024:[(0),(0),"Chicken\t",      (0),   (0),    (8),    (10),    (5),     (0),    (8),    (0),   (0)],                          #          1 = lvl range (0-10, 10-20, 20+)  
    1025:[(0),(0),"Exp Scroll",     (0),   (0),    (0),    (70),    (1),     (0),    (6),    (0),   (0)],                          #          2 = use/eq (see index 11)  
    1026:[(0),(0),"Letttuce",       (0),   (0),    (2),    (1),     (10),    (0),    (7),    (0),   (0)],                          #          3 + 4 = Numerate
    1027:[(0),(0),"Muddy Gloves",   (0),   (1),    (0),    (1),     (5),     (1),    (7),    (0),   (16)],                         
    1028:[(0),(0),"Dungeon Key",    (0),   (0),    (0),    (200),   (1),     (0),    (9),    (0),   (7)]}                          
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq

    while True:  # >>>>>>>>>> MAIN GAME LOOP <<<<<<<<<<<
        playerStats, playerStatPoints, itemsDict = Stats.LevelUp(playerStats, playerStatPoints, playerName, itemsDict)
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
    # sleep(1)
    while _temp == "x":
        userInput = input("\nWhich direction do you want to go? \n'north' 'east' 'south' 'west'\n").lower()
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
