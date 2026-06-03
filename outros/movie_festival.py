n = int(input())
lista = []
for i in range(n):
    lista.append(list(map(int, input().split())))

lista.sort(key=lambda x: x[1])

proximo = lista[0][1]
total = 1
for lis in lista:
    if (lis[0] >= proximo):
        total += 1
        proximo = lis[1]
print(total)