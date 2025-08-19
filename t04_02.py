def inch_to_cm(inch) -> float:
    return inch * 2.54

while True:
    inch = float(input("Syötä tuumat: "))
    if inch < 0:
        break

    cm = inch_to_cm(inch)
    print(f"{inch} tuumaa on {cm} senttimetriä.")
