#!/usr/bin/env python3
import os
import sqlite3
import sys

def create_database(db_name="mydatabase.db"):
    exists = os.path.exists(db_name)
    try:
        conn = sqlite3.connect(db_name)
        conn.close()
        if not exists:
            print(f"Database '{db_name}' created successfully.")
        else:
            print(f"Database '{db_name}' already exists.")
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_database(sys.argv[1])
    else:
        create_database()
