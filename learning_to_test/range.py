class range2:

    def __init__(self, start, end, step=1):
        self.lst = []
        self.__start = start
        self.__end = end
        self.__step = step
        self.__cur = start
        self.create_list()

    def __iter__(self):
        return ranre_iter(self.lst,self.__step)

    def create_list(self):
        while self.__cur != self.__end:
            self.lst.append(self.__cur)
            self.__cur+=1

class ranre_iter:

    def __init__(self,lst,step):
        self.__lst = lst
        self.__cur = -1
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.__cur+=self.__step
        if self.__cur>=len(self.__lst):
            raise StopIteration
        else:
            return self.__lst[self.__cur]

s= range2(5,9,2)
a=iter(s)

for i in a:
    print(i)







