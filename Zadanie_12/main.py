import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "todo.json"

STATUSY = ["do zrobienia", "w trakcie", "zrobione"]


def dodaj_zadanie(lista, nazwa, opis):
    zadanie = {
        "nazwa": nazwa,
        "opis": opis,
        "status": "do zrobienia"
    }
    lista.append(zadanie)
    print("Dodano zadanie.")


def wyswietl_zadania(lista):
    if len(lista) == 0:
        print("Brak zadań.")
        return

    for i, zadanie in enumerate(lista, start=1):
        print(f"{i}. {zadanie['nazwa']} - {zadanie['status']}")
        print(f"   Opis: {zadanie['opis']}")


def zmien_status(lista, indeks, nowy_status):
    if indeks < 0 or indeks >= len(lista):
        print("Błąd: nieprawidłowy numer zadania.")
        return

    if nowy_status not in STATUSY:
        print("Błąd: nieprawidłowy status.")
        return

    lista[indeks]["status"] = nowy_status
    print("Zmieniono status.")


def usun_zadanie(lista, indeks):
    if indeks < 0 or indeks >= len(lista):
        print("Błąd: nieprawidłowy numer zadania.")
        return

    usuniete = lista.pop(indeks)
    print(f"Usunięto zadanie: {usuniete['nazwa']}")


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
        print("\n=== TODO LIST ===")
        print("1. Dodaj zadanie")
        print("2. Lista zadań")
        print("3. Zmień status")
        print("4. Usuń zadanie")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nazwa = input("Nazwa zadania: ")
            opis = input("Opis: ")
            dodaj_zadanie(lista, nazwa, opis)

        elif wybor == "2":
            wyswietl_zadania(lista)

        elif wybor == "3":
            wyswietl_zadania(lista)

            try:
                indeks = int(input("Numer zadania: ")) - 1
            except ValueError:
                print("Błąd: wpisz liczbę.")
                continue

            print("Dostępne statusy:")
            for s in STATUSY:
                print("-", s)

            nowy_status = input("Nowy status: ")
            zmien_status(lista, indeks, nowy_status)

        elif wybor == "4":
            wyswietl_zadania(lista)

            try:
                indeks = int(input("Numer zadania do usunięcia: ")) - 1
            except ValueError:
                print("Błąd: wpisz liczbę.")
                continue

            usun_zadanie(lista, indeks)

        elif wybor == "0":
            zapisz_plik(lista, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()