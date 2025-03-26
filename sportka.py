import random


def losovani_cisel():
    cisla = random.sample(range(1, 50), 7)  
    return cisla[:6], cisla[6]  


def ziskej_cisla(use_generated=True):
    if use_generated:
        return random.sample(range(1, 50), 6) 
    else:
        uzivatelova_cisla = []
        print("Zadejte 6 různých čísel mezi 1 a 49:")
        while len(uzivatelova_cisla) < 6:
            try
               
                cislo = int(input(f"Číslo {len(uzivatelova_cisla) + 1}: "))
                if cislo < 1 or cislo > 49:
                    print("Číslo musí být mezi 1 a 49.")
                elif cislo in uzivatelova_cisla:
                    print("Toto číslo už jste zadali, zvolte jiné.")
                else:
                    uzivatelova_cisla.append(cislo)  
                print("To není platné číslo! Zadejte celé číslo.")
        return uzivatelova_cisla


def porovnej_cisla(uzivatelova_cisla, losovana_cisla, bonusove_cislo):
    shody = set(uzivatelova_cisla) & set(losovana_cisla) 
    bonusova_shoda = len(shody) == 5 and bonusove_cislo in uzivatelova_cisla 


losovana_cisla, bonusove_cislo = losovani_cisel()


uzivatelova_cisla = ziskej_cisla(use_generated=True)

losovane_vysledky = sorted(losovana_cisla)
uzivatelova_vysledky = sorted(uzivatelova_cisla)


print("\nLosovaná čísla:", losovane_vysledky)
print("Bonusové číslo:", bonusove_cislo)
print("Vaše čísla:", uzivatelova_vysledky)


shody, bonusova_shoda = porovnej_cisla(uzivatelova_cisla, losovana_cisla, bonusove_cislo)
print(f"Počet shod: {len(shody)}")
print("Shodná čísla:", sorted(shody))


if bonusova_shoda:
    print("Uhodli jste 5 čísel a bonusové číslo!")