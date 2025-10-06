#guess the number game
import random

print("\nHello and welcome to confidence world, Today we're going to play a guess the number game.")
name = input("\nPlease enter your name to get started: ")
while name.strip() == "":
    print("Name cannot be empty please provide your name to get started: ")
    name = input("\nPlease enter your name to get started: ")
print(name," Welcome to guessing number game: ")

secret_number = random.randint(1, 20)
attempt = 0
while True:
    attempt +=1
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret_number:
        print("Number is too low! Try again.")
    elif guess > secret_number:
        print("Number is too high!, Try again.")
    else:
        print("Congratulation", name, "You guessed right on", attempt, "attempts.")
        break