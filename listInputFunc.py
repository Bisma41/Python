def ListInput():
    n = int(input("enter the length of list: "))
    num = [None] * n
    for i in range(n):
        num[i] = input(f"Enter number {i+1}: ")
    return names

entered_numbers = ListInput()
print("\nThe entered numbers are:")
for number in entered_numbers:
    print(num)
