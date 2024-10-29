import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150) NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY,
        title VARCHAR(100) NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250) NOT NULL,
        category_code VARCHAR(2),
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES store(store_id)
    );
''')

categories = [
    ('FD', 'Food products'),
    ('HC', 'Household chemicals')
]
cursor.executemany('''
    INSERT OR IGNORE INTO categories (code, title)
    VALUES (?, ?)
''', categories)

stores = [
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar')
]
cursor.executemany('''
    INSERT OR IGNORE INTO store (store_id, title)
    VALUES (?, ?)
''', stores)

products = [
    (1, 'Chocolate', 'FD', 10.5, 129, 1),
    (2, 'Bread', 'FD', 1.2, 200, 2),
    (3, 'Soap', 'HC', 2.5, 50, 1),
    (4, 'Milk', 'FD', 1.0, 150, 3),
    (5, 'Shampoo', 'HC', 5.0, 80, 2)
]
cursor.executemany('''
    INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id)
    VALUES (?, ?, ?, ?, ?, ?)
''', products)
import sqlite3


def display_stores():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()

    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

    connection.close()


def display_products_by_store(store_id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
    ''', (store_id,))

    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print()
    else:
        print("Продукты в этом магазине не найдены.")

    connection.close()


def main():
    while True:
        display_stores()
        try:
            store_id = int(input("Введите id магазина: "))
            if store_id == 0:
                print("Выход из программы.")
                break
            display_products_by_store(store_id)
        except ValueError:
            print("Пожалуйста, введите корректный id.")

# расскомментировать после создания таблицы
# if __name__ == '__main__':
#     main()

connection.commit()
connection.close()