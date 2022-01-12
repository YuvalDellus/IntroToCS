def compress(lst):
    my_list = list()
    counter = 1

    for i in range(len(lst)):
        if i == len(lst)-1:
            my_list.append((lst[i],counter))
            return my_list
        if lst[i] == lst[i+1]:
            counter += 1
        else:
            my_list.append((lst[i],counter))
            counter = 1

# a = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']

# print(compress(a))

def count_sums(a,s):
    res = []

    def sub_set(lst):
        if len(lst) == 0:
            yield []
        else:
            for tail in sub_set(lst[1:]):
                yield tail
                yield [lst[0]] + tail

    my_list = list(sub_set(a))

    for i in my_list:
        if sum(i) == s:
            res.append(i)

    return res

# a = [3,5,8,9,11,12,20]
#
# print(count_sums(a,20))

my_list = dict()

class Student:

    def __init__(self,name):
        self.__name = name
        self.__grades = list()
        my_list[name] = self

    def add_grade(self,new_grade):
        self.__grades.append(new_grade)

    def get_average(self):
        return sum(self.__grades) / len(self.__grades)

def get_student_by_name(name):
    return my_list[name]

# s = Student("sup")
# s.add_grade(90)
# s.add_grade(80)
# print(s.get_average())
#
# print(get_student_by_name("sup").get_average())

def f(x):
    return x*2

def aggregate(f):
    lst = list()

    def af(x):
        lst.append(f(x))
        return lst

    return af

# h= aggregate(f)
# print(h(7))
# print(h(5))

def zipper(head1,head2):
    if not head2:
        next = head1.next
        head1.next = head2
        zipper(head2,next)

def get_re_it(head):
    if not head:
        return

    yield from get_re_it(head.next)
    yield head.data

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

lst1 = Node('a',(Node('b', Node('c',Node('d')))))
lst2 = Node('1',(Node('2', Node('3',Node('4')))))

lst3 = zipper('a','1')
# print(lst2)

# for x in get_re_it(lst2):
#     print(x)

