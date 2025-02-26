n = int(input("Zadej počet řádků: "))

for i in range(n):
    číslo = 1
    for j in range(i + 1):
        print(číslo, end=" ")
        číslo = číslo * (i - j) // (j + 1)
    print()
