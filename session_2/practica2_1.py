
#
# descriere_masina = "Masina aleasa costa 20 000 euro si se poate achita in rate!”. descriere_masina = “Masina aleasa costa 20 000 euro si se poate achita in rate!"
#
# print(descriere_masina[:5])
# print(descriere_masina[-5:])
#
# my_str = "abcde"
# print(my_str.isnumeric()) # False
#
# my_str = "1234"
# print(my_str.isnumeric()) # True
#
# a = 1
# a += 1 # 1 + 1 = 2
# a *= 2 # 2 * 2 = 4
# a = a * 2 # 4 * 2 = 8
# print(a)
#
# str1 = "minge"
# str2 = "rosie"
# print(str1+str2)

# # LISTE
# # Exemplu de lista ordonata de numere intregi
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# # Output: [1, 2, 3, 4, 5]
#
# # Lista este ORDONATA
# # Fiecare element din lista poate fi accesat dupa index
# print(numbers[0]) # accesarea primului element din lista -> 1
# print(numbers[2]) # 3
# print(numbers[-1]) # 5
#
# print(numbers[::-1]) # inversarea unei liste
#
# # Lista este MUTABILA
# # Putem sa modificam, sa stergem si sa adaugam elemente intr-o lista
#
# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# print(cifre)
# # adaugam cifra 9 in lista cifre la finalul listei
# cifre.append(9)
# print(cifre)
#
# # adaugam 9 in lista cifre la indexul 2
# cifre.insert(2, 9)
# print(cifre)
#
# # stergem ultimul element din lista
# cifre.pop()
# print(cifre)
#
# # stergem elementul de la indexul 1 in lista cifre
# element_sters = cifre.pop(1)
# print(element_sters)
# print(cifre)
#
# # stergem prima aparitie a unui element in lista
# # dupa valoare
# cifre.remove(3)
# print(cifre)
#
# # cifre.remove(6) # -> ValueError
#
# caractere = ["a", "b", "a", "b", "c", "a"]
# print(caractere)
# caractere.remove("a")
# print(caractere)
# caractere.remove("a")
# print(caractere)
# caractere.remove("a")
# print(caractere)
#
# # actualizam valoarea unui element
# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# cifre[1] = 5
# print(cifre)
#
# print(type(cifre)) # <class 'list'>

# DICTIONARE

my_dict = {
    'nume_produs': 'produs_1',
    'pret': 23.00,
    'in_stoc': False
}

# my_dict = {'nume_produs': 'produs_1', 'pret': 23.00, 'in_stoc': False}

# print(my_dict)

contacte = ["0722345567", "0784553344", "0745332211"]

contacte = {
    'Ana': "0722345567",
    'Marius': '0784553344',
    'Maria': '0745332211'
}

contacte = [
    {
        'nume': 'Popa',
        'prenume': 'Ana',
        'nr_telefon': '0722345567',
        'adresa' : 'Strada Mihai Eminescu, 46',
        'adresa_mail': 'ana@popa.com',
        'varsta': 25,
        'are_masina': False
    }
]

# Dictionarul este NEORDONAT => elementele din dictionar nu
# sunt pastrate in memorie in ordinea in care au fost adaugate
# + NU putem sa accesam elementele dintr-un dictionar dupa index

# Dictionarul este MUTABIL => elementele din dictionar
# pot sa fie modificare, adaugate, sterse

contacte = {
    'Ana': '0722345678',
    'Marius': '0721549888',
    'Maria': '0765332967'
}

# dorim sa accesam numarul lui Marius
# accesam o valoare din dictionar furnizand cheia
# asociata cu acea valoare
# print(contacte['Marius'])

# dorim sa accesam numarul lui Alin
# dorim sa accesam valoarea aferenta cheii Alin
# -> DEZAVANTAJ: daca cheia nu exista in dictionar,
# si folosim aceasta sintaxa => obtinem eroare
# print(contacte['Alin']) # -> eroare: KeyError
# print("here")

# pentru a nu avea eroare in cazul in care
# cheia nu exista in dictionar,
# ne folosim de metoda ajutatoare get
# Metoda get ia ca si parametri:
# - primul parametru: cheia pentru care dorim sa ii aflam/returnam valoarea
# - al doilea parametru: spunem ce vrem sa se returneze daca nu s-a gasit cheia furnizata in dictinar
# print(contacte.get('Alin', "Nu am gasit numarul de telefon cerut"))


#
#
#
# Cate perechi cheie-valoare/elemente avem intr-un dictionar?
# print(len(contacte))

# Dictionarele sunt MUTABILE -> ca putem sa adaugam, modificam,
# stergem elemente din dictionar


person = {
    "name": "John",
    "age": 30,
    "city": ["New York", "Los Angeles"],
    "occupation": "teacher",
}

# ADAUGAREA unui element nou in dictionar
# v1
person['salary'] = 3000.00
# print(person)

# v2
person.update({"has_car": True}) # cream perechea cheie-valoare
# print(person)
person.update({"has_car": False}) # actualizam perechea cheie-valoare
# print(person)

person.update({
    "eyes_color": "green",
    "email": "john@gmail.com"
})

# print(person)

# MODIFICAREA unui element in dictionar
# v1
person['age'] = 31
# print(person)

# v2
person.update({"age": 32})
# print(person)

# STERGEREA unui element din dictionar
# v1
del person['city']
if person.get("city", False):
    del person["city"]
del person['salary'] # stergem mai multe key:value deodata
# print(person)

# v2
# stergerea unui perechi cheie:valoare dupa cheie
person.pop("name")
# print(person)