import json
from pathlib import Path

# plik zapisuje się zawsze obok main.py
FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "biblioteczka_ksiazek.json"

STATUSY = ["do przeczytania", "czytam", "przeczytana"]


def zapisz_plik(kolekcja, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(kolekcja, plik, indent=4, ensure_ascii=False)
    print("Dane zapisane do pliku.")


def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def dodaj_ksiazke(kolekcja):
    tytul = input("Podaj tytuł: ")
    autor = input("Podaj autora: ")
    gatunek = input("Podaj gatunek: ")
    status = input(f"Podaj status {STATUSY}: ")

    if status not in STATUSY:
        print("Błąd: nieprawidłowy status.")
        return

    ksiazka = {
        "tytul": tytul,
        "autor": autor,
        "gatunek": gatunek,
        "status": status
    }

    kolekcja.append(ksiazka)
    print("Dodano książkę.")


def lista_ksiazek(kolekcja):
    if not kolekcja:
        print("Brak książek w biblioteczce.")
        return

    print("\n=== LISTA KSIĄŻEK ===")
    for i, k in enumerate(kolekcja, 1):
        print(f"{i}. {k['tytul']} | {k['autor']} | {k['gatunek']} | {k['status']}")


def statystyki(kolekcja):
    if not kolekcja:
        print("Brak danych do statystyk.")
        return

    print("\n=== STATYSTYKI ===")
    for status in STATUSY:
        liczba = sum(1 for k in kolekcja if k["status"] == status)
        print(f"{status}: {liczba}")


def main():
    kolekcja = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== MOJA BIBLIOTECZKA ===")
        print("1. Dodaj książkę")
        print("2. Lista książek")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_ksiazke(kolekcja)

        elif wybor == "2":
            lista_ksiazek(kolekcja)

        elif wybor == "3":
            statystyki(kolekcja)

        elif wybor == "0":
            zapisz_plik(kolekcja, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()