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


ItemDic = {
        10011 : ["Sword     ",0 , 2 , 4 , 5],
        10101 : ["Shield    ",0 , 2 , 4 , 5],
        10001 : ["Apple     ",0 , 2 , 4 , 5]}


listMerchant = ()

print(listMerchant)

listPlayer = []
listPlayer = []
listTemp = []

print(listPlayer)
y = int(input("bitte Anzahl auswählen!"))

for i in range(0,y):
    x = int(input("bitte 1 auswählen"))
    listTemp.append(x)
for j in range(0,y):
    testindex = 10000 + listTemp[j]
    listMerchant = (ItemDic[testindex][0])
    print(listMerchant)




# #######################






# # print("Item\t\tATK\tDEF\tHeal\tValue")
# # print(test[1][0],end = "\t ")
# # print(test[1][1],end = "\t ")
# # print(test[1][2],end = "\t ")
# # print(test[1][3],end = "\t ")
# # print(test[1][4])

# # print(test[2][0],end = "\t ")
# # print(test[2][1],end = "\t ")
# # print(test[2][2],end = "\t ")
# # print(test[2][3],end = "\t ")
# # print(test[2][4],end = "\t ")

# # MonsterHP -= test[1][1]# * critchance

# # input("Which Item to use/equip?")
# # input = "1" (for Apple)
# # HP += test[0][3]
# # inventory -= test[1]