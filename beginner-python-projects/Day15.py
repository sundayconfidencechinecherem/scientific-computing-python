#simple calculator app

print("\n Simple Calculator App")
print("\nLet's do some simple maths with our simple calculator app")
try:
    number1 = float(input("\nEnter the first number: "))
    operator_sign = input("Choose your operator sign. (+, -, *, /):")
    number2 = float(input("Enter the second number: "))
    if operator_sign == '+' :
        print(f"Your result is {number1 + number2}")
    elif operator_sign == '-':
        print(f" Your result is {number1 - number2}")
    elif operator_sign == '*':
        print(f"your result is {number1 * number2}")
    elif operator_sign == '/':
        print(f"your result is {number1 / number2}")
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Your result is {number1 / number2}")
    else:
        print("Invalid operator sign, try again")
except ValueError:
    print("Please enter a valid number!")

