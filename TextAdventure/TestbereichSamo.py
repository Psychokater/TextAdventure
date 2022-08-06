all_items = {
1:["Apple    ",(0),(0),(7),(6),(5)],
2:["ItemName1",(9),(8),(0),(6),(5)],
3:["ItemName2",(9),(8),(0),(6),(5)],
4:["ItemName3",(9),(8),(0),(6),(5)],
5:["ItemName4",(9),(8),(0),(6),(5)],
6:["ItemName5",(9),(8),(0),(6),(5)],
7:["ItemName6",(9),(8),(0),(6),(5)],
8:["ItemName7",(9),(8),(0),(6),(5)],
9:["ItemName8",(9),(8),(0),(6),(5)],}
player_items= {
1:["Apple2   ",(0),(0),(7),(3),(2)],
2:["ItemName1",(1),(1),(0),(3),(0)],}
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
            sold_item = dict ({ x : all_items[x]})
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
                    print ('!!')
                    break
            except ValueError:
                print ('pick an Item number from the Items list ! ')
                continue
        merchant_sell(x)

    buy_an_item()

