rest = int(input())

notes = [100, 50, 20, 10, 5, 2, 1]

print(rest)
for n in notes:
    print("%d nota(s) de R$ %d,00" %(rest/n, n))
    rest = rest % n
    