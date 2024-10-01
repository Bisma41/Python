# Sort the numbers using a series of comparisons and swaps
def sort_numbers(a, b, c, d):
  if a > b:
    a, b = b, a
  if b > c:
    b, c = c, b
  if c > d:
    c, d = d, c
  if a > b:
    a, b = b, a
  if b > c:
    b, c = c, b
  if c > d:
    c, d = d, c

  return a, b, c, d

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

sorted_numbers = sort_numbers(a, b, c, d)
print("Sorted numbers:", sorted_numbers)
