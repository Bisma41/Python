number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
operation = input('enter the operator:')

if operation == '+':
    print("Sum is:",number_1 + number_2)

elif operation == '-':
    print("Difference is:",number_1 - number_2)

elif operation == '*':
    print("Multiplication is:",number_1 * number_2)

elif operation == '/':
    print("Division is:",number_1 % number_2)

else:
    print('You have not typed a valid operator, please run the program again.')
