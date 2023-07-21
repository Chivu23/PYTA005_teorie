# definim o variabila string
culoare = 'rosu'
# afisam in consola tipul variabilei culoare
# print(type(culoare)) # <class 'str'>

# definim o variabila int
numar = 20
# print(type(numar))

# definim o variabila float
numar2 = 20.5
# print(type(numar2))

# definim o variabila bool
este_inmatriculata = True
# print(type(este_inmatriculata))

# TYPE CASTING

numar1 = 10
numar2 = '10'

# Sunt numar1 si numar2 de acelasi tip?
# print(type(numar1))
# print(type(numar2))

numar2 = int(numar2)
# print(numar2)
# print(type(numar2))

# my_str = "10euro"
# my_str = int(my_str) # -> da eroare: ValueError
# print(my_str)

# int -> str
numar1 = 10
# print("before", type(numar1))
numar1 = str(numar1) # '10'
# print("after", type(numar1))

# float -> str
numar2 = 25.5
# print("before", type(numar2))
numar2 = str(numar2) # '25.5'
# print("after", type(numar2))

# int -> float
numar3 = 120
numar3 = float(numar3) # -> 120.0
# print(numar3)

# float -> int
numar4 = 30.6
numar4 = int(numar4)
# print(numar4)

my_str = "Ana are mere"
# print(bool(my_str)) # True

my_str2 = ""
# print(bool(my_str2)) # False

my_str3 = None
# print(bool(my_str3)) # False

x = 5
# print(bool(x)) # True

y = 0
# print(bool(y)) # False

z = -5
# print(bool(z))

w = 0.0
# print(bool(w)) # False

a = 1.2
# print(bool(a)) # True

b = 2.0
# print(bool(b)) # True

"""
EX8: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""

# a.
a = 5
# print(a)

# b.
# print(type(a)) # <class 'int'>

# c.
b = float(a)
# print(b) # 5.0

# d.
# print(type(b)) # <class 'float'>

# FUNCTIA INPUT

# input() # apelam functia input fara parametrii
# nume = input("Cum te numesti?")
# print(f"Numele meu este {nume}.")
# print(type(nume))

# varsta = int(input("Care este varsta ta?"))
# print(f"Varsta: {varsta}")
# print(type(varsta))

"""
EX11: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
# pret = float(input("Ce pret are produsul? "))
# print(f"Pretul produsului este {pret}")

# STRING - caracteristici si metode disponibile


# INDEX
info = 'Afara sunt 2 grade'
# print(info[0]) # => 'A' (primul caracter din string se afla la indexul 0)
# print(info[1]) # => 'f'
# print(info[5]) # => ' ' (la indexul 5 avem un spatiu gol)

# accesam caracterul 'e' de la ultima pozitie din string

# v1 - index pozitiv
# print(info[17])

# v2 - index negativ
# print(info[-1])

# accesam penultimul caracter din string
# print(info[-2])

# LUNGIMEA
# info = 'Afara sunt 2 grade'

# afisam lungimea string-ului info
# print(len(info)) # => 18

# SLICING

info = 'Afara sunt 2 grade'

# Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
# print(info[0:2]) # => 'Af'

# Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
# print(info[0:5]) # => 'Afara'

# Daca nu specificam end_pos, se va extrage string-ul
# pana la ultimul caracter, inclusiv
# print(info[6:])  # => 'sunt 2 grade'

# Daca nu specificam start_pos, se va extrage string-ul
# incepand cu primul caracter.
# print(info[:5])  # => 'Afara'

# Inversare string
# print(info[::-1]) # => 'edarg 2 tnus arafA'

# Slicing intr-un string si sa iau elementele din doi in doi
# setand pasul ca fiind 2

cifre = "123456789"
# print(cifre[::2])
# print(cifre[0:5:2])
# print(cifre[:5:2])

"""
EX14: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""

prop3 = 'Concertul va avea loc maine.'
# a.
primul_cuvant = prop3[:9]
# print(primul_cuvant)

# b.
# print(primul_cuvant[0:3])

# c.
# print(prop3[::-1])

# metode ajutatoare string

# str1 = 'bAnAnA'
# print(str1.upper()) # => 'BANANA' (tot cu litere mari)
# print(str1.capitalize())  # => 'Banana'
# print(str1.lower())
# print(str1.count('A'))
# print(str1.count('a'))
# print(str1.count('A', 0, 3))
# print(str1.replace('A', 'a'))
# print(str1.find('A'))
# print(str1.find('x'))

# String-ul este ORDONAT si IMUTABIL

# STRING = ORDONAT -> elementele pot fi accesate dupa index
my_str = "abc"
print(my_str[0])
# STRING = IMUTABIL - > string-ul nu poate fi modificat
my_str = "aabbcc"
result = my_str.replace("a", "x")
print(result)
print(my_str)

# my_str[1] = 'x'
# print(my_str)
my_str = "cde" # suprascriem
print(my_str)

# OPERATORI

# OPERATORI ARITMETICI

x = 2
y = 3

# # adunarea
# suma = x + y
# print(x + y) # 5
# # # scaderea
# print(y - x) # 1
# # # inmultirea
# print(x * y) # 6
# # # impartirea
# print(y / x) # 1.5
# # # restul impartirii
# print(y % x) # 1
# # # ridicarea la putere
# print(x ** y) # 2 la puterea 3 -> 8
# # # floor division
# print(y // x) # 3 // 2; 1.5 => 1
#
# # inmultirea pe string-uri
# my_str = 'a'
#
# # vreau sa afisez mesajul 'aaa'
# print(my_str + my_str + my_str)
# print(my_str * 3)

# In cazul impartirii, indiferent daca rezultatul
# va fi un numar intreg (adica fara virgula) sau un numar
# zecimal, rezultatul impartirii in Python va fi de tip float

# print(10 / 2) # nu va fi 5, ci va fi 5.0 (mereu va fi float)

# floor division

# 1. floor division intre doua numere intregi
# print(3 // 2) # 1 => numar intreg

# 2. floor division intre doua numere si avem cel putin unul din ele
# ca fiind float
# print(3.0 // 2) # 1.0

# 3. floor division cand rezultatul este negativ (cand un numar din operatia
# floor division este negativ
# print(-3 // 2) # -3 / 2 = -1.5 => -2

# OPERATORI LOGICI

x = 2
print(x < 5 and x < 10) # True and True -> True
print(x > 6 and x < 10) # False and True -> False

y = 20
print(y > 1 or y < -5) # True or False - > True
print(y < 5 or y == 3) # False or False -> False

print(not True) # False
print(not False) # True

print(not 10 > 11) # True

a = 2
b = 10
print(a == 2) # True
print(a != b) # True
print(a > 5) # False
print(a < 4) # True
print(a >= 2) # True

# IF
x = 10
# if x == 5:
#     print("x este egal cu 5") # indentare cod
#     print("si asta")
# else:
#     print("x nu este egal cu 5")


x = 20
if x < 20:
    print("x este mai mic decat 20")  # indentare cod
elif x > 20:
    print("x e mai mare decat 20")
else:
    print("x e egal 20.")
print("final document")

# operatori de atribuire
x = 1

# +=
x += 3 # -> x = x + 3 => 1 + 3 => 4
print(x)

x -= 2 # -> x = x - 2 => 4 - 2 => 2
print(x)