n = int(input("Enter a number: "))
for i in range(n, 1, -1):
    print('*' * i)
print('*' + ' ' * (1 * n - 2) + '*')
for i in range(2, n + 1):
    print('*' * i)
