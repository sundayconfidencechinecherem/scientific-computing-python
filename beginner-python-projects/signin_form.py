#learning conditionals with user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))


#additional logic with password validation

if age <18:
    print("sorry", name, "you're not of age")
else:
   
    email = input("Enter your email: ")
    password = input("Create a password: ")
    confirm_password = input("Confirm your password: ")
    
    #print
    print("My name is ", name)
    print("I am ", age)
    print("My email is ", email)
    print("My password is ", password)

    if len(password) <6:
        print("password is too short, password must not be less than 6 characters")
    elif password != confirm_password:
        print("password did not match!")
    else: 
        print("Congratulations", name, "registration successful")