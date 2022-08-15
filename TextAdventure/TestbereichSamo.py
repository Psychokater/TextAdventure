# import os

# #ENTRYPOINT (change later?!) (Choose where to go -> Merchant or Inventory)
# def WandererMenu(itemsDict, playerName):

#         while True:   
#             userInput = input("\nWhere do you want to go?\n(1) Wanderer shop \t(2) Inventory\t(3) Exit\n")      
#             match userInput:
#                 case "1": itemsDict = WandererShop(itemsDict, playerName)                                                           
#                 case "2": itemsDict = InventoryMenu(itemsDict, playerName)                                                          
#                 case "3": break

#                 case _: print("\nCouldn't understand you?!")


# # Merchant                                (Print Merchant+PlayerInventory - Choose if Buy or Sell)
# def WandererShop(itemsDict, playerName):
#     PicMerchant()
#     playerItemIDs = []
#     merchantItemIDs = []
#     while True:
#         itemsDict, merchantItemIDs = GetInventoryWanderer(itemsDict, merchantItemIDs)
#         itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName)

#         userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(3) Leave Wanderer\n")      
#         match userInput:
#             case "1": itemsDict, playerItemIDs, merchantItemIDs = WandererItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName)
#             case "2": itemsDict, playerItemIDs, merchantItemIDs = wandererItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName)
#             case "3": break
#             case _: print("\nCouldn't understand you?!")
    
#     return itemsDict

# # PlayerInventory                      (Choose "Equip", "Remove"---- function for later)
# def InventoryMenu(itemsDict, playerName):
#     os.system('cls')
#     playerItemIDs = []
#     while True:
#         itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict , playerItemIDs, playerName)
#         userInput = input("\n(1) Equip\t\t(2) Remove from Inventory\t(3) Leave Inventory\n")
#         if userInput == "1":
#             pass
#         elif userInput == "2":
#             pass
#         elif userInput == "3": break
#         else: print("\nCouldn't understand you?!")
    
#     return itemsDict

# # print PlayerInventory + getting ID's
# def GetInventoryPlayer(itemsDict, playerItemIDs, playerName):
#     print(f'{playerName} Items: ')
#     print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tValue\tQuantity\n'\
#     '------------------------------------------------------------------------')
#     z = 1
#     for i in range (0,len(itemsDict)):
#         k = i + 1001
#         playerItemIDs = []
#         if itemsDict[k][9] > 0:
#             itemsDict[k][1] = z
#             z += 1            
#             playerItemIDs.append(i)
#             print('\u2009 ',itemsDict[k][1],end='\t:\t')
#             for j in range (2,len(itemsDict[k])-3):
#                 print(itemsDict[k][j],end='\t')
#             print(itemsDict[k][9])
#     print('------------------------------------------------------------------------\n')
#     return itemsDict, playerItemIDs
    
# # print MerchantInventory + getting iD's
# def GetInventoryWanderer(itemsDict, merchantItemIDs):
#     print('Merchant Items:')
#     print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tPrice\tQuantity\n'\
#     '------------------------------------------------------------------------')
#     z = 1
#     for i in range (0,len(itemsDict)):
#         i += 1001
#         if itemsDict[i][8] > 0:
#             itemsDict[i][0] = z
#             z += 1            
#             merchantItemIDs.append(i)
#             print ('\u2009 ',itemsDict[i][0],end='\t:\t')
#             for j in range (1,len(itemsDict[i])):
#                 if j == 1 or j == 7 or j == 9:
#                     continue
#                 if j == 6:                                       
#                     print(itemsDict[i][j]* 1.5 + 2,end='\t')                
#                     continue
#                 print (itemsDict[i][j],end='\t')
#             print()
#     print('------------------------------------------------------------------------\n')
#     return itemsDict, merchantItemIDs


# def WandererItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName):
#     os.system('cls')
#     itemsDict, merchantItemIDs = GetInventoryWanderer(itemsDict, merchantItemIDs)
#     itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName)
#     userInputItemNumber = int (input ('Pick an Item number to buy it: \n'))
#     for i in range (0,len(itemsDict)):
#         i +=1001       
#         if userInputItemNumber == itemsDict[i][0]:
#             itemsDict[i][8] -= 1
#             itemsDict[i][9] += 1
#             if itemsDict[i][8] == 0:
#                 itemsDict[i][0] = 0

#     return itemsDict, playerItemIDs, merchantItemIDs


# def wandererItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName):
#     os.system('cls')
#     itemsDict, merchantItemIDs = GetInventoryWanderer(itemsDict, merchantItemIDs)
#     itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName)    
#     userInputItemNumber = int (input ('Pick an Item number to sell it: \n'))
#     for i in range (0,len(itemsDict)):
#         i +=1001
#         if userInputItemNumber == itemsDict[i][1]:
#             itemsDict[i][8] += 1
#             itemsDict[i][9] -= 1
#             if itemsDict[i][9] == 0:
#                 itemsDict[i][1] = 0
                               
#     return itemsDict, playerItemIDs, merchantItemIDs


# # ######################################## Friends ################################################

# def PicWanderer(): 
#     print("""
#     A mystic old man wanders through this valley, maybe he has some free candys?
     
#                      .x    
#                      .    x    
#                        x`  
#             /\       .x   .
#             / />        o        
#            /  \}      .o x             ____ _____   
#           /`---\   .-`---'-.        ,-'  ,-'_ ,-'|   
#           |  \__D  \`--.--'/       |""-'" ,-'|   |   
#          /     /    \     /        ||"\"""|   |,-'   
#         /_____/\   _//^-^\\\\_._      |____|,-'   
#     """)



# def PicMerchant():
#     print("""
#     'buy two Potions, pay for three and get one for free!'
    
#             /'''''''''''''''''''\\
#            /_____/Merchant\\______\\     
#             |       ____ _,       |
#             |      |_|_|_||       |
#         ;,_<|_--_----__----___--|\_
#               \\_/        \\_/     
#     """)    

