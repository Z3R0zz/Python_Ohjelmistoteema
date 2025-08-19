def gallons_to_liters(gallons: float) -> float:
    return gallons * 3.78541

def prompt_gallons():
    while True:
        try:
            gallons = float(input("Syötä bensan määrä galloneina: "))
            if gallons < 0:
                break

            liters = gallons_to_liters(gallons)
            print(f"{gallons} galloneita on {liters} litraa.")
        except ValueError:
            print("Virheellinen luku.")

def main():
  prompt_gallons()

if __name__ == "__main__":
    main()
