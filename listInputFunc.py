def ListInput():
    n = int(input("How many names do you want to enter? "))
    names = [None] * n
    for i in range(n):
        names[i] = input(f"Enter name {i+1}: ")
    return names

entered_names = ListInput()
print("\nThe entered names are:")
for name in entered_names:
    print(name)
