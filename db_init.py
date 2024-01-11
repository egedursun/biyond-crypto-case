import sqlite3

from server.clients.DBClients import SQLiteClient


def initialize_db(delete_existing_table=False):
    sql_client = SQLiteClient('db.sqlite3')
    try:
        with sql_client:
            if delete_existing_table:
                sql_client.execute("""
                    DROP TABLE IF EXISTS configurations;
                """)
            sql_client.execute("""
                CREATE TABLE IF NOT EXISTS configurations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    hyperparameters BLOB NOT NULL,
                    test_set BLOB NOT NULL
                );
            """)
    except sqlite3.Error as e:
        raise e

    # close connection
    sql_client.close()
    print('DB initialized successfully.')
    return
