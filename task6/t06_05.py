import random

def generate_list() -> list:
    numbers = []
    for _ in range(random.randint(3, 10)):
        numbers.append(random.randint(1, 100))
    return numbers

def remove_odd_numbers(numbers: list) -> list:
    return [num for num in numbers if num % 2 == 0]

def main():
    numbers = generate_list()
    print("Generoidut luvut:", numbers)
    even_numbers = remove_odd_numbers(numbers)
    print("Parittomat luvut poistettu:", even_numbers)

if __name__ == "__main__":
    main()
