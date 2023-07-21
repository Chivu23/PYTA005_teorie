# Curs 5.1: Design Patterns

## 📝 OBIECTIVE
1. Sa intelegem ce sunt Design Patterns
2. Sa intelegem cum functioneaza si cand sunt folosite Design Patterns
3. Sa invatam ce categorii de Design Patterns exista:
- creational
- structural
- behavioral

## 📌 Design Patterns
- Design Pattern-urile ofera o solutie generala, reutilizabila pentru probleme comune
care apar in timpul dezvoltarii software-ului.
Pattern-ul, in general, arata relatia si interactiunea dintr clase
si obiecte.
- Reprezinta un set de "good practices" dupa care se ghideaza scrierea
de cod in OOP
- Ideea din spatele lor este sa accelereze timpul de dezvoltare
al unei aplicatii folosindu-se de paradigme deja bine testate si
utilizate in situatii similare.
- Practic sunt niste strategii independente pentru rezolvare de probleme
comune.
- Aceasta inseamna ca un design pattern reprezinta o idee, nu o
implementare particulara, iar folosindu-ne de ele, ne putem dezvolta
codul mult mai flexibil, reutilizabil si usor de intretinut.
- Scopul principal este sa intelegem care este scopul si utilitatea
la fiecare design pattern ca sa putem sa alegem si sa implementam codul in mod
corespunzator pe baza lui.
- Spre exemplu, in multe situatii din lumea reala, am dori sa cream
o singura instanta a unei clase, spre exemplu, poate sa fie un singur
presedinte activ al unei tari. Alt exemplu: dorim sa avem un singur manager de
configurare, sau un singur manager care gestioneaza erorile intr-o aplicatie,
decat sa avem manageri multipli etc => Singleton Design Pattern.

## 📌 Cele trei mari categorii de Design Patterns
1. Creational Design Pattern
- Aceste design patterns sunt despre instantierea de clase sau
creare de obiecte.
- Ele la randul lor pot fi categorisite in class-creational si
object-creational patterns.
- In timp ce class-creational utilizeaza in mod efectiv inheritance-ul
in instantierea de procese, object-creational pattern foloseste o delegare
eficienta a obiectelor.
- Ex: Factory Method, Abstract Factory, Builder, Singleton, Object Pool,
Prototype

2. Structural Design Pattern
- Aceste design patterns sunt folosite in organizarea de clase
si obiecte diferite pentru a forma o structura mult mai mare si sa
aduca o functionalitate noua.
- Ex: Adapter, Bridge, Composite, Decorator, Facade, Flyweight,
Private Class Data si Proxy.

3. Behavioral Design Pattern
- Aceste design patterns sunt despre identificarea tiparelor comune
de comunicare intre obiecte si realizarea acestor pattern-uri
- Ex: Chain of responsability, Command, Interpreter, Iterator,
Mediator, Memento, Null Object, Observer, State, Strategy, Template method,
Visitor.

## 📌 Exemplu Creation DP: Singleton DP
- pattern care permite crearea unei singure instante
a unei clase pe durata executiei programului.
- util in a limita accesul concurent la anumite resurse,
creand un punct de acces global (ex: accesul la o baza de date)

```python
class SingletonClass:
    __instance = None
    sector = "IT"
    
    def __init__(self, name):  
        # initializam attribute,
        # chemat in momentul instantei obiectului
        self.name = name
        
    def __new__(cls, *args):    
        # initializam clasa, metoda magica __new__
        # se apeleaza inaintea __init__
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    
obj1 = SingletonClass("JavaScript")
print(obj1.name)
print(obj1.sector)
print(obj1)
print(id(obj1))

obj2 = SingletonClass("Python")
print(obj2.name)
print(obj2.sector)
print(obj2)
print(id(obj2))

print(obj1.name)
print(obj1 == obj2)
print(obj1 is obj2)

obj3 = SingletonClass("Assembly")
print(obj1.name)
print(obj2.name)
print(obj3.name)
```

## 📌 Exemplu Structural DP: Proxy DP

- Proxy DP = pattern care controleaza si administreaza accesul
la obiectele pe care le protejeaza

```python
from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def drive(self):
        pass   
    
class Car(AbstractCar):
    def drive(self):
        print("You are driving the car.")
        
        
class Driver:
    def __init__(self, age):
        self.age = age
        

class ProxyCar(AbstractCar):
    def __init__(self, driver: Driver):
        self.car = Car()
        self.driver = driver
        
    def drive(self):
        if self.driver.age < 18:
            print("Sorry little driver, you are too young to drive.")
        else:
            self.car.drive()
            
driver = Driver(16)
print(driver.age)
# Daca instantiem direct clasa Car, 
# nu avem constrangere asupra varstei
car = Car()   
car.drive()

# Asa ca nu instantiem direct Car, ci instantiem ProxyCar, 
# aceasta verificand varsta soferului
proxy_car = ProxyCar(driver) 
proxy_car.drive()

new_driver = Driver(20)
proxy_car = ProxyCar(new_driver)
proxy_car.drive()
```

## 📌 Exemplu Behavioral DP: Observer DP
- pattern care permite definirea unui mecanism de observare intre obiecte,
ce permite trimiterea de notificari obiectelor "observator" (observer)
despre evenimentele noi ale obiectlui "observabil" (observable)

```python
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
```

##  🎓 INTREBARI INTERVIU
- Care este rolul unui design pattern?
- Care sunt tipurile de design patterns cunoscute si cand le folosim?




