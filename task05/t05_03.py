import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False

    return True


try:
    n = int(input("Anna kokonaisluku: "))
except ValueError:
    print("Syöte ei ole kokonaisluku.")
    exit()

if is_prime(n):
    print(f"{n} on alkuluku.")
else:
    print(f"{n} ei ole alkuluku.")
