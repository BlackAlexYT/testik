t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    summa = 0
    for j in range(z-1):
        print(j, j)
        summa += j
    print(x*z-summa, y*z-summa)
