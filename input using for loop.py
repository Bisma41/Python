n = int(input("enter the length of list:"))

num=[None] * n

for i in range(n):
    num[i] = input(f"Enter number {i+1}: ")

print("\nThe entered list is:")
print(num)
