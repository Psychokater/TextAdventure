####################################
#                                  #
#     ~~~ TEXTADVENTURE ~~~        #
#                                  # 
#  Author: Nils aka Psychokater    #
#  CoAuthor: Samo aka Samoooooooo  #
#                                  #
#################################### 

#----------------------------#
#           ToDo             #
#----------------------------#
#
# add something...
#
#
#----------------------------#


import os
import random
import pickle
from time import sleep
from Colors import cl
from Intro import IntroAnimation

import MainMenu
import SaveLoad
import Encounter
import Stats
import Inventory
import Items
import Maps



#############################################################################################################################################################################
#---------------------------------------------------------------------------------- MAIN -----------------------------------------------------------------------------------#
#############################################################################################################################################################################



################################################################################# MAIN GAME #################################################################################
### Main Game
def Main(): 
    newGame = True    
    while True:  
           
        itemsDict = {}
        itemsDict = Items.Items(itemsDict)
        playerInventoryMoney = 5.00
        playerStatPoints = 0    
        playerStats = [1, 15.0, round(15,2), 2.0, 1.0, 0.00] # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
        playerName = ""
        savePoints = []
        autoSave = 0
        dataSaveList = [autoSave, savePoints, playerName, "", "", playerInventoryMoney, playerStatPoints, playerStats, itemsDict]
        #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]    
        try:
            with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
                dataSaveList[1] = pickle.load(loadAllHandler)
        except FileNotFoundError:        
            with open(f'Savepoint_Status.pickle', 'wb') as manSaveHandler:
                pickle.dump(dataSaveList[1], manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
        
        if newGame == True:
            newGame = False                
            # sleep(2)        
            dataSaveList, newGame, load = MainMenu.MainMenu(dataSaveList, newGame)       
            if newGame == True:
                newGame = False               
                dataSaveList = Start(dataSaveList)
        elif newGame == False:        
            dataSaveList = Start(dataSaveList)              
        dataSaveList, newGame, load = IngameMenu(dataSaveList, newGame)
        if newGame == True:           
            newGame = False
            del dataSaveList            
            continue




############################################################################### START (only once) ############################################################################
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
    IntroAnimation()
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
    sleep(0.5)
    print(f"\nWelcome to a new adventure {playerName}!")
    sleep(0.5)
    print(f"\nYou wake up in {location}")
    PicStartFire()
    sleep(0.5)    
    dataSaveList[2] = playerName
    dataSaveList[3] = startLocation
    dataSaveList[4] = location

    return dataSaveList

################################################################################## MENU (MOVE...) ##################################################################################
### Move, Inventory, Stats
def IngameMenu(dataSaveList, newGame):
   #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    while True:
        playerName = dataSaveList[2]
        startLocation = dataSaveList[3]
        location = dataSaveList[4]
        playerInventoryMoney = dataSaveList[5]
        playerStatPoints = dataSaveList[6]
        playerStats = dataSaveList[7]
        itemsDict = dataSaveList[8]

        while True:  # >>>>>>>>>> MAIN GAME LOOP <<<<<<<<<<<
            itemAddStats = []
            itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict) 
            playerStats, playerStatPoints, itemsDict = Stats.LevelUp(playerStats, playerStatPoints, playerName, itemsDict)        
            dataSaveList[4] = location
            dataSaveList[5] = playerInventoryMoney 
            dataSaveList[6] = playerStatPoints
            dataSaveList[7] = playerStats
            dataSaveList[8] = itemsDict
            dataSaveList[0] = 0
            dataSaveList = SaveLoad.Save(dataSaveList)
            dataSaveList[0] = 1            
            userInput = input("\nWhat to do now?\n(1) Move\t(2) Inventory\t(3) Stats\t(0) Exit to main menu\n")
            os.system('cls')
            if userInput == "1":
                startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict = Move(
                        startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)
            elif userInput == "2":
                itemsDict, playerStats = Inventory.InventoryMenu(
                    startLocation,location,itemsDict, playerName, playerInventoryMoney, playerStats)  
            elif userInput == "3":
                playerStats, playerStatPoints = Stats.StatMenu(
                        playerStats, playerStatPoints, playerName, itemsDict)  
            elif userInput == "0":
                dataSaveList, newGame, load = MainMenu.MainMenu(dataSaveList, newGame)                
                if newGame == True:                 
                    return dataSaveList, newGame, load
                if load == True:
                    break
            else:
                print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}")        
        
    
        
        


#############################################################################################################################################################################
#---------------------------------------------------------------------------------- MOVING ---------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################# DIRECTION TO MOVE ##############################################################################
### Move() -> World()
def Move(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
    _temp = "x"
    
    # sleep(1)
    while _temp == "x":
        print(f"\nLocation: {location}")
        userInput = input("\nWhich direction do you want to go? \n'north' 'east' 'south' 'west'\t\t(0) Abort\n").lower()
        if userInput == "0":
            return startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict
        os.system('cls')
        direction = userInput[:1]
        _temp,_tempPic = World(startLocation, location, direction)        
        # sleep(2)        
        if _temp != "x":
            location = _temp
            _tempPic()
            print(f"\nYou moved to {location}\n")       
            break      
    #Maps.MapFlatlands(startLocation, location)
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
    # Location                    North                  East                 South                  West
    startLocation   :   [    "the flatlands"   ,          0          ,          0          ,          0          ,PicStartFire],
    "the town"      :   [           0          ,  "the flatlands"    ,          0          ,          0          ,PicTheTown],
    "the flatlands" :   [      "green land"    ,    "the forest"     ,    startLocation    ,      "the town"     ,PicFlatlands],
    "the forest"    :   [    "the mountains"   ,    "the islands"    ,          0          ,   "the flatlands"   ,PicForest],
    "the mountains" :   [      "the castle"    ,          0          ,    "the forest"     ,     "the desert"    ,PicMountains],
    "the castle"    :   [           0          ,          0          ,   "the mountains"   ,          0          ,PicCastle],
    "the islands"   :   [           0          ,          0          ,    "mystic stones"  ,    "the forest"     ,PicIslands],
    "mystic stones" :   [     "the islands"    ,          0          ,          0          ,          0          ,PicMysticStones],
    "green land"    :   [     "the desert"     ,          0          ,   "the flatlands"   ,          0          ,PicGreenLand],
    "the desert"    :   [      "the lake"      ,   "the mountains"   ,     "green land"    ,          0          ,PicTheDesert],
    "the lake"      :   [           0          ,          0          ,     "the desert"    ,          0          ,PicTheLake],

    }

    for i in range(0,4):
        if compass[i] == direction:
            if worldmap[location][i] != 0:
                return worldmap[location][i],worldmap[worldmap[location][i]][4]

   
    
    print(f"\n{cl.RED}You can't move there, try a different direction!{cl.RESET}\n")
    return "x", "0"  
        
def PicStartFire():
    print(f"""   
                     {cl.RED}(            
                       )          
                     (  (          
                         )        
                   (    ({cl.RESET}       
                    {cl.RED}){cl.RESET} {cl.YELLOW}/\  {cl.RESET}{cl.RED}({cl.RESET}
                  {cl.RED}({cl.RESET} {cl.YELLOW} //\  {cl.RESET} {cl.RED}({cl.RESET}     
                _ -.;{cl.MAGENTA}_/ \\{cl.RESET}--._    
               (_;-{cl.MAGENTA}// | \ \{cl.RESET}-'.\   
               ( `.__ _  ___,')   
                `'(_ )_)(_)_)'
""")
########################################################################

def PicTheDesert():
    print(f"""
               ,                        '           .        '        ,                     .        '
       .            .        '       .         ,         
                                                       .       '     +          .        '
           +          {cl.YELLOW}.-'''''-.{cl.RESET}       '     +
                    {cl.YELLOW}.'         `.{cl.RESET}    +     .             
           ___     {cl.YELLOW}:             :{cl.RESET}                        .     '                  .    '     +      '
      ____/   \   {cl.YELLOW}:               :{cl.RESET}      .              ||
     /         \  {cl.YELLOW}:      {cl.RESET}_/|{cl.YELLOW}      :{cl.RESET}    `           ,.|| ||             
    /  ,   '  . \  {cl.YELLOW}:    {cl.RESET}/_/{cl.YELLOW}      :{cl.RESET}       '           || || ||   .                     .        '
        |        \  {cl.YELLOW}`.{cl.RESET}_/ |{cl.YELLOW}     .'{cl.RESET}                    \\\\ || ||...    ,     '     +
       ;|,   '   (   /  ,|{cl.YELLOW}...-'{cl.RESET}            '   ,      \\\\|| //             
     ___|____     \_/^\/||__             __.________,.  ||//         .  ,  '     +
               _/~  `""~`"` \_           ''(       ..\.,||/       '                         .        '
     ..,...  __/  -'/  `-._ `\_\__          \           ||``\___,.__.____
                  '`  `\   \  \-.\          /_:_,..     || ____/         \\________Î.,___________,.
                                                ______/"###""")
########################################################################

def PicTheLake():
    print(f"""
                  _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \.
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
{cl.BLUE}                                      ____________.'
                         __________.-'
      _______          .'                  
 ___.'       '.       /               {cl.RESET}'-._{cl.BLUE}        
             .'\    .' ._,.__,        {cl.RESET}____\____.o.{cl.BLUE}
             '..'._/                 {cl.RESET}'-._______.-'{cl.BLUE}
                                     .-'_______'-.
                                         _/    'o'
                                      .-'

{cl.RESET}""")
########################################################################

def PicGreenLand():
    print(f"""
                                        __
                 ,-_                  (`  ).
                 |-_'-,              (     ).
                 |-_'-'           _(        '`.
        _        |-_'/        .=(`(      .     )
       /;-,_     |-_'        (     (.__.:-`-_.'
      /-.-;,-,___|'          `(       ) )
     /;-;-;-;_;_/|\_ _ _ _ _   ` __.:'   )
        x_( __`|_#_|`-;-;-;,|        `--'
        |\ \    _||   `-;-;-'
        | \`   -_|.      '-'
        | /   /-_| `
        |/   ,'-_|  \.
        /____|'-_|___\.
{cl.GREEN} _..,____]__|_\-_'|_[___,.._
'                          ``'--,..,.{cl.RESET}
""")
########################################################################

def PicFlatlands():
    print(f"""
              __                                 
            (`  ).                              
           (     ).                            
        _(        '`.                                                                              
    .=(`(      .     )                                           ((````))                         
   (     (.__.:-`-_.'                        ((````))          _(        '`                        
   `(       ) )                            (        '`.      (      .     )                   
     ` __.:'   )                          (      .     )       (.__.:-`-_.'                            
           `--'                           (.__.:-`-_.'                                                                                                   
   

{cl.YELLOW}        , . ,                     . , .                      . , .  
{cl.GREEN} _..,____\|/___,,_,._,___,.._.,____\|/{cl.YELLOW}, . ,{cl.GREEN} ...,______,.._____\|/____..,______,.._
'  ..,______,.._         ``'--,..,.____\|/____..,______,.._{cl.RESET} """)
########################################################################

def PicForest():
    print(f"""       
                                               .:
       {cl.GREEN}^  ^  ^   ^{cl.RESET}      ___I_      {cl.GREEN}^  ^   ^  ^  ^   ^  ^{cl.RESET}
      {cl.GREEN}/|\/|\/|\ /|\{cl.RESET}    /\-_--\    {cl.GREEN}/|\/|\ /|\/|\/|\ /|\/|\.{cl.RESET}
      {cl.GREEN}/|\/|\/|\ /|\{cl.RESET}   /  \_-__\   {cl.GREEN}/|\/|\ /|\/|\/|\ /|\/|\.{cl.RESET}
      {cl.GREEN}/|\/|\/|\ /|\{cl.RESET}   |[]| [] |   {cl.GREEN}/|\/|\ /|\/|\/|\ /|\/|\ {cl.RESET}
      """)
########################################################################

def PicMountains():
    print("""           .          .           .     .                .       .
  .      .      *           .       .          .                       .
                 .       .   . *            "There's nothing quite like an adventure in the mountains,
  .       ____     .      . .            .     being surrounded by nature's giants"
         >>         .        .               .
 .   .  /WWWI; \  .       .    .  ____               .         .     .         
  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .
  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
 . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
 /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *  
/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \ 
WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \ XXXXXXXXXXXX
WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::       \.XXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""")
########################################################################
def PicCastle():
    print("""

   /\                                                        /\.
  |  |                                                      |  |
 /----\                 Lord Dark's Keep                   /----\.
[______]            Where Brave Knights Tremble           [______]
 |    |         _____                        _____         |    |
 |[]  |        [     ]                      [     ]        |  []|
 |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
 |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
 |             |     |/'    ____..____    '\|     |             |
  \  []        |     |    /'    ||    '\    |     |        []  /
   |      []   |     |   |o     ||     o|   |     |  []       |
   |           |  _  |   |     _||_     |   |  _  |           |
   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
   |           |     |   |     (||)     |   |     |           |
   |           |     |   |      ||      |   |     |           |
 /''           |     |   |o     ||     o|   |     |           ''\.
[_____________[_______]--'------''------'--[_______]_____________]
""")
########################################################################
def PicIslands():
    print("""
           _  _             _  _
  .       /\\/%\       .   /%\/%\     .
      __.<\\%#//\,_       <%%#/%%\,__  .
.    <%#/|\\%%%#///\    /^%#%%\///%#\\
      ""/%/""\ \""//|   |/""'/ /\//"//'
 .     L/'`   \ \  `    "   / /  ```
        `      \ \     .   / /       .
 .       .      \ \       / /  .
        .        \ \     / /          .
   .      .    ..:\ \:::/ /:.     .     .
______________/ \__;\___/\;_/\________________________________
YwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw
""")
########################################################################
def PicMysticStones():
    print("""
               v                                                                         
       \             /               __________                _________                                          
          ._________.               /\____;;___\.             /_|_____|_\                                        
        ./  \______/ \.            | /         /              '._\___/_.'                                   
       ./  /       \  \.           `. ())oo() .         ``'--,..,._.,______,.._        
_     ./__/_ _ . _ _\__\    _       |\(%()*^^()^\.                         ____                                
      .\  \         /  /.          %| |-%-------|           ____          /___/\                 
       .\  \ ______/  /.          % \ | %  ))   |          /\__/\        //o  \_\                      
        .\_/_______\_/.           %  \|%________|         /_/  \_\       \\___/ /           
  ``'--,..,._______,.._                                   \ \__/ /        \\_/_/   
                                  ``'--,..,._______,..     \/__\/       _______,,_,._,__
                               . , .                     _______,,_,._,__
 _..,_______,,_,._,___,.._.,____\|/, . , ...,______,..____/, . , ...,___/, . , ...,___
' ..,______,.._         ``'--,..,._______,.._
                      
    """)
########################################################################
def PicTheTown():
    print(""" 
~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '
""")
##########################################################
def PicGateWay():
    print ("""
                                                                      
                   _              .::::::::::::.              _            
                __(_)___         .::::::::::::::.         ___(_)__          
---------------/  / \  /|       .:::::;;;:::;;:::.       |\  / \  \-------  
______________/_______/ |      .::::::;;:::::;;:::.      | \_______\________
|       |     [===  =] /|     .:::::;;;::::::;;;:::.     |\ [==  = ]   |    
|_______|_____[ = == ]/ |    .:::::;;;:::::::;;;::::.    | \[ ===  ]___|____
     |       |[  === ] /|   .:::::;;;::::::::;;;:::::.   |\ [=  ===] |      
_____|_______|[== = =]/ |  .:::::;;;::::::::::;;;:::::.  | \[ ==  =]_|______
 |       |    [ == = ] /| .::::::;;:::::::::::;;;::::::. |\ [== == ]      | 
_|_______|____[=  == ]/ |.::::::;;:::::::::::::;;;::::::.| \[  === ]______|_
   |       |  [ === =] /.::::::;;::::::::::::::;;;:::::::.\ [===  =]   |    
___|_______|__[ == ==]/.::::::;;;:::::::::::::::;;;:::::::.\[=  == ]___|_____    
""")
Main()
