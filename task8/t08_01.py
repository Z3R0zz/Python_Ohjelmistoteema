import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port= 3306,
            user='zero',
            password='1234567890',
            database='flight_game',
            autocommit=True
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
        return None

def fetch_airport_data(connection, icao_code):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result


def main():
    connection = connect_to_database()

    code = input("Syötä lentoaseman ICAO-koodi: ")
    if connection:
        airport_data = fetch_airport_data(connection, code)
        if airport_data:
            print(airport_data["name"])
            print(airport_data["municipality"])

        else:
            print("Lentoasemaa ei löytynyt.")
        connection.close()


if __name__ == "__main__":
    main()
