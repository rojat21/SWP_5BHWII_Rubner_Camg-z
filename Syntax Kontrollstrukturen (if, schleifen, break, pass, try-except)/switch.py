tag = "Samstag"

match tag:
    case "Montag" | "Dienstag" | "Mittwoch" | "Donnerstag" | "Freitag":
        print("Es ist ein Arbeitstag.")
    case "Samstag" | "Sonntag":
        print("Es ist Wochenende!")
    case _:    #_ bedeuetet alles andere was da reingeschrieben wird
        print("Ungültiger Wochentag.")