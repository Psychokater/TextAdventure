from time import sleep

# def Start(dataSaveList):
#     #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]    
#     playerName = dataSaveList[2]
#     startLocation = dataSaveList[3]
#     location = dataSaveList[4]
#     _startLocations = ["a small homestead", "a comfy cabin", "a small tent", "a cave"]
#     # sleep(2)
#     startLocation = _startLocations[random.randint(0,len(_startLocations)-1)]
#     location = startLocation ### FOR TESTING CHANGE THIS: ## CHANGE FROM "location = startLocation" TO "location = "the flatlands"  ONLY FOR TESTING!!!!!!
#     while True:
#         playerName = input("\nHis Name was:\n").capitalize()
#         os.system('cls')
#         if playerName.isdigit():
#             print ("Enter a real warrior name you're not a number! ")
#             # sleep(2)
#             continue
#         elif playerName == "":
#             print("Hey, get a name! You are not 'nothing'!")
#             # sleep(2)
#             continue
#         else:
#             break
#     sleep(0.5)
#     print(f"\nWelcome to your first adventure {playerName}!")
#     sleep(0.5)
#     print(f"\nYou wake up in {location}")
#     PicStartFire()
#     sleep(0.5)    
#     dataSaveList[2] = playerName
#     dataSaveList[3] = startLocation
#     dataSaveList[4] = location

#     return dataSaveList

def IntroAnimation():
  print("""











  Once upon a time...
              """)

  sleep(4)

  print("""
      
                                                      .
     .                  ,d88b,                                        .                   __..-
                        888888                                           .            .--SEAL:.
          .             `?88P'            .                       __                ,'WWII::.
                                                                .MW:`-.            /WWII::..
                                                        .    _.MWII:'. `.     .  ,'WII::..
                                                          _.-MWII::'.     `-.   ,'WWI::.
         _._ _                                   _..vvvv,'WWII::'            `.'WII::.
        (__((_(                               ,-'WI:'''/WII:'.                 \WI:.
  _____;'-:--:-/____________________________,'WWI:'.  /WI:'.          :.        `.I:.
        '-----'        ~~~ - .,,           ,'WWI:'.  ,'I:.              ::.        \..
                    ~~~ - ~-~_~ _        /\?I:'.   /WI:.       ,.       ::.        \ .
                  ~-~-,-~ ~~,,,.~~~      /  )------'WI:.____ _.d88P_____::::.        \.
                          
  
  ...there was a hopeful land with peaceful people and ongoing trade...""")


  sleep(8)


  print("""

                    _.--.    .--._
                  ."  ."      ".  ".
                  ;  ."    /\    ".  ;
                  ;  '._,-/  \-,_.`  ;
                  \  ,`  / /\ \  `,  /
                  \/    \/  \/    \/
                  ,=_    \/\/    _=,
                  |  "_   \/   _"  |
                  |_   '"-..-"'   _|
                  | "-.        .-" |
                  |    "\    /"    |
                  |      |  |      |
          ___     |      |  |      |     ___
      _,-",  ",   '_     |  |     _'   ,"  ,"-,_
    _(  \  \   \.=--"-.  |  |  .-"--=./   /  /  )_
  ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
  !     \  \  \   \                  /   /  /  /     !
  :      \  \  \   \                /   /  /  /      

  ...but than one day, Osama, brother of the rightfull crown prince became greedy...""")
  sleep(8)

  print("""




                          .
                         / \\
                        _\ /_
              .     .  (,'v`.)  .     .
              \)   ( )  ,' `.  ( )   (/
               \`. / `-'     `-' \ ,'/
                : '    _______    ' :
                |  _,-'  ,-.  `-._  |
                |,' ( )__`-'__( ) `.|
                (|,-,'-._   _.-`.-.|)     
                  ,   .-.   .-.   ,        
                    ) (__/   \__) (   
                  /      /\      \ 
                  (_      ^^      _)         
                    \___|uuuu|___/       
                        (nnnn)



  he attacked the crowns guard and took what he waited for so long.
              """)
  sleep(8)
  print("""


                              ==(W{==========-      /===-                        
                                ||  (.--.)         /===-_---~~~~~~~~~------____  
                                | \_,|**|,__      |===-~___                _,-' `
                  -==\.\       `\ ' `--'   ),    `//~\.\  ~~~~`---.___.-~~      
              ______-==|        /`\_. .__/\ \    | |  \.\         _-~`         
        __--~~~  ,-/-=\.\      (   | .  |~~~~|   | |    `\      ,'             
      _-~       /'    | \.\     )__/==0==-\<>/   / /       \    /               
    .'        /       |  \.\      /~\___/~~\/  /' /         \  /'                
  /  ____  /         |   \`\.__/-~~   \  |_/'  /           \/'                  
  /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   
                    \_|      /        _) | ;  ),   __--~~                        
                      '~~--_/      _-~/- |/ \   '-~ \                            
                    {\__--_/}    / \.\_>-|)<_\      \                           
                    /'   (_/  _-~  | |__>--<__|      |                          
                    |   _/) )-~     | |__>--<__|      |                          
                    / /~ ,_/       / /__>---<__/      |                          
                  o-o _//        /-~_>---<__-~      /                           
                  (^(~          /~_>---<__-      _-~                            
                  ,/|           /__>--<__/     _-~                               
              ,//('(          |__>--<__|     /                  .----_          
              ( ( '))          |__>--<__|    |                 /' _---_~\        
          `-)) )) (           |__>--<__|    |               /'  /     ~\`\      
          ,/,'//( (             \__>--<__\    \            /'  //        ||      
        ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       
      `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  
    ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    
    ;'( ')/ ,)(                              ~~~~~~~~~~                         
    ' ') '( (/                                                                   
      '   '  `

  Osama formed an army to reach for the underworld, but he did not expect the heavy resistance, he fainted.
  """)

  sleep(8)

  print("""



                              ,.=,,==. ,,_                                 
              _ ,====, _    |I|`` ||  `|I `|     
            |`I|    || `==,|``   ^^   ``  |                                
            | ``    ^^    ||_,===TT`==,,_ | 
            |,==Y``Y==,,__| \L=_-`'   +J/`   
              \|=_  ' -=#J/..-|=_-     =|                                   
              |=_   -;-='`. .|=_-     =|----T--,                           
              |=/\  -|=_-. . |=_-/^\  =||-|-|::|____  
              |=||  -|=_-. . |=_-| |  =|-|-||::\____  
              |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::   
              |=_   -|=_-_.  |=_-     =|-|-||:::::::  
              |=_   -|=//^\. |=_-     =||-|-|:::::::  
          ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::  
        ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::  
    ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::  
  |;:;K`__,...;=\_____,=``           %%%&     %#,---  
  |;::::::::::::|       `'.________+-------\   ``                          
  /%;;:::;;:::::|                  |        `-------                       



  The new king commanded his army into battle, they should not leave anything alive, not foe, not friend....
  """)
  sleep(8)

  print("""



                              .
                             / \\
                            _\ /_
                  .     .  (,'v`.)  .     .
                  \)   ( )  ,' `.  ( )   (/
                    \`. / `-'     `-' \ ,'/
                    : '    _______    ' :
                    |  _,-'  ,-.  `-._  |
                    |,' ( )__`-'__( ) `.|
                    (|,-,'-._   _.-`.-.|)
                    /  /<( ° ) ( ° )>\  \\
                    :  :     | |     :  :
                    |  |     ; :     |  |
                    |  |    (.-.)    |  |
                    |  |  ,' ___ `.  |  |
                    ;  |)/ ,'---'. \(|  :
                _,-/   |/\(       )/\|   \-._
          _..--'.-(    |   `-'''-'   |    )-.`--.._
                    `.  ;`._________,':  ,'
                  ,' `/               \\'`.
                        `------.------'     


  ...he became mad as his whole new kingdom sunk into chaos...

  """)
  sleep(8)
  print("""







  
  ... but there was hope, an adventurer on his new quest to free the land.

  His name was...

  """)

  sleep(4)
