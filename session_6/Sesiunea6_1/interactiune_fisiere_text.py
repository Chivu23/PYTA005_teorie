# INTERACTIUNEA CU FISIERELE TEXT

'''
open() = functie folosita pentru a interactiona cu un fisier.
- ne returneaza o referinta cu fisierul cu care dorim sa interactionam
(practic, este fisierul deschis)

Functia open() poate lua mai multi parametri:

1. un parametru OBLIGATORIU, numit file
-calea catre fisierul cu care dorim sa interactionam/ file path
- file path = locatia unde se alfla fisierul cu care dorim sa interactionam
- un file path este compus din 3 mari parti:
    --- folder path = calea catre fiolderul unde e localizat fisierul
    --- file name = numele fisierul
    --- file extension = extensia fisierului (.txt, .csv, .json, etc)
2. parametru optional -> mode :
- modul in care dorim sa interactionam cu fisierul
- este un string si poate sa aiba mai multe valori
- cele mai comune val pt param mode:
    --- 'r'-> dechidem pt a citi
    --- 'w'-> deschidem pt a scrie
! ATENTIE !!! - SE SUPRASCRIE SI GENEREZA FISIER NOU DACA NU E (NEW FILE)
    --- ' a' -> apend - deschidem pentru a scrie la FINAL  ( extindem, actualizam)!!!

'''

# deschid fisierul dummy.txt in modul read
new_folder = open(file='dummy.txt', mode='r')

# met readlines() - > citeste topt continutul fisierului
lines = new_folder.readline()
# print(lines)
# print(lines[3])
# print(lines[8])

# deschid  dogs.txt in modul read

folder1 = open(file='fisiere_text/dogs.txt', mode='r')
lines = folder1.readline()
# print(lines)
print(folder1.read())

'''
dupa ce interactionam cu un fisier acesta trebuie inchis.
deoarce: datele din fiser raman vulnerabile, scade eficienta programului,
ocupa memorie.

'''

new_folder.close()
folder1.close()

# fisierul se inchide si cu "with"  <-- RECOMANDAT

with open(file="dummy.txt", mode='r') as f:
#    lines = f.readlines()
#    lines = f.readline()
    print(f.readlines())   # afiseaza toate liniile
    print(f.readline())   # afiseaza doar prima linie

# scrierea in fisiere text
# cu modul 'w'sau cu modul 'a'

# scriem intr un fiser nou + creeare
# apoi suprascriem folosim tot modul 'w'
# in final folosim modul 'a'sa extindem/actualizam.

with open('danny2.txt', mode='a') as file:
    file.write('Continut nou, dar vechi')

with open('danny3.txt', mode='a') as file:
    file.write('sa inteleg ca merge sa faci fisier nou si cu mdetoda a')

with open('danny2.txt', mode='w') as file:
    file.write('asta e suprascrierea de vineri')

with open('danny2.txt', mode='a') as file:
    file.write('asta e suprascrierea de vineri')

with open('danny3.txt', mode='w') as file:
    file.writelines([
        'asta e suprascrierea de vineri\n',
        'dupa ce joi seara\n',
        'ai fost la fotbal\n',
        'si ai bagat 5 g00luri'
    ])


with open('danny3.txt', mode='a') as file:
    file.writelines([
        '...unul mai frumos ca celalat.\n',
        'capodopere!!!\n',
        'ce sa mai?!?!?!'
    ])
