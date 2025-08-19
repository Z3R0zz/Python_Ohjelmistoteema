def calculate_pizza_value(diameter: float, price: float):
  radius = diameter / 2
  area = 3.14159 * radius**2
  value = area / price
  return value

def main():
  pizza_1_diameter = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
  pizza_1_price = float(input("Syötä ensimmäisen pizzan hinta (€): "))

  pizza_2_diameter = float(input("Syötä toisen pizzan halkaisija (cm): "))
  pizza_2_price = float(input("Syötä toisen pizzan hinta (€): "))

  pizza_1_value = calculate_pizza_value(pizza_1_diameter, pizza_1_price)
  pizza_2_value = calculate_pizza_value(pizza_2_diameter, pizza_2_price)

  print("Ensimmäisen pizzan arvo (cm²/€):", pizza_1_value)
  print("Toisen pizzan arvo (cm²/€):", pizza_2_value)

  if pizza_1_value > pizza_2_value:
    print("Ensimmäinen pizza on parempi valinta.")
  elif pizza_1_value < pizza_2_value:
    print("Toinen pizza on parempi valinta.")
  else:
    print("Molemmat pizzat ovat yhtä hyviä.")

if __name__ == "__main__":
  main()
