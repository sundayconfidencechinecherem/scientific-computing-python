#learning conditionals with user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")

#print
print("My name is ", name)
print("I am ", age)
print("My email is ", email)

#additional logic

if age <18:
    print("sorry", name, "you're not of age")
else: print("Congratulations", name, "registration successful")