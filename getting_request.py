import requests
import psycopg2
from global_variables import db_info, Fore

url = requests.get('https://dummyjson.com/products')

conn = psycopg2.connect(user=db_info["user"],
                        password=db_info["password"],
                        database=db_info["database"],
                        host=db_info["host"],
                        port=db_info["port"]
                        )
cur = conn.cursor()


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper


@commit
def create_table():
    creating_table_query = """DROP TABLE IF EXISTS Products;
    CREATE TABLE IF NOT EXISTS Products(
            id serial primary key ,
            title varchar(255) ,
            description text ,
            price int,
            discountPercentage float,
            rating float ,
            stock int,
            category varchar(200),
            thumbnail varchar(255),
            images TEXT
    );"""

    cur.execute(creating_table_query)


@commit
def insert_data():
    inserting_query = """INSERT INTO Products(title, description, price, discountPercentage, rating, stock, category, thumbnail,images)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    for product in url.json()['products']:
        data = (product['title'], product['description'], product['price'], product['discountPercentage'],
                product['rating'], product['stock'], product['category'], product['thumbnail'], str(product['images']))

        cur.execute(inserting_query, data)


def displaying_data():
    displaying_data_query = """SELECT * FROM Products;"""
    cur.execute(displaying_data_query)
    full_data = cur.fetchall()
    for data in full_data:
        print(Fore.MAGENTA, data, Fore.RESET, end='\n')
    print()
