# Curs 6: OOP (Programare orientata pe obiect)

## 📝 OBIECTIVE
1. Recapitulare
2. Ce este o clasa?
3. Ce este un obiect?
4. Ce sunt atributele/field-urile?
5. Ce sunt metodele?
6. Ce este un constructor?
7. Cum importam clase din alte fisiere?

## 🔥 <span style="color:orange;">OOP</span>

- <span style="color:#FF5733;">OOP</span> = <span style="color:#FF5733;">**Object-oriented programming** </span>
- <span style="color:#FF5733;">**Programare orientata pe obiect**</span> == modalitate 
prin care dezvoltam programe software, prin gruparea 
<span style="color:#FF5733;">**proprietatilor**</span> si 
<span style="color:#FF5733;">**comportamentelor**</span>
similare in **OBIECTE** individuale.
- **Programarea orientata pe obiect** ne ajuta astfel sa
transpunem in cod <span style="color:#FF5733;">**modele concrete, din viata reala,
sa le definim proprietatile si comportamentul,
cum interactioneaza intre ele**</span>.
**(masini, companii, angajati, studenti, scoli etc.)**
- **Exemplul 1**: un obiect poate reprezenta o 
<span style="font-size:20px">👨</span> **PERSOANA**.
Acest obiect poate fi caracterizat
de **PROPRIETATI** precum: **nume, varsta, adresa**, dar si
**COMPORTAMENT/ACTIUNI**: **se plimba, respira, alearga,
lucreaza** etc.
- **Exemplul 2**: un obiect poate reprezenta un 
<span style="font-size:20px">📧</span> **EMAIL**. 
Acest obiect poate fi caracterizat de **PROPRIETATI** precum:
**destinatar, subiect, continut mesaj**, dar si **COMPORTAMENT**:
**trimitere mail, adaugare atasament la mail**.
- **Exemplul 3**: un obiect poate reprezenta o 
<span style="font-size:20px">🚗</span> **MASINA**. Acest obiect poate
fi caracterizat de **PROPRIETATI** precum: **marca, model,
an fabricatie, culoare**, dar si **COMPORTAMENT**:**pornire masina,
accelerare, oprire**.


## 📌 <span style="color:orange;">CLASE</span> in Python

- Sa presupunem ca lucram la o reprezentanta auto:
Reprezentanta Auto DACIA. 
- Ne dorim sa tinem evidenta masinilor pe care le avem in reprezentanta.
- Dorim sa salvam detalii despre masini precum: model, pret, 
an fabricatie, culoare etc.

- VARIANTA 1: Folosirea structurilor de date: 
lista pentru fiecare masina
```python
masina_1 = ['Logan', 12000, 2012, 'rosu']
masina_2 = ['Duster', 18000, 2016, 'albastru']
masina_3 = ['Spring', 2019, 'alb']
```
❌ Care ar putea sa fie <span style="color:red">**problemele**</span> cu aceasta abordare in timp?
- Cu cat avem mai multe masini in reprezentanta, cu atat <span style="color:red">**va creste
fisierul**</span> in care salvam datele. Daca la un moment dat,
vei accesa masina_1[2], in alta parte decat imediat dupa definirea listei
masina_1, vei mai tine minte ca intr-adevar la indexul 2, pentru masina_1,
ai salvat anul fabricatiei?
- <span style="color:red">**NU avem consistenta**</span> in definirea proprietatilor masinilor.
Pentru masina_3, NU am salvat si pretul, pentru celalalte da.
Atunci accesand masina_3[1], vom obtine anul fabricatiei in loc de pret

💡 VARIANTA 2: Pentru a avea un cod consistent si mai usor de gestionat,
putem folosi **CLASE**.

### 📝 Ce este o <span style="color:orange;">**CLASA**</span>?
- O clasa este o <span style="color:orange;">**reteta**</span>
(<span style="color:orange;">**un blueprint**</span>) pentru
<span style="color:orange;">**crearea obiectelor**</span>.
- Ea contine **elemente descriptive/proprietati**: 
**atribute/fields** (practic niste variabile).
- Contine si **actiuni posibile/comportament**:
**metode** (practic niste functii).
- O clasă este creată folosind cuvântul cheie class. Atributele şi metodele 
clasei sunt listate într-un bloc de cod indentat.
- **Denumirea claselor**: cuvinte capitalizate (care incep cu litera mare)
legate intre ele. Exemple: SaleOrder, RentedCar, DeliveryOrder etc.

```python
class Car:
    # fields (atributtes)
    make = 'Dacia'
    model = None
    year = 2022
    color = None

    # methods
    def accelerate(self):
        print("Vrum vrrrum")
    
    def stop(self):
        print('STOP')
```

- Deci o clasa este doar un <span style="color:orange;">**concept**</span>,
cum ar fi reteta pentru <span style="font-size:20px">🍝</span> paste carbonara.
Faptul ca exista reteta nu inseamna ca exista si pastele.
- Dar aceeasi reteta o putem folosi ca sa facem 1, 2, 100 de portii carbonara.

- O clasa reprezinta o <span style="color:orange;">**structura logica**<span style="color:orange;">
care <span style="color:orange;">**defineste comportamentul si starea obiectelor**<span style="color:orange;">.
- Dupa definirea clasei, aceasta poate fi utilizata pentru **a crea obiecte de tipul respectiv**.

## 📌 Ce este un <span style="color:#286CC2">OBIECT</span>?
- <span style="color:#286CC2">**Obiect = instanta a clasei**</span>
- Toate obiectele de tip Car, vor avea acelasi comportament:

  - Aceleasi atribute
  - Aceleasi metode
  - Atributele pot suferi modificari dupa initializarea obiectului
  - Ex: o masina se poate vopsi intr-o culoare noua.

- Putem crea oricate obiecte de tip Car dorim.
- Acesta e si **avantajul OOP**: write once, use n times

```python
car1 = Car() # initializam obiecte de tip Car
car2 = Car() # car2 este instanta a clasei Car
print(car1.make) # dupa . avem acces la fields
print(car2.make)

car1.model = 'Duster' # putem suprascrie valori
car2.model = 'Logan'

car1.accelerate() # dupa . avem acces la metode
car2.accelerate()
car1.stop()
car2.stop()
```

## 📌 Ce sunt metodele?
- Metodele au o diferenta specifica fata de functiile
obisnuite: ele trebuie sa aiba un prefix suplimentar care trebuie
adaugat la inceputul listei de parametri, dar nu trebuie sa-i
dati o valoare cand apelati metoda. Python o va furniza.

## 📌 self
- Aceasta variabila speciala se refera la obiectul insusi (engl. self)
si prin conventie este numita self.
- Self - este instanta clasei, ajuta functia sa aiba acces la 
atributele/metodele clasei.
- Cand ne referim la membrii clasei, vom folosi self.membru.

## 📌 Ce este un constructor?
- Am invatat ca intr-o clasa putem sa definim atribute care vor caracteriza
obiecte de tipul clasei respective.
- Daca dorim ca atunci cand cream obiecte dintr-o clasa, sa setam
anumite atribute obligatoriu/ sa dam valori unor atribute, avem nevoie de
un constructor.
- **Constructorul** se asigura ca la crearea obiectelor setam niste
date fara de care obiectul nu are sens sa existe.
- Practic atribuim valori atributelor.
- Daca ne gandim la un formular, ar fi acele field-uri cu *
care sunt obligatorii.

### \_\_init__
- Metoda speciala \_\_init__() este apelata la instantierea unei clase
  (crearea unui obiect de tipul clasei) si poate fi asemanata unui constructor.
- Daca prin constructor suntem obligati sa dam model si color, nu am
putea sa instantiem obiecte de tip Car fara sa dam aceste valori obligatorii.

```python
class Car:
    # fields (attributes)
    make = 'Dacia'
    year = 2022

    def __init__(self, model, color):
        self.model = model
        self.color = color

car1 = Car('Duster', 'white')
car2 = Car('Logan', 'blue')

print(car1.make)
print(car1.model)
print(car1.color)
```

- Definirea clasei Complex

```python
class Complex:

    def __init__(self, real, imag):
        self.r = real
        self.i = imag

z = Complex(3.0, -4.5)
```
- Valorile furnizate intre paranteze sunt parametrii transmisi
functiei __init__. Aceasta va fi executata automat,
initializand proprietatile r si i ale obiectului cu valorile
3.0 si 4.5.
- Instanta clasei este retinuta in variabila z.

## 📌 Variabile de clasa, variabile de instanta

- Partea de date, atributele clasei, nu sunt altceva decat variabile
obisnuite care sunt legate de spatiile de nume ale claselor si obiectelor.
- Asta inseamna ca aceste nume sunt valabile doar in contextul
claselor si obiectelor respective.
- Din acest motiv, acestea sunt numite spatii de nume.
- Exista doua tipuri de campuri: variabile de clasa si variabile de obiect/instanta,
care sunt clasificate in functie de proprietarul variabilei.

1. VARIABILE DE CLASA (CLASS ATTRIBUTES) = sunt partajate, ele pot fi accesate
de toate instantele acelei clase. Exista doar un exemplar al variabilei
de clasa si cand o instanta (un obiect) ii modifica valoarea, aceasta
modificare este vazuta imediat de celalalte instante.
2. VARIABILE DE INSTANTA (OBJECT ATTRIBUTES) = proprietatea fiecarei instante a clasei.
In acest caz, fiecare obiect are propriul exemplar al acelui camp, adica
ele nu sunt relationte in niciun fel cu campurile avand acelasi nume in alte instante.

## 📌 Cum importam clase din alte fisiere?
- from folder.folder.fisier import nume_clasa
```python
from folder1.car import Car

car1 = Car('Duster', 'orange')
```

```python
"""
EX:
a. Defineste o clasa noua Dog.
b. Obiectele de tip Dog vor avea obligatoriu 2 atribute:
name si age.
c. Creeaza doua obiecte de tip clasa Dog, acceseaza atributele
si afiseaza-le.
d. Schimba atributul nume pentru unul din obiecte
si afiseaza-l din nou.
e. Creaza o metoda description, care returneaza
mesajul '{nume} is {age} years old'.
f. Folosind unul din obiectele instantiate la exercitiul
apeleaza metoda description, salveaza rezultatul
intr-o variabila si afiseaza variabila.
g. Clasa Dog este caracterizata si de atributul rasa.
Adauga acest atribut ca si un atribut al clasei (nu al obiectului)
h. Adauga o noua metoda in clasa Dog, numita speak,
care ia un parametru numit sound.
Metoda trebuie sa returneze mesajul "<name> says <sound>."
i. Apeleaza metoda speak pe unul din obiecte si afiseaza
rezultatul.
"""
```