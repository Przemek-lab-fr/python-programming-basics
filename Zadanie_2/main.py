import json

NAZWA_PLIKU = "wydatki.json"
MINIMALNA_KWOTA = (0.0,)

def dodaj_wydatek(lista, nazwa, kwota):
    if kwota < MINIMALNA_KWOTA[0]:
        print(f"Błąd: kwota nie może być ujemna.")
        return

    wydatek = {
        "nazwa": nazwa,
        "kwota": kwota
    }

    lista.append(wydatek)
    print("Dodano wydatek.")


def wyswietl_liste(lista):
    if len(lista) == 0:
        print("Brak danych.")
        return

    for w in lista:
        print(f"Nazwa: {w['nazwa']}, Kwota: {w['kwota']} zł")


def statystyki(lista):
    if len(lista) == 0:
        print("Brak danych do statystyk.")
        return

    suma = 0

    for w in lista:
        suma += w["kwota"]

    srednia = suma / len(lista)

    print(f"Suma wydatków: {suma:.2f} zł")
    print(f"Liczba wpisów: {len(lista)}")
    print(f"Średni wydatek: {srednia:.2f} zł")


def zapisz_plik(lista, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        json.dump(lista, plik, indent=4)
    print("Dane zapisane do pliku.")


def main():
    lista = []

    while True:
        print("\n=== LISTA WYDATKÓW ===")
        print("1. Dodaj wydatek")
        print("2. Pokaż listę")
        print("3. Statystyki")
        print("0. Zapisz i wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            nazwa = input("Podaj nazwę wydatku: ")

            try:
                kwota = float(input("Podaj kwotę: "))
            except:
                print("Błąd: wpisz liczbę!")
                continue

            dodaj_wydatek(lista, nazwa, kwota)

        elif wybor == "2":
            wyswietl_liste(lista)

        elif wybor == "3":
            statystyki(lista)

        elif wybor == "0":
            zapisz_plik(lista, NAZWA_PLIKU)
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()