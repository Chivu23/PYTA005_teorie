# # # # Exemplu de set neordonat
# # # fruits = {"apple", "banana", "orange", "grape"}
# # # print(fruits)
# # # # Output: {'banana', 'apple', 'orange', 'grape'}
# # #
# # fruits = {"apple", "banana", "orange", "grape"}
# # print(fruits)
# #
# # # ADAUGAREA unui element in set
# #
# # # adaugarea unui element care nu exista in set
# # # in momentul adaugarii
# # fruits.add("watermelon")
# # fruits.add("Watermelon")
# # print(fruits)
# # # fruits.add([1, 2]) # da eroare
# #
# # # adaugarea unui element care exista in set
# # # in momentul adaugarii
# # fruits.add("apple")
# # print(fruits)
# #
# # # STERGEREA elementelor dintr-un set
# #
# # # stergerea unui element specific
# # fruits.remove("apple")
# # print(fruits)
# #
# # # stergerea unui element care NU exista in set
# # # fruits.remove("blueberry") # da eroare
# #
# # # stergerea unui element aleator
# # element_sters = fruits.pop()
# # print(element_sters)
# # print(fruits)
# #
# # # Putem adauga elemente MUTABILE intr-un set?
# # # fruits.add([1, 2]) # da eroare
# #
# # # Cum putem sa eliminam duplicatele dintr-o lista?
# #
# # cifre = [0, 0, 1, 2, 3, 2, 1, 4, 5, 5, 5]
# # cifre_set = set(cifre)
# # print(cifre_set)
# # print(list(cifre_set))
#
# """
# EX8: Se da setul: my_set = {1, 2, 3, 4}.
# a. Adauga nr 5 in set.
# b. Adauga nr 6 in set.
# c. Adauga nr 1 in set. Ce observi?
# d. Sterge un element din set folosind metoda remove().
# e. Sterge un element din set folosind metoda pop().
# """
#
my_set = {2, 5, 4, 1}
# # a.
# my_set.add(5)
# print(my_set)
#
# # b.
# my_set.add(6)
# print(my_set)
#
# # c.
# my_set.add(1)
# # 1 exista deja in set, motiv pentru care
# # nu se mai adauga din nou
# # seturile au elemente unice
# print(my_set)
#
# # d.
# my_set.remove(4)
# print(my_set)
#
# # e.
# element_sters = my_set.pop()
# print(element_sters)
# print(my_set)
# my_set.add(element_sters)
# print(my_set)
#
# print(len(my_set))
#
# """
# EX9:
# Se da urmatoarea structura de date:
# locatie = (44.34, 12.456)
# a. Verifica tipul structurii de date
# b. Este aceasta structura de date ordonata?
# c. Este aceasta structura de date mutabila?
# d. Determina lungimea structurii de date.
# e. Salveaza a doua valoare intr-o variabila.
# Verifica daca aceasta este mai mare de 13, si afiseaza
# un mesaj corespunzator.
# """
#
# locatie = (44.34, 12.456)
#
# # a.
# print(type(locatie))
#
# # b. Tuplurile -> ORDONATE
# print(locatie[0]) # 44.34
#
# # c. Tuplurile sunt IMUTABILE
#
# # d.
# print(len(locatie))
#
# # e.
# val2 = locatie[1] # al doilea element - 12.456
# if val2 > 13:
#     print("Val2 e mai mare decat 13")
# else:
#     print("Val2 nu e mai mare decat 13")
# print("here")

# CICLURI REPETITIVE

# while

# Exemplul 1 - Afisarea numerelor de la 0 la 3
# i = 0
#
# while i <= 3:
#     print(i) # 0 1 2 3
#     i += 1 # conditie de iesire din while

# Exemplul 3 - validarea credentialelor de conectare
# username = input("Introduceti numele de utilizator: ")
# password = input("Introduceti parola: ")
#
# while len(username) < 6 or len(password) < 6:
#     print("Username-ul si parola trebuie sa aiba min 6 caractere!")
#     username = input("Introduceti numele de utilizator: ")
#     password = input("Introduceti parola: ")
# print("Autentificare reusita")

# Exemplul 4 - ghicirea unui numar introdus la tastatura
# import random
#
# secret_number = random.randint(1, 10)
#
# guessed = False

# not False -> True
#
# while not guessed:
#     guess_number = int(input("Alege un numar de la 1 la 10: "))
#     if guess_number == secret_number:
#         print("Felicitari! Ai ghicit!")
#         guessed = True # conditia de iesire
#     elif guess_number < secret_number:
#         print("Numarul este prea mic. Incercati din nou.")
#     else:
#         print("Numarul este prea mare. Incercati din nou.")

# Exemplul 1 - Afisarea cifrelor de la 0 la 3
# i = 0
#
# while i <= 3:
#     print(i) # 0 1 2 3
#     if i == 2:
#         break # 0 1 2
#     i += 1
# else:
#     print("Am terminat ciclul repetitiv while.")


# FOR

# executam functia print de 4 ori
# for i in range(0, 4, 1):
#     # i este o variabila care va reprezenta
#     # pe rand, fiecare valoarea din range(4)
#     # adica 0, 1, 2, 3
#
#     # in loc de i putem pune orice alt nume
#
#     # avem acces la variabila i doar in interiorul for-ului
#     print(i)

"""
EX3: Afiseaza toate numerele pare pana la 10. 0-10)
"""

# v1 - numere PARE
# for numar in range(0, 11):
#     if numar % 2 == 0:
#         print(numar)

# v2 - numere PARE
# for numar in range(0, 11, 2):
#     print(numar)

# v1 - numar IMPARE
# for numar in range(0, 11):
#     if numar % 2 != 0:
#         print(numar)

# v2 - numar IMPARE
# for numar in range(1, 11, 2):
#     print(numar)

# Cum verificam daca un numar este prim

# nr_prim = int(input("Introduceti un numar: "))
#
# for i in range(2, nr_prim): # 2, 3, 4
#     if nr_prim % i == 0:
#         print(f"{nr_prim} nu este prim!")
#         break
# else:
#     print(f"{nr_prim} este prim!")

# continue

# for i in range(5): # 0 1 2 3 4
#     if i == 3:
#         continue
#     print(i)

# Cum putem sa iteram printr-o lista accesand
# la fiecare iteratie indexul elementului curent

# my_list = [1, "a", False, 12.5]
#
# for index in range(len(my_list)): # 0 1 2 3
#     print(index)
#     print(my_list[index])

# FOR EACH

my_list = ["produs1", "produs2", "produs3"]

for produs in my_list:
    print(produs)

# vrem sa accesam atat indexul cat si elementul direct
# dintr-o lista

for i, element in enumerate(my_list):
    print(i)
    print(element)

# Cum putem accesa si itera cheile dintr-un dictionar ?

my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# keys()
# print(my_dict.keys())

for key in my_dict.keys():
    print(f"key {key}")

# Cum accesam valorile dintr-un dictionar?
# values()

for value in my_dict.values():
    print(value)

# Cum accesam atat valorile cat si cheie dintr-un dictionar?
# items()

for cheie, valoare in my_dict.items():
    print(f"Cheie {cheie}")
    print(f"Valoare {valoare}")




