# Creational Design Pattern -> SINGLETON

# SINGLETON DP -> crearea unei singure instante a unei clase

class SingletonClass:
    __instance = None

    sector = "IT"

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance
#
# obj1 = SingletonClass("JavaScript")
# print(obj1.name)
# print(obj1.sector)
# print(obj1)
# print(id(obj1))
#
# obj2 = SingletonClass("Python")
# print(obj2.name)
# print(obj2.sector)
# print(obj2)
# print(id(obj2))
# print(obj1.name)

# Structural Design Pattern: PROXY DP

# from abc import ABC, abstractmethod
#
#
# class AbstractCar(ABC):
#
#     @abstractmethod
#     def drive(self):
#         pass
#
#
# class Car(AbstractCar):
#     def drive(self):
#         print("You are driving the car.")
#
#
# class Driver:
#     def __init__(self, age):
#         self.age = age
#
#
# class ProxyCar(AbstractCar):
#     def __init__(self, driver: Driver):
#         self.car = Car()
#         self.driver = driver
#
#     def drive(self):
#         if self.driver.age < 18:
#             print("Sorry little driver, you are too young to drive.")
#         else:
#             self.car.drive()


# driver = Driver(16)
# print(driver.age)
# Daca instantiem direct clasa Car,
# nu avem constrangere asupra varstei
# car = Car()
# car.drive()

# Asa ca nu instantiem direct Car, ci instantiem ProxyCar,
# aceasta verificand varsta soferului
# proxy_car = ProxyCar(driver)
# proxy_car.drive()
#
# new_driver = Driver(20)
# proxy_car = ProxyCar(new_driver)
# proxy_car.drive()

# BEHAVIOURAL DP - OBSERVER DP

class ObservablePerson:
    name = "Default User"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"I am {self.name}"

    def register_observer(self, observer):
        # inregistram un observer
        self._observers.append(observer)

    def notify_observers(self, message):
        # fiecare Observer este notificat
        # prin apelul functiei notify din clasa Observer
        for obs in self._observers:
            obs.notify(self, message)


class Observer:
    def __init__(self, name, observable):
        # in momentul instantierii Observerului, acesta este
        # inregistrat in lista de observeri ai obiectului Observable
        self.name = name
        observable.register_observer(self)

    def notify(self, observable, message):
        print(f"Observer: {self.name} Got message: {message}")
        print(f" from observable obj: {observable}")


subject = ObservablePerson()
observer_obj1 = Observer("obs1", subject)
observer_obj2 = Observer("obs2", subject)

# in momentul apelului ambele obiecte observer primesc notificare
subject.notify_observers("An event occured....")

class A:

    def __str__(self):
        return "I am object A"

obj_a = A()
print(obj_a)