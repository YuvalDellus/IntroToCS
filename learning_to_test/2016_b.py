from _functools import reduce
from math import fabs

two_to_one = lambda g: (lambda y: g(y, y))
one_to_two = lambda f: (lambda x, y: f(x) + f(y))
h = one_to_two(two_to_one(lambda x, y: x*y))

# print((h(3,2)))

def split(s):
    words_list = list()
    word = ""
    for i in range(len(s)):
        if s[i] == " ":
            if word:
                words_list.append(word)
                word = ""
        else:
            word += s[i]
    return words_list

# print(split("  hhh drgg   g uuuuu ff"))

def cartesean_product(lst):
    if len(lst)== 0:
        print([""])

    else:

       def f(ls1,ls2):
           words = list()
           for lt1 in ls1:
               for lt2 in ls2:
                   temp = lt1+lt2
                   words.append(temp)
           return words

       a = reduce(f,lst)
       print(a)

# cartesean_product([])

class MultiDict:

    def __init__(self):
        self.__multidic = list()

    def add(self,key,value):
        self.__multidic.append((key,value))

    def has_val(self,tup):
        key, val = tup
        for k, v in self.__multidic:
            if k == key and v == val:
                return True
        return False

# m = MultiDict()
# m.add('a', 1)
# m.add('b', 2)
# m.add('a', 3)
# print(m.has_val(('a', 1)))
# print(m.has_val(('a', 2)))
# print(m.has_val(('b', 1)))
# print(m.has_val(('a', 3)))


def interpolated(d):

    def the_closest(x):
        temp = fabs(min(d)-x)
        # temp_res = min(d)
        for val in d:
            if fabs(val-x)<=temp:
                temp = fabs((val - x))
                temp_res = val
        return d[temp_res]
    return the_closest

d= {0:0,7:10,20:30}

f= interpolated(d)

# print(f(-1),f(5), f(7),f(18))

def diff_iter(some_iter):
    a = next(some_iter)

    while True:
        b = next(some_iter)
        yield b - a
        a = b

a = [1,1,5,7,1,3,8]
d = iter(a)
c = diff_iter(d)

# for i in range(7):
#     print(next(c))

def find_duplicate(root):
    children_list = []

    def children_runner(root):
        child_list = []
        if root.children:
            for child in root.children:
                child_list += children_runner(child)
        else:
            return child_list

    children_list += children_runner(root)

    for child in children_list:
        temp_child = child
        children_list.remove(child)
        if temp_child in children_list:
            return temp_child

    return None
