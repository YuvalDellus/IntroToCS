from random import randint

def partial_sum(lst,num):

    def to_work_with(lst):
        if len(lst)==0:
            yield []
        else:
            for tail in to_work_with(lst[1:]):
                yield tail
                yield [lst[0]]+tail

    for part_lst in list(to_work_with(lst)):
        temp = 0
        for a in part_lst:
            temp += a
        if temp == num:
            return True


k = [1,5,3]
# print(partial_sum(k,7))


def throw_cube():
    cube_1 = randint(1, 6)
    cube_2 = randint(1, 6)

    return cube_1 + cube_2

cube_results = dict()

for number in range(2,13):
    cube_results[number] = 0

for throw in range(500):
    cube_results[throw_cube()] +=1

for number in cube_results:
    print(number, ">>>",cube_results[number]*"*")



