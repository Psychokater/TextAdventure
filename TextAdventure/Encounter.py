import random
# from time import sleep
import Stats
import Inventory



def Encounter(startLocation, location, playerStats, playerStatPoints, playerInventoryMoney, playerName, itemsDict):
 
   # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
    locationIndex = 0
    enemyID = 0
    enemyLevel = random.randint(playerStats[0]-1, playerStats[0]+2)

    enemyDictEasy = {
            1001 : ["Pack of Rats", enemyLevel, 2, 1, 0, 1.00, PicRat],
            1002 : ["Wolf", enemyLevel, 10, 2, 1, 2.00, PicWolf],
            1003 : ["Skeleton", enemyLevel, 5, 2, 2, 2.00, PicSkeleton]
            } #Enemy: 0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic
            

    enemyDictMedium = {
            1011 : ["Ghost", enemyLevel, 15, 4, 5, 6.00, PicGhost],
            1012 : ["Bandit", enemyLevel, 20, 6, 4, 8.00, PicBandit],
            1013 : ["Troll", enemyLevel, 30, 2, 1, 8.00, PicTroll],
            1014 : ["Centaur", enemyLevel, 20, 8, 10, 10.00, PicCentaur]
            } #Enemy: 0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic

    enemyDictHard = {
            1101 : ["Minotaur", enemyLevel, 20, 10, 4, 15.00, PicMinotaur],
            1102 : ["Gryphon", enemyLevel, 25, 10, 8, 20.00, PicGryphon],
            1103 : ["Dragon", enemyLevel, 50, 20, 30, 30.00, PicDragon]
            }# Enemy: 0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic
    

    if location == startLocation:
        locationIndex = 1
    elif location == "the town":
        PicTheTown()
        itemsDict, playerInventoryMoney, playerStats = Inventory.ShopMenu(itemsDict, playerName, playerInventoryMoney, playerStats)
        return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict   
    elif location == "the flatlands":
        locationIndex = 1
    elif location == "the forrest":
        locationIndex = 2
    elif location == "the islands":
        locationIndex = 6
    elif location == "the mountains":
        locationIndex = 8
    elif location == "the castle":
        locationIndex = 10
    
    luck = random.randint(1,100)
    encounterIndex = round(luck - (luck * (playerStats[0]) * 0.01) - locationIndex)             # high = good, low = bad, max = 100 (lvl 1, location 1)    
    enemyID, selectedDict = EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard)                     
    
 


    if enemyID != 0:
        
        
        enemyMaxHP = (selectedDict[enemyID][2])  
        (selectedDict[enemyID][6]())                                                            # select Enemy with ID from Dict (Random) -> see EnemySelection()
        while True:
            
            UserInputChoose = input(""\
            f"\n{playerName}\t\tLVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}\n"\
            f"----------- VS -----------\n"\
            f"{selectedDict[enemyID][0]}\t\tLVL {selectedDict[enemyID][1]}\tHP {selectedDict[enemyID][2]+selectedDict[enemyID][1]*2}/{enemyMaxHP}\n\n"\
            f"What do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(4) Flee\n")

            if UserInputChoose == "1":
                playerInventoryMoney, playerStats, playerStatPoints, location = Fight(
                    playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict, )
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
                print(f"""\nYou managed to escape the fight, you used up {round(_temp,2)} gold to distract your enemy.
                \nYou have {round(playerStats[2],2)} HP left.""")
                break
            else: 
                print("\nYou can't choose that?!")
        
    return location, playerStats, playerStatPoints, playerInventoryMoney, itemsDict


def EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard):       
    enemyID = 0                                                                                        #Edit this function later to config chances for Encounter
    selectedDict = {}
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    if encounterIndex <= 10:
        EncounterNothing()

    elif encounterIndex > 10 and encounterIndex <= 20:
        _luck = random.randint(1,len(enemyDictHard))
        enemyID = 1100 + _luck
        selectedDict = enemyDictHard
    elif encounterIndex > 21 and encounterIndex <= 52:
        _luck = random.randint(1,len(enemyDictMedium))
        enemyID = 1010 + _luck
        selectedDict = enemyDictMedium
    elif encounterIndex > 53 and encounterIndex <= 100:
        _luck = random.randint(1,len(enemyDictEasy))
        enemyID = 1000 + _luck
        selectedDict = enemyDictEasy
    
    if selectedDict == enemyDictHard and playerStats[0] < 10:
        EncounterLowLevel()        
        enemyID = 0
    elif selectedDict == enemyDictMedium and playerStats[0] < 5:
        EncounterLowLevel()        
        enemyID = 0

    return enemyID, selectedDict

def EnemyItemSelection(itemsDict, enemyID):
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
    if enemyID <= 1010:
        _tempItemList = _tempItemListEasy
    elif enemyID > 1010 and enemyID <= 1100:
        _tempItemList = _tempItemListMedium
    elif enemyID > 1100:
        _tempItemList = _tempItemListHard
    
    j = random.randint(1,len(_tempItemList)-1)
                                          # give Random Item from List as Lootitem
    lootItemID = _tempItemList[j]

    for y in range(1,7):                                                                                    
        for k in itemsDict:
            if itemsDict[k][10] != 0:                                                              # from all choosen Items, append one of every type to enemyItems
                if itemsDict[k][11] == y or itemsDict[k][11] == (y + 10):
                    _tempItemListRandom.append(k)
            if bool(_tempItemListRandom) == True:
                o = random.randint(0,len(_tempItemListRandom)-1)                
                _itemEnemyItems.append(_tempItemListRandom[o])
                _tempItemListRandom = []

    for s in _itemEnemyItems:                                                   # Values for adding Stats to enemy    
        itemEnemyAddStats[3] += itemsDict[s][3]
        itemEnemyAddStats[4] += itemsDict[s][4]

    for t in _itemEnemyItems:
        itemEnemyItems.append(itemsDict[t][2])                                  # Names of enemy Items
            

    
    return itemEnemyItems, itemEnemyAddStats, lootItemID  

def Fight(playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, location, playerName, enemyMaxHP, itemsDict):
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    #EnemyDict:  0 Name, 1 LVL, 2 HP, 3 ATK, 4 DEF, 5 Dropvalue, 6 Pic   
    _tempMoney = 0.00
    _tempExp = 0.00
    itemAddStats = []
    itemAddStats, itemPlayerPrimary, itemPlayerSecondary = Stats.AdditionalStats(itemAddStats, itemsDict)
    itemEnemyItems, itemEnemyAddStats, lootItemID  = EnemyItemSelection(itemsDict, enemyID) 
   
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

        UserInputFight = input(""\
        f"\n{playerName}\t\tLVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}\n"\
        f"----------- VS -----------\n"\
        f"{selectedDict[enemyID][0]}\t\tLVL {selectedDict[enemyID][1]}\tHP {selectedDict[enemyID][2]}/{enemyMaxHP}\n\n"\
        f"(1) Attack\t(2) Inventory\t(3) Stats\t (4) Flee\n")                                             # Fight (P = Player, E = Enemy)
        
    ################# 1 Attack ############    
        if UserInputFight == "1":                                                                           # Player attacks first
            print(f"\nYou attack {selectedDict[enemyID][0]} with {itemPlayerPrimary} and did {playerStats[3] + itemAddStats[3]} damage.")
            # sleep(1)
            print(f"{selectedDict[enemyID][0]} defends himself with {itemEnemyItems[2]} and blocks {selectedDict[enemyID][4] + itemEnemyAddStats[4]} damage.")
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




######################################## Enemys ##################################################

def PicRat():
    print("""
    'Two rats walk into a bar...
    ...the bar had to be shut down due to health violations.'
    
     ~~(  )8:>    <;3(  )~~
     """)

def PicWolf():
    print("""
    'What do you call a wolf with Stockholm Syndrome?...
    ...a Dog.'

                /^._        Bark
  ,___,--~~~~--' /'~ Bark
  `~--~\ )___,)/'               Bark
      (/\\\_  (/\\\_
       """)   


def PicSkeleton():
    print("""
    'The average human body contains enough bones...
    ...to make an entire human skeleton'

      .-.
     (o.o)
      |=|
     __|__
   //.=|=.\\\\
  // .=|=. \\\\
  \\\\ .=|=. //
   \\\\(_=_)//
    (:| |:)
     || ||
     () ()
     || ||
     || ||
     
     """)

def PicGhost():
    print("""
    'What is your religion? Mine is Boo-ddhism'
       .-.
      ( " )
   /\_.' '._/\\
   |         |
    \       /
     \    /`
   (__)  /
   `.__.'
    """)

def PicBandit():
    print("""
    'Broke into someones home last night, searching for money.
    He woke up, but started searching with me'
  <=======]}======
    --.   /|
   _\\\"/_.'/
 .'._._,.'
 :/ \{}/
(L  /--',
   /  A \\
  ( /|| |
   \\ V\ |
    """)


def PicTroll():
    print("""
    'How do you kill a troll?
    Deactivate his LAN Adapter'

        .-\"\"\"\".
       /       \\
   __ /   .-.  .\\
  /  `\  /   \/  \\
  |  _ \/   .==.==.
  | (   \  /____\__\\
   \ \      (_()(_()
    \ \            '---._
     \                   \_
  /\ |`       (__)________/
 /  \|     /\___/
|    \     \||VV
|     \     \|\"\"\"\",
|      \     ______)
\       \  /`
 \\       \(

    """)

def PicCentaur():
    print("""
    'Shopping is quite a hassle.
    Shirts are not the problem, 
    but how the fuck am I supposed to find fitting pants?'
                __
               / _\ #
               \c /  #
               / \___ #
               \`----`#==>  
               |  \  #
    ,%.-\"\"\"---'`--'\#_
   %%/             |__`\\
  .%'\     |   \   /  //
  ,%' >   .'----\ |  [/
     < <<`       ||
      `\\\\       ||
        )\\\      )\\
    """)

def PicMinotaur():
    print("""
    'I am so fuckin horny'
     .      .
     |\____/|
    (\|----|/)
     \ 0  0 /
      |    |
   ___/\../\____
  /     --       \\
 /  \         /   \\
|    \___/___/(   |
\   /|  }{   | \  )
 \  ||__}{__|  |  |
  \  |;;;;;;;\  \ / \_______
   \ /;;;;;;;;| [,,[|======'
     |;;;;;;/ |     /
     ||;;|\   |
     ||;;/|   /
     \_|:||__|
      \ ;||  /
      |= || =|
      |= /\ =|
      /_/  \_\\

        """)

def PicGryphon():
    print(""" 
    'Yeah do not pretend we are free air carrier for some hobbits
    to throw this stupid ring into lava.' 
                        ______
             ______,---'__,---'
         _,-'---_---__,---'
  /_    (,  ---____',
 /  ',,   `, ,-'
;/)   ,',,_/,'
| /\   ,.'//\\
`-` \ ,,'    `.
     `',   ,-- `.
     '/ / |      `,         _
     //'',.\_    .\\\\      ,{==>-
  __//   __;_`-  \ `;.__,;'
((,--,) (((,------;  `--'
""")

def PicDragon():
    print("""
    'It does not do to leave a live dragon out of your calculations, if you live near him.'      

                                             ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \\
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \\
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\\ V   V, /`     /
   ,--\(        ,     <_/`\\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`
                   
                   """)


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
  ..    ..-''    ;       ''. ' """)

