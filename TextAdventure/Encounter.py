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
    playerStats = _playerStats #Level, HP, Atk, Def, Exp  
    startLocation = _startLocation
    location = _location
    locationIndex = 0
    enemyID = 0

    enemyDict = {
            1001 : ["Pack of Rats", 1, 0, 2, 1, PicRat],
            1002 : ["Wolf", 3, 1, 10, 2, PicWolf],
            1003 : ["Bandit", 6, 4, 20, 4, PicBandit],
            1004 : ["Troll", 2, 1, 30, 10, PicTroll],
            1005 : ["Centaur", 8, 10, 20, 15, PicCentaur],
            1006 : ["Minotaur", 10, 4, 20, 15, PicMinotaur],
            1007 : ["Dragon", 20, 30, 50, 10, PicDragon]
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
        (enemyDict[enemyID][5]())                                   # select Enemy with ID from Dict (Random) -> see EnemySelection()
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


def EnemySelection(_encounterIndex):
    enemyID = 0
    
    if _encounterIndex <= 10:
        EncounterNothing()
    elif _encounterIndex > 10 or _encounterIndex <= 100:
        _luck = random.randint(1,len(enemyDict))
        enemyID = 1000 + _luck
    return enemyID


def Fight(_playerStats, _enemyDict, _enemyID, _playerInventoryMoney, _playerInventoryItems, _location):
    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic
    lootItem = "lootItem" #(add Item later!!!)
    tempMoney = 0.00
    tempExp = 0.00

    while True:

        if _playerStats[1] <= 0:                                                        # if player dead
            sleep(2)
            PicDeath()
            sleep(2)
            PicFairie()
            _playerInventoryMoney -= _playerInventoryMoney * 0.1
            _playerStats[4] *= 0.25
            _location = "the town"
            _playerStats[1] = 1
            break

        elif _enemyDict[_enemyID][3] <= 0:                                                # if enemy dead
            print("\n---Enemy has been eleminated---")
            sleep(2)
            tempMoney += (_enemyDict[_enemyID][1] + _enemyDict[_enemyID][2] + _enemyDict[_enemyID][3]) / 2
            tempExp += _enemyDict[_enemyID][4] * 100
            print(f"\nYou received {lootItem}, {tempMoney} Gold and {tempExp} Experience.")
            _playerInventoryMoney = tempMoney
            _playerStats[4] = tempExp
            _playerStats[1] = _playerStats[1]
            break
  
    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

        UserInputFight = input("\n(1) Attack\t(2) Inventory\t(3) Flee\n")                                   # Fight (P = Player, M = Monster)
        if UserInputFight == "1":                                                                           # Player attacks first
            print(f"\nYou attack {_enemyDict[_enemyID][0]} with {_playerStats[2]} Points.")
            sleep(1)
            print(f"{_enemyDict[_enemyID][0]} defends himself with {_enemyDict[_enemyID][2]} Points.")
            sleep(1)
            if  _enemyDict[_enemyID][2] < _playerStats[2]:                                                 # P_DEF < M_ATK?
                _enemyDict[_enemyID][3] += (_enemyDict[_enemyID][2] - _playerStats[2])                     # M_HP += M_DEF - P_ATK
            else:
                print("Attack blocked")
            print(f"{_enemyDict[_enemyID][0]} has {_enemyDict[_enemyID][3]} HP left.")
            sleep(2)
            
            print(f"{_enemyDict[_enemyID][0]} attacks you with {_enemyDict[_enemyID][1]} Points.")          # Monster attacks second
            sleep(1)
            print(f"You defend yourself with {_playerStats[3]} Points.")
            sleep(1)
            if _playerStats[3] < _enemyDict[_enemyID][1]:                                                   # M_DEF < P_ATK?
                 _playerStats[1] += (_playerStats[3] - _enemyDict[_enemyID][1])                             # P_HP += P_DEF - M_ATK 
            else:
                print("Attack blocked")
            print(f"You have {_playerStats[1]} HP left.")
            sleep(1)
                        
        #elif UserInputFight == "2":
            #Main.InventoryMenu()
        elif UserInputFight == "3":                                                                          # Flee (loose Gold + Monster
            _temp1 = (_playerStats[0] * 2)                                                                   #        hits with 1 atk)
            _playerInventoryMoney -= (_playerStats[0] * 2)
            _temp2 = (_enemyDict[_enemyID][1])
            _playerStats[3] -= _enemyDict[_enemyID][1]
            print(f"""You managed to flee while you distracted the enemy with {_temp1} gold,
            but {_enemyDict[_enemyID][0]} got a hit. You received {_temp2} dmg!""")
            break
        else: 
            print("You can't choose that?!")

    return _playerInventoryMoney, _playerStats, _playerInventoryItems, _location


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
    print("""
    oh no, wolf!
                /^._        Bark
  ,___,--~~~~--' /'~ Bark
  `~--~\ )___,)/'               Bark
      (/\\\_  (/\\\_
       """)
    


def PicRat():
    print("""
    look, rats!
    
     ~~(  )8:>    <;3(  )~~
     """)

def PicBandit():
    print("""
    this thug wants your money!
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

def PicCentaur():
    print("""
    mythical creatures everywhere!
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

def PicTroll():
    print("""
    serious trolling here!
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

def PicMinotaur():
    print("""
    mythical creautures Everywhere!
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
            ---You have been defeated---

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
         """)


def PicFairie():
    print("""
                Your head feels dizzy.
            A beautiful (fully naked) fairie brought you back to the town.
            She thankfully took some of your gold in advance.
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
