n = int(input())

for i in range(n):
    for k in range(n - i - 1):
        print(' ', end = '')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
for i in range(n - 1):
    for k in range(i + 1):
        print(' ',end ='')
    for j in range(2 * (n - 1)- 2 * i - 1):
        print('*', end='')
    print()
    
