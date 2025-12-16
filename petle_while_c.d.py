'''from time import sleep
from random import randint

#Zadanie 6.

wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) |x|
    akcja += 1 #akcja = akcja + 1
    print(f'Akcja {akcja}')
   #druzyna = int(input('Podaj nr drużyny, która wygrała akcję'))
    druzyna = randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(1)

if wynik1 > wynik2:
    print('Wygrała drużyna 1')
else:
    print('Wygrała drużyna 2')

#Zadanie 7.

liczba = int(input('Podaj liczbę: '))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

#Zadanie 8.

liczba = int(input('Podaj liczbę: '))
d = 2
ile_czyn = 0
while liczba > 1:
    while liczba % d == 0:
        liczba = liczba // d
        ile_czyn += 1
    d += 1
print(ile_czyn)