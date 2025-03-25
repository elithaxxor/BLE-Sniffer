
# NOTE: These are loud, and will print to console 

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
