print("Welcome to the pokemon quiz!")
playing = input("Do you want to play the game? ")
score = 0

if playing.lower() != "yes":
    print("Baibai o ^o")
    quit()

print("You wanna play? Let's play :)")

answer = input("What type is Charmander? ")
if answer.lower() == "fire":
    print("Correct!")
    score += 1
else:
    print("Incorrect...")

answer = input("What type is Balbasaur? ")
if answer.lower() == "grass":
    print("Correct!")
    score += 1
else:
    print("Incorrect...")

answer = input("What type is Squirtle? ")
if answer.lower() == "water":
    print("Correct!")
    score += 1
else:
    print("Incorrect...")

answer = input("What type is Pikachu? ")
if answer.lower() == "electric":
    print("Correct!")
    score += 1
else:
    print("Incorrect...")

print("You got: " + str(score) + "/4")