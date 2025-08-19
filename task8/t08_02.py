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

def fetch_airport_count(connection, iso_country, airport_type):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT count(*) FROM airport WHERE iso_country = %s AND type = %s"
    cursor.execute(query, (iso_country, airport_type))
    result = cursor.fetchone()
    cursor.close()
    return result

def main():
    connection = connect_to_database()
    if connection:
        iso_country = input("Syötä maan ISO-koodi: ")
        small_airports = fetch_airport_count(connection, iso_country, 'small_airport')
        medium_airports = fetch_airport_count(connection, iso_country, 'medium_airport')
        large_airports = fetch_airport_count(connection, iso_country, 'large_airport')
        if small_airports:
            print(f"Pieniä lentoasemia maassa {iso_country}: {small_airports['count(*)']}")
        if medium_airports:
            print(f"Keskikokoisia lentoasemia maassa {iso_country}: {medium_airports['count(*)']}")
        if large_airports:
            print(f"Suuria lentoasemia maassa {iso_country}: {large_airports['count(*)']}")
        connection.close()

if __name__ == "__main__":
    main()
