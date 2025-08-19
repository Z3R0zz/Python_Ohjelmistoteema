import random

def generate_random_numbers(count: int) -> list[int]:
    return [random.randint(0, 9) for _ in range(count)]

print(f"Kolmenumeroinen pin: {''.join(map(str, generate_random_numbers(3))) }")
print(f"Nelinumeroinen pin: {''.join(map(str, generate_random_numbers(4))) }")
