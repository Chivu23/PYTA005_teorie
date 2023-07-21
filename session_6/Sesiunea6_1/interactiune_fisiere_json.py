# interactiunea cu fisiere JSON

"""
JSON = Javascript Object Notation
"""
import json

"""
citire din fisier json:

metoda json.load()
- folosim aceasta metoda ca sa incarcam/decodam
un obiect de tip json dintr-un fisier intr-un obiect
corespunzator in Python

fisier json -> obiect corespunzator Python
"""


def citire_din_fisier_json(cale_fisier):
    with open(cale_fisier, 'r') as file:
        return json.load(file)

data = citire_din_fisier_json('quiz.json')
print(type(data))
sport_question = data["quiz"]["sport"]["q1"]["question"]
print(sport_question)
quiz = data["quiz"]
sport_category = quiz["sport"]
q1 = sport_category["q1"]
question = q1["question"]
print(question)

"""
scrierea intr-un fisier json:

json.dump() = codifica si scrie un obiect Python
intr-un fisier JSON

Aceasta primeste ca si argumente:
- un obiect Python care dorim sa fie converit la un obiect
JSON si scris intr-un fisier
- fisierul unde dorim sa salvam continutul json
"""

def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    with open(cale_fisier, 'w') as file:
        json.dump(randuri_informatii, file, indent=4)


data = {
    "nume": "Ana Popa",
    "varsta": 25,
    "oras": "Cluj-Napoca",
    "tara": "Romania",
    "meserie": "programator software",
    "salariu": 6000,
    "zodie": "sagetator"
}

scriere_in_fisier_json("contact.json", data)

data_list = [
    {
        "nume": "Marc Paula",
        "varsta": 25,
        "oras": "Iasi"
    },
    {
        "nume": "Alin Pop",
        "varsta": 34,
        "oras": "Bucuresti"
    }
]

scriere_in_fisier_json("contacte.json", data_list)


