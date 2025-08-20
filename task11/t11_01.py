class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjailija: str, sivumaara: int):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self) -> None:
        print(f"Kirja: {self.nimi}\n  Kirjailija: {self.kirjailija}\n  Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi: str, paatoimittaja: str):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self) -> None:
        print(f"Lehti: {self.nimi}\n  Päätoimittaja: {self.paatoimittaja}")

def main():
    lehti = Lehti("Harry Potter ja Azkabanin vanki", "J. K. Rowling")
    kirja = Kirja("Harry Potter ja puoliverinen prinssi", "J. K. Rowling", 200)

    lehti.tulosta_tiedot()
    kirja.tulosta_tiedot()

if __name__ == "__main__":
    main()
