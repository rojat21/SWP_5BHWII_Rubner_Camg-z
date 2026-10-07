import random

def lottoziehung():
    zahlen = list(range(1, 46))
    gezogen = [] #Leere Liste, hier werden die 6 Zahlen gespeichert, die gezogen werden
    
    for _ in range(6): #For-Schleife, die sich 6 mal wiederholt
  
        index = int(random.random() * len(zahlen)) #len(zahlen) wie viele Zahlen in der Liste sind, also z.B. nachdem man gezogen hat 44, 43 usw.
                                                    #random.random() gibt eine Zufallszahl zwischen 0 und 1 zurück, wird mit len multipliziert, und int schneidet die Nachkommastellen ab
        gezogen.append(zahlen.pop(index))           #pop(index) nimmt index raus und löscht sie aus der Liste und fügt sie der Ergebnisliste hinzu
        
    return gezogen

def statistik_inkrementieren(statistik_dict, ziehung):
    for zahl in ziehung:
        statistik_dict[zahl] += 1 #nimmt die gezogene Zahl und erhöht den Wert im Dictionary um 1, also sagt welche Zahl wie oft gezogen wurde

def lottostatistik(anzahl):
    statistik_dict = {i: 0 for i in range(1, 46)} 
    
    for _ in range(anzahl):
        ziehung = lottoziehung()
        statistik_inkrementieren(statistik_dict, ziehung) #schreibt die gezogenen Zahlen in das Dictionary, also wie oft jede Zahl gezogen wurde
        
    return statistik_dict

# 1. Einzelne Ziehung 
# Eine Ziehung durchführen
statistik_1_ziehung = lottostatistik(1)

# Aus dem Dictionary nur die 6 Zahlen heraussuchen, die eine 1 haben
gezogene_zahlen = [zahl for zahl, anzahl in statistik_1_ziehung.items() if anzahl == 1]

print("Gezogene Zahlen:", gezogene_zahlen)
print("Statistik dazu:", statistik_1_ziehung)


# 2. Statistik durchführen (1000, 10000, 100000 Ziehungen)
anzahl_ziehungen = 1000
ergebnis = lottostatistik(anzahl_ziehungen)
print(f"\nStatistik nach {anzahl_ziehungen} Ziehungen:\n", ergebnis)