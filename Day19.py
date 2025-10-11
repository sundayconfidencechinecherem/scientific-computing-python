#shopping list

print("Shopping List App")
shopping_list = []

while True:
    print("\n1. Add Item\n2. View List\n3. Remove Item\n0. Exit")
    choice = input("Select: ")

    if choice == '1':
        item = input("Enter item name: ")
        shopping_list.append(item)
        print(f"{item} added.")
    elif choice == '2':
        print("\n Your Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    elif choice == '3':
        num = int(input("Enter item number to remove: "))
        if 0 < num <= len(shopping_list):
            removed = shopping_list.pop(num - 1)
            print(f"{removed} removed.")
        else:
            print("Invalid number.")
    elif choice == '0':
        print("Thank you, and have a nice day!")
        break
    else:
        print("Invalid choice.")