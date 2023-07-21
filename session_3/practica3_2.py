# EXCEPTII
from Sesiunea_3.Sesiunea3_2.calculator import Calculator


# my_list = [1, 2]
#
# print(my_list[6])

# Exemplul 1:
# x = 5 / 0  # ZeroDivisionError

# Exemplul 2:
# my_dict = {'pret': 25.00, 'nume': 'perna'}
# print(my_dict['culoare']) # KeyError

# try:
#     # execute/run this code
#     x = 5 / 0
# except ZeroDivisionError:
#     # execute this block when exception occured
#     print("Can not divide by zero!")
# else:
#     # execute this block if no exception occured
#     print("Yeah! Your answer is: ", x)
# finally:
#     # always execute this block of code
#     print("This is always executed!")


# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Al doilea parametru trebuie "
#                                 "sa fie diferit de 0.")
#     return a / b
#
#
# print(divide(1, 0))

# OOP

# CLASE

# class Car:
#     # fields (atributtes) / atribute ale clasei
#     make = 'Dacia'
#     model = None
#     year = 2022
#     color = None
#
#     # methods
#     def accelerate(self):
#         print(f"Masina {self.make} face Vrum vrrrum")
#
#     def stop(self):
#         print('STOP')
#
# # cream o instanta a clasei Car
#
# car1 = Car()
#
# print(car1.year)
# print(car1.color)
# car1.color = "red"
# print(car1.color)
#
# car2 = Car()
# print("car2 color", car2.color)
#
#
# Car.color = "blue"
#
# car3 = Car()
# print("car3 color", car3.color)
#
#
# car1.accelerate()
#
# my_list = [1, 2]

class Car:
    # fields (attributes)/ atribute ale clasei
    make = 'Dacia'
    year = 2022

    # metoda de initializare/constructor
    def __init__(self, m, c):
        self.model = m # atribut al obiectului
        self.color = c # atribut al obiectului


car1 = Car('Duster', 'white') # positional args
car2 = Car('Logan', 'blue') # positional args

car3 = Car(m='Duster', c='red') # named args
# car3 = Car(c='red', m='Duster')

print(car3.color)

# car3 = Car('Duster')

print(car1.make)
print(car1.model)
print(car1.color)


# valori default pentru parametrii

# functii
def multiply(a, b=2):
    return a * b

print(multiply(1, 5))
print(multiply(4))

# clase

class Employee:

    def __init__(self, name, age, working_experience=0):
        self.name = name
        self.age = age
        self.working_experience = working_experience

    def describe(self):
        print(f"{self.name} lucreaza la aceasta companie de {self.working_experience} ani.")

employee1 = Employee("Ana",30,5)
employee1.describe()

student1 = Employee("Gelu",20)
student1.describe()
student1.working_experience = 2
print(student1.working_experience)
student1.describe()

class Complex:

    def __init__(self, real, imag):
        self.r = real
        self.i = imag

z = Complex(3.0, -4.5)

calc1 = Calculator(a=5, b=2)

print(calc1.a)
print(calc1.b)
print(calc1.adunare())
print(calc1.scadere())
print(calc1.inmultire())
# print(calc1.impartire())

calc2 = Calculator(a=20, b=0)
print(calc2.impartire())
