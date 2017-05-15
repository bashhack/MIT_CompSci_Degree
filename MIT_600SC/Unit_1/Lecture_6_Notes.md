# MIT 6.00SC - Lecture 6 Notes
# ============================

* Recap of dictionaries, with a `keySearch` function to simulate dictionaries without dictionaries

* Retrieval of data from a dictionary in Python is constant time O(1) - wow! Very quick!

* Here we go, time to learn about recursion:
  - A way of describing problems
  - A way of designing solutions

* Elements of recursion:
  - Base case: direct answer
  - Recursive (inductive) case: reduce to a simpler version of the same problem, plus other simple ops

* Ex. 1:
b^n = {b * b * b * b} x n
    =  b * {b * b * b * b} x n - 1
    = b * b^n-1, if n > 0 and 1, if n = 0

```python
def simpleExp(b, n):
    if n = 0:
        return 1
    else:
        return b * simpleExp(b, n - 1)
```

* Ex. 2 (Tower of Hanoi) / Ex. 3 (Palindrome) / Ex. 4 (Fibonacci) are in `Lecture_6_Examples.py`

# Check Yourself
# ==================

1) What is recursion?
"Recursion is a method of solving a problem by means of calling a function itself repeatedly
until the input satisfies a base case."

2) What is a recursive case?
"The recursive case is the main work of the recursive function, where a simpler version
of the problem at hand is defined along with other simple operations."

3) What is a base case?
"The base case is the direct answer, where the recursion 'unwraps' and evaluated."

# Problem Set 3
# ==================

- Introduction:
In this problem set, you'll implement two different versions of the 6.00 wordgame!

Don't be intimidated by the length of this problem set. It's a lot of reading, but very doable.

Let's begin by describing the 6.00 wordgame. This game is a lot like Scrabble or Text Twist,
if you've played those. Letters are dealt to players, who then construct one or more words out of
their letters. Each valid word receives a score, based on the length of the word and the letters in
that word.

The rules of the game are as follows:

a) Dealing
   - A player is dealt a handof n letters chosen at random (assume n=7 for now)
   - The player arranges the hand into as many words as thy want out of the letters,
     but using each letter at most once.
   - Some letters may remain unused (those won't affect the score)
b) Scoring
   - The score for the hand is the sum of the score for the words times the lenght of the word
   - The score for a word is the sum of the point for letters in the word, multiplied by
     the length of the word, plus 50 points if all n letters are used on the first go.
   - Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2,
     E is worth 1, and so on. We have defined the dictionary

     `SCRABBLE_LETTER_VALUES`

     that maps each lowercase letter to its Scrabble letter value.
   - For example, 'weed' would be worth 32 points `((4+1+1+2)*4=32)`, as long as the hand
     actually has 1 'w', 2 'e's, and 1 'd'
   - As another example, if n=7 and you get 'waybill' on the first go, it would be worth
     155 points `((4+1+4+3+1+1+1)*7=105, +50)` for the bonus of using all seven letters

- Workload
Please let us know how long you spend on each problem. We want to be careful not to overload
you by giving out problems that take longer than we anticipated.

- Getting Started
1) Download and save the Problem Set 3 code files.
2) Run `ps3a.py` without making any modifications to it, in order to ensure that everything
   is set up correctly. The code we have given you loads a list of valid words from a file and
   then calls the `play_game` function. You will implement the functions it needs in order to
   work. If everything is okay, after a small delay, you should see the following printed out:
3) `Loading word list from file...
        83667 words loaded.`

   If you see an IOError instead (e.g., No such file or directory), you should change the value
   of the `WORDLIST_FILENAME` constant to the complete pathname for the file `words.txt`.
4) The file `ps3a.py` has a number of already implemented functions you can use while writing
   up your solution. You can ignore the code between the helper comments, though you should
   read and understand everything else.
5) This problem set is structured so that you will write a number of modular functions and
   then glue them together to form the complete word playing game. Instead of waiting until the
   entire game is 'ready', you should test each function you write, individually, before moving
   on. This aproach is known as 'unit testing' and it will help you debug your code.

We have provided several test functions to get you started. As you make progress on the problem set,
run `test_ps3a.py` as you go.

If your code passes the unit tests you will see a SUCCESS message; otherwise, you will see a
FAILURE message. These tests aren't exhaustive. You may want to test your code in other ways too.

If you run `test_ps3a.py` using the provided `ps3a.py` skeleton, you should see that all the
tests fail.

- PART A:
- Problem 1 - Word Scores
The first step is to implement some code that allows us to calculate the score for a single word.

The function `get_word_score` should accept a string of lowercase letters as input (a word) and
return the integer score for that word, using the game's scoring rules.

You may assume that the input word is always either a string of lowercase letters, or the empty
string "". You will want to use the `SCRABBLE_LETTER_VALUES` dictionary defined at the top of
`ps3a.py`. You should not change its value.

Do NOT assume that there are always 7 letters in a hand! The parameter n is the number of letters
required for a bonus score (the max number of letters in the hand).

Also test your implementation of `get_word_score` using some reasonable English words.

- Problem 2 - Dealing with hands
- Representing hands
A hand is the set of letters held by a player during the game. The player is initially dealt
a set of random letters. For example:

`a, q, l, m, u, i, l`

In our program, a hand will represented as a dictionary: the keys are (lowercase) letters and the
values are the number of times the particular letter is repeated in that hand. For example, the above
hand would be represented as:

`hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

Notice how the letter 'l' is represented.

Notice that with a dictionary representation, the usual way to access a value is `hand['a']`, where
'a' is the key we want to find. However, this only works if the key is in the dictionary; otherwise,
we get a `KeyError`. To avoid this, we can use the call `hand.get('a', 0)`. This is the 'safe' way to
access a value if we are not sure the key is in the dictionary. `d.get(key, default)` returns the value
for key if key is in the dictionary d, else default. If default is not given, it returns None, so that
this method never raises a KeyError.

- Converting words into dictionary representation
One useful function we've defined for you is `get_frequency_dict`, defined near the top of `ps3a.py`.
When given a string of letters as an input, it returns a dictionary where the keys are letters
and the values are the number of times that letter is represented in the input string.

- Displaying a hand
Given a hand represented as a dictionary, we want to display it in a user-friendly way. We have
provided the implementation for this in the `display_hand` function. Make sure you read through
this carefully and understand what it does and how it works.

- Generating a random hand
The hand a player is dealt is a set of letters chosen at random. We provide you with the
implementation of a function that gnereates this random hand, `deal_hand`. The function takes
as a positive integer n, and returns a new object, hand containing n lowercase letters.

- Removing letters from a hand (you implement this)
The player starts with a hand, a set of letters. As the player spells out words, letters
from this set are used up. For example, the player could start out with the following hand:

`a, q, l, m, u, i, l`

The player could choose to spell the word `quail`. This would leave the following letters in
the player's hand:

`l, m`

You will now write a function that takes a hand and a word as inputs, uses letters from that
hand to spell the word, and returns the remaining letters in the hand.

For example:
```python
>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
>> display_hand(hand)
a q l l m u i
>> hand = update_hand(hand, 'quail')
>> hand
{'l': 1, 'm': 1}
>> display_hand(hand)
l m
```

Implement the `update_hand` function. Make sure this function has no side effects!

TESTING: make sure the `test_update_hand()` tests pass. You may also want to test your
implementation of `update_hand` with some reasonable inputs.

- Problem 3 - Valid words
At this point, we have written code to generate a random hand and display that hand to
the user. We can also ask the user for a word (Python's `raw_input`) and score the word
(using your `get_word_score`). However, at this point we have not written any code to
verify that a word given by a player obeys the rules of the game.

A valid word is in the word list; AND it is composed entirely of letters from the current hand.

TESTING: Make sure the `test_is_valid_word` tests pass. In particular, you may want to test your
implementation by calling it multiple times on the same hand - what should the correct
behavior be here?

- Problem 4 - Playing a hand
We are now ready to begin writing code that interacts with the player.

Implement the `play_hand` function. This function allows the user to play out a single hand.

TESTING: Try out your implementation as if you were playing the game.

NOTE: Do NOT assume that there will always be 7 letters in a hand! The global variable
`HAND_SIZE` represents this value.

- Problem 5 - Playing a game
A game consists of playing multiple hands. We need to implement one final function to complete
our word-game program.

Write the code that implements the `play_game` function. You should remove the code that is currently
uncommented in the `play_game` body. Read through the specs and make sure you understand
what this function accomplishes.

- PART B:
- Problem 6A - Computer Word Choose
First we must create a function that allows the computer to choose a word.

We have provided the function `get_perms(hand, n)` (defined in `perm.py` but usable by
simply calling `get_perms(hand, n)`).

You are not required to know how `get_perms` works.

It is your responsibility to create the function `comp_choose_word(hand, word_list)`.

HINT: First try to make a legal player, and then worry about making the computer player better
(if you have time)

- Problem 6B - Computer's turn to play a hand
Now you need to write a function similar to Part A's `play_hand`.

Implement the `comp_play_hand` function. This function should allow the computer to play the
game through comletion.

- Problem 6C: U & Ur Computer
Now that your computer can choose a word, you need to give the computer the option to play.

Write the code that re-implements the `play_game` function. You will modify the function to behave
as described below in the function's comments.

As before you should use the `HAND_SIZE` constant to determine the number of cards in a hand.
If you like, you can try out different values for `HAND_SIZE` with your program.
