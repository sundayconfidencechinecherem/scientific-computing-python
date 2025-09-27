users = {}
#sign up
print("Sign up to create account")
name = input("Enter your name: ")
email = input("Enter a valid email address: ")
password = input("Create a password")
users[email]={"name": name, "password": password}
print("Registration successful", name, "!")


#Reset password
print("Reset your password  ")
email = input("Enter the email you used for registration: ")
if email in users:
    new_password = input("Create a new password: ")
    confirm_new_password = input("Confirm your password: ")
    if len(new_password) < 6:
        print("password is too short!, it should be atleast 6 character long.") 
    elif new_password != confirm_new_password:
        print("Passwords did not match!")
    else:
        users[email]["password"] = new_password
        print("Password reset sucessfully")
else:
    print("Email not found!")

