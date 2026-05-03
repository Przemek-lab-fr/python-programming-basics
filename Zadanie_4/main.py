import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "lista_zadan.json"

PRIORYTETY = ("niski", "normalny", "wysoki", "pilne")


def dodaj_zadanie(zadania, tresc, priorytet):
    if tresc == "":
        print("Błąd: treść zadania nie może być pusta.")
        return

    if priorytet not in PRIORYTETY:
        print("Błąd: nieprawidłowy priorytet.")
        print(f"Dostępne priorytety: {PRIORYTETY}")
        return

    zadanie = {
        "tresc": tresc,
        "priorytet": priorytet,
        "wykonane": False
    }

    zadania.append(zadanie)
    print("Dodano zadanie.")


def oznacz_wykonane(zadania, numer):
    if len(zadania) == 0:
        print("Brak zadań do oznaczenia.")
        return

    if numer < 1 or numer > len(zadania):
        print("Błąd: nieprawidłowy numer zadania.")
        return

    zadania[numer - 1]["wykonane"] = True
    print("Zadanie oznaczone jako wykonane.")


def wyswietl_zadania(zadania, tylko_niewykonane=False):
    if len(zadania) == 0:
        print("Brak zadań na liście.")
        return

    znaleziono = False

    for indeks, zadanie in enumerate(zadania, start=1):
        if tylko_niewykonane and zadanie["wykonane"]:
            continue

        status = "[X]" if zadanie["wykonane"] else "[ ]"
        print(f"{indeks}. {status} {zadanie['tresc']} - priorytet: {zadanie['priorytet']}")
        znaleziono = True

    if not znaleziono:
        print("Brak niewykonanych zadań.")


def zapisz_plik(zadania, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(zadania, plik, indent=4, ensure_ascii=False)
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
    zadania = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== LISTA ZADAŃ ===")
        print("1. Dodaj zadanie")
        print("2. Oznacz jako wykonane")
        print("3. Pokaż wszystkie zadania")
        print("4. Pokaż tylko niewykonane")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            tresc = input("Podaj treść zadania: ")

            print(f"Dostępne priorytety: {PRIORYTETY}")
            priorytet = input("Podaj priorytet: ")

            dodaj_zadanie(zadania, tresc, priorytet)

        elif wybor == "2":
            wyswietl_zadania(zadania)

            try:
                numer = int(input("Podaj numer zadania do oznaczenia: "))
            except ValueError:
                print("Błąd: wpisz liczbę całkowitą.")
                continue

            oznacz_wykonane(zadania, numer)

        elif wybor == "3":
            wyswietl_zadania(zadania)

        elif wybor == "4":
            wyswietl_zadania(zadania, tylko_niewykonane=True)

        elif wybor == "0":
            zapisz_plik(zadania, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()