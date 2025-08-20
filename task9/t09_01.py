class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

car = Auto("ABC-123", 142)

print(car.rekisteritunnus)
print(f"{car.huippunopeus} km/h")
print(car.nopeus)
print(car.kuljettu_matka)
