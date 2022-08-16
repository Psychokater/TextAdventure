import pickle
import os



#############################################################################################################################################################################
#-------------------------------------------------------------------------------- SAVE/LOAD --------------------------------------------------------------------------------#
#############################################################################################################################################################################



#################################################################################### SAVE ####################################################################################
def Save(dataSaveList):    
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    if dataSaveList[0] == 0:
        with open(f"SaveFile_Autosave.pickle", 'wb') as autoSaveHandler:
            pickle.dump(dataSaveList, autoSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
            if len(dataSaveList[1]) == 0:
                dataSaveList[1].append("Autosave")
            else:
                dataSaveList[1] = "Autosave"                                                                           #Add AutoSave to savePoints[0]        
    elif dataSaveList[0] == 1:
        while True:
            saveFileID = 1
            print(' Nr.\t\tSavefile'\
                '\n------------------------------------------------------------------------')
            for i in range(0, len(dataSaveList[1])):
                print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                saveFileID += 1
            print('------------------------------------------------------------------------\n')
            userInput = input(f"\n(1) Save\t(2) Delete\t (0) Return\n")
            if userInput == "1": 
                while True:
                    saveFileID = 1
                    print(' Nr.\t\tSavefile'\
                        '\n------------------------------------------------------------------------')
                    for i in range(0, len(dataSaveList[1])):
                        print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                        saveFileID += 1
                    print(f" {saveFileID}\t-\t<new slot>")
                    print('------------------------------------------------------------------------\n')
                    
                    userInputOverwrite = input("Choose slot for saving:\t\t(0) Abort\n")
                    os.system('cls')
                    if userInputOverwrite == "0":
                        continue
                    elif userInputOverwrite == str(saveFileID):
                        
                        userInputFileName = input("\nName your slot:\t\t(0) Abort\n")
                        os.system('cls')                       
                        if userInputFileName != "0":    
                            with open(f'SaveFile_{userInputFileName}.pickle', 'wb') as manSaveHandler:
                                pickle.dump(dataSaveList, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
                                dataSaveList[1].append(userInputFileName)
                            with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                                pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                        
                            break
                        else:
                            print("Couldn't understand you?\n") 
                            continue
                    elif userInputOverwrite == "1":
                        print("You can't overwrite 'Autosave'!\n")
                    elif userInputOverwrite < str(saveFileID):
                        
                        userInputChoose = input("overwrite Slot? (1) Yes\t(2) No\n")
                        os.system('cls')
                        if userInputChoose == "1":
                            saveFileID = int(userInputOverwrite)                
                            
                            userInputFileName = input("\nName your slot:\t\t(0) Abort\n")
                            os.system('cls')
                            if userInputFileName != "0":    
                                with open(f'SaveFile_{userInputFileName}.pickle', 'wb') as manSaveHandler:
                                    pickle.dump(dataSaveList, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
                                    dataSaveList[1][saveFileID-1] = (userInputFileName)
                                with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                                    pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                        
                                break
                            else:
                                print("Couldn't understand you?\n") 
                                continue
                        elif userInputChoose == "2":
                            continue
                        else:
                            print("Couldn't understand you?\n") 
                            continue   
                    else:
                        print("Couldn't understand you?\n") 
                        continue   
            elif userInput == "2":
                saveFileID = 1
                print(' Nr.\t\tSavefile'\
                    '\n------------------------------------------------------------------------')
                for i in range(0, len(dataSaveList[1])):
                    print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                    saveFileID += 1
                print('------------------------------------------------------------------------\n')
                userInputDelete = input("\nChoose file to delete:\t\t(0) Abort\n")
                os.system('cls')
                if userInputDelete != "0":
                    dataSaveList[1][int(userInputDelete)-1]
                    break
                else:
                    print("Couldn't understand you?\n") 
                    continue  
            elif userInput == "0":
                break
            else:
                print("\nCouldn't understand you?\n")
                continue

    return dataSaveList


################################################################################## LOAD ##################################################################################
def Load(dataSaveList):
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
    while True: 
        saveFileID = 1
        print(' Nr.\t\tSavefile'\
            '\n------------------------------------------------------------------------')
        for i in range(0, len(dataSaveList[1])):
            print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
            saveFileID += 1
        print('------------------------------------------------------------------------\n')        
        userInputNumber = int(input("\nChoose number to load:\t\t(0) Abort\n"))
        os.system('cls')        
        if userInputNumber != "0":
            if userInputNumber > len(dataSaveList[1]):
                print("Selected slot is empty")
                continue

            with open(f'SaveFile_{dataSaveList[1][userInputNumber-1]}.pickle', 'rb') as loadHandler: 
                dataSaveList = pickle.load(loadHandler)
            with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
                dataSaveList[1] = pickle.load(loadAllHandler)
            break
        else:
            break
    
    return dataSaveList    

def LoadAutosave(dataSaveList):
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]

    saveFileID = 0 
    with open(f'SaveFile_Autosave.pickle', 'rb') as loadHandler: 
        dataSaveList = pickle.load(loadHandler)
    with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
        dataSaveList[1] = pickle.load(loadAllHandler)
    
    return dataSaveList             