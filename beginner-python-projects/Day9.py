#NOTEPAD
#create note, save note and view notes
notes = []
print("Welcome to my unique note app")
while True:
    print("\n1 add note \n2 View note \n0 exit app")
    choice = input("Select: ")
    if choice == '1':
        note  = input("Write your notes here: ")
        notes.append(note)
        print("Your note has been saved!")
    elif choice == '2':
        print("\n Saved notes: ")
        for i, n in enumerate(notes, 1):
            print(f"{i}. {n}")
    elif choice == '0':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!, choose from the above lited options")
