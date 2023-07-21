# class Car:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         print("Getter")
#         if self.__color is not None:
#             return self.__color.upper()
#         return "nu avem culoare"
#
#     # @color.getter
#     # def color(self):
#     #     print("Getter")
#     #     if self.__color is not None:
#     #         return self.__color.upper()
#     #     return "nu avem culoare"
#
#     @color.setter
#     def color(self, culoare_noua):
#         print("Setter")
#         self.__color = culoare_noua
#
#     @color.deleter
#     def color(self):
#         print("Deleter")
#         self.__color = None
#
#
#
# car1 = Car("rosu")
# print(car1.color)
#
# car1.color = "verde"
# print(car1.color)
#
# del car1.color
# print(car1.color)

class Person:

    def __init__(self, name, cnp, age, height):
        self.name = name
        self.__cnp = cnp # atribut privat
        self.age = age
        self.height = height

    @property
    def cnp(self):
        print("Getter cnp")
        return self.__cnp

    @cnp.setter
    def cnp(self, new_cnp):
        print("Setter cnp")
        if len(new_cnp) == 13:
            self.__cnp = new_cnp
        else:
            print("Invalid CNP value")


person1 = Person("George", "1970629204466", 26, 170)
print(person1.cnp)
person1.cnp = "1970629"
print(person1.cnp)
person1.cnp = "1970629204467"
print(person1.cnp)
# print(person1.__cnp)

