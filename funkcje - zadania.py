def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]

def iloczyn_v(u, v):
    wynik = 0
    for i in range(len(u)):
        wynik += u[i] * v[i]
    return wynik
u = [2, 7, 3]
v = [-1, 0, 4]
wynik = iloczyn_v(u, v)
print(wynik)