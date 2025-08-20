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

    def kulje(self, tunnit: float) -> None:
        self.kuljettu_matka += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus: str, huippunopeus: int, akkukapasiteetti_kwh: float):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti_kwh = akkukapasiteetti_kwh


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus: str, huippunopeus: int, tankin_koko_l: float):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko_l = tankin_koko_l

def main():
    s = Sahkoauto("ABC-15", 180, 52.5)
    p = Polttomoottoriauto("ACD-123", 165, 32.3)

    s.kiihdyta(150)
    p.kiihdyta(140)

    s.kulje(3)
    p.kulje(3)

    print(f"{s.rekisteritunnus} mittarissa: {s.kuljettu_matka:.0f} km @ {s.nopeus} km/h")
    print(f"{p.rekisteritunnus} mittarissa: {p.kuljettu_matka:.0f} km @ {p.nopeus} km/h")

if __name__ == "__main__":
    main()
