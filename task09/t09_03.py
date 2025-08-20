class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, amount):
        self.nopeus += amount
        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunti):
        self.kuljettu_matka += self.nopeus * tunti

car = Auto("ABC-123", 142, 2000)

car.kiihdyta(60)
car.kulje(1.5)

print(f"Auton kuljettu matka: {car.kuljettu_matka} km")
