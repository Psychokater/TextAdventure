def call_P_list(all_items):
    print ('Your Items : ')
    print (' Item.NR      Item    Attack  Defence  Heal   Quantity ')
    z = 1
    for i in range (0,len(all_items)):
        i +=1001
        if all_items[i][8] > 0:
            all_items[i][0]=z
            z+=1
            inputliste = []
            inputliste.append(i)
            print ('\u2009 ',all_items[i][0],end='  :  ')
            for j in range (1,len(all_items[i])-4):
                print (all_items[i][j],end='\t')
            print (all_items[i][8])
    return all_items


def call_M_list(all_items):
    print ('Merchant Items : ')
    print ('  Item.NR      Item    Attack  Defence   Heal   Value   Price  Quantity ')
    z = 1
    for i in range (0,len(all_items)):
        i +=1001
        if all_items[i][7] > 0:
            all_items[i][0]=z
            z+=1
            inputliste = []
            inputliste.append(i)
            print ('\u2009 ',all_items[i][0],end='  :  ')
            for j in range (1,len(all_items[i])-1):
                print (all_items[i][j],end='\t')
            print ()
    return all_items

def buy_anItem(all_items):
    all_items = call_M_list(all_items)
    Item_number = int (input ('Pick an Item number to buy it : \n'))
    for i in range (0,len(inputliste)):
        i +=1001
        Item_number+=1000
        if Item_number == all_items[i][0]:
            all_items[Item_number][7]-=1
            all_items[Item_number][8]+=1
            all_items = call_P_list(all_items)
    return all_items

def sell_anItem(all_items):
    all_items = call_P_list(all_items)
    Item_number = int (input ('Pick an Item number to sell it : \n'))
    if Item_number in all_items:
        all_items[Item_number][6]+=1
        all_items[Item_number][7]-=1
        all_items = call_P_list(all_items)
    return all_items

def shop_menu():
        all_items = {
        #                         atk def  hp val  pr  qnt  qnt  
        #                                               M    P
        1001:[(0),"Apple     ==>",(0),(0),(2),(6),(99),(99),(2)],
        1002:[(0),"ItemName1 ==>",(9),(8),(1),(6),(99),(99),(1)],
        1003:[(0),"ItemName2 ==>",(9),(8),(1),(6),(99),(99),(0)],
        1004:[(0),"ItemName3 ==>",(9),(8),(1),(6),(99),(99),(1)],
        1005:[(0),"ItemName4 ==>",(9),(8),(0),(6),(99),(99),(0)],
        1006:[(0),"ItemName5 ==>",(5),(8),(1),(6),(99),(99),(0)],
        1007:[(0),"ItemName6 ==>",(9),(8),(0),(6),(99),(99),(0)],
        1008:[(0),"ItemName7 ==>",(9),(8),(0),(6),(99),(99),(0)],
        1009:[(0),"ItemName8 ==>",(9),(8),(1),(6),(99),(99),(1)],
        1010:[(0),"ItemName9 ==>",(9),(8),(1),(6),(99),(99),(1)]}


        userInput = input("\nWhat whould you like ?\n(1) Buy an Item\t\t(2) Sell an Item\t(3) Inventory\t  (4) Exit to main menu\n")
        match userInput:
            case "1": all_items = buy_anItem(all_items)

            case "2": all_items = sell_anItem(all_items)

            case "3": all_items = call_P_list(all_items)

            # case "4":
            case _: print("\nCouldn't understand you?!")
        return all_items

shop_menu()
