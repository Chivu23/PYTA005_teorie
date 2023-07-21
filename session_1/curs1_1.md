# Curs 1: Variable, tipuri de date
## 📝 OBIECTIVE
1. Setup functional
2. Principii de baza in programare
3. Primul meu program Python
4. Print statement
5. Comentarii
6. Variabile
7. Cele mai uzuale tipuri de date
8. Type casting
9. Intro in operatori
10. Input statement
11. Complexitatea unui string (index, length, metode ajutatoare)

## 📌 Principii de baza in programare
- A compila = a traduce din 'human reading syntax' in 'machine language'
- Codul se interpreteaza secvential, linie cu linie, de sus in jos.
- Machine language = binary code (cod binar) - combinatii diferite de 0 si 1.
- Principiul seamana cu cel din codul morse. Pentru 1 se transmite un impuls electric, pentru 0 o pauza.
- 1 bit = memorie in care incape doar o singura valoare. 1 (true), 0 (false).
- 1 Byte = 8 biti. Numere intre 0 (000000) si 255 (111111).
- 1 Kilobyte = 1.024 bytes
- 1 Megabyte = 1.024 kilobytes (1.048.575 bytes)
- Terminal = zona in care trimitem instructiuni catre program (altele decat cod python).
Exemplu: 'python --version'.
Tot de aici putem instala librarii externe (ex: pip install selenium).
- Consola = zona in care primim output (raspuns vizual) de la programul rulat.
- IDE = Integrated Development Environment - Pycharm. Este un editor de cod.
- Venv = Virtual Environment - zona in care folosim in mod izolat si securizat toate librariile externe.

## 📌 Limbaj compilat vs limbaj interpretat
- limbaj compilat = transformarea codului din sintaxa citibila in cod citibil de procesor
    - codul e transformat (compilat) in limbaj masina iar ulterior rulat
    - limbaj compilat: Java
- limbaj interpretat = codul e citit la momentul executiei linie cu linie si transformat in cod masina "on the go"
    - limbaj interpretat: Python
    - in Python, interpretorul Python citeste codul linie cu linie si il transforma in cod masina in momentul executiei

## 📌 Primul meu program Python
Afisarea in terminal a mesajului "Hello World".

```python
print("Hello World")
```

## 📌 Functia built-in print()

❔ Ce este o functie?
- O functie este o logica de cod predefinita care face ceva.
- Are sintaxa **nume_functie()**
- In paranteza punem datele de intrare/ input (argumente sau parametri)
- Vom discuta pe larg despre functii in capitolele urmatoare.

🔸 Functia print(), afiseaza in consola ce punem in paranteze.

```python
print("Produsul acesta costa 5 lei.")
```

```python
print(3)
print(3.5)

print("rosu", "galben")
print("verde", "albastru", sep=",")

print("text1", end="*")
print("text2", end="*")

print("text3", "text4", sep=",", end="***")
```

## 📌 Comentarii
### 🔸 Definitie
- Comentariile sunt linii de cod care sunt ignorate in timpul rularii unui program.

### 🔸 Tipuri de comentarii
In Python, comentariile sunt definite folosind semnul '#' la inceputul liniei de cod.

#### *Single-line comments*
- Exemplu
```python
# Acesta este un comentariu pe o singura linie
```

#### *Multi-line comments*
- Exemplu 1:
```python
# Acesta este un comentariu
# pe mai multe linii
```

- Exemplu 2:
```python
"""
Acesta este alt comentariu
pe mai multe linii
"""
```

### 🔸 De ce avem nevoie de comentarii?
- Documentarea codului
- Cresterea intelegerii codului
- Prevenirea executarii uneia sau mai multor linii de cod.

## 📌 Variabile: definitie, de ce avem nevoie de variabile
### 🔸 Definitie
- O variabila este un container din memorie care stocheaza valori.
- Va puteti imagina o cutiuta, pe care punem o eticheta.

```python
# declaram si initializam 2 variabile
marca_masina = 'Volvo'
model_masina = 'XC 60'
```
### ❗ De retinut
- Variabilele au un nume unic, ca sa poata fi identificate si folosite anterior.
- Variabila este creata in momentul in care ii atribuim o valoare.
- NU putem pune spatiu in numele unei variabile.
- Variabilele incep cu litera mica dar pot contine cifre (user1) si simbolul _.
- Variabilele sunt CASE-SENSITIVE (my_var = 5 e diferita de my_Var = 5).
- Variabilele pot sa isi schimbe valoarea pe parcursul executiei programului (suprascriere).
- Variabilele pot sa isi schimbe tipul de date pe parcursul executiei.
- Putem atribui mai multe valori in one line, sau aceeasi valoare mai multor variabile.
```python
x, y, z = "Orange", "Banana", "Cherry"
a = b = c = "Apple"
```
## 📌 Tipuri de date: string, int, float, bool
- Datele/valorile salvate in variabile pot avea mai multe tipuri
- Exista mai multe tipuri de date dar cele mai importante/folosite sunt:
1. int = numar intreg
```python
# initializam o variabila de tip int/numar intreg
cantitate = 10
```
2. float = numar zecimal
```python
# initializam o variabila de tip float/numar zecimal
pret = 10.45
```
3. bool = adevarat/fals
```python
# initializam variabile de tip boolean
este_impar = False
este_par = True
```
4. string = sir de caractere de la tastatura delimitate de '  ' sau "  "
```python
# definim o variabila string folosind ghilimele simple
nume = 'Popa'

# definim o variabila string folosind ghilimele duble
prenume = "Maria"
```

```python
"""
EX1: 
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
```

```python
"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""
```

```python
"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.
"""
```

📌 Concatenarea string-urilor
- Putem concatena string-uri in doua moduri:
    - cu semnul "+"
    - folosind f-strings
```python
nume = 'Bacter'
print(nume)

prenume = 'Cosmina'
print(prenume)

nume_complet = nume + prenume
print(nume_complet)
print('Numele meu este ' + nume + prenume)

varsta = 20
# print("Varsta mea este de:" + varsta) # da eroare
print(f"Varsta mesa este de: {varsta}") 
```

```python
"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""
```

```python
"""
EX6:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""
```

## 📌 Functia built-in type()
- Functia type ne expune tipul de date al variabilei date ca input.

```python
# definim o variabila string
culoare = 'rosu'
# afisam in consola tipul variabilei culoare
print(type(culoare)) # <class 'str'>
```

- Convertirea tipurilor de variabile - type casting
```python
numar1 = 10
numar2 = '10'

# Sunt numar1 si numar2 de acelasi tip?
```
Functiile int(), str(), bool(), float() schimba tipul de date.

```python
"""
EX7:
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
"""
```

```python
"""
EX8: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""
```

```python
"""
EX9:
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
"""
```


## 📌 Functia built-in input()
- Functia input() ne ajuta sa luam date de la tastatura si sa le salvam intr-o variabila.
- Daca nu facem type casting, default-ul datelor furnizate de utilizator for fi te tip string.
- Ulterior putem accesa valorile salvate in variabile dupa necesitate.

```python
nume = input('Cum te numesti? ') # default - string
varsta = int(input('Cati ani ai? ')) # fortam varsta sa fie un int
```

```python
"""
EX10: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
```

```python
"""
EX11: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
```


## 📌 Tipul string - metode disponibile

### 🔸 Index
- String-ul este format din unul sau mai multe caractere.
- Fiecare caracter dintr-un string are un numar asociat/pozitie asociata, numit index.
- ❗ ATENTIE: indexul incepe de la 0.
- Exemplu:
```python
info = 'Afara sunt 2 grade'
print(info[0]) # => 'A' (primul caracter din string se afla la indexul 0)
print(info[1]) # => 'f'
print(info[5]) # => ' ' (la indexul 5 avem un spatiu gol)
```
- Cum aflam ce caracter avem la ultima pozitie din string?
```python
info = 'Afara sunt 2 grade'
# prima varianta - e o modalitate dar NU e indicata - DE CE?
print(info[17]) # => e

# a doua varianta (PREFERATA)
print(info[-1]) # => e
```

```python
"""
EX12: Se da variabila prop1 = 'Andy este prescurtarea de la Andrei"
a. Afiseaza primul caracter.
b. Afiseaza al 4-lea caracter.
c. Afiseaza ultimul caracter.
"""
```

### 🔸 Lungimea unui string
- Functia len() ne spune cate caractere are string-ul.
```python
info = 'Afara sunt 2 grade'

# afisam lungimea string-ului info
print(len(info)) # => 18
```

```python
"""
EX13: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""
```

### 🔸 Slicing
- Putem accesa "felii" din string, folosind sintaxa
**my_str[start_pos:end_pos:pas]**
- Practic, extragem o parte dintr-un string, specificand indexul de la care sa pornim
si indexul final.
- start_pos = indexul de inceput (inclusiv); daca lipseste, este inceputul
string-ului (0)
- end_pos = indexul de final (EXCLUSIV)
- ❗ ATENTIE: Caracterul de la indexul final nu se va lua in considerare.
Practic vom extrage un string care va include ca ultimul caracter, cel aflat la **end_pos** - 1.
- pas = este optional - pasul cu care se merge; daca lipseste, valoarea lui
este 1
- daca pasul este negativ, se merge invers (de la final la inceput)
```python
info = 'Afara sunt 2 grade'

# Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
print(info[0:2]) # => 'Af'

# Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
print(info[0:5]) # => 'Afara'

# Daca nu specificam end_pos, se va extrage string-ul
# pana la ultimul caracter, inclusiv
print(info[6:])  # => 'sunt 2 grade'

# Daca nu specificam start_pos, se va extrage string-ul
# incepand cu primul caracter.
print(info[:5])  # => 'Afara'

## Inversare string
print(info[::-1]) # => 'edarg 2 tnus arafA'
```

```python
"""
EX14: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""
```


### 🔸 Metode ajutatoare string
- Daca dupa my_str punem . ajungem la functiile ajutatoare.
- Exemple: upper, lower, replace, count etc.
- Accesam descrierea acestora apasand CTRL + Click pe numele lor

```python
str1 = 'banana'
print(str1.upper()) # => 'BANANA' (tot cu litere mari)
```

```python
"""
EX15: Se da string-ul my_str = 'vacanta'.
a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.
c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.
d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
"""
```

```python
"""
EX16: Exploreaza urmatoarele metode ajutatoare ale string-ului:
a. endswith()
b. index()
c. lower()
d. replace()
e. strip()
"""
```
