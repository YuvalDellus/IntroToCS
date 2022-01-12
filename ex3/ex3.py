############################################################
# FILE : ex3.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex3 2016-2017
# DESCRIPTION :  At README
############################################################
import math


def create_list():
    """convert strings to a list"""
    string_from_user = []
    while True:
        temp_string = input()
        if temp_string != "":
            string_from_user.append(temp_string)
        else:
            break
    return string_from_user


def concat_list(str_lst):
    """convert list to a string"""
    string = ""
    for i in str_lst:  # each unit in the list
        string += i
    return string


def average(num_list):
    """do average to all numbers in a list"""
    counter = 0
    total_sum = 0
    if num_list == list():  # an empty list
        return None
    for i in num_list:  # each number in list
        counter += 1  # counting how many numbers
        total_sum += i  # summing all the numbers
    avg = total_sum / counter  # do average
    return avg


def cyclic(lst1, lst2):
    """determine if a list is cyclic of a given list"""
    if lst1 == lst2:  # if the lists are even we can spare the calculate
        return True
    counter = 0
    l = len(lst1)
    temp_lst = lst2[:]  # coping the list to not modify the input
    temp_lst = is_cyclic(temp_lst)  # generating cyclic possibility
    while lst1 != temp_lst:  # comparing the list with the cyclic option
        counter += 1
        temp_lst = is_cyclic(temp_lst)  # generating new cyclic possibility
        if temp_lst == lst1:  # we have cyclic!
            return True
        if counter == l:  # breaking point when generated all cyclic options
            return False


def is_cyclic(lst):
    """generate cyclic possibilities fo a given list"""
    temp_list = list()
    temp_list.append(lst[-1])  # entering the last unit of the given list
    del lst[-1]  # deleting the last unit of given unit
    temp_list += lst  # combine the list to generate cyclic possibility
    return temp_list


def histogram(n, num_list):
    """generating the histogram of a given list"""
    histo = [0] * n  # generate an empty histogram in n length
    numbers = []
    for num in num_list:  # check all the arguments in the list
        if num not in numbers:
            numbers.append(num)

    for i in numbers:  # check for each argument
        counter = 0  # zero the counting for every new argument
        for j in num_list:  # running on the original list
            if i == j:
                counter += 1  # counting each time we have the num in the list
        histo[i] = counter  # entering the counter in the right index
    return histo


def prime_factors(n):
    """calculate the prime factors of a number"""
    primes = []
    for i in range(2, int(math.sqrt(n))+2):
        if n % i == 0:  # if the number is a factor
            while n % i == 0:  # check how many times the factor divise the num
                primes.append(i)
                n /= i   # devise the num by the factor and checks agian
    return primes


def cartesian(lst1, lst2):
    """generates cartesian product of 2 give lists"""
    cartezs = []
    for i in lst1:
        for j in lst2:
            cartezs.append((i, j))  # enter each cartesian product to the list
    return cartezs


def pairs(n, num_list):
    """checks if addition of 2 numbers in a list can equal to a given number"""
    pairs_list = list()
    for i in num_list:
        for j in num_list:
            if i + j == n and i != j:  # checks addition and non repeats
                if [j, i] not in pairs_list:
                    pairs_list.append([i, j])
    return pairs_list
