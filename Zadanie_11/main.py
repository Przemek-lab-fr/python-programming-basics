import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "dziennik_snu.json"

JAKOSCI = (
    (1, "bardzo zły"),
    (2, "zły"),
    (3, "przeciętny"),
    (4, "dobry"),
    (5, "bardzo dobry")
)


def opis_jakosci(jakosc):
    for liczba, opis in JAKOSCI:
        if jakosc == liczba:
            return opis
    return "nieznana"


def oblicz_dlugosc_snu(godzina_snu, godzina_pobudki):
    godzina_snu = godzina_snu.replace(".", ":")
    godzina_pobudki = godzina_pobudki.replace(".", ":")

    sen_h = int(godzina_snu.split(":")[0])
    pobudka_h = int(godzina_pobudki.split(":")[0])
    pobudka_h = int(godzina_pobudki.split(":")[0])

    if pobudka_h > sen_h:
        return pobudka_h - sen_h
    else:
        return 24 - sen_h + pobudka_h


def dodaj_wpis(dziennik, data, godzina_snu, godzina_pobudki, jakosc):
    if jakosc < 1 or jakosc > 5:
        print("Błąd: jakość musi być od 1 do 5.")
        return

    dlugosc_h = oblicz_dlugosc_snu(godzina_snu, godzina_pobudki)

    wpis = {
        "data": data,
        "godzina_snu": godzina_snu,
        "godzina_pobudki": godzina_pobudki,
        "dlugosc_h": dlugosc_h,
        "jakosc": jakosc
    }

    dziennik.append(wpis)
    print("Dodano wpis snu.")


def wyswietl_dziennik(dziennik):
    if len(dziennik) == 0:
        print("Brak wpisów snu.")
        return

    for wpis in dziennik:
        opis = opis_jakosci(wpis["jakosc"])

        print(
            f"Data: {wpis['data']}, "
            f"Sen: {wpis['godzina_snu']}, "
            f"Pobudka: {wpis['godzina_pobudki']}, "
            f"Długość: {wpis['dlugosc_h']} h, "
            f"Jakość: {wpis['jakosc']} - {opis}"
        )


def statystyki(dziennik):
    if len(dziennik) == 0:
        print("Brak danych do statystyk.")
        return

    suma_snu = 0
    suma_jakosci = 0
    ponizej_7h = 0

    for wpis in dziennik:
        suma_snu += wpis["dlugosc_h"]
        suma_jakosci += wpis["jakosc"]

        if wpis["dlugosc_h"] < 7:
            ponizej_7h += 1

    srednia_snu = suma_snu / len(dziennik)
    srednia_jakosci = suma_jakosci / len(dziennik)

    print(f"Średnia długość snu: {srednia_snu:.2f} h")
    print(f"Średnia jakość snu: {srednia_jakosci:.2f}")
    print(f"Liczba nocy poniżej 7h: {ponizej_7h}")


def zapisz_plik(dziennik, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(dziennik, plik, indent=4, ensure_ascii=False)
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
    dziennik = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== DZIENNIK SNU ===")
        print("1. Dodaj wpis snu")
        print("2. Historia snu")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            data = input("Podaj datę: ")
            godzina_snu = input("Podaj godzinę zaśnięcia (np. 23:00): ")
            godzina_pobudki = input("Podaj godzinę pobudki (np. 07:00): ")

            try:
                jakosc = int(input("Podaj jakość snu od 1 do 5: "))
            except ValueError:
                print("Błąd: wpisz liczbę całkowitą.")
                continue

            dodaj_wpis(dziennik, data, godzina_snu, godzina_pobudki, jakosc)

        elif wybor == "2":
            wyswietl_dziennik(dziennik)

        elif wybor == "3":
            statystyki(dziennik)

        elif wybor == "0":
            zapisz_plik(dziennik, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()