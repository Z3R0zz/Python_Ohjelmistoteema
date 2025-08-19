names = set()

def main():
  while True:
      name = input("Syötä nimi (tai tyhjää lopettaaksesi): ")
      if name.lower() == "":
          break

      if name in names:
          print("Aiemmin syötetty nimi")
          continue

      names.add(name)
      print("Uusi nimi")

  for name in names:
      print(f"Nimi: {name}")

if __name__ == "__main__":
    main()
