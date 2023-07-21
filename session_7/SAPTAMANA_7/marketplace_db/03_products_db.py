"""
Interactiunea cu tabelul products
"""
import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# CRUD

# CREATE PRODUCT
# product_query = """
# INSERT INTO products (name, category, price, stock_count, description)
# VALUES (?, ?, ?, ?, ?);
# """
#
# products = [
#     ("birou negru", "mobilier", 120, 2, "birou negru descriere"),
#     ("pitic de gradina", "gradina", 56.99, 5, "pitic gradina descriere"),
#     ("ghiveci flori alb", "gradina", 25.45, 10, "ghiveci flori descriere")
# ]
#
# cursor.executemany(product_query, products)
# connection.commit()


# READ PRODUCT (BY ID)

# READ/GET ALL PRODUCTS

# UPDATE PRODUCT

# DELETE PRODUCT
