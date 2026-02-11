zbior = set()1

lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]
]

for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)

print(zbior)

for x in lista2d:
    zbior2 = set(x)
    zbior_caly = zbior_caly.union(zbior2)
print(zbior_caly)
