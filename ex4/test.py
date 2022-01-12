def pattern_letters(pattern):
    """returns all the real letters in a pattern"""
    pattern_letters_lst = [letter for letter in pattern if letter != "_"]
    # pattern_letters_lst = list()
    # for letter in pattern:
    #     if letter != "_":
    #         pattern_letters_lst.append(letter)
    print(pattern_letters_lst)

    return pattern_letters_lst

def filter_words_list(words, pattern, wrong_guess_lst):
    """ generates filtered list with all the words that can mach"""
    first_filtration = [word for word in words if len(word) == len(pattern)]
    # first filtration only words in the same length of our pattern
    real_filtered = first_filtration[:]
    pattern_letters_lst = pattern_letters(pattern)


    for word in first_filtration:
        # running on the first filtration list but removing from the second
        # list to avoid index problems
        for wrong_letter in wrong_guess_lst:
            if wrong_letter in word and word in real_filtered:
                real_filtered.remove(word)
                break  # one wrong letter is enough

        for letter in range(len(pattern)):
            if word[letter] != pattern[letter] and pattern[letter] != "_" and\
                            word in real_filtered:
                real_filtered.remove(word)
                # check and remove any word that not in the same pattern as
                # the given pattern
                break  # one wrong letter is enough

        for letter in pattern_letters_lst:
            for i in range(len(pattern)):
                if letter in word and word[i] == letter and pattern[i] == "_" \
                        and word in real_filtered:
                    real_filtered.remove(word)
                    # check and remove any word that have a guessed letter not
                    # in the same place as the pattern
                    break # one wrong letter is enough

    return real_filtered


def choose_letter(words, pattern):
    """gives the most frequent letter as a hint"""
    frequency = {}
    reverse_frequency_list = list()
    for word in words:
        for letter in word:
            if letter not in pattern:
                if letter not in frequency:
                    frequency[str(letter)] = 1
                else:
                    frequency[str(letter)] += 1

    for letter in frequency:
        # switching key and value in the dic to be able using the max function
        reverse_frequency_list.append((frequency[letter], letter))

    hint_letter = max(reverse_frequency_list)[LETTER_PLACE]
    # getting list of tuples, want the letter data out of it

    return hint_letter


words = ["aaa", "afc", "hello", "dog", "ahg", "aba"]
pattern = "a__"
wrong_guess_lst = []

print(filter_words_list(words, pattern, wrong_guess_lst))
