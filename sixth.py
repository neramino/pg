import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    try:
        # Stažení obsahu stránky
        response = requests.get(url)
        response.raise_for_status()  # Zkontroluje status kód, vyvolá výjimku pro kód != 200

        # Dekódování obsahu stránky
        content = response.text

        # Regulární výraz pro extrakci odkazů
        href_pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]+)"'
        hrefs = re.findall(href_pattern, content)

        return hrefs

    except requests.RequestException as e:
        raise RuntimeError(f"Chyba při stahování URL: {e}")
    except Exception as e:
        raise RuntimeError(f"Obecná chyba: {e}")


if __name__ == "__main__":
    try:
        # Ověření, zda uživatel zadal URL jako argument
        if len(sys.argv) < 2:
            raise ValueError("Musíte zadat URL jako argument příkazového řádku.")

        url = sys.argv[1]
        # Zavolání funkce a vypsání nalezených odkazů
        hrefs = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for href in hrefs:
            print(href)

    except Exception as e:
        print(f"Program skončil chybou: {e}")
