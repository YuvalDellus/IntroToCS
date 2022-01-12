# class Dlist:
#     def __init__(self,lst):
#         self.__lst = lst
#
#     def __iter__(self):
#         return Diter(self.__lst)
#
# class Diter:
#     def __init__(self,lst):
#         self.__iter = lst
#         self.__cur = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__cur += 1
#         if self.__cur>= len(self.__iter):
#             raise StopIteration
#         else:
#             return self.__iter[self.__cur]
#         # return next(iter(self))
#
# b = Dlist([1,2,3,4,5])
#
# # a = iter(b)
# #
# # print(next(a))
# # print(next(a))
# # print(next(a))
# #
# for x in b:
#     print(x)

def subset(lst):
    if len(lst) == 0:
        yield []

    else:
        for tail in subset(lst[1:]):
            yield tail
            if tail == []:
                yield [lst[0]] + tail
            elif len(tail) > 0 and tail[0] > lst[0]:
                yield [lst[0]] + tail


print(list(subset([1,5,3,7,4])))