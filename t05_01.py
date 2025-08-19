import random

def throw_dices(num_dices: int) -> list[int]:
    results = []
    for _ in range(num_dices):
        results.append(random.randint(1, 6))
    return results

def sum_dices(dice_results: list[int]) -> int:
    return sum(dice_results)

dices = int(input("Kuinka monta noppaa heitetään? "))

results = throw_dices(dices)
print(f"Noppien summa: {sum_dices(results)}")
