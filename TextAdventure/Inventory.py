from math import ceil
import os

#ENTRYPOINT (Choose where to go -> Merchant, Wizard or Inventory)
def ShopMenu(itemsDict, playerName, playerInventoryMoney):
    while True:   
        userInput = input("\nWhere do you want to go?\n(1) Merchant\t(2) Wizard \t(3) Inventory\t(4) Exit\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerInventoryMoney = MerchantShop(itemsDict, playerName, playerInventoryMoney)                                                           
            case "2": itemsDict, playerInventoryMoney = WizardShop(itemsDict, playerName, playerInventoryMoney)
            case "3": itemsDict = InventoryMenu(itemsDict, playerName, playerInventoryMoney)                                                          
            case "4": break

            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney


####################################### MERCHANT SHOP ##################################

# Merchant (Print Merchant and PlayerInventory - Choose if Buy or Sell)
def MerchantShop(itemsDict, playerName, playerInventoryMoney):
    PicMerchant()
    playerItemIDs = []
    merchantItemIDs = []
    while True:
        itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(3) Leave Merchant\n")
        os.system('cls')      
        match userInput:
            case "1": itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney = MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney)
            case "2": itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney = MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney)
            case "3": break
            case _: print("\nCouldn't understand you?!")
    
    return itemsDict, playerInventoryMoney


# print PlayerInventory + getting ID's
def GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    print(f'{playerName}\t\t\tGold:\t{playerInventoryMoney}')
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
        _tempListIndexValue = [1, 2, 3]                                         #       List of ID to Sell at Merchant
        if itemsDict[i][10] in _tempListIndexValue and (                        #       If Item ID of selected Item is activated AND ->
            (itemsDict[i][7] - itemsDict[i][8]) > 0):                           #       Item Quantity Merchant > 0
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
                    print(itemsDict[i][j] - itemsDict[i][8])                    #           print "MaxQuantity" (for "Merchant Quantity")
                    continue                                                    #           
                print (itemsDict[i][j],end='\t')                                #           print Value in this line
                                                                                #   new Line of Inventory
    print('------------------------------------------------------------------------\n')
    return itemsDict, merchantItemIDs

# +ItemPlayer -MoneyPlayer
def MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)
    userInputItemNumber = int (input ('Pick an Item number to buy it: \n'))
    for i in range (0,len(itemsDict)):
        i +=1001       
        if userInputItemNumber == itemsDict[i][0] and playerInventoryMoney >= itemsDict[i][6] * 1.5 + 2:
            playerInventoryMoney -= itemsDict[i][6] * 1.5 + 2
            itemsDict[i][8] += 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][0] = 0

    return itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney

# -ItemPlayer +MoneyPlayer
def MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)    
    userInputItemNumber = int (input ('Pick an Item number to sell it: \n'))
    for i in range (0,len(itemsDict)):
        i +=1001
        if userInputItemNumber == itemsDict[i][1]:
            playerInventoryMoney += itemsDict[i][6]
            itemsDict[i][8] -= 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney

####################################### WIZARD SHOP ##################################

#Wizard (Print Wizard and PlayerInventory - Choose if Buy or Sell)
def WizardShop(itemsDict, playerName, playerInventoryMoney):
    os.system('cls')
    PicWizard()
    playerItemIDs = []
    wizardItemIDs = []
    while True:
        itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(3) Leave Wizard\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney = WizardItemBuy(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney)
            case "2": itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney = WizardItemSell(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney)
            case "3": break
            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney 

# print MerchantInventory + getting iD's
def GetInventoryWizard(itemsDict, wizardItemIDs):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    print('Merchant Items:')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tPrice\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1   
    for i in range (0,len(itemsDict)):                                          # for every Item in itemsDictionary      
        i += 1001                                                               #       i = Item ID
        _tempListIndexValue = [4, 5, 6]                                         #       List of ID to Sell at Merchant
        if itemsDict[i][10] in _tempListIndexValue and (                        #       If Item ID of selected Item is activated AND ->
            (itemsDict[i][7] - itemsDict[i][8]) > 0):                           #       Item Quantity Merchant > 0
            itemsDict[i][0] = z                                                 #       Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            wizardItemIDs.append(i)                                             #   append Item ID to List of ItemID's
            print ('\u2009 ',itemsDict[i][0],end='\t:\t')                       #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 8, 9, 10]                              #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                                                    #
                if j == 6:                                                      #           if Index == "Value of Item":
                    print(itemsDict[i][j]* 1.5 + 2,end='\t')                    #               Print "Value" of Item * 1.5 + 2
                    continue                                                    #
                if j == 7:                                                      #           if Index == "MaxQuantity" of Item:
                    print(itemsDict[i][j] - itemsDict[i][8])                    #           print "MaxQuantity" (for "Merchant Quantity")
                    continue                                                    #           
                print (itemsDict[i][j],end='\t')                                #           print Value in this line
                                                                                #   new Line of Inventory
    print('------------------------------------------------------------------------\n')
    return itemsDict, wizardItemIDs

# +ItemPlayer -MoneyPlayer
def WizardItemBuy(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    os.system('cls')
    itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)
    userInputItemNumber = int (input ('Pick an Item number to buy it: \n'))
    for i in range (0,len(itemsDict)):
        i +=1001       
        if userInputItemNumber == itemsDict[i][0] and playerInventoryMoney >= itemsDict[i][6] * 1.5 + 2:
            playerInventoryMoney -= itemsDict[i][6] * 1.5 + 2
            itemsDict[i][8] += 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][0] = 0

    return itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney

# -ItemPlayer +MoneyPlayer
def WizardItemSell(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON  
    os.system('cls')
    itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)    
    userInputItemNumber = int (input ('Pick an Item number to sell it: \n'))
    for i in range (0,len(itemsDict)):
        i +=1001
        if userInputItemNumber == itemsDict[i][1]:
            playerInventoryMoney += itemsDict[i][6]
            itemsDict[i][8] -= 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney

####################################### INVENTORY ##################################

# PlayerInventory                      (Add "Equip" function for later)
def InventoryMenu(itemsDict, playerName, playerInventoryMoney):
    os.system('cls')
    playerItemIDs = []
    while True:
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict , playerItemIDs, playerName, playerInventoryMoney)
        userInput = input("\n(1) Equip\t\t(2) Remove from Inventory\t(3) Leave Inventory\n")
        if userInput == "1":
            pass
        elif userInput == "2":
            userInputItemNumber = int (input ('Select Item to Remove: \n'))
            for i in range (0,len(itemsDict)):
                i +=1001
                if userInputItemNumber == itemsDict[i][1]:
                    itemsDict[i][8] -= 1            
                    if itemsDict[i][8] == 0:
                        itemsDict[i][1] = 0
            print("\nItem has brought back to his owner!\n")

        elif userInput == "3": break
        else: print("\nCouldn't understand you?!")
    
    return itemsDict


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

