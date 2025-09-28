#validation with user details

#variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))


#if conditional statement for sign up
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