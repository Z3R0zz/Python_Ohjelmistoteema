import random

class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int, kuljettu_matka: float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, amount: int):
        self.nopeus += amount
        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunti: float):
        self.kuljettu_matka += self.nopeus * tunti

def generate_cars(num_cars: int) -> list[Auto]:
    cars = []
    for i in range(1, num_cars + 1):
        car = Auto(f"ABC-{i}", random.randint(100, 200), 0)
        cars.append(car)
    return cars

def race(cars: list[Auto]) -> None:
    while True:
        for car in cars:
            car.kiihdyta(random.randint(-10, 15))
            car.kulje(1)
            if car.kuljettu_matka >= 10000:
                print(f"Car {car.rekisteritunnus} has finished the race!")
                return

def print_results(cars: list[Auto]):
    print(f"{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
    print("-" * 45)
    for car in cars:
        print(f"{car.rekisteritunnus:<10}{car.huippunopeus:<15}{car.nopeus:<10}{car.kuljettu_matka:<10.0f}")

cars = generate_cars(10)
race(cars)
print_results(cars)
