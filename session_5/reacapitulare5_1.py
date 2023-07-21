class forma_geometrica:
    pass

f1 = forma_geometrica()


class A:

    def __init__(self, param1):
        self.param1 = param1
        self._key1 = 0 # atribut protected
        self.__key2 = 0 # atribut private

    def metoda_1(self):
        print("Metoda 1")


class B(A):

    def __init__(self, param1, param2):
        self.param2 = param2
        super().__init__(param1)

    def metoda_1(self):
        # Metoda 1
        # Metoda 2

        print("Metoda 2")
        # super().metoda_1()

obj_a = A(param1="param1")
obj_a.metoda_1()
print(obj_a._key1)
# print(obj_a.__key2)
obj_b = B(param1="param1", param2="param2")
obj_b.metoda_1()

class Dreptunghi:

    def __init__(self, latime, lungime):
        self.latime = latime
        self.lungime = lungime

    def __calculeaza_arie(self):
        return self.latime * self.lungime

    def afiseaza_arie(self):
        arie = self.__calculeaza_arie()
        print(f"aria este {arie}")

dreptunghi1 = Dreptunghi(2, 3)
dreptunghi1.afiseaza_arie()
# dreptunghi1.__calculeaza_arie() # da eroare
#
# def func1(num):
#     return num + 25
#
# func1(5)
# print(num)

def func1(name, age=20):
    print(name, age)

func1("Emma", 25)
func1("Emma") # Emma 20


def func2():
    try:
        x = 5 / 2
        return "1"
    except ZeroDivisionError:
        return "2"
    finally:
        return "3"

print(func2())


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        return 'The animal is eating'

class Dog(Animal):

    def eat(self):
        return 'The dog is eating'

class Cat(Animal):

    def eat(self):
        return 'The cat is eating'

class Bird(Animal):

    def eat(self):
        return 'The bird is eating'


animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

# dog1 = Dog("Buddy")
# cat1 = Cat("Whiskers")
# bird1 = Bird("Tweety")
# animals = [dog1, cat1, bird1]

# colors = ["alb", "rosu", "verde"]
# for c in colors:
#     print(c)

for animal in animals:
    print(animal.eat())


