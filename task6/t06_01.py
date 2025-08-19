import random

def roll_dice() -> int:
    return random.randint(1, 6)

def loop_dice():
    while True:
        number = roll_dice()
        print(f"Nopan arvo: {number}")
        if number == 6:
            print("Arvo oli 6, lopetetaan.")
            break

def main():
    loop_dice()

if __name__ == "__main__":
    main()
