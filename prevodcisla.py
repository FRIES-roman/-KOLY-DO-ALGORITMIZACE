def secti_bin_cisla(bin1, bin2):
    return format(int(bin1, 2) + int(bin2, 2), 'b')

cislo1 = input("Zadej první binární číslo: ")
cislo2 = input("Zadej druhé binární číslo: ")

vysledek = secti_bin_cisla(cislo1, cislo2)
print("Součet v binární soustavě je:", vysledek)
