from time import sleep







 # SAMOOOO CAN YOU FINALLY MAKE THIS FUCKIN FEATURE SO WE CAN FINISH THIS GAME?!?!?!





def InventoryMenu(playerInventoryItems, playerInventoryMoney, playerName):
    while True:
        userInput = input(f"""
{playerName}
\nGold: {playerInventoryMoney}
Inventory: {playerInventoryItems}

(1) Return\n
""")                                                                             

        match userInput:
            case "1": break
            case _: print("\nCouldn't understand you?!")     
                                                                                     
    return playerInventoryItems, playerInventoryMoney



# def EncounterMerchant():
#     while True:
#         userInput = input(f"\nYour Inventory: {playerInventoryItems}\n(1) Buy\t(2) Sell\t(3) Return\n")
#         match userInput:
#             case "1": MerchantBuy()
#             case "2": MerchantSell()
#             case "3": break
#             case _: print("\nCouldn't understand you?!")

# def MerchantBuy():
#     print("\nWhat do you want to buy?")
#     sleep(2)
#     print(f"Your Gold: {playerInventoryMoney}")
#     print(f"Merchant Gold: {merchantInventoryMoney}")    
#     print(merchantInventoryItems)
#     print(playerInventoryItems)

    ### maybe print Inventory like this:
    ###                 ATK     DEF     HEAL     Value
    ### (1) "Item1"      2       0       0         2
    ### (2) "Item2"      0       0       4         5

    ### "Buy "Item": = Int User Input
    ### if Money >= Value: 
    ### playerInventoryMoney -= Value Item
    ### merchantInventoryMoney += Value Item
    ### playerInventoryItem += Item
    ### MerchantInventoryItem -= Item

    ### maybe Option for "equip" and "use" ?

# def MerchantSell():
#     print("\nWhat do you want to sell?")
#     sleep(2)
#     print(f"Your Gold: {playerInventoryMoney}")
#     print(f"Merchant Gold: {merchantInventoryMoney}")
#     print(merchantInventoryItems)
#     print(playerInventoryItems)
    
    #see MerchantBuy()