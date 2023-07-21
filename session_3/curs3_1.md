# Curs 5: Functii

## 📝 OBIECTIVE
1. Recapitulare saptamana 2
2. Functii simple
3. Functii cu parametri
4. Functii cu return
5. Functii cu parametri si return
6. Functii din alte fisiere
7. Sa stim ce e o exceptie si cum o 'tratam'

## 📌 Functii - introducere
- **DEFINITIE**: O functie reprezinta un bloc de cod care se executa doar atunci cand este apelata.
- O functie este reutilizabila, ceea ce inseamna ca o putem folosi
in codul nostru ori de cate ori vrem, apeland-o.
Aceasta este si utilitatea ei principala: ne ajuta sa eliminam copierea/duplicarea codului in programul nostru.
- In Python, avem doua tipuri de functii:
1. Standard library functions - functii built-in care sunt disponibile
pentru utilizare (exemple: print, int, sum, max etc.).
2. User-defined functions - putem sa ne cream propriile functii care
sa indeplineasca propriile noastre cerinte/necesitati.

## 📌 Functii - sintaxa: Cum definim o functie in Python? Cum o apelam apoi?
- Sintaxa pentru a declara o functie in Python este urmatoarea:
```python
def function_name(parameters):
    # function body
```
- **def** = keyword folosit pentru declararea functiilor
- **function_name** = numele functiei
- **parameters** (optionali) = parametri dati la functie, disponibili in interiorul functiei
- A se observa ca indentarea este importanta si in cazul functiilor!
- Reguli pentru numele functiei: litere mici, cuvinte separate prin _.
- Exemplu:
```python
# functie simpla -> nu are parametri si nu returneaza nimic
def first_function():
    print("Hello World!")
```
- Pentru a apela o functie/ pentru a-i activa comportamentul, scriem
numele functiei urmat de paranteze rotunde.

```python
first_function()
```
- Ce se intampla cand apelam o functie?
1. Cand o functie este apelata, programul se duce la definitia functiei.
2. Codul din interiorul functiei se executa.
3. Programul nostru se continua de la linia de dupa apelarea functiei.

```python
"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""
```

## 📌 Ce este un parametru
- Parametri = datele de intrare (input) intr-o functie.
- Uneori functia are nevoie de niste date ca sa poata functiona.
- O functie poate sa aiba oricati parametri.
- Parametri sunt OPTIONALI.
- Daca avem mai multi, se despart de ,
- Practic sunt niste variabile declarate
dar neinitializate.
- Cand scriem logica functiei, in interiorul functiei, vom avea acces la
numele parametrilor, dar nu si la valorile lor.
- Acesti parametri primesc valori/sunt initializati cand apelam functia.
- Parametrii exista doar in interiorul functiei in care au fost definiti,
si singurul loc in care un parametru poate fi definit este in spatiul dintre paranteze
in def statement.
- Asignarea valorii unui parametru a unei functii se face in timpul invocarii/apelarii functiei,
specificand argumentul corespunzator.

### PARAMETRII vs ARGUMENTE
- Parametrii sunt in interiorul functiilor.
- Argumentele exista in afara functiilor si sunt purtatorii valorilor
parametrilor corespunzatori.

```python
# functie cu parametri care nu returneaza nimic

# functie cu 1 singur argument/parametru
def print_hi(user):
    print(f"Hi, {user}")

print_hi('Andy87')
print_hi('Andrei')
```

```python
# functie cu parametri care nu returneaza nimic

# functie cu doi parametri
def add_numbers(a, b):
    result = a + b
    print(f'Sum: {result}')

add_numbers(1, 2)
add_numbers(3, 4)
```

- Atentie! Cand definim o functie, trecem unul sau mai multi parametri
in semnatura sa. Atunci cand apelam functia, acelasi numar de valori (pentru fiecare parametru)
trebuie scris, altfel obtinem eroare!

```python
# functie cu parametri care nu returneaza nimic

# functie cu doi parametri
def add_numbers(a, b):
    result = a + b
    print(f'Sum: {result}')

add_numbers(1, 2)
add_numbers(3, 4)

add_numbers(1) # => EROARE!!
add_numbers(1, 2, 3) # => EROARE!!
```
- Cand apelam functia, putem sa scriem parametrii/argumentele pentru functie si
mentionand numele parametrilor la care le atribuim valoare.

```python
def add_numbers(a, b):
    result = a + b
    print(f'Sum: {result}')

add_numbers(a=1, b=2)
add_numbers(a=3, b=4)

```

```python
"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""
```

```python
"""
EX3: Scrie o functie care calculeaza patratul unui numar.
Afiseaza rezultatul.
"""
```

```python
"""
EX4: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""
```

## 📌 Ce este un return
- O functie poate sau nu sa returneze o valoare atunci cand este apelata.
- Altfel spus, folosim return cand functia ne si expune un raspuns (output).
- Raspunsul/output-ul primit de la o functie apelata se poate salva in variabile.
- Return e OPTIONAL
- Se poate returna orice tip de date cunoscut.
- In general, return e ultimul lucru in functie, 
deoarece aici se iese din functie.

```python
# functie cu return

def numar_preferat():
    numar = 7
    return numar
```
- Statement-ul return denota de asemenea si ca excutarea functiei
s-a oprit. Codul scris dupa return nu se va executa.

```python
def numar_preferat():
    numar = 7
    return numar
    print(f"{numar}") # !!! NU se va executa niciodata
```

- In general avem un singur return.
- Exceptie: cand folosim if else, 
atunci putem avea mai multe, 
dar oricum la rulare se va ajunge doar  
intr-un singur caz

```python

# functie cu parametri si return
def is_natural(numar):
    if numar >= 0:
        return 'numarul este natural'
    else:
        return 'numarul nu este natural'

raspuns = is_natural(3)
print(raspuns)
```

```python
"""
EX5: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""
```

```python
"""
EX6: Rescrie functia de la exercitiul 3, 
astfel incat sa returneze rezultatul.
"""
```

```python
"""
EX7: Rescrie functia de la exercitiul 4, 
astfel incat sa returneze rezultatul.
"""
```

```python
"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""
```

## 📌Functii din alte fisiere
- Atunci cand scriem un program, foarte des intalnim situatia in care
ne organizam codul in mai multe fisiere.
- Daca intr-un fisier am definit o functie si vrem sa invocam acea functie
in alt fisier, primul pas este sa o facem sa fie disponibila in fisierul
in care dorim sa o apelam, iar mai apoi o putem apela.

## 📌 Avantajele utilizarii functiilor
1. Reutilizarea codului
- Putem folosi acelasi functie de mai multe ori in programul nostru,
ceea ce face functia reutilizabila.
- Exemplu:
```python
def get_square(num):
    return num * num

for i in [1, 2, 3]:
    result = get_square(i)
    print(f'Square of {i} is {result}.')
```
2. Intelegerea si structurarea codului
- Functiile pot fi utilizate pentru a structura programul in blocuri
logice de cod mai mici, mai usor de gestionat. Acestea pot face codul mai clar
si mai usor de inteles.

## 📌 Exceptii in Python

- Exista situatii in care codul nu poate fi executat/apar erori.
- In aceste cazuri, codul 'arunca' o exceptie.

```python
# Exemplul 1:
x = 5 / 0  # ZeroDivisionError

# Exemplul 2:
my_dict = {'pret': 25.00, 'nume': 'perna'}
print(my_dict['culoare']) # KeyError
```

- Programatorii se pot astepta la ea, pot sa o 'prinda' si sa o 'trateze'
- In acest sens, putem anticipa erori si evitam sa 'crape' aplicatia
- Se foloseste sintaxa try/except
- else si finally sunt optionali

```python
try:
    # execute/run this code
    x = 5 / 0
except ZeroDivisionError:
    # execute this block when exception occured
    print("Can not divide by zero!")
else:
    # execute this block if no exception occured
    print("Yeah! Your answer is: ", x)
finally:
    # always execute this block of code
    print("This is always executed!")
```

- Uneori, dorim sa 'ridicam' noi o exceptie intentionat.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Al doilea parametru trebuie "
                                "sa fie diferit de 0.")
    return a / b

print(divide(1, 0))
```



