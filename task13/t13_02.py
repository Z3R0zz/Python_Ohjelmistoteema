import mysql.connector, flask

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

    app = flask.Flask(__name__)

    @app.route("/kenttä/<string:icao_code>")
    def home(icao_code):
        data = fetch_airport_data(connection, icao_code)
        if data:
            return {
                "ICAO": icao_code,
                "Name": data["name"],
                "Municipality": data["municipality"]
            }
        return {"error": "Lentoasemaa ei löytynyt."}

    app.run(debug=True)


if __name__ == "__main__":
    main()
