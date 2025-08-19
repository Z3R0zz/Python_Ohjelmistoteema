import random

def sum_of_numbers(numbers: list) -> int:
    return sum(numbers)

def generate_list() -> list:
    numbers = []
    for _ in range(random.randint(3, 10)):
        numbers.append(random.randint(1, 100))
    return numbers

def main():
    numbers = generate_list()
    print("Generoidut luvut:", numbers)
    print("Lukujen summa:", sum_of_numbers(numbers))

if __name__ == "__main__":
    main()
