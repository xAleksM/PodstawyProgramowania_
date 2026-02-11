oceny = {'matematyka': 3, 'fizyka': 2, 'jezyk polski': 4}

#Klucze: 'matematyka', 'fizyka', 'jezyk polski'
#Wartości: 3, 2, 4

#1. Dostawanie się do wartośći pod danym kluczem
print(oceny['fizyka']) #Pobieramy wartość przypisaną do klucza 'fizyka', czyli 2

#2. Modyfikacja wartości pod danym kluczem
oceny['język polski'] = 5
print(oceny['jezyk polski'])

#3. Dodawanie klucza do słownika
oceny['geografia'] = 6
print(oceny)

#4. Sklejanie słownika z listy kluczy i listy wartośći
klucze = ['Bitwa pod Grunwaldem', 'Chrzest Polski', 'III Rozbiór Polski']
wartosci = [1410, 996, 1795]

'''for k, w in zip(klucze, wartosci):
    print(k, w)'''

zbior = {}
for i in range(len(klucze)):
    #print(klucze[i], wartosci[i])
    zbior[klucze[i]] = wartosci[i]

slownik2 = dict(zip(klucze, wartosci))

slownik3 = dict(janusz = 23, alojzy = 99, bornislawa = 67)
print(slownik3)

#5. Usuwanie klcza ze słwonika
del oceny['fizyka']
print(oceny)

#6. Chodzenie w pętli po słowniku:
for k in oceny:
    print(k, oceny[k])

for i in oceny.items():
    print(i)