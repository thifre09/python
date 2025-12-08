import math
A = 3000
B = 5000
contador = 0
for i in range(A, B + 1):
    if (math.isqrt(i) ** 2 == i) and (math.ceil(i ** (1/3)) ** 3 == i):
        contador += 1

print(contador)