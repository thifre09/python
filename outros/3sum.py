n, target = map(int, input().split())
lista = list(map(int, input().split()))
a = ""
d = {}
for i, item in enumerate(lista):
    d[target-item] = i

p1 = 0
p2 = 1
shouldBreak = False
for i in range(len(lista)):
    p1 = i
    if (shouldBreak):
        break
    for j in range(i+1, len(lista)):
        if (shouldBreak):
            break
        p2 = j
        s = lista[p1] + lista[p2]
        if (s in d):
            if (p1 != d[s] and p2 != d[s]):
                temp = [d[s], p1, p2]
                temp.sort()
                a = f"{temp[0]+1} {temp[1]+1} {temp[2]+1}"
                shouldBreak = True
        
if (a != ""):
    print(a)
else:
    print("IMPOSSIBLE")