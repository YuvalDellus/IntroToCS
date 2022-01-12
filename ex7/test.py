def print_sequences_helper(char_list, n, comb_list):
    if len(comb_list) == n:
        print(comb_list)
    for char in char_list:
        if len(comb_list) < n:
            comb_list.append(char)
            print_sequences_helper(char_list, n, comb_list)
            comb_list.remove(char)


def print_sequences(char_list, n):
    comb_list = list()
    print_sequences_helper(char_list, n, comb_list)


# print_sequences(['a','b'], 3)

def print_sequences_helper(char_list, n, comb_list,i):
    i += 1
    if i == n:
        print(comb_list)
        return
    for x in char_list:
        comb_list[i] = x
        print_sequences_helper(char_list, n, comb_list, i)


def print_sequences(char_list, n):
    comb_list = ["0"]*n
    comb_list[0] = char_list[0]
    print_sequences_helper(char_list, n, comb_list,-1)


print_sequences(['a','b','c'], 3)