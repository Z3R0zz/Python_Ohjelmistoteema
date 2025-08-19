numbers = []

while True:
  integer = input("Syötä luku: ")
  if integer == "":
    break

  try:
    value = float(integer)
    numbers.append(value)
  except ValueError:
    print("Virheellinen syöte, yritä uudelleen.")

sorted_numbers = sorted(numbers, reverse=True)
top_5_numbers = sorted_numbers[:5]

for top_5_number in top_5_numbers:
    print(f"Syötit arvon: {top_5_number}")
