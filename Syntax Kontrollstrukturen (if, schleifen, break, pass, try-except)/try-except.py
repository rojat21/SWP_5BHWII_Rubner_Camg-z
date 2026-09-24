try:
    zahl1 = 10
    zahl2 = 0
    ergebnis = zahl1 / zahl2  # Erzeugt normalerweise einen ZeroDivisionError
    print(f"Ergebnis: {ergebnis}")
except ZeroDivisionError:
    print("Fehler: Du kannst nicht durch 0 teilen!")
else:
    print("Rechnung erfolgreich durchgeführt!")
