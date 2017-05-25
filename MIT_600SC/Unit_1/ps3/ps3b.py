# 6.00 Problem Set 3B
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

# Problem Set 3b
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 2 hours 30 minutes


from ps3a import *
import time
from perm import *


#
# Problem #6A: Computer chooses a word
#
def comp_choose_word(hand, word_list):
    """Given a hand and a word_dict, find the word that gives the
    maximum value score, and return it. This word should be
    calculated by considering all possible permutations of lengths
    1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    perms = []
    max_score = 0
    word_with_max_score = None

    for length in range(1, HAND_SIZE + 1):
        perms.extend(get_perms(hand, length))

    for word in perms:
        if word in word_list:
            curr_score = get_word_score(word, HAND_SIZE)

            if curr_score > max_score:
                max_score = curr_score
                word_with_max_score = word

    # print 'Word with highest score was \'{}\' and earned {} points'.format(
    #     word_with_max_score,
    #     max_score
    # )

    return word_with_max_score


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its
       possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    len_count = calculate_handlen(hand)
    score_total = 0

    while calculate_handlen(hand) > 0:
        print 'Current hand: '
        display_hand(hand)
        comp_word = comp_choose_word(hand, word_list)
        if comp_word is None:
            break
        else:
            score = get_word_score(comp_word, len_count)
            score_total += score
            hand = update_hand(hand, comp_word)
            print 'Computer recieved {} point(s) for the word: {}'.format(
                score,
                comp_word,
            )

    print 'Computer out of letters. Total score: {} points.'.format(
        score_total
    )


#
# Problem #6C: Playing a game
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game
      as before using play_hand.
    * If the user inputs 'c', let the computer play the game
      using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    game_prompt_msg = '''
    Please type "n" to start a new game,
    "r" to replay previous game hand,
    or "e" to exit the game:
    >> '''

    player_select_msg = '''
    Please type "u" to play the game,
    or type "c" to let the computer play the game:
    >> '''

    hand = deal_hand(HAND_SIZE)

    while True:
        user_cmd = raw_input(game_prompt_msg)
        while user_cmd != 'n' and user_cmd != 'e' and user_cmd != 'r':
            print 'Sorry! Invalid input, please try again.'
            user_cmd = raw_input(game_prompt_msg)

        if user_cmd == 'e':
            print 'Sorry to see you go - but, thanks for playing!'
            return False

        player = raw_input(player_select_msg)
        while player != 'u' and player != 'c':
            print 'Sorry! Invalid input, please try again.'
            player = raw_input(player_select_msg)

        if user_cmd == 'n':
            print 'Playing a new hand.'
            hand = deal_hand(HAND_SIZE)

        if user_cmd == 'r':
            print 'Now replaying the last hand.'
            if player == 'u':
                play_hand(hand.copy(), word_list)
            else:
                comp_play_hand(hand.copy(), word_list)

        if player == 'u' and user_cmd != 'r':
            play_hand(hand.copy(), word_list)
        elif user_cmd != 'r':
            comp_play_hand(hand.copy(), word_list)


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
