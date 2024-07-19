import random
# from random import randint <- ez azt jelenti, hogy a random osztályBÓL (from) importáljuk a "randint" metódust.

# print("1. feladat")

print(f"Milyen műveletet szeretne gyakorolni? \n\n\t1. Összeadás \n\t2. Kivonás \n\t3. Szorzás")

# print("2. feladat")

valasz = int(input("\nVálasztás (1-3): ")) # "3" <- stringként menti el, és ezt kell intté (egész számmá alakítani.) Jegyezd meg: int(input())

# print("3. feladat")

# db = int(input("Hány műveletet szeretnél?: "))
db = 0 # <- ez alapvetően int, ha meg macskaköröm közé van ékelve, akkor alapvetően string. "0"
ok = 0

# print("4. feladat"), print("5. feladat")

# a feltételes ciklus mindig a while ciklus! - amíg, (amíg valami igaz, addig fusson, pl.: amíg i = 3, addig fusson, amint i nem 3, álljon le. Tehát a while ciklus majdnem olyan, mint a for ciklus, csak "break"-kel.)

while ok < 5:
    db += 1
    a = random.randint(1,10) # <- itt nem úgy van, mint a range-nél, hogy [x, y[, hanem itt így van: [x, y].
    b = random.randint(1, 10)

    if valasz == 1:
        d = (a + b)
        c = int(input(f"{a} + {b} = "))
    elif valasz == 2:
        d = (a - b)
        c = int(input(f"{a} - {b} = "))
    else:
        d = (a * b)
        c = int(input(f"{a} * {b} = "))

    if c == d:
        ok += 1
        print("Helyes! ")
    else:
        print("Hibás! ")

# print("6. feladat")

print(f"Gratulálunk!\nSikerült 5 helyes műveletet elvégezni {db} próbálkozásból. ", end="")

# átlag/százalékszámítás, kerekítés
# illetve felhasználó által megadott feladat kiírása pluszba
# válasz CSAK 1 és 3 közötti szám lehet
# 4. opció: OSZTÁS

print(f"{round((ok/db) * 100, 2)}%") # <- round = kerekítés