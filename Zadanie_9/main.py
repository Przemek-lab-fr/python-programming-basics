import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "rekordy_osobiste.json"

DYSCYPLINY = ("bieg 5 km", "bieg 10 km", "pompki", "podciąganie", "plank", "rower 20 km")


def czy_rekord(wyniki, dyscyplina, wynik):
    # dla biegów (czas) rekord = najmniejszy
    if "bieg" in dyscyplina:
        najlepszy = None
        for w in wyniki:
            if w["dyscyplina"] == dyscyplina:
                if najlepszy is None or w["wynik"] < najlepszy:
                    najlepszy = w["wynik"]

        return najlepszy is None or wynik < najlepszy

    # dla reszty rekord = największy
    else:
        najlepszy = None
        for w in wyniki:
            if w["dyscyplina"] == dyscyplina:
                if najlepszy is None or w["wynik"] > najlepszy:
                    najlepszy = w["wynik"]

        return najlepszy is None or wynik > najlepszy


def dodaj_wynik(wyniki, data, dyscyplina, wynik):
    if dyscyplina not in DYSCYPLINY:
        print("Błąd: nieprawidłowa dyscyplina.")
        print(f"Dostępne: {DYSCYPLINY}")
        return

    if wynik <= 0:
        print("Błąd: wynik musi być > 0.")
        return

    rekord = czy_rekord(wyniki, dyscyplina, wynik)

    wpis = {
        "data": data,
        "dyscyplina": dyscyplina,
        "wynik": wynik,
        "jednostka": "min" if "bieg" in dyscyplina else "ilość",
        "rekord": rekord
    }

    wyniki.append(wpis)

    if rekord:
        print("🔥 Nowy rekord!")
    else:
        print("Dodano wynik.")


def wyswietl_wyniki(wyniki, dyscyplina=None):
    if len(wyniki) == 0:
        print("Brak wyników.")
        return

    for w in wyniki:
        if dyscyplina and w["dyscyplina"] != dyscyplina:
            continue

        znak = "[REKORD]" if w["rekord"] else ""

        print(
            f"{w['data']} | {w['dyscyplina']} | {w['wynik']} {w['jednostka']} {znak}"
        )


def aktualne_rekordy(wyniki):
    if len(wyniki) == 0:
        print("Brak danych.")
        return

    rekordy = {}

    for w in wyniki:
        d = w["dyscyplina"]

        if d not in rekordy:
            rekordy[d] = w
        else:
            if "bieg" in d:
                if w["wynik"] < rekordy[d]["wynik"]:
                    rekordy[d] = w
            else:
                if w["wynik"] > rekordy[d]["wynik"]:
                    rekordy[d] = w

    for d, w in rekordy.items():
        print(f"{d}: {w['wynik']} ({w['data']})")


def zapisz_plik(wyniki, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(wyniki, plik, indent=4, ensure_ascii=False)
    print("Zapisano dane.")


def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except:
        return []


def main():
    wyniki = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== MOJE REKORDY ===")
        print("1. Dodaj wynik")
        print("2. Lista wyników")
        print("3. Aktualne rekordy")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            data = input("Podaj datę: ")

            print(f"Dostępne dyscypliny: {DYSCYPLINY}")
            dyscyplina = input("Podaj dyscyplinę: ")

            try:
                wynik = float(input("Podaj wynik: "))
            except:
                print("Błąd: wpisz liczbę.")
                continue

            dodaj_wynik(wyniki, data, dyscyplina, wynik)

        elif wybor == "2":
            wyswietl_wyniki(wyniki)

        elif wybor == "3":
            aktualne_rekordy(wyniki)

        elif wybor == "0":
            zapisz_plik(wyniki, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()