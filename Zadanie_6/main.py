import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "wyniki_egzaminow.json"

PROGI = (
    (90, "celujący"),
    (75, "bardzo dobry"),
    (60, "dobry"),
    (45, "dostateczny"),
    (30, "dopuszczający"),
    (0, "niedostateczny")
)

MIN_PUNKTY = 30


def ocena_slowna(punkty):
    for prog, nazwa in PROGI:
        if punkty >= prog:
            return nazwa


def dodaj_wynik(wyniki, uczen, egzamin, punkty, data):
    if uczen == "":
        print("Błąd: imię i nazwisko nie może być puste.")
        return

    if egzamin == "":
        print("Błąd: nazwa egzaminu nie może być pusta.")
        return

    if punkty < 0 or punkty > 100:
        print("Błąd: punkty muszą być od 0 do 100.")
        return

    wynik = {
        "uczen": uczen,
        "egzamin": egzamin,
        "punkty": punkty,
        "data": data
    }

    wyniki.append(wynik)
    print("Dodano wynik.")


def wyswietl_wyniki(wyniki):
    if len(wyniki) == 0:
        print("Brak wyników.")
        return

    for wynik in wyniki:
        status = "zdał" if wynik["punkty"] >= MIN_PUNKTY else "nie zdał"
        ocena = ocena_slowna(wynik["punkty"])

        print(
            f"Uczeń: {wynik['uczen']}, "
            f"Egzamin: {wynik['egzamin']}, "
            f"Punkty: {wynik['punkty']}, "
            f"Ocena: {ocena}, "
            f"Status: {status}, "
            f"Data: {wynik['data']}"
        )


def statystyki(wyniki):
    if len(wyniki) == 0:
        print("Brak danych do statystyk.")
        return

    suma = 0
    punkty_lista = []

    for wynik in wyniki:
        suma += wynik["punkty"]
        punkty_lista.append(wynik["punkty"])

    srednia = suma / len(wyniki)

    print(f"Średnia punktów: {srednia:.2f}")
    print(f"Najwyższy wynik: {max(punkty_lista)}")
    print(f"Najniższy wynik: {min(punkty_lista)}")


def zapisz_plik(wyniki, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(wyniki, plik, indent=4, ensure_ascii=False)
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
    wyniki = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== WYNIKI EGZAMINÓW ===")
        print("1. Dodaj wynik")
        print("2. Lista wyników")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            uczen = input("Podaj imię i nazwisko ucznia: ")
            egzamin = input("Podaj nazwę egzaminu: ")
            data = input("Podaj datę (YYYY-MM-DD): ")

            try:
                punkty = int(input("Podaj punkty od 0 do 100: "))
            except ValueError:
                print("Błąd: wpisz liczbę całkowitą.")
                continue

            dodaj_wynik(wyniki, uczen, egzamin, punkty, data)

        elif wybor == "2":
            wyswietl_wyniki(wyniki)

        elif wybor == "3":
            statystyki(wyniki)

        elif wybor == "0":
            zapisz_plik(wyniki, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()