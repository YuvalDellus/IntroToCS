############################################################
# FILE : ex10.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex10 2016-2017
# DESCRIPTION :  WikiNetwork, Article class
############################################################

class Article:
    """
    Class that represent an article, each article contain it's name and the
    articles it's linked to
    """

    def __init__(self,  article_title):
        self.__name = article_title
        self.__neighbors = set()

    def get_title(self):
        """
        :return: the name title of an article object
        """
        return self.__name

    def add_neighbor(self, neighbor):
        """
        adding a link to given article from our article
        :param neighbor: an object from article type
        """
        self.__neighbors.add(neighbor)

    def get_neighbors(self):
        """
        :return: all the neighbors of a given article.
        """
        return list(self.__neighbors)

    def __repr__(self):
        """
        A function that determine how to print an article object
        """
        names = list()
        for neighbor in self.__neighbors:
            names.append(neighbor.get_title())
        rep = (self.__name, names)
        return str(rep)


    def __len__(self):
        """
        A function that determine the len of article object by the amount of
        its neighbors
        """
        return len(self.__neighbors)

    def __contains__(self, article):
        """
        A function that determine the if an article is neighbor of othe article
        :param article: an article object
        :return: True or False
        """
        return article in self.__neighbors
