import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players: (1 - 4) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("There should be 2 - 4 players.")
    else:
        print("Enter valid input.")

max_score = 50
playerScores = [0 for i in range(players)]

while max(playerScores) < max_score:
    for player_idx in range(players):

        print("Player", str(player_idx + 1) + "'s turn")
        current_score = 0

        while True:
            wannaRoll = input("Do you want to roll? (y/n) ").lower()
            if wannaRoll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled:", value)
                print("Your score is:", current_score)

        playerScores[player_idx] += current_score
        print("You current score is:", playerScores[player_idx])

max_score = max(playerScores)
winningIndex = playerScores.index(max_score)
print("Player", winningIndex + 1, "is the winner with a score of:", max_score)