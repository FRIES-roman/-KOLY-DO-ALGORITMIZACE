import random

# Počet bodů, které budeme generovat
pocet_bodu = 100000

# Strana čtverce (vypočítaná z úhlopříčky, která je rovna průměru kružnice)
strana_ctverce = 10 * (2 ** 0.5)

# Vrcholy trojúhelníku PQR
P = (0, 0)
Q = (strana_ctverce, 0)
R = (0, strana_ctverce)

# Funkce pro výpočet obsahu trojúhelníku
# Používáme vzorec pro výpočet obsahu trojúhelníku z vrcholů
# |(x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)) / 2|
def obsah_trojuhelniku(A, B, C):
    return abs((A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) / 2.0)

# Skutečný obsah trojúhelníku PQR (polovina obsahu čtverce)
skutecny_obsah = (strana_ctverce ** 2) / 4

def je_v_trojuhelniku(x, y):
    # Spočítáme součet obsahů tří menších trojúhelníků
    obsah1 = obsah_trojuhelniku((x, y), Q, R)
    obsah2 = obsah_trojuhelniku(P, (x, y), R)
    obsah3 = obsah_trojuhelniku(P, Q, (x, y))
    # Pokud součet odpovídá celkovému obsahu, bod je uvnitř
    return abs(obsah1 + obsah2 + obsah3 - skutecny_obsah) < 1e-6

# Počítadlo bodů uvnitř trojúhelníku
pocet_v_trojuhelniku = 0

# Generování náhodných bodů a kontrola, zda jsou uvnitř
for _ in range(pocet_bodu):
    x_nahodne = random.uniform(0, strana_ctverce)
    y_nahodne = random.uniform(0, strana_ctverce)
    if je_v_trojuhelniku(x_nahodne, y_nahodne):
        pocet_v_trojuhelniku += 1

# Odhad obsahu trojúhelníku podle Monte Carlo metody
odhadem_obsah = (pocet_v_trojuhelniku / pocet_bodu) * (strana_ctverce ** 2)

# Výsledek
print(f"Odhadnutý obsah trojúhelníku PQR: {odhadem_obsah:.2f} cm²")
