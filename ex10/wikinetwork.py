############################################################
# FILE : ex10.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION :  WikiNetwork, WikiNetwork class
############################################################

from article import Article
from copy import deepcopy

def read_article_links(file_name):
    """
    :param file_name:  the file which we read from.
    :return: list of tuples that represent links between articles.
    """
    art_list = list()
    file = open(file_name, "r")
    for line in file:
        line = line.rstrip()
        art1, art2 = line.split("\t")
        art_list.append((art1, art2))
    file.close()
    return art_list

class WikiNetwork:
    """
    Class that represent a Wikipedia like network, contain articles
    """

    def __init__(self, link_list):
        self.__articles = self.initiate(link_list)
        self.__articles_values_dict = self.initiate_value_dict()
        self.__entry_level_dict = dict()

    def initiate(self, link_list):
        """
        initiate and build a WikiNetwork object
        :param link_list: list of tuples that represent links between articles.
        """
        articles_list = dict()
        for couple in link_list:
            if couple[0] not in articles_list:  # checks if need to build an
                # article in the given name
                if couple[1] not in articles_list:  # checks if need to build
                    # a neighbor article in the given name
                    article_neighbor = Article(couple[1])  # build neighbor
                    articles_list[couple[1]] = article_neighbor

                article = Article(couple[0]) # build an article
                article.add_neighbor(articles_list[couple[1]])  # adding the
                # neighbor to the article
                articles_list[couple[0]] = article
            else:  # we already have have article in that name
                if couple[1] not in articles_list: # checks if need to build
                    # a neighbor article in the given name
                    article_neighbor = Article(couple[1])
                    articles_list[couple[1]] = article_neighbor
                articles_list[couple[0]].add_neighbor(articles_list[couple[1]])

        return articles_list

    def update_network(self, link_list):
        """
        update the WikiNetwork with new articles
        :param link_list: st of tuples that represent links between articles
        :return:
        """
        for couple in link_list:
            if couple[0] not in self.__articles:
                if couple[1] not in self.__articles:
                    article_neighbor = Article(couple[1])
                    self.__articles[couple[1]] = article_neighbor
                article = Article(couple[0])
                article.add_neighbor(self.__articles[couple[1]])
                self.__articles[couple[0]] = article
            else:
                if couple[1] not in self.__articles:
                    article_neighbor = Article(couple[1])
                    self.__articles[couple[1]] = article_neighbor
                self.__articles[couple[0]].add_neighbor(self.__articles[couple[1]])

    def __getitem__(self, title):
        if title not in self.get_titles():
            raise KeyError("the article: " + str(title) + " is not in the network")
        return self.__articles[title]

    def get_articles(self):
        """
        :return: a list of all the articles object in the WikiNetwork
        """
        articles_list = list()
        for article in self.__articles:
            articles_list.append(self.__articles[article])

        return deepcopy(articles_list)

    def get_titles(self):
        """
        :return: a list of the titles of all the articles
        """
        return list(self.__articles.keys())

    def __contains__(self, title):
        """
        determine if a given atricle in the WikiNetwork or not
        :param title: article name
        :return: True or False
        """
        return title in self.__articles

    def __len__(self):
        """
        determine the len of the WikiNetwork by the amount of articles it
        contains
        """
        return len(self.__articles)

    def __repr__(self):
        """
        representation of the WikiNetwork
        :return: string of all the articles that it contains
        """
        return str(self.__articles)

    def initiate_value_dict(self, value=1):
        """
        An assist function to the Page Rank function, initiate a dict of all
        the articles with a given value
        :param value: the starting value, 1 by default
        """
        articles_values_dict = dict()
        for title in self.get_titles():
            articles_values_dict[title] = value
        return articles_values_dict

    def get_values_dict(self):
        """
        Assist fuunction th Page Rank
        :return: the articles values dict
        """
        return self.__articles_values_dict

    def page_rank(self, iters, d=0.9):
        """
        determine the relevans of the articles in the Wiki by the number of
        articles that linked to it and the number of articles it linked to.
        :param iters: the number of iterations
        :param d: a value that determine how much credit the article spread
        :return: list of the the relevance of the articles sorted from most to
        least and alphabetic
        """
        temp_articles_values_dict = self.initiate_value_dict(1 - d)  # hold the
        # amount of credit of each article every iteration
        for iter in range(iters):
            for title in self.get_titles():  # checks each article
                print(self.__articles[title].get_neighbors())
                for neighbor in self.__articles[title].get_neighbors():  #
                    # check each neighbor of the article
                    if neighbor.get_title() in temp_articles_values_dict:
                        credit_to_share = (d * self.__articles_values_dict[title])
                        number_of_neighbors = len(self.__articles[title].get_neighbors())
                        temp_articles_values_dict[neighbor.get_title()] += \
                            credit_to_share / number_of_neighbors
                    else:
                        credit_to_share = (d * self.__articles_values_dict[title])
                        number_of_neighbors = len(self.__articles[title].get_neighbors())
                        temp_articles_values_dict[neighbor.get_title()] = \
                            credit_to_share / number_of_neighbors

            self.__articles_values_dict = temp_articles_values_dict
            temp_articles_values_dict = self.initiate_value_dict(1 - d)

        sorted_list = [article[0] for article in sorted(self.__articles_values_dict.items(),
                                            key=lambda article: (-article[1], article[0]))]
        # sorting the list by value and alphabetic
        return sorted_list

    def jaccard_index(self,article_title):
        """
        check the strength of the link between to articles
        :param article_title: the aritcle we check
        """
        if article_title not in self or not self.__articles[article_title].get_neighbors():
            return None
        jaccard_dict = dict()
        neighbors_set = set(self.__articles[article_title].get_neighbors())

        for title in self.get_titles():
            article_neighbors = set(self.__articles[title].get_neighbors())
            intersection = article_neighbors & neighbors_set
            union = neighbors_set | article_neighbors
            jaccard_dict[title] = len(intersection) / len(union)

        sorted_list = [article[0] for article in sorted(jaccard_dict.items(),
                                    key=lambda article: (-article[1], article[0]))]
        # sorting the list by value and alphabetic

        return sorted_list

    def find_entry_rank(self):
        """
        assist function to travel path iterator, checks the entry rank of each
        article in the Wiki
        """
        for article in self.get_articles():
            for neighbor in article.get_neighbors():
                if neighbor.get_title() not in self.__entry_level_dict:
                    self.__entry_level_dict[neighbor.get_title()] = 1
                else:
                    # each time we touch an article we updates it's entry level
                    self.__entry_level_dict[neighbor.get_title()] += 1

    def travel_path_iterator(self, article_title):
        """
        A recursive generator, in each iteration the function will print the
        current article title and check who is the neighbor with the highest
        entry level, then will call to itself with this neighbor.
        the function will stop when get input of article that doesn't exist in
        th Wiki, or when an article has not neighbors to move to.
        At the first iteration the function will generate the entry level dict
        of all the articles in the Wiki.
        :param article_title: String, the title of the first article.
        :return: The article you moved to, if there is one.
        """
        if article_title not in self.get_titles():
            return  # if the given article title is not in our Wiki, will
            # return an empty generator

        if not len(self.__articles[article_title]):  # if the article have no
            # neighbors the generator will yield this last title and returns
            yield article_title
            return

        if not self.__entry_level_dict:
            self.find_entry_rank()  # will work only at the first iteration,
            # creates a list with every entry level of any article in our Wiki

        yield article_title  # yielding the step we in each iteration

        entry_rank_list = [(article_title, 0)]  # entering a temp article for
        # reference, a tuple of the title and its entry level

        for neighbor in self.__articles[article_title].get_neighbors():
            # checks for all the neighbors of the article the following
            # conditions:
            if self.__entry_level_dict[neighbor.get_title()] > entry_rank_list[0][1]:
                # if the entry rank of the article we checking is higher than
                # the one that already in the list, the new article will
                # replace it.
                entry_rank_list.clear()
                entry_rank_list.append((neighbor.get_title(), self.__entry_level_dict[neighbor.get_title()]))

            elif self.__entry_level_dict[neighbor.get_title()] == entry_rank_list[0][1]:
                # if the entry rank of the article we checking is equal to
                # the one that already in the list, we add the article to the
                # existing one
                entry_rank_list.append((neighbor.get_title(), self.__entry_level_dict[neighbor.get_title()]))

        entry_rank_list = sorted(entry_rank_list)  # if there is more than one
        # article with the same entry rank, will sort them alphabetic.

        yield from self.travel_path_iterator(entry_rank_list[0][0])
        # recursive calling, will move to the next neighbor with the highest
        # entry rank and start over.

    def friends_by_depth(self, article_title, depth):
        """
        A function that cheaks all the neighbors of an article in a given depth
        :param article_title: the article we want to start with
        :param depth: the depth we want to check neighbors for
        """
        neighbors_set = set()
        neighbors_set.add(article_title)

        if article_title not in self.get_titles():
            return None

        if depth == 0:
            return {article_title}

        for neighbor in self.__articles[article_title].get_neighbors():
            neighbors_set.add(neighbor.get_title())  # adding new neighbor
            neighbors_set = neighbors_set | self.friends_by_depth(neighbor.get_title(), depth-1)
            # a recursive call, decrease the depth and check for the neighbor

        return neighbors_set