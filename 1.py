#Faktoriális számítás
"""
faktorialis = int(input("Faktoriális: "))
ertek = 1
while faktorialis != 0:
    ertek = ertek * faktorialis
    faktorialis -= 1
print(ertek)
"""
#N négyzetszám
"""
n = int(input("Szám: "))
for i in range(n):
    print(i*i)
"""
#Számtól kisebb páratlan számok összege
"""
n = int(input("Szám: "))
szam = 0
osszeg = 0
while szam < n:
    if szam %2 != 0:
        osszeg = osszeg + szam
    szam += 1
print(osszeg)
"""
#Számkitalálós játék
"""
import random
kitalalando = random.randint(1, 1000)
print(kitalalando)
szam = 0
lepes = 0
while szam != kitalalando:
    szam = int(input("Tipp: "))
    if szam < kitalalando:
        print("Tippelj nagyobbat")
    elif szam > kitalalando:
        print("Kisebbet tippelj")
    else:
        print("Eltaláltad!")
    lepes += 1
print(f"{lepes} Lélésből találtad el.")
"""
#Fibonacchi számoló
"""x
n = int(input("Szam: "))
szam1 = 0
szam2 = 1
osszeg = 0
print(szam1)
print(szam2)
for i in range(n):
    osszeg = szam1 +szam2
    print(osszeg)
    szam1 = szam2
    szam2 = osszeg
"""
#kukacigolvasó
"""
s = ""
while s != "@":
    s = input("Írj be valamit: ")
    if s == "@":
        print("Vége")
"""
#számstatisztika
"""
szam = 1
osszeg = 0
lepes = 0
atlag = 0
legtobb = 0
while szam != 0:
    szam = int(input("Szám: "))
    lepes += 1
    osszeg = osszeg + szam
    if legtobb < szam:
        legtobb = szam
    if szam == 0:
        print(f"A számok összege: {osszeg}")
        atlag = osszeg / (lepes-1)
        print(f"A számok átlaga: {atlag:.2f}")
        print(f"A legnagyobb szám: {legtobb}")
"""

#18. feladat A példa szerint
"""
n = int(input("Szám: "))
for i in range(n):
    xo = "XO"
    ox = "OX"
    for i in range(n):
        print(xo, end="")
    print("")
    for i in range(n):
        print(ox, end="")
    print("")
"""

"""
#17 feladat CSak a feladat szövege alapján:
n = int(input("Szám: "))
xo = "XO"
for i in range(n):
    print(xo, end="")
print("")
"""
#19
"""
import random
while True:
    dobas = random.randint(1, 6)
    s = input("Új dobás? ")
    if s != "y":
        break
    print(dobas)
"""
#8. feladat
"""
szam = -1
osszeg = 0
while osszeg < 5000:
    szam += 1
    osszeg = szam + osszeg
print(szam)
print(osszeg)
"""
#9
"""
szam = int(input("Osztandó: "))
print(f"{szam} osztói: ",end="")
for i in range(szam + 1):
    if i == 0 :
        continue
    if szam % i == 0:
        print(i, end=";")
"""
#10
"""
szam = int(input("Írj be egy pozitív egész számot: "))
osszeg = 0
for i in range(szam):
    if i == 0:
        continue
    if szam % i == 0:
        osszeg += i
if osszeg == szam:
    print("Tökéletes szám!")
else:
    print("Nem tökéletes szám!")
"""
#11
"""
szam = int(input("Írj be egy pozitív egész számot: "))
osztok = 0
for i in range(szam + 1):
    if i == 0:
        continue
    if szam % i == 0:
        osztok += 1
if osztok == 2:
    print("Prím.")
else:
    print("Nem prím.")
"""
"""
n = int(input("Szám: "))
osztok = 0
prim = 0
for szam in range(n):
    osztok = 0
    for i in range(szam + 1):
        if i == 0:
            continue
        if szam % i == 0:
            osztok += 1
    if osztok == 2:
        print(szam)
"""
#13
"""x
szam = 0
for i in range(99):
    szam += i
print(szam)
"""
"""
szam = 0
for i in range(6):
    szam *= i
print(szam)
"""
"""
szam = 0
for i in range(201):
    if i % 2 == 0:
        szam += i
print(szam)
"""
""""
szam = 0
for i in range(201):
    if i % 2 != 0:
        szam += i
print(szam)
"""