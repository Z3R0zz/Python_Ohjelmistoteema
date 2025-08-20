class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, amount):
        self.nopeus += amount
        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

car = Auto("ABC-123", 142)

print(car.rekisteritunnus)
print(f"{car.huippunopeus} km/h")
print(car.nopeus)
print(car.kuljettu_matka)

print("Kiihdytetään 30 km/h")
car.kiihdyta(30)

print("Kiihdytetään 70 km/h")
car.kiihdyta(70)

print("Kiihdytetään 50 km/h")
car.kiihdyta(50)

print(f"Auton nopeus: {car.nopeus} km/h")

print("Hätäjarrutus")
car.kiihdyta(-200)

print(f"Auton nopeus: {car.nopeus} km/h")
