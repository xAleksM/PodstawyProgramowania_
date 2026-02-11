from ipaddress import summarize_address_range

zbior = {5,6,6,1,1,5,9}
print(zbior)

zbior2 = {'kot', 'pies', 'gołąb', 'kot', 'pies' }
print(len(zbior2))

A = set(range(0, 20, 2)) #{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
B = {1, 2, 3, 4, 6, 12}

#Suma zbiorów
suma_A_B = A.union(B)
print(suma_A_B)

suma_A_B2 = set(list(A) + list(B))
print(suma_A_B2)

#Część wspólna
iloczyn_A_B = A.intersection(B)
print(iloczyn_A_B)

#różnica
roznica_A_B = A.difference(B)
print(roznica_A_B)

#Dodawamie elementu do zbioru:
C = {1, 7, 4, 5}
C.add(2)
print(C)