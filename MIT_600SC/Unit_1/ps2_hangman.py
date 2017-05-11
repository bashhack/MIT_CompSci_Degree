# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print "Loading word list from file..."

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)

    # line: string
    line = inFile.readline()

    # wordlist: list of strings
    wordlist = string.split(line)

    print "  ", len(wordlist), "words loaded."

    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """

    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program


wordlist = load_words()

# your code begins here!


# =============================================================================
# Utilities
# =============================================================================

def get_word(xs):
    return random.choice(xs)


def prompt_for_guess(msg):
    return raw_input(msg)


def show_msg(msg, *data):
    print msg.format(*data)


def display_word(g, accum_g):
    r = ''
    for c in g['word']:
        if g['guess'] == c or c in accum_g:
            r += c
        else:
            r += '_'
    return r


def update_letters(xs, g=None):
    # if xs.find(g) == -1:
    #     print 'Sorry, letter already used! Please choose another letter:'
    #     return prompt_for_guess(guess_msg)
    # else:
        xs = xs.replace(g, '')
        return xs


def check_guess(w, g):
    _g = g.lower()
    return {
        'word': w,
        'guess': _g,
        'found': _g in w,
    }


# =============================================================================
# Declarations
# =============================================================================

spacer_msg = '\n' + ('-' * 60)
intro_msg = '''Welcome to the game, Hangman!
I am thinking of a word that is {} letters long.{}'''

show_guess_count_msg = 'You have {} guesses left.'
guess_choice_msg = 'Available letters: {}'
guess_msg = 'Please guess a letter: '
round_update_msg = '{}{}{}'

incorrect_guess_msg = 'Oops! That letter is not in my word: '
correct_guess_msg = 'Good guess: '

win_msg = 'Congratulations, you won!'
lose_msg = '''You lost this one, better luck next time!
The word was: {}'''

word_to_guess = get_word(wordlist)
letters_available = 'abcdefghijklmnopqrstuvwxyz'

# =============================================================================
# State
# =============================================================================

guessed_so_far = ''
word_shown_to_user = ''
guess_count = 8


# =============================================================================
# Main Game Loop
# =============================================================================

show_msg(intro_msg, str(len(word_to_guess)), spacer_msg)

while guess_count > 0:
    show_msg(show_guess_count_msg, guess_count)
    show_msg(guess_choice_msg, letters_available)

    user_guess = check_guess(word_to_guess, prompt_for_guess(guess_msg))
    letters_available = update_letters(letters_available, user_guess['guess'])
    guessed_so_far += user_guess['guess']
    word_shown_to_user = display_word(user_guess, guessed_so_far)

    if user_guess['found']:
        show_msg(
            round_update_msg,
            correct_guess_msg,
            word_shown_to_user,
            spacer_msg,
        )

        if word_shown_to_user == word_to_guess:
            show_msg(win_msg)
            sys.exit(0)
    else:
        guess_count -= 1
        show_msg(
            round_update_msg,
            incorrect_guess_msg,
            word_shown_to_user,
            spacer_msg,
        )

show_msg(lose_msg, word_to_guess)

# =============================================================================
# End Main Game Loop
# =============================================================================
