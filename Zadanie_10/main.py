import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "tracker_nauki.json"

PRZEDMIOTY = ("matematyka", "fizyka", "programowanie", "angielski", "historia", "inne")


def dodaj_sesje(sesje, data, przedmiot, czas_min, notatka):
    if przedmiot not in PRZEDMIOTY:
        print("Błąd: nieprawidłowy przedmiot.")
        print(f"Dostępne przedmioty: {PRZEDMIOTY}")
        return

    if czas_min <= 0:
        print("Błąd: czas nauki musi być większy od 0.")
        return

    sesja = {
        "data": data,
        "przedmiot": przedmiot,
        "czas_min": czas_min,
        "notatka": notatka
    }

    sesje.append(sesja)
    print("Dodano sesję nauki.")


def wyswietl_sesje(sesje, przedmiot=None):
    if len(sesje) == 0:
        print("Brak sesji nauki.")
        return

    znaleziono = False

    for sesja in sesje:
        if przedmiot is not None and sesja["przedmiot"] != przedmiot:
            continue

        print(
            f"Data: {sesja['data']}, "
            f"Przedmiot: {sesja['przedmiot']}, "
            f"Czas: {sesja['czas_min']} min, "
            f"Notatka: {sesja['notatka']}"
        )
        znaleziono = True

    if not znaleziono:
        print("Brak sesji dla wybranego przedmiotu.")


def statystyki(sesje):
    if len(sesje) == 0:
        print("Brak danych do statystyk.")
        return

    czas_per_przedmiot = {}

    for sesja in sesje:
        przedmiot = sesja["przedmiot"]

        if przedmiot in czas_per_przedmiot:
            czas_per_przedmiot[przedmiot] += sesja["czas_min"]
        else:
            czas_per_przedmiot[przedmiot] = sesja["czas_min"]

    laczny_czas = sum(czas_per_przedmiot.values())
    najwiecej = max(czas_per_przedmiot, key=czas_per_przedmiot.get)
    najmniej = min(czas_per_przedmiot, key=czas_per_przedmiot.get)

    print(f"Łączny czas nauki: {laczny_czas} min")

    for przedmiot, czas in czas_per_przedmiot.items():
        print(f"{przedmiot}: {czas} min")

    print(f"Najwięcej czasu: {najwiecej}")
    print(f"Najmniej czasu: {najmniej}")


def zapisz_plik(sesje, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(sesje, plik, indent=4, ensure_ascii=False)
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
    sesje = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== TRACKER NAUKI ===")
        print("1. Dodaj sesję nauki")
        print("2. Lista sesji")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            data = input("Podaj datę: ")

            print(f"Dostępne przedmioty: {PRZEDMIOTY}")
            przedmiot = input("Podaj przedmiot: ")

            try:
                czas_min = int(input("Podaj czas nauki w minutach: "))
            except ValueError:
                print("Błąd: wpisz liczbę całkowitą.")
                continue

            notatka = input("Podaj notatkę (opcjonalnie): ")

            dodaj_sesje(sesje, data, przedmiot, czas_min, notatka)

        elif wybor == "2":
            print("1. Wszystkie sesje")
            print("2. Sesje z wybranego przedmiotu")
            podwybor = input("Wybierz opcję: ")

            if podwybor == "1":
                wyswietl_sesje(sesje)

            elif podwybor == "2":
                print(f"Dostępne przedmioty: {PRZEDMIOTY}")
                przedmiot = input("Podaj przedmiot: ")
                wyswietl_sesje(sesje, przedmiot)

            else:
                print("Nieprawidłowa opcja.")

        elif wybor == "3":
            statystyki(sesje)

        elif wybor == "0":
            zapisz_plik(sesje, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()