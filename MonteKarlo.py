import random

zakladna = 10
vyska = 5
pokusy = 10000
v_trojuhelniku = 0

for _ in range(pokusy):
    x = random.uniform(0, zakladna)
    y = random.uniform(0, vyska)

    if y <= (-vyska / zakladna) * x + vyska:
        v_trojuhelniku += 1

obsah_obdelniku = zakladna * vyska

odhad = (v_trojuhelniku / pokusy) * obsah_obdelniku

print(f"Odhadovaný obsah trojúhelníku je přibližně {odhad} cm²")
