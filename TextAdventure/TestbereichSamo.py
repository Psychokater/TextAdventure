from multiprocessing.dummy import Value


all_items = {
1:["Apple    ",(0),(0),(7),(6),(5)],
2:["ItemName1",(9),(8),(0),(6),(5)],
3:["ItemName2",(9),(8),(0),(6),(5)],
4:["ItemName3",(9),(8),(0),(6),(5)],
5:["ItemName4",(9),(8),(0),(6),(5)],
6:["ItemName5",(9),(8),(0),(6),(5)],
7:["ItemName6",(9),(8),(0),(6),(5)],
8:["ItemName7",(9),(8),(0),(6),(5)],
9:["ItemName8",(9),(8),(0),(6),(5)]}
player_items= {
1:["Apple1   ",(0),(0),(7),(3),(2)],
2:["ItemName1",(1),(1),(0),(3),(1)]}
while True:
    def call_item_list():
        print ('Merchant Items : ')
        print ('\u2009____________________________________')
        print ('\uFF5C         Item    ATK DEF HP VL PR \uFF5C')
        for y,(key,value) in enumerate (all_items.items(),start=1):
            print ('\uFF5C',y,':',value,'\uFF5C')
        print (end='\u2009')
        print ('\u203e'*36)
    def call_player_list():
        print ('Your Items : ')
        print ('\u2009____________________________________')
        print ('\uFF5C         Item    ATK DEF HP VL QTY\uFF5C')
        for y,(key,value) in enumerate (player_items.items(),start=1):
            print ('\uFF5C',y,':',value,'\uFF5C')
        print (end='\u2009')
        print ('\u203e'*36)

    def merchant_sell(x):
        if x in player_items.keys():
            player_items[x][5]+=1
            print ('Here is Your Invantory : ')
            call_player_list()
        else:
            sold_item =  { x : all_items[x]}
            sold_item[x][5]-=(sold_item[x][5]-1)
            player_items.update(sold_item)
            print ('Sold Item : ',sold_item)
            print ('Here is Your Invantory : ')
            call_player_list()
    def buy_an_item():
        call_item_list()
        while True:
            try :
                x = int (input ('pick an item number to buy : '))
                if x in all_items.keys():
                    print ('                     Item    ATK DEF HP VL PR ')
                    sold_item = dict ({ x : all_items[x]})
                    print ('Sold Item : ',sold_item)
                    break
            except ValueError:
                print ('pick an Item number from the Items list ! ')
                continue
        merchant_sell(x)


    def merchant_buy(x):
        if x not in player_items.keys():
            print ('Pick an Item number from your Items list !')
            sell_an_item()
        elif x in player_items.keys() and player_items[x][5]==1:
            del player_items[x]
            print ('Here is Your Invantory : ')
            call_player_list()
        elif x in player_items.keys():
            player_items[x][5]-=1
            print ('Here is Your Invantory : ')
            call_player_list()
        else:
            bought_item = dict ({ x : all_items[x]})
            print ('Bought Item :',bought_item)
            print ('Here is Your Invantory : ')
            call_player_list()
    def sell_an_item():
        call_player_list()
        while True:
            try :
                x = int (input ('pick an item number to sell : '))
                if x in all_items.keys():
                    print ('                     Item    ATK DEF HP VL PR ')
                    bought_item = dict ({ x : all_items[x]})
                    print ('Bought Item : ',bought_item)
                    break
            except ValueError:
                print ('pick an Item number from the Items list ! ')
                continue

        merchant_buy(x)
    x = input (' bey 1 , sell 2 : \n')
    if '1' in x :
        buy_an_item()
    else :
        sell_an_item()

