# átlag/százalékszámítás, kerekítés
# illetve felhasználó által megadott feladatok kiírása pluszba
# válasz CSAK 1 és 3 közötti szám lehet -->  HIBA!! ha 1-nél kisebb vagy 4-nél nagyobb számot adunk meg hibára fut
import random

print(f"Milyen műveletet szeretnél gyakorolni? \n\n\t1. Összeadás \n\t2. Kivonás \n\t3. Szorzás \n\t4. Osztás")


valasz = int(input("\nVálasztás (1-4): "))


# db = int(input("Hány műveletet szeretnél?: "))
db = 0
ok = 0

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
    elif valasz == 3:
        d = (a * b)
        c = int(input(f"{a} * {b} = "))
    elif valasz == 4:
        d = (a / b)
        c = int(input(f"{a} / {b} = "))
    else:
        print("Rossz számot adtál meg!")
        valasz = int(input("\nVálasztás (1-4): "))
    if c == d:
        ok += 1
        print("Helyes! ")
    else:
        print("Hibás! ")

print(f"Gratulálunk!\nSikerült 5 helyes műveletet elvégezni {db} próbálkozásból. ", end="")


print(f"{round((ok/db) * 100, 2)}%")
