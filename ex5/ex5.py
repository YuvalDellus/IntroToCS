# FILE : ex5.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex5 2016-2017
# DESCRIPTION :  build a virtual store
############################################################
import xml.etree.ElementTree as ET

ITEM_CODE_STYLE_LEFT = '['
ITEM_CODE_STYLE_RIGHT = ']'
ITEM_NAME_STYLE_LEFT = '{'
ITEM_NAME_STYLE_RIGHT = '}'
SPACER = '\t'
LINE_DOWN = '\n'
ZERO = 0
BEGIN = 1
END = -2
PENALTY = 1.25
STORE_1 = 0
STORE_2 = 1
STORE_3 = 2

def get_attribute(store_db, ItemCode, tag):
    '''
    Returns the attribute (tag) 
    of an Item with code: Itemcode in the given store

    '''
    return store_db[ItemCode][tag]


def string_item(item):
    '''
    Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'

    '''
    ItemCode = item["ItemCode"]
    ItemName = item["ItemName"]
    final_form = ITEM_CODE_STYLE_LEFT + ItemCode + ITEM_CODE_STYLE_RIGHT\
                 + SPACER + \
                 ITEM_NAME_STYLE_LEFT + ItemName + ITEM_NAME_STYLE_RIGHT

    return final_form

  

def string_store_items(store_db):
    '''
    Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    '''
    store = ""
    for item in store_db:
        store += string_item(store_db[item]) + LINE_DOWN

    return store


def read_prices_file(filename):
    '''
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad haclcala".
    Returns a tuple: store_id and a store_db, 
    where the first variable is the store name
    and the second is a dictionary describing the store. 
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    '''
    tree = ET.parse(filename)
    root = tree.getroot()
    store_id = root.find("StoreId").text
    element = root.find("Items")
    items = element.findall("Item")
    my_item = dict()
    store_contain = dict()

    for item in items:  # for each item in the store
        for detail in item:  # for each ditail on specific item
            my_item[detail.tag] = detail.text
        store_contain[item.find("ItemCode").text] = dict(my_item)  # entering
        #  all the details of an item to the right place in a dict by key
        #  of the item code
        my_item = dict()  # get ready for new details set
        item = ""  # get ready for new item
    return store_id, store_contain



def filter_store(store_db, filter_txt):  
    '''
    Create a new dictionary that includes only the items 
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName. 
    Args:
    store_db: a dictionary of dictionaries as created in read_prices_file.
    filter_txt: the filter text as given by the user.
    '''
    filtered_items = dict()
    for item in store_db:
        if filter_txt in store_db[item]["ItemName"]:  # checks if item in store
            filtered_items[item] = store_db[item]  # getting all details
    return filtered_items


def create_basket_from_txt(basket_txt): 
    '''
    Receives text representation of few items (and maybe some garbage 
      at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt

    '''
    numbers_list = list()
    for (i, letter) in enumerate(basket_txt):
        if letter == ITEM_CODE_STYLE_LEFT:
            temp = basket_txt[i + 1:]  # getting the string without '['
            for (i, letter) in enumerate(temp):  # running on new string
                if letter == ITEM_CODE_STYLE_RIGHT:
                    final = temp[:i]  # cutting the string without ']'
                    numbers_list.append(final)  # saves the item code string
                    break
                elif letter == ITEM_CODE_STYLE_LEFT:  # if we get '[' agian in
                    #  a row, the user chose partial item code and we break
                    break
    return numbers_list


def get_basket_prices(store_db, basket):
    '''
    Arguments: a store - dictionary of dictionaries and a basket - 
       a list of ItemCodes
    Go over all the items in the basket and create a new list 
      that describes the prices of store items
    In case one of the items is not part of the store, 
      its price will be None.

    '''
    prices = list()
    for code in basket:
        if code in store_db:  # if item exist in the store
            prices.append(float(store_db[code]["ItemPrice"]))  # get item price
        else:
            prices.append(None)  # if item not exist, saves None as price
    return prices


def sum_basket(price_list):
    '''
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones) 
      and the number of missing items (Number of Nones)

    '''
    sum_price_list = ZERO
    missing_items = ZERO
    for item_price in price_list:
        if item_price is None:
            missing_items += 1  # counts missing items
        else:
            sum_price_list += item_price  # sum all prices
    return (sum_price_list, missing_items)


 
def basket_item_name(stores_db_list, ItemCode): 
    ''' 
    stores_db_list is a list of stores (list of dictionaries of 
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not avaiable in any of the stores return only [ItemCode]

    '''
    for store in stores_db_list:
        if ItemCode in store:
            return string_item(store[ItemCode])
    return ITEM_CODE_STYLE_LEFT + ItemCode + ITEM_CODE_STYLE_RIGHT




def save_basket(basket, filename):
    ''' 
    Save the basket into a file
    The basket reresentation in the file will be in the following format:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    '''
    f = open(filename, 'w')
    for line in basket:
        n = f.write(ITEM_CODE_STYLE_LEFT
                    + line +  # writes the line to a file
                    ITEM_CODE_STYLE_RIGHT + LINE_DOWN)
    f.close()


def load_basket(filename):
    ''' 
    Create basket (list of ItemCodes) from the given file.
    The file is assumed to be in the format of:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    '''
    items = list()
    f = open(filename, 'r')
    for line in f:
        items.append(line[BEGIN:END])  # slicing the "[]" and the "\n"
    f.close()
    return items


def item_price_calculation(stores_list, store_index, item_index):
    """takes a list of lists of prices and checks if an item exist in a given
     store, if the item does'nt exist it will check the existence in the other
      stores and calculate the price of the given item + penalty"""
    main_store = store_index
    store_a = store_index - 1  # index manipulation
    store_b = store_index - 2  # index manipulation

    if stores_list[main_store][item_index] is None:

            # if exists in one store but not in the other
        if stores_list[store_a][item_index] is None:
            return stores_list[store_b][item_index] * PENALTY

            # if exists in one store but not in the other
        elif stores_list[store_b][item_index] is None:
            return stores_list[store_a][item_index] * PENALTY

        else:
            # if exists in both store will take the higher price for penalty
            return max(stores_list[store_a][item_index],
                       stores_list[store_b][item_index]) * PENALTY
    else:
        return stores_list[main_store][item_index]  # the price in the store

def best_basket(list_of_price_list):
    '''
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a 
    missing item has a price of its maximal price in the other stores *1.25

    '''
    sum_1, sum_2, sum_3 = ZERO, ZERO, ZERO
    prices = list()
    store_1, store_2, store_3 = list_of_price_list
    best = ZERO

    for i in range(len(store_1)):  # arbitrary Store for length
        sum_1 += item_price_calculation(list_of_price_list, STORE_1, i)

        sum_2 += item_price_calculation(list_of_price_list, STORE_2, i)

        sum_3 += item_price_calculation(list_of_price_list, STORE_3, i)

    prices.append(sum_1)
    prices.append(sum_2)
    prices.append(sum_3)
    low = min(prices)
    for i in range(len(prices)):
        if low == prices[i]:
            best = i  # getting the index of the cheapest basket
    return best
