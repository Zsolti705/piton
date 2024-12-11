import random
rand = random.randint(1, 1000)
lista = [random.randint(1, 1000), random.randint(1, 1000),random.randint(1, 1000),random.randint(1, 1000), random.randint(1, 1000) ,random.randint(1, 1000),random.randint(1, 1000),random.randint(1, 1000),random.randint(1, 1000),random.randint(1, 1000),]
print(lista)
#ötödik hely 50
lista[4] = 50 
print(f"A lista 5-dik eleme 50: {lista}")
#hány listaelem van
print('A lista hossza: ')
print(len(lista))
#hanyadik elem az 50
print(lista.index(50))
#hányszor van 50
print(lista.count(50))
#50 törlése
lista.remove(50)
#fordított sorrend
lista.sort(reverse=True)
print(lista)
#2-8-ig minden 2. elem
print(lista[1:8])
#7-3ig
print(lista[-3:2:])
#elemek összege
ossz = sum(lista)
print(ossz)
#atlag
atlag = ossz/9
print(atlag)
#azonos 
#kétjegyű számok száma
#egyjegyű számok négyzetei
#hárommal oszthahóak összege
oszthato = [x for x in lista if x %3 == 0]
harmasoszto = sum(oszthato)
print(harmasoszto)
#nullára végződő szám
#van-e 500
