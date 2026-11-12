import random

# 14 = Ass
Form = ['Kreuz', 'Pik', 'Herz', 'Karo']
Raenge = list(range(2, 15))

# 52 Karten
karten_stapel = []
for form in Form:
    for rang in Raenge:
        karten_stapel.append((form, rang))

# FUNKTIONEN FÜR DIE KOMBINATIONEN

def ist_royal_flush(hand):
    return ist_straight_flush(hand) and max([k[1] for k in hand]) == 14

def ist_straight_flush(hand):
    return ist_flush(hand) and ist_strasse([k[1] for k in hand])

def ist_poker(raenge):
    for rang in raenge:
        if raenge.count(rang) == 4:
            return True
    return False

def ist_full_house(raenge):
    return ist_drilling(raenge) and ist_paar(raenge)

def ist_flush(hand):
    farben = [k[0] for k in hand]
    return len(set(farben)) == 1

def ist_strasse(raenge):
    sortiert = sorted(list(set(raenge)))
    if len(sortiert) != 5:
        return False
    # Normale Straße (z.B. 5-6-7-8-9)
    if sortiert[4] - sortiert[0] == 4:
        return True
    # Sonderfall: Ass als 1 (A-2-3-4-5)
    if sortiert == [2, 3, 4, 5, 14]:
        return True
    return False

def ist_drilling(raenge):
    for rang in raenge:
        if raenge.count(rang) == 3:
            return True
    return False

def ist_zwei_paare(raenge):
    anzahl_paare = 0
    for rang in set(raenge):
        if raenge.count(rang) == 2:
            anzahl_paare += 1
    return anzahl_paare == 2

def ist_paar(raenge):
    for rang in raenge:
        if raenge.count(rang) == 2:
            return True
    return False


# SIMULATION (100.000 SPIELE)

ANZAHL_SPIELE = 100000

ergebnisse = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Poker (Vierling)": 0,
    "Full House": 0,
    "Flush": 0,
    "Straße": 0,
    "Drilling": 0,
    "Zwei Paare": 0,
    "Paar": 0,
    "High Card": 0
}

for _ in range(ANZAHL_SPIELE):
    hand = random.sample(karten_stapel, 5)
    raenge = [karte[1] for karte in hand]

    # Höchste Kombination zuerst prüfen
    if ist_royal_flush(hand):
        ergebnisse["Royal Flush"] += 1
    elif ist_straight_flush(hand):
        ergebnisse["Straight Flush"] += 1
    elif ist_poker(raenge):
        ergebnisse["Poker (Vierling)"] += 1
    elif ist_full_house(raenge):
        ergebnisse["Full House"] += 1
    elif ist_flush(hand):
        ergebnisse["Flush"] += 1
    elif ist_strasse(raenge):
        ergebnisse["Straße"] += 1
    elif ist_drilling(raenge):
        ergebnisse["Drilling"] += 1
    elif ist_zwei_paare(raenge):
        ergebnisse["Zwei Paare"] += 1
    elif ist_paar(raenge):
        ergebnisse["Paar"] += 1
    else:
        ergebnisse["High Card"] += 1


# AUSWERTUNG & WIKIPEDIA VERGLEICH

# Wikipedia Richtwerte in %
wiki_werte = {
    "Royal Flush": 0.000154,
    "Straight Flush": 0.00139,
    "Poker (Vierling)": 0.0240,
    "Full House": 0.1441,
    "Flush": 0.1965,
    "Straße": 0.3925,
    "Drilling": 2.1128,
    "Zwei Paare": 4.7539,
    "Paar": 42.2569,
    "High Card": 50.1177
}

print(f"\n--- ERGEBNISSE NACH {ANZAHL_SPIELE} SPIELEN ---")
print(f"{'Kombination':<18} | {'Absolut':<8} | {'Simuliert %':<12} | {'Wikipedia %':<12}")
print("-" * 58)

for kombi, anzahl in ergebnisse.items():
    prozent = (anzahl / ANZAHL_SPIELE) * 100
    wiki = wiki_werte[kombi]
    print(f"{kombi:<18} | {anzahl:<8} | {prozent:<11.4f}% | {wiki:<11.4f}%")