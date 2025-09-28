#authenticating registered users

#variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))


#conditional statement for sign up
if age < 18:
    print("Your are not of age", name)
else:
    email = input("Enter your email: ")
    password = input("Create a password ")
    confirm_password = input("Confirm your password ")
    if len(password) < 6:
        print("Password is too short!, It must be atleast 6 character long")
    elif password != confirm_password:
        print("Password does not match!")
    else:
        print("Registration successful", name)

#conditional statements for login
print("\n Continue to Login ")
login_email = input("Enter your email: ")
if login_email != email:
    print("Incorrect email")
else:
    login_password = input("Enter your password: ")
    if len(login_password) < 6:
     print("Password is too short!, It must be atleast 6 character long!")
    elif login_password != password:
     print("Incorrect password")
    elif login_email == email and login_password == password:
     print("Welcome back!", name, "Login successful")
    else:
     print("User Not Found!")