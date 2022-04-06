# import random so that the PC can pick a random weapon
import random

# add win counter to track pc and user wins for victory
userWinCounter = 0
pcWinCounter = 0

while True:
    # Prompt user to pick a weapon
    userInput = input("Pick your weapon (Rock, Paper, or Scissors)")

    # Have PC pick a random weapon
    weapons = ["rock", "paper", "scissors"]
    pcChoice = random.choice(weapons)

    # Print user and PC choices
    print("You chose", userInput)
    print("computer chose", pcChoice)

    # Compare PC and User choices and decide how to return that info
    # Step one check if its a tie now so I dont have to later, if tied then skip to end and restart
    if userInput == pcChoice:
        print("It's a tie, no one wins, Try again")
    # step 2 is to check each case against the only 2 other options to see who wins
    elif userInput == "rock":
        if pcChoice == "scissors":
            print("Rock beats scissors, you win")
            userWinCounter += 1
        else:
            print("Paper beats rock, you lose")
            pcWinCounter += 1
    elif userInput == "paper":
        if pcChoice == "rock":
            print("Paper beats rock, you win")
            userWinCounter += 1
        else:
            print("Scissors beats paper, you lose")
            pcWinCounter += 1
    elif userInput == "scissors":
        if pcChoice == "paper":
            print("Scissors beats paper, you win")
            userWinCounter += 1
        else:
            print("Rock beats scissors, you lose")
            pcWinCounter += 1

    print(userWinCounter)
