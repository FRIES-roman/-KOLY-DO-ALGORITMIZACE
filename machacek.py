import random
import time

# Globální proměnné
denni_rutina = [
    "vstává", "snídá", "pracuje na projektu", "programuje", "čte knihu", 
    "se učí nový jazyk", "venčí psa", "nakupuje", "cvičí", "hledá inspiraci",
    "dělá si kávu", "píše poznámky", "hraje deskovky", "sleduje seriály",
    "hledá nový problém k vyřešení", "dělá analýzu dat", "učí se chemii",
    "zapisuje své myšlenky", "přednáší o vědě", "relaxuje"
]

oblíbené_aktivity = ["programování", "věda", "chemie", "četba", "studium"]

# Funkce pro simulaci jedné aktivity
def simuluj_aktivitu(jmeno):
    aktivita = random.choice(denni_rutina)
    print(f"{jmeno} právě {aktivita}...")
    time.sleep(0.5)  # Simulace prodlevy
    return aktivita

# Funkce pro vyhodnocení dne
def vyhodnot_den(aktivity):
    oblibene = set(oblíbené_aktivity)
    zapocitane = len([a for a in aktivity if a.split()[0] in oblibene])
    print("\nDEN JE UKONČEN!")
    print(f"Dnes {len(aktivity)} aktivit: {', '.join(aktivity)}")
    print(f"Z toho {zapocitane} byly oblíbené. Dobrá práce, Macháčku!")

# Funkce pro simulaci dne
def simuluj_den(jmeno):
    aktivity_dne = []
    print(f"Simulace dne pro {jmeno} začíná...\n")
    for hodina in range(8, 22):  # Den od 8:00 do 22:00
        print(f"\nHodina: {hodina}:00")
        aktivita = simuluj_aktivitu(jmeno)
        aktivity_dne.append(aktivita)
    vyhodnot_den(aktivity_dne)

# Rozšíření: Macháček se učí nové dovednosti
def nauc_se_neco_noveho(jmeno):
    dovednosti = ["vaření", "hraní na kytaru", "psaní článků", "analýza dat"]
    nova_dovednost = random.choice(dovednosti)
    print(f"{jmeno} se rozhodl naučit {nova_dovednost}. Teď má nové zájmy!")
    oblíbene_aktivity.append(nova_dovednost)

# Hlavní program
def hlavni():
    jmeno = "Macháček"
    print(f"Vítejte v simulátoru života {jmeno}!\n")
    simuluj_den(jmeno)
    nauc_se_neco_noveho(jmeno)
    print(f"\n{jmeno} má nyní nové oblíbené aktivity: {', '.join(oblíbené_aktivity)}")

# Spuštění programu
if __name__ == "__main__":
    hlavni()