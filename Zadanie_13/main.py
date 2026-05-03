import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "studenci.json"


def dodaj_studenta(lista, imie, nazwisko):
    student = {
        "imie": imie,
        "nazwisko": nazwisko,
        "oceny": []
    }
    lista.append(student)
    print("Dodano studenta.")


def dodaj_ocene(lista, indeks, ocena):
    if indeks < 0 or indeks >= len(lista):
        print("Błąd: nieprawidłowy student.")
        return

    lista[indeks]["oceny"].append(ocena)
    print("Dodano ocenę.")


def wyswietl_studentow(lista):
    if len(lista) == 0:
        print("Brak studentów.")
        return

    for i, s in enumerate(lista, start=1):
        print(f"{i}. {s['imie']} {s['nazwisko']} | Oceny: {s['oceny']}")


def srednia(oceny):
    if len(oceny) == 0:
        return 0
    return sum(oceny) / len(oceny)


def statystyki(lista):
    if len(lista) == 0:
        print("Brak danych.")
        return

    for s in lista:
        sr = srednia(s["oceny"])
        print(f"{s['imie']} {s['nazwisko']} -> średnia: {sr:.2f}")


def znajdz_studenta(lista, nazwisko):
    for s in lista:
        if s["nazwisko"].lower() == nazwisko.lower():
            print(f"Znaleziono: {s['imie']} {s['nazwisko']}")
            print("Oceny:", s["oceny"])
            return
    print("Nie znaleziono studenta.")


def zapisz_plik(lista, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(lista, plik, indent=4, ensure_ascii=False)
    print("Zapisano dane.")


def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def main():
    lista = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== SYSTEM STUDENTÓW ===")
        print("1. Dodaj studenta")
        print("2. Lista studentów")
        print("3. Dodaj ocenę")
        print("4. Statystyki")
        print("5. Znajdź studenta")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            imie = input("Imię: ")
            nazwisko = input("Nazwisko: ")
            dodaj_studenta(lista, imie, nazwisko)

        elif wybor == "2":
            wyswietl_studentow(lista)

        elif wybor == "3":
            wyswietl_studentow(lista)

            try:
                indeks = int(input("Numer studenta: ")) - 1
                ocena = float(input("Podaj ocenę: "))
            except ValueError:
                print("Błąd: wpisz poprawne dane.")
                continue

            dodaj_ocene(lista, indeks, ocena)

        elif wybor == "4":
            statystyki(lista)

        elif wybor == "5":
            nazwisko = input("Podaj nazwisko: ")
            znajdz_studenta(lista, nazwisko)

        elif wybor == "0":
            zapisz_plik(lista, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()