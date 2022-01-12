def foo(lst=[]):
    lst.append(3)
    return lst

temp = foo()
# print(foo(temp))

D = {1:['apple'], 0:['banana']}
D[0].append('kk')
# print(D[0])

def f():
    y = 3
    g = lambda x: x+y
    y = 4
    return g(10)

# print(f())


def count_digits(n,lst):
    my_dict = dict()

    for i in lst:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for i in range(1,n+1):
        if i not in my_dict:
            return False
        elif my_dict[i] != i:
            return False

    return True

# print(count_digits(3,[2,2,3,3,3]))

def ladder(n):
    lists = set()
    lst = [1]*n
    print(lst)
    while 1 in lst:
        lst.remove(1)
        lst.remove(1)
        lst.append(2)
        print(lst)
        temp_lst = lst[:]
        for k in range(len(lst)-1):
            for i in range(len(lst)-1,0,-1):
                lst[i], lst[i-1] = lst[i-1], lst[i]
                lists.add(tuple(lst))
                # print(lists)
                if tuple(lst) in lists:
                    print(lst)
        lst = temp_lst[:]

# ladder(6)

class A:

    def __init__(self,msg):
        self.__msg = msg

    def set_message(self,msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg

# a = A('test')
# print(a)
# a.set_message('best')
# print(a)

def f(x):
    return x +50

def g(x):
    return x*2

def switch(f,g):
    visited = []
    def do_it(x):
        if x not in visited:
            visited.append(x)
            return f(x)
        else:
            return g(x)
    return do_it

h = switch(f,g)
print(h(7))
print(h(7))
h = switch(f,g)
print(h(7))
# print(h(7))



def multi_iter(lst):
    for a,b in lst:
        if a !=0:
            for i in range(a):
                yield b

# w = multi_iter([(3,'A'), (0, 'B'), (2, 'C')])
# for x in w:
#     print(x)

class Person:
    def __init__(self, name, father=None):
        self.__name = name
        self.__father = father

    def get_name(self):
        return self.__name

    def get_father(self):
        return self.__father

    def ancestors(self,fathers=[]):
        if self.__father:
            fathers.append(self.get_name())
            fad = self.get_father()
            return fad.ancestors(fathers)
        else:
            fathers.append(self.get_name())
            fathers = fathers[::-1]
            return fathers[:len(fathers)-1]


a = Person('Avraham')
b = Person('Yitzhak', a)
c = Person('Yaackov', b)
# print(c.ancestors())

def ladder(n):
    ladder_helper(n, '')

def ladder_helper(n, steps):
    if n == 1:
        print("1" + steps)
        return
    if n == 2:
        print("11" + steps)
        print("2" + steps)
        return
    ladder_helper(n-1, "1"+steps)
    ladder_helper(n-2, "2" + steps)

# ladder(6)