numbers = []

while True:
    num = input("Syötä luku: ")
    if num == "":
        break
    numbers.append(float(num))

numbers.sort()

print(f"Pienin luku on {numbers[0]}")
print(f"Suurin luku on {numbers[-1]}")
