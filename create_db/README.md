Here’s an engaging, visually rich, and creatively reformatted version of your README.md, complete with visuals, icons, and a more interactive style. This makes it more appealing and easier to follow:

⸻

Create SQLite Database – In Bash, PowerShell & C

Quick-start scripts for local database setup across platforms

⸻



<p align="center">
  <img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" width="300" alt="Database creation animation">
</p>




⸻

What’s Inside?

This repository gives you quick, plug-and-play scripts in Bash, PowerShell, and C to:
	•	Check if a SQLite database already exists
	•	Create one if it doesn’t
	•	Print a success or info message

⸻

1. Bash Script

Script Overview

Perfect for Linux/macOS or WSL users
Checks if the DB exists, creates it if not, and prints out a message.

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/bash.png" width="60"/>
</p>


<details>
<summary><strong>Click to view the Bash script</strong></summary>


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

# Use custom DB name if provided
if [ $# -gt 0 ]; then
    create_database "$1"
else
    create_database "mydatabase.db"
fi

</details>


How to Use

chmod +x create_db.sh
./create_db.sh custom_database.db



⸻

2. PowerShell Script

Script Overview

Ideal for Windows devs
Performs the same logic as the Bash version using PowerShell.

<p align="center">
  <img src="https://img.icons8.com/color/96/powershell.png" width="60"/>
</p>


<details>
<summary><strong>Click to view the PowerShell script</strong></summary>


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

if ($args.Count -gt 0) {
    Create-Database -dbName $args[0]
} else {
    Create-Database
}

</details>


How to Use
```powershell
.\create_db.ps1 custom_database.db
```


⸻

3. C Program

Script Overview

For those who want low-level control
Checks, creates, and logs using C + SQLite3.

<p align="center">
  <img src="https://img.icons8.com/color/96/c-programming.png" width="60"/>
</p>


<details>
<summary><strong>Click to view the C code</strong></summary>


#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <stdbool.h>

bool file_exists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file != NULL) {
        fclose(file);
        return true;
    }
    return false;
}

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

</details>




⸻

How to Compile and Run

Windows (Using MinGW)
	1.	Install MinGW
	2.	Add it to your system’s PATH
	3.	Compile:

gcc create_db.c -o create_db -lsqlite3

	4.	Run:

create_db.exe my_custom.db



⸻

Windows (Using Visual Studio)
	1.	Install Visual Studio
	2.	Create a new project and add create_db.c
	3.	Set up SQLite:
	•	Download SQLite from sqlite.org
	•	Add headers and link DLL
	4.	Build (Ctrl+Shift+B) and run (Ctrl+F5)

⸻
```bash
Linux
	1.	Install dependencies:

sudo apt update
sudo apt install gcc libsqlite3-dev

	2.	Compile:


gcc create_db.c -o create_db -lsqlite3

	3.	Run:

./create_db my_custom.db
```


⸻

Why Use This?
	•	Works across multiple platforms
	•	Helps you quickly bootstrap a SQLite DB for testing or dev
	•	Shows how to interface with SQLite in various languages

⸻



<p align="center">
  <img src="https://media.giphy.com/media/3o6ZsUk4kjJjSzcXJu/giphy.gif" width="400" alt="Success"/>
</p>




⸻

License

MIT

⸻

Would you like me to generate an actual animated demo GIF of the scripts running? Or convert this into a GitHub Pages-style landing page?

----------------
This shell script performs the same functionality as the original Python script:

    It defines a function create_database that takes the database name as an argument.
    It checks if a database file exists.
    It creates the database if it doesn't exist and prints a success message.
    If the database already exists, it informs the user.

You can run this script with an optional argument to specify the database name, like so:
bash

```bash 
  ./create_db.sh custom_database.db
```

This PowerShell script performs the same functionality as the original Bash script:

    It defines a function Create-Database that takes the database name as an argument.
    It checks if a database file exists.
    It creates the database if it doesn't exist and prints a success message.
    If the database already exists, it informs the user.

You can run this script with an optional argument to specify the database name, like so:
PowerShell

```powershell
    .\create_db.ps1 custom_database.db
```
