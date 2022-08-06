all_items = {
1:["Apple    ",(9),(8),(7),(6),(5)],
2:["ItemName1",(9),(8),(7),(6),(5)],
3:["ItemName2",(9),(8),(7),(6),(5)],
4:["ItemName3",(9),(8),(7),(6),(5)],
5:["ItemName4",(9),(8),(7),(6),(5)],
6:["ItemName5",(9),(8),(7),(6),(5)],
7:["ItemName6",(9),(8),(7),(6),(5)],
8:["ItemName7",(9),(8),(8),(6),(5)],
9:["ItemName8",(9),(8),(7),(6),(5)],
}
def call_item_list():
    print ('\u2009____________________________________')
    print ('\uFF5C     Item       ATK DEF HP VL PR  \uFF5C')
    for (key,value) in (all_items.items()):
        print ('\uFF5C',key,':',value,'\uFF5C')
    print (end='\u2009')
    print ('\u203e'*36)
call_item_list()