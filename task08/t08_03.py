import mysql.connector
from geopy.distance import distance as geo_distance

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

def get_coords(conn, icao: str) -> tuple[float, float] | None:
    icao = icao.strip().upper()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
            (icao,),
        )
        row = cursor.fetchone()
        if not row:
            return None
        lat, lon = row["latitude_deg"], row["longitude_deg"]
        if lat is None or lon is None:
            return None
        return float(lat), float(lon)
    finally:
        cursor.close()

def main():
    connection = connect_to_database()
    if not connection:
        print("Ei yhteyttä tietokantaan.")
        return

    a = input("Syötä 1. lentoaseman ICAO-koodi: ")
    b = input("Syötä 2. lentoaseman ICAO-koodi: ")

    coords_a = get_coords(connection, a)
    coords_b = get_coords(connection, b)

    if not coords_a:
        print("1. koodia ei löytynyt tai puuttuvat koordinaatit.")
    if not coords_b:
        print("2. koodia ei löytynyt tai puuttuvat koordinaatit.")
    if not coords_a or not coords_b:
        connection.close()
        return

    km = geo_distance(coords_a, coords_b).km
    print(f"Etäisyys: {km:.2f} km")

    connection.close()

if __name__ == "__main__":
    main()
