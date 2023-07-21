"""
Definim o clasa numita Calculator, care:
- va avea 2 atribute ale obiectului (in init): a, b
- metode:
    -- adunare -> va returna rezultatul adunarii dintre
atributele a si b
    -- scadere
    -- inmultire
    -- impartire
"""

class Calculator:

    # metoda de initializare / constructor
    def __init__(self, a, b):
        self.a = a # am definit atributul a care ia valoarea venita din constructor, din parametrul a
        self.b = b # am definit atributul b care ia ca valoare, valoarea parametrului b venit din constructor

    def adunare(self):
        return self.a + self.b

    def scadere(self):
        return self.a - self.b

    def inmultire(self):
        return self.a * self.b

    def impartire(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Nu se poate sa facem impartirea la 0 !!!"
        finally:
            return "S-a terminat operatia de impartire!"
