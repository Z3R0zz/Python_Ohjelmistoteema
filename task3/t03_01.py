size = float(input("Syötä kuhan pituus (cm): "))

if size < 37:
    cm_needed = 37 - size
    print(f"Laita kuha takaisin veteen. Tarvitset {cm_needed} cm lisää.")
    exit()

print("Kuha on tarpeeksi iso, voit pitää sen.")
