#multiplication table 

print("\nMultiplication table generator")
number = int(input("\n Enter a number and see the multiplication table of that number from 1 to 50: "))
for iteration in range(1, 50):
    print(f"\n {number} x {iteration} = {number * iteration} ")