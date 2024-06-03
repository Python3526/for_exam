import sys
from global_variables import db_info, checker, Fore

while True:
    try:
        if not checker():
            db_info["user"] = input(Fore.GREEN + "Username: ")
            db_info["password"] = input("Password: ")
            db_info["database"] = input("Database name: " + Fore.RESET)

        if checker():
            print(Fore.LIGHTCYAN_EX + "\n1. Table Creating")
            print("2. Database CRUD")
            print("3. Alphabet Iterator")
            print("4. Working with Threads")
            print("5. Product Attributes")
            print("6. Context Manager")
            print("7. Getting Requests")
            print("8. Change the Database")
            print("9. Exit")
            choice = input("..." + Fore.RESET)
            if choice == "1":
                from working_with_db import ConnectWithDB

                ConnectWithDB()
                print(Fore.LIGHTBLUE_EX + 'SUCCESSFULLY, TABLE CREATED✅', Fore.RESET)

            elif choice == "2":
                from working_with_db import ConnectWithDB

                obj1 = ConnectWithDB()
                while True:
                    inner_choice = input(Fore.CYAN + "1. Create a new product\n2. Update Product\n3. Delete Product"
                                                     "\n4. Display Products\n5. Display specific product"
                                                     "\n6. Back\n..." + Fore.RESET)

                    if inner_choice == "1":
                        obj1.insert_product()
                    elif inner_choice == "2":
                        obj1.update_product()
                    elif inner_choice == "3":
                        obj1.delete_product()
                    elif inner_choice == "4":
                        obj1.display_products()
                    elif inner_choice == "5":
                        obj1.display_one_product()
                    elif inner_choice == "6":
                        break
                    else:
                        print(Fore.RED + "Enter a valid option\n" + Fore.RESET)


            elif choice == "3":
                from iterator import FullAlphabet

                obj2 = FullAlphabet(int(input(Fore.BLUE + "Enter number of letters: ")),
                                    int(input("Enter Step: " + Fore.RESET)))

                for i in obj2:
                    print(i, end='    ')
                print()

            elif choice == "4":
                from working_with_threads import start_threads

                start_threads()

            elif choice == "5":
                from database_class import Product

                obj3 = Product(input(Fore.BLUE + "Enter Product Name: "), input("Enter Product Price: "),
                               input("Enter Product Color: "), input("Enter Product Image: " + Fore.RESET))
                obj3.save()

            elif choice == "6":
                from context_manager import DatabaseManager

                with DatabaseManager(db_info["user"], db_info["password"], db_info["database"]) as db:
                    db


            elif choice == "7":
                from getting_request import create_table, insert_data, displaying_data

                create_table()
                insert_data()
                displaying_data()
                print(Fore.LIGHTBLUE_EX + 'SUCCESSFULLY, ALL DATA INSERTED✅', Fore.RESET)

            elif choice == "8":
                db_info["user"] = None
                db_info["password"] = None
                db_info["database"] = None
                print(Fore.LIGHTYELLOW_EX + "\nNow, You can enter into a new database" + Fore.RESET)

            elif choice == "9":
                print(Fore.LIGHTGREEN_EX + "Thanks for using this🫡" + Fore.RESET)
                sys.exit()

            else:
                print(Fore.RED + "Pls, enter a valid option\n" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "Error while connecting to PostgreSQL\n", Fore.RESET)


    except Exception as err:
        print(Fore.LIGHTRED_EX + "Smth went wrong❗" + Fore.LIGHTYELLOW_EX + "Check this: {}\n".format(err))
