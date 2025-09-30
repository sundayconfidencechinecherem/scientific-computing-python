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
    attempt = 3
    while attempt > 0:
        new_password = input("Create a new password: ")
        confirm_new_password = input("Confirm your password: ")
        if len(new_password) < 6:
            print("Password is too short!, It must be atleast 6 character long!")
        elif new_password != confirm_new_password:
            attempt -= 1
            if attempt > 0:
                print("Password does not match! you have ", attempt, "remaining")
            else:
                print("Too many failed attempts, Password reset failed.")
        else:
            users[email]["password"] = new_password
            print("Password reset, Successful")
            break
else:
    print("User not found!")
        

