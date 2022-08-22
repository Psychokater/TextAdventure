import random
from Colors import cl
from time import sleep
import Stats
import Inventory
import Enemys
import os




#############################################################################################################################################################################
#-------------------------------------------------------------------------------- ENCOUNTER --------------------------------------------------------------------------------#
#############################################################################################################################################################################


######################################################################### ENCOUNTER (luck + location) #######################################################################
def Encounter(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
 
   # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
    locationIndex = 0
    enemyID = 0
    _locations = [startLocation, "the town", "the flatlands", "the forest", "the mountains", "the islands", "the castle"]
    _locationIndexList = [1,          100,             1,              1,            1,             1,             201  ]

    
    for i in range(0,len(_locations)):
        if location == _locations[i]:
            locationIndex = _locationIndexList[i]
            if locationIndex == 201 or locationIndex == 202 or locationIndex == 203:
                locationIndex, itemsDict = DungeonSelection(
                    locationIndex, itemsDict)
                if locationIndex > 3:
                    startLocation, location, locationIndex, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict = Dungeon(
                        startLocation, location, locationIndex, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict)
                    return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict

                
            if locationIndex == 100:
                itemsDict, playerInventoryMoney, playerStats = Inventory.ShopMenu(startLocation, location, itemsDict, playerName, playerInventoryMoney, playerStats)
                return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict 
            
                

    luck = random.randint(1,100)                                                    
    if luck >= 98:                                                          
        itemsDict, playerInventoryMoney, playerStats = Inventory.WandererMenu(startLocation, location, itemsDict, playerName, playerInventoryMoney, playerStats)
    encounterIndex = round(luck - (luck * (playerStats[0]) * 0.01) - locationIndex)             # high = good, low = bad, max = 100 (lvl 1, location 1)    
    enemyID, selectedDict, selectedDictID = EnemySelection(playerStats, encounterIndex)
    
                         
    
    if enemyID != 0:
                
        enemyMaxHP = (selectedDict[enemyID][2])  
                                                                        # select Enemy with ID from Dict (Random) -> see EnemySelection()
        while True:           
            
            (selectedDict[enemyID][6]()) 
            UserInputChoose = input(""\
            f"\n{cl.BLUE}{'{:<15}'.format(playerName)}{cl.RESET}\t\tLVL {cl.BLUE}{playerStats[0]}{cl.RESET}\tHP {cl.GREEN}{round(playerStats[2],2)}/{round(playerStats[1],2)}{cl.RESET}\n"\
            f"----------- VS -----------\n"\
            f"{cl.RED}{'{:<15}'.format(selectedDict[enemyID][0])}{cl.RESET}\t\tLVL {cl.BLUE}{selectedDict[enemyID][1]}{cl.RESET}\tHP {cl.BLUE}{round(selectedDict[enemyID][2],2)}/{round(enemyMaxHP,2)}{cl.RESET}\n\n"\
            f"What do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(0) Flee\n")
            os.system('cls')

            if UserInputChoose == "1":
                playerInventoryMoney, playerStats, playerStatPoints, location = Fight(
                    startLocation, playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID)
                break
            
            elif UserInputChoose == "2":
                itemsDict, playerStats = Inventory.InventoryMenu(
                    startLocation, location, itemsDict, playerName, playerInventoryMoney, playerStats)  

            elif UserInputChoose == "3": 
                playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName, itemsDict )

            elif UserInputChoose == "0": 
                _temp = round(playerStats[0] * 0.1 *(selectedDict[enemyID][1] - playerStats[0]),2)
                if _temp < 0:
                    _temp = 0  
                playerInventoryMoney -= (_temp)
                if playerInventoryMoney - (_temp) < 0:
                    playerInventoryMoney = 0
                print(f"""\nYou managed to escape the fight, you used up {cl.RED}{round(_temp,2)}{cl.RESET} gold to distract your enemy.
                \nYou have {cl.GREEN}{round(playerStats[2],2)}{cl.RESET} HP left.""")
                break
            else: 
                print("\nYou can't choose that?!")
        
    return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict

############################################################################# SELECT ENEMY #############################################################################
def EnemySelection(playerStats, encounterIndex):   
    #Edit this function later to config chances for Encounter    
    enemyDictEasy = {}
    enemyDictMedium = {}
    enemyDictHard = {}    

    enemyDictEasy, enemyDictMedium, enemyDictHard = Enemys.Enemys(enemyDictEasy, enemyDictMedium, enemyDictHard)
    enemyID = 0                                                                                      
    selectedDict = {}
    _tempList = []
    selectedDictID = 0
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP   
    while True:
        if encounterIndex <= 10:
            _luck = random.randint(0,len(enemyDictHard)-2)
            for i in enemyDictHard:
                _tempList.append(i)
            enemyID = _tempList[_luck]
            selectedDict = enemyDictHard
            selectedDictID = 3        
        elif encounterIndex > 11 and encounterIndex <= 42:
            _luck = random.randint(0,len(enemyDictMedium)-2)
            for i in enemyDictMedium:
                _tempList.append(i)
            enemyID = _tempList[_luck]
            selectedDict = enemyDictMedium
            selectedDictID = 2
        elif encounterIndex > 43 and encounterIndex <= 100:
            _luck = random.randint(0,len(enemyDictEasy)-2)
            for i in enemyDictEasy:
                _tempList.append(i)
            enemyID = _tempList[_luck]       
            selectedDict = enemyDictEasy
            selectedDictID = 1

        if selectedDictID == 3 and playerStats[0] < 20:
            EncounterLowLevel()        
            enemyID = 0
            break
        elif selectedDictID == 2 and playerStats[0] < 10:
            EncounterLowLevel()        
            enemyID = 0
            break
        if enemyID != 0:
            selectedDict[enemyID][1] = random.randint(selectedDict[enemyID][5],selectedDict[enemyID][5]+3)            
            for i in range(2,5):
                selectedDict[enemyID][i] += round((selectedDict[enemyID][1] - selectedDict[enemyID][5]) * (selectedDict[enemyID][5] * 0.5))

        if enemyID != 0 and (selectedDict[enemyID][1] - playerStats[0]) > 3:       
            continue
        else:
            break  
   
  

    return enemyID, selectedDict, selectedDictID


############################################################################# ENEMY ITEMS #############################################################################
def EnemyItemSelection(itemsDict, enemyID, selectedDict, selectedDictID):
#Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
#Enemy: 0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic 
    _tempItemList = []
    _tempItemListEasy = []
    _tempItemListMedium = []
    _tempItemListHard = []
    _tempItemListRandom = []
    _tempItemListDungeon = []
    _itemEnemyItems = []
    itemEnemyItems = []
    itemEnemyAddStats = [0, 0, 0, 0, 0, 0, 0]
    lootItemID = 1
    itemKeyList = [key for key in itemsDict]                                          
    for i in itemKeyList:
        if  itemsDict[i][10] == 7:
            _tempItemListEasy.append(i)
        elif itemsDict[i][10] == 8:
            _tempItemListMedium.append(i)
        elif itemsDict[i][10] == 9:
            _tempItemListHard.append(i)
        elif itemsDict[i][10] == 14+selectedDictID:
            _tempItemListDungeon.append(i)
                                                                             # Choose witch Items (Easy, Medium, Hard)
    if selectedDictID == 1:
        _tempItemList = _tempItemListEasy
    elif selectedDictID == 2:
        _tempItemList = _tempItemListMedium
    elif selectedDictID == 3:
        _tempItemList = _tempItemListHard
    
                                 # give Random Item from List as Lootitem
    while True:
        lootChanceEquipment = random.randint(1,3)
        j = random.randint(0,len(_tempItemList)-1)
        lootItemID = _tempItemList[j]
        if itemsDict[lootItemID][11] > 0 and lootChanceEquipment < 3:
            continue
        else:
            break

    
    jd = random.randint(0,len(_tempItemListDungeon)-1) 
    if enemyID == sorted(selectedDict.keys())[-1]:                   # in Dungeons give random Item from Dungeonitems
        lootItemID = _tempItemListDungeon[jd]                           # Bossloot!

    for y in range(1,3):                                                                                    
        
        for k in itemsDict:
           
            if itemsDict[k][10] > 0 and itemsDict[k][10] < 15:                      # from all choosen Items, append one Primary and Secondary Equipment to enemyItems
                if itemsDict[k][11] == y or itemsDict[k][11] == (y + 10):
                    _tempItemListRandom.append(k)
        if bool(_tempItemListRandom) == True:
            o = random.randint(0,len(_tempItemListRandom)-1)                
            _itemEnemyItems.append(_tempItemListRandom[o])
            _tempItemListRandom = []

    enemyWithoutEquipment = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009] ### chould be changed later after testing

    if enemyID not in enemyWithoutEquipment:
        for s in _itemEnemyItems:                                                   # Values for adding Stats to enemy    
            itemEnemyAddStats[3] += round(itemsDict[s][3])
            itemEnemyAddStats[4] += round(itemsDict[s][4])     
                                                                                         # Names of enemy Items
        for t in _itemEnemyItems:
            itemEnemyItems.append(itemsDict[t][2])  

    else: 
        itemEnemyItems = ["Claws", "Body"]
            

    
    return itemEnemyItems, itemEnemyAddStats, lootItemID  



#############################################################################################################################################################################
#---------------------------------------------------------------------------------- FIGHT ----------------------------------------------------------------------------------#
#############################################################################################################################################################################



################################################################################### FIGHT ###################################################################################
def Fight(startLocation, playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID):
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    #Enemy: 0 Name,        1 LVL+, 2 HP, 3 ATK, 4 DEF, 5 LVL, 6 Pic   
    _tempMoney = 0.00
    _tempExp = 0.00
    itemAddStats = []
    itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict)
    itemEnemyItems, itemEnemyAddStats, lootItemID  = EnemyItemSelection(itemsDict, enemyID, selectedDict, selectedDictID) 
    (selectedDict[enemyID][6]())
    while True:
        
        if playerStats[2] <= 0:                                                            	    # if player dead
            sleep(2)
            PicDeath()
            sleep(4)
            PicFairie()
            playerInventoryMoney -= round(playerInventoryMoney * 0.1,2)
            playerStats[5] *= 0.25
            location = "the town"
            playerStats[2] = 1
            break

        elif selectedDict[enemyID][2] <= 0:                                                         # if enemy dead
            print(f"\n--- {cl.RED}{selectedDict[enemyID][0]}{cl.RESET} has been eleminated ---")
            # sleep(2)
            _tempMoney += (round((selectedDict[enemyID][1] + selectedDict[enemyID][2] + selectedDict[enemyID][3] + selectedDict[enemyID][4]) / 9.6 ,2))
            if _tempMoney < 0:
                _tempMoney = 0.00
            _tempExp += (round((selectedDict[enemyID][1] + 2 - playerStats[0]) * (selectedDict[enemyID][2] + selectedDict[enemyID][3])*9.4 ,2))
            if _tempExp < 0:
                _tempExp = 0.00
            print(f"\nYou received {cl.YELLOW}{itemsDict[lootItemID][2]}{cl.RESET}, {cl.YELLOW}{round(_tempMoney,2)}{cl.RESET} Gold and {cl.YELLOW}{round(_tempExp,2)}{cl.RESET} Experience.")
            if _tempMoney < 0:
                _tempMoney = 0
            if _tempExp < 0:
                _tempExp = 0
            playerInventoryMoney += _tempMoney
            playerStats[5] += _tempExp
            itemsDict[lootItemID][8] += 1            
            break
  
        #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
        #Enemy: 0 Name,        1 LVL+, 2 HP, 3 ATK, 4 DEF, 5 LVL, 6 Pic
        
        if location == "dungeon castle" or location == "dungeon slumps" or location == "dungeon cave":
            UserInputFight = input(""\
            f"\n{cl.BLUE}{'{:<15}'.format(playerName)}{cl.RESET}\t\tLVL {cl.BLUE}{playerStats[0]}{cl.RESET}\tHP {cl.GREEN}{round(playerStats[2],2)}/{round(playerStats[1],2)}{cl.RESET}\n"\
            f"----------- VS -----------\n"\
            f"{cl.RED}{'{:<15}'.format(selectedDict[enemyID][0])}{cl.RESET}\t\tLVL {cl.BLUE}{selectedDict[enemyID][1]}{cl.RESET}\tHP {cl.BLUE}{round(selectedDict[enemyID][2],2)}/{round(enemyMaxHP,2)}{cl.RESET}\n\n"\
            f"(1) Attack\t(2) Inventory\t(3) Stats\t (0) Leave Dungeon\n")                                             # Fight (P = Player, E = Enemy)
            os.system('cls')
        else:
            UserInputFight = input(""\
            f"\n{cl.BLUE}{'{:<15}'.format(playerName)}{cl.RESET}\t\tLVL {cl.BLUE}{playerStats[0]}{cl.RESET}\tHP {cl.GREEN}{round(playerStats[2],2)}/{playerStats[1]}{cl.RESET}\n"\
            f"----------- VS -----------\n"\
            f"{cl.RED}{'{:<15}'.format(selectedDict[enemyID][0])}{cl.RESET}\t\tLVL {cl.BLUE}{selectedDict[enemyID][1]}{cl.RESET}\tHP {cl.BLUE}{round(selectedDict[enemyID][2],2)}/{round(enemyMaxHP,2)}{cl.RESET}\n\n"\
            f"(1) Attack\t(2) Inventory\t(3) Stats\t (0) Flee\n")                                             # Fight (P = Player, E = Enemy)
            os.system('cls')

    ################# 1 Attack ###############
        
        if UserInputFight == "1":
            (selectedDict[enemyID][6]())
            itemAddStats = []
            itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict)
            blockMessage = ""
            critMessage = "" 
            blockChance = 0
            critChance = 0
            hitchance = 0
            blockChance = (random.randint(75,100))/100
            if blockChance >= 90:
                blockMessage = "(crit)"
            
            critChance = random.randint(0,100)
            if critChance >= 95:
                critDmg = 1.5
                critMessage = "(crit)"
            else:
                critDmg = 1 
            
            hitchance = (random.randint(1,101))
            if hitchance < 10:
                critMessage = "(miss)"
                critDmg = 0
                                                                                          # Player attacks first
            print(f"\nYou attack {cl.RED}{selectedDict[enemyID][0]}{cl.RESET} with {cl.YELLOW}{itemPlayerPrimary}{cl.RESET} and did {cl.YELLOW}{round((playerStats[3] + itemAddStats[3]) * critDmg,2)} {cl.YELLOW}{critMessage}{cl.RESET} damage.")
            sleep(0.5)
            print(f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET} defends himself with {cl.YELLOW}{itemEnemyItems[1]}{cl.RESET} and blocks {cl.BLUE}{round((selectedDict[enemyID][4] + itemEnemyAddStats[4]) * blockChance,2)}{cl.RESET} {cl.YELLOW}{blockMessage}{cl.RESET} damage.")
            sleep(0.5)
            if  (round((selectedDict[enemyID][4] + itemEnemyAddStats[4]) * blockChance,2)) < (round((playerStats[3] + itemAddStats[3]) * critDmg,2)):                               # P_DEF < E_ATK?
               selectedDict[enemyID][2] -= ((round((playerStats[3] + itemAddStats[3]) * critDmg,2)) - (round((selectedDict[enemyID][4]  + itemEnemyAddStats[4]) * blockChance,2))) # E_HP -= P_ATK - E_DEF
            else:
                print(f"{cl.YELLOW}Attack blocked{cl.RESET}")
            if selectedDict[enemyID][2] < 0:                                                                                                                  # HP < 0? Then HP 0
                selectedDict[enemyID][2] = 0
            print(f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET} has {cl.BLUE}{round(selectedDict[enemyID][2],2)}{cl.RESET} HP left.")
            sleep(1)

            if selectedDict[enemyID][2] > 0:                                                                 # Enemy alive?
                blockMessage = ""
                critMessage = ""        
                blockChance = 0
                critChance = 0
                hitchance = 0
                blockChance = (random.randint(75,100))/100
                if blockChance >= 90:
                    blockMessage = "(crit)"
                
                critChance = random.randint(0,100)
                if critChance >= 95:
                    critDmg = 1.5
                    critMessage = "(crit)"
                else:
                    critDmg = 1
                
                hitchance = (random.randint(1,101))
                if hitchance < 10:
                    critMessage = "(miss)"
                    critDmg = 0 

                print(f"{cl.RED}{selectedDict[enemyID][0]}{cl.RESET} attacks you with {cl.YELLOW}{itemEnemyItems[0]}{cl.RESET} and did {cl.RED}{round((selectedDict[enemyID][3] + itemEnemyAddStats[3])  * critDmg,2)}{cl.RESET} {cl.YELLOW}{critMessage}{cl.RESET} damage.")  # Enemy attacks second
                sleep(0.5)
                print(f"You defend yourself with {cl.YELLOW}{itemPlayerSecondary}{cl.RESET} and block {cl.BLUE}{(round((playerStats[4] + itemAddStats[4]) * blockChance,2))}{cl.RESET} {cl.YELLOW}{blockMessage}{cl.RESET} damage.")
                sleep(0.5)
                if (round((playerStats[4] + itemAddStats[4]) * blockChance,2)) < (round((selectedDict[enemyID][3] + itemEnemyAddStats[3])  * critDmg,2)):                       # E_DEF < P_ATK?
                    playerStats[2] -= ((round((selectedDict[enemyID][3] + itemEnemyAddStats[3]) * critDmg,2)) - (round((playerStats[4] + itemAddStats[4]) * blockChance,2)))  # P_HP -= E_ATK - P_DEF 
                else:   
                    print(f"{cl.YELLOW}Attack blocked{cl.RESET}")
                if playerStats[2] < 0:
                    playerStats[2] = 0                                                                                                                  # HP < 0? Then HP 0
                print(f"You have {cl.GREEN}{round(playerStats[2],2)}{cl.RESET} HP left.")
                sleep(1)
                

    ################ 2 Inventory ##############      
                  
        elif UserInputFight == "2":
            itemsDict, playerStats = Inventory.InventoryMenu(
                startLocation, location, itemsDict, playerName, playerInventoryMoney, playerStats)
            (selectedDict[enemyID][6]())

    ################ 3 Stats #################

        elif UserInputFight == "3":
            playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName, itemsDict)
            (selectedDict[enemyID][6]())

    ################ 4 Flee ################

    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #Enemy: 0 Name,        1 LVL+, 2 HP, 3 ATK, 4 DEF, 5 LVL, 6 Pic

        elif UserInputFight == "0":                                                                         # Flee (loose Gold + Enemy
            _temp1 = round(playerStats[0] * 0.1 *(selectedDict[enemyID][1] - playerStats[0]),2)
            if _temp1 < 0:
                _temp1 = 0                                                                   #        hits with 0.5 atk)
            playerInventoryMoney -= (_temp1)
            if playerInventoryMoney - (_temp1) <= 0:
                playerInventoryMoney = 0
            _temp2 = (round((selectedDict[enemyID][3] + itemEnemyAddStats[3]) / 2.5 ,2))
            if _temp2 < 0:
             _temp2 = 0
            playerStats[2] -= round(_temp2,2)
            if playerStats[2] < 0:
                    playerStats[2] = 0 
            print(f"You managed to flee while you distracted the enemy with {cl.RED}{round(_temp1,2)}{cl.RESET} gold,")
            print(f"but {cl.RED}{selectedDict[enemyID][0]}{cl.RESET} got a hit on you. You received {cl.RED}{round(_temp2,2)}{cl.RESET} dmg!")
            print(f"You have {cl.GREEN}{round(playerStats[2],2)}{cl.RESET} HP left.")
            if playerStats[2] <= 0:                                                                        # if player dead (from 1 atk)
                sleep(2)
                PicDeath()
                sleep(4)
                PicFairie()
                playerInventoryMoney -= round(playerInventoryMoney * 0.1,2)
                playerStats[5] *= 0.25
                location = "the town"
                playerStats[2] = 1
                break
            break
        else: 
            print(f"\n{cl.RED}You can't choose that?!{cl.RESET}")

    return playerInventoryMoney, playerStats, playerStatPoints, location

################################################################################ NO ENCOUNTER ###############################################################################
def EncounterLowLevel():
    print("'A dangerous sphere approaches you, but as you turn around, it disappears.")

def EncounterNothing():
    print("Phew, nothing happened here.")

def DungeonSelection(locationIndex, itemsDict):
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
    i = locationIndex - 200
    while True:
        if locationIndex == 200 + i:       
            if itemsDict[1900 + i][8] < 1:
                print(f"There seems to be a Dungeon here, if you get {cl.YELLOW}{itemsDict[1900 + i][2]}{cl.RESET} you can enter.\n")
                locationIndex = i
                break
            else:
                userInput = input(f"There seems to be a Dungeon here,\nuse {cl.YELLOW}{itemsDict[1900 + i][2]}{cl.RESET} and enter Dungeon?\n(1) Yes\t(2) No\n")
                os.system('cls')
                if userInput == ("2"):
                    locationIndex = i
                    break
                elif userInput == ("1"):
                    locationIndex = 200 + i
                    itemsDict[1900 + i][8] -= 1
                    break          
                else: 
                    print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}")
                    continue         
            
    return locationIndex, itemsDict

def Dungeon(startLocation, location, locationIndex, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
    enemyID = 0
    enemyDictEasy = {}
    enemyDictMedium = {}
    enemyDictHard = {}
    enemyList = []
    _tempEnemyList = []
    _tempLocation = location
    selectedDictID = 0
    enemyDictEasy, enemyDictMedium, enemyDictHard = Enemys.Enemys(enemyDictEasy, enemyDictMedium, enemyDictHard)
    # select enemyDict for DungeonLocation and get Enemies for Dungeon:
    if locationIndex == 201:
        selectedDict = enemyDictEasy
        location = "dungeon castle"
        selectedDictID = 1
    elif locationIndex == 202:
        selectedDict = enemyDictMedium
        location = "dungeon slumps"
        selectedDictID = 2
    elif locationIndex == 203:
        selectedDict = enemyDictHard
        location = "dungeon cave"
        selectedDictID = 3
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Level, 6 Pic
    
    # get ID's of all Enemys:    
    for i in selectedDict:
        _tempEnemyList.append(i) 
    # get ID's of last 3 Enemys:
    for j in range(len(_tempEnemyList)-3, len(_tempEnemyList)):
        enemyList.append(_tempEnemyList[j])      
    print(f"You now entered {location}")
    # make enemys maxLVL + give them Stats:    
    for enemyDict in enemyList:
        selectedDict[enemyDict][1] = (selectedDict[enemyDict][5]+3)           
        for k in range(2,5):
            selectedDict[enemyDict][k] += round((selectedDict[enemyDict][1] - selectedDict[enemyDict][5]) * (selectedDict[enemyDict][5] * 0.5))
    # fight Enemys:
    for enemyID in enemyList:
        os.system('cls')
        enemyMaxHP = (selectedDict[enemyID][2])  
        playerInventoryMoney, playerStats, playerStatPoints, location = Fight(
            startLocation, playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID)
        if location == "the town":
            location = _tempLocation
            _tempLocation = "the town"
            break

    # Leave Dungeon:    
    print(f"You left {location}, you are now in {_tempLocation}")
    location = _tempLocation  

    return startLocation, location, locationIndex, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict



#############################################################################################################################################################################
#----------------------------------------------------------------------------------- PICS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################


######################################## Death ##################################################

def PicDeath():
    print(f"""
           
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................

          --- {cl.RED}You have been defeated{cl.RESET} ---

         """)


def PicFairie():
    print("\nYour head feels dizzy.")
    sleep(2) 
    print("A beautiful (fully naked) fairie helps you back to the town.")
    sleep(4)
    print("""
      .--.   _,
  .--;    \ /(_
 /    '.   |   '-._    . ' .
|       \  \    ,-.)  -= * =-
 \ /\_   '. \((` .(    '/. '
  )\ /     \ )\  _/   _/
 /  \\\    .-'   '--. /_\\
|    \\\_.' ,        \/||
\     \_.-';,_) _)'\ \||
 '.       /`\   (   '._/
   `\   .;  |  . '.
     ).'  )/|      \\
     `    ` |  \|   |
             \  |   |
              '.|   |
                 \  '\__
                  `-._  '. _
                     \`;-.` `._
                      \ \ `'-._\\
                       \ |
                        \ )
                         \_\\    
    """)

    print(f"She thankfully took some of your {cl.RED}gold{cl.RESET} in advance.")
    sleep(2)



