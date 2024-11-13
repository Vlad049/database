import sqlite3


def create_db(name_db: str):
    try:
        sql_con = sqlite3.connect(name_db)
        cursor = sql_con.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS Pizzas (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            ingredients VARCHAR(200),
            price REAL
        );
        """
        print("Запит успішно сформовано")
        cursor.execute(query)
        sql_con.commit()
        print("Таблиця успішно створена")

    except sqlite3.Error as error:
        print("error: ", error)

    finally:
        cursor.close()
        sql_con.close()
        print("З'єднання з базою даних успішно завершене")


def add_pizzas(name, ingredients, price):
    try:
        sql_con = sqlite3.connect("Pizza.db")
        cursor = sql_con.cursor()

        query = """
        INSERT INTO Pizzas (name, ingredients, price) VALUES (?, ?, ?)
        """

        cursor.execute(query, (name, ingredients, price))
        sql_con.commit()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print("Помилка: ", error)

    finally:
        cursor.close()
        sql_con.close()
        print("Підключення успішно завершене")


def get_pizzas():
    try:
        sql_con = sqlite3.connect("Pizza.db")
        cursor = sql_con.cursor()

        query = """
        SELECT * FROM Pizzas;
        """

        return cursor.execute(query).fetchall()

    except sqlite3.Error as error:
        print("error: ", error)

    finally:
        cursor.close()
        sql_con.close()


create_db("Pizza.db")
# add_pizzas("Маргарита", "помідор, сир, соус, базилік", 150)
# add_pizzas("Пепероні", "соус, сир, салямі", 200)
# add_pizzas("Класична м'ясна", "салямі, сосиски, сир, соус", 220)