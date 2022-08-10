import os

######## call Itemlist of Player (Index 8 != 0)
def call_P_list(all_items):
    print ('Your Items : ')
    print (' Item.NR      Item    Attack  Defence  Heal   Quantity ')
    z = 1
    for i in range (0,len(all_items)):
        k = i + 1001
        inputListeP = []
        if all_items[k][9] > 0:
            all_items[k][1] = z
            z += 1            
            inputListeP.append(i)
            print ('\u2009 ',all_items[k][1],end='  :  ')
            for j in range (2,len(all_items[k])-4):
                print (all_items[k][j],end='\t')
            print (all_items[k][9])

    return inputListeP, all_items


def call_M_list(all_items):
    print ('Merchant Items : ')
    print ('  Item.NR      Item    Attack  Defence   Heal   Value   Price  Quantity ')
    z = 1
    for i in range (0,len(all_items)):
        i += 1001
        inputListeM = []
        if all_items[i][8] > 0:
            all_items[i][0] = z
            z += 1            
            inputListeM.append(i)
            print ('\u2009 ',all_items[i][0],end='  :  ')
            for j in range (1,len(all_items[i])-1):
                if j == 1:
                    continue
                print (all_items[i][j],end='\t')
            print ()

    return inputListeM, all_items

def buy_anItem(all_items):
    os.system('cls')
    inputListeM, all_items = call_M_list(all_items)
    inputListeP, all_items = call_P_list(all_items)
    Item_number = int (input ('Pick an Item number to buy it : \n'))
    for i in range (0,len(all_items)):
        i +=1001       
        if Item_number == all_items[i][0]:
            all_items[i][8] -= 1
            all_items[i][9] += 1
            if all_items[i][8] == 0:
                all_items[i][0] = 0

    return all_items

def sell_anItem(all_items):
    os.system('cls')
    inputListeM, all_items = call_M_list(all_items)
    inputListeP, all_items = call_P_list(all_items)    
    Item_number = int (input ('Pick an Item number to sell it : \n'))
    for i in range (0,len(all_items)):
        i +=1001
        if Item_number == all_items[i][1]:
            all_items[i][8] += 1
            all_items[i][9] -= 1
            if all_items[i][9] == 0:
                all_items[i][1] = 0
                               
    return all_items



def shop_menu():
        all_items = {
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
                case "1": all_items, inputListeP, inputListeM = merchant(all_items, inputListeP, inputListeM)

                case "2": inputListeP, all_items = inventory(inputListeP, all_items)

                case "3": break

                case _: print("\nCouldn't understand you?!")

def merchant(all_items, ):
    os.system('cls')
    while True:
        inputListeM, all_items = call_M_list(all_items)
        inputListeP, all_items = call_P_list(all_items)

        userInput = input("\nWhat whould you like ?\n(1) Buy an Item\t\t(2) Sell an Item\t(3) Leave Merchant\n")      
        match userInput:
            case "1": all_items = buy_anItem(all_items)
            case "2": all_items = sell_anItem(all_items)
            case "3": break
            case _: print("\nCouldn't understand you?!")
    
    return all_items, inputListeP, inputListeM

def inventory(inputListeP, all_items):
    while True:
        inputListeP, all_items = call_P_list(all_items)
        userInput = input("\n(1) Equip\t\t(2) Remove from Inventory\t(3) Leave Inventory\n")
        if userInput == "1":
            pass
        elif userInput == "2":
            pass
        elif userInput == "3": break
        else: print("\nCouldn't understand you?!")
    return inputListeP, all_items
shop_menu()
