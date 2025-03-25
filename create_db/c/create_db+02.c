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
