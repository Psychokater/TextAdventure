import os
import Intro
import Helpfile
import SaveLoad



#############################################################################################################################################################################
#-------------------------------------------------------------------------------- MAIN MENU --------------------------------------------------------------------------------#
#############################################################################################################################################################################



################################################################################## MAIN MENU #################################################################################
### MainMENU: START/EXIT
def MainMenu(dataSaveList, newGame):
    load = False
    Intro.Intro() 
    dataSaveList[0] = 0
    dataSaveList = SaveLoad.Save(dataSaveList)
    dataSaveList[0] = 1 
    #dataSaveList = [0 autoSave, 1 savePoints, 2 playerName, 3 startLocation, 4 location, 5 playerInventoryMoney, 6 playerStatPoints, 7 playerStats, 8 itemsDict]      
    while True:
        if dataSaveList[2] == "" and len(dataSaveList[1]) <= 1:
            userInput = input('\n(1) New Game\t(2) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": newGame = True; break                               
                case "2": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        elif dataSaveList[2] == "" and len(dataSaveList[1]) > 1:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Load\t(4) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": newGame = True; break   
                case "2": SaveLoad.LoadAutosave(dataSaveList); break
                case "3": dataSaveList = SaveLoad.Load(dataSaveList); load = True; break                                        
                case "4": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")
        
        elif dataSaveList[2] != "" and len(dataSaveList[1]) == 1:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Save\t(4) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": newGame = True; break     
                case "2": dataSaveList = SaveLoad.LoadAutosave(dataSaveList); break
                case "3": dataSaveList = SaveLoad.Save(dataSaveList); break       
                case "4": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye")
                case _: print("\nCouldn't understand you?!")

        else:
            userInput = input('\n(1) New Game\t(2) Continue\t(3) Save\t(4) Load\t(5) Help\t(0) Exit Game\n')
            os.system('cls')
            match userInput:
                case "1": newGame = True; break       
                case "2": SaveLoad.LoadAutosave(dataSaveList); break
                case "3": dataSaveList = SaveLoad.Save(dataSaveList); break                        
                case "4": dataSaveList = SaveLoad.Load(dataSaveList); load = True; break
                case "5": Helpfile.HelpTxt()
                case "0": exit(f"\nGoodbye {dataSaveList[2]}")
                case _: print("\nCouldn't understand you?!")
        # sleep(2)
        dataSaveList[0] = 1
    return dataSaveList, newGame, load       