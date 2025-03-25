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
