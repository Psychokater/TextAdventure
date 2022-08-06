import random
#import Main
from time import sleep

def Encounter(_startLocation, _location, _playerStats, _playerInventoryItems, _playerInventoryMoney):
    global startLocation
    global location
    global encounterIndex
    global enemyDict
    playerInventoryItems = _playerInventoryItems
    playerInventoryMoney = _playerInventoryMoney
    playerStats = _playerStats #Level, Atk, Def, HP    
    startLocation = _startLocation
    location = _location
    locationIndex = 0
    enemyID = 0

    enemyDict = {
            1001 : ["Rats", 1, 0, 2, 1, PicRat],
            1002 : ["Wolf", 3, 1, 10, 2, PicWolf],
            1003 : ["Bandit", 6, 4, 20, 4, PicBandit],
            1004 : ["Dragon", 20, 10, 50, 10, PicDragon]
            } # 0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

    
    # enemyHP = 0
    # enemyLevel = 1
    # enemyName = ""
    # enemyATK = 0
    # enemyDEF = 0
    
    

    if location == startLocation:
        locationIndex = 1        
    elif location == "the town":
        locationIndex = 1
    elif location == "the flatlands":
        locationIndex = 2
    elif location == "the forrest":
        locationIndex = 2
    elif location == "the islands":
        locationIndex = 6
    elif location == "the mountains":
        locationIndex = 8
    elif location == "the castle":
        locationIndex = 10
    
    luck = random.randint(1,100)
    encounterIndex = round(luck / (playerStats[0] * locationIndex)) # high = good, low = bad, max = 100 (lvl 1, location 1)    
    enemyID = EnemySelection(encounterIndex)
    if enemyID != 0:
        (enemyDict[enemyID][5]())
        while True:

            UserInputChoose = input("\nWhat do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(4) Flee\n")
            if UserInputChoose == "1":
                _playerInventoryMoney, _playerStats, _playerInventoryItems, _location = Fight(
                    playerStats, enemyDict, enemyID, playerInventoryMoney, playerInventoryItems, location)
                break
            #elif UserInputChoose == "2": 
                #Main.InventoryMenu()
            #elif UserInputChoose == "3": 
                #Main.StatMenu()
            elif UserInputChoose == "4": 
                _temp = (playerStats[0] * 2)
                playerInventoryMoney -= (playerStats[0] * 2)
                print(f"\nYou managed to escape the fight, you used up {_temp} gold to distract your enemy")
                break
            else: 
                print("You can't choose that?!")
        
    return _location, _playerStats, _playerInventoryItems, _playerInventoryMoney

def Fight(_playerStats, _enemyDict, _enemyID, _playerInventoryMoney, _playerInventoryItems, _location):
    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic
    lootItem = "lootItem" #(add Item later!!!)
    tempMoney = 0.00
    tempExp = 0
    global tempPlayerHP
    global tempEnemyHP
    tempPlayerHP = _playerStats[1]
    tempEnemyHP = _enemyDict[_enemyID][3]

    while True:

        if tempPlayerHP <= 0:
            print("\n---You have been defeated---")
            sleep(2)
            print("""
            Your head feels dizzy.
            A beautiful (fully naked) angel brought you back to the town.
            She thankfully took some of your gold in advance.
            """)
            _playerInventoryMoney -= _playerInventoryMoney * 0.1
            _playerStats[4] -= _playerStats * 0.25
            _location = "the town"
            _playerStats[1] = tempPlayerHP
            break

        if tempPlayerHP <= 0:
            print("\n---Enemy has been eleminated---")
            sleep(2)
            _playerInventoryItems.append(lootItem)
            tempMoney += (_enemyDict[_enemyID][1] + _enemyDict[_enemyID][2] + _enemyDict[_enemyID][3]) / 2
            tempExp += _enemyDict[_enemyID][4] * 100
            print(f"\nYou received {lootItem}, {tempMoney} Gold and {tempExp} Experience.")
            _playerInventoryMoney = tempMoney
            _playerStats[4] = tempExp
            _playerStats[1] = tempPlayerHP
            break


        UserInputFight = input("\n(1) Attack\t(2) Inventory\t(3) Flee\n")
        if UserInputFight == "1":
            if  _playerStats[3] - _enemyDict[_enemyID][1] >= 0:
                tempEnemyHP -= _playerStats[3] - _enemyDict[_enemyID][1]
            print(f"\nYou attack {_enemyDict[_enemyID][0]} with {_playerStats[1]} Points.")
            sleep(1)
            print(f"{_enemyDict[_enemyID][0]} defends himself with {_enemyDict[_enemyID][2]} Points.")
            sleep(1)
            print(f"{_enemyDict[_enemyID][0]} has {tempEnemyHP} HP left.")
            sleep(2)

            if _enemyDict[_enemyID][2] - _playerStats[2] >= 0:
                 tempPlayerHP -= _enemyDict[_enemyID][2] - _playerStats[2]
            print(f"{_enemyDict[_enemyID][0]} attacks you with {_enemyDict[_enemyID][1]} Points.")
            sleep(1)
            print(f"You defend yourself with {_playerStats[1]} Points.")
            sleep(1)
            print(f"You have {tempPlayerHP} HP left.")
            sleep(1)
                        
        #elif UserInputFight == "2":
            #Main.InventoryMenu()
        elif UserInputFight == "3":
            _temp1 = (_playerStats[0] * 2)
            _playerInventoryMoney -= (_playerStats[0] * 2)
            _temp2 = (_enemyDict[_enemyID][1])
            _playerStats[3] -= _enemyDict[_enemyID][1]
            print(f"""You managed to flee while you distracted the enemy with {_temp1} gold,
            but {_enemyDict[_enemyID][0]} got a hit. You received {_temp2} dmg!""")
            break
        else: 
            print("You can't choose that?!")

    return _playerInventoryMoney, _playerStats, _playerInventoryItems, _location



def EnemySelection(_encounterIndex):
    enemyID = 0
    
    if _encounterIndex <= 10:
        EncounterNothing()
    elif _encounterIndex > 10 or _encounterIndex <= 100:
        _luck = random.randint(1,4)
        enemyID = 1000 + _luck
    return enemyID

# def Mountains():
#     global encounterIndex
    
#     luck = random.randint(1,100)
#     if luck == 100 and playerLevel > 5:
#         print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
#         encounterIndex = 20        
#     if luck <= 10 and playerLevel > 5:
#         EncounterWolf()
#         encounterIndex = 2
#     if luck > 10 and luck <= 30 and playerLevel > 5:
#         EncounterRat()
#         encounterIndex = 3
#     if luck > 30 and luck <= 80 and playerLevel > 5:
#         Nothing()
#         encounterIndex = 0        
#     if luck > 80 and luck < 100 and playerLevel > 5:
#         EncounterWanderer() 
#         encounterIndex = 10
#     if playerLevel < 5:
#         LowLevel()




# ########################################## No Encounter ##################################

def EncounterLowLevel():
    print("You couldn't find anything here, maybe you come back when you are stronger?")

def EncounterNothing():
    print("Phew, nothing happened here.")


# ######################################## Friends ################################################

def PicWanderer(): 
    print("""A mystic old man wanders through this valley, maybe he has something for you?
     
                     .x    
                     .    x    
                       x`  
            /\       .x   .
            / />        o        
           /  \}      .o x             ____ _____   
          /`---\   .-`---'-.        ,-'  ,-'_ ,-'|   
          |  \__D  \`--.--'/       |""-'" ,-'|   |   
         /     /    \     /        ||"\"""|   |,-'   
        /_____/\   _//^-^\\\\_._      |____|,-'   
    """)



def PicMerchant():
    print("""
    
            /'''''''''''''''''''\\
           /_____/Merchant\\______\\     
            |       ____        |
            |      |_|_|        |
        ;,_<|_--_----__----___--|\_
              \\_/        \\_/     
    """)    



######################################## Enemys ##################################################



def PicWolf():
    print("""oh no, Wolf!
                /^._        Bark
  ,___,--~~~~--' /'~ Bark
  `~--~\ )___,)/'               Bark
      (/\\\_  (/\\\_
       """)
    


def PicRat():
    print("""look, rats!
    
     ~~(  )8:>    <;3(  )~~
     """)

def PicBandit():
    print("""
    
    ToDo: Make a Pic of Bandit
    
    """)


def PicDragon():
    print("""
    'It does not do to leave a live dragon out of your calculations, if you live near him.'      

                     __/>^^^;:,
                    /-.       :,/|/|
                 __/ `c        :,/ \__
                (~             ;/ /  /
                 `-'--._       / / ,<     _
                       /=\     /  _/     | '.
                      / ',\ \\    \_     ,| |"       
                     |=|  E_  |     \. ,/  |
                     \=\   ""       `,,/   |
                      \=\            ||    /
                       \=\____       |\    \\
                      / \/    `     <__)    \\
                      | |                    |
                    ,__\,\                   /
                   ,--____>    /\.         ./
                   '-__________>  \.______/
                   
                   """)


