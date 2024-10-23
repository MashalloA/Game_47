import sqlite3

db_name = 'Hw7.db'

def create_table(name, sql):
    try:
        with sqlite3.connect(name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def insert_product(product):
    sql = """INSERT INTO product (product_title, price, quantity)
    VALUES (?, ?, ?)"""
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as error:
        print(error)

def update_product(product):
    sql = """UPDATE product SET (product_title, price, quantity)
    VALUES (?, ?, ?)"""
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as error:
        print(error)

sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

# create_table(db_name, sql_to_create_products_table)
insert_product(("ds", 12.2, 123))
