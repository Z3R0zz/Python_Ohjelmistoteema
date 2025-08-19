def calculate_area(radius: float) -> float:
    return 3.14 * radius**2

radius = float(input("Syötä ympyrän säde:"))

area = calculate_area(radius)
print(f"Ympyrän pinta-ala on: {area}")
