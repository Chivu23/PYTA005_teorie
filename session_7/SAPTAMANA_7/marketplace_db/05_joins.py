"""
Join-uri:

Join-urile sunt comenzi SQL prin care putem combina/ lua simultan
datele din doua sau mai multe tabele, pe baza coloanei de legatura
(foreign key).

Tipuri de JOIN-uri:

1. INNER JOIN:
- obtinem inregistrarile care fac match la valori din ambele tabele.

2. LEFT (OUTER) JOIN:
- obtinem toate inregistrarile din tabelul din stanga +
inregistrarile din tabelul din dreapta care fac match

3. RIGHT (OUTER) JOIN:
- obtinem toate inregistrarile din tabelul din dreapta +
inregistrarile din tabelul din stanga care fac match

4. FULL (OUTER) JOIN:
- se returneaza toate inregsitrarile din ambele tabele, cand se
face match fie in tabelul din stanga, fie in tabelul din dreapta
"""

import sqlite3

connection = sqlite3.connect("marketplace.db")
cursor = connection.cursor()

# exemplu de inner join
# Am selectat id-ul comenzii si username-ul user-ului pentru
# acele inregsitrari din db in care se face match dupa foreign key
# customer_id (orders) = id (users)
#
# query = """
# SELECT orders.id, users.username
# FROM orders
# INNER JOIN users ON orders.customer_id == users.id;
# """

# cursor.execute(query)
#
# print(cursor.fetchall())
#
# # exemplu de left join
# # selectam id-ul comenzii, data comenzii, id-ul user-ului,
# # email-ul user-ului, facand un left join intre tabelul users
# # (tabelul din stanga) si tabelul orders (tabelul din dreapta)
# # Astfel vom obtine din db, toti userii cu datele cerute,
# # si doar datele despre comenzile in care se face match.
#
# query2 = """
# SELECT orders.id, orders.order_date, users.id, users.email
# FROM users
# LEFT JOIN orders ON users.id == orders.customer_id;
# """
# cursor.execute(query2)
# print(cursor.fetchall())

# Right join nu e suportat in sqlite3,
# dar putem inversa tabelele si folosim tot un left join
# si obtinem rezultatul dorit
# query2 = """
# SELECT orders.id, orders.order_date, users.id, users.email
# FROM orders
# LEFT JOIN users ON users.id == orders.customer_id;
# """
# cursor.execute(query2)
# print(cursor.fetchall())

