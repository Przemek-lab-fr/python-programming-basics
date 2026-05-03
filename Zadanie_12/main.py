import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "planer_wyjsc.json"

MIEJSCA = ("restauracja", "kino", "dom", "park", "kawiarnia", "klub", "inne")
STATUSY = ("planowane", "odbyło się", "odwołane")


def dodaj_wydarzenie(planer, nazwa, data, miejsce, zaproszeni):
    if nazwa == "":
        print("Błąd: nazwa wydarzenia nie może być pusta.")
        return

    if data == "":
        print("Błąd: data nie może być pusta.")
        return

    if miejsce not in MIEJSCA:
        print("Błąd: nieprawidłowy typ miejsca.")
        print(f"Dostępne miejsca: {MIEJSCA}")
        return

    wydarzenie = {
        "nazwa": nazwa,
        "data": data,
        "miejsce": miejsce,
        "zaproszeni": zaproszeni,
        "status": "planowane"
    }

    planer.append(wydarzenie)
    print("Dodano wydarzenie.")


def zmien_status(planer, nazwa, nowy_status):
    if nowy_status not in STATUSY:
        print("Błąd: nieprawidłowy status.")
        print(f"Dostępne statusy: {STATUSY}")
        return

    for wydarzenie in planer:
        if wydarzenie["nazwa"].lower() == nazwa.lower():
            wydarzenie["status"] = nowy_status
            print("Zmieniono status wydarzenia.")
            return

    print("Nie znaleziono wydarzenia o podanej nazwie.")


def wyswietl_planer(planer, status=None):
    if len(planer) == 0:
        print("Brak wydarzeń.")
        return

    znaleziono = False

    for wydarzenie in planer:
        if status is not None and wydarzenie["status"] != status:
            continue

        print(
            f"Nazwa: {wydarzenie['nazwa']}, "
            f"Data: {wydarzenie['data']}, "
            f"Miejsce: {wydarzenie['miejsce']}, "
            f"Zaproszeni: {wydarzenie['zaproszeni']}, "
            f"Status: {wydarzenie['status']}"
        )
        znaleziono = True

    if not znaleziono:
        print("Brak wydarzeń o wybranym statusie.")


def zapisz_plik(planer, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(planer, plik, indent=4, ensure_ascii=False)
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
    planer = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== PLANER WYJŚĆ ===")
        print("1. Dodaj wydarzenie")
        print("2. Zmień status wydarzenia")
        print("3. Lista wydarzeń")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę wydarzenia: ")
            data = input("Podaj datę: ")

            print(f"Dostępne miejsca: {MIEJSCA}")
            miejsce = input("Podaj miejsce: ")

            zaproszeni = input("Podaj zaproszone osoby: ")

            dodaj_wydarzenie(planer, nazwa, data, miejsce, zaproszeni)

        elif wybor == "2":
            nazwa = input("Podaj nazwę wydarzenia: ")

            print(f"Dostępne statusy: {STATUSY}")
            nowy_status = input("Podaj nowy status: ")

            zmien_status(planer, nazwa, nowy_status)

        elif wybor == "3":
            print("1. Wszystkie wydarzenia")
            print("2. Filtruj po statusie")
            podwybor = input("Wybierz opcję: ")

            if podwybor == "1":
                wyswietl_planer(planer)

            elif podwybor == "2":
                print(f"Dostępne statusy: {STATUSY}")
                status = input("Podaj status: ")
                wyswietl_planer(planer, status)

            else:
                print("Nieprawidłowa opcja.")

        elif wybor == "0":
            zapisz_plik(planer, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()