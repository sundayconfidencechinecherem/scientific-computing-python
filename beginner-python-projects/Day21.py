print(" Leap Year Checker")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"yes {year} is a Leap Year.")
else:
    print(f"no {year} is not a Leap Year.")