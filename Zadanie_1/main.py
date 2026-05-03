import json

NAZWA_PLIKU = "dziennik_biegania.json"
MINIMALNY_DYSTANS = (1.0,)


def dodaj_bieg(historia, data, dystans, czas):
    if dystans < MINIMALNY_DYSTANS[0]:
        print(f"Błąd: minimalny dystans to {MINIMALNY_DYSTANS[0]} km.")
        return

    if czas <= 0:
        print("Błąd: czas musi być większy od 0.")
        return

    tempo = czas / dystans

    bieg = {
        "data": data,
        "dystans_km": dystans,
        "czas_min": czas,
        "tempo_min_km": tempo
    }

    historia.append(bieg)
    print("Dodano bieg.")


def wyswietl_historie(historia):
    if len(historia) == 0:
        print("Brak zapisanych biegów.")
        return

    for bieg in historia:
        print(
            f"Data: {bieg['data']}, "
            f"Dystans: {bieg['dystans_km']} km, "
            f"Czas: {bieg['czas_min']} min, "
            f"Tempo: {bieg['tempo_min_km']:.2f} min/km"
        )


def statystyki(historia):
    if len(historia) == 0:
        print("Brak danych do statystyk.")
        return

    laczny_dystans = 0
    laczny_czas = 0

    for bieg in historia:
        laczny_dystans += bieg["dystans_km"]
        laczny_czas += bieg["czas_min"]

    srednie_tempo = laczny_czas / laczny_dystans

    print(f"Łączny dystans: {laczny_dystans:.2f} km")
    print(f"Liczba treningów: {len(historia)}")
    print(f"Średnie tempo: {srednie_tempo:.2f} min/km")


def zapisz_plik(historia, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(historia, plik, indent=4, ensure_ascii=False)

    print("Dane zapisane do pliku.")


def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Plik JSON jest pusty albo uszkodzony. Startuję z pustą historią.")
        return []


def main():
    historia = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== DZIENNIK BIEGANIA ===")
        print("1. Dodaj bieg")
        print("2. Historia biegów")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            data = input("Podaj datę biegu (np. 2026-03-01): ")

            if data == "":
                print("Błąd: data nie może być pusta.")
                continue

            try:
                dystans = float(input("Podaj dystans w km: "))
                czas = float(input("Podaj czas w minutach: "))
            except ValueError:
                print("Błąd: dystans i czas muszą być liczbami.")
                continue

            if dystans <= 0:
                print("Błąd: dystans musi być liczbą dodatnią.")
                continue
            elif czas <= 0:
                print("Błąd: czas musi być liczbą dodatnią.")
                continue
            else:
                dodaj_bieg(historia, data, dystans, czas)

        elif wybor == "2":
            wyswietl_historie(historia)

        elif wybor == "3":
            statystyki(historia)

        elif wybor == "0":
            zapisz_plik(historia, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja. Wybierz 1, 2, 3 albo 0.")


if __name__ == "__main__":
    main()