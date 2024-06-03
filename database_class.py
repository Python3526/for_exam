import psycopg2
from global_variables import db_info
from colorama import Fore


class Product:
    def __init__(self, en_name, en_price, en_color, en_image):
        self.en_name = en_name
        self.en_price = en_price
        self.en_color = en_color
        self.en_image = en_image

        self.connection = psycopg2.connect(user=db_info["user"],
                                           password=db_info["password"],
                                           database=db_info["database"],
                                           host=db_info["host"],
                                           port=db_info["port"]
                                           )
        self.cursor = self.connection.cursor()

    def save(self):
        inserting_product_query = """INSERT INTO Product(name_, price, color, image)
                                     VALUES (%s, %s, %s, %s)"""

        data = (self.en_name, self.en_price, self.en_color, self.en_image)

        self.cursor.execute(inserting_product_query, data)
        self.connection.commit()
        print(Fore.LIGHTGREEN_EX + "Product inserted successfully✅" + Fore.RESET)
