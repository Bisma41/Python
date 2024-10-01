h = 9
y = 1
x = h // 3 + 2
print(' ' * x, '*')
for x in range(h // 3, 0, -1):
    print(' ' * x, '*', ' ' * y, '*')
    y += 2
print(' ', '*' * h)
