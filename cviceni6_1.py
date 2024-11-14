import sys
import requests
import re

"""
Program stáhne obsah URL a vrátí všechny nadpisy:
<h1>Hlavní nadpis</h1>
<h2>Podnadpis</h2>
<h3>Podpodnadpis</h3>
<h4>Malý nadpis</h4>
<h5>Nejmenší nadpis</h5>
"""

def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Pokud je HTTP kód jiný než 200, vyvolá chybu
    except requests.exceptions.RequestException as e:
        print(f"Nastala chyba při připojování nebo stahování: {e}")
        return []
    
    # Získáme obsah HTML stránky jako text
    html = response.text
    
    # Regulární výraz pro vyhledání nadpisů h1 až h5
    nadpisy_h1_h5 = re.findall(r'<h([1-5])>(.*?)</h\1>', html)

    # Pro každý nalezený nadpis přidáme text do seznamu
    for _, nadpis in nadpisy_h1_h5:
        nadpisy.append(nadpis.strip())  # Odstraníme zbytečné mezery

    return nadpisy


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Prosím, zadejte URL jako argument.")
        sys.exit(1)
    
    url = sys.argv[1]
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    
    if nadpisy:
        print("Nalezené nadpisy:")
        for nadpis in nadpisy:
            print(nadpis)
    else:
        print("Nebyly nalezeny žádné nadpisy.")
