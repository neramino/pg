jednotky = ["", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
jedenact_devatenact = ["", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

def cislo_text(cislo):
    if cislo == 0:
        return "nula"

    if cislo < 0:
        return "mínus " + cislo_text(-cislo)

    result = ""
    if cislo == 100:
        return "sto"

    if cislo >= 11 and cislo <= 19:
        result += jedenact_devatenact[cislo % 10] + " "
        cislo = 0
    elif cislo >= 10:
        result += desitky[cislo // 10] + " "
        cislo = cislo % 10

    if cislo > 0:
        result += jednotky[cislo] + " "

    return result.strip()

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)