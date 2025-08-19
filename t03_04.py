year = int(input("Syötä vuosiluku: "))

if year < 0:
    print("Virheellinen vuosiluku")
    exit()

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  print("Vuosi on karkausvuosi.")
else:
  print("Vuosi ei ole karkausvuosi.")
