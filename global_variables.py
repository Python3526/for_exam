import psycopg2
from colorama import Fore

db_info: dict[str: str] = {'user': None,
                           'password': None,
                           'database': None,
                           'host': 'localhost',
                           'port': 5432}


def checker():
    try:
        if psycopg2.connect(**db_info):
            return True

    except Exception:
        return False
