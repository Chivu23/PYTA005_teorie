"""
Interactiunea cu fisiere CSV
"""

"""
CSV = Coma Separated Values
Fisiere CSV -> forma tabelara
"""

import csv

# citim dintr-un fisier csv

# v1 -> luam doar valorile din fiecare linie
# with open("employees.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     print(reader)
#
#     for row in reader:
#         print(row)

# v2 -> luam atat denumirea coloanelor cat si valoarile aferente
# pentru fiecare linie

with open("employees.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

# salvam randurile/datele din fisierul csv
# intr-o lista, pentru ca vrem poate sa modificam
# mai apoi valori din fiecare rand
# rows = []
# with open("employees.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         rows.append(row)
#
# print(rows)

# scriere intr-un fisier csv
# with open("new_employees.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)

    # v1
    # adaugam cate o linie pe rand
    # for row in rows:
    #     writer.writerow(row)

    # v2
    # adaugam toate liniile deodata
    # writer.writerows(rows)






