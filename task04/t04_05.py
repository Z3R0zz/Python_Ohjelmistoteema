username = "python"
password = "rules"

attempts = 0

while attempts < 5:
    input_username = input("Käyttäjätunnus: ")
    input_password = input("Salasana: ")

    if input_username == username and input_password == password:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        attempts += 1

if attempts == 5:
    print("Liian monta yritystä. Kirjautuminen epäonnistui.")
