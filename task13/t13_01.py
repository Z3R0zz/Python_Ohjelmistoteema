import flask, math

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

app = flask.Flask(__name__)

@app.route("/alkuluku/<int:luku>")
def home(luku):
    return {
        "Number": luku,
        "isPrime": is_prime(luku)
    }

if __name__ == "__main__":
    app.run(debug=True)
