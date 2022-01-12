import xml.etree.ElementTree as ET


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
    final_form = "[" + ItemCode + "]" + "\t" + "{" + ItemName + "}"

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
        store += string_item(store_db[item]) + "\n"

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
    for item in items:
        for detail in item:
            my_item[detail.tag] = detail.text
        store_contain[item.find("ItemCode").text] = dict(my_item)
        my_item = dict()
        item = ""
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
        if filter_txt in store_db[item]["ItemName"]:
            filtered_items[item] = store_db[item]
    return filtered_items


def create_basket_from_txt(basket_txt): 
    '''
    Receives text representation of few items (and maybe some garbage 
      at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt

    '''
    numbers_list = list()
    temp = list()
    final = list()
    for (i, letter) in enumerate(basket_txt):
        if letter == "[":
            temp = basket_txt[i + 1:]
            for (i, letter) in enumerate(temp):
                if letter == "]":
                    final = temp[:i]
                    numbers_list.append(final)
                    break
                    temp = []
                    final = []
                elif letter == "[":
                    break
                    temp = []
                    final = []
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
        if code in store_db:
            prices.append(float(store_db[code]["ItemPrice"]))
        else:
            prices.append(None)
    return prices


def sum_basket(price_list):
    '''
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones) 
      and the number of missing items (Number of Nones)

    '''
    sum_price_list = 0
    missing_items = 0
    for item in price_list:
        if item is None:
            missing_items += 1
        else:
            sum_price_list += item
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
    return '['+ItemCode+']'




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
        n = f.write('[' + line + ']' + '\n')
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
        items.append(line[1:-2])  # slicing the "[]" and the "\n"
    f.close()
    return items


def best_basket(list_of_price_list):
    '''
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a 
    missing item has a price of its maximal price in the other stores *1.25

    '''
    sum_1, sum_2, sum_3 = 0, 0, 0
    prices = list()
    store_1, store_2, store_3 = list_of_price_list
    best = 0

    for i in range(len((store_1))):
        if store_1[i] is None:
            if store_2[i] is None:
                sum_1 += store_3[i]*1.25
            elif store_3[i] is None:
                sum_1 += store_2[i] * 1.25
            else:
                sum_1 += max(store_2[i],store_3[i])*1.25
        else:
            sum_1 += store_1[i]
            # continue

        if store_2[i] is None:
            if store_1[i] is None:
                sum_2 += store_3[i]*1.25
            elif store_3[i] is None:
                sum_2 += store_1[i] * 1.25
            else:
                sum_2 += max(store_1[i],store_3[i])*1.25
        else:
            sum_2 += store_2[i]
            # continue

        if store_3[i] is None:
            if store_1[i] is None:
                sum_3 += store_2[i]*1.25
            elif store_2[i] is None:
                sum_3 += store_1[i] * 1.25
            else:
                sum_3 += max(store_1[i],store_2[i])*1.25
        else:
            sum_3 += store_3[i]
            # continue

    prices.append(sum_1)
    prices.append(sum_2)
    prices.append(sum_3)
    low = min(prices)
    for i in range(len(prices)):
        if low == prices[i]:
            best = i
    return best

