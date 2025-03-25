#!/bin/bash

create_database() {
    local db_name="$1"
    if [ -f "$db_name" ]; then
        echo "Database '$db_name' already exists."
    else
        sqlite3 "$db_name" ".databases" >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "Database '$db_name' created successfully."
        else
            echo "Error accessing database."
        fi
    fi
}

if [ $# -gt 0 ]; then
    create_database "$1"
else
    create_database "mydatabase.db"
fi
