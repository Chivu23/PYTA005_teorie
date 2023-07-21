lst = ['a', 'b', 'c']

# for litera in lst:
#     print(litera)
    # avem 3 iteratii
    # iteratia 1 -> litera = 'a'
    # iteratia 2 -> litera = 'b'
    # iteratia 3 -> litera = 'c'

# ITERABIL = obiect care are disponibila metoda __iter__

# nums = [1, 2, 3]
# print(nums.__iter__())

# nums.__iter__() <-> iter(nums)
# metoda __iter__ ne returneaza un obiect iterator

# ITERATORI

# Un ITERATOR este un obiect care implementeaza
# 2 metode speciale (ITERATOR PROTOCOL):
# - metoda __iter__
# - metoda __next__

nums = [1, 2, 3] # este un ITERABIL, pentru ca are
# implementata metoda __iter__
i_nums = iter(nums) # este un ITERATOR
# i_nums.__iter__() <-> iter(i_nums)
# i_nums.__next__() <-> next(i_nums)
# print(i_nums)
# print(iter(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums)) # da eroare: StopIteration

"""
EX1: Implementeaza o clasa care sa fie atat iterabila
cat si un iterator
si sa aiba acelasi comportament ca si functia range
din Python.
"""

range(1, 5) # -> 1, 2, 3, 4
range(3, 6) # -> 3, 4, 5

# for x in range(1, 5):
#     print(x)
#
# print("============")

# for x in range(3, 6):
#     print(x)

# REZULTAT DORIT:

# for x in MyRangeClass(1, 5):
#     print(x)
#
# for x in MyRangeClass(3, 6):
#     print(x)


class MyRangeClass:

    def __init__(self, start, end):
        self.value = start # 1 2 3 4
        self.end = end # 4

    # facem clasa sa fie iterabila
    def __iter__(self):
        # trebuie sa returneze un iterator
        # iteratorul trebuie sa implementeze metoda __iter__ si __next__
        # ce putem face, ca clasa curenta sa fie in acelasi
        # timp si un iterabil, dar si un iterator?
        return self

    def __next__(self):
        # coditie in care aruncam exceptia StopIteration
        if self.value >= self.end:
            # 1. daca 1 >= 4
            # 2. daca 2 >= 4
            # 3. daca 3 >= 4
            # 4. daca 4 >= 4
            raise StopIteration
        current_value = self.value # 1 2 3
        self.value += 1 # 2 3 4
        return current_value

# nums = MyRangeClass(1, 10)
# for num in nums:
#     print(num)
#
# for number in MyRangeClass(1, 4):
#     print(number)

# 1
# 2
# 3

# GENERATORI

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

# for number in my_gen():
#     print(number)

generator = my_gen()
# print(next(generator))
# print(next(generator))
# print(next(generator))

"""
EX2: Creeaza un generator care face acelasi lucru ca si 
clasa MyRangeClass
implementata la exercitiul anterior.
"""

def my_range(start, end):
    # start 1
    # end 4
    current = start # 1 2 3 4
    while current < end: # 1 < 4, 2 < 4, 3 < 4, 4 < 4
        yield current # 1 2 3
        current += 1 # 2 3 4

# for number in MyRangeClass(1, 4):
#     print(number)

for number in my_range(1, 4):
    print(number)

# 1
# 2
# 3