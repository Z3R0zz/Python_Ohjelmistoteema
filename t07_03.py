airports = {
    "EFHK": "Helsinki-Vantaa Airport",
    "EGLL": "London Heathrow Airport",
    "LFPG": "Paris Charles de Gaulle",
    "EDDF": "Frankfurt am Main Airport",
    "KJFK": "John F. Kennedy International"
}

def main():
    while True:
        print("\nValitse toiminto:")
        print("1) Syötä uusi lentoasema")
        print("2) Hae lentoaseman tiedot")
        print("0) Lopeta")
        choice = input("> ").strip()

        if choice == "1":
            icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
            nimi = input("Anna lentoaseman nimi: ").strip()
            airports[icao] = nimi
            print(f"Tallennettu: {icao}: {nimi}")
            continue

        if choice == "2":
            icao = input("Anna haettava ICAO-koodi: ").strip().upper()
            if icao in airports:
                print(f"{icao}: {airports[icao]}")
            else:
                print("Ei löytynyt.")
            continue

        if choice == "0":
            break

        print("Tuntematon valinta.")

if __name__ == "__main__":
    main()
