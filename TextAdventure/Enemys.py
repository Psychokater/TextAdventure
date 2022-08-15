#############################################################################################################################################################################
#--------------------------------------------------------------------------------- ENEMYS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################




def Enemys(enemyDictEasy, enemyDictMedium, enemyDictHard, enemyLevel):
    sl = round(enemyLevel / 1.5)
    
    enemyDictEasy = {
            1001 : ["Pack of Rats", enemyLevel,     4+sl,    2+sl,   1+sl,   1.00,   PicRat],
            1002 : ["Bird",         enemyLevel,     4+sl,    3+sl,   1+sl,   2.00,   PicBird],
            1003 : ["Wolf",         enemyLevel,     6+sl,    4+sl,   2+sl,   2.00,   PicWolf],
            1004 : ["Skeleton",     enemyLevel,     8+sl,    2+sl,   2+sl,   2.00,   PicSkeleton]
            }  #Enemy: 0 Name,       1 LVL,         2 HP,   3 ATK,   4 DEF,  5 Dropvalue, 6 Pic       
    enemyDictMedium = {
            1011 : ["Ghost",        enemyLevel,     10+sl,   4+sl,   2+sl,   6.00,   PicGhost],
            1012 : ["Bandit",       enemyLevel,     10+sl,   4+sl,   2+sl,   8.00,   PicBandit],
            1013 : ["Troll",        enemyLevel,     12+sl,   6+sl,   4+sl,   8.00,   PicTroll],
            1014 : ["Centaur",      enemyLevel,     15+sl,   8+sl,   5+sl,  10.00,   PicCentaur]
            }  #Enemy: 0 Name,       1 LVL,         2 HP,   3 ATK,   4 DEF,  5 Dropvalue, 6 Pic
    enemyDictHard = {
            1101 : ["Minotaur",     enemyLevel,     20+sl,   10+sl,  4+sl,  15.00,   PicMinotaur],
            1102 : ["Gryphon",      enemyLevel,     25+sl,   10+sl,  8+sl,  20.00,   PicGryphon],
            1103 : ["Dragon",       enemyLevel,     50+sl,   20+sl,  12+sl, 30.00,   PicDragon]
            }  #Enemy: 0 Name,       1 LVL,         2 HP,   3 ATK,   4 DEF,  5 Dropvalue, 6 Pic
    
    return enemyDictEasy, enemyDictMedium, enemyDictHard




#############################################################################################################################################################################
#------------------------------------------------------------------------------- ENEMY PICS --------------------------------------------------------------------------------#
#############################################################################################################################################################################




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

def PicBird():
    print("""
'Everybody heard about the bird, bird is the word!'
      ,~
     ('v)__
    (/ (``/
     \__>' 
      ^^
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


