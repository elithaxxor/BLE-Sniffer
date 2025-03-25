

```markdown
# Create Database Script

This repository contains scripts to create an SQLite database in various programming languages including Bash, PowerShell, and C.

## Bash Script

### Description
The Bash script checks if a database file exists, creates the database if it doesn't, and prints a success message. If the database already exists, it informs the user.

### Script

```bash
#!/bin/bash

# Function to create a database
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

# Check if an argument is provided, use it as the database name
# If no argument is provided, default to "mydatabase.db"
if [ $# -gt 0 ]; then
    create_database "$1"
else
    create_database "mydatabase.db"
fi
```

### Usage
Run the script with an optional argument to specify the database name:
```sh
./create_db.sh custom_database.db
```

## PowerShell Script

### Description
The PowerShell script performs the same functionality as the Bash script: it checks if a database file exists, creates the database if it doesn't, and prints a success message. If the database already exists, it informs the user.

### Script

```powershell
# Function to create a database
function Create-Database {
    param (
        [string]$dbName = "mydatabase.db"
    )
    
    if (Test-Path $dbName) {
        Write-Output "Database '$dbName' already exists."
    } else {
        try {
            sqlite3 $dbName ".databases" | Out-Null
            Write-Output "Database '$dbName' created successfully."
        } catch {
            Write-Output "Error accessing database: $_"
        }
    }
}

# Check if an argument is provided, use it as the database name
# If no argument is provided, default to "mydatabase.db"
if ($args.Count -gt 0) {
    Create-Database -dbName $args[0]
} else {
    Create-Database
}
```

### Usage
Run the script with an optional argument to specify the database name:
```powershell
.\create_db.ps1 custom_database.db
```

## C Program

### Description
The C program performs the same functionality as the scripts: it checks if a database file exists, creates the database if it doesn't, and prints a success message. If the database already exists, it informs the user.

### Script

```c
#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <stdbool.h>

// Function to check if a file exists
bool file_exists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file != NULL) {
        fclose(file);
        return true;
    }
    return false;
}

// Function to create a database
void create_database(const char *db_name) {
    bool exists = file_exists(db_name);
    sqlite3 *db;
    int rc = sqlite3_open(db_name, &db);

    if (rc) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
    } else {
        sqlite3_close(db);
        if (!exists) {
            printf("Database '%s' created successfully.\n", db_name);
        } else {
            printf("Database '%s' already exists.\n", db_name);
        }
    }
}

int main(int argc, char *argv[]) {
    const char *db_name = "mydatabase.db";

    if (argc > 1) {
        db_name = argv[1];
    }

    create_database(db_name);

    return 0;
}
```

### Compilation and Usage

#### On Windows

##### Using MinGW (GCC)
1. **Install MinGW**: Download and install MinGW from the [MinGW official website](https://osdn.net/projects/mingw/releases/).
2. **Add MinGW to PATH**: Ensure that the `bin` directory of MinGW is added to your system's PATH environment variable.
3. **Compile the Program**: Open Command Prompt and navigate to the directory containing your `create_db.c` file. Run the following command to compile the program:
    ```sh
    gcc create_db.c -o create_db -lsqlite3
    ```
4. **Run the Program**: After compiling, you can run the program using:
    ```sh
    create_db.exe custom_database.db
    ```

##### Using Microsoft Visual Studio
1. **Install Visual Studio**: Download and install Visual Studio from the [Visual Studio official website](https://visualstudio.microsoft.com/).
2. **Open Visual Studio**: Open Visual Studio and create a new project.
3. **Add Existing Item**: Add your `create_db.c` file to the project.
4. **Set Up SQLite**:
    - Download the SQLite3 DLL and include files from the [SQLite download page](https://www.sqlite.org/download.html).
    - Include the SQLite3 header files in your project.
    - Link against the SQLite3 library (DLL).
5. **Compile and Run**:
    - Build the project by pressing `Ctrl+Shift+B`.
    - Run the program by pressing `Ctrl+F5`.

#### On Linux
1. **Install GCC and SQLite3 Development Libraries**: Open a terminal and install GCC and SQLite3 development libraries using the package manager:
    ```sh
    sudo apt-get update
    sudo apt-get install gcc libsqlite3-dev
    ```
2. **Compile the Program**: Navigate to the directory containing your `create_db.c` file. Run the following command to compile the program:
    ```sh
    gcc create_db.c -o create_db -lsqlite3
    ```
3. **Run the Program**: After compiling, you can run the program using:
    ```sh
    ./create_db custom_database.db
    ```
```

This `README.md` file includes instructions and scripts for creating an SQLite database in Bash, PowerShell, and C, along with compilation and usage instructions for Windows and Linux systems.
