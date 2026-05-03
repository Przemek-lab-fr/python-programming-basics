import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "oceny.json"

SKALA = (1, 2, 3, 4, 5, 6)
PROGI = (
    (5.0, "celujący"),
    (4.5, "bardzo dobry"),
    (3.5, "dobry"),
    (2.5, "dostateczny"),
    (1.5, "dopuszczający"),
    (0, "niedostateczny")
)


def dodaj_ocene(oceny, opis, ocena, data):
    if opis == "":
        print("Błąd: opis oceny nie może być pusty.")
        return

    if ocena not in SKALA:
        print("Błąd: ocena musi być w skali od 1 do 6.")
        return

    wpis = {
        "opis": opis,
        "ocena": ocena,
        "data": data
    }

    oceny.append(wpis)
    print("Dodano ocenę.")


def wyswietl_oceny(oceny):
    if len(oceny) == 0:
        print("Brak ocen.")
        return

    for wpis in oceny:
        print(
            f"Opis: {wpis['opis']}, "
            f"Ocena: {wpis['ocena']}, "
            f"Data: {wpis['data']}"
        )


def wyznacz_ocene_slowna(srednia):
    for prog, nazwa in PROGI:
        if srednia >= prog:
            return nazwa

    return "niedostateczny"


def statystyki(oceny):
    if len(oceny) == 0:
        print("Brak danych do statystyk.")
        return

    suma = 0

    for wpis in oceny:
        suma += wpis["ocena"]

    srednia = suma / len(oceny)
    ocena_slowna = wyznacz_ocene_slowna(srednia)

    oceny_liczbowe = []
    for wpis in oceny:
        oceny_liczbowe.append(wpis["ocena"])

    print(f"Średnia ocen: {srednia:.2f}")
    print(f"Ocena słowna: {ocena_slowna}")
    print(f"Najniższa ocena: {min(oceny_liczbowe)}")
    print(f"Najwyższa ocena: {max(oceny_liczbowe)}")


def zapisz_plik(oceny, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(oceny, plik, indent=4, ensure_ascii=False)
    print("Dane zapisane do pliku.")


def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def main():
    oceny = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== DZIENNIK OCEN ===")
        print("1. Dodaj ocenę")
        print("2. Lista ocen")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            opis = input("Podaj opis oceny: ")
            data = input("Podaj datę (YYYY-MM-DD): ")

            try:
                ocena = int(input("Podaj ocenę od 1 do 6: "))
            except ValueError:
                print("Błąd: wpisz liczbę całkowitą.")
                continue

            dodaj_ocene(oceny, opis, ocena, data)

        elif wybor == "2":
            wyswietl_oceny(oceny)

        elif wybor == "3":
            statystyki(oceny)

        elif wybor == "0":
            zapisz_plik(oceny, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()