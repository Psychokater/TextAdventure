all_items = {
#                     atk def  hp val  pr  qnt  qnt  
#                                           M    P
1001:["Apple     ==>",(0),(0),(2),(6),(99),(99),(2)],
1002:["ItemName1 ==>",(9),(8),(1),(6),(99),(99),(1)],
1003:["ItemName2 ==>",(9),(8),(1),(6),(99),(99),(0)],
1004:["ItemName3 ==>",(9),(8),(1),(6),(99),(99),(1)],
1005:["ItemName4 ==>",(9),(8),(0),(6),(99),(99),(0)],
1006:["ItemName5 ==>",(5),(8),(1),(6),(99),(99),(0)],
1007:["ItemName6 ==>",(9),(8),(0),(6),(99),(99),(0)],
1008:["ItemName7 ==>",(9),(8),(0),(6),(99),(99),(0)],
1009:["ItemName8 ==>",(9),(8),(1),(6),(99),(99),(1)],
1010:["ItemName9 ==>",(9),(8),(1),(6),(99),(99),(1)]}
# while True:
while True:
    def call_P_list():
        print ('Your Items : ')
        print ('  Item.NR      Item          Attack  Defence   Heal   Value  Quantity ')
        for i in range (0,len(all_items)):
            i +=1001
            if all_items[i][7] > 0 :
                print ('\u2009 ',i,end='  :  ')
                for j in range (0,len(all_items[i])-3):
                    print (all_items[i][j],end='\t')
                print (all_items[i][7])


    def call_M_list():
        print ('Merchant Items : ')
        print ('  Item.NR      Item          Attack  Defence   Heal   Value   Price  Quantity ')
        for i in range (0,len(all_items)):
            i +=1001
            if all_items[i][6] > 0:
                print ('\u2009 ',i,end='  :  ')
                for j in range (0,len(all_items[i])-1):
                    print (all_items[i][j],end='\t')
                print ()

    def buy_anItem():
        call_M_list()
        Item_number = int (input ('Pick an Item number to buy it : \n'))
        if Item_number in all_items.keys():
            all_items[Item_number][6]-=1
            all_items[Item_number][7]+=1
            call_P_list()

    def sell_anItem():
        call_P_list()
        Item_number = int (input ('Pick an Item number to sell it : \n'))
        if Item_number in all_items:
            all_items[Item_number][6]+=1
            all_items[Item_number][7]-=1
            call_P_list()

    def shop_menu():
            userInput = input("\nWhat whould you like ?\n(1) Buy an Item\t\t(2) Sell an Item\t(3) Inventory\t  (4) Exit to main menu\n")
            match userInput:
                case "1":buy_anItem()

                case "2": sell_anItem()

                case "3": call_P_list()

                # case "4":
                case _: print("\nCouldn't understand you?!")
    
    shop_menu()
