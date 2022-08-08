def StatMenu(playerStatPoints, playerStats):
     # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    while True:
        print(f"\nPoints: {playerStatPoints}\n\n HP: {playerStats[2]}/{playerStats[1]}\nATK: {playerStats[3]}\nDEF: {playerStats[4]}")
        if playerStatPoints == 0:  
            userInput = input("\n(1) Return\n")
            if userInput == "1":
                break
            else: print("\nCouldn't understand you?!")
        else: 
            userInput = input(f"\n(1) Edit Stats ({playerStatPoints} P)\t(2) Return\n")
            if userInput == "1":
                playerStats, playerStatpoints = EditStats(playerStats, playerStatpoints)
            elif userInput == "2":
                return
            else: print("\nCouldn't understand you?!")
    return playerStatPoints, playerStats

def EditStats(playerStats, playerStatPoints):
     # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP
    while True:
        print(f"\nPoints: {playerStatPoints}\n\n HP: {playerStats[1]}\nATK: {playerStats[3]}\nDEF: {playerStats[4]}")
        userInput = input("\n(1) HP +10\t (2) Atk + 1\t (3) Def + 1\t (4) Return\n")
        match userInput:
            case "1": playerStats[1] += 10 ; playerStatPoints -= 1
            case "2": playerStats[3] += 1 ; playerStatPoints -= 1
            case "3": playerStats[4] += 1; playerStatPoints -= 1
            case "4": break
            case _: print("\nCouldn't understand you?!")
    return playerStats, playerStatPoints

def LevelUp(playerStats, playerStatPoints):
    # Playerstats = 0 Level, 1 MAX HP, 2 HP, 3 ATK, 4 DEF, 5 EXP

    if playerStats[5] == playerStats[0] * round((2**(playerStats[0]*0.6))):
        playerStats[0] += 1
        if playerStats[0] % 5 == 0:
            playerStatPoints += 4
        else:
            playerStatPoints += 2
        print("\nYay, Level Up!")
        
    return playerStats, playerStatPoints