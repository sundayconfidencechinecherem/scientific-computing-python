#Simple bank operation app


print("\n Welcome to confidence bank")
bank_balance = 0
while True:
    print("\n 1. Deposite \n 2. Withdraw \n 3. Check balance \n 0. Exit app")
    user_choice = input("Select from the options avaliable: ")
    if user_choice == '1':
        deposite_amount = float(input("Enter the amount you want to deposite: "))
        bank_balance += deposite_amount
        print(f"Your have successfully, deposited ₦{deposite_amount} into your account. Your new balance is ₦{bank_balance}")
    elif user_choice == '2':
        withdrawal_amount = float(input("Enter the amount you wish to withdraw: "))
        if withdrawal_amount > bank_balance:
            print("\n Insuffient balance!")
        else:
            bank_balance -= withdrawal_amount
            print(f"You have successfully withdrawn ₦{withdrawal_amount} and your new balance is ₦{bank_balance}")
    elif user_choice == '3':
        print(f"Your current bank balance is ₦ {bank_balance}")
    elif user_choice == '0':
        print("Thanks for banking with Us!")
        break
    else:
        print("\n Invalid option!")
