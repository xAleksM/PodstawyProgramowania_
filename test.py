def f1(x, y):
    return x * y
def f2(f, a, b, n):
    return f(a, b) * n

print(f2(f1, 2, 3, 10))

def f(x):
    return 0.5 * x ** 2 - 3

print(f(6))

def Zw(f, D):
    wynik = []
    for x in D:
        y = f(x)
        wynik.append(y)
    return wynik

X = [-1, 0, 1]
Y = Zw(f, X)
print(Y)

def ile_liter(tekst):
    slownik = {}
    zbior = set(tekst)
    for x in tekst:
        ile = tekst.count(x)
        slownik[x] = ile
    return slownik
print(ile_liter('Litwo, Ojczyzno moja! ty jesteś jak zdrowie')