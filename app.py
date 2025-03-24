from flask import Flask, render_template
import sqlite
app = Flask(__name__)

def get_devices():
    """Retrieve all device logs from the database."""
    conn = sqlite3.connect("bluetooth_devices.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices ORDER BY id DESC")
    devices = cursor.fetchall()
    conn.close()
    return devices

@app.route("/")
def index():
    devices = get_devices()
    return render_template("index.html", devices=devices)

if __name__ == "__main__":
    # Run the Flask app on localhost:5000
    app.run(debug=True)