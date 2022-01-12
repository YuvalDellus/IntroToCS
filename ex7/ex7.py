############################################################
# FILE : ex7.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION :  different recursive applications
############################################################


def print_to_n(n):
    """
    prints all the numbers to n increasing order
    """
    if n == 0:
        return None
    if n > 0:
        print_to_n(n - 1)
        print(n)


def print_reversed(n):
    """
    prints all the numbers to n decreasing order
    """
    if n > 0:
        print(n)
    if n == 1:
        return None
    if n > 0:
        print_reversed(n - 1)


def has_divisor_smaller_than(n, i):
    """
    An assist function to 'is prime' function, checks if the number divise in
    all the natural number till the root of the number
    """
    if i == int(n ** 0.5) + 1:  # need to check only to the root + 1
        return True
    elif n % i == 0:
        return False  # if the number divise return false
    else:
        return has_divisor_smaller_than(n, i + 1) and True


def is_prime(n):
    """
    calculate if a given number is a prime or not, using an assist function
    """
    if n > 1:
        return has_divisor_smaller_than(n, 2)
    return False


def divisor_helper(div_lst, n, i):
    """
    checks if a number divise the given number, and if so, saves it and return
    """
    if i == 1:  # if the number is 1 it will divise only by itself
        return 1
    elif n % i == 0:
        div_lst.append(i)  # saves a number that devise
    return divisor_helper(div_lst, n, i - 1)


def divisors(n):
    """
    A function that returns all the number that devise a given number, using
    assit function
    """
    divisors_lst = list()  # initiation list
    if n < 0:
        n = -n
    if n == 0:
        return divisors_lst
    divisors_lst.append(divisor_helper(divisors_lst, n, n))
    divisors_lst = divisors_lst[::-1]  # change the order from small to big
    return divisors_lst


def exp_helper(exp, i, x):
    """
    An assist function,  calculate the exponential of a given number
    """
    if i == 0:  # the exponential of 0 is 1
        return 1, 1  # returns the sum and the factorial

    summation, factorial_base = exp_helper(exp, i - 1, x)
    exp = summation + x ** i / (factorial_base * i)  #calculate the exponential
    return exp, factorial_base * i


def exp_n_x(n, x):
    """
    returns exponential sum
    """
    exp = 0
    if n >= 0:
        exp += exp_helper(exp, n, x)[0]
    return exp


def play_hanoi(hanoi, n, src, dest, temp):
    """
    runs the hanoi tower game
    """
    if n <= 0:  # illegal number of discs
        return
    if n == 1:  # when we have 1 disc, move it
        hanoi.move(src, dest)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)  # moves the discs to temp
        play_hanoi(hanoi, 1, src, dest, temp)  # moves 1 disc to the target
        play_hanoi(hanoi, n - 1, temp, dest, src)  # moves discs from temp to
                                                   # target


def print_binary_sequences_with_prefix(prefix, n, counter):
    """
    receive a list and change the next index to 0 or 1
    """
    counter += 1
    if counter == len(prefix):  # ran over all the list
        print("".join(prefix))
        return
    if counter < len(prefix):  # when didn't run all over the list yet
        prefix[n] = "1"
        print_binary_sequences_with_prefix(prefix, n - 1, counter)
    if counter < len(prefix):  # when didn't run all over the list yet
        prefix[n] = "0"
        print_binary_sequences_with_prefix(prefix, n - 1, counter)


def print_binary_sequences(n):
    """
    print all the possible combinations of 0 and 1 in a length of n
    """
    prefix = ["0"]*n
    print_binary_sequences_with_prefix(prefix, n-1, -1)


def print_sequences_helper(char_list, n, comb_list, index):
    """
    Assist function, in each iteration enter a different letter from the list
    """
    index += 1
    if index == n:  # when ran all over the list length
        print("".join(comb_list))
        return
    for char in char_list:
        comb_list[index] = char  # entering different letter each iteration
        print_sequences_helper(char_list, n, comb_list, index)


def print_sequences(char_list, n):
    """
    prints all the combination of the letters in given list, in length of n,
    using an assist function
    """
    if n == 0:
        print("")
        return
    comb_list = ["0"]*n  # initialize the list
    comb_list[0] = char_list[0]  # entering the first letter to the list
    print_sequences_helper(char_list, n, comb_list, -1)


def check(list_to_check):
    """
    A function that check if a letter appears in a list more then once
    """
    for char in list_to_check:  # run on all the letters in the list
        temp_list = list_to_check[:]  # avoiding index problems
        temp_list.remove(char)
        if char in temp_list:
            return False  # if the letter still in the list after removing it,
                          # it appeard more then once
    return True


def print_no_repetition_sequences_helper(char_list, n, comb_list, i):
    """
    Assist function, in each iteration enter a different letter from the list
    """
    i += 1
    if i == n:  # when ran all over the list length
        if check(comb_list):  # when a letter appear only once will be True
            print("".join(comb_list))
        return
    for char in char_list:
        comb_list[i] = char  # entering different letter each iteration
        print_no_repetition_sequences_helper(char_list, n, comb_list, i)


def print_no_repetition_sequences(char_list, n):
    """
    prints all the combination of the letters in given list, in length of n,
    each letter can appear only once in the combination,
    using two assist functions
    """
    if n == 0:
        print("")
        return
    comb_list = ["0"]*n  # initialize the list
    print_no_repetition_sequences_helper(char_list, n, comb_list,-1)


def print_no_repetition_sequences_list_helper(char_list, n, comb_list, i, results_list):
    """
    Assist function, in each iteration enter a different letter from the list
    """
    i += 1
    if i == n:  # when ran all over the list length
        if check(comb_list):  # when a letter appear only once will be True
            item = "".join(comb_list)
            results_list.append(item)  # saves the relevant results
            return
        return
    for char in char_list:
        comb_list[i] = char # entering different letter each iteration
        print_no_repetition_sequences_list_helper(char_list, n, comb_list, i, results_list)
    return results_list  # returns the list after finish run all the sequences


def no_repetition_sequences_list(char_list, n):
    """
    returns a list of  all the combination of the letters in given list,
     in length of n, each letter can appear only once in the combination,
    using two assist functions
    """
    if n == 0:
        return [""]
    comb_list = ["0"]*n  # initialize the list
    results_list = list()
    return print_no_repetition_sequences_list_helper(char_list, n, comb_list, -1, results_list)

