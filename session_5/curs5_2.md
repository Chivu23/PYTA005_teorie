# Curs 5_2: Iteratori, generatori, context managers, decoratori
## 📝 OBIECTIVE

1. Iteratori
2. Generatori
3. Context Managers
4. Decoratori

## 📌 Iteratori

Iterable vs Iterators

- Un interabil este un obiect prin care putem itera (cu for si while loops)
- ex: lista, dict, tuplu, string etc

```python
lst = ['a', 'b', 'c']
for x in lst:
    print(x)
    # avem 3 iteratii: x = 'a', x = 'b', x = 'c'
```

```python
nums = [1, 2, 3]

for num in nums:
    print(num)
```
- Cum ne dam seama daca un obiect este iterabil sau nu/
Cum ne dam seama daca putem folosi cicluri repetitive pe un obiect?
- Trebuie ca obiectul respectiv sa aiba disponibila metoda 
\_\_iter__()

```python
nums = [1, 2, 3]
print(nums.__iter__()) # <list_iterator object at 0x017AE658>
```

- \_\_iter__() ne returneaza un iterator
- Loop-urile (for, while) apeleaza aceasta metoda \_\_iter__()
in spate, se returneaza un ITERATOR, si astfel putem sa accesam elementele
pe rand.
- Functia iter() (care la randul ei apeleaza metoda \_\_iter__())
returneaza un iterator de la acestea.

```python
nums = [1, 2, 3]

i_nums = iter(nums) 
```

- Iteratorii sunt peste tot in Python.
- ITERATORUL in Python este pur și simplu un obiect
care poate fi iterat astfel incat 
va returna date, cate un element pe rand. 
- Tehnic vorbind, un obiect iterator Python trebuie sa implementeze
doua metode speciale, \_\_iter__() și \_\_next__(),
numite colectiv protocol iterator.
- Un iterator tine minte state-ul iteratiei si stie care este elementul
urmator din iteratie.
- Daca o iteratie a ajuns la final, se arunca exceptia StopIteration.

```python
nums = [1, 2, 3]

i_nums = iter(nums)
print(i_nums)
print(iter(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums)) # StopIteration error
```
- Folosim functia next() pentru a itera manual 
toate elementele unui iterator.
Cand ajungem la sfarsit si nu mai exista date de returnat, va ridica exceptia StopIteration

```python
# Implementarea for loop-ului este de fapt:

# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

```python
"""
EX1: Implementeaza o clasa care sa fie atat iterabila cat si un iterator
si sa aiba acelasi comportament ca si functia range din Python.
"""
```


## 📌 Generatori
- Exista multa munca în construirea unui iterator în Python.
- Trebuie sa implementam o clasa cu metoda \_\_iter__()
si \_\_next__(), sa tinem evidenta starilor interne
si sa ridicam StopIteration atunci cand nu exista
valori de returnat.
- Acest lucru este atat lung, cat si contraintuitiv.
- Generatorul vine in ajutor in astfel de situatii.
- Generatoarele Python sunt o modalitate simpla de a crea
iteratoare. 
- Toate lucrurile mentionate mai sus sunt gestionate automat
de generatori în Python.
- Pur si simplu vorbind, un generator este o functie
care returneaza un obiect (iterator) pe care il putem itera
(o valoare la un moment dat).
- Este destul de simplu sa creezi un generator in Python.
- Este la fel de usor ca definirea unei functii normale,
dar cu o instructiune yield in loc de o instructiune return.
- Daca o functie contine cel putin o instructiune yield
(poate conține alte instructiuni yield sau return),
ea devine o functie generatoare.
- Atat yield, cat si return-ul vor returna o valoare
dintr-o functie.
- Diferenta este ca, in timp ce o instructiune return
incheie o functie in intregime,
instructiunea yield opreste functia salvand toate starile sale
si mai tarziu continua de acolo la apeluri succesive.

- utili pentru crearea easy-to-read iterators
- arata ca functiile normale, dar in loc sa returnam
valori cu "return", ne folosim de yield.
- yield va returna o valoare si va tine minte state-ul pana
unde a ramas pana cand generatorul este invocat din nou.
- Generatorii sunt tot iteratori, dar metodele \_\_iter__ si
\_\_next__ sunt create in mod automat pentru noi

```python
def my_gen():
    n = 1
    print('This is printed first')
    
    # Generator function contains yield statements
    yield n
    
    n += 1 
    print("This is printed second")
    yield n
    
    n += 1
    print('This is printed at last')
    yield n

my_gen()
```
```python
"""
EX2: Creeaza un generator care face acelasi lucru ca si clasa MyRange
implementata la exercitiul anterior.
"""

"""
EX3: Implementeaza un generator de numere pare care ne va da acces la toate
numerele pare pana la un numar maxim luat ca si parametru.
"""

"""
EX4: Implementeaza un generator de puteri ale unui numar.
Va lua doi parametri: numarul ce va fi ridicat la putere, si
un numar care va reprezenta puterea maxima pana la care primul
parametru va fi ridicat.
"""
```

## 📌 Context Managers

- Context Managers = obiecte care ne ajuta sa controlam accesul la
anumite resurse
- Una din marile provocari in programare este manipularea
resurselor externe (interactiunea cu fisiere, baza de date,
link-uri externe).
- Atunci cand interactionam cu resurse externe trebuie sa avem
in vedere o manipulare corecta a fazei de setup si teardown a resurselor.

- Cel mai intalnit mod de iteractiune cu context managers, este
utilizarea blocului with.

```python
with expression as target_var:
    do_something(target_var)
```

- "expression" trebuie sa returneze un context manager object, adica
un obiect care implementeaza protocolul context management.
- The Context Management Protocol - este format din 2 metode:
  - metoda \_\_enter\_\_ - este invocata cand se intra in blocul with
  - metoda \_\_exit\_\_ - este invocata cand se iese din blocul with
- cuvantul "as" este optional. Daca il specificam si dupa acesta,
furnizam numele unei variabile (care nume vrem noi), se va salva in
acesta rezultatul returnat din apelul metodei \_\_enter\_\_ si vom
avea acces la el in blocul with.

- Fisierele pot fi manipulate cu ajutorul unui with statement,
pentru ca functia open() returneaza un io.TextIOBase object,
obiect care este la randul lui un context manager (are implementate
metodele de \_\_enter\_\_ si \_\_exit\_\_)

### Definirea unui context manager
- Minimul necesar pentru a avea un context manager intr-o clasa
este ca aceasta sa aiba definite metodele \_\_enter\_\_ si \_\_exit\_\_
- Doar prin definirea celor doua metode o sa putem sa ne folosim
de instante ale clasei respective in with statements.
```python
class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        return self.file_obj
    
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with File('demo.txt', 'w') as opened_file:
    opened_file.write("Hola!")
```

```python
"""
EX5: Implementeaza un context manager care va masura si va afisa
durata de executie a codului executat.
"""
```

## 📌 Decoratori

- Decoratorii sunt niste tool-uri foarte puternice in Python
pentru ca permit programatorilor sa modifice comportamentul
initial al unei functii sau al unei clase.
- Decoratorii ne permit sa cream un wrapper peste o alta functie
pentru a-i extinde comportamentul, fara ai schimba implementarea
originala.

```python
def new_decorator(original_func):
    
    def wrapper_func():
        print("Niste cod inaintea apelului original_func")
        original_func()
        print("Niste cod dupa apelul original_func")
    
    return wrapper_func

@new_decorator
def func_needs_decoration():
    print("Vreau sa fiu decorata")

@new_decorator
def hello():
    print("Hello Pythonistas!")

@new_decorator
def greet():
    print("Greetings to you")

func_needs_decoration()
hello()
greet()

# Daca aplicam decoratorul pe functia de mai jos, va functiona?

def salut(name):
    print(f"Salut, {name}")


```

- Aplicarea decoratorilor pe functii care iau parametri:

```python
def decorator_salut(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"Am intrat in functia {original_func.__name__}")
        
        original_func(*args, **kwargs)

        print(f"Am iesit din functia {original_func.__name__}")
    return wrapper_func
```