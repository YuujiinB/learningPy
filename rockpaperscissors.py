import random

userWins = 0
compWins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    userOption = input("Choose rock, paper or scissors. Q to quit. ").lower()
    if userOption == "q":
        break
    
    if userOption not in ["rock", "paper", "scissors"]:
        print("Enter a valid option")
        continue

    randomNumber = random.randint(0, 2)
    # rock = 0, paper = 1, scossors =2 
    compPicks = options[randomNumber]
    print("Computer picks:", compPicks + ".")

    if userOption == "rock" and compPicks == "scissors":
        print("You won!")
        userWins += 1
        continue

    elif userOption == "paper" and compPicks == "rock":
        print("You won!")
        userWins += 1
        continue

    elif userOption == "scissors" and compPicks == "paper":
        print("You won!")
        userWins += 1
        continue

    elif userOption == compPicks:
        print("Draw!")
        draws += 1

    else:
        print("You lost!")
        compWins += 1

totalGames = compWins + userWins + draws
if totalGames != 0:
    winPercent = (userWins/totalGames) * 100
    print("User have won", userWins, "times")
    print("Your win percentage:", winPercent + "%")
print("Baibai")