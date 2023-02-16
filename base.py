import sqlite3
from pathlib import Path
def db_init():
    DB_NAME = 'db.sqlite'
    DB_PATH = Path(__file__)
    print(DB_PATH)
    db = sqlite3.connect(DB_PATH/DB_NAME)
    cur = db.cursor()

'''
CREATE TABLE products (
    product_id INT PRIMARY KEY,
        
)
'''