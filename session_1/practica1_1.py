# print("Produsul acesta costa 5 lei.", end=",")
# print(3)
# functia print este o functie built-in din Python
# prin care putem afisa mesaje in consola
# vrem sa afisam trei culori
# print("rosu", "galben", "verde")
# print("portocaliu", "albastru", sep="*")

'''
Acesta este un comentariu
pe mai multe linii
'''

# declaram si initializam 2 variabile
# marca_masina = 'Volvo'
model_masina = 'XC 60'
#
# fructe_preferate_1 = "capsuni, struguri"
#
# my_var = 5
# print(my_var)

# my_Var = 10
# print(my_Var)

# print(my_var == my_Var)
# print(id(my_var))
# print(id(my_Var))

# suprascriere = atribuirea unei noi valori pentru o variabila deja definita

# declaram/initializam o variabila cu numele pret si valoarea 100
# pret = 100
# print(pret)

# suprascriem valoarea variabilei pret cu valoarea 200
# pret = 200
# print(pret)

# atribuim mai multe valori pentru mai multe variabile in aceeasi linie
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = "Orange"
# y = "Banana"
# z = "Cherry"


# atribuim aceeasi valoare pentru mai multe variabile in acceasi linie
# a = b = c = "Apple"
# print(a)
# print(b)
# print(c)

# a = "Apple"
# b = "Apple"
# c = "Apple"

# TIPURI DE DATE

"""
EX1: 
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""

# a.
latime = 130

# b.
descriere = 'descriere'

# c.
pret = 2.77
# pret = 100.0
discount = 34.55

# d.
initializat = True

# e.
# print(latime)
# print(descriere)
# print(pret)
# print(discount)
# print(initializat)

"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, 
de tip int, cu valoarea 10.
"""
# x = y = 10
# print("x:", x)
# print("y:", y)

"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste
doua variabile de tip string cu valori diferite.
"""
# nume, prenume = "Popescu","Marius"
# print(nume, end=" ")
# print(prenume)

# Concatenarea string-urilor

# v1
nume = "Popa"
prenume = "Maria"

# nume_complet = "Popa Maria"
nume_complet = nume + " " + prenume
print(nume_complet)

pret_produs = 25.5
# descriere_produs = "Produsul nostru costa 25.5 euro."
# descriere_produs = "Produsul nostru costa " + pret_produs + " euro." # => da EROARE!!
# pentru ca nu putem aduna/concatena string-uri cu int-uri

# v2 -> folosirea f-string-urilor

descriere_produs = f"Produsul nostru costa {pret_produs} euro."
print(descriere_produs)

nume_complet = f"{nume} {prenume}"
print(nume_complet)

"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""
nume = "Ionescu"
pret = "100"

# v1 - concatenare string-uri
# Ionescu a cumparat rosii de 100 de lei.
print(nume + " a cumparat rosii de " + pret + " de lei.")

# v2 - f-string-uri
print(f"{nume} a cumparat rosii de {pret} de lei.")

"""
EX6:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""

nume = "Ionescu"
varsta = 37

print(f"{nume} are {varsta} de ani.")