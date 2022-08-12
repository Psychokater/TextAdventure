# from time import sleep
from math import ceil
import os

#ENTRYPOINT (Choose where to go -> Merchant, Wizard or Inventory)
def ShopMenu(itemsDict, playerName, playerInventoryMoney, playerStats):
    while True:   
        userInput = input("\nWhere do you want to go?\n(1) Merchant\t(2) Wizard \t(3) Inventory\t(4) Exit\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerInventoryMoney = MerchantShop(itemsDict, playerName, playerInventoryMoney)                                                           
            case "2": itemsDict, playerInventoryMoney = WizardShop(itemsDict, playerName, playerInventoryMoney)
            case "3": itemsDict, playerStats = InventoryMenu(itemsDict, playerName, playerInventoryMoney, playerStats)                                                          
            case "4": break

            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney, playerStats


####################################### MERCHANT SHOP ##################################

# Merchant (Print Merchant and PlayerInventory - Choose if Buy or Sell)
def MerchantShop(itemsDict, playerName, playerInventoryMoney):
    PicMerchant()

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
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    print(f'{playerName}\t\t\tGold:\t{playerInventoryMoney}\n')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tValue\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1
    
    itemKeyList = [key for key in itemsDict]                                    # for every Item in itemsDictionary  
    playerItemIDs = [] 
         
    for i in itemKeyList:   
        itemsDict[i][1] = 0                                                     #       i = Item ID
        if itemsDict[i][8] > 0:                                                 #   Quantity Player > 0 for that ItemID?
            itemsDict[i][1] = z                                                 #   Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            playerItemIDs.append(i)                                             #   append Item ID to List of ItemID's
            print('\u2009 ',itemsDict[i][1],end='\t:\t')                        #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 7, 9, 10, 11]                          #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue
                                                                                #
                print (itemsDict[i][j],end='\t')                                #           print Value in this line 
            print()                                                             #   new Line of Inventory        
    print('------------------------------------------------------------------------\n')
    return itemsDict, playerItemIDs
    
# print MerchantInventory + getting iD's
def GetInventoryMerchant(itemsDict, merchantItemIDs):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    print('Merchant:\n')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tPrice\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1   
    
    itemKeyList = [key for key in itemsDict]                                    # for every Item in itemsDictionary  
    for i in itemKeyList:  
        itemsDict[i][0] = 0                                                     #       i = Item ID
        _tempListIndexValue = [1, 2, 3]                                         #       List of ID to Sell at Merchant
        if itemsDict[i][10] in _tempListIndexValue and (                        #       If Item ID of selected Item is activated AND ->
            (itemsDict[i][7] - itemsDict[i][8]) > 0):                           #       Item Quantity Merchant > 0
            itemsDict[i][0] = z                                                 #       Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            merchantItemIDs.append(i)                                           #   append Item ID to List of ItemID's
            print ('\u2009 ',itemsDict[i][0],end='\t:\t')                       #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 8, 9, 10, 11]                          #           except for these Indexes!
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
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)
    userInputItemNumber = int (input ('Pick an Item number to buy it: \n'))       

    itemKeyList = [key for key in itemsDict]
    for i in itemKeyList:    
        if userInputItemNumber == itemsDict[i][0]:
            if playerInventoryMoney < itemsDict[i][6] * 1.5 + 2: 
                print("\nNot enough money, fool!\n")
                # sleep(1)
                break     
            else: 
                playerInventoryMoney -= itemsDict[i][6] * 1.5 + 2
                itemsDict[i][8] += 1            
                if itemsDict[i][8] == 0:
                    itemsDict[i][0] = 0

    return itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney

# -ItemPlayer +MoneyPlayer
def MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)    
    userInputItemNumber = int (input ('Pick an Item number to sell it: \n'))

    itemKeyList = [key for key in itemsDict]
    for i in itemKeyList:  
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
    wizardItemIDs = []
    playerItemIDs = []
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
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    print('Wizard:\n')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tPrice\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1                                         

    itemKeyList = [key for key in itemsDict]                                    # for every Item in itemsDictionary  
    for i in itemKeyList:  
        itemsDict[i][0] = 0                                                     #       i = Item ID
        _tempListIndexValue = [4, 5, 6]                                         #       List of ID to Sell at Merchant
        if itemsDict[i][10] in _tempListIndexValue and (                        #       If Item ID of selected Item is activated AND ->
            (itemsDict[i][7] - itemsDict[i][8]) > 0):                           #       Item Quantity Merchant > 0
            itemsDict[i][0] = z                                                 #       Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            wizardItemIDs.append(i)                                             #   append Item ID to List of ItemID's
            print ('\u2009 ',itemsDict[i][0],end='\t:\t')                       #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 8, 9, 10, 11]                          #           except for these Indexes!
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
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)
    userInputItemNumber = int (input ('Pick an Item number to buy it: \n'))

    itemKeyList = [key for key in itemsDict]
    for i in itemKeyList:  
        if userInputItemNumber == itemsDict[i][0]:
            if playerInventoryMoney < itemsDict[i][6] * 1.5 + 2: 
                print("\nNot enough money, fool!\n")
                # sleep(1)
                break
            else:
                playerInventoryMoney -= itemsDict[i][6] * 1.5 + 2
                itemsDict[i][8] += 1            
                if itemsDict[i][8] == 0:
                    itemsDict[i][0] = 0
       

    return itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney

# -ItemPlayer +MoneyPlayer
def WizardItemSell(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
    itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)    
    userInputItemNumber = int (input ('Pick an Item number to sell it: \n'))
 
    itemKeyList = [key for key in itemsDict]
    for i in itemKeyList:  
        if userInputItemNumber == itemsDict[i][1]:
            playerInventoryMoney += itemsDict[i][6]
            itemsDict[i][8] -= 1            
            if itemsDict[i][8] == 0:
                itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney

####################################### INVENTORY ##################################
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq

# PlayerInventory                 
def InventoryMenu(itemsDict, playerName, playerInventoryMoney, playerStats):
    os.system('cls')
    playerItemIDs = []

    while True:
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict , playerItemIDs, playerName, playerInventoryMoney)
        userInput = input("\n(1) Equipment\t(2) Items\t(3) Return\n")
################ Player Equipment ##########################
        if userInput == "1":
            itemsDict, playerItemIDs = PlayerEquipment(itemsDict, playerItemIDs, playerName, playerInventoryMoney)
################ Items ####################################
        elif userInput == "2":
            itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney)
            userInput = input("\n(1) Use\t(2) Remove from Inventory\t(3) Return\n")
################ Items #### Use Item #################################
            if userInput == "1":
                userInputItemNumber = int (input ('Select item to use: \n'))
             
                itemKeyList = [key for key in itemsDict]
                for i in itemKeyList: 
                    if userInputItemNumber == itemsDict[i][1]:
                        if itemsDict[i][11] > 0:
                            print(f"You can't use this {itemsDict[i][2]}")
                            break
                         #################################### Healitems #########################
                         # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
                        if itemsDict[i][5] > 0:
                            if playerStats[2] >= playerStats[1]:
                                print(f"You already have full HP, do you really want to use {itemsDict[i][2]}?")
                                userItemInput = input("(1) Yes!\t(2) No!")
                                if userItemInput == "1":
                                    itemsDict[i][8] -= 1            
                                    if itemsDict[i][8] == 0:
                                        itemsDict[i][1] = 0
                                    print(f"You used {itemsDict[i][2]}")
                                    break   
                                elif userItemInput == "2":
                                    break
                                else: print("\nCouldn't understand you?!")
                            if playerStats[2] + itemsDict[i][5] <= playerStats[1]:       
                                playerStats[2] += itemsDict[i][5]
                                print(f"You got healed for {itemsDict[i][5]} Points. HP: {playerStats[2]}/{playerStats[1]}")                                
                            else:
                                print(f"You got fully healed with {playerStats[1] - playerStats[2]} Points. HP: {playerStats[2]}/{playerStats[1]} ") 
                                playerStats[2] = playerStats[1]                                
                        
                            itemsDict[i][8] -= 1            
                            if itemsDict[i][8] == 0:
                                itemsDict[i][1] = 0    
                        
                                                             
############### Items #### Remove Item ##############################
            elif userInput == "2":            
                userInputItemNumber = int (input ('Select item to remove: \n'))
                
                itemKeyList = [key for key in itemsDict]
                for i in itemKeyList:  
                    if userInputItemNumber == itemsDict[i][1]:
                        itemsDict[i][8] -= 1 
                        print(f"\n{itemsDict[i][2]} was brought back to his owner!\n")           
                        if itemsDict[i][8] == 0:
                            itemsDict[i][1] = 0
                        
############### Items #### Break ####################################
            elif userInput == "3":
                break
            else: print("\nCouldn't understand you?!")
############### Break #####################
        elif userInput == "3": break
        else: print("\nCouldn't understand you?!")
    
    return itemsDict, playerStats

    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
def PlayerEquipment(itemsDict , playerItemIDs, playerName, playerInventoryMoney):
        while True:
            print(f'{playerName}\t\t\tGold:\t{playerInventoryMoney}\n')
            print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tValue\tQuantity\n'\
            '------------------------------------------------------------------------')
            z = 1
       
            playerItemIDs = []        
            itemKeyList = [key for key in itemsDict]                                    # for every Item in itemsDictionary  
            for i in itemKeyList:
                itemsDict[i][1] = 0                                                       #       i = Item ID
                if itemsDict[i][8] > 0 and itemsDict[i][11] > 0:                        #   Quantity Player > 0 for that ItemID AND Equipable?
                    itemsDict[i][1] = z                                                 #   Enumerate Itemline
                    z += 1                                                              #   Enumerate + 1
                    playerItemIDs.append(i)                                             #   append Item ID to List of ItemID's
                    print('\u2009 ',itemsDict[i][1],end='\t:\t')                        #   print Enumerate
                    for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                        if j == 11:
                            if itemsDict[i][j] > 10:
                                print ("\u25cf",end='') #"Equipped"
                        _tempListIndexJ = [0, 1, 7, 9, 10, 11]                          #           except for these Indexes!
                        if j in _tempListIndexJ:                                        #
                            continue                   
                                                                                        #
                        print (itemsDict[i][j],end='\t')                                #           print Value in this line 
                    print()                                                             #   new Line of Inventory        
            print('------------------------------------------------------------------------\n')    
            userInput = input("\n(1) Equip item\t(2) Unequip item\t(3) Remove item\t(4) Return\n")
################################## 1 equip Item #############################   
            if userInput == "1":
                userInputItemNumber = int (input ('Select item to equip: \n'))
                
                itemKeyList = [key for key in itemsDict]
                for j in itemKeyList: 
                    if userInputItemNumber == itemsDict[j][1]:
                        if itemsDict[j][11] == 0:
                            print(f"You can't equip {itemsDict[j][2]}")
                            # sleep(1)
                            break 
                        elif itemsDict[j][11] >= 10:
                            print(f"{itemsDict[j][2]} item is already equipped!")
                            # sleep(1)
                            break 
                        else:
                            itemsDict[j][11] += 10
                            for k in itemKeyList:
                                if itemsDict[j][11] == itemsDict[k][11] and j != k:
                                    itemsDict[k][11] -= 10                        
                                    break            
                
                            print(f"You equipped {itemsDict[j][2]}")
                            break                        
################################## 2 Equip Item #############################               
            elif userInput == "2":  
                userInputItemNumber = int (input ('Select item to unequip: \n'))
                
                itemKeyList = [key for key in itemsDict]
                for o in itemKeyList: 
                    if userInputItemNumber == itemsDict[o][1]:
                        if itemsDict[o][11] < 10:
                            print(f"You can't unequip {itemsDict[o][2]}")
                            # sleep(1)
                            break 
                        elif itemsDict[o][11] >= 10: 
                            itemsDict[o][11] -= 10
                            print(f"You unequipped {itemsDict[o][2]}")
                            # sleep(1)
################################## 3 Remove Item #############################                            
            elif userInput == "3":                         
                userInputItemNumber = int (input ('Select item to remove: \n'))
                
                itemKeyList = [key for key in itemsDict]
                for n in itemKeyList:  
                    if userInputItemNumber == itemsDict[n][1]:
                        itemsDict[n][8] -= 1
                        if itemsDict[n][11] >= 10:
                            itemsDict[n][11] -= 10
                        print(f"\n{itemsDict[n][2]} was brought back to his owner!\n")            
                        if itemsDict[n][8] == 0:
                            itemsDict[n][1] = 0                
                # sleep(1)
################################## 4 Return#### #############################     
            elif userInput == "4":
                break 
            else: print("\nCouldn't understand you?!")               

        return itemsDict, playerItemIDs

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

