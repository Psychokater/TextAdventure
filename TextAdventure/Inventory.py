# from time import sleep
import os
from Colors import cl


#############################################################################################################################################################################
#---------------------------------------------------------------------------------- MENUS ----------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################# SHOP MENU (TOWN) #############################################################################

#ENTRYPOINT (Choose where to go -> Merchant, Wizard or Inventory)
def ShopMenu(itemsDict, playerName, playerInventoryMoney, playerStats):
    while True:
        userInput = input("\nWhere do you want to go?\n(1) Merchant\t(2) Wizard \t(3) Inventory\t(0) Leave Town\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerInventoryMoney = MerchantShop(itemsDict, playerName, playerInventoryMoney, playerStats)                                                           
            case "2": itemsDict, playerInventoryMoney = WizardShop(itemsDict, playerName, playerInventoryMoney, playerStats)
            case "3": itemsDict, playerStats = InventoryMenu(itemsDict, playerName, playerInventoryMoney, playerStats)                                                          
            case "0": break

            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney, playerStats

############################################################################# WANDERER MENU #############################################################################

def WandererMenu(itemsDict, playerName, playerInventoryMoney, playerStats):
    while True:
        print("The sky gets dark... you feel the cold...\n")
        userInput = input("\nWhat do you want to do?\n(1) Investigate\t(2) Inventory\t(0) Move On\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerInventoryMoney = WandererShop(itemsDict, playerName, playerInventoryMoney, playerStats);break
            case "2": itemsDict, playerStats = InventoryMenu(itemsDict, playerName, playerInventoryMoney, playerStats)                                                          
            case "0": break

            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney, playerStats


#############################################################################################################################################################################
#--------------------------------------------------------------------------------- PLAYER ----------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################# PRINT PLAYER INVENTORY #############################################################################
# print PlayerInventory + getting ID's
def GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    print(f'{cl.BLUE}{playerName}{cl.RESET}\t\t\tGold:\t{cl.BLUE}{round(playerInventoryMoney,2)}{cl.RESET}\tHP {cl.GREEN}{playerStats[2]}/{playerStats[1]}{cl.RESET}\n\n')
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
            for j in range (0,len(itemsDict[i])):
                if j == 2:
                    print('{:<15}'.format(itemsDict[i][j]),end='')                
                if j == 11:
                    if itemsDict[i][j] > 10:
                        print ("\u25cf",end='')                     
                    elif itemsDict[i][j] > 0 and itemsDict[i][j] < 8:
                        print ("\u25cb",end='')                                 #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 2, 7, 9, 10, 11]                          #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue
                                                                                #
                print (itemsDict[i][j],end='\t')                                #           print Value in this line 
            print()                                                             #   new Line of Inventory        
    print('------------------------------------------------------------------------\n')
    return itemsDict, playerItemIDs
    
############################################################################# INVENTORY MENU #############################################################################
# PlayerInventory                 
def InventoryMenu(itemsDict, playerName, playerInventoryMoney, playerStats):
    os.system('cls')
    playerItemIDs = []

    while True:
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats)
        userInput = input("\n(1) Equipment\t(2) Use Item (3) Remove Items\t(0) Leave Inventory\n")
        os.system('cls')
################ Player Equipment ##########################
        if userInput == "1":
            itemsDict, playerItemIDs = PlayerEquipment(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)
################ Items ####################################
        # elif userInput == "2":
        #     itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)
        #     userInput = input("\n(1) Use\t(2) Remove from Inventory\t(0) Return\n")
            #os.system('cls')
################ Items #### Use Item #################################
        elif userInput == "2":
            while True:
                itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)
                try:
                    userInputItemNumber = int (input ('Select item to use:\t\t(0) Abort \n'))                        
                except ValueError:
                    print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
                    continue
                if userInputItemNumber == 0:
                    break
                os.system('cls')  
                itemKeyList = [key for key in itemsDict]
                for i in itemKeyList: 
                    if userInputItemNumber == itemsDict[i][1]:              
                        if itemsDict[i][11] > 0:
                            print(f"{cl.RED}You can't use{cl.RESET} {cl.YELLOW}{itemsDict[i][2]}{cl.RESET}")
                            continue
                        #################################### Healitems #########################
                        # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
                        if itemsDict[i][5] > 0:
                            if playerStats[2] >= playerStats[1]:
                                print(f"You already have full HP, do you really want to use {cl.YELLOW}{itemsDict[i][2]}{cl.RESET}?")
                                userItemInput = input("(1) Yes!\t(2) No!\n")
                                os.system('cls')
                                if userItemInput == "1":
                                    itemsDict[i][8] -= 1            
                                    if itemsDict[i][8] == 0:
                                        itemsDict[i][1] = 0
                                    print(f"You used {cl.YELLOW}{itemsDict[i][2]}{cl.RESET}")
                                    continue   
                                elif userItemInput == "2":
                                    continue
                                else: print("\nCouldn't understand you?!")
                            if playerStats[2] + itemsDict[i][5] <= playerStats[1]:       
                                playerStats[2] += itemsDict[i][5]
                                print(f"You got healed for {cl.GREEN}{itemsDict[i][5]}{cl.RESET} Points. HP: {cl.GREEN}{playerStats[2]}/{playerStats[1]}{cl.RESET}")                                
                            else:
                                print(f"You got fully healed with {cl.GREEN}{playerStats[1] - playerStats[2]}{cl.RESET} Points. HP: {cl.GREEN}{playerStats[2]}/{playerStats[1]}{cl.RESET}") 
                                playerStats[2] = playerStats[1]                                
                        
                            itemsDict[i][8] -= 1            
                            if itemsDict[i][8] == 0:
                                itemsDict[i][1] = 0    
                            
                                                             
############### Items #### Remove Item ##############################
            # elif userInput == "2":            
            #     while True:
            #         try:
            #             userInputItemNumber = int (input ('Select item to remove:\t\t(0) Abort \n'))                        
            #         except ValueError:
            #             print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            #             continue
            #         os.system('cls')  
            #         itemKeyList = [key for key in itemsDict]
            #         for i in itemKeyList:  
            #             if userInputItemNumber == itemsDict[i][1]:
            #                 if userInputItemNumber == 0:                            
            #                     break
            #                 itemsDict[i][8] -= 1 
            #                 print(f"\n{cl.YELLOW}{itemsDict[i][2]}{cl.RESET} was brought back to his owner!\n")           
            #                 if itemsDict[i][8] == 0:
            #                     itemsDict[i][1] = 0
                        
############### Items #### Break ####################################
            # elif userInput == "0":
            #     break
            # else: print("\nCouldn't understand you?!")
############### Break #####################
        elif userInput == "3":                                               
            while True:
                try:
                    userInputItemNumber = int (input ('Select equipment to remove:\t\t(0) Abort\n'))                        
                except ValueError:
                    print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
                    continue
                os.system('cls')
                if userInputItemNumber == 0:
                    break 
                itemKeyList = [key for key in itemsDict]
                for n in itemKeyList:  
                    if userInputItemNumber == itemsDict[n][1]:                      
                        itemsDict[n][8] -= 1
                        if itemsDict[n][11] >= 10:
                            itemsDict[n][11] -= 10
                        print(f"\n{cl.YELLOW}{itemsDict[n][2]}{cl.RESET} was brought back to his owner!\n")                                   
                        if itemsDict[n][8] == 0:
                            itemsDict[n][1] = 0
                        
        elif userInput == "0": break
        else: print("\nCouldn't understand you?!")
    
    return itemsDict, playerStats

    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq


def GetPlayerEquipment(itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats):
    print(f'{cl.BLUE}{playerName}{cl.RESET}\t\t\tGold:\t{cl.BLUE}{round(playerInventoryMoney,2)}{cl.RESET}\tHP {cl.GREEN}{playerStats[2]}/{playerStats[1]}{cl.RESET}\n\n')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tValue\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1

    playerItemIDs = []        
    itemKeyList = [key for key in itemsDict]                                    # for every Item in itemsDictionary  
    for i in itemKeyList:
        itemsDict[i][1] = 0                                                       #       i = Item ID
        if itemsDict[i][8] > 0 and itemsDict[i][11] > 0:                      #   Quantity Player > 0 for that ItemID AND Equipable?
                    
            itemsDict[i][1] = z                                                 #   Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            playerItemIDs.append(i)                                             #   append Item ID to List of ItemID's
            print('\u2009 ',itemsDict[i][1],end='\t:\t')                        #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                if j == 11:                    
                    if itemsDict[i][j] > 10:
                        print ("\u25cf",end='') #"Equipped"
                    elif itemsDict[i][j] > 0 and itemsDict[i][j] < 8:
                        print ("\u25cb",end='') 
                if j == 2:
                        print('{:<15}'.format(itemsDict[i][j]),end='')          
                _tempListIndexJ = [0, 1, 2, 7, 9, 10, 11]                          #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                   
                                                                                #
                print (itemsDict[i][j],end='\t')                                #           print Value in this line 
            print()                                                             #   new Line of Inventory        
    print('------------------------------------------------------------------------\n')
    return itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats  

def PlayerEquipment(itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats):
    os.system('cls')
    while True:
        itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats = GetPlayerEquipment(
            itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats)   
        userInput = input("\n(1) Equip item\t(2) Unequip item\t(0) Return\n")
        os.system('cls')
################################## 1 Equip Item #############################   
        if userInput == "1":
            while True:
                itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats = GetPlayerEquipment(
                    itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats)                       
                try:
                    userInputItemNumber = int (input ('Select item to equip:\t\t(0) Abort \n'))                        
                except ValueError:
                    print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
                    continue
                os.system('cls')
                if userInputItemNumber == 0:
                    break      
                itemKeyList = [key for key in itemsDict]
                for j in itemKeyList: 
                    if userInputItemNumber == itemsDict[j][1]:                         
                        if itemsDict[j][11] >= 10:
                            print(f"{cl.YELLOW}{itemsDict[j][2]}{cl.RESET} is already equipped!")
                            # sleep(1)
                            continue 
                        else:
                            itemsDict[j][11] += 10
                            for k in itemKeyList:
                                if itemsDict[j][11] == itemsDict[k][11] and j != k:
                                    itemsDict[k][11] -= 10
                
                            print(f"You equipped {itemsDict[j][2]}")
                            continue                        
################################## 2 Unequip Item #############################               
        elif userInput == "2":  
            while True:
                itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats = GetPlayerEquipment(
                    itemsDict , playerItemIDs, playerName, playerInventoryMoney, playerStats)   
                try:
                    userInputItemNumber = int (input ('Select item to unequip:\t\t(0) Abort\n'))                        
                except ValueError:
                    print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
                    continue
                os.system('cls')  
                if userInputItemNumber == 0:                            
                    break                     
                itemKeyList = [key for key in itemsDict]
                for o in itemKeyList: 
                    if userInputItemNumber == itemsDict[o][1]:                          
                        if itemsDict[o][11] < 10:
                            print(f"{cl.RED}You have already unequipped{cl.RESET} {cl.YELLOW}{itemsDict[o][2]}{cl.RESET}")
                            # sleep(1)
                            continue 
                        elif itemsDict[o][11] >= 10: 
                            itemsDict[o][11] -= 10
                            print(f"You unequipped {cl.YELLOW}{itemsDict[o][2]}{cl.RESET}")
                            continue                                
                            # sleep(1)
################################## 3 Remove Item #############################                            
        # elif userInput == "3":                         
        #     while True:
        #         try:
        #             userInputItemNumber = int (input ('Select item to remove:\t\t(0) Abort\n'))                        
        #         except ValueError:
        #             print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
        #             continue
        #         os.system('cls')
                
        #         itemKeyList = [key for key in itemsDict]
        #         for n in itemKeyList:  
        #             if userInputItemNumber == itemsDict[n][1]:
        #                 if userInputItemNumber == 0:
        #                     break 
        #                 itemsDict[n][8] -= 1
        #                 if itemsDict[n][11] >= 10:
        #                     itemsDict[n][11] -= 10
        #                 print(f"\n{cl.YELLOW}{itemsDict[n][2]}{cl.RESET} was brought back to his owner!\n")                                   
        #                 if itemsDict[n][8] == 0:
        #                     itemsDict[n][1] = 0
                                        
            # sleep(1)
################################## 4 Return#### #############################     
        elif userInput == "0":
            break 
        else: print("\nCouldn't understand you?!")               

    return itemsDict, playerItemIDs



#############################################################################################################################################################################
#-------------------------------------------------------------------------------- MERCHANT ---------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################### MERCHANT SHOP ###############################################################################

# Merchant (Print Merchant and PlayerInventory - Choose if Buy or Sell)
def MerchantShop(itemsDict, playerName, playerInventoryMoney, playerStats):
    os.system('cls')
    PicMerchant()
    merchantItemIDs = []
    playerItemIDs = []
    while True:
        itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(0) Leave Merchant\n")
        os.system('cls')      
        match userInput:
            case "1": itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney = MerchantItemBuy(
                itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney, playerStats)
            case "2": itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney = MerchantItemSell(
                itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney, playerStats)
            case "0": break
            case _: print("\nCouldn't understand you?!")
    
    return itemsDict, playerInventoryMoney

############################################################################# MERCHANT INVENTORY #############################################################################
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
                _tempListIndexJ = [0, 1, 2, 8, 9, 10, 11]
                if j == 2:
                    print('{:<15}'.format(itemsDict[i][j]),end='')                            #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                                                    #
                if j == 6:                                                      #           if Index == "Value of Item":
                    print(round(itemsDict[i][j]* 1.5 + 2,2),end='\t')                    #               Print "Value" of Item * 1.5 + 2
                    continue                                                    #
                if j == 7:                                                      #           if Index == "MaxQuantity" of Item:
                    print(itemsDict[i][j] - itemsDict[i][8])                    #           print "MaxQuantity" (for "Merchant Quantity")
                    continue                                                    #           
                print (itemsDict[i][j],end='\t')                                #           print Value in this line
                                                                                #   new Line of Inventory
    print('------------------------------------------------------------------------\n')
    return itemsDict, merchantItemIDs

############################################################################# BUY FROM MERCHANT #############################################################################
# +ItemPlayer -MoneyPlayer
def MerchantItemBuy(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    while True:
        itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)
        try:
            userInputItemNumber = int (input ('Pick an Item number to buy it:\t\t(0) Abort \n'))
        except ValueError:
            print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            continue          
        os.system('cls') 
        if userInputItemNumber == 0:
            break   
        itemKeyList = [key for key in itemsDict]
        for i in itemKeyList:    
            if userInputItemNumber == itemsDict[i][0]:
           
                if playerInventoryMoney < round(itemsDict[i][6] * 1.5 + 2,2): 
                    print("\nNot enough money, fool!\n")
                    # sleep(1)
                    continue     
                else: 
                    playerInventoryMoney -= round(itemsDict[i][6] * 1.5 + 2,2)
                    itemsDict[i][8] += 1            
                    if itemsDict[i][8] == 0:
                        itemsDict[i][0] = 0

    return itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney

############################################################################# SELL TO MERCHANT #############################################################################
# -ItemPlayer +MoneyPlayer
def MerchantItemSell(itemsDict, playerItemIDs, merchantItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    while True: 
        itemsDict, merchantItemIDs = GetInventoryMerchant(itemsDict, merchantItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)    
        try:
            userInputItemNumber = int (input ('Pick an Item number to sell it:\t\t(0) Abort \n'))            
        except ValueError:
            print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            continue
        os.system('cls')
        if userInputItemNumber == 0:
            break          
        itemKeyList = [key for key in itemsDict]
        for i in itemKeyList:  
            if userInputItemNumber == itemsDict[i][1]:
                playerInventoryMoney += round(itemsDict[i][6],2)
                itemsDict[i][8] -= 1            
                if itemsDict[i][8] == 0:
                    itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, merchantItemIDs, playerInventoryMoney



#############################################################################################################################################################################
#--------------------------------------------------------------------------------- WIZARD ----------------------------------------------------------------------------------#
#############################################################################################################################################################################




################################################################################ WIZARD SHOP ################################################################################

#Wizard (Print Wizard and PlayerInventory - Choose if Buy or Sell)
def WizardShop(itemsDict, playerName, playerInventoryMoney, playerStats):
    os.system('cls')
    PicWizard()
    wizardItemIDs = []
    playerItemIDs = []
    while True:
        itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(0) Leave Wizard\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney = WizardItemBuy(
                itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney, playerStats)
            case "2": itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney = WizardItemSell(
                itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney, playerStats)
            case "0": break
            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney 

############################################################################# WIZARD INVENTORY #############################################################################
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
        _tempListIndexValue = [4, 5, 6]                                         #       List of ID to Sell at Wizard
        if itemsDict[i][10] in _tempListIndexValue and (                        #       If Item ID of selected Item is activated AND ->
            (itemsDict[i][7] - itemsDict[i][8]) > 0):                           #       Item Quantity Wizard > 0
            itemsDict[i][0] = z                                                 #       Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            wizardItemIDs.append(i)                                             #   append Item ID to List of ItemID's
            print ('\u2009 ',itemsDict[i][0],end='\t:\t')                       #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 2, 8, 9, 10, 11]
                if j == 2:
                    print('{:<15}'.format(itemsDict[i][j]),end='')                            #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                                                    #
                if j == 6:                                                      #           if Index == "Value of Item":
                    print(round(itemsDict[i][j]* 1.5 + 2,2),end='\t')                    #               Print "Value" of Item * 1.5 + 2
                    continue                                                    #
                if j == 7:                                                      #           if Index == "MaxQuantity" of Item:
                    print(itemsDict[i][j] - itemsDict[i][8])                    #           print "MaxQuantity" (for "Wizard Quantity")
                    continue                                                    #           
                print (itemsDict[i][j],end='\t')                                #           print Value in this line
                                                                                #   new Line of Inventory
    print('------------------------------------------------------------------------\n')
    return itemsDict, wizardItemIDs

############################################################################# BUY FROM WIZARD #############################################################################
# +ItemPlayer -MoneyPlayer
def WizardItemBuy(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    while True:
        itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)
        try:    
            userInputItemNumber = int (input ('Pick an Item number to buy it:\t\t(0) Abort \n'))            
        except ValueError:
            print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            continue
        os.system('cls')
        if userInputItemNumber == 0:
            break          
        itemKeyList = [key for key in itemsDict]
        for i in itemKeyList:  
            if userInputItemNumber == itemsDict[i][0]:               
                if playerInventoryMoney < round(itemsDict[i][6] * 1.5 + 2,2): 
                    print("\nNot enough money, fool!\n")
                    # sleep(1)
                    continue
                else:
                    playerInventoryMoney -= round(itemsDict[i][6] * 1.5 + 2,2)
                    itemsDict[i][8] += 1            
                    if itemsDict[i][8] == 0:
                        itemsDict[i][0] = 0
       

    return itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney

############################################################################# SELL TO WIZARD #############################################################################
# -ItemPlayer +MoneyPlayer
def WizardItemSell(itemsDict, playerItemIDs, wizardItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    while True:    
        itemsDict, wizardItemIDs = GetInventoryWizard(itemsDict, wizardItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)    
        try:
            userInputItemNumber = int (input ('Pick an Item number to sell it:\t\t(0) Abort \n'))            
        except ValueError:
            print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            continue
        os.system('cls') 
        if userInputItemNumber == 0:
            break        
        itemKeyList = [key for key in itemsDict]
        for i in itemKeyList:            
            if userInputItemNumber == itemsDict[i][1]:
                playerInventoryMoney += round(itemsDict[i][6],2)
                itemsDict[i][8] -= 1            
                if itemsDict[i][8] == 0:
                    itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, wizardItemIDs, playerInventoryMoney




#############################################################################################################################################################################
#-------------------------------------------------------------------------------- WANDERER ---------------------------------------------------------------------------------#
#############################################################################################################################################################################



############################################################################# WANDERER SHOP #############################################################################
    #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
#Wanderer (Print Wanderer and PlayerInventory - Choose if Buy or Sell)
def WandererShop(itemsDict, playerName, playerInventoryMoney, playerStats):
    os.system('cls')
    PicWanderer()
    wandererItemIDs = []
    playerItemIDs = []
    while True:
        itemsDict, wandererItemIDs = GetInventoryWanderer(itemsDict, wandererItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)

        userInput = input("\nWhat whould you like ?\n(1) Buy\t\t(2) Sell\t(0) Leave Wanderer\n")      
        os.system('cls')
        match userInput:
            case "1": itemsDict, playerItemIDs, wandererItemIDs, playerInventoryMoney = WandererItemBuy(
                itemsDict, playerItemIDs, wandererItemIDs, playerName, playerInventoryMoney, playerStats)
            case "2": itemsDict, playerItemIDs, wandererItemIDs, playerInventoryMoney = WandererItemSell(
                itemsDict, playerItemIDs, wandererItemIDs, playerName, playerInventoryMoney, playerStats)
            case "0": break
            case _: print("\nCouldn't understand you?!")

    return itemsDict, playerInventoryMoney 

############################################################################# WANDERER INVENTORY #############################################################################
    # print WandererInventory + getting iD's
def GetInventoryWanderer(itemsDict, wandererItemIDs):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    print('Wanderer:\n')
    print('  Nr.\t\tItem\t\tATK\tDEF\tHeal\tPrice\tQuantity\n'\
    '------------------------------------------------------------------------')
    z = 1   
    
    itemKeyList = [key for key in itemsDict]                                    # for every Item in itemsDictionary  
    for i in itemKeyList:  
        itemsDict[i][0] = 0                                                     #       i = Item ID
        _tempListIndexValue = [10,11,12]                                        #       List of ID to Sell at Wanderer
        if itemsDict[i][10] in _tempListIndexValue and (                        #       If Item ID of selected Item is activated AND ->
            (itemsDict[i][7] - itemsDict[i][8]) > 0):                           #       Item Quantity Wanderer > 0
            itemsDict[i][0] = z                                                 #       Enumerate Itemline
            z += 1                                                              #   Enumerate + 1
            wandererItemIDs.append(i)                                           #   append Item ID to List of ItemID's
            print ('\u2009 ',itemsDict[i][0],end='\t:\t')                       #   print Enumerate
            for j in range (0,len(itemsDict[i])):                               #       for every Value Index of every Item
                _tempListIndexJ = [0, 1, 2, 8, 9, 10, 11]
                if j == 2:
                    print('{:<15}'.format(itemsDict[i][j]),end='')                            #           except for these Indexes!
                if j in _tempListIndexJ:                                        #
                    continue                                                    #
                if j == 6:                                                      #           if Index == "Value of Item":
                    print(round(itemsDict[i][j]* 1.5 + 2,2),end='\t')                    #               Print "Value" of Item * 1.5 + 2
                    continue                                                    #
                if j == 7:                                                      #           if Index == "MaxQuantity" of Item:
                    print(itemsDict[i][j] - itemsDict[i][8])                    #           print "MaxQuantity" (for "Wanderer Quantity")
                    continue                                                    #           
                print (itemsDict[i][j],end='\t')                                #           print Value in this line
                                                                                #   new Line of Inventory
    print('------------------------------------------------------------------------\n')
    return itemsDict, wandererItemIDs

############################################################################# BUY FROM WANDERER #############################################################################
    # +ItemPlayer -MoneyPlayer
def WandererItemBuy(itemsDict, playerItemIDs, wandererItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    while True:
        itemsDict, wandererItemIDs = GetInventoryWanderer(itemsDict, wandererItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)
        try:    
            userInputItemNumber = int (input ('Pick an Item number to buy:\t\t(0) Abort \n'))            
        except ValueError:
            print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            continue
        os.system('cls') 
        if userInputItemNumber == 0:
            break 
        itemKeyList = [key for key in itemsDict]
        for i in itemKeyList:  
            if userInputItemNumber == itemsDict[i][0]:             
                if playerInventoryMoney < round(itemsDict[i][6] * 1.5 + 2,2): 
                    print("\nNot enough money, fool!\n")
                    # sleep(1)
                    continue
                else:
                    playerInventoryMoney -= round(itemsDict[i][6] * 1.5 + 2,2)
                    itemsDict[i][8] += 1            
                    if itemsDict[i][8] == 0:
                        itemsDict[i][0] = 0
       

    return itemsDict, playerItemIDs, wandererItemIDs, playerInventoryMoney

############################################################################# SELL TO WANDERER #############################################################################
# -ItemPlayer +MoneyPlayer
def WandererItemSell(itemsDict, playerItemIDs, wandererItemIDs, playerName, playerInventoryMoney, playerStats):
      #Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq 
    os.system('cls')
    while True:    
        itemsDict, wandererItemIDs = GetInventoryWanderer(itemsDict, wandererItemIDs)
        itemsDict, playerItemIDs = GetInventoryPlayer(itemsDict, playerItemIDs, playerName, playerInventoryMoney, playerStats)    
        try:
            userInputItemNumber = int (input ('Pick an Item number to sell:\t\(0) Abort \n'))           
        except ValueError:
            print(f"\n{cl.RED}That's not a number, dumbass!{cl.RESET}")
            continue
        os.system('cls')
        if userInputItemNumber == 0:
            break         
        itemKeyList = [key for key in itemsDict]
        for i in itemKeyList:            
            if userInputItemNumber == itemsDict[i][1]:
                playerInventoryMoney += round(itemsDict[i][6],2)
                itemsDict[i][8] -= 1            
                if itemsDict[i][8] == 0:
                    itemsDict[i][1] = 0
                               
    return itemsDict, playerItemIDs, wandererItemIDs, playerInventoryMoney
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

def PicWanderer():
    print("""
                    O 
           ___      |    
          / .-\   ./=}
         |  |"|_/\/ |
         ;  |-;| /_ |
        / \_| |/ \  |
       /      \/\(  @
       |   /  |` )  |
       /   \ _/     @
      /--._/  \     |
      `/|)    |     |
        /     |     |
      .'      |     |
     /         \    |
    (_.-.__.__./    /
    """)













