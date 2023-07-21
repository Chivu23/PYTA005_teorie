# Curs 3: Structuri de date
## 📝 OBIECTIVE
1. Recapitulare Saptamana 1
2. Structuri de date: liste, dictionare, seturi, tupluri


## Recapitulare Saptamana 1
1. Cum putem sa luam datele introduse de utilizator de la tastatura?
2. Ce este un index in string?
3. Cum aflam lungimea unui string?
4. Ce inseamna slicing (string)?
5. Ce metode ajutatoare pentru variabile de tip string cunosti? (min 2)
6. Tipuri de Operatori: aritmetici, de atribuire, de comparare, logici
7. Conditia IF

## 📌 Lista
- Lista este o colectie de elemente. 
- Pastreaza mai multe valori intr-o singura variabila.
- Se defineste in Python folosind [], iar elementele sunt separate prin virgula.
- In Python, putem pastra diferite tipuri de date in aceeasi lista.

```python
list1 = ["abc", 34, True, 40, "male", "male"]
```

- Lista este **ORDONATA/ORDERED** (elementele sunt pastrate in ordinea in care au fost adaugate).

```python
# Exemplu de listă ordonată de numere întregi
numbers = [1, 2, 3, 4, 5]
print(numbers)
# Output: [1, 2, 3, 4, 5]
```
- Fiecare element din lista, are **INDEX**, incepand de la 0 (ca si string-ul)
- Lista este **MUTABILA/MUTABLE** (elementele sale pot fi modificate, adaugate sau sterse).

```python
# Exemplu de modificare a unui element dintr-o listă
numbers = [1, 2, 3, 4, 5]
numbers[2] = 7
print(numbers)
# Output: [1, 2, 7, 4, 5]
```

- In lista putem pune **VALORI DUPLICATE**
- len() ne va da dimensiunea listei (Cate elemente avem in lista?)

Alte exemple:

```python
lista_cumparaturi = ['rosii', 'paine', 'lapte']
print(type(lista_cumparaturi))
print(len(lista_cumparaturi))
print(lista_cumparaturi[0])
culori_preferate = ['rosu', 'galben', 'mov']
contacte = ['0722345678', '0721549888', '0765332967']
```

```python
list1 = ["abc", 34, True, 40, "male", "male"]
print(list1)
print(list1[0])
print(len[list1])
```

- Cum adaugam elemente noi in lista?
```python
cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]

# adaugam cifra 9 in lista cifre la finalul listei
cifre.append(9)
print(cifre)

# adaugam 9 in lista cifre la indexul 2
cifre.insert(2, 9)
print(cifre)
```

- Cum stergem un element din lista?

```python
cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]

# stergem ultimul element din lista
cifre.pop()
print(cifre)

# stergem elementul de la indexul 1 in lista cifre
element_sters = cifre.pop(1)
print(element_sters)
print(cifre)

# stergem prima aparitie a unui element in lista
# dupa valoare
cifre.remove(3)
print(cifre)
```

```python
"""
EX1: 
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""
```

```python
"""
EX2:
a. Defineste o lista numita filme_preferate, cu cel putin 3 elemente.
b. Inverseaza lista folosind slicing. (ca la string)
c. Folosind if, verifica daca lista este goala sau nu,
si afiseaza un mesaj corespunzator pentru fiecare situatie.
"""
```

```python
"""
EX3: Se da structura de date cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8].
a. Verifica tipul structurii de date dat.
b. Accesand metodele de pe lista, sorteaza lista cifre.
c. Verifica daca 9 este in lista cifre. Afiseaza un mesaj corespunzator.
"""
```

```python
"""
EX4: Exploreaza metodele ajutatoare ale listelor.
"""
```

## 📌 Dictionar
- Un dictionar este o colectie de perechi cheie:valoare.
- Se defineste folosind {} si are structura generala {key1:val1, key2:val2}

```python
my_dict = {
    'nume_produs': 'produs_1',
    'pret': 23.00,
    'in_stoc': False
}
```

- Dictionarul este **NEORDONAT/UNORDERED** (elementele nu sunt pastrate in ordinea in care au fost adaugate.)
- Dictionarul este **MUTABIL/MUTABLE** (elementele sale pot fi modificate, adaugate sau sterse).


- Cheile sunt **unice**, nu putem avea chei duplicate, ar crea confuzie.
- Ne gandim ca folosim nume pt un index.
- Putem folosi len() pentru a afla dimensiunea.


```python
my_dict = {
    "brand" : "Volvo",
    "model": "XC 60",
    "year": 2011
}

print(my_dict)
print(my_dict['brand'])
print(len(my_dict))
```

- Cum accesam elementele dintr-un dictionar? 

```python
contacte = {
    'Ana': '0722345678',
    'Marius': '0721549888',
    'Maria': '0765332967'
}

# dorim sa accesam numarul lui Marius
print(contacte['Marius'])

# dorim sa accesam numarul lui Alin
print(contacte['Alin']) # -> eroare: KeyError
print(contacte.get('Alin', 0))
```

```python
person = {
    "name": "John",
    "age": 30,
    "city": ["New York", "Los Angeles"],
    "occupation": "teacher"
}

# ADAUGAREA unui element nou in dictionar
# v1
person['salary'] = 3000.00
print(person)

# v2
person.update({"has_car": True})

# MODIFICAREA unui element in dictionar
# v1
person['age'] = 31
print(person)

# v2
person.update({"age": 32})

# STERGEREA unui element din dictionar
# v1
del person['city']
# del person['city'], person['salary'] # stergem mai multe key:value deodata
print(person)

# v2
# stergerea unui perechi cheie:valoare dupa cheie
person.pop("name")
print(person)
```

```python
"""
EX5: 
a. Defineste un dictionar, numit student1, cu urmatoarele chei:
nume, prenume, varsta, an_studiu, facultate, medie. 
Valorile le alegi tu.
b. Afiseaza lungimea dictionarului.
c. Printeaza prenumele studentului.
d. Adauga o noua pereche cheie-valoare, cu tara in care studiaza studentul.
e. Verifica daca dictionarul contine cheia oras.
"""
```

```python
"""
EX6:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
ingrediente, timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""
```

```python
"""
EX7:
a. Se da un dictionar cu contacte din agenda telefonica:
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
b. Aurel si-a schimbat numarul de telefon. Actualizeaza-l.
c. Ai obtinut numarul de telefon a lui Mihai. Adauga-l in contacte.
d. Maria a plecat in strainatate si nu mai are numar de telefon. Sterge-l.
e. Verifica daca ai numarul Mihaelei si afiseaza un mesaj corespunzator.
"""
```

## 📌 Set

- Set-urile pastreaza elemente **UNICE**.
- Seturile se definesc folosind {} si elementele sale sunt separate prin virgula.

- Set-urile sunt **NEORDONATE/UNORDERED** (elementele nu sunt pastrate in ordinea in care au fost adaugate si nu pot fi accesate dupa index.)

```python
# Exemplu de set neordonat
fruits = {"apple", "banana", "orange", "grape"}
print(fruits)
# Output: {'banana', 'apple', 'orange', 'grape'}
```

- Set-urile sunt MUTABILE/MUTABLE, pentru ca putem adauga si sterge elemente.
- Elementele din set sunt immutable.

```python
fruits = {"apple", "banana", "orange", "grape"}

# ADAUGAREA unui element in set

# adaugarea unui element care nu exista in set
# in momentul adaugarii
fruits.add("watermelon")
print(fruits)

# adaugarea unui element care exista in set
# in momentul adaugarii
fruits.add("apple")
print(fruits)

# STERGEREA elementelor dintr-un set

# stergerea unui element specific
fruits.remove("apple")
print(fruits)

# stergerea unui element aleator
fruits.pop()
print(fruits)

# Putem adauga elemente MUTABILE intr-un set?
# fruits.add([1, 2]) # da eroare
```

- Putem folosi len() pentru a afla dimensiunea set-ului

```python
culori = {'alb', 'rosu', 'galben'}
print(culori)
print(len(culori))
```

```python
"""
EX8: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
```

## 📌 Tuplu

- Pastreaza mai multe valori imutabile intr-o singura variabila.
- Se definesc folosind () si punem virgula intre elemente.
- TUPLU-urile sunt **ORDONATE/ORDERED** (elementele sunt pastrate in ordinea in care au fost adaugate si pot fi accesate dupa index.)
- TUPLU-urile sunt **IMUTABILE/IMMUTABLE** (elementele sale NU pot fi modificate, adaugate sau sterse).
- Accepta valori duplicate.
- Putem folosi len() pentru a afla dimensiunea

```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(len(my_tuple))
```

```python
"""
EX9:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""
```



