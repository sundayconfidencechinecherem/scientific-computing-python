#if conditional statement with user details

#variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))


#if conditional statement
if age < 18:
    print("Your are not of age", name)
else:
    email = input("Enter your email: ")
    password = input("Create a password ")
    confirm_password = input("Confirm your password ")

#outputing result
    print("My name is ", name, "I am ", age, "years old.", "My email address is ", email, " And i just created my password successfully")