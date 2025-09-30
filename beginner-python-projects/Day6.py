#Limited login attempt added muilti user 

#variables
users = {}

while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 18:
        print("Not of age!")
    else:
        email = input("Enter your email: ")
        if email in users:
            print("Email already exist!, Try loggin instead")
            continue
        else:
            password = input("Create a password: ")
            if len(password) < 6:
                print("Pasword is too short!, Atleast 6 character long")
                continue
            confirm_password = input("Confirm your password: ")
            if password != confirm_password:
                print("Password did not match!, Try again")
            else:
                users[email] = {"name": name, "age": age, "password": password }
                print("Registration successful", name)
                #login section
                print("\n Login Section")
                attempt = 3
                login_email = input("Enter your registered email: ")
                while attempt > 0:
                    if login_email not in users:
                        attempt -= 1
                        if attempt > 0:
                            print(f"Email not found, You have", attempt, " left. Try again")
                            login_email = input("Enter your email: ")
                        else:
                            print("Too many failed attempts!, Please Try creating a new account")
                        continue
                    password_attempt = 3
                    while password_attempt > 0:
                        login_password = input("Enter your password: ")
                        if login_password != users[login_email]["password"]:
                            password_attempt -= 1
                            if password_attempt > 0:
                                print("Wrong password, Please re-enter the correct password and you have", password_attempt, "remaining!")
                            else:
                                print("Too many failed attempts, your account is locked")
                        else:
                            print("Login successful", users[login_email]["name"])
                            password_attempt = 0
                            attempt = 0
                break
                    
                   

    
          