import psycopg2
from colorama import Fore


class DatabaseManager:
    """
    Database Manager class to manage database connections
    """

    def __init__(self, username, password, database):
        self.username = username
        self.password = password
        self.database = database

    def __enter__(self):
        self.conn = psycopg2.connect(user=self.username,
                                     password=self.password,
                                     database=self.database,
                                     host='localhost',
                                     port='5432')

        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Product")
        self.users = self.cursor.fetchall()
        for i in self.users:
            print(Fore.LIGHTCYAN_EX + str(i) + Fore.RESET)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
