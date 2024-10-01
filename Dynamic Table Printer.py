num = int(input("Table of: "))
count = int(input("Enter the number of multiples you want: "))
print(f"\nMultiplication Table of {num} up to {count}:\n")
for x in range(1, count + 1):
    print(f"{num} x {x} = {num * x}")
