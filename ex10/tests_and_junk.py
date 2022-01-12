# from fractions import Fraction
#
# f = lambda x: x**3+64*x-1
#
# y = 4/256
#
# print(f(y))
# print(Fraction(f(y)))


a = [('a',2),('b',3),('h',5),('g',5)]

print(sorted(a))


# def travel_path_iterator(self, article_title):
#     if not self.__entry_level_dict:
#         self.find_entry_rank()
#     entry_rank_list = [('temp', 0)]
#     for neighbor in self.__articles[article_title].get_neighbors():
#         if self.__entry_level_dict[neighbor] > entry_rank_list[0][1]:
#             entry_rank_list.clear()
#             entry_rank_list.append(
#                 (neighbor, self.__entry_level_dict[neighbor]))
#         elif self.__entry_level_dict[neighbor] == entry_rank_list[0][1]:
#             entry_rank_list.append(
#                 (neighbor, self.__entry_level_dict[neighbor]))
#     sorted(entry_rank_list)
#
#     if entry_rank_list[0][0] == 'France':
#         return






def travel_path_iterator(self, article_title):
    if article_title not in self.get_titles():
        yield []
        return
    self.find_entry_rank()
    yield from self.travel_path_iterator_helper(article_title, [])


def travel_path_iterator_helper(self, article_title, traveled_list):
    traveled_list.append(article_title)
    entry_rank_list = [('temp', 0)]
    for neighbor in self.__articles[article_title].get_neighbors():
        if self.__entry_level_dict[neighbor] > entry_rank_list[0][1]:
            entry_rank_list.clear()
            entry_rank_list.append(
                (neighbor, self.__entry_level_dict[neighbor]))

        elif self.__entry_level_dict[neighbor] == entry_rank_list[0][1]:
            entry_rank_list.append(
                (neighbor, self.__entry_level_dict[neighbor]))

    entry_rank_list = sorted(entry_rank_list)
    print(entry_rank_list)

    if entry_rank_list[0][0] not in traveled_list:
        self.travel_path_iterator_helper(entry_rank_list[0][0], traveled_list)


def update_network(self, link_list):
    for couple in link_list:
        if couple[0] not in self.__articles:
            article = Article(couple[0])
            if couple[1] not in self.__articles:
                article_neighbor = Article(couple[1])
            else:
                article_neighbor = self.__articles[couple[1]]
            article.add_neighbor(article_neighbor)
            self.__articles[couple[0]] = article
        else:
            if couple[1] not in self.__articles:
                article_neighbor = Article(couple[1])
            else:
                article_neighbor = self.__articles[couple[1]]

            self.__articles[couple[0]].add_neighbor(article_neighbor)