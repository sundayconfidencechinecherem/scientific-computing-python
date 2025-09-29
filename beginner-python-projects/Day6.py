#Multi user system and unique user system

#variables
users = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))


#conditional statement for sign up
if age < 18:
    print("Your are not of age", name)
else:
    email = input("Enter your email: ")
    if email in users:
        print("Email already exists! Try logging in instead.")
        # --- Login Section ---
        attempts = 3
        while attempts > 0:
            login_email = input("Enter your email: ")
            login_password = input("Enter your password: ")

            if login_email in users and login_password == users[login_email]["password"]:
                print("Welcome back,", users[login_email]["name"], "Login successful ✅")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Invalid details. You have", attempts, "attempts left.")
                else:
                    print("Too many failed attempts. Account locked ❌") 
    else:
        password = input("Create a password ")
        confirm_password = input("Confirm your password ")
        if len(password) < 6:
            print("Password is too short!, It must be atleast 6 character long")
        elif password != confirm_password:
            print("Password does not match!")
        else:
            users[email] = {"name": name, "password": password}
            print("Registration successful", name)

#conditional statements for login
    print("\n Continue to Login ")
    login_email = input("Enter your email: ")
    if login_email not in  users:
        print("Incorrect email")
    else:
        login_password = input("Enter your password: ")
        if len(login_password) < 6:
         print("Password is too short!, It must be atleast 6 character long!")
        elif login_password != users[login_email]["password"]:
         print("Incorrect password")
        else:
         print("Welcome back!", users[login_email]["name"], "Login successful")
    attempts = 2
    while attempts > 0:
        print("Try logging in again")
        login_email = input("Enter your email ")
        if login_email not in users:
            print("Incorrect email")
        else:
            login_password = input("Enter your password ")
            if len(login_password) < 6:
                print("Password is too short!, It must be atleast 6 character long!")
            elif login_password != users[login_email]["password"]:
                print("Incorrect password")
            attempts -= 1
            if attempts > 0:
                print("Incorrect details ", name, "you have", attempts, "attempts left")
            else:
                print('Too many failed attempts, your account is locked')
