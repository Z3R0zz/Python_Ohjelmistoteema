class Hissi:
    def __init__(self, alin: int, ylin: int):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self) -> None:
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self) -> None:
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, uusi_kerros: int) -> None:
        if uusi_kerros < self.alin:
            uusi_kerros = self.alin
        elif uusi_kerros > self.ylin:
            uusi_kerros = self.ylin

        if uusi_kerros > self.kerros:
            while self.kerros < uusi_kerros:
                self.kerros_ylos()
        elif uusi_kerros < self.kerros:
            while self.kerros > uusi_kerros:
                self.kerros_alas()



h1 = Hissi(0, 10)

h1.siirry_kerrokseen(10)
h1.siirry_kerrokseen(0)
