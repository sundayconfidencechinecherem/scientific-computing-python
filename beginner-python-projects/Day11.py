import random;

#dice rolling game

print(" Welcome to Dice Battle! 🎲")
print("You and the computer will roll a dice. Highest number wins!\n")

while True:
    play = input("Press Enter to roll (or type 'q' to quit): ")
    if play.lower() == 'q':
        print("Thanks for playing! 👋")
        break
    
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)
    
    print(f"\nYou rolled: {user_roll}")
    print(f"Computer rolled: {comp_roll}")
    
    if user_roll > comp_roll:
        print(" You WIN this round! \n")
    elif user_roll < comp_roll:
        print("💻 Computer wins this round! 💻\n")
    else:
        print("Get, better luck !\n")
