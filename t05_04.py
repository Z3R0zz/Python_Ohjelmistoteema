i = 0
cities = []

while i < 5:
    city = input("Syötä kaupunki: ")
    cities.append(city)
    i += 1

print("Syöttämäsi kaupungit:")
for city in cities:
    print(city)
