"""
import random
n = int(input('Hány elemű lista legyen? : '))
lista = []
for i in range(n):
    lista.append(random.randint(1,10))
print(lista)
paros = [x for x in lista if x% 2 == 0]
print(paros)
paratlan = [x for x in lista if x% 2 == 1]
print(paratlan)
"""
#1. Feltölt egy N elemű listát 1 és 100 közé eső véletlen számokkal. 
#2. Feltöltés után a lista elemeit a program írja ki a képernyőre!
#3. Írjuk ki a képernyőre a lista legkisebb elemét!
#4. Írjuk ki a képernyőre a lista legnagyobb elemét!
#5. Írjuk ki a képernyőre a lista elemeinek összegét!
#6. Írjuk ki a képernyőre a lista elemeinek átlagát!
#7. Van-e 50-es érték a listában?
#8. A program adja meg a listában szereplő páros számok közül a legnagyobb számértéket (ügyeljünk arra az esetre, mikor a listában minden szám páratlan)!
import random
lista = []
n = int(input('Hány számot generáljunk? '))
for i in range(n):
    rand = random.randint(1, 100)
    lista.append(rand)
print(lista)
print(min(lista))
print(max(lista))
print(sum(lista))
print(sum(lista)/n)
print('50' in lista)
#paros = [x for x in lista if x% 2 == 0]
#print(max(paros))
harommaloszhato = [x for x in lista if x % 3 == 0]
harommalnemoszhato = [x for x in lista if x % 3 != 0]
