zahlen = [1, 2, 3, 4, 5, 6, 7]

for zahl in zahlen:
    if zahl == 4:
        print("Zahl 4 gefunden, Schleife wird abgebrochen!")
        break  # Verlässt die for-Schleife sofort
    print(f"Aktuelle Zahl: {zahl}") #das f im Print sorgt dafür das der Wert in der geschweiften Klammer {} nicht als "{zahl}" sondern als 5

    #Da jedes Element der Liste ein int ist, bekommt zahl bei jedem Durchlauf automatisch den Datentyp int