import os

#ENTRYPOINT (change later?!) (Choose where to go -> Merchant or Inventory)
def ShopMenu(itemsDict, playerName):

        while True:   
            userInput = input("\nWhere do you want to go?\n(1) Merchant\t(2)\t Wizard \t(3) Inventory\t(4) Exit\n")      
            match userInput:
                case "1": itemsDict = MerchantShop(itemsDict, playerName)                                                           
                case "2": itemsDict = InventoryMenu(itemsDict, playerName)                                                          
                case "3": pass
                case "4": break

                case _: print("\nCouldn't understand you?!")


# Merchant                                (Print Merchant+PlayerInventory - Choose if Buy or Sell)
def MerchantShop(itemsDict, playerName):
    PicMerchant()
    playerItemIDs = []
    merchantItemIDs = []
    while True:
        itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(3) Leave Merchant\n")      
        match userInput:
            case "1": itemsDict, playerItemIDs, merchantItemIDs = MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName)
            case "2": itemsDict, playerItemIDs, merchantItemIDs = MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName)
            case "3": break
            case _: print("\nCouldn't understand you?!")
    
    return itemsDict

#Wizard
def  WizardShop(itemsDict, playerName):
    PicWizard()
    while True:
        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(3) Leave Wizard\n")      
        match userInput:
            case "1": pass #itemsDict, playerItemIDs, merchantItemIDs = MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName)
            case "2": pass #itemsDict, playerItemIDs, merchantItemIDs = MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName)
            case "3": break
            case _: print("\nCouldn't understand you?!")

    return itemsDict  

# PlayerInventory                      (Choose "Equip", "Remove"---- function for later)
def InventoryMenu(itemsDict, playerName):
    os.system('cls')
    playerItemIDs = []
    while True:
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict , playerItemIDs, playerName)
        userInput = input("\n(1) Equip\t\t(2) Remove from Inventory\t(3) Leave Inventory\n")
        if userInput == "1":
            pass
        elif userInput == "2":
            pass
        elif userInput == "3": break
        else: print("\nCouldn't understand you?!")
    
    return itemsDict

# print PlayerInventory + getting ID's
def GetInventoryPlayer(itemsDict, playerItemIDs, playerName):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    print(f'{playerName} Items: ')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tValue\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1
    for i in range (0,len(itemsDict)):                                          # for every Item in itemsDictionary
        i += 1001                                                               #       i = Item ID
        playerItemIDs = []        
        if itemsDict[i][8] > 0:                                                 #   Quantity Player > 0 for that ItemID?
            itemsDict[i][1] = z                                                 #   Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            playerItemIDs.append(i)                                             #   append Item ID to List of ItemID's
            print('\u2009 ',itemsDict[i][1],end='\t:\t')                        #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 7, 9, 10]                              #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                                                    #
                print (itemsDict[i][j],end='\t')                                #           print Value in this line 
            print()                                                             #   new Line of Inventory        
    print('------------------------------------------------------------------------\n')
    return itemsDict, playerItemIDs
    
# print MerchantInventory + getting iD's
def GetInventoryMerchant(itemsDict, merchantItemIDs):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    print('Merchant Items:')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tPrice\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1   
    for i in range (0,len(itemsDict)):                                          # for every Item in itemsDictionary      
        i += 1001                                                               #       i = Item ID
        _tempListIndexValue = [1, 2, 3, 10, 11, 12]                             #       List of ID to Sell at Merchant
        if itemsDict[i][10] in _tempListIndexValue:                             #       If Item ID of selected Item is activated
            itemsDict[i][0] = z                                                 #       Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            merchantItemIDs.append(i)                                           #   append Item ID to List of ItemID's
            print ('\u2009 ',itemsDict[i][0],end='\t:\t')                       #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 8, 9, 10]                              #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                                                    #
                if j == 6:                                                      #           if Index == "Value of Item":
                    print(itemsDict[i][j]* 1.5 + 2,end='\t')                    #               Print "Value" of Item * 1.5 + 2
                    continue                                                    #
                if j == 7:                                                      #           if Index == "MaxQuantity" of Item:
                    print(((itemsDict[i][j]/2) - itemsDict[i][8]))              #           print "MaxQuantity" / 2 (for "Merchant Quantity")
                print (itemsDict[i][j],end='\t')                                #           print Value in this line
            print()                                                             #   new Line of Inventory
    print('------------------------------------------------------------------------\n')
    return itemsDict, merchantItemIDs


def MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName)
    userInputItemNumber = int (input ('Pick an Item number to buy it: \n'))
    for i in range (0,len(itemsDict)):
        i +=1001       
        if userInputItemNumber == itemsDict[i][0]:
            itemsDict[i][8] -= 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][0] = 0

    return itemsDict, playerItemIDs, merchantItemIDs


def MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName)    
    userInputItemNumber = int (input ('Pick an Item number to sell it: \n'))
    for i in range (0,len(itemsDict)):
        i +=1001
        if userInputItemNumber == itemsDict[i][1]:
            itemsDict[i][8] += 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, merchantItemIDs


# ######################################## Friends ################################################

def PicWizard(): 
    print("""
    A mystic old man hides in this dark lane, maybe he has some free candys?
     
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
            |       ____ _,       |
            |      |_|_|_||       |
        ;,_<|_--_----__----___--|\_
              \\_/        \\_/     
    """)    

