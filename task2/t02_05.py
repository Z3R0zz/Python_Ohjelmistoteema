leiviskat = float(input("Syötä leivisköiden määrä: "))
naulat = float(input("Syötä naulojen määrä: "))
luodit = float(input("Syötä luotien määrä: "))

yhteensaGramma = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)

kilot = int(yhteensaGramma // 1000)
grammat = yhteensaGramma % 1000

print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa")
