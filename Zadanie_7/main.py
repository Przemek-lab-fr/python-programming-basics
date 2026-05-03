import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "ksiazka_adresowa.json"

GRUPY = ("rodzina", "przyjaciele", "praca", "znajomi", "inne")


def dodaj_kontakt(kontakty, imie_nazwisko, telefon, email, grupa):
    if imie_nazwisko == "":
        print("Błąd: imię i nazwisko nie może być puste.")
        return

    if telefon == "":
        print("Błąd: numer telefonu nie może być pusty.")
        return

    if "@" not in email:
        print("Błąd: email musi zawierać znak @.")
        return

    if grupa not in GRUPY:
        print("Błąd: nieprawidłowa grupa.")
        print(f"Dostępne grupy: {GRUPY}")
        return

    kontakt = {
        "imie_nazwisko": imie_nazwisko,
        "telefon": telefon,
        "email": email,
        "grupa": grupa
    }

    kontakty.append(kontakt)
    print("Dodano kontakt.")


def wyswietl_kontakty(kontakty, grupa=None):
    if len(kontakty) == 0:
        print("Brak kontaktów.")
        return

    znaleziono = False

    for kontakt in kontakty:
        if grupa is not None and kontakt["grupa"] != grupa:
            continue

        print(
            f"Imię i nazwisko: {kontakt['imie_nazwisko']}, "
            f"Telefon: {kontakt['telefon']}, "
            f"Email: {kontakt['email']}, "
            f"Grupa: {kontakt['grupa']}"
        )
        znaleziono = True

    if not znaleziono:
        print("Brak kontaktów w wybranej grupie.")


def szukaj(kontakty, fraza):
    if len(kontakty) == 0:
        print("Brak kontaktów.")
        return

    znaleziono = False
    fraza = fraza.lower()

    for kontakt in kontakty:
        if fraza in kontakt["imie_nazwisko"].lower():
            print(
                f"Imię i nazwisko: {kontakt['imie_nazwisko']}, "
                f"Telefon: {kontakt['telefon']}, "
                f"Email: {kontakt['email']}, "
                f"Grupa: {kontakt['grupa']}"
            )
            znaleziono = True

    if not znaleziono:
        print("Nie znaleziono kontaktu.")


def zapisz_plik(kontakty, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(kontakty, plik, indent=4, ensure_ascii=False)
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
    kontakty = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== KSIĄŻKA ADRESOWA ===")
        print("1. Dodaj kontakt")
        print("2. Lista kontaktów")
        print("3. Szukaj kontaktu")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            imie_nazwisko = input("Podaj imię i nazwisko: ")
            telefon = input("Podaj numer telefonu: ")
            email = input("Podaj email: ")

            print(f"Dostępne grupy: {GRUPY}")
            grupa = input("Podaj grupę: ")

            dodaj_kontakt(kontakty, imie_nazwisko, telefon, email, grupa)

        elif wybor == "2":
            print("1. Wszystkie kontakty")
            print("2. Kontakty z wybranej grupy")
            podwybor = input("Wybierz opcję: ")

            if podwybor == "1":
                wyswietl_kontakty(kontakty)

            elif podwybor == "2":
                print(f"Dostępne grupy: {GRUPY}")
                grupa = input("Podaj grupę: ")
                wyswietl_kontakty(kontakty, grupa)

            else:
                print("Nieprawidłowa opcja.")

        elif wybor == "3":
            fraza = input("Podaj fragment imienia lub nazwiska: ")
            szukaj(kontakty, fraza)

        elif wybor == "0":
            zapisz_plik(kontakty, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()