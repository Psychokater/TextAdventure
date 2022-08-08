import random
from time import sleep
import Stats
import Inventory

def Encounter(startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney, playerName):
 
   # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
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
    enemyID = EnemySelection(encounterIndex, enemyDict)                        
    if enemyID != 0:
        (enemyDict[enemyID][5]())                                   # select Enemy with ID from Dict (Random) -> see EnemySelection()
        while True:

            UserInputChoose = input(f"""\n{playerName}: LVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}
            \nWhat do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(4) Flee\n""")
            if UserInputChoose == "1":
                playerInventoryMoney, playerStats, playerStatPoints, playerInventoryItems, location = Fight(
                    playerStats, playerStatPoints, enemyDict, enemyID, playerInventoryMoney, playerInventoryItems, location, playerName)
                break
            
            elif UserInputChoose == "2":
                playerInventoryItems, playerInventoryMoney = Inventory.InventoryMenu(
                playerInventoryItems, playerInventoryMoney, playerName)   

            elif UserInputChoose == "3": 
                playerStats, playerStatPoints = Stats.StatMenu(
                playerStats, playerStatPoints, playerName)

            elif UserInputChoose == "4": 
                _temp = (playerStats[0] * 2)
                playerInventoryMoney -= (playerStats[0] * 2)
                print(f"""\nYou managed to escape the fight, you used up {_temp} gold to distract your enemy.
                \nYou have {playerStats[2]} HP left.""")
                break
            else: 
                print("\nYou can't choose that?!")
        
    return location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney


def EnemySelection(encounterIndex, enemyDict):                                                                                  #Edit this function later to config chances for Encounter
    enemyID = 0
    
    if encounterIndex <= 10:
        EncounterNothing()
    elif encounterIndex > 10 or encounterIndex <= 100:
        _luck = random.randint(1,len(enemyDict))
        enemyID = 1000 + _luck
    return enemyID


def Fight(playerStats, playerStatPoints, enemyDict, enemyID, playerInventoryMoney, playerInventoryItems, location, playerName):
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    #EnemyDict:  0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic
    _lootItem = "lootItem" #(add Item later!!!)
    _tempMoney = 0.00
    _tempExp = 0.00

    while True:

        if playerStats[2] <= 0:                                                            	    # if player dead
            sleep(2)
            PicDeath()
            sleep(4)
            PicFairie()
            playerInventoryMoney -= playerInventoryMoney * 0.1
            playerStats[5] *= 0.25
            location = "the town"
            playerStats[2] = 1
            break

        elif enemyDict[enemyID][3] <= 0:                                                         # if enemy dead
            print("\n---Enemy has been eleminated---")
            sleep(2)
            _tempMoney += (enemyDict[enemyID][1] + enemyDict[enemyID][2] + enemyDict[enemyID][3]) / 2
            _tempExp += enemyDict[enemyID][4] * 100
            print(f"\nYou received {_lootItem}, {_tempMoney} Gold and {_tempExp} Experience.")
            playerInventoryMoney = _tempMoney
            playerStats[5] = _tempExp
            playerStats[2] = playerStats[1]
            break
  
    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

        UserInputFight = input(f"""
        \n{playerName}: LVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}
        \n(1) Attack\t(2) Inventory\t(3) Stats\t (4) Flee\n""")                                   # Fight (P = Player, E = Enemy)
        
    ################# 1 Attack ############    
        if UserInputFight == "1":                                                                           # Player attacks first
            print(f"\nYou attack {enemyDict[enemyID][0]} with {playerStats[3]} Points.")
            sleep(1)
            print(f"{enemyDict[enemyID][0]} defends himself with {enemyDict[enemyID][2]} Points.")
            sleep(1)
            if  enemyDict[enemyID][2] < playerStats[3]:                                                  # P_DEF < E_ATK?
                enemyDict[enemyID][3] += (enemyDict[enemyID][2] - playerStats[3])                      # E_HP += E_DEF - P_ATK
            else:
                print("Attack blocked")
            print(f"{enemyDict[enemyID][0]} has {enemyDict[enemyID][3]} HP left.")
            sleep(2)

            if enemyDict[enemyID][3] > 0:                                                                 # Enemy alive?

                print(f"{enemyDict[enemyID][0]} attacks you with {enemyDict[enemyID][1]} Points.")      # Enemy attacks second
                sleep(1)
                print(f"You defend yourself with {playerStats[4]} Points.")
                sleep(1)
                if playerStats[4] < enemyDict[enemyID][1]:                                               # E_DEF < P_ATK?
                    playerStats[2] += (playerStats[4] - enemyDict[enemyID][1])                          # P_HP += P_DEF - E_ATK 
                else:
                    print("Attack blocked")
                print(f"You have {playerStats[2]} HP left.")
                sleep(1)

    ################ 2 Inventory ##############      
                  
        elif UserInputFight == "2":
               playerInventoryItems, playerInventoryMoney = Inventory.InventoryMenu(
                playerInventoryItems, playerInventoryMoney, playerName)  

    ################ 3 Stats #################

        elif UserInputFight == "3":
            playerStats, playerStatPoints = Stats.StatMenu(playerStats, playerStatPoints, playerName)

    ################ 4 Flee ################
        elif UserInputFight == "4":                                                                         # Flee (loose Gold + Enemy
            _temp1 = (playerStats[0] * 2)                                                                   #        hits with 1 atk)
            playerInventoryMoney -= (playerStats[0] * 2)
            _temp2 = (enemyDict[enemyID][1])
            playerStats[2] -= enemyDict[enemyID][1]
            print(f"""You managed to flee while you distracted the enemy with {_temp1} gold,
            but {enemyDict[enemyID][0]} got a hit. You received {_temp2} dmg!
            You have {playerStats[2]} HP left.""")
            if playerStats[2] <= 0:                                                                        # if player dead (from 1 atk)
                sleep(2)
                PicDeath()
                sleep(4)
                PicFairie()
                playerInventoryMoney -= playerInventoryMoney * 0.1
                playerStats[5] *= 0.25
                location = "the town"
                playerStats[2] = 1
                break
            break
        else: 
            print("\nYou can't choose that?!")

    return playerInventoryMoney, playerStats, playerStatPoints, playerInventoryItems, location

# ########################################## No Encounter ##################################

def EncounterLowLevel():
    print("You couldn't find anything here, maybe you come back when you are stronger?")

def EncounterNothing():
    print("Phew, nothing happened here.")


# ######################################## Friends ################################################

def PicWanderer(): 
    print("""
    A mystic old man wanders through this valley, maybe he has something for you?
     
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

    print("She thankfully took some of your gold in advance.")
    sleep(2)