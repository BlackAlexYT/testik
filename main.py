import random
from random import randint

t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    summa1 = 0
    summa2 = 0
    for j in range(z - 1):
        a = random.randint(-1 * 10 ** 7, 1 * 10 ** 7)
        b = random.randint(-1 * 10 ** 7, 1 * 10 ** 7)
        summa1 += a
        summa2 += b
        print(a, b)
    print(x * z - summa1, y * z - summa2)
