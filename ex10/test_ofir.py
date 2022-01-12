from wikinetwork import *
from article import *

def test_jac():
    network = [('a', 'c'), ('a', 'e'), ('a', 'd'), ('a', 'f'),
               ('b', 'g'), ('b', 'c'), ('b', 'd'), ('b', 'f')]
    wiki = WikiNetwork(network)
    print(wiki.jaccard_index('a'))


def test_page():
    network = [('A', 'B'), ('A', 'D'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'B')]
    wiki = WikiNetwork(network)
    print(wiki.page_rank(1, 0.0))
    # articles = wiki.get_articles()
    # for art in articles:
    #     print("title: " + art.get_title() + " len: " + str(len(art)))


def test_path():
    network = [('a', 'b'), ('a', 'c'), ('c', 'b'), ('c', 'd'), ('b', 'e'), ('b', 'f'), ('d', 'h'),('e', 'g'), ('e', 'h'), ('f', 'd'), ('g', 'c'), ('g', 'd'),('g', 'b'), ('h', 'g')]
    wiki = WikiNetwork(network)
    for i in wiki.travel_path_iterator('a'):
        # input()
        print(i)

# links = read_article_links("links.txt")
# print("done")
# wiki = WikiNetwork(links)
# print("done")
# chosen = "XXX"
# while chosen != "exit":
#     chosen = input()
#     if chosen == "page":
#         print(wiki.page_rank(50))
#     elif chosen == "jac":
#         print(wiki.jaccard_index("Louis_XIV_of_France"))
#         print()
#         print(wiki.jaccard_index("The_Godfather"))
#         print()
#         print(wiki.jaccard_index("The_Lord_of_the_Rings"))
#         print()
#         print(wiki.jaccard_index("The_Simpsons"))
#     elif chosen == "friends":
#         print(len(wiki.friends_by_depth("United_States", 1)) / len(wiki))
#         print()
#         print(len(wiki.friends_by_depth("United_States_dollar", 2)) / len(wiki))
#         print()
#         print(len(wiki.friends_by_depth("Microsoft", 3)) / len(wiki))
#     else:
#         print("Wrong")

test_path()
