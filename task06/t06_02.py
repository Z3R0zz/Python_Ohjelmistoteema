import random

def roll_dice(sides: int) -> int:
    return random.randint(1, sides)

def loop_dice(sides: int):
    while True:
      number = roll_dice(sides)
      print(f"Nopan arvo: {number}")
      if number == sides:
          print(f"Arvo oli {sides}, lopetetaan.")
          break

def main():
    sides = int(input("Syötä nopan sivujen määrä: "))
    loop_dice(sides)

if __name__ == "__main__":
    main()
