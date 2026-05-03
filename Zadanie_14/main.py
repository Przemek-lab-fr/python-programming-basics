import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "ranking_studentow.json"


def dodaj_studenta(studenci, imie, nazwisko, srednia):
    student = {
        "imie": imie,
        "nazwisko": nazwisko,
        "srednia": srednia
    }

    studenci.append(student)
    print("Dodano studenta.")


def wyswietl_studentow(studenci):
    if len(studenci) == 0:
        print("Brak studentów.")
        return

    for student in studenci:
        print(f"{student['imie']} {student['nazwisko']} - średnia: {student['srednia']:.2f}")


def ranking(studenci):
    if len(studenci) == 0:
        print("Brak danych do rankingu.")
        return

    posortowani = sorted(studenci, key=lambda x: x["srednia"], reverse=True)

    print("\n=== RANKING STUDENTÓW ===")
    for miejsce, student in enumerate(posortowani, start=1):
        print(f"{miejsce}. {student['imie']} {student['nazwisko']} - {student['srednia']:.2f}")


def najlepsi(studenci, prog):
    if len(studenci) == 0:
        print("Brak studentów.")
        return

    znaleziono = False

    for student in studenci:
        if student["srednia"] >= prog:
            print(f"{student['imie']} {student['nazwisko']} - {student['srednia']:.2f}")
            znaleziono = True

    if not znaleziono:
        print("Brak studentów spełniających próg.")


def zapisz_plik(studenci, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(studenci, plik, indent=4, ensure_ascii=False)
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
    studenci = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== RANKING STUDENTÓW ===")
        print("1. Dodaj studenta")
        print("2. Lista studentów")
        print("3. Ranking")
        print("4. Pokaż studentów od wybranej średniej")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")

            try:
                srednia = float(input("Podaj średnią: "))
            except ValueError:
                print("Błąd: wpisz liczbę.")
                continue

            dodaj_studenta(studenci, imie, nazwisko, srednia)

        elif wybor == "2":
            wyswietl_studentow(studenci)

        elif wybor == "3":
            ranking(studenci)

        elif wybor == "4":
            try:
                prog = float(input("Podaj minimalną średnią: "))
            except ValueError:
                print("Błąd: wpisz liczbę.")
                continue

            najlepsi(studenci, prog)

        elif wybor == "0":
            zapisz_plik(studenci, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()