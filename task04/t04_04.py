import random

number = random.randint(1, 10)

while True:
    guess = int(input("Arvaa luku 1-10: "))

    if guess == number:
        print("Oikein!")
        break

    if guess < number:
        print("Liian pieni.")
        continue

    print("Liian suuri.")
