import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
        price REAL NOT NULL DEFAULT 0.0 CHECK(price < 1000000000.00), -- Ограничение на 10 цифр
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

conn.commit()

def add_products():
    products = [
        ('Product 1', 10.99, 50),
        ('Product 2', 12.50, 30),
        ('Product 3', 8.75, 100),
        ('Product 4', 15.00, 20),
        ('Product 5', 7.60, 60),
        ('Product 6', 22.99, 10),
        ('Product 7', 5.00, 200),
        ('Product 8', 14.30, 15),
        ('Product 9', 9.90, 45),
        ('Product 10', 3.75, 150),
        ('Product 11', 11.00, 70),
        ('Product 12', 18.50, 25),
        ('Product 13', 20.00, 5),
        ('Product 14', 6.45, 80),
        ('Product 15', 4.99, 120),
    ]
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)
    ''', products)
    conn.commit()

def update_quantity_by_id(product_id, new_quantity):
    cursor.execute('''
        UPDATE products 
        SET quantity = ? 
        WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

def update_price_by_id(product_id, new_price):
    cursor.execute('''
        UPDATE products 
        SET price = ? 
        WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

def delete_product_by_id(product_id):
    cursor.execute('''
        DELETE FROM products 
        WHERE id = ?
    ''', (product_id,))
    conn.commit()

def select_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def select_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)

def search_products_by_title(search_term):
    cursor.execute('''
        SELECT * FROM products
        WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

add_products()
select_all_products()

print("\n")
update_quantity_by_id(1, 300)
select_all_products()

print("\n")
update_price_by_id(1, 15.99)
select_all_products()

print("\n")
delete_product_by_id(2)
select_all_products()

print("\n")
select_products_by_price_and_quantity(100, 5)

print("\n")
search_products_by_title('Product 1')

conn.close()