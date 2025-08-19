gender = input("Syötä sukupuolesi (m/n): ").lower()

if gender not in ["m", "n"]:
    print("Virheellinen sukupuoli")
    exit()

hemoglobin = float(input("Syötä hemoglobiiniarvosi (g/l): "))

if gender == "m":
    if hemoglobin < 134:
        print("Hemoglobiiniarvo liian alhainen.")
    elif hemoglobin > 170:
        print("Hemoglobiiniarvo liian korkea.")
    else:
        print("Hemoglobiiniarvo normaali.")
else:
    if hemoglobin < 117:
        print("Hemoglobiiniarvo liian alhainen.")
    elif hemoglobin > 153:
        print("Hemoglobiiniarvo liian korkea.")
    else:
        print("Hemoglobiiniarvo normaali.")
