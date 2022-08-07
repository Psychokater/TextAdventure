#Textadventure
import random
import Helpfile
from time import sleep
import Intro
import Encounter


#ToDo:  Encounter
#       Fehleingaben
#       Inventar
#       Monster / Fight
#       

#erl. Menu
#   Start
#   Help
#   Exit

#erl. Game
#   Move
#   Inventar
#   Stats
#   Exit to main menu

#Inventar
#   Geld
#   Gegenstand

#erl. Stats
#   Level
#   Atk
#   Def
#   HP

#####################

# erl.
#   Town
#   Forrest
#   Desert
#   Islands
#   Mountains

#   Monster
#       Level
#       HP
#       Atk
#       Loot

#   Händler
#       Geld
#       Gegenstand




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
playerLevel = 1
playerExp = 0
playerHP = 20
playerAtk = 4
playerDef = 5
playerInventoryMoney = 10
merchantInventoryMoney = 200
playerInventoryItems = {"Butterknife":[1, 0, 0, 2], "Apple":[0, 0, 2, 1], "Hat":[0, 2, 0, 2]} # {Item:[ATK,DEF,HEAL,VALUE]}
merchantInventoryItems = {"testitem":[1, 2, 3, 4]} ### maybe Random??!! Maybe add a counter for "Days" which increment with every Move()? More Days = More/Better Items (Monster Loot and Merchant)
playerName = ''
location = ''
playerStats = [playerLevel, playerHP, playerAtk, playerDef, playerExp]



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
            case "3": StatMenu()
            case "4": MainMenu()
            case _: print("\nCouldn't understand you?!")



def StatMenu():
    global playerStatPoints,playerAtk,playerDef,playerHP
    while True:
        print(f"\nPoints: {playerStatPoints}\n\n HP: {playerHP}\nATK: {playerAtk}\nDEF: {playerDef}")
        if playerStatPoints == 0:  
            userInput = input("\n(1) Return\n")
            if userInput == "1":
                break
            else: print("\nCouldn't understand you?!")
        else: 
            userInput = input(f"\n(1) Edit Stats ({playerStatPoints} P)\t(2) Return\n")
            if userInput == "1":
                EditStats()
            elif userInput == "2":
                return
            else: print("\nCouldn't understand you?!")

            
def EditStats():
    global playerHP, playerAtk, playerDef, playerStatPoints
    while True:
        print(f"\nPoints: {playerStatPoints}\n\n HP: {playerHP}\nATK: {playerAtk}\nDEF: {playerDef}")
        userInput = input("\n(1) HP +10\t (2) Atk + 1\t (3) Def + 1\t (4) Return\n")
        match userInput:
            case "1": playerHP += 10 ; playerStatPoints -= 1
            case "2": playerAtk += 1 ; playerStatPoints -= 1
            case "3": playerDef += 1; playerStatPoints -= 1
            case "4": break
            case _: print("\nCouldn't understand you?!")


### Level Up ???
def LevelUp():
    global playerLevel, playerExp, playerStatPoints

    if playerExp == playerLevel * round((2**(playerLevel*0.6))):
        playerLevel += 1
        if playerLevel % 5 == 0:
            playerStatPoints += 4
        else:
            playerStatPoints += 2
        print("\nYay, Level Up!")


def InventoryMenu():
    global playerInventoryItems
    print(f"\nInventory: {playerInventoryItems}")
    sleep(2)       


### Move() -> World()
def Move():
    temp = "x"
    global location
    print(f"\nLocation: {location}")
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
    LevelUp()


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
   global startLocation, location, playerStats, playerInventoryItems, playerInventoryMoney 
   location, playerStats, playerInventoryItems, playerInventoryMoney = Encounter.Encounter(
    startLocation, location, playerStats, playerInventoryItems, playerInventoryMoney)



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
