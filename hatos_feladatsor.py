"""
import random
lista = []
for i in range(12):
    lista.append(random.randint(-20, 20))
print(lista)
print(f"A napi hőingás: {max(lista)-min(lista)} °C.")
"""
"""
#2.	Írj programot, mely beolvas 10 pozitív egész számot, majd kiírja, hogy
import random
lista = []
for i in range(10):
    lista.append(random.randint(1,100))
paros = [x for x in lista if x % 2 == 0]
#a)	hány szám páros közülük?
print(len(paros))
#b)	mennyi a megadott számok összege?
print(sum(paros))
#c)	melyik a legnagyobb szám?
print(max(paros))
#d)	melyik a második legnagyobb szám?
lista.reverse()
print(lista[1])
"""
#3.	Egy túrázó elhatározza, hogy a nyár folyamán 100 km-t szeretne gyalogtúra formájában megtenni. Írj programot, mely beolvassa, hogy egy-egy nap hány km utat tett meg a túrázó, mindaddig, míg el nem éri, vagy meg nem haladja az addig megtett út összesen a 100 km-t. Ebben az esetben a program írja ki azt is, hogy hány nap alatt teljesítette a minimum 100 km-es gyalogtúrát! Példa a kimenetre!
"""
lista = []
osszeg = 0
while osszeg <= 100:
    ut = int(input("Mekkora utat tett meg?"))
    lista.append(ut)
    osszeg += ut
print('Gratulálok! Elérted a célt! Megtettél 100 km-t!')
tul = osszeg-100
print(f'{tul} km-rel túltelljesítetted.')
print(f'A túrát {len(lista)} nap alatt teljesítetted.')
#Melyik nap mennyit ment?
for index in range (len(lista)):
    print(f' {index + 1} napon - {lista[index]} km')
"""
# 4.	Írj programot, melyben a felhasználótól bekéred egy 10 fős osztály névsorát. A program számolja meg, hány olyan gyermek van, akinek 3 neve van! A program írja ki a leghosszabb nevű tanuló nevét is! Példa kimenet:

"""
nevek = []
for i in range(3):
    nev = input('Kérek egy nevet: ')
    nevek. append(nev)
print(nevek)
szokoz = 0
for nev in nevek:
    szokoz = 0
    for betu in nev:
        if betu == " ":
            szokoz += 1
    if szokoz == 2:
        print(nev)
nevhossz =  []
for nev in nevek:
    nevhossz.append(len(nev))
print(nevhossz)
leghoszabb = max(nevhossz)
for nev in nevek:
    if len(nev) == leghoszabb:
        print(nev)
"""
#5.	Egy váltó futóversenyen 5 fős csapatok indulnak, a versenyzők egymás után, egymást váltva futnak. A versenyzők maguk dönthetik el, hogy melyik csapattag hány km-t fut le, így kell megtenniük az 50 km-es távot. Készíts programot, mely beolvassa (ciklussal) az egyes versenyzők nevét, és azt, hogy hányadik km-ig futottak, majd a program írja ki, hogy melyik versenyző vállalta a legnagyobb távolságot a versenyen, és mekkora volt ez a távolság! Példa kimenet:
"""
nev = []
km = []
for i in range(5):
    km.append(int(input()))
    nev.append(input)
print(km)
print(nev)
leghosszabb = max(km)
sorszam = km.index(leghosszabb)
print(nev[sorszam])
print(leghosszabb)
"""












