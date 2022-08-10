import os

#ENTRYPOINT (change later?!) (Choose where to go -> Merchant or Inventory)
def ShopMenu():
        itemsDict = {
        #                             atk def  hp val  pr  qnt  qnt  
        #                                                   M    P
        1001:[(0),(0),"Apple     ==>",(0),(0),(4),(1),(99),(1),(1)],
        1002:[(0),(0),"ItemName1 ==>",(9),(8),(1),(6),(99),(98),(0)],
        1003:[(0),(0),"ItemName2 ==>",(9),(8),(1),(6),(99),(99),(0)],
        1004:[(0),(0),"ItemName3 ==>",(9),(8),(1),(6),(99),(98),(0)],
        1005:[(0),(0),"ItemName4 ==>",(9),(8),(0),(6),(99),(99),(1)],
        1006:[(0),(0),"ItemName5 ==>",(5),(8),(1),(6),(99),(99),(0)],
        1007:[(0),(0),"ItemName6 ==>",(9),(8),(0),(6),(99),(99),(1)],
        1008:[(0),(0),"ItemName7 ==>",(9),(8),(0),(6),(99),(99),(0)],
        1009:[(0),(0),"ItemName8 ==>",(9),(8),(1),(6),(99),(98),(0)],
        1010:[(0),(0),"ItemName9 ==>",(9),(8),(1),(6),(99),(1),(0)]}
        
        while True:   
            userInput = input("\nWhere do you want to go?\n(1) Merchant\t(2) Inventory\t(3) Exit\n")      
            match userInput:
                case "1": itemsDict = MerchantShop(itemsDict)                                                           
                case "2": itemsDict = InventoryMenu(itemsDict)                                                          
                case "3": break

                case _: print("\nCouldn't understand you?!")


# Merchant                                (Print Merchant+PlayerInventory - Choose if Buy or Sell)
def MerchantShop(itemsDict):
    os.system('cls')
    playerItemIDs = []
    merchantItemIDs = []
    while True:
        itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(3) Leave Merchant\n")      
        match userInput:
            case "1": itemsDict, playerItemIDs, merchantItemIDs = MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs)
            case "2": itemsDict, playerItemIDs, merchantItemIDs = MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs)
            case "3": break
            case _: print("\nCouldn't understand you?!")
    
    return itemsDict

# PlayerInventory                      (Choose "Equip", "Remove"---- function for later)
def InventoryMenu(itemsDict):
    os.system('cls')
    playerItemIDs = []
    while True:
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict , playerItemIDs)
        userInput = input("\n(1) Equip\t\t(2) Remove from Inventory\t(3) Leave Inventory\n")
        if userInput == "1":
            pass
        elif userInput == "2":
            pass
        elif userInput == "3": break
        else: print("\nCouldn't understand you?!")
    
    return itemsDict

# print PlayerInventory + getting ID's
def GetInventoryPlayer(itemsDict, playerItemIDs):
    print ('Your Items : ')
    print (' Item.NR      Item    Attack  Defence  Heal   Quantity ')
    z = 1
    for i in range (0,len(itemsDict)):
        k = i + 1001
        playerItemIDs = []
        if itemsDict[k][9] > 0:
            itemsDict[k][1] = z
            z += 1            
            playerItemIDs.append(i)
            print ('\u2009 ',itemsDict[k][1],end='  :  ')
            for j in range (2,len(itemsDict[k])-4):
                print (itemsDict[k][j],end='\t')
            print (itemsDict[k][9])

    return itemsDict, playerItemIDs

# print MerchantInventory + getting iD's
def GetInventoryMerchant(itemsDict, merchantItemIDs):
    print ('Merchant Items : ')
    print ('  Item.NR      Item    Attack  Defence   Heal   Value   Price  Quantity ')
    z = 1
    for i in range (0,len(itemsDict)):
        i += 1001
        if itemsDict[i][8] > 0:
            itemsDict[i][0] = z
            z += 1            
            merchantItemIDs.append(i)
            print ('\u2009 ',itemsDict[i][0],end='  :  ')
            for j in range (1,len(itemsDict[i])-1):
                if j == 1:
                    continue
                print (itemsDict[i][j],end='\t')
            print ()

    return itemsDict, merchantItemIDs


def MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs):
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs)
    userInputItemNumber = int (input ('Pick an Item number to buy it : \n'))
    for i in range (0,len(itemsDict)):
        i +=1001       
        if userInputItemNumber == itemsDict[i][0]:
            itemsDict[i][8] -= 1
            itemsDict[i][9] += 1
            if itemsDict[i][8] == 0:
                itemsDict[i][0] = 0

    return itemsDict, playerItemIDs, merchantItemIDs


def MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs):
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs)    
    userInputItemNumber = int (input ('Pick an Item number to sell it : \n'))
    for i in range (0,len(itemsDict)):
        i +=1001
        if userInputItemNumber == itemsDict[i][1]:
            itemsDict[i][8] += 1
            itemsDict[i][9] -= 1
            if itemsDict[i][9] == 0:
                itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, merchantItemIDs




ShopMenu()
