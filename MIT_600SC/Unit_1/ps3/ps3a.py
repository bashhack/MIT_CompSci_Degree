# 6.00 Problem Set 3A
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

# Problem Set 3a
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 4 hours


import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------


#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word multiplied by the length of the word, plus 50
    points if all n letters are used on the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    wordlen = len(word)
    score = 0

    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            score += SCRABBLE_LETTER_VALUES[letter] * wordlen

    if wordlen == n:
        return score + 50
    return score


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,  # print all on the same line
    print  # print an empty line


#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    >> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    >> display_hand(hand)
    a q l l m u i
    >> hand = update_hand(hand, 'quail')
    >> hand
    {'l': 1, 'm': 1}
    >> display_hand(hand)
    l m

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    _hand = hand.copy()
    for letter in word:
        _hand[letter] -= 1
    return _hand

    # Original (I had originally read the specs as detailing a
    #           return value of all k, v pairs with v > 0...tests
    #           pass with the amended version, but would like to
    #           keep both for my own reference):
    # _hand = {}
    # word_freq = get_frequency_dict(word)

    # for k, v in hand.items():
    #     if k in word_freq:
    #         remaining_count = hand[k] - word_freq[k]
    #         if remaining_count >= 1:
    #             _hand[k] = remaining_count
    #     else:
    #         _hand[k] = hand[k]
    # return _hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings

    """
    if word not in word_list:
        return False

    word_freq = get_frequency_dict(word)

    for k, v in word_freq.items():
        # if freq of letter in word is greater
        # than occurance in hand, return False
        if v > hand.get(k, 0):
            return False

    return True


def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen


#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings

    """
    len_count = calculate_handlen(hand)
    score_total = 0

    while calculate_handlen(hand) > 0:
        print 'Current hand: '
        display_hand(hand)
        user_word = raw_input(
            '''Please enter a word, or type "." to end the game. '''
        )

        if user_word == '.':
            print 'Thanks for playing! Total score: {} points'.format(
                score_total
            )
            return
        else:
            is_valid = is_valid_word(user_word, hand, word_list)
            if is_valid:
                score = get_word_score(user_word, len_count)
                hand = update_hand(hand, user_word)
                score_total += score
                print 'You\'ve recieved {} point(s) for the word: {}'.format(
                    score,
                    user_word,
                )
            else:
                print 'Sorry, please select another word!'
    print 'You\'re out of letters. Total score: {} points.'.format(score_total)


#
# Problem #5: Playing a game
# Make sure you understand how this code works!

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    game_prompt_msg = '''
    Please type "n" to start a new game,
    "r" to replay previous game hand,
    or "e" to exit the game:
    >> '''

    hand = deal_hand(HAND_SIZE)

    while True:
        user_reply_to_game_prompt = raw_input(game_prompt_msg)
        if user_reply_to_game_prompt == 'e':
            print 'Sorry to see you go - but, thanks for playing!'
            return False
        elif user_reply_to_game_prompt == 'n':
            print 'Playing a new hand.'
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
        elif user_reply_to_game_prompt == 'r':
            print 'Now replaying the last hand.'
            play_hand(hand.copy(), word_list)
        else:
            print 'Sorry! Invalid input, please try again.'


#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
