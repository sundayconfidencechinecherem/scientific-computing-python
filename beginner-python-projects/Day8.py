#Expenses tracker
expenses = []

print("Store your expenses")
while True:
    amount = input("Enter your expense amount:  or exist ('q' to 'quite'): ")
    if amount.lower() == 'q':
        break
    try:
        amount = float(amount)
        desc = input("Enter expenses description: ")
        expenses.append({"amount": amount, "desc": desc})
        print("your ", desc, "expenses added.")
        choice = input("('y' for 'yes' and 'n' for 'no'): ")
        if choice == 'y' :
            break
    except ValueError:
            print("Invalid amount, Try again")





