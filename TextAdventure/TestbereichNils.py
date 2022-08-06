# MonsterHP = 1
# playergold = 20
# merchantInventoryMoney = 20
# all_items = {
# "Apple    " :[[f'HP : {9} '],[f'Value: {9} '],],
# "ItemName2" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# "ItemName3" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# "ItemName4" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# "not apple" :[[f'HP : {9} '],[f'Value: {9} ']],
# "ItemName5" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# "ItemName6" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# "ItemName7" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# }
# # playeritems = {"Apple    " :[[f'HP : {9} '],[f'Value: {9} ']],
# # "ItemName2" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# # "ItemName3" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']],
# # "ItemName4" :[[f'ATK: {9} '],[f'DEF: {9} '],[f'Value: {9} ']]
# # }

# # def Merchantsell():
# Item_number = input ('Pick an item number')
# match Item_number :
#     case '1': 
#         picked_item = {}
#         picked_item = {}
#         print (picked_item)




# def MerchantMenu():
#     print ('Your items : ')
#     for (y),(key,value) in enumerate ((playeritems.items()),start=1):
#         print (y,key,'',value)
#     print ()
#     print(f"Merchant Gold: {merchantInventoryMoney}")
#     print ('Items for sale : ')
#     for (y),(key,value) in enumerate ((all_items.items()),start=1):
#         print (y,key,'',value) 
#     print("\nWhat do you want to buy?")
#     print(f"you have : {playergold} Gold")
# Merchantsell()


# ItemDic = {
#         10011 : ["Sword     ",0 , 2 , 4 , 5],
#         10101 : ["Shield    ",0 , 2 , 4 , 5],
#         10001 : ["Apple     ",0 , 2 , 4 , 5]}


# listMerchant = ()

# print(listMerchant)

# listPlayer = []
# listPlayer = []
# listTemp = []

# print(listPlayer)
# y = int(input("bitte Anzahl auswählen!"))
#
# for i in range(0,y):
#     x = int(input("bitte 1 auswählen"))
#     listTemp.append(x)
# for j in range(0,y):
#     testindex = 10000 + listTemp[j]
#     listMerchant = (ItemDic[testindex][0])
#     print(listMerchant)




# #######################






# # print("Item\t\tATK\tDEF\tHeal\tValue")
# # print(test[1][0],end = "\t ")
# # print(test[1][1],end = "\t ")
# # # print(test[1][2],end = "\t ")
# # # print(test[1][3],end = "\t ")
# # # print(test[1][4])

# # # print(test[2][0],end = "\t ")
# # # print(test[2][1],end = "\t ")
# # # print(test[2][2],end = "\t ")
# # # print(test[2][3],end = "\t ")
# # # print(test[2][4],end = "\t ")

# # # MonsterHP -= test[1][1]# * critchance

# # # input("Which Item to use/equip?")
# # # input = "1" (for Apple)
# # # HP += test[0][3]
# # # inventory -= test[1]

# from math import ceil
# import random
# encounterIndex = 0
# playerLevel = 0
# locationIndex = 0

# luck = 1 #random.randint(1,100)
# lucklist = [1,2,3,4,10,20,40,50,60,70,80,90,100]


# for i in range(1,11):
#     print(f"\n\n##################### Level = {i} ##########################")
#     playerLevel = i
#     for j in range(1,11):
#         locationIndex = j
#         #print(f"--- location = {j}\n")
#         print(f"\n\nLuck / Level: {playerLevel } * Location: {locationIndex}\n")
#         for k in range (1,101):
#             luck = k    
#             encounterIndex = ceil(luck / (playerLevel * locationIndex))
#             print(encounterIndex, end = " ")




def PicWolf():
    print("""oh no, Wolf!
                /^._        Bark
  ,___,--~~~~--' /'~ Bark
  `~--~\ )___,)/'               Bark
      (/\\\_  (/\\\_
       """)
    


def PicRat():
    print("""look, rats!
    
     ~~(  )8:>    <;3(  )~~
     """)

def PicBandit():
    print("""
    
    ToDo: Make a Pic of Bandit
    
    """)


def PicDragon():
    print("""
    'It does not do to leave a live dragon out of your calculations, if you live near him.'      

                     __/>^^^;:,
                    /-.       :,/|/|
                 __/ `c        :,/ \__
                (~             ;/ /  /
                 `-'--._       / / ,<     _
                       /=\     /  _/     | '.
                      / ',\ \\    \_     ,| |"       
                     |=|  E_  |     \. ,/  |
                     \=\   ""       `,,/   |
                      \=\            ||    /
                       \=\____       |\    \\
                      / \/    `     <__)    \\
                      | |                    |
                    ,__\,\                   /
                   ,--____>    /\.         ./
                   '-__________>  \.______/
                   
                   """)



enemyDict = {
        1001 : ["Rats", 1, 0, 2, 1, PicRat],
        1002 : ["Wolf", 3, 1, 10, 2, PicWolf],
        1003 : ["Bandit", 6, 4, 20, 4, PicBandit],
        1004 : ["Dragon", 20, 10, 50, 10, PicDragon]
        } # 0 Name, 1 ATK, 2 DEF, 3 HP, 4 Dropvalue, 5 Pic

enemyDict[1001][5]()

