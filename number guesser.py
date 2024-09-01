import random

# randrange is start to a hardcap of stop
# randint is start to stop
top = input("Type a number: ")

if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please enter a digit")
    quit()


randomNumber = random.randint(0, top)
tries = 0

while True:
    tries += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number vro")
        continue
    if guess == randomNumber:
            print("Correct!")
            print("It took you", str(tries), "tries")
            break
    elif guess > randomNumber:
            print("You were above the number")
    else:
            print("You are below the number")
         
