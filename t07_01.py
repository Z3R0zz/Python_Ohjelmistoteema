def main():
  seasons = (
      None,
      "Talvi",
      "Talvi",
      "Kevät",
      "Kevät",
      "Kevät",
      "Kesä",
      "Kesä",
      "Kesä",
      "Syksy",
      "Syksy",
      "Syksy",
      "Talvi",
  )

  month = int(input("Syötä kuukausi (1-12): "))
  if 1 <= month <= 12:
      print(f"Kuukauden {month} vuodenaika on: {seasons[month]}")
  else:
      print("Virheellinen kuukausi")

if __name__ == "__main__":
   main()
