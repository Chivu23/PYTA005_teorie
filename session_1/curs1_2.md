# Curs 2: Functia input(), metode string, Operatori, conditionale
## 📝 OBIECTIVE
1. Recapitulare sesiunea 1.1
2. Tipuri de Operatori
Sa cunoastem tipurile principale de operatori
- De atribuire
- Artimetici
- De comparare
- Logici
3. Conditionalul if else (flow control)
Sa intelegem cum functioneaza if statement
- If simplu
- If/else
- If/elif/else

## 💡 Recapitulare Sesiunea 1.1
1. Ce sunt comentariile in Python si la ce ne ajuta?
2. Ce este o variabila?
3. Ce tipuri de variabile cunosti?
4. Cum afisam un mesaj cand rulam programul Python?
5. Ce metoda folosim ca sa verificam tipul variabilelor?
6. Ce inseamna type casting?

## 📌 Operatori aritmetici

| Operator | Name           | Example |
|----------|----------------|---------|
| +        | Addition       | x + y   |
| -        | Substraction   | x - y   |
| *        | Multiplication | x * y   |
| /        | Division       | x / y   |
| %        | Modulus        | x % y   |
| **       | Exponentiation | x ** y  |
| //       | Floor division | x // 2  |

```python
x = 2
y = 3

# # adunarea
print(x + y) # 5
# # scaderea
print(y - x) # 1
# # inmultirea
print(x * y) # 6
# # impartirea
print(y / x) # 1.5
# # restul impartirii
print(y % x) # 1
# # ridicarea la putere
print(x ** y) # 2 la puterea 3 -> 8
# # floor division
print(y // x) # 3 // 2; 1.5 => 1

# inmultirea pe string-uri
my_str = 'a'

# vreau sa afisez mesajul 'aaa'
print(my_str + my_str + my_str)
print(my_str * 3)
```

### 🔸 Floor division: // operator
- Rotunjeste rezultatul fata de cel mai apropiat intreg

```python
x = 17
y = 2

# daca ambele numere sunt int -> rezultatul va fi int
print (x // y) # 8.5 -> rezultatul este 8

x = 17.8
y = 2

# daca cel putin unul din numere este float -> rezultatul va fi float 
print(x // y) # 8.9 -> rezultatul este 8.0


x = -17
y = 2
print(x // y) # -8.5 -> rezultatul este -9
```

```python
"""
EX1: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""
```

#### ❔ Pe ce principiu se rotunjeste?
Intregul catre care se orienteaza trebuie sa indeplineasca urmatoarea conditie: Rezultat rotunjit <= intregul rezultatului

## 📌 Operatori de atribuire
| Operator | Example | Same as   |
|----------|---------|-----------|
| =        | x = 5   | x = 5     |
| +=       | x += 3  | x = x + 3 |
| -=       | x -= 3  | x = x - 3 |
| *=       | x *= 3  | x = x * 3 |
| /=       | x /= 3  | x = x / 3 |


## 📌 Operatori logici

| Operator | Description                                            | Example               |
|----------|--------------------------------------------------------|-----------------------|
| and      | Returns True if both statements are true               | x < 5 and x < 10      |
| or       | Returns True if one of the statements is true          | x < 5 or x < 4        |
| not      | reverse the result, return False if the result is True | not(x < 5 and x < 10) |

```python
"""
EX2: Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu
rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand
si ruleaza exemplele si verifica output-ul.
"""

# Exemplul 1:
a = True
b = False
# print(not(a))
# print(not(b))

# Exemplul 2:
a = True
b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)

# Exemplul 3:
a = False
b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)
```

## 📌 Operatori de comparare

| Operator | Name                       | Example |
|----------|----------------------------|---------|
| ==       | Equal                      | x == y  |
| !=       | Not equal                  | x != y  |
| &gt;     | Greater than               | x > y   |
| &lt;     | Less than                  | x < y   |
| &gt;=    | Greater than or equal than | x >= y  |
| <=       | Less than or equal to      | x <= y  |

```python
"""
EX3: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""
```

## 📌 If...
- If este o declaratie/ un statement in cod prin care ghidam programul nostru sa execute o bucata de cod in functie de un criteriu/o conditie.
- Codul se executa doar daca conditia data la if este evaluata ca True/Adevarata.
- In engleza acest principiu se numeste ‘flow control’ - controlam pe unde curge codul.
- Un if simplu e ca o usa: daca usa e deschisa (true), se va executa codul din spate. Daca usa (conditia) e inchisa (false), python nu va afla ce e in spatele usii. Pentru Python, acea zona de cod e inaccesibila, nu exista.
- Cum definim un if?
```python
x = 5
if x == 5:
    print("x este egal cu 5") # indentare cod
```
 
- Dupa cele : ale unei ramuri, cand apasam ‘Enter’ se vor pune automat 4 spatii sau un TAB
- Acest lucru se numeste indentare. Indentarea are scopul de a-i transmite la python de unde pana unde tine blocul de cod corespunzator acelei conditii. (Sau altfel spus, marcheaza peretii camerei din spatele usii)

```python
nota_de_trecere = 4.5
nota = float(input('alege nota'))
if nota >= nota_de_trecere:
    print(f'Ai luat nota {nota}')
    print('Felicitari, ai trecut examenul!')
```

- E ok logica codului?

```python
"""
EX4: Verifica daca varsta introdusa de utilizator este mai mare
decat 18 ani.
"""
```

```python
"""
EX5: Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
"""
```


## 📌 If...else
- Daca conditia scrisa la if nu se indeplineste (este evaluata ca fiind False), vrem sa spunem programului ce sa faca.
- Are tot timpul fix 2 ramuri
- If are conditie urmata de :
- Else nu mai are nevoie de conditie.
- Ex: Un numar daca nu e par, e automat impar

```python
# constanta = are o valoare stabila, nu ne dorim sa o schimbe nimeni
# standardul este sa o scriem cu litere mari
NOTA_DE_TRECERE = 4.5
nota = float(input('Alege nota'))
if nota >= NOTA_DE_TRECERE:
    print(f'Ai luat nota {nota}')
    print('Felicitari ai trecut examenul')
else:
    print(f'Ai luat doar nota {nota}')
    print('Ne vedem la vara! Ai picat examenul')
```

```python
"""
EX6:
a. Citeste un numar de la tastatura.
b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
"""
```

```python
"""
EX7:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
"""
```

## 📌 If...else if ... else
- Se foloseste cand avem mai mult de 2 situatii posibile
- Conditiile se evalueaza de sus in jos
- Se executa codul aferent primei conditii adevarate
- Dupa ce s-a gasit un true, nu se mai verifica ce a mai ramas mai jos

```python
# robotelul telefonic
optiune = int(input('alege o optiune'))
if optiune == 0:
    print('meniul anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print('ati ales eng')
else:
    print('Nu am identificat optiunea, mai incearca.')
```

- Un singur if la inceput
- Oricate elif-uri sunt necesare
- Un singur else la final
- Daca nu gaseste nici un true mai sus, else se va executa automat (e ca un default)

```python
"""
EX8: Citeste de la tastatura varsta utilizatorului si afiseaza categoria
de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
"""
```

```python
"""
EX9: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
cosul de cumparaturi, in functie de totalul cosului de cumparaturi
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
dupa aplicarea reducerii.
"""
```


# 📌 Nested if conditions

```python
'''
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
else:
    eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
else:
    go_shopping()
'''
```

```python
"""
EX10:
a. Citeste de la tastatura nr de ore lucrate de un angajat intr-o saptamana.
b. Tinand cont ca numarul de ore standard de munca dintr-o saptamana este 40,
si se considera overtime, ce e peste 40 de ore, afiseaza bonusul pe care angajatul
il primeste si un mesaj sugestiv, tinand cont de urmatoarele criterii:
- bonusul este de 50 lei daca angajatul a lucrat intre 40 si 50 ore.
- bonusul este de 100 lei daca angajatul a lucrat mai mult de 50 de ore.
- daca s-a lucrat nr de ore standard, angajatul nu e eligibil pentru bonus.
"""
```

```python
"""
EX11:
a. Citeste de la tastatura varsta utilizatorului.
b. Spune-i utilizatorului daca are drept de vot in Romania.
Ia de la utilizator datele necesare.
criterii:
- utilizatorul are drept de vot daca este mai mare de 18 ani.
- utilizatorul are drept de vot daca locuieste in Romania.
"""
```
