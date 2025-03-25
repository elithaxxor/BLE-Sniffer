from flask import Flask, render_template  # Import the Flask class and the render_template function from the flask module
import sqlite3  # Import the sqlite3 module to interact with SQLite databases

app = Flask(__name__)  # Create a new Flask web application instance

def get_devices():
    """Retrieve all device logs from the database."""
    conn = sqlite3.connect("bluetooth_devices.db")  # Connect to the SQLite database named 'bluetooth_devices.db'
    conn.row_factory = sqlite3.Row  # Set the row factory to sqlite3.Row to access columns by name
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries
    cursor.execute("SELECT * FROM devices ORDER BY id DESC")  # Execute a SQL query to retrieve all rows from the 'devices' table, ordered by 'id' in descending order
    devices = cursor.fetchall()  # Fetch all results from the executed query
    conn.close()  # Close the database connection
    return devices  # Return the fetched device logs

@app.route("/")  # Define the route for the root URL
def index():
    devices = get_devices()  # Retrieve the device logs from the database
    return render_template("index.html", devices=devices)  # Render the 'index.html' template and pass the device logs to it

if __name__ == "__main__":
    # Run the Flask app on localhost:5000 in debug mode if this script is executed directly
    app.run(debug=True)
