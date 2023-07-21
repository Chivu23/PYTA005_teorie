'''
acest fiser este pentru practica, testare, probe si altele.
'''


print("verde", "albastru", sep=" ---, ")
# este fix un separator

print("text1 si inca unu", end="sau doi*")
# ramane e acelasi rand

print("text3", "text4")

idee = 'azi e azi'
print(idee[4])
print(idee[1])

print(type(idee))

caz_number = 55
caz_number_ = '55'
print(type(caz_number))     # intiger pt ca-i fara ghilimele
print(type(caz_number_))   # str


number = '2'
text = 'Azi mananc cateva mere, adica'
print(text +' '+ number +'.')

print(f'Ma gandeam asa:{text} {number}')    # diferite forme de alcatuire

nume = 'Jon'
varsta = 55
print(f'azi {nume} are {varsta} de bicle')


print(type(varsta)) # functia type


"""
EX8: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""

#a
var_int = 7
print(var_int)

#b
print(type(var_int))

#c
#print(type(var_int))     # before
alta_var = float(var_int)

print(alta_var)        #after
#alta_var = var_int

#d
print(type(alta_var))

"""
EX13: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""

prop2 = 'Masina e rosie'
print(len(prop2))


cifre = '123456789'    #slicing
print(cifre[0:3])
print(cifre[3:4])    # fara 5

"""
EX14: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""

#a
prop3 = 'Concertul va avea loc maine.'
primul_cuvant= prop3[:9]
print(primul_cuvant)

#b
print(prop3[0:4])

#c
print(prop3[::-1])
