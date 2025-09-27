#login and sign up with criterias

#learning conditionals with user input
users = {}
name = input("Enter your name start: ")
age = int(input("Enter your age: "))


#additional logic with password validation

if age <18:
    print("sorry", name, "you're not of age")
else:
   
    email = input("Enter your email: ")
    password = input("Create a password: ")
    confirm_password = input("Confirm your password: ")
    
    #print
    # print("My name is ", name)
    # print("I am ", age)
    # print("My email is ", email)
    # print("My password is ", password)

    if len(password) <6:
        print("password is too short, password must not be less than 6 characters")
    elif password != confirm_password:
        print("password did not match!")
    else: 
        print("Congratulations", name, "registration successful")
    #login authentication 
    print("\n Please login to continue to login")
    login_email = input("Enter your email: ")
    login_password = input("Enter your password: ")
    if login_email == email and login_password == password:
        print("Welcome back ",name,", login successfully!")
    else:
        print("User not found")
    #limited attempt added
    #print("\n Continue to login")
    attempt = 3
    while attempt > 0:
        login_email == input("Enter your email: ")
        login_password == input("Enter your password: ")
        if login_email == email and login_password == password:
            print("Welcome back ", name, "you are logged in")
            break
        else:
            attempt -= 1
            if attempt > 0:
                print("Incorrect details ", name, "you have", attempt, "attempts left")
            else:
                print('Too many failed attempts, your account is locked')

#New registration section
print("Sign up again")
while True:
    name = input("Enter your name")
    age = int(input("Enter your age"))
    email = input("Enter your email")
    if email in users:
        print("Email already exist!, Try loggin instead")
        break
    password = input("Create a password: ")
    confirm_password = input("Confirm your password: ")
    if age <18:
        print("Sorry", name, "You are not of age")
    elif len(password) < 6:
        print("Password is too short, It must be aleast 6 character long")
    elif confirm_password != password:
        print("Password did not match, try again")
    else:
        users[email] = {"Name": name, "Email": email, "Age": age, "Password": password}
        print("Account created successfully", name)
# Login section
print("\n Welcome back login section final, please login misss")
while attempt > 0:
    login_email = input("Enter your email: ")
    login_password = input("Enter your password: ")
    
    if login_email in users and users[login_email]["Password"] == login_password:
        print("Welcome back,", users[login_email]["Name"], "You are fully logged in")
        break
    else:
        attempt -= 1
        if attempt > 0:
            print("Invalid email or password. You have", attempt, "attempts left")
        else:
            print("Too many failed attempts, you're locked out.")

