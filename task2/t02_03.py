def calculate_area(base: float, height: float) -> float:
    return base * height

def calculate_perimeter(base: float, height: float) -> float:
    return 2 * (base + height)

base = float(input("Syötä suorakulmion kannan pituus: "))
height = float(input("Syötä suorakulmion korkeuden pituus: "))

area = calculate_area(base, height)
print(f"Suorakulmion pinta-ala on: {area}")

perimeter = calculate_perimeter(base, height)
print(f"Suorakulmion piiri on: {perimeter}")
