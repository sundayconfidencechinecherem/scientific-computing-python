#BMI Calculator

print("\n Hello and welcome to BMI Calculator")
print("\n I will help you confirm your weight, Let's start")
name = input("Enter your name: ")
while name == "":
    print("Name can't be empty")
    name = input("Enter your name: ")
while True:
    heights = float(input("Enter your height in meters(m): "))
    weights = float(input("Enter your weight in kilogram(kg): "))

    bmis = weights / (heights ** 2)
    print(f"Your BMI is: {bmis:.2f}")
    if bmis < 18.5:
        print("You're underweight ", name)
    elif bmis <= 24.9:
        print("you're normal ", name)
    elif bmis <= 29.9:
        print("you're overweight ", name)
    else:
        print("You're obesed, hit the gym!")
    break