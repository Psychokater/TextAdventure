import pickle
import os
from Colors import cl



#############################################################################################################################################################################
#-------------------------------------------------------------------------------- SAVE/LOAD --------------------------------------------------------------------------------#
#############################################################################################################################################################################



#################################################################################### SAVE ####################################################################################
def Save(dataSaveList):    
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]

####################################### AUTOSAVE    
    if dataSaveList[0] == 0:
        with open(f"SaveFile_Autosave.pickle", 'wb') as autoSaveHandler:
            pickle.dump(dataSaveList, autoSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
            if len(dataSaveList[1]) == 0:
                dataSaveList[1].append(f"Autosave --- {dataSaveList[2]} --- {dataSaveList[4]}")
            else:
                dataSaveList[1][0] = (f"Autosave --- {dataSaveList[2]} --- {dataSaveList[4]}")
        with open(f'Savepoint_Status.pickle', 'wb') as manSaveHandler:
            pickle.dump(dataSaveList[1], manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                                                                           #Add AutoSave to savePoints[0]        
####################################### MANUAL SAVE    
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
####################################### Choose Slot                    
                    userInputOverwrite = input("Choose slot for saving:\t\t(0) Abort\n")
                    os.system('cls')
                    if userInputOverwrite == "0":
                        continue
                    elif userInputOverwrite == str(saveFileID):
####################################### Name Slot -> Save                        
                        userInputFileName = input("\nName your slot:\t\t(0) Abort\n")
                        os.system('cls')                       
                        if userInputFileName != "0":    
                            with open(f'SaveFile_{saveFileID}.pickle', 'wb') as manSaveHandler:
                                pickle.dump(dataSaveList, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
                                dataSaveList[1].append(f"{userInputFileName} --- {dataSaveList[2]} --- {dataSaveList[4]}")
                            with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                                pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                        
                            break
                        else:
                            print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}") 
                            continue
                    elif userInputOverwrite == "1":
                        print(f"{cl.RED}You can't overwrite 'Autosave'!{cl.RESET}\n")
                        continue
                    elif userInputOverwrite < str(saveFileID):
####################################### Overwrite?                        
                        userInputChoose = input("overwrite Slot? (1) Yes\t(2) No\n")
                        os.system('cls')
                        if userInputChoose == "1":
                            saveFileID = int(userInputOverwrite)                
####################################### Name Slot -> Save                          
                            userInputFileName = input("\nName your slot:\t\t(0) Abort\n")
                            os.system('cls')
                            if userInputFileName != "0":    
                                with open(f'SaveFile_{saveFileID}.pickle', 'wb') as manSaveHandler:
                                    pickle.dump(dataSaveList, manSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)
                                    dataSaveList[1][saveFileID-1] = (f"{userInputFileName} --- {dataSaveList[2]} --- {dataSaveList[4]}")
                                with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                                    pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL)                        
                                break
                            else:
                                print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}") 
                                continue
                        elif userInputChoose == "2":
                            continue
                        else:
                            print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}") 
                            continue   
                    else:
                        print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}") 
                        continue 
####################################### Delete Slot 
            elif userInput == "2":
                saveFileID = 1
                print(' Nr.\t\tSavefile'\
                    '\n------------------------------------------------------------------------')
                for i in range(0, len(dataSaveList[1])):
                    print(f" {saveFileID}\t-\t{dataSaveList[1][i]}")
                    saveFileID += 1
                print('------------------------------------------------------------------------\n')
#######################################  Choose Slot to delete                
                userInputDelete = input("\nChoose file to delete:\t\t(0) Abort\n")
                os.system('cls')
                if userInputDelete == "1":
                        print(f"{cl.RED}You can't delete 'Autosave'!{cl.RESET}\n")
                        continue
                elif userInputDelete != "0":                 
                    dataSaveList[1].pop(int(userInputDelete)-1) 
                    os.remove(f'SaveFile_{int(userInputDelete)}.pickle')
                    with open('Savepoint_Status.pickle', 'wb') as allSaveHandler:
                        pickle.dump(dataSaveList[1], allSaveHandler, protocol=pickle.HIGHEST_PROTOCOL) 
                    break
                else:
                    print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}") 
                    continue  
            elif userInput == "0":
                break
            else:
                print(f"\n{cl.RED}Couldn't understand you?!{cl.RESET}")
                continue

    return dataSaveList


################################################################################## LOAD ##################################################################################
####################################### LOAD MANUAL #######################################  
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
####################################### Choose Slot to Load       
        userInputNumber = int(input("\nChoose number to load:\t\t(0) Abort\n"))
        os.system('cls')        
        if userInputNumber != "0":
            if userInputNumber > len(dataSaveList[1]):
                print(f"{cl.RED}Selected slot is empty{cl.RESET}")
                continue
####################################### Load File
            elif userInputNumber == "1":
                with open(f'SaveFile_Autosave.pickle', 'rb') as loadAutoHandler: 
                    dataSaveList = pickle.load(loadAutoHandler) 
            else:           
                with open(f'SaveFile_{userInputNumber}.pickle', 'rb') as loadHandler: 
                    dataSaveList = pickle.load(loadHandler)
            with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
                dataSaveList[1] = pickle.load(loadAllHandler)
            break       
    
    return dataSaveList    
####################################### LOAD AUTOSAVE #######################################  
def LoadAutosave(dataSaveList):
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]
####################################### Load File
    with open(f'SaveFile_Autosave.pickle', 'rb') as loadAutoHandler: 
        dataSaveList = pickle.load(loadAutoHandler)
    with open('Savepoint_Status.pickle', 'rb') as loadAllHandler:
        dataSaveList[1] = pickle.load(loadAllHandler)
    
    return dataSaveList             