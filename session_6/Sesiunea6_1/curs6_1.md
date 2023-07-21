# Curs 6_1: Interactiunea cu fisiere, JSON, Python Packages
## 📝 OBIECTIVE
- Interactiunea cu fisiere: citire, scriere in fisiere
- Manipulare fisiere txt, json, csv
- JSON
- Python Packages
- Virtual environments

## 📌 Interactiunea cu fisiere txt
- open() = functie folosita pentru a interactiona cu un fisier
- In urma citirii/scrierii intr-un fisier, trebuie sa il inchidem.

```python
def citire_din_fisier_txt(calea_catre_fisier_txt):
    fisier = open(file=calea_catre_fisier_txt, mode='r')
    lines = fisier.readlines()
    print(lines)
    fisier.close()

citire_din_fisier_txt("dummy.txt")
citire_din_fisier_txt("fisiere_text/dogs.txt")
```

- Pentru a ne simplifica viata, putem sa ne folosim de sintaxa
"with open()" iar aceasta va incheia interactiunea cu fisierul
pentru noi.

```python
def citire_din_fisier_txt(calea_catre_fisier_txt):
    with open(calea_catre_fisier_txt, 'r') as file:
        return file.readlines()
```

```python
with open("dummy.txt") as file:
    lines = file.readlines()
    print(lines)

with open("fisiere_text/dogs.txt") as file:
    lines = file.readlines()
    print(lines)
```

```python
def scriere_in_fisier_txt(calea_fisier, informatii_as_list):
    with open(calea_fisier, mode="w") as file:
        file.writelines(informatii_as_list)
```


## 📌 JSON
- JSON = Javascript Object Notation
- Este un format tip text pentru stocare si transportare de date
- El este independent de orice limbaj de programare, toate il folosesc
- Suporta tipurile de date uzuale (str, int, float, list, dict)
- Arata si se comporta ca un dictionar

## 📌 Interactiunea cu fisiere JSON
```python
import json

def citire_din_fisier_json(cale_fisier):
    with open(cale_fisier, 'r') as file:
        return json.load(file)
```

```python
import json

def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    with open(cale_fisier, 'w') as file:
        json.dump(randuri_informatii, file)
```

## 📌 Interactiunea cu fisiere csv
- CSV = Coma Separated Values
- Fisierele CSV sunt fisiere structurate sub forma tabelara
  (excel), unde valorile coloanelor sunt separate prin virgula.

```python
import csv

with open("path_to_csv_file.csv", "r") as read_csv:
    csv.reader(read_csv)
```

```python
# EXERCITII BONUS FISIERE

"""
EX1:
1. Copierea continutului dintr-un fisier in alt fisier.
- creeaza un fisier sursa.txt (din cod) si pune continut in el
(continutul e la alegerea ta)
- copiaza continutul din fisierul sursa.txt intr-un fisier nou,
numit destinatie.txt.
Afiseaza apoi contintul din fisierul destinatie.txt
"""

"""
EX2: Numararea cuvintelor
- creeaza o functie care sa ia ca si parametru un cuvant si un fisier txt,
si afiseaza de cate ori apare acel cuvant in fisierul text.
"""

"""
EX3: Creeaza un fisier CSV, numit produse.csv cu urmatorul continut:
- coloane: id, nume_produs, pret, cantitate.
Adauga 4 randuri in fisierul csv cu detalii despre 4 produse.

Citeste informatiile din fisierul csv folosind DictReader si
pune informatiile citite intr-un fisier json, numit "produse.json".
"""
```

## 📌 Python Packages
- Python Standard Library - putem face import fara sa instalam
librarii. Exemple: math, random
- Python Packages - este necesar sa facem instalarea pachetului
inainte sa il utilizam si astfel putem folosi functiile/metodele
astfel incat sa ne optimizam codul. Exemple: behave, SQLAlchemy etc.
- Pentru pachete extra, facute de alti developeri, avem PYPI:
https://pypi.org si folosim comanda pip pentru instalarea lor.
- Link-uri de studiat:
1. https://packaging.python.org/tutorials/installing-packages/
2. https://packaging.python.org/tutorials/packaging-projects/


## 📌 Virtual environments
- Este folosit pentru a gestiona python packages pentru diferite
proiecte.
- Avantaje virtual environment:
  - putem descarca pachete in proiectul nostru fara privilegii de administrator
  - putem crea un pachet cu aplicatia noastra si ulterior o putem partaja cu alti programatori
  - putem crea cu usurinta o lista de dependinte si subdependinte intr-un fisier
, ceea ce face mai usor pentru alti programatori sa reproduca/dezvolte
si sa instaleze toate dependintele utilizate de noi in virtual environment
- Instalare virtualenv (adica programul care ne ajuta sa cream si sa folosim un virtual env)
  - putem folosi comanda: pip install virtualenv
- Avem 3 parti importante in folosirea lui:
1. Creare: python -m venv <nume_folder_venv> - aici de obicei
folosim env/venv/myenv pentru acel nume de folder, sa zicem de exemplu
ca il numim myenv. Crearea se face o singura data!
2. Activare: trebuie sa il activam ori de cate ori avem nevoie
sa rulam proiectul, sa instalam o librarie; comanda de activare e diferita in functie
de sistemul de operare:
- OSX: source myenv/bin/activate
- Windows Powershell: myenv/Scripts/Activate.ps1
- Windows cmd/Pycharm Terminal: myenv/Scripts/activate.bat
3. Dezactivare: asta o putem face cand vrem in acelasi terminal sa trecem
sa lucram la un alt proiect, comanda e: deactivate


