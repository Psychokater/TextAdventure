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



# all_items = {
# 1001:["Apple    ",(0),(0),(7),(6),(5)],
# 1010:["ItemName1",(9),(8),(0),(6),(5)],
# 1011:["ItemName2",(9),(8),(0),(6),(5)],
# 1100:["ItemName3",(9),(8),(0),(6),(5)],
# 1101:["ItemName4",(9),(8),(0),(6),(5)],
# 1110:["ItemName5",(9),(8),(0),(6),(5)],
# 1111:["ItemName6",(9),(8),(0),(6),(5)],
# 2000:["ItemName7",(9),(8),(0),(6),(5)],
# 2001:["ItemName8",(9),(8),(0),(6),(5)]}
# # ItemNumber   1 Item    2 ATK,  3 DEF, 4 HP, 5 VL, 6 PR 

# merchantItems = []
# playerItems = []

# #buy
# ####################################################################### print Shop
# merchantItems += 1001,1010,1011    #Items nur Testweise zugefügt
# playerItems += 2001, 2000          #
# for i in range(0,len(merchantItems)):
#     print(all_items[merchantItems[i]])
# print("")
# for j in range(0,len(playerItems)):
#     print(all_items[playerItems[j]])
# ####################################################################### buy
# buyItem = int(input("welches Item? "))
# playerItems.append(buyItem)
# merchantItems.remove(buyItem)
# all_items[buyItem][5] = 1           # 1 kann auch über eine variable ermittelt werden!!!
# ####################################################################### print Shop
# for i in range(0,len(merchantItems)):
#     print(all_items[merchantItems[i]])
# print("")
# for j in range(0,len(playerItems)):
#     print(all_items[playerItems[j]])

itemsDict = {
1001:[1,"Apple    ",(0),(0),(7),(6),(5),(3)],
1010:[2,"ItemName1",(9),(8),(0),(6),(5),(1)],
1011:[3,"ItemName2",(9),(8),(0),(6),(5),(1)],
1100:[4,"ItemName3",(9),(8),(0),(6),(5),(1)],
1101:[5,"ItemName4",(9),(8),(0),(6),(5),(1)],
1110:[6,"ItemName5",(9),(8),(0),(6),(5),(1)],
1111:[7,"ItemName6",(9),(8),(0),(6),(5),(1)],
2000:[8,"ItemName7",(9),(8),(0),(6),(5),(1)],
2001:[9,"ItemName8",(9),(8),(0),(6),(5),(1)]}

############################## 6 Merchant, 7 Player

playerInventory = [1001, 1100, 1101]
merchantInventory = [1001, 1010, 1111]

print("Player:")
print("ID\tItem\t\tATK\tDEF\tHP\tVL\tQT")
for i in range(0,len(playerInventory)):
    for j in range(0,8):
        if j == 6:            
            continue
        print(itemsDict[playerInventory[i]][j], end='\t')
    print("")
print("\nMerchant")
print("ID\tItem\t\tATK\tDEF\tHP\tVL\tQT")
for k in range(0,len(merchantInventory)):
    for l in range(0,8):
        if l == 7:
            continue
        print(itemsDict[merchantInventory[k]][l], end='\t')
    print("")

