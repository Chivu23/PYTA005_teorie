# Curs 4: Seturi, Tupluri, Cicluri repetitive

## 📝 OBIECTIVE
1. Recapitulare
2. Structuri de date (continuare): Seturi, tupluri: vezi curs2_1
3. While
4. For each
5. For
6. Controlul iteratiilor cu break si continue


## 📑 Recapitulare
1. Ce sunt listele? Cum se definesc in Python?
2. Putem avea in liste elemente care au tipuri diferite de date?
3. Sunt listele ordonate sau neordonate?
4. Cum inversam o lista?
5. Cum accesam un element dintr-o lista?
6. Ce metode ajutatoare folosite pe liste cunosti (min 3)?
7. Sunt listele mutabile sau imutabile?
8. Ce sunt dictionarele?
9. Cum se definesc dictionarele in Python?
10. Sunt dictionarele ordonate sau neordonate?
11. Cum accesam elementele/valorile dintr-un dictionar? (2 variante)
12. Sunt dictionarele mutabile sau imutabile? Explica de ce.

## 📌 CICLURI REPETITIVE

- ciclu repetitiv = proces prin care se executa un bloc de cod
de mai multe ori

## 📌 WHILE/WHILE ELSE
- Ciclul repetitiv while ne ajuta sa executam un bloc de cod
atat timp cat o conditie este adevarata.

```python
"""
#sintaxa while
while conditie_adevarata: # conditia se evalueaza ca True sau False
    # bloc de instructiuni care se executa atata timp
    # cat conditia <conditie_adevarata> ramane adevarata
    # de exemplu:
    print("Hello")
    x = 2
    y = 2 * x
    # OBLIGATORIU: cod care schimba valoarea de adevar
    # a conditiei trecute la while, astfel incat
    # sa nu se execute codul la infinit!
"""
```

```python
# Exemplul 1 - Afisarea numerelor de la 0 la 3
i = 0

while i <= 3:
    print(i)
    i += 1
```

```python
# Exemplul 2 - Afisarea numerelor pozitive
x = 8
while x > 0:
    print(f"Numarul {x} este pozitiv")
    x -= 1
print("S-a iesit din while")
print(f"Dupa while, x are valoarea {x}")
```

```python
# Exemplul 3 - validarea credentialelor de conectare
username = input("Introduceti numele de utilizator: ")
password = input("Introduceti parola: ")

while len(username) < 6 and len(password) < 6:
    print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
    username = input("Introduceti numele de utilizator: ")
    password = input("Introduceti parola: ")
print("Autentificare reusita")
```

```python
# Exemplul 4 - ghicirea unui numar introdus la tastatura
import random

secret_number = random.randint(1, 10)

guessed = False

while not guessed:
    guess_number = int(input("Alege un numar de la 1 la 10: "))
    if guess_number == secret_number:
        print("Felicitari! Ai ghicit!")
        guessed = True # conditia de iesire
    elif guess_number < secret_number:
        print("Numarul este prea mic. Incercati din nou.")
    else:
        print("Numarul este prea mare. Incercati din nou.")
```

- OPTIONAL: La final, se poate pune un else. Blocul de cod din else
se va executa mereu 1 data, la final, atata timp cat ciclul repetitiv
nu este intrerupt intentionat

```python
# Exemplul 1 - Afisarea cifrelor de la 0 la 3
i = 0

while i <= 3:
    print(i)
    i += 1
else:
    print("Am terminat ciclul repetitiv while.")
```

```python
# Exemplul 2 - Validarea inputului de la tastatura ca nr pozitiv
number = int(input("Introduceti un numar intreg pozitiv: "))

while number <= 0:
    print("Numarul introdus e negativ!")
    number = int(input("Introduceti un numar intreg pozitiv"))
else:
    print("Numarul introdus este pozitiv!")
```

```python
# Exemplul 3 - Cautarea unui element intr-o lista
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

search_value = int(input("Ce numar cautati? "))

index = 0
while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Valoarea a fost gasita la indexul: {index}")
        break
    index += 1
else:
    print("Valoarea nu a fost gasita in lista!")
```

```python
"""
EX1: Se da numarul x = -5.
Foloseste un while pentru a afisa numerele negative pornind
de la -5.
La final, afiseaza un mesaj ca s-au afisat toate numerele
negative.
"""
```

```python
"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""
```

## 📌 FOR/FOR ELSE - executam codul de un anumit numar de ori
- Se executa un bloc de cod pentru fiecare valoare dintr-un range
- Range este o functie built-in din Python care ne genereaza numere din intervalul dat.
- Range seamana cu slicing: range(valoare_start, valoare_final, pas)
- valoare start = de unde incepem (default e 0)
- valoare final = pana unde iteram (e exclusiv)
- Optional: pasul
- OPTIONAL: la final se poate pune un else. Blocul de cod din else se va executa mereu
1 data, la final.

```python
# executam functia print de 4 ori
for i in range(4):
    # i este o variabila care va reprezenta
    # pe rand, fiecare valoarea din range(4)
    # adica 0, 1, 2, 3

    # in loc de i putem pune orice alt nume
    
    # avem acces la variabila i doar in interiorul for-ului
    print(i)
```
```python
for i in range(4):
    print(i)
else:
    print("Am terminat.")
```

```python
"""
EX3: Afiseaza toate numerele pare pana la 10.
"""
```

```python
"""
EX4: Se da lista:
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
Afiseaza toate elementele din lista accesandu-le dupa index.
"""
```

## 📌 FOR EACH - executam cod pentru fiecare element dintr-o structura de date
- Se parcurge o colectie de date/ o structura de date 
si se salveaza fiecare element, pe rand, intr-o variabila
pe care o putem accesa in for
- La fiecare iteratie, variabila se va suprascrie cu valoarea actuala.
- Rand pe rand, se vor parcuge toate elementele dintr-o colectie.

```python
culori = ["rosu", "albastru", "galben", "mov"]

for culoare in culori:
    print(f"Culoarea mea preferata este {culoare}")
```

```python
"""
EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
"""
```

## 📌 BREAK
- Cuvantul cheie break va opri iteratia
- Practic se iese automat din loop
- Nu se mai executa codul de dupa break, din cadrul for/while

```python
for i in range(1, 50):
    if i == 3:
        break
    print(i)
```

```python
"""
EX6: Sa se afiseze primul numar par din intervalul 1 - 10
(inclusiv capetele de interval).
"""
```

```python
"""
EX7:
Se da lista:
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
Folosind un ciclu repetitiv, cauta daca 'Marius' se afla in lista de participanti.
Dupa ce l-ai gasit intrerupe ciclul repetitiv.
"""
```

## 📌 CONTINUE

- Cuvantul cheie continue va sari peste iteratia actuala
- E un fel de skip.
- Se va sari peste blocul de dupa skip, care tine de for/while

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

```python
"""
EX8: 1. Se da lista:
numere = [1, 2, 3, 4, 5, 6, 7]
Afiseaza toate elementele din lista numere,
cu exceptia numerelor 3 si 5
"""
```

## 🎓 Intrebari interviu
1. Cand folosim while si cand folosim for?
2. Ce este obligatoriu sa avem in interiorului blocului de cod while?
3. Ce reprezinta functia range?
4. Cand alegem sa folosim break intr-o structura repetitiva?
5. Cand alegem sa folosim continue intr-o structura repetitiva?
6. Ce face else-ul dintr-un for/else si while/else?
7. Daca avem un while/else, in ce caz nu se va executa codul din else?
