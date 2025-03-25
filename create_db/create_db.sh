#!/bin/bash

# Function to create a database
create_database() {
    local db_name="$1"  # Assign the first argument to db_name
    if [ -f "$db_name" ]; then  # Check if the database file already exists
        echo "Database '$db_name' already exists."  # Inform the user that the database exists
    else
        sqlite3 "$db_name" ".databases" >/dev/null 2>&1  # Create the database and suppress output
        if [ $? -eq 0 ]; then  # Check if the database creation was successful
            echo "Database '$db_name' created successfully."  # Inform the user that the database was created
        else
            echo "Error accessing database."  # Inform the user of an error
        fi
    fi
}

# Check if an argument is provided, use it as the database name
# If no argument is provided, default to "mydatabase.db"
if [ $# -gt 0 ]; then
    create_database "$1"
else
    create_database "mydatabase.db"
fi
