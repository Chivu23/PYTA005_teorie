numar = int(input("Introdu un numar: "))
rezultat = 0
try:
    rezultat = 10 / numar
except ZeroDivisionError:
    print("Nu se poate face impartirea la 0.")
else:
    # OPTIONAL: se intra in blocul else doar daca nu s-a aruncat exceptie
    print("blocul else")
finally:
    # OPTIONAL: indiferent daca se arunca exceptie sau nu, acest
    # bloc este executat.
    print("finally se executa mereu")
print(rezultat)


from abc import ABC, abstractmethod


class CarABC(ABC):

    @abstractmethod
    def describe(self):
        pass

    def accelerate(self):
        return 50