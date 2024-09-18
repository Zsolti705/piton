""""
matek = int(input("Matek: "))
angol = int(input("Angol: "))
info = int(input("Info: "))
print((matek + angol + info) /3)
"""
""""
ido = int(input("Hány óra van?"))
kesobb = int(input("Hány óra múlva szóljon az ébresztő?"))
print(f"Az ébresztő ilyenkor fog megszólalni: {ido+kesobb}")
"""
"""
eur = float(input("Hány forint most egy euro? "))
print(f"Euro: {eur:.2f}")
valto = float(input("Hány euród van? "))
print(f"Összesen {eur*valto:.2f} forintod van.")
"""
"""
a = float(input("Hány dm a téglalap 'a' oldala?"))
b = float(input("Hány dm a téglalap 'b' oldala?"))
print(f"A téglalap kerülete: {((a+b)*2)*10:.2} centiméter.")
print(f"A téglalap területe: {(a*b)*100:.2} négyzetcentiméter.")
print(f"A téglalap kerülete: {((a+b)*2)/10:.2} méter")
print(f"A téglalap területe:{(a*b)/100:.2} négyzetméter.")
"""
"""
menny = float(input("Hány liter benzin van az üzemanyagtartályban? "))
fogy = float(input("Mennyi az autó átlagos fogyasztása? "))
print(f"Az autóval {(menny/100)*fogy:.2} kilómétert tudsz megtenni.")
"""
"""
r = float(input("Mennyi a kör sugara? "))
import math
x = math.pi
y = math.pow(r, 2)
print(f"A kör kerülete: {2*r*x:.2f}")
print(f"A kör területe: {y*x:.2f}")
print(f"A gömb felszíne: {4*x*y:.2f}")
print(f"A gömb térfogata: {(4*x/3)*r*r*r:.2f}")
"""
""""
a = 20
b = 25
print(f"A drót {((((a+b)*2)*0.9)-3)*1500} forintba kerül.")
"""
"""
d = float(input("Hány méter a hordó alapjának átmérője?"))
r = d/2
m = float(input("Hány méter magas a hordó?"))
lyuk = m-0.1
import math
pi = math.pi
print(f"A hordóba {(2*r*pi)*lyuk:.2} liter víz fér.")
"""
"""
db = int(input("Hány pár zoknit vásárolsz? "))
print(f"A zoknik ára: {db*250}Ft")
print(f"Akció esetén ez {db*250*.90}Ft-ba került volna.")
"""
""""
kolcson = int(input("Mekkora külcsönt szeretnél felvenni? "))
kamat = kolcson*1.20
print(f"Ez esetben a visszafizetendő ár {kamat}Ft lesz.")
"""
"""print("Hello world!")"""
"""
S = input("Add meg a neved:")
print(f"Üdvüzlöm {S}!")
"""
"""
x = int(input("Adj meg egy számot!"))
print(f"A szám kétszerese: {x*2}")
"""
"""
x = int(input("Adj meg egy számot!"))
y = int(input("Adj meg egy számot!"))
print(f"A számok összege: {x+y}")
print(f"A számok különbsége: {x-y}")
print(f"A számok szorzata: {x*y}")
print(f"A számok hányadosa: {x/y}")
"""
"""
x = int(input("Adj meg egy számot!"))
y = int(input("Adj meg egy számot!"))
print(f"A nagyobbik szám: {max(x, y)}")
"""
"""
x = int(input("Adj meg egy számot!"))
y = int(input("Adj meg egy számot!"))
z = int(input("Adj meg egy számot!"))
print(f"A kisebbik szám: {min(x, y, z)}")
"""
a = float(input("A háromszög a oldala"))
b = float(input("A háromszög b oldala"))
c = float(input("A háromszög c oldala"))
