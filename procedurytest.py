import random
import math


def aritmeticky_prumer(pole):
    return sum(pole) / len(pole)


def smerodajna_odchylka(pole, prumer):
    soucet = sum((x - prumer) ** 2 for x in pole)
    return math.sqrt(soucet / len(pole))


def pocet_vzdalenosti(pole, prumer, odchylka):
    pocet = sum(1 for x in pole if abs(x - prumer) <= odchylka)
    return pocet


def generuj_pole(délka):
    return [random.randint(1, 100) for _ in range(délka)]


delka_pole = 30
pole = generuj_pole(delka_pole)


prumer = aritmeticky_prumer(pole)
odchylka = smerodajna_odchylka(pole, prumer)


pocet = pocet_vzdalenosti(pole, prumer, odchylka)


procento = (pocet / delka_pole) * 100


print("Generované pole:")
print(pole)
print(f"Aritmetický průměr (AP): {prumer:.2f}")
print(f"Směrodatná odchylka: {odchylka:.2f}")
print(f"Počet prvků v odchylce: {pocet}")
print(f"Procento prvků v odchylce: {procento:.2f}%")
