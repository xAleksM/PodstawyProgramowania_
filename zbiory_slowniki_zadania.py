# zbior = set()1

# lista2d = [
# [5, 2, 8, 5, 1],
# [3, 8, 2, 9, 5],
# [1, 4, 4, 2, 7],
# [6, 3, 9, 1, 4],
# [8, 2, 5, 6, 3]
# ]
#
# for x in range(len(lista2d)):
#     for y in range(len(lista2d[0])):
#         element = lista2d[x][y]
#         zbior.add(element)
#
# print(zbior)
#
# for x in lista2d:
#     zbior2 = set(x)
#     zbior_caly = zbior_caly.union(zbior2)
# print(zbior_caly)
#
slowa = [
"LETTER",
"BALLOON",
"SUCCESS",
"HAPPY",
"COFFEE",
"BOOKKEEPER",
"ASSESS",
"MISSISSIPPI",
"ADDRESS",
"TOOLBOX"
]

slowo = 'LETTER'
slowo_zbior = set(slowo)
print(len(slowo_zbior))

max_x = ''
max_l_r_l = 0
for x in slowa:
    x_zbior = set(x)
    l_r_l = len(x_zbior)
    if l_r_l > max_l_r_l:
        max_l_r_l = l_r_l
        max_x = x
print(max_x)

#sposób 2
max_slowo = max(slowo, key = lambda x:(len(set(x))))
print(max_slowo)

    #print(f'{x} {len(x_zbior)}')

#zadanie 2. 2
zbior = set()
for x in slowa:
    for y in x:
        zbior.add(y)

for l in sorted(zbior):
    lista = []
    for s in slowa:
        if l in s:
            lista.append(s)
    print(f'{l}: {lista}')