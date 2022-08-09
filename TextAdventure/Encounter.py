import random
from time import sleep
import Stats
import Inventory

def Encounter(startLocation, location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney, playerName):
 
   # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP 
    locationIndex = 0
    enemyID = 0

    enemyDictEasy = {
            1001 : ["Pack of Rats", 1.00, 0.00, 2.00, 1.00, PicRat],
            1002 : ["Wolf", 2.00, 1.00, 10.00, 2.00, PicWolf],
            1003 : ["Skeleton", 2.00, 2.00, 5.00, 2.00, PicSkeleton]
            } # 0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

    enemyDictMedium = {
            1011 : ["Ghost", 4.00, 5.00, 15.00, 6.00, PicGhost],
            1012 : ["Bandit", 6.00, 4.00, 20.00, 8.00, PicBandit],
            1013 : ["Troll", 2.00, 1.00, 30.00, 8.00, PicTroll],
            1014 : ["Centaur", 8.00, 10.00, 20.00, 10.00, PicCentaur]
            } # 0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

    enemyDictHard = {
            1101 : ["Minotaur", 10.00, 4.00, 20.00, 15.00, PicMinotaur],
            1102 : ["Gryphon", 15.00, 8.00, 25.00, 20.00, PicGryphon],
            1103 : ["Dragon", 20.00, 30.00, 50.00, 30.00, PicDragon]
            } # 0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic
    

    if location == startLocation:
        locationIndex = 1        
    elif location == "the town":
        locationIndex = 1
    elif location == "the flatlands":
        locationIndex = 2
    elif location == "the forrest":
        locationIndex = 1
    elif location == "the islands":
        locationIndex = 6
    elif location == "the mountains":
        locationIndex = 8
    elif location == "the castle":
        locationIndex = 10
    
    luck = random.randint(1,100)
    encounterIndex = round(luck - (luck * (playerStats[0]) * 0.01) - locationIndex) # high = good, low = bad, max = 100 (lvl 1, location 1)    
    enemyID, selectedDict = EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard)                        
    if enemyID != 0:
        (selectedDict[enemyID][5]())                                   # select Enemy with ID from Dict (Random) -> see EnemySelection()
        while True:

            UserInputChoose = input(f"""\n{playerName}: LVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}
            \nWhat do you want to do now?\n(1) Fight\t(2) Inventory\t(3) Stats\t(4) Flee\n""")
            if UserInputChoose == "1":
                playerInventoryMoney, playerStats, playerStatPoints, playerInventoryItems, location = Fight(
                    playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, playerInventoryItems, location, playerName)
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
                print(f"""\nYou managed to escape the fight, you used up {round(_temp,2)} gold to distract your enemy.
                \nYou have {round(playerStats[2],2)} HP left.""")
                break
            else: 
                print("\nYou can't choose that?!")
        
    return location, playerStats, playerStatPoints, playerInventoryItems, playerInventoryMoney


def EnemySelection(playerStats, encounterIndex, enemyDictEasy, enemyDictMedium, enemyDictHard):       
    enemyID = 0                                                                                        #Edit this function later to config chances for Encounter
    selectedDict = None
    print(f"TEST1:::EC: ",encounterIndex)
    #PlayerStats: # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    if encounterIndex <= 10:
        EncounterNothing()

    elif encounterIndex > 10 and encounterIndex <= 33:
        _luck = random.randint(1,len(enemyDictHard))
        enemyID = 1100 + _luck
        selectedDict = enemyDictHard
    elif encounterIndex > 33 and encounterIndex <= 66:
        _luck = random.randint(1,len(enemyDictMedium))
        enemyID = 1010 + _luck
        selectedDict = enemyDictHard
    elif encounterIndex > 66 and encounterIndex <= 100:
        _luck = random.randint(1,len(enemyDictEasy))
        enemyID = 1000 + _luck
        selectedDict = enemyDictHard
    print("TEST2::: ",enemyID,selectedDict)
    if selectedDict == enemyDictHard and playerStats[0] < 10:
        EncounterLowLevel()
        selectedDict = None
        enemyID = 0
    elif selectedDict == enemyDictMedium and playerStats[0] < 5:
        EncounterLowLevel()
        selectedDict = None
        enemyID = 0

    print("TEST3::: ",enemyID,selectedDict)
    return enemyID, selectedDict


def Fight(playerStats, playerStatPoints, selectedDict, enemyID, playerInventoryMoney, playerInventoryItems, location, playerName):
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

        elif selectedDict[enemyID][3] <= 0:                                                         # if enemy dead
            print("\n---Enemy has been eleminated---")
            sleep(2)
            _tempMoney += (selectedDict[enemyID][1] + selectedDict[enemyID][2] + selectedDict[enemyID][4]) / 2
            _tempExp += selectedDict[enemyID][4] * 100
            print(f"\nYou received {_lootItem}, {round(_tempMoney,2)} Gold and {round(_tempExp,2)} Experience.")
            playerInventoryMoney += _tempMoney
            playerStats[5] += _tempExp            
            break
  
    #PlayerStats: 0 Level, 1 HP 2 Atk, 3 Def, 4 Exp  
    #EnemyDict:  0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

        UserInputFight = input(f"""
        \n{playerName}: LVL {playerStats[0]}\tHP {playerStats[2]}/{playerStats[1]}
        \n(1) Attack\t(2) Inventory\t(3) Stats\t (4) Flee\n""")                                   # Fight (P = Player, E = Enemy)
        
    ################# 1 Attack ############    
        if UserInputFight == "1":                                                                           # Player attacks first
            print(f"\nYou attack {selectedDict[enemyID][0]} with {round(playerStats[3],2)} Points.")
            sleep(1)
            print(f"{selectedDict[enemyID][0]} defends himself with {round(selectedDict[enemyID][2],2)} Points.")
            sleep(1)
            if  selectedDict[enemyID][2] < playerStats[3]:                                                  # P_DEF < E_ATK?
                selectedDict[enemyID][3] += (round(selectedDict[enemyID][2],2) - round(playerStats[3],2))                        # E_HP += E_DEF - P_ATK
            else:
                print("Attack blocked")
            if selectedDict[enemyID][3] < 0:                                                                    # HP < 0? Then HP 0
                selectedDict[enemyID][3] = 0
            print(f"{selectedDict[enemyID][0]} has {round(selectedDict[enemyID][3],2)} HP left.")
            sleep(2)

            if selectedDict[enemyID][3] > 0:                                                                 # Enemy alive?

                print(f"{selectedDict[enemyID][0]} attacks you with {round(selectedDict[enemyID][1],2)} Points.")        # Enemy attacks second
                sleep(1)
                print(f"You defend yourself with {round(playerStats[4],2)} Points.")
                sleep(1)
                if playerStats[4] < selectedDict[enemyID][1]:                                                # E_DEF < P_ATK?
                    playerStats[2] += (round(playerStats[4],2) - round(selectedDict[enemyID][1],2))                            # P_HP += P_DEF - E_ATK 
                else:   
                    print("Attack blocked")
                if playerStats[2] < 0:
                    playerStats[2] = 0                                                                       # HP < 0? Then HP 0
                print(f"You have {round(playerStats[2],2)} HP left.")
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
            _temp1 = (playerStats[0] * 2)                                                                   #        hits with 0.5 atk)
            playerInventoryMoney -= (playerStats[0] * 2)
            _temp2 = (selectedDict[enemyID][1] / 2)
            playerStats[2] -= (selectedDict[enemyID][1] / 2)
            if playerStats[2] < 0:
                    playerStats[2] = 0 
            print(f"You managed to flee while you distracted the enemy with {round(_temp1,2)} gold,")
            print(f"but {selectedDict[enemyID][0]} got a hit on you. You received {_temp2} dmg!")
            print(f"You have {playerStats[2]} HP left.")
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
    print("A dangerous sphere approaches you, but as you turn around, it disappears.\n Maybe you escaped your downfall this time.")

def EncounterNothing():
    print("Phew, nothing happened here.")


# ######################################## Friends ################################################

def PicWanderer(): 
    print("""
    A mystic old man wanders through this valley, maybe he has some free candys?
     
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
    'buy two Potions, pay for three and get one for free!'
    
            /'''''''''''''''''''\\
           /_____/Merchant\\______\\     
            |       ____        |
            |      |_|_|        |
        ;,_<|_--_----__----___--|\_
              \\_/        \\_/     
    """)    



######################################## Enemys ##################################################

def PicRat():
    print("""
    'Two rats walk into a bar...
    ...the bar had to be shut down due to health violations.'
    
     ~~(  )8:>    <;3(  )~~
     """)

def PicWolf():
    print("""
    'What do you call a wolf with Stockholm Syndrome?
    A Dog.'

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