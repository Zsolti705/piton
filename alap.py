"""
import math
a = int(input("Szám: "))
print(f"{a} kétszerese: {a*2}")
print(f"{a} köbe: {math.pow(a,3):.2f}")
print(f"{a} négyzetgyöke: {math.sqrt(a):.2f}")
"""

"""
a = float(input("Tört: "))
b = float(input("Másik tört: "))
print(f"{a} és {b} törtek összege: {a+b:.2f}")
print(f"{a} és {b} törtek különbsége: {a-b:.2f}")
print(f"{a} és {b} törtek szorzata: {a*b:.2f}")
print(f"{a} és {b} törtek hányadosa: {a/b:.2f}")
"""
"""
a = int(input("Szám: "))
if a > 0 :
    print(f"pozitív")
elif  a==0:
    print("nulla")
else:
    print("negatív")
"""
"""
a = int(input("Szám: "))
b = int(input("Szám: "))
c = int(input("Szám: "))
if a+b>c and a+c>b and b+c>a:
    print("Szerkeszthető.")
else:
    print("Nem szerkeszthető.")
    """
"""
import math
a = int(input("Szám: "))
b = int(input("Szám: "))
c = int(input("Szám: "))
D = math.pow(b,2)-4*a*c
print(D)
if D>0:
    gyok=math.sqrt(D)
    x1=(-b+gyok)/2*a
    x2=(-b-gyok)/2*a
    print(x1)
    print(x2)
else:
    print("Negatív")
"""
""""
import math
alfa = int(input("Alfa: "))
r = int(input("Sugár: "))
T = alfa/360*math.pow(r,2)*math.pi
print(f"A terület{T:.2}")
K = alfa/360*2*r*math.pi
print(f"A kerület{K:.2}")
i = K - 2*r
print(f"A körcikk külső részének hossza{i:.2}")
"""
"""
a = int(input("Első szám: "))
b = int(input("Második szám: "))
c = int(input("Harmadik szám: "))
if c>a>b:
    print("Az első a legkisebb")
elif a>b>c:
    print("A második a legkisebb")
elif b>c>a:
    print("A harmadik a legkisebb.")
"""
"""
a = int(input("Első szám: "))
b = int(input("Második szám: "))
c = int(input("Harmadik szám: "))
if a>b>c:
    print("Az első a legnagyobb szám")
elif b>a>c:
    print("A haramdik a legnagyobb szám.")
elif c>b>a:
    print("Az első szám a legkisebb")    
"""
"""
x = int(input("Kérem a dolgozat pontszámát: "))
if x<50:
    print("A dolgozat elégtelen.")
elif 50<=x<=60:
    print("A dolgozat elégséges.")
elif 60<=x<70:
    print("A dolgozat közepes.")
elif 70<=x<=85:
    print("A dolgozat jó.")
elif 88<=x:
    print("A dolgozat jeles.")
"""
"""
x = int(input("Szám: "))
if x % 3==0 and x % 5 != 0:
    print("bizz")
elif x % 3!=0 and x % 5==0 :
    print("buzz")
elif x % 3==0 and x % 5==0:
    print("bizz-buzz")
elif x % 3 !=0 and x % 5 != 0 :
    print("A szám nem osztható ezekkel a számokkal.")
"""
"""
a = int(input("Első szám: "))
b = int(input("Második szám: "))
c = int(input("Harmadik szám: "))
if a+b==c or a+c==b or b+c== a:
    print("lehet") 
else:
    print("NEM lehet")
"""
a = int(input("Első szám: "))
b = int(input("Második szám: "))
c = int(input("Harmadik szám: "))



