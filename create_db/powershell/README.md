
```markdown
# BLE-Sniffer: PowerShell Scripts for Database Creation

Welcome to the **BLE-Sniffer** project! This repository contains various scripts and tools to help you work with Bluetooth Low Energy (BLE) devices. In this directory, you will find PowerShell scripts designed to create and manage SQLite databases. This README provides detailed information about the scripts, their usage, and how to get started.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The PowerShell scripts in this directory are intended to facilitate the creation and management of SQLite databases. These scripts can be used to initialize databases for storing BLE sniffing data or any other application requiring a lightweight database solution.

## Features

- Creates an SQLite database file if it does not already exist.
- Checks if the database file already exists and informs the user.
- Handles errors gracefully and provides informative error messages.

## Prerequisites

Before you can use the PowerShell scripts, ensure that you have the following prerequisites installed on your system:

- PowerShell 5.1 or higher
- SQLite3

## Installation

1. **Clone the Repository**: Start by cloning the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/elithaxxor/BLE-Sniffer.git
   ```

2. **Navigate to the Script Directory**: Change to the directory containing the PowerShell scripts:
   ```bash
   cd BLE-Sniffer/create_db/powershell
   ```

## Usage

To use the PowerShell scripts, you can run them from the command line. The scripts accept an optional argument for the database name. If no argument is provided, they default to `mydatabase.db`.

### Basic Usage

```powershell
.\create_db.ps1 [database_name]
```

- `[database_name]` (optional): The name of the database file to be created. If omitted, the default name `mydatabase.db` will be used.

### Examples

1. **Create a Database with the Default Name**:
   ```powershell
   .\create_db.ps1
   ```
   Output:
   ```
   Database 'mydatabase.db' created successfully.
   ```

2. **Create a Database with a Custom Name**:
   ```powershell
   .\create_db.ps1 custom_database.db
   ```
   Output:
   ```
   Database 'custom_database.db' created successfully.
   ```

3. **Handle Existing Database**:
   If the database file already exists, the script will inform you:
   ```powershell
   .\create_db.ps1
   ```
   Output:
   ```
   Database 'mydatabase.db' already exists.
   ```

## Contributing

We welcome contributions to the BLE-Sniffer project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Create a pull request with a detailed description of your changes.

For more information, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file in the repository.
```
