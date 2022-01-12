def travel_path_iterator_helper(self, article_title, traveled_list):
    traveled_list.append(article_title)
    entry_rank_list = [('temp', 0)]
    yield article_title
    for neighbor in self.__articles[article_title].get_neighbors():
        if self.__entry_level_dict[neighbor] > entry_rank_list[0][1]:
            entry_rank_list.clear()
            entry_rank_list.append(
                (neighbor, self.__entry_level_dict[neighbor]))

        elif self.__entry_level_dict[neighbor] == entry_rank_list[0][1]:
            entry_rank_list.append(
                (neighbor, self.__entry_level_dict[neighbor]))

    entry_rank_list = sorted(entry_rank_list)
    # print(entry_rank_list)

    # if entry_rank_list[0][0] not in traveled_list:
    # yield entry_rank_list[0][0]
    yield from self.travel_path_iterator_helper(entry_rank_list[0][0],
                                                traveled_list)
    # print(entry_rank_list[0][0])
    # self.travel_path_iterator(entry_rank_list[0][0])
    # return traveled_list