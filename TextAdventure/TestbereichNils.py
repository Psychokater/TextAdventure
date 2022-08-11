
itemsDict = {
#      0   1        2          3     4       5      6         7        8       9       10     11
#                  Name       atk    def     hp      val      qnt      qnt      ID    ID_ON  use/eq                        Quantity Merchant resets every lvlUp (qnt Max / 2 - qnt P)
#                                                            Max       P                                                    qnt Max = Max qnt in Game
1001:[(0),(0),"Apple",       (0),   (0),    (4),    (1),    (100),    (5),    (10),   (10),  (0)],                          # ID (row 9 and 10)
1002:[(0),(0),"Fish",        (9),   (8),    (1),    (6),     (10),    (5),    (1),    (1),    (0)],                          # 1, 2, 3 = Merchant Inv lvl 5, 10, 20+
1003:[(0),(0),"Cabbage",     (9),   (8),    (1),    (6),      (2),    (0),    (4),    (4),   (0)],                          # 4, 5, 6 = Wizard Inv lvl 5, 10, 20+   
1004:[(0),(0),"Sword",       (9),   (8),    (1),    (6),      (4),    (0),    (6),    (0),   (2)],                          # 7, 8, 9 = Loot Inv lvl 5, 10, 20+                          
1005:[(0),(0),"Shield",      (9),   (8),    (0),    (6),      (4),    (0),    (3),    (0),   (2)],                          # 
1006:[(0),(0),"10 HP Potion",(5),   (8),    (1),    (6),      (2),    (0),    (8),    (0),   (0)],                          # use = 0, equip = 1, equipped = 2
1007:[(0),(0),"20 HP Potion",(9),   (8),    (0),    (6),      (2),    (1),    (10),   (10),  (0)],                          # 
1008:[(0),(0),"ItemName7",   (9),   (8),    (0),    (6),      (2),    (0),    (11),   (0),   (0)],                          # IF lvl "x" Then itemsDict(10) = itemsDict(9)
1009:[(0),(0),"ItemName8",   (9),   (8),    (1),    (6),      (2),    (0),    (12),   (0),   (1)],                          # IF itemsDict(10)  = Value = Item is in game!
1010:[(0),(0),"ItemName9",   (9),   (8),    (1),    (6),      (2),    (0),    (10),   (10),  (1)]}                          # IF itemsDict(10)  = 0 = Item is NOT in game!
#Items: 0 Enum Merch, 1 Enum Player, 2 ItemName, 3 ATK, 4 DEF, 5 HEAL, 6 Value, 7 QntMAX, 8 QntPlayer, 9 ID, 10 ID_ON, 11 use/eq
itemKeyList = []


itemKeyList = [key for key in itemsDict]
for i in itemKeyList:
    print(i)