#Creating simple todo list
todos = []
print("Log your todos")
while True:
    print("\n 1. Add \n 2. View List \n 3. Checked \n 0. Exist")
    choice = input("Choose options: ")
    if choice == "1":
       task = input("Add your todos here: ")
       todos.append({"task": task, "done": False})
       print("Task added ")
    elif choice == "2":
        print("\n Your Todo list")
        for i, t in enumerate(todos, 1):
            status = "yes" if t["done"] else "no"
            print(f"{i}. {t['task']} [{status}]")
    elif choice == "3":
        num = int(input("Enter task number to mark as done: "))
        if 0 < num <= len(todos):
            todos[num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    elif choice == "0":
        break
    else:
        print("Invalid choice!")       
    