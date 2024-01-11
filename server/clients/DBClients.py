import sqlite3


class SQLiteClient:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # custom methods
    class Configurations:

        @staticmethod
        def add_configuration(name, description, hyperparameters, test_set):
            query = f"""
                INSERT INTO configurations (name, description, hyperparameters, test_set)
                VALUES (?, ?, ?, ?);
            """
            try:
                sql = SQLiteClient('db.sqlite3').cursor
                sql.execute(query, (name, description, hyperparameters, test_set))
                sql.connection.commit()
            except sqlite3.Error as e:
                raise e
            return

        @staticmethod
        def get_all_configurations():
            query = """
                SELECT id FROM configurations;
            """
            try:
                sql = SQLiteClient('db.sqlite3').cursor
                sql.execute(query)
            except sqlite3.Error as e:
                raise e
            try:
                data = sql.fetchall()
            except sqlite3.Error as e:
                raise e
            return data

        @staticmethod
        def get_configuration(configuration_id):
            query = f"""
                SELECT * FROM configurations
                WHERE id = {configuration_id}
            """

            try:
                sql = SQLiteClient('db.sqlite3').cursor
                sql.execute(query)
            except sqlite3.Error as e:
                raise e
            try:
                data = sql.fetchone()
            except sqlite3.Error as e:
                raise e
            return data

        @staticmethod
        def update_configuration(configuration_id, name, description, hyperparameters, test_set):
            query = f"""
                UPDATE configurations
                SET """
            if name:
                query += f"name = '{name}', "
            if description:
                query += f"description = '{description}', "
            if hyperparameters:
                query += f"hyperparameters = '{hyperparameters}', "
            if test_set:
                query += f"test_set = '{test_set}', "

            query = query[:-2]
            query += f"""
                WHERE id = {configuration_id}
            """
            try:
                sql = SQLiteClient('db.sqlite3')
                sql.execute(query)
            except sqlite3.Error as e:
                raise e
            return


        @staticmethod
        def delete_configuration(configuration_id):
            query = f"""
                DELETE FROM configurations
                WHERE id = {configuration_id}
            """
            try:
                sql = SQLiteClient('db.sqlite3')
                sql.execute(query)
            except sqlite3.Error as e:
                raise e
            return
