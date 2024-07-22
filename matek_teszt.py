# átlag/százalékszámítás, kerekítés
# illetve felhasználó által megadott feladatok kiírása pluszba
# válasz CSAK 1 és 3 közötti szám lehet -->  HIBA!! ha 1-nél kisebb vagy 4-nél nagyobb számot adunk meg hibára fut
import random

print(f"Milyen műveletet szeretnél gyakorolni? \n\n\t1. Összeadás \n\t2. Kivonás \n\t3. Szorzás \n\t4. Osztás")


valasz = int(input("\nVálasztás (1-4): "))


# db = int(input("Hány műveletet szeretnél?: "))
darab = 0
helyes = 0

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
        eredmeny = (szam_1 / szam_2)
        tipp = int(input(f"{szam_1} / {szam_2} = "))

    if valasz < 1:
        print("Adj meg egy nagyobb számot!")
        valasz = int(input("\nVálasztás (1-4): "))
    elif valasz > 4:
        print("Adj meg egy kisebb számot!")
        valasz = int(input("\nVálasztás (1-4): "))

    # if tipp == eredmeny:
    #     helyes += 1
    #     print("Helyes! ")
    # else:
    #     print("Hibás! ")

print(f"Gratulálunk!\nSikerült 5 helyes műveletet elvégezni {darab} próbálkozásból. ", end="")


print(f"{round((helyes/darab) * 100, 2)}%")
