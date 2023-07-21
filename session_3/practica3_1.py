# my_list = [5, 10, 15, 25]
#
# list2 = my_list[::-1]
# list3 = list2[::2]
# print(list3) # output: 25, 10
# print(my_list[-2::-2]) # output: 15, 5
#
# # my_list[start_pos:end_pos:pas]
#
# my_list = ["a", "b", "c"]
#
# # for
# for index in range(len(my_list)):
#     print(my_list[index])
#
# # foreach
# for litera in my_list:
#     print(litera)
#
# result_list = []
#
# for number in range(0, 6):
#     print(number)
#     if number == 3 or number == 4:
#         continue
#     print(number)
#
#     result_list.append(number)
#
# print(result_list)
#
#
#

# FUNCTII

# functie simpla -> nu are parametri si nu returneaza nimic
# def first_function():
#     print("Hello World!")


# first_function() # apelul/invocarea functiei
# first_function()
# first_function()
# first_function()

"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""
from Sesiunea_3.Sesiunea3_1.func import multiply

# for number in range(1, 11):
#     print(number)


# def get_numbers():
#     for number in range(1, 11):
#         print(number)
#
# def get_numbers_2_5():
#     for number in range(2, 6):
#         print(number)


# get_numbers()

# def get_numbers(start, end):
#     for number in range(start, end):
#         print(number)
#
# get_numbers(1, 11)
# get_numbers(2, 6)

# functie cu parametri care nu returneaza nimic

# functie cu 1 singur argument/parametru
# def print_hi(user):
#     print(f"Hi, {user}")
#
# print_hi('Andy87')
# print_hi('Andrei')

# functie cu parametri care nu returneaza nimic


# functie cu doi parametri
# def add_numbers(a, b):
#     result = a + b
#     print(f'Sum: {result}')


# add_numbers(1, 2) # positional arguments
# add_numbers(3, 4)

# add_numbers(1) -> EROARE
#
# add_numbers(a=1, b=2)
# add_numbers(b=3, a=1)

# number1 = int(input("Introdu valoarea pentru a: "))
# number2 = int(input("Introdu valoarea pentru b: "))

# add_numbers(number1, number2)
# add_numbers(a=number1, b=number2)

# add_numbers(int(input("a: ")), int(input("b: ")))

"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""

# my_str = "abc"
# print(isinstance(my_str, int))

# functii cu return

# functie cu return


# def numar_preferat():
#     numar = 7
#     return numar
#     # print("hello")
#
# numar = numar_preferat()
# print(numar)


# functie cu parametri si return
# def is_natural(numar):
#     if numar >= 0 and isinstance(numar, int):
#         return 'numarul este natural'
#     else:
#         return 'numarul nu este natural'

# def is_natural(numar):
#     if numar >= 0 and isinstance(numar, int):
#         return 'numarul este natural'
#     return 'numarul nu este natural'


# raspuns = is_natural(3)
# print(raspuns)
#
# raspuns2 = is_natural(-2)
# print(raspuns2)
#
# raspuns3 = is_natural(2.5)
# print(raspuns3)

# raspuns4 = is_natural("abc") # da eroare: TypeError
# print(raspuns4)

"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""

print(multiply(2, 4))

