import hangman_helper

MAX_ERRORS = 6
WIN_MSG = 'Correct guess, this is the word!!!'
LOSS_MSG = 'You have run out of guesses, the word was: '
ALREADY_CHOSEN_MSG = 'You have already chosen '
NON_VALID_MSG = 'Please enter a valid letter'
HINT_MSG = 'Consider choosing: '
NO_HINTS_MSG = 'Hints not supported'
DEFAULT_MSG = ''
HINT = 1
LETTER = 2
PLAY_AGAIN = 3

LETTER_PLACE = 1
START_GAME_ERRORS = 0


def update_word_pattern(word, pattern, letter):
    """Checks if the letter in the world and updates the pattern"""
    temp_pattern = list(pattern)  # easier to manipulate a list
    for (i, l) in enumerate(pattern):  # runs on the index instead the letter
        if word[i] == letter:
            temp_pattern[i] = letter
    temp_pattern = "".join(temp_pattern)  # back to string
    return temp_pattern


def filter_words_list(words, pattern, wrong_guess_lst):
    """ generates filtered list with all the words that can mach"""
    first_filtration_list = [word for word in words if len(word) == len(pattern)]
    # first filtration only words in the same length of our pattern
    real_filtered = first_filtration_list[:]

    for word in first_filtration_list:
        # running on the first filtration list but removing from the second
        # list to avoid index problems
        for wrong_letter in wrong_guess_lst:
            if wrong_letter in word and word in real_filtered:
                real_filtered.remove(word)
                break  # one wrong letter is enough

        for letter in range(len(pattern)):
            if word[letter] != pattern[letter] and pattern[letter] != "_" and word in real_filtered:
                real_filtered.remove(word)
                # check and remove any word that not in the same pattern as
                # the given pattern
                break  # one wrong letter is enough

    return real_filtered


def choose_letter(words, pattern):
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
        reverse_frequency_list.append((frequency[letter], letter))

    hint_letter = max(reverse_frequency_list)[LETTER_PLACE]

    return hint_letter


def run_single_game(words_list):
    """reboots the parameters and run the game"""
    word = hangman_helper.get_random_word(words_list)
    pattern = "_"*len(word)  # the pattern in the length of the word
    error_count = START_GAME_ERRORS
    wrong_guess_lst = list()
    msg = DEFAULT_MSG

    while "_" in pattern and error_count != MAX_ERRORS:  # all time we still
        # have guesses to do and didn't out of errors
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg)
        letter = hangman_helper.get_input()[LETTER_PLACE]  # getting the letter

        if letter is True:  # in case of a HINT the boolean will be True
            filtered_list = filter_words_list(words_list, pattern, wrong_guess_lst)
            words_list = filtered_list  # for next hint iteration
            hint = choose_letter(filtered_list, pattern)
            msg = HINT_MSG + hint

        elif len(letter) != 1 and letter.isalpha() or letter == letter.upper():
            # checks all the restricts of being one lower case letter
            msg = NON_VALID_MSG

        elif letter in wrong_guess_lst:
            # in case we already wrong guessed the letter
            msg = ALREADY_CHOSEN_MSG + str(letter)

        elif letter in word:
            # guessed right, the letter will be shown on the pattern
            pattern = update_word_pattern(word, pattern, letter)
            msg = DEFAULT_MSG

        else:
            # guessed wrong, the letter will enter to the wrong guesses list
            wrong_guess_lst.append(letter)
            error_count += 1
            msg = DEFAULT_MSG

    if pattern == word:
        # guess correctly all the letters
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, WIN_MSG)
    else:
        # didn't success guessing all the letters
        msg = LOSS_MSG + word
        hangman_helper.display_state(pattern, error_count, wrong_guess_lst, msg, True)


def main():
    """initializing the game"""
    words_list = hangman_helper.load_words()
    run_single_game(words_list)
    while hangman_helper.get_input()[1]:
        # while user choose keep playing, the value will be True
        run_single_game(words_list)


if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()
