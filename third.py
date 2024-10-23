import math

def je_prvocislo(cislo):
    
    if cislo <= 1:
        return False
    
    deleni_limit = int(math.sqrt(cislo))
    for delitel in range(2, deleni_limit + 1):
        if cislo % delitel == 0:
            return False 
    
    return True

def vrat_prvocisla(maximum):
    
    prvocisla = []
    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla


if __name__ == "__main__":
    cislo = int(input("Zadej číslo do kterého program zjistí prvočísla: "))
    prvocisla = vrat_prvocisla(cislo)

    print(f"Prvočísla od 1 do {cislo}: {prvocisla}")