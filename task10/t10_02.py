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

class Talo:
    def __init__(self, alin: int, ylin: int, hisseja: int):
        self.hisseja = [Hissi(alin, ylin) for _ in range(hisseja)]

    def aja_hissia(self, hissin_numero: int, kerros: int) -> None:
        if 0 <= hissin_numero < len(self.hisseja):
            self.hisseja[hissin_numero].siirry_kerrokseen(kerros)

t1 = Talo(0, 10, 3)

t1.aja_hissia(0, 5)
t1.aja_hissia(1, 10)
t1.aja_hissia(2, 2)
t1.aja_hissia(0, -1)
t1.aja_hissia(1, 0)
