
import sqlite3
from pathlib import Path

import cur as cur

import db


def db_init():
    DB_NAME = 'db.sqlite'
    DB_PATH = Path(__file__).parent.parent
    print(DB_PATH)
    db = sqlite3.connect(DB_PATH/DB_NAME)
    cur = db.cursor()

def create_tables():
    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
      product_id INT PRIMARY KEY,
      name TEXT,
      price INT,
      photo TEXT
     )""")

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS orders(
          order_id INT PRIMARY KEY,
          user_name TEXT,
          product_id INT,
          FOREING KEY (product_id)
               REFERENCES products(product_id)
               ON DELETE CASCADE
        """
    )

def delete_tables():
    cur.execute("""DROP TABLE IF EXISTS products""")
    db.commit()

def populate_products():
    cur.execute(
    """INSERT INTO products (name, price, photo) VALUES
                         ('book 1, 200, 'images/random.webp'),
                         ('book 2, 300,  'images/random.webp'),
    """)

def get_products():
    cur.execute("""SELECT * FROM products""")
    all_products = cur.fetchall()
    print(all_products)
    return all_products

if __name__ == "__main__":
    db_init()
    delete_tables()
    create_tables()
    populate_products()