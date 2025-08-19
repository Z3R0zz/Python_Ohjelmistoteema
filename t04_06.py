import random

def estimate_pi(n_points: int) -> float:
    inside = 0
    for _ in range(n_points):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if x*x + y*y <= 1.0:
            inside += 1
    return 4.0 * inside / n_points

N = int(input("Syötä arvottavien pisteiden määrä: "))
if N <= 0:
    print("Syötä positiivinen kokonaisluku.")
    exit()

pi_est = estimate_pi(N)
print(f"Piin likiarvo: {pi_est:.10f}")
