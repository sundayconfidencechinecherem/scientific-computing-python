#dice rolling game
import random;

name = input("Enter your name ").strip()

print("welcome to Dice game")
print(f"\n you and the computer will play and who gets the hightest number wins ")
while name == "":
    print("Name cannot be empty! Please enter your name. ")
    name = input("Enter your name: ").strip()
while True:
    player1 = input("Press enter to roll a dice or (press 'q' to quit): ")
    if player1.lower() == 'q':
        print("It's sad to see you go, ", name, " Goodbye!")
        break
    player1_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    print(f"\n You rolled {player1_roll}")
    print(f"\n computer rolled {computer_roll}")

    if player1_roll > computer_roll:
            print(name, " You win this time")
    elif player1_roll < computer_roll:
            print(name, "you loose!,","Computer wins this time")
    else:
            print("Try again")

