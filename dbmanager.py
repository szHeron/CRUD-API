import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv("HOST_DB"),
  user=os.getenv("USER_DB"),
  password=os.getenv("PASS_DB"),
  database=os.getenv("DATABASE")
)

cursor = mydb.cursor()

def checkExistsTable():
  cursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'products'")
  value = cursor.fetchall()
  if(len(value) < 1):
    cursor.execute("CREATE TABLE products(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, section VARCHAR(255) NOT NULL, price DECIMAL(6,2) NOT NULL, available INT(4) DEFAULT 1)")

def addNewProduct(name, section, price, available):
  cursor.execute("INSERT INTO products (name, section, price, available) VALUES(%s, %s, %s, %s)", (name, section, price, available))
  mydb.commit()

def listProducts(id = -1):
  if id > 0:
    cursor.execute("SELECT JSON_OBJECT('id', id, 'name', name, 'section', section, 'price', price, 'available', available) FROM products WHERE id = {}".format(id))
    return cursor.fetchone()
  else:
    cursor.execute("SELECT JSON_OBJECT('id', id, 'name', name, 'section', section, 'price', price, 'available', available) FROM products")
    return cursor.fetchall()

def delProduct(id):
  cursor.execute("DELETE FROM products WHERE id = %s", (id))
  mydb.commit()

def updateProduct(id):
  cursor.execute("UPDATE products SET name WHERE id = {}".format(id))
  mydb.commit()