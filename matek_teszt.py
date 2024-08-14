# átlag/százalékszámítás, kerekítés
# illetve felhasználó által megadott feladatok kiírása pluszba
import random

print(f"Milyen műveletet szeretnél gyakorolni? \n\n\t1. Összeadás \n\t2. Kivonás \n\t3. Szorzás \n\t4. Osztás")


valasz = int(input("\nVálasztás (1-4): "))


# db = int(input("Hány műveletet szeretnél?: "))
darab = 0
helyes = 0

while valasz < 1 or valasz > 4:
    if valasz < 1:
        print("Adj meg egy nagyobb számot!")
        valasz = int(input("\nVálasztás (1-4): "))
    elif valasz > 4:
        print("Adj meg egy kisebb számot!")
        valasz = int(input("\nVálasztás (1-4): "))

while helyes < 5:
    darab += 1
    szam_1 = random.randint(1, 10)  # <- itt nem úgy van, mint a range-nél, hogy [x, y[, hanem itt így van: [x, y].
    szam_2 = random.randint(1, 10)

    if valasz == 1:
        eredmeny = (szam_1 + szam_2)
        tipp = int(input(f"{szam_1} + {szam_2} = "))
    elif valasz == 2:
        eredmeny = (szam_1 - szam_2)
        tipp = int(input(f"{szam_1} - {szam_2} = "))
    elif valasz == 3:
        eredmeny = (szam_1 * szam_2)
        tipp = int(input(f"{szam_1} * {szam_2} = "))
    elif valasz == 4:
        eredmeny = (round(szam_1 % szam_2, 1)) # Ez így rendben van, mert "/" -> ez a sima osztás, round-dal kerekíthetsz és megadhatod, hogy hány tizedesjegyig, "//" -> ez pedig az egész osztás. Ezt nevezzük DEV-nek. Van még "%", ez a maradékos osztás, MOD-nak nevezzük.
        tipp = float(input(f"{szam_1} / {szam_2} = "))

    if tipp == eredmeny:
        helyes += 1
        print("Helyes! ")
    else:
        print("Hibás! ")

print(f"Gratulálunk!\nSikerült 5 helyes műveletet elvégezni {darab} próbálkozásból. ", end="")


print(f"{round((helyes/darab) * 100, 2)}%")
