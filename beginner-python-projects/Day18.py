#rock paper scissors game
import random

print(f"\n Rock, Paper & Scissor Game!")
choice_box = ["rock", "papper", "scissors"]
while True:
    human_choice = input("Enter rock, paper or scissors to get started or (press 'q' to quit): ").lower()
    if human_choice == 'q':
        print("It's sad to see you go, Thanks for playing with me!")
        break
    if human_choice not in choice_box :
        print("Invalid choice, Try again. ")
        continue
    computer_choice = random.choice(choice_box)
    print(f"\n Computer choose: {computer_choice}")
    if human_choice == computer_choice :
        print("It's draw draw! ")
    elif (human_choice == "rock" and computer_choice == "scissors") or \
         (human_choice == "paper" and computer_choice == "rock") or \
         (human_choice == "scissors" and computer_choice == "paper"):
         print("You Win!")
    else:
        print("\n you lose!")

