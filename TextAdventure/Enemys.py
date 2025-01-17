


#############################################################################################################################################################################
#--------------------------------------------------------------------------------- ENEMYS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################



def Enemys(enemyDictEasy, enemyDictMedium, enemyDictHard):
  
  enemyDictEasy = {
          1001 : ["Pack of Rats",      0,     4.0,    3.0,   2.0,   1,   PicRat],
          1002 : ["Bird",              0,     5.0,    4.0,   2.0,   1,   PicBird],
          1003 : ["Cave Bat",          0,     6.0,    5.0,   1.0,   2,   PicCaveBat],
          1004 : ["Minosaur ",         0,     8.0,    6.0,   3.0,   2,   PicMinosaur],
          1005 : ["Wild Cat",          0,    10.0,    5.0,   2.0,   3,   PicWildCat],
          1006 : ["Scorpion",          0,    12.0,    7.0,   4.0,   3,   PicScorpion],
          1007 : ["Wolf",              0,    14.0,    8.0,   5.0,   4,   PicWolf],
          1008 : ["Sea Crab",          0,    14.0,    5.0,   6.0,   4,   PicSeeCrab],
          1009 : ["Alligator",         0,    16.0,   10.0,   7.0,   5,   PicAlligator],
          1010 : ["Crazy Monkey",      0,    14.0,    6.0,   4.0,   5,   PicCrazyMonkey],
          1011 : ["Native Cannibal",   0,    18.0,    7.0,   3.0,   6,   PicNativeCannibal],
          1012 : ["Amateur Warrior",   0,    24.0,   12.0,   7.0,   7,   PicAmateurWarrior],
          1013 : ["Skeleton",          0,    17.0,   14.0,   3.0,   8,   PicSkeleton],
          1014 : ["ApeMan",            0,    20.0,   16.0,   5.0,   9,   PicApeMan],
          1015 : ["Mutant Fox",        0,    18.0,   17.0,   6.0,   9,   PicMutantFox],
          1016 : ["CyClops",           0,    24.0,   18.0,   8.0,  10,   PicCyclops]
          }  #Enemy: 0 Name,        1 LVL+, 2 HP, 3 ATK, 4 DEF, 5 LVL, 6 Pic
  enemyDictMedium = {   
          1101 : ["Ghost",             0,     10.0,   4.0,   2.0,  11,   PicGhost],
          1102 : ["Bandit",            0,     10.0,   4.0,   2.0,  14,   PicBandit],
          1103 : ["Troll",             0,     12.0,   6.0,   4.0,  16,   PicTroll],
          1104 : ["Centaur",           0,     15.0,   8.0,   5.0,  20,   PicCentaur]
          }  #Enemy: 0 Name,        1 LVL+, 2 HP, 3 ATK, 4 DEF, 5 LVL, 6 Pic
  enemyDictHard = {   
          1201 : ["Minotaur",          0,     20.0,   10.0,  4.0,  22,   PicMinotaur],
          1202 : ["Gryphon",           0,     25.0,   10.0,  8.0,  24,   PicGryphon],
          1203 : ["Dragon",            0,     50.0,   20.0, 12.0,  30,   PicDragon]
          }  #Enemy: 0 Name,        1 LVL+, 2 HP, 3 ATK, 4 DEF, 5 LVL, 6 Pic
     
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
###########################################################
def PicBird():
    print("""
'Everybody heard about the bird, bird is the word!'
      ,~
     ('v)__
    (/ (``/
     \__>' 
      ^^
    """)
##########################################################
def PicWolf():
    print("""
    'What do you call a wolf with Stockholm Syndrome?...
    ...a dog.'

                /^._        Bark
  ,___,--~~~~--' /'~ Bark
  `~--~\ )___,)/'               Bark
      (/\\\_  (/\\\_
       """)   

###############################################################
def PicWildCat():
  print ("""
  'Big Meaaaaooowwwwwwww'

      ( \.
       \ \.
       / /                |\\\\
      / /     .-`````-.   / ^`-.
      \ \    /         \_/  {|} `o
       \ \  /   .---.   \\\\ _  ,--'
        \ \/   /     \,  \( `^^^
         \   \/\      (\  )
          \   ) \     ) \ \.
           ) /__ \__  ) (\ \___
          (___)))__))(__))(__)))""")
#############################################################
def PicSeeCrab():
  print ("""
'If you hold a crab up to your ear...
...you can hear what it's like to be attacked by a crab!' 
       ___     ___
     .i .-'   `-. i.
   .'   `/     \.  _`.
   |,-../ o   o \.' `|
(| |   /  _\ /_  \   | |)
 \\\\\  (_.'.'"`.`._)  ///
  \\\\`._(..:   :..)_.'//
   \`.__\ .:-:. /__.'/
    `-i-->.___.<--i-'
    .'.-'/.=^=.\`-.`.
   /.'  //     \\\\  `.\.
  ||   ||       ||   ||
  \)   ||       ||  (/
       \)       (/     
  """)
#############################################################
def PicCaveBat():
  print ("""
  'Vampire bats that typically target large birds have been found to be sucking human blood now'

    =/\                 /\=
    /  \._   (\_/)  _.'/  \.
   / .''._'--(o.o)--'_.''. \.
  /.' _/ |`'=/ " \='`| \_ `.\.
 /` .' `\;-,'\___/',-;/` '. '\.
/.-'       `\(-V-)/`       `-.\.
`            "   "            `
  """)
############################################################################
def PicMinosaur():
  print ("""
  'If I get bigger I will eat you!' 

  oo`'._..---.___..-
 (_,-.        ,..'`
      `'.    ;
         : :`
        _;_;
""")
##############################################################
def PicScorpion():
  print ("""
  'Life is too short for bad coffee'
       ___ __
     _{___{__}\.
    {_}      `\)
   {_}        `            _.-''''--.._
   {.}                    //'.--.  \___`.
    { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)
     `-.{_{_{_{_{_{_{_{_//  -- 8;=- `
        `-:,_.:,_:,_:,.`\\._ ..'=- ,
            // // // //`-.`\`   .-'/
           << << << <<    \ `--'  /----)
            ^  ^  ^  ^     `-.....--'''
""")
#######################################################
def PicAlligator():
  print ("""
    _ _      (0)(0)-._  _.-'^^'^^'^^'^^'^^'--.
   (.(.)----'`        ^^'                /^   ^^-._
   (    `                 \             |    _    ^^-._
    VvvvvvvVv~~`__,/.._>  /:/:/:/:/:/:/:/\  (_..,______^^-.
     `^^^^^^^^`/  /   /  /`^^^^^^^^^>^^>^`>  >        _`)  )
              (((`   (((`          (((`  (((`        `'--'^
""")
#######################################################
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

#############################################################
def PicAmateurWarrior():
  print("""
  'Give me your shield and the loots!'

     ,/|)
     //&')
     '')(
      (( )
      )( (
      (=M=[)###########>
      (( )
      (( )_
      ((__,) 
  """)
######################################################################
def PicCyclops():
  print ("""
  'Never seen someone handsome with one eye?
  Stars… are my eyes!'
            _......._
        .-'.'.'.'.'.'.`-.
      .'.'.'.'.'.'.'.'.'.`.
     /.'.'               '.)
     |.'    _.--...--._     |
     \    `._.-.....-._.'   /
     |     _..- .-. -.._   |
  .-.'    `.   ((@))  .'   '.-.
 ( ^ \      `--.   .-'     / ^ )
  \  /         .   .       \  /
  /          .'     '.  .-    (
 ( _.\    \ (_`-._.-'_)    /._\)
  `-' \   ' .--.          / `-'
      |  / /|_| `-._.'\   |
      |   |       |_| |   /-.._
  _..-\   `.--.______.'  |
       \       .....     |
        `.  .'      `.  /
          \           .'
           `-..___..-`
           """)
  ###########################################################
def PicApeMan():
    print("""
'Its not evolution if you genetically engineer stuff.
Genetic engineering becomes revolution just does not have the same ring to it.'

         ||
        _;|
       /__3
      / /||
     / / // .--.
     \ \// / (OO)
      \//  |( _ )
      // \__/`-'\__
     // \__      _ )
 _.-'/    | ._._.|\ )
(_.-'     |      \ \ )
   .-._   /    o ) / /
  /_ \ \ /   \__/ / /
    \ \_/   / /  E_/
     \     / /
      `-._/-' 
      """)
##########################################################
def PicMutantFox():
  print ("""
'It was not my desire to be killer but your blood calls me' 

                  (\    /)
                  |_)//(_|
                  |4\_/4)(
                 '( (_  -)D
                   ) _)  /\,__
                 _,\_._,/ /   `)
    \.,_,,      ( _   ~ .   ,   )
     \   (\      \(   \/  _)(    )
      \   \\\\     ()  )). _______>-.-`*
       \( ,\\\\ ..-'  ' /    \/    |
         '  \><)_'.)|/\/\/\/\/\|
              \) ,( |\/\/\/\/\/|
              ' ((  \    /\    /
               ((((  \___\/___/)
                ((,) /   ((()   )
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                          _/,/'
                        /,/," 
                        """)
###############################################
def PicNativeCannibal():
  print ("""
'no time for unga bunga, got hunger!'

                   \\\\\|||///
                 .  ======= 
                / \| O   O |
                \ / \`___'/ 
                 #   _| |_
                (#) ( . . )  
                 #\//|   |\\\\ 
                 #\/(  *  )/   
                 #   =====  
                 #   ( U ) 
                 #   || ||
                .#---'| |`----.
                `#----' `-----'   
""")
#################################################
def PicCrazyMonkey():
  print ("""
The difference between monkey and chipmunk
 ... is that monkey is (label) to meddle; to mess with; to interfere
                  ___
                 / _,\.
                 \_\.
      ,,,,    _,_)  #      /)
     (= =)D__/    __/     //
    C/^__)/     _(    ___//
      \_,/  -.   '-._/,--'
 _|_,  /           -//.
 \_ \_/  -,._ _     ) )
   \/    /    )    / /
   \-__,/    (    ( (
              \.__,-)\_
               )\_ / -(
              / -(////
             ////
  """)
#################################################
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
##########################################################
def PicBandit():
    print("""
    'Broke into someones home last night, searching for money.
    He woke up, but started searching with me'

  <=======]}======
    --.   /|
   _\\\"/_.'/
 .'._._,.'
 :/ \[]/
(L  /--',
   /  A \\
  ( /|| |
   \\ V\|
    """)
##########################################################
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
##########################################################
def PicCentaur():
    print("""
    'Shopping is quite a ha.
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
##########################################################
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
##########################################################
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
##########################################################
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
  ##############################################