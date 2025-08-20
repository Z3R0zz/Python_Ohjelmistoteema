import random

class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0.0

    def kiihdyta(self, muutos: int) -> None:
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit: float = 1.0) -> None:
        self.kuljettu_matka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi: str, pituus_km: int, autot: list[Auto]):
        self.nimi = nimi
        self.pituus = pituus_km
        self.autot = autot

    def tunti_kuluu(self) -> None:
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self) -> None:
        print(f"\n{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        print("-" * 45)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.kuljettu_matka:<10.0f}")

    def kilpailu_ohi(self) -> bool:
        return any(a.kuljettu_matka >= self.pituus for a in self.autot)

def generate_cars(n: int) -> list[Auto]:
    return [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, n + 1)]

def main():
    kilpailu = Kilpailu("Suuri romuralli", 8000, generate_cars(10))
    tunnit = 0

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    print("\nKilpailu on ohi!")
    kilpailu.tulosta_tilanne()

if __name__ == "__main__":
    main()
