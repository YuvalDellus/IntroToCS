# # import xml.etree.ElementTree as ET
# # from ex5 import *
# #
# #
# # # tree = ET.parse('Store_1.xml')
# # # root = tree.getroot()
# # # stord_Id = root.find("StoreId").text
# # # my_item = dict()
# # # store_contain = dict()
# # # element = root.find("Items")
# # # items = element.findall("Item")
# # # for item in items:
# # #     for detail in item:
# # #         my_item[detail.tag] = detail.text
# # #     store_contain[item.find("ItemCode")] = my_item
# # # full_store = dict()
# # # full_store[stord_Id] = store_contain
# # # print(full_store)
# #
# #
# # # a = """0060200]	{פתיתים אפויים קוסקוס500ג}
# # # [7290100929728]	{מרכך ארומה סגול 900מל}
# # # [7290006385178]	{לחם שאור+אגוז+צימ.ח.א525}
# # # [7290004165017]	{רסק תפו"ע בלי סוכר560גרם}
# # # [7290101869917]	{איירוויק מילוי 250מל}
# # # [7290011618162]	{ביסקו.שוק.שמנת זביונה180}
# # # [7290001136973]	{ארומה סבון מועשר בלחות1ל"""
# # # numbers_list = list()
# # # temp = list()
# # # final = list()
# # # for (i, letter) in enumerate(a):
# # #     if letter == "[":
# # #         temp = a[i+1:]
# # #         for (i, letter) in enumerate(temp):
# # #             if letter == "]":
# # #                 final = temp[:i]
# # #                 numbers_list.append(final)
# # #                 break
# # #                 temp = []
# # #                 final = []
# # #             elif letter == "[":
# # #                 break
# # #                 temp = []
# # #                 final = []
# # # print(numbers_list)
# # # #
# # # print(create_basket_from_txt(a))
# #
# # store_db = {'59907': {'ManufacturerName': 'מעדנות בע"מ',
# #       'ManufactureCountry': 'IL', 'Quantity': '500.00','ItemCode': '59907',
# #       'ItemPrice': '26.10', 'PriceUpdateDate': '2014-07-22 08:09',
# #       'UnitOfMeasure': '100 גרם', 'ItemName': 'פיצה משפחתית'},
# #       '66196': {'ManufacturerName': 'אסם',
# #       'ManufactureCountry': 'IL', 'Quantity':
# #       '200.00', 'ItemCode': '66196', 'ItemPrice': '3.80',
# #       'PriceUpdateDate': '2015-05-19 08:34',
# #       'UnitOfMeasure': '100 גרם', 'ItemName': 'ביסלי גריל'},
# #       '30794': {'ManufacturerName': 'תנובה',
# #       'ManufactureCountry': 'IL', 'Quantity': '1.00',  'ItemCode': '30794',
# #       'ItemPrice': '10.90', 'PriceUpdateDate': '2013-12-08 13:48',
# #       'UnitOfMeasure': 'ליטר', 'ItemName': 'משקה סויה'},
# #       '13520': {'ManufacturerName': 'יוניליוור',
# #       'ManufactureCountry': 'IL', 'Quantity': '75.00', 'ItemCode': '13520',
# #       'ItemPrice': '4.90', 'PriceUpdateDate': '2015-07-07 08:26',
# #       'UnitOfMeasure': '100 גרם', 'ItemName': 'קליק קורנפלקס'},
# #       '84316': {'ManufacturerName': 'החברה המרכזית לייצור משקאות',
# #       'ManufactureCountry': 'IL', 'Quantity': '1.50', 'ItemCode': '84316',
# #       'ItemPrice': '7.20', 'PriceUpdateDate': '2013-12-31 07:28',
# #       'UnitOfMeasure': 'ליטר', 'ItemName': 'קוקה קולה בקבוק 1.5 ליטר'}}
# #
# # # basket = ['84316','13520','30794',"555"]
# # # prices = list()
# # # for code in basket:
# # #     if code in store_db and code in store_db[code]["ItemCode"]:
# # #         prices.append(float(store_db[code]["ItemPrice"]))
# # #     else:
# # #         prices.append(None)
# # # print(prices)
# #
# # def store():
# #     tree = ET.parse('Store_1.xml')
# #     root = tree.getroot()
# #     stord_Id = root.find("StoreId").text
# #     element = root.find("Items")
# #     items = element.findall("Item")
# #     my_item = dict()
# #     store_contain = dict()
# #     counter = 0
# #     for item in items:
# #         # print(item.tag)
# #         counter +=1
# #         for detail in item:
# #             # print(detail.tag)
# #             my_item[detail.tag] = detail.text
# #         store_contain[item.find("ItemCode").text] = dict(my_item)
# #         my_item = dict()
# #         item = ""
# #         # if counter == 10:
# #         #     break
# #     return stord_Id, store_contain
# #
# # store_db = store()
# #
# # # print(aa)
# #
# # basket = ['1349511350']
# # prices = list()
# # for code in basket:
# #     # print(store_db[1][code])
# #     # print(code in store_db[1])
# #     if code in store_db[1] :#and code == store_db[1][code]["ItemCode"]:
# #         print("aaa")
# #         prices.append(float(store_db[1][code]["ItemPrice"]))
# #     else:
# #         prices.append(None)
# # print(prices)
#
# # list_of_price_list = [[5.0,2.0,8.0],[6.0,None,3.0],[9.0,5,3.0]]
# #
# # store_1, store_2, store_3 = list_of_price_list
# #
# # print(store_1)
# #
# # a = max(store_1)
# # for i in range(len(store_1)):
# #     if a == store_1[i]:
# #         print(i)
# # print(max(None, 1))
#
#
#
# # sum_1, sum_2, sum_3 = 0, 0, 0
# # prices = list()
# # store_1, store_2, store_3 = list_of_price_list
# # best = 0
# #
# # for i in range(len((store_1))):
# #     if store_1[i] is None:
# #         if store_2[i] is None:
# #             sum_1 += store_3[i] * 1.25
# #         elif store_3[i] is None:
# #             sum_1 += store_2[i] * 1.25
# #         else:
# #             sum_1 += max(store_2[i], store_3[i]) * 1.25
# #         continue
# #
# #     if store_2[i] is None:
# #         if store_1[i] is None:
# #             sum_2 += store_3[i] * 1.25
# #         elif store_3[i] is None:
# #             sum_2 += store_1[i] * 1.25
# #         else:
# #             sum_2 += max(store_1[i], store_3[i]) * 1.25
# #         continue
# #
# #     if store_3[i] is None:
# #         if store_1[i] is None:
# #             sum_3 += store_2[i] * 1.25
# #         elif store_2[i] is None:
# #             sum_3 += store_1[i] * 1.25
# #         else:
# #             sum_3 += max(store_1[i], store_2[i]) * 1.25
# #         continue
# #
# #     sum_1 += store_1[i]
# #     sum_2 += store_2[i]
# #     sum_3 += store_3[i]
# #     prices.append(sum_1, sum_2, sum_3)
# #     low = min(prices)
# #     for i in range(len(prices)):
# #         if low == prices[i]:
# #             best = i
# # return best
#
# # a = [1,2,3]
# # b = [4,5,6]
# # c = a+b
# # print(c)
# #
# # print(min(5.6,7.6))
#
# items = list()
# f = open('aaaaaa.txt', 'r')
# for line in f:
#     items.append(line[1:-2])  # slicing the "[]" and the "\n"
# f.close()
# print(items)

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
    best = 0

    for i in range(len((store_1))):  # arbitrary Store for length
        if store_1[i] is None:
            if store_2[i] is None:
                sum_1 += store_3[i] * PENALTY
            elif store_3[i] is None:
                sum_1 += store_2[i] * PENALTY
            else:
                sum_1 += max(store_2[i],store_3[i]) * PENALTY
        else:
            sum_1 += store_1[i]

        if store_2[i] is None:
            if store_1[i] is None:
                sum_2 += store_3[i] * PENALTY
            elif store_3[i] is None:
                sum_2 += store_1[i] * PENALTY
            else:
                sum_2 += max(store_1[i],store_3[i]) * PENALTY
        else:
            sum_2 += store_2[i]

        if store_3[i] is None:
            if store_1[i] is None:
                sum_3 += store_2[i] * PENALTY
            elif store_2[i] is None:
                sum_3 += store_1[i] * PENALTY
            else:
                sum_3 += max(store_1[i],store_2[i]) * PENALTY
        else:
            sum_3 += store_3[i]

    prices.append(sum_1)
    prices.append(sum_2)
    prices.append(sum_3)
    low = min(prices)
    for i in range(len(prices)):
        if low == prices[i]:
            best = i
    return best