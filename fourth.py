def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    radek, sloupec = cilova_pozice
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

   
    if cilova_pozice in obsazene_pozice:
        return False
    
   
    typ_figurky = figurka["typ"]
    start_radek, start_sloupec = figurka["pozice"]

    
    if typ_figurky == "pěšec":
        if radek == start_radek + 1 and sloupec == start_sloupec:
            return True
        
        if start_radek == 1 and radek == start_radek + 1 and sloupec == start_sloupec:
            if (start_radek + 1, sloupec) not in obsazene_pozice:  # Kontrola, zda je pole před volné
                return True  

    
    elif typ_figurky == "jezdec":
        if (abs(radek - start_radek), abs(sloupec - start_sloupec)) in [(2, 1), (1, 2)]:
            return True  
    
   
    elif typ_figurky == "věž":
        if radek == start_radek or sloupec == start_sloupec:
            radek_smer = 1 if radek > start_radek else -1 if radek < start_radek else 0
            sloupec_smer = 1 if sloupec > start_sloupec else -1 if sloupec < start_sloupec else 0
            current_radek = start_radek + radek_smer
            current_sloupec = start_sloupec + sloupec_smer
            while (current_radek, current_sloupec) != (radek, sloupec):
                if (current_radek, current_sloupec) in obsazene_pozice:
                    return False
                current_radek += radek_smer
                current_sloupec += sloupec_smer
            return True

    
    elif typ_figurky == "střelec":
        if abs(radek - start_radek) == abs(sloupec - start_sloupec):
            radek_smer = 1 if radek > start_radek else -1
            sloupec_smer = 1 if sloupec > start_sloupec else -1
            current_radek = start_radek + radek_smer
            current_sloupec = start_sloupec + sloupec_smer
            while (current_radek, current_sloupec) != (radek, sloupec):
                if (current_radek, current_sloupec) in obsazene_pozice:
                    return False
                current_radek += radek_smer
                current_sloupec += sloupec_smer
            
            return True


    elif typ_figurky == "dáma":
        if radek == start_radek or sloupec == start_sloupec or abs(radek - start_radek) == abs(sloupec - start_sloupec):
            radek_smer = 1 if radek > start_radek else -1 if radek < start_radek else 0
            sloupec_smer = 1 if sloupec > start_sloupec else -1 if sloupec < start_sloupec else 0
            current_radek = start_radek + radek_smer
            current_sloupec = start_sloupec + sloupec_smer
            while (current_radek, current_sloupec) != (radek, sloupec):
                if (current_radek, current_sloupec) in obsazene_pozice:
                    return False
                current_radek += radek_smer
                current_sloupec += sloupec_smer
            return True

    # Král
    elif typ_figurky == "král":
        if max(abs(radek - start_radek), abs(sloupec - start_sloupec)) == 1:
            return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True