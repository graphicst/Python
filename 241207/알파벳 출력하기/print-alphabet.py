n = int(input())
asc = 65
for i in range(n):
    for j in range(i+1):
        print(chr(asc), end='')
        asc += 1
        if asc > 90:
            asc = 65
    print()
