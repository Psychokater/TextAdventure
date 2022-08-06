import random

def Encounter(_startLocation, _location, _playerLevel):
    global startLocation
    global location
    global playerLevel
    global encounterIndex
    startLocation = _startLocation
    location = _location
    playerLevel = _playerLevel  
    locationIndex = 0
    

    if location == startLocation:
        locationIndex = 1
    elif location == "the town":
        locationIndex = 2
    elif location == "the flatlands":
        locationIndex = 3
    elif location == "the forrest":
        locationIndex = 4
    elif location == "the islands":
        locationIndex = 5
    elif location == "the mountains":
        locationIndex = 6
    elif location == "the castle":
        locationIndex = 7
    
    luck = random.randint(1,100)
    encounterIndex = round(playerLevel * 10 * locationIndex / luck)
    return encounterIndex

    StartLocation()
    TheTown()
    Flatlands()
    Forrest()
    Islands()
    Mountains()
    Castle()

#
#  def grabEncounter(location, playerLevel)
#      global encounterIndex
#      
#
#
#


############################################ Start Location ################################

def StartLocation():
    global encounterIndex
    
    luck = random.randint(1,100)
    if luck == 100 and playerLevel > 5:
        print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
        encounterIndex = 20        
    if luck <= 10 and playerLevel > 5:
        EncounterWolf()
        encounterIndex = 2
    if luck > 10 and luck <= 30 and playerLevel > 5:
        EncounterRat()
        encounterIndex = 3
    if luck > 30 and luck <= 80 and playerLevel > 5:
        Nothing()
        encounterIndex = 0
    if luck > 80 and luck < 100 and playerLevel > 5:
        EncounterWanderer() 
        encounterIndex = 10
    if playerLevel < 5:
        LowLevel()



################################################ The Town ###########################################

def TheTown():
    global encounterIndex    
    Merchant()
    encounterIndex = 1
    

################################################ The Flatlands ###########################################

def Flatlands():
    global encounterIndex
    
    luck = random.randint(1,100)
    if luck == 100 and playerLevel > 5:
        print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
        encounterIndex = 20        
    if luck <= 10 and playerLevel > 5:
        EncounterWolf()
        encounterIndex = 2
    if luck > 10 and luck <= 30 and playerLevel > 5:
        EncounterRat()
        encounterIndex = 3
    if luck > 30 and luck <= 80 and playerLevel > 5:
        Nothing()
        encounterIndex = 0        
    if luck > 80 and luck < 100 and playerLevel > 5:
        EncounterWanderer() 
        encounterIndex = 10
    if playerLevel < 5:
        LowLevel()

################################################ The Forrest ###########################################

def Forrest():
    global encounterIndex
    
    luck = random.randint(1,100)
    if luck == 100 and playerLevel > 5:
        print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
        encounterIndex = 20        
    if luck <= 10 and playerLevel > 5:
        EncounterWolf()
        encounterIndex = 2
    if luck > 10 and luck <= 30 and playerLevel > 5:
        EncounterRat()
        encounterIndex = 3
    if luck > 30 and luck <= 80 and playerLevel > 5:
        Nothing()
        encounterIndex = 0
    if luck > 80 and luck < 100 and playerLevel > 5:
        EncounterWanderer() 
        encounterIndex = 10
    if playerLevel < 5:
        LowLevel()

################################################ The Islands ###########################################

def Islands():
    global encounterIndex
    
    luck = random.randint(1,100)
    if luck == 100 and playerLevel > 5:
        print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
        encounterIndex = 20        
    if luck <= 10 and playerLevel > 5:
        EncounterWolf()
        encounterIndex = 2
    if luck > 10 and luck <= 30 and playerLevel > 5:
        EncounterRat()
        encounterIndex = 3
    if luck > 30 and luck <= 80 and playerLevel > 5:
        Nothing()
        encounterIndex = 0        
    if luck > 80 and luck < 100 and playerLevel > 5:
        EncounterWanderer() 
        encounterIndex = 10
    if playerLevel < 5:
        LowLevel()

################################################ The Mountains ###########################################

def Mountains():
    global encounterIndex
    
    luck = random.randint(1,100)
    if luck == 100 and playerLevel > 5:
        print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
        encounterIndex = 20        
    if luck <= 10 and playerLevel > 5:
        EncounterWolf()
        encounterIndex = 2
    if luck > 10 and luck <= 30 and playerLevel > 5:
        EncounterRat()
        encounterIndex = 3
    if luck > 30 and luck <= 80 and playerLevel > 5:
        Nothing()
        encounterIndex = 0        
    if luck > 80 and luck < 100 and playerLevel > 5:
        EncounterWanderer() 
        encounterIndex = 10
    if playerLevel < 5:
        LowLevel()

################################################ THe Castle #######################################

def Castle():
    global encounterIndex
    
    luck = random.randint(1,100)
    if luck == 100 and playerLevel > 5:
        print("☆*:・ﾟnice, what a lucky day! (20 Gold found")
        encounterIndex = 20        
    if luck <= 10 and playerLevel > 5:
        EncounterWolf()
        encounterIndex = 2
    if luck > 10 and luck <= 30 and playerLevel > 5:
        EncounterRat()
        encounterIndex = 3
    if luck > 30 and luck <= 80 and playerLevel > 5:
        Nothing()
        encounterIndex = 0
    if luck > 80 and luck < 100 and playerLevel > 5:
        EncounterWanderer() 
        encounterIndex = 10
    if playerLevel < 5:
        LowLevel()



########################################## No Encounter ##################################

def LowLevel():
    print("You couldn't find anything here, maybe you come back when you are stronger?")

def Nothing():
    print("Phew, nothing happened here.")


######################################## Friends ################################################

def EncounterWanderer(): 
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



def Merchant():
    print("""
    
            /'''''''''''''''''''\\
           /_____/Merchant\\______\\     
            |       ____        |
            |      |_|_|        |
        ;,_<|_--_----__----___--|\_
              \\_/        \\_/     
    """)    



######################################## Enemys ##################################################



def EncounterWolf():
    print("""oh no, Wolf!
                /^._        Bark
  ,___,--~~~~--' /'~ Bark
  `~--~\ )___,)/'               Bark
      (/\\\_  (/\\\_
       """)
    


def EncounterRat():
    print("""look, ra3s!
    
     ~~(  )8\:"> <";3(   )~~""")



def EncounterDragon():
    print("""

    'It does not do to leave a live dragon out of your calculations, if you live near him.'      
            ,                      \,   
            /|           \    ,     |\         
            [ ,          |\  /|     | | 
            | |       ,.`  `,` `,  /  | 
            \  \  __ ,-` `  ,  , `/  /
            \  \_\,``,   ` , ,  /  /
            \  '  `  ,_ _`_,-,<._.<
                ', `>.,`  `  `   ,., |_
                \/`  `,   `   ,`  | /_
            -,-..\  _  \  `  /  ,  / `._)
            \_,,.) /\    ` /  / ) (-,, |
                )  | \_\       '-`  |  `(
                /```(   , --, ,' \   |`<` 
            /_,--`\   <\  V /> ,` )<_/)
            `   (_,\ \    |   /) / __/ 
                    ) \ ('_.-._)/ /,`   
                    `/ \\\ V    V ,/` \   
                    <_/`\\\       /|`\_>   
                        \-A.A-`|     
                        -,,_-`""")

