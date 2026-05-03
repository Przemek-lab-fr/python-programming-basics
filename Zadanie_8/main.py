import json
from pathlib import Path

FOLDER_PROGRAMU = Path(__file__).parent
NAZWA_PLIKU = FOLDER_PROGRAMU / "dziennik_pogody.json"

WARUNKI = ("słonecznie", "pochmurno", "deszcz", "śnieg", "mgła", "burza")


def dodaj_wpis(dziennik, data, temperatura, warunki, wilgotnosc):
    if warunki not in WARUNKI:
        print("Błąd: nieprawidłowe warunki.")
        print(f"Dostępne: {WARUNKI}")
        return

    if wilgotnosc < 0 or wilgotnosc > 100:
        print("Błąd: wilgotność musi być 0–100.")
        return

    wpis = {
        "data": data,
        "temperatura": temperatura,
        "warunki": warunki,
        "wilgotnosc": wilgotnosc
    }

    dziennik.append(wpis)
    print("Dodano wpis.")


def wyswietl_wpisy(dziennik):
    if len(dziennik) == 0:
        print("Brak danych.")
        return

    for w in dziennik:
        print(
            f"Data: {w['data']}, "
            f"Temp: {w['temperatura']}°C, "
            f"Warunki: {w['warunki']}, "
            f"Wilgotność: {w['wilgotnosc']}%"
        )


def statystyki(dziennik):
    if len(dziennik) == 0:
        print("Brak danych.")
        return

    temp_lista = []
    warunki_count = {}

    for w in dziennik:
        temp_lista.append(w["temperatura"])

        war = w["warunki"]
        if war in warunki_count:
            warunki_count[war] += 1
        else:
            warunki_count[war] = 1

    srednia = sum(temp_lista) / len(temp_lista)
    max_temp = max(temp_lista)
    min_temp = min(temp_lista)

    najczestsze = max(warunki_count, key=warunki_count.get)

    print(f"Średnia temperatura: {srednia:.2f}")
    print(f"Najcieplejszy dzień: {max_temp}")
    print(f"Najchłodniejszy dzień: {min_temp}")
    print(f"Najczęstsze warunki: {najczestsze}")


def zapisz_plik(dziennik, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(dziennik, plik, indent=4, ensure_ascii=False)
    print("Zapisano dane.")


def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except:
        return []


def main():
    dziennik = wczytaj_plik(NAZWA_PLIKU)

    while True:
        print("\n=== DZIENNIK POGODY ===")
        print("1. Dodaj wpis")
        print("2. Historia")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            data = input("Podaj datę: ")

            try:
                temperatura = float(input("Podaj temperaturę: "))
                wilgotnosc = int(input("Podaj wilgotność (0-100): "))
            except:
                print("Błąd: wpisz liczby.")
                continue

            print(f"Dostępne warunki: {WARUNKI}")
            warunki = input("Podaj warunki: ")

            dodaj_wpis(dziennik, data, temperatura, warunki, wilgotnosc)

        elif wybor == "2":
            wyswietl_wpisy(dziennik)

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