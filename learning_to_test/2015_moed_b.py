from copy import deepcopy

def g(x):
    # print(x)
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + g(x[1:])


def f(x,y):
    # print(x,y, (x+y) % 2)
    return (x+y) % 2

def h(x):
    if len(x) == 1:
        return x[0]
    else:
        return f(x[0],h(x[1:]))

# print(h([0, 1, 0, 1, 0]))
# print(h([1, 1, 1, 1, 0]))

def foo(x,y):
    # print([f(x[i],y[i]) for i in range(len(y))])
    return g([f(x[i],y[i]) for i in range(len(y))])

# print(foo([0,0,1,1,1,0,0], [1,1,1,1,1]))

def bar(x,y,z):
    print(x)
    if len(x) < len(y):
        return False
    elif foo(x,y) <= z:
        return True
    else:
        return bar(x[1:],y,z)

# print(bar([0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0], [1,1,1,1,1], 1))
# print(bar([1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0], [1,1,1,1,1], 2))

def my_bar(x,y,z):
    for i in range(len(x)):
        if len(x[i:]) < len(y):
            return False
        elif foo(x[i:],y) <= z:
            return True

# print(my_bar([0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0], [1,1,1,1,1], 1))
# print(my_bar([1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0], [1,1,1,1,1], 2))



def subsets(lst):
    if len(lst)==0:
        yield []
    else:
        for tail in subsets(lst[1:]):
            yield tail
            yield [lst[0]]+tail

k = [4,7,9]

def filtered_subsets(lst,max_sum):

    a = subsets(lst)

    def fun1(x):
        if sum(x) <= max_sum:
            return True
        else:
            return False

    b = filter(fun1,a)

    for i in b:
        yield i


# print(list(filtered_subsets([1,5,3],4)) )

def subsets2(lst,max_sum):
    if len(lst)==0:
        yield []
    else:
        for tail in subsets2(lst[1:],max_sum):
            if sum(tail)<= max_sum:
                yield tail
                if sum(tail) + lst[0]<= max_sum :
                    yield [lst[0]]+tail


def filtered_subsets(lst,max_sum):

    a = subsets2(lst,max_sum)

    for i in a:
        yield i

# print(list(filtered_subsets([-5,5],0)) )

def subsets3(lst,min_sum,max_sum):
    if len(lst)==0:
        yield []
    else:
        for tail in subsets3(lst[1:],min_sum, max_sum):
            print(tail)
            if min_sum <= sum(tail)<= max_sum:
                yield tail
            if min_sum <=(sum(tail) + lst[0])<= max_sum :
                yield [lst[0]]+tail


def filtered_subsets2(lst,min_sum,max_sum):

    a = subsets3(lst,min_sum,max_sum)

    for i in a:
        yield i

print(list(filtered_subsets2([1,5,3],2,4)) )

def neighbors(table, i, j):
    counter = 0
    for k in range(3):
        if k+i >= len(table[i]):
            if table[k-i][j]:
                counter += 1
        elif table[i + k][j]:
            counter += 1
        if table[i - k][j]:
            counter += 1

    if j + 1 >= len(table[i]):
        if table[i][0]:
            counter += 1

    elif table[i][j + 1]:
        counter += 1
    if table[i][j - 1]:
        counter += 1

    return counter



def table_create(n):
    table = []
    for i in range(n):
        row = [False]*n
        table.append(row)
    return table

def print_table(table):
    for row in table:
        for i in row:
            if i:
                print("x",end="")
            else:
                print("0",end="")
        print("")

my_table = table_create(4)

my_table[1][1] = True
my_table[1][2] = True
my_table[2][1] = True
my_table[2][2] = True

def life(table):
    cur_table = deepcopy(table)
    table_len = len(table[0])
    yield cur_table

    for i in range(table_len):
        for j in range(table_len):
            alive(cur_table,(i,j))

    yield from life(cur_table)

k = life(my_table)

# print_table(next(k))
# print_table(next(k))
# for i in range(7):
#     print_table(next(k))
#     print("\n")




