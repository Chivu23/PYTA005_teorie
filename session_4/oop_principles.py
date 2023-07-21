# base class / parent class
class Chef:

    def __init__(self, experience):
        self.experience = experience

    def make_salad(self):
        print("salad")

    def make_fries(self):
        print("fries")


# child class - mosteneste din clasa Chef
# se trece intre paranteze numele clasei parinte
class JapaneseChef(Chef):

    def make_sushi(self):
        print("sushi")


# child class - mosteneeste din clasa Chef
# se trece intre paranteze numele clasei parinte
class ItalianChef(Chef):

    def make_pizza(self):
        print("pizza")


# chef1 = Chef(2)
# # chef1.make_sushi()
# chef1.make_salad()
# chef1.make_fries()
# print(chef1.experience)
#
# chef2 = JapaneseChef(15)
# chef2.make_sushi()
#
# chef2.make_salad()
# chef2.make_fries()
# print(chef2.experience)
#
# chef3 = ItalianChef(23)
# chef3.make_pizza()
# #
# chef3.make_salad()
# chef3.make_fries()
# print(chef3.experience)

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Animal {self.name} has {self.age} years old.")


class Dog(Animal):

    # Pentru a adauga proprietati noi:
    # 1. Extindem lista de parametrii pe care
    # metoda __init__ ii poate lua.
    # 2. Apelam __init__-ul din clasa parinte, folosindu-ne de
    # super(), cu parametrii pentrunecesari pentru clasa parinte.
    def __init__(self, name, age, sound, color):
        super().__init__(name, age)
        self.sound = sound
        self.color = color

    # Pentru a extinde metode din clasa parinte:
    # Facem apel la metoda din clasa parinte folosind super()
    def describe(self):
        super().describe()
        print(f"Animal's color is {self.color}.")
        print(f"He says: {self.sound}.")


animal = Animal(name="John", age=5)
# print(animal.age)
# print(animal.name)
# animal.describe()

dog1 = Dog(
    name="Max",
    age="12",
    sound="ham ham",
    color="black"
)

# print(dog1.name)
# print(dog1.age)
# print(dog1.sound)
# print(dog1.color)
#
# dog1.describe()

"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""


class Persoana:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descrie(self):
        print(f"Persoana {self.nume} are {self.varsta} ani.")


class Angajat(Persoana):

    def __init__(self, nume, varsta, salariu, post):
        super().__init__(nume, varsta)
        self.salariu = salariu
        self.post = post

    def afiseaza_salariu(self):
        return self.salariu

# POLIMORFISM

# Exemplu de class methods polimorfice
class Romania:
    def language(self):
        print("Romanian")


class USA:
    def language(self):
        print("English")


obj_ro = Romania()
obj_usa = USA()
#
# obj_ro.language()
# obj_usa.language()


def get_country_language(country_obj):
    country_obj.language()


# get_country_language(obj_ro)
# get_country_language(obj_usa)

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def describe(self):
        print("This animal is my favourite!")


class Dog(Animal):

    def sound(self):
        print("Ham ham")

    def sleep(self):
        print('ZZZZ')


class Cat(Animal):

    def sound(self):
        print("Miau miau")

    def sleep(self):
        print("Prrrr")


cat = Cat()
cat.sound()
cat.sleep()
cat.describe()

dog = Dog()
dog.sound()
dog.sleep()
dog.describe()


# Incapsulare

# class Car:
#
#     def __init__(self, brand, price):
#         self.__brand = brand # atribut privat
#         self._price = price # atribut protected
#
#     def run(self):
#         print(f"Please run {self.__brand}")
#
#
# car = Car("Dacia", 5000)
#
# # print(car.__brand) # -> eroare
# print(car._price)
# car.run()

class Car:
    __color = 'grey'

    def get_color(self):  # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita):  # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita


class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def get_password(self):
        return "*" * len(self.__password)

    def set_password(self, new_password):
        # Criterii de setare parola
        # - are cel putin o litera mare
        # - are cel putin un numar
        # - are minim 10 caractere
        if len(new_password) < 10:
            print("Parola noua trebuie sa aiba 10 caractere!")
            return
        for caracter in new_password:
            # if caracter == caracter.upper():
            #     break

            if caracter.isupper():
                break
        # for index in range(0, len(new_password)):
        #     if new_password[index] == new_password[index].upper():
        #         break
        self.__password = new_password

# my_str = "abc"
# my_str.isupper()

user1 = User("cosminabacter", "cosmina@gmail.com", "123")
print(user1.email)
print(user1.username)
# print(user1.__password)
print(user1.get_password())

user1.set_password("cosmina")
print(user1.get_password())
