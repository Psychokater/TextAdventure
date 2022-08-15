from math import ceil
import random
# from time import sleep
import Stats
import Inventory
import Enemys
import os



def Encounter(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
 
   # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
    locationIndex = 0
    enemyID = 0
    _locations = [startLocation, "the town", "the forest", "the flatlands", "the mountains", "the castle", "the islands"]
    _locationIndexList = [1,          100,            1,             2,               6,              8,          10]
    enemyLevel = random.randint(playerStats[0]-1, playerStats[0]+2)
    if enemyLevel <= 0:
        enemyLevel = 1
    
    enemyDictEasy = {}
    enemyDictMedium = {}
    enemyDictHard = {}
    enemyDictEasy, enemyDictMedium, enemyDictHard = Enemys.Enemys(enemyDictEasy, enemyDictMedium, enemyDictHard, enemyLevel)

    
    for i in range(0,len(_locations)):
        if location == _locations[i]:
            locationIndex = _locationIndexList[i]
            if locationIndex == 100:
                itemsDict, playerInventoryMoney, playerStats = Inventory.ShopMenu(itemsDict, playerName, playerInventoryMoney, playerStats)
                return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict 
            
                

    luck = random.randint(1,100)
    encounterIndex = round(luck - (luck * (playerStats[0]) * 0.01) - locationIndex)             # high = good, low = bad, max = 100 (lvl 1, location 1)    
    enemyID, selectedDict, selectedDictID = EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard)                     
    
    if enemyID != 0:
                
        enemyMaxHP = (selectedDict[enemyID][2])  
        (selectedDict[enemyID][6]())                                                            # select Enemy with ID from Dict (Random) -> see EnemySelection()
        while True:
            
            UserInputChoose = input(""\
            f"\n{playerName}\t\tLVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}\n"\
            f"----------- VS -----------\n"\
            f"{selectedDict[enemyID][0]}\t\tLVL {selectedDict[enemyID][1]}\tHP {selectedDict[enemyID][2]}/{enemyMaxHP}\n\n"\
            f"What do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(4) Flee\n")
            os.system('cls')

            if UserInputChoose == "1":
                playerInventoryMoney, playerStats, playerStatPoints, location = Fight(
                    playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID)
                break
            
            elif UserInputChoose == "2":
                itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)  

            elif UserInputChoose == "3": 
                playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName, itemsDict )

            elif UserInputChoose == "4": 
                _temp = (playerStats[0] * 2)
                playerInventoryMoney -= (playerStats[0] * 2)
                if playerInventoryMoney - (playerStats[0] * 2) < 0:
                    playerInventoryMoney = 0
                print(f"""\nYou managed to escape the fight, you used up {round(_temp,2)} gold to distract your enemy.
                \nYou have {round(playerStats[2],2)} HP left.""")
                break
            else: 
                print("\nYou can't choose that?!")
        
    return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict


def EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard):       
    enemyID = 0                                                                                        #Edit this function later to config chances for Encounter
    selectedDict = {}
    _tempList = []
    selectedDictID = 0
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    if encounterIndex <= 10:
        EncounterNothing()

    elif encounterIndex > 10 and encounterIndex <= 20:
        _luck = random.randint(0,len(enemyDictHard)-1)
        for i in enemyDictHard:
            _tempList.append(i)
        enemyID = _tempList[_luck]
        selectedDict = enemyDictHard
        selectedDictID = 3        
    elif encounterIndex > 21 and encounterIndex <= 52:
        _luck = random.randint(0,len(enemyDictMedium)-1)
        for i in enemyDictMedium:
            _tempList.append(i)
        enemyID = _tempList[_luck]
        selectedDict = enemyDictMedium
        selectedDictID = 2
    elif encounterIndex > 53 and encounterIndex <= 100:
        _luck = random.randint(0,len(enemyDictEasy)-1)
        for i in enemyDictEasy:
            _tempList.append(i)
        enemyID = _tempList[_luck]       
        selectedDict = enemyDictEasy
        selectedDictID = 1
    
    if selectedDictID == 3 and playerStats[0] < 20:
        EncounterLowLevel()        
        enemyID = 0
    elif selectedDictID == 2 and playerStats[0] < 10:
        EncounterLowLevel()        
        enemyID = 0

    return enemyID, selectedDict, selectedDictID

def EnemyItemSelection(itemsDict, enemyID, selectedDictID):
#Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6  Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
#Enemy: 0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic 
    _tempItemList = []
    _tempItemListEasy = []
    _tempItemListMedium = []
    _tempItemListHard = []
    _tempItemListRandom = []
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
                                                                             # Choose witch Items (Easy, Medium, Hard)
    if selectedDictID == 1:
        _tempItemList = _tempItemListEasy
    elif selectedDictID == 2:
        _tempItemList = _tempItemListMedium
    elif selectedDictID == 3:
        _tempItemList = _tempItemListHard
    
    j = random.randint(0,len(_tempItemList)-1)
                                                                       # give Random Item from List as Lootitem
    lootItemID = _tempItemList[j]

    for y in range(1,7):                                                                                    
        
        for k in itemsDict:
           
            if itemsDict[k][10] > 0:                                                      # from all choosen Items, append one of every type to enemyItems
                if itemsDict[k][11] == y or itemsDict[k][11] == (y + 10):
                    _tempItemListRandom.append(k)
        if bool(_tempItemListRandom) == True:
            o = random.randint(0,len(_tempItemListRandom)-1)                
            _itemEnemyItems.append(_tempItemListRandom[o])
            _tempItemListRandom = []

    enemyWithoutEquipment = [1001, 1002, 1003, 1011]

    if enemyID not in enemyWithoutEquipment:
        for s in _itemEnemyItems:                                                   # Values for adding Stats to enemy    
            itemEnemyAddStats[3] += itemsDict[s][3]
            itemEnemyAddStats[4] += itemsDict[s][4]      
                                                                                         # Names of enemy Items
        for t in _itemEnemyItems:
            itemEnemyItems.append(itemsDict[t][2])  

    else: 
        itemEnemyItems = ["Claws", "Body"]
            

    
    return itemEnemyItems, itemEnemyAddStats, lootItemID  

def Fight(playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, selectedDictID):
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic   
    _tempMoney = 0.00
    _tempExp = 0.00
    itemAddStats = []
    itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict)
    itemEnemyItems, itemEnemyAddStats, lootItemID  = EnemyItemSelection(itemsDict, enemyID, selectedDictID) 
   
    while True:

        if playerStats[2] <= 0:                                                            	    # if player dead
            # sleep(2)
            PicDeath()
            # sleep(4)
            PicFairie()
            playerInventoryMoney -= playerInventoryMoney * 0.1
            playerStats[5] *= 0.25
            location = "the town"
            playerStats[2] = 1
            break

        elif selectedDict[enemyID][2] <= 0:                                                         # if enemy dead
            print(f"\n--- {selectedDict[enemyID][0]} has been eleminated ---")
            # sleep(2)
            _tempMoney += ((selectedDict[enemyID][3] + selectedDict[enemyID][2] + selectedDict[enemyID][5]) / 2)
            _tempExp += (selectedDict[enemyID][5] * 100)
            print(f"\nYou received {itemsDict[lootItemID][2]}, {round(_tempMoney,2)} Gold and {round(_tempExp,2)} Experience.")
            playerInventoryMoney += _tempMoney
            playerStats[5] += _tempExp
            itemsDict[lootItemID][8] += 1            
            break
  
    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic
        (selectedDict[enemyID][6]())
        UserInputFight = input(""\
        f"\n{playerName}\t\tLVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}\n"\
        f"----------- VS -----------\n"\
        f"{selectedDict[enemyID][0]}\t\tLVL {selectedDict[enemyID][1]}\tHP {selectedDict[enemyID][2]}/{enemyMaxHP}\n\n"\
        f"(1) Attack\t(2) Inventory\t(3) Stats\t (4) Flee\n")                                             # Fight (P = Player, E = Enemy)
        os.system('cls')

    ################# 1 Attack ############    
        if UserInputFight == "1":                                                                           # Player attacks first
            print(f"\nYou attack {selectedDict[enemyID][0]} with {itemPlayerPrimary} and did {playerStats[3] + itemAddStats[3]} damage.")
            # sleep(1)
            print(f"{selectedDict[enemyID][0]} defends himself with {itemEnemyItems[1]} and blocks {selectedDict[enemyID][4] + itemEnemyAddStats[4]} damage.")
            # sleep(1)
            if  (selectedDict[enemyID][4] + itemEnemyAddStats[4]) < (playerStats[3] + itemAddStats[3]):                                                  # P_DEF < E_ATK?
                selectedDict[enemyID][2] += ((selectedDict[enemyID][4]  + itemEnemyAddStats[4]) - (playerStats[3] + itemAddStats[3]))                        # E_HP += E_DEF - P_ATK
            else:
                print("Attack blocked")
            if selectedDict[enemyID][2] < 0:                                                                    # HP < 0? Then HP 0
                selectedDict[enemyID][2] = 0
            print(f"{selectedDict[enemyID][0]} has {selectedDict[enemyID][2]} HP left.")
            # sleep(2)

            if selectedDict[enemyID][2] > 0:                                                                 # Enemy alive?

                print(f"{selectedDict[enemyID][0]} attacks you with {itemEnemyItems[0]} and did {selectedDict[enemyID][3] + itemEnemyAddStats[3]} damage.")        # Enemy attacks second
                # sleep(1)
                print(f"You defend yourself with {itemPlayerSecondary} and block {(playerStats[4] + itemAddStats[4])} damage.")
                # sleep(1)
                if (playerStats[4] + itemAddStats[4]) < selectedDict[enemyID][3] + itemEnemyAddStats[3]:                                                # E_DEF < P_ATK?
                    playerStats[2] += ((playerStats[4] + itemAddStats[4]) - (selectedDict[enemyID][3] + itemEnemyAddStats[3]))                 # P_HP += P_DEF - E_ATK 
                else:   
                    print("Attack blocked")
                if playerStats[2] < 0:
                    playerStats[2] = 0                                                                       # HP < 0? Then HP 0
                print(f"You have {playerStats[2]} HP left.")
                # sleep(1)

    ################ 2 Inventory ##############      
                  
        elif UserInputFight == "2":
               itemsDict, playerStats = Inventory.InventoryMenu(
                    itemsDict, playerName, playerInventoryMoney, playerStats)

    ################ 3 Stats #################

        elif UserInputFight == "3":
            playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName, itemsDict)

    ################ 4 Flee ################

    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic

        elif UserInputFight == "4":                                                                         # Flee (loose Gold + Enemy
            _temp1 = (playerStats[0] * 2)                                                                   #        hits with 0.5 atk)
            playerInventoryMoney -= (playerStats[0] * 2)
            if playerInventoryMoney - (playerStats[0] * 2) <= 0:
                playerInventoryMoney = 0
            _temp2 = (((selectedDict[enemyID][3] + itemEnemyAddStats[3]) / 2))
            playerStats[2] -= round(_temp2,2)
            if playerStats[2] < 0:
                    playerStats[2] = 0 
            print(f"You managed to flee while you distracted the enemy with {round(_temp1,2)} gold,")
            print(f"but {selectedDict[enemyID][0]} got a hit on you. You received {round(_temp2,2)} dmg!")
            print(f"You have {playerStats[2]} HP left.")
            if playerStats[2] <= 0:                                                                        # if player dead (from 1 atk)
                # sleep(2)
                PicDeath()
                # sleep(4)
                PicFairie()
                playerInventoryMoney -= playerInventoryMoney * 0.1
                playerStats[5] *= 0.25
                location = "the town"
                playerStats[2] = 1
                break
            break
        else: 
            print("\nYou can't choose that?!")

    return playerInventoryMoney, playerStats, playerStatPoints, location

# ########################################## No Encounter ##################################

def EncounterLowLevel():
    print("'A dangerous sphere approaches you, but as you turn around, it disappears.\nMaybe you escaped your downfall this time.'")

def EncounterNothing():
    print("Phew, nothing happened here.")



######################################## Death ##################################################

def PicDeath():
    print("""
           
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

          ---You have been defeated---

         """)


def PicFairie():
    print("\nYour head feels dizzy.")
    # sleep(2) 
    print("A beautiful (fully naked) fairie helps you back to the town.")
    # sleep(4)
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

    print("She thankfully took some of your gold in advance.")
    # sleep(2)



