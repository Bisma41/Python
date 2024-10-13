from random import *

# Length of the marks array
length = 30

# Initializing the marks array with random integers between 0 and 100
marks = [randint(0, 100) for _ in range(length)]
print("Marks: ", marks)

# Setting the sentinel value and initializing count
SEN = -1
count = 0

# Looping through the marks
for i in range(length):
    # Setting sentinel value if necessary
    if marks[i] == SEN:
        continue  # If the value is already SEN, skip

    for j in range(i + 1, length):
        if marks[j] == marks[i]:  # If a duplicate is found
            marks[j] = SEN  # Set it to the sentinel value
            count += 1  # Increase count

# Printing the final marks array
print("Updated Marks with sentinel values (SEN = -1):", marks)

# Check if count reaches 5
if count == 5:
    print("Count reached 5!")
else:
    print("Count did not reach 5. Total duplicates removed:", count)
