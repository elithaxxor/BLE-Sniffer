
```markdown
# Create Database Script

This repository contains scripts to create an SQLite database in various programming languages including Python, Bash, PowerShell, and C. The primary script discussed here is the Python script located in the `create_db/python/create_db.py` directory.

## Overview

The `create_db.py` script is designed to create an SQLite database if it doesn't already exist. This script is useful for initializing a new database file as part of a setup process for various applications.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Script Explanation](#script-explanation)
- [Additional Scripts](#additional-scripts)
  - [Bash Script](#bash-script)
  - [PowerShell Script](#powershell-script)
  - [C Program](#c-program)
- [Compilation Instructions](#compilation-instructions)
  - [On Windows](#on-windows)
  - [On Linux](#on-linux)
- [Contributing](#contributing)
- [License](#license)

## Usage

To use the `create_db.py` script, you need to have Python and SQLite3 installed on your system. You can run the script from the command line as follows:

```sh
python create_db.py [database_name]
```

- `database_name` (optional): The name of the database to create. If not provided, the default name `mydatabase.db` will be used.

## Script Explanation

The Python script performs the following steps:
1. Checks if a database file exists.
2. Creates the database if it doesn't exist and prints a success message.
3. If the database already exists, it informs the user.

```python
import sqlite3
import os
import sys

def create_database(db_name="mydatabase.db"):
    if os.path.exists(db_name):
        print(f"Database '{db_name}' already exists.")
    else:
        conn = sqlite3.connect(db_name)
        conn.close()
        print(f"Database '{db_name}' created successfully.")

if __name__ == "__main__":
    db_name = sys.argv[1] if len(sys.argv) > 1 else "mydatabase.db"
    create_database(db_name)
```

## Additional Scripts

### Bash Script

The Bash script performs the same functionality as the Python script. It checks if a database file exists, creates the database if it doesn't, and prints a success message.

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

### PowerShell Script

The PowerShell script also performs the same functionality. It checks if a database file exists, creates the database if it doesn't, and prints a success message.

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

### C Program

The C program performs the same functionality as the scripts. It checks if a database file exists, creates the database if it doesn't, and prints a success message.

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

## Compilation Instructions

### On Windows

#### Using MinGW (GCC)

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

#### Using Microsoft Visual Studio

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

### On Linux

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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` covers the usage, script explanations, additional scripts in different languages, compilation instructions for both Windows and Linux, and sections for contributing and licensing. It aims to be clear and comprehensive for any user looking to understand and use the `create_db` scripts.
