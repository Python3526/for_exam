import psycopg2

from global_variables import db_info, Fore


class ConnectWithDB:
    def __init__(self):
        self.connection = psycopg2.connect(user=db_info["user"],
                                           password=db_info["password"],
                                           database=db_info["database"],
                                           host=db_info["host"],
                                           port=db_info["port"]
                                           )

        self.cursor = self.connection.cursor()

        creating_table_query = """DROP TABLE IF EXISTS Product;
                                        CREATE TABLE IF NOT EXISTS Product(
                                        id SERIAL,
                                        name_ VARCHAR(50),
                                        price INTEGER,
                                        color VARCHAR(20),
                                        image VARCHAR(255)
                                        );"""
        self.cursor.execute(creating_table_query)
        self.connection.commit()

    def insert_product(self):
        en_name = input(Fore.BLUE + "Enter Product Name: ")
        en_price = input("Enter Product Price: ")
        en_color = input("Enter Product Color: ")
        en_image = input("Enter Product Image: " + Fore.RESET)

        inserting_product_query = """INSERT INTO Product(name_, price, color, image)
                                     VALUES (%s, %s, %s, %s)"""

        data = (en_name, en_price, en_color, en_image)
        self.cursor.execute(inserting_product_query, data)
        print(Fore.LIGHTGREEN_EX + "Successfully, Product Inserted✅\n" + Fore.RESET)

    def update_product(self):
        en_id = input(Fore.BLUE + "Enter Product ID: ")
        new_name = input("Enter New Product Name: ")
        new_price = input("Enter New Product Price: ")
        new_color = input("Enter New Product Color: ")
        new_image = input("Enter New Product Image: " + Fore.RESET)

        updating_product_query = """UPDATE Product 
                SET name_ = %s, price = %s, color = %s, image = %s WHERE id = %s"""

        data = (new_name, new_price, new_color, new_image, en_id)

        self.cursor.execute(updating_product_query, data)
        print(Fore.LIGHTGREEN_EX + "Successfully, Product Updated✅\n" + Fore.RESET)

    def delete_product(self):
        en_id = input(Fore.BLUE + "Enter Product ID: " + Fore.RESET)

        deleting_product_query = """DELETE FROM Product WHERE id = %s"""

        self.cursor.execute(deleting_product_query, (en_id,))
        print(Fore.LIGHTGREEN_EX + "Successfully, Deleted Product✅\n" + Fore.RESET)

    def display_products(self):
        displaying_products_query = """SELECT * FROM Product"""

        self.cursor.execute(displaying_products_query)
        full_data = self.cursor.fetchall()
        for i in full_data:
            print(Fore.MAGENTA, i, Fore.RESET, end='\n')
        print()

    def display_one_product(self):
        en_id = input(Fore.BLUE + "Enter Product ID: " + Fore.RESET)
        displaying_one_product_query = """SELECT * FROM Product WHERE id = %s"""

        self.cursor.execute(displaying_one_product_query, (en_id,))
        data = self.cursor.fetchall()
        print(data)
