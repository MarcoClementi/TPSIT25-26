from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/elabora')
def elabora():
    q = request.args.get('stringa', '')

    if len(q) == 0:
        return ""

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="provephp"
        )

        cursor = db.cursor(dictionary=True)

        # Query (simile al LIKE in PHP)
        query = "SELECT name, lat, lng FROM comuni WHERE name LIKE %s"
        cursor.execute(query, (q + "%",))

        risultati = cursor.fetchall()

        if len(risultati) == 0:
            return "nessun nome trovato"

        output = "(comune, latitudine, longitudine)<br><br>"

        for riga in risultati:
            output += f"{riga['name']}, {riga['lat']}, {riga['lng']}<br>"

        return output

    except mysql.connector.Error as err:
        return f"Errore database: {err}"

    finally:
        if db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    app.run(debug=True)