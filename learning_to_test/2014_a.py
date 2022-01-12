x = 'abcdef'
# y = ''
k = 2
# print(x[0:k] + x[k+1:], y+x[k])

def f1(x,y=[]):
    if len(x) == 0:
        print(y)
    else:
        for k in range(len(x)):
            f1(x[0:k] + x[k+1:], y+x[k])

# f1([1,2,3])


def first_gen(n):
    for index in range(n):
        yield 1 if index%2 else 2


def second_gen(n):
    for index in range(n):
        yield sum(first_gen(index))

def third_gen(n):
    if n:
        yield n + next(third_gen(n-1))
    else:
        yield 0

print(list(third_gen(4)))