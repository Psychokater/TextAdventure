
all_items = {
1010:["ItemName1",(9),(8),(0),(6),(5)],
1001:["Apple    ",(0),(0),(7),(6),(5)],
1011:["ItemName2",(9),(8),(0),(6),(5)],
1100:["ItemName3",(9),(8),(0),(6),(5)],
1101:["ItemName4",(9),(8),(0),(6),(5)],
1110:["ItemName5",(5),(8),(0),(6),(5)],
1111:["ItemName6",(9),(8),(0),(6),(5)],
2000:["ItemName7",(9),(8),(0),(6),(5)],
2001:["ItemName8",(9),(8),(0),(6),(5)],
2010:["ItemName9",(9),(8),(0),(6),(5)]}
player_items= {
1001:["Apple    ",(0),(0),(7),(3),(2)],
1010:["ItemName1",(1),(1),(0),(3),(1)]}

while True:

    def call_item_list():
        print ('Merchant Items : ')
        print ('\u2009_________________________________________')
        print ('\uFF5C ItemNumber   Item    ATK DEF HP VL PR \uFF5C')
        for y,(key,value) in enumerate (sorted(all_items.items()),start=1):
            print ('\uFF5C',y,key,'==>',value,'\uFF5C')
        print (end='\u2009')
        print ('\u203e'*41)


    def call_player_list():
        print ('Your Items : ')
        print ('\u2009_________________________________________')
        print ('\uFF5C ItemNumber   Item    ATK DEF HP VL QTY\uFF5C')
        for y,(key,value) in enumerate (sorted(player_items.items()),start=1):
            print ('\uFF5C',y,key,'==>',value,'\uFF5C')
        print (end='\u2009')
        print ('\u203e'*41)

            
        
    def merchant_sell(x):
        
        if x in player_items.keys():
            player_items[x][5]+=1
            call_player_list()
        elif x not in player_items.keys():
            sold_item = all_items[x]
            print (sold_item)
            player_items[x]=sold_item
            player_items[x][5]= 1
            call_player_list()
        else :
            pass


    def buy_an_item():
        call_item_list()
        while True:
            try :
                x = int (input ('pick an item number to buy : '))
                if x in all_items.keys():
                    print ('           ItemNumber   Item    ATK DEF HP VL PR ')
                    sold_item = dict ({ x : all_items[x]})
                    print ('Sold Item : ',sold_item)
                    break
                if x not in all_items.keys():
                    print ('pick an Item number from the Items list ! ')
                    call_item_list()
                continue
            except ValueError:
                print ('pick an Item number from the Items list ! ')
                call_item_list()
                continue
        merchant_sell(x)


    def merchant_buy(x):
        if x not in player_items.keys():
            print ('Pick an Item number from your Items list !')
            sell_an_item()
        elif x in player_items.keys() and player_items[x][5]==1:
            del player_items[x]
            call_player_list()
        else:
            x in player_items.keys() and player_items[x][5]>1
            player_items[x][5]-=1
            call_player_list()


    def sell_an_item():
        call_player_list()
        while True:
            try :
                x = int (input ('pick an ItemNumber to sell : '))
                if x in player_items.keys():
                    print ('             ItemNumber   Item    ATK DEF HP VL PR ')
                    bought_item = dict ({ x : all_items[x]})
                    print ('Bought Item : ',bought_item)
                    break
                if x not in player_items.keys():
                    print ('pick an Item number from the Items list ! ')
                    call_player_list()
                    continue
            except ValueError:
                print ('pick an Item number from the Items list ! ')
                call_player_list()
                continue
        merchant_buy(x)


    f = input (' bey 1 , sell 2 : \n')
    if '1' in f :
         buy_an_item()
    elif '2' in f :
        sell_an_item()

