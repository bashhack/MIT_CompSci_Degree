# Quiz 1
# =============================================================================
#
# NOTE: Original quiz handout questions are provided in `./MIT6_00SC11_q1.pdf`
#

# 1)
#   1.1) In Python the values of a dict must be immutable - FALSE, the keys must be immutable
#   1.2) There exist problems that cannot be solved in Python without using either
#        iteration or recursion - TRUE
#   1.3) Floating point arithmetic behaves exactly like normal arithmetic on real
#        numbers. - FALSE, floating point arithmetic is going to bound by rules of approximation
#   1.4) On all inputs, a bisection search will run faster than a linear search - FALSE,
#        while on many inputs this is the case, if we have the element to search for
#        located at index 0, linear search will be computationally more efficient
#   1.5) Let L be a list, each element of which is a list of ints. In Python, the
#        assignment statement L[0][0] - 3 mutates the list L - FALSE, it mutates the inner element list

# 2) What does the following code print?
T = (0.1, 0.1)
x = 0.0
for i in range(len(T)):  # value at loop 1: 0, value at loop 2: 1
    for j in T:  # value at loop 1: 0.1, value at loop 2: 0.1
        x += i + j
        # outer: 1, inner: 1: x = 0 + 0.1,
        # outer: 1, inner: 2: 0.1 + 0.1 + 0
        # outer: 2, inner: 1: 0.2 + 0.1 + 1
        # outer: 2, inner: 2: 1.3 + 0.1 + 1
        print x
print i

# Answer to 2:
# 0.1
# 0.2
# 1.3
# 2.4
# 1 => value of i outside loop

# 3) What does the following code print?
def f(s):
    if len(s) <= 1:
        return s
    # f(f('at')) + 'm'
    # f(f('t')) + 'a'
    # f('ta') => will reverse these => 'at' + 'm'

    # f(f('ath')) + 'm'
    # f(f('th')) + 'a'
    # f(f('h')) + 't'
    # ? - having trouble from here on out...
    return f(f(s[1:])) + s[0]  # Note double recursion
print f('mat')
print f('math')

# Answer to 3:
# atm
# ? - Not sure here


# 4) Implement the body of the function specified in the box:
def findAll(wordList, lStr):
    """assumes: wordList is a list of words in lowercase.
                lStr is a str of lowercase letters.
                No letter occurs in lStr more than once.
       returns: a list of all the words in lStr exactly once
                and no letters not in lStr"""


# Answer to 4:
def findAll(wordList, lStr):
    """assumes: wordList is a list of words in lowercase.
                lStr is a str of lowercase letters.
                No letter occurs in lStr more than once.
       returns: a list of all the words in lStr exactly once
                and no letters not in lStr"""
    result = []
    lStr_sorted = ''.join(sorted(lStr))
    for word in wordList:
        if ''.join(sorted(word)) == lStr_sorted:
            result.append(word)
    return result

# 5) The following code deos not meet its specification. Correct it.
def addVectors(v1, v2):
    """assumes v1, and v2 are lists of ints.
       Returns a list containing the pointwise sum of the elements
       in v1 and v2. For example, addVectors([4, 5], [1, 2, 3]) returns
       [5, 7, 3], and addVectors([], []) returns []. Does not modify inputs."""
    if len(v1) > len(v2):
        result = v1
        other = v2
    else:
        result = v2
        other = v1
    for i in range(len(other)):
        result[i] += other[i]
    return result

# Answer to 5:
def addVectors(v1, v2):
    """assumes v1, and v2 are lists of ints.
       Returns a list containing the pointwise sum of the elements
       in v1 and v2. For example, addVectors([4, 5], [1, 2, 3]) returns
       [5, 7, 3], and addVectors([], []) returns []. Does not modify inputs."""
    if len(v1) > len(v2):
        result = v1[:]  # create a copy to avoid mutation
        other = v2
    else:
        result = v2[:]  # create a copy to avoid mutation
        other = v1
    for i in range(len(other)):
        result[i] += other[i]
    return result


# 6) Consider the following code:
def f(s, d):
    for k in d.keys():
        d[k] = 0
        # a reset of d2 will occur here
    for c in s:
        if c in d:
            d[c] += 1
            # d2
            # d = {'a': 0, 'b': 0, 'c': 0} # after reset
            # d = {'a': 0, 'b': 1, 'c': 0}
            # d = {'a': 0, 'b': 2, 'c': 0}
            # d = {'a': 0, 'b': 2, 'c': 1}
            # d = {'a': 1, 'b': 2, 'c': 1}
            # d = {'a': 2, 'b': 2, 'c': 1}
        else:
            # d1
            # d = {}
            # d = {'a': 0}
            # d = {'a': 0, 'b': 0}
            # d = {'a': 0, 'b': 1}
            # d = {'a': 0, 'b': 1, 'c': 0}
            d[c] = 0
    return d

def addUp(d):
    result = 0
    for k in d:
        result += d[k]
    return result

d1 = {}
d2 = d1
d1 = f('abbc', d1)
print addUp(d1)
d2 = f('bbcaa', d2)
print addUp(d2)
print f('', {})
print result

#   6.1) What does it print?
#   6.2) Does it terminate normally? Why or why not?

# Answer to 6.1:
# 1
# 5
# {}

# Answer to 6.2:
# 'No, we will encounter a NameError because `result` is not a global and will be undefined in outer scope'

# 7) Consider the following code:
def logBase2(n):
    """assumes that n is a postivie int
       returns a float that approximates the log base 2 of n"""
    import math
    return math.log(n, 2)

def f(n):
    """assumes n is an int"""
    if n < 1:
        # n = 0
        # curDigit = 0
        return
    curDigit = int(logBase2(n))
    # n = 1
    # curDigit = 0
    # if 1 % (2**0) < 1
    # if 1 % 1 < 1
    # if 0 < 1 => True
    # ans = '' += '1'

    # n = 2
    # curDigit = 1
    # if 1 % (2**1) < 2
    # if 1 % 2 < 2
    # if 1 < 2 => True
    # n = 2 - 2**1 = 0
    # curDigit = 0
    # if 0 % (2**0) < 0
    # if 0 % 1 < 0
    # if 0 < 0 => False
    # ans = '1' += '0' => '10'
    ans = 'n ='
    while curDigit >= 0:
        if n % (2**curDigit) < n:
            ans = ans + '1'
            n = n - 2**curDigit
        else:
            ans = ans + '0'
        curDigit -= 1
    return ans

for i in range(3):
    print f(i)

#   7.1) What does it print?
#   7.2) Under the assumption that logBase2 is O(n), what is the order (use big Oh notation) of f?

# Answer to 7.1:
# None
# 1
# 10


# Answer to 7.2:
# 'The runtime complexity here should still be O(n), because our total runtime is O(n) + log2(n).'

# 8) Next to each item in the left column write the letter labeling the item in the right column that best matches
#    the item in the left column. No item in the right column should be used more than once.

# [ b ] Big O notation                             a) induction

# [ d ] Newton's method                            b) upper bound

# [ a ] recursion                                  c) lower bound

#                                                  d) approximation

#                                                  e) expected running time

#                                                  f) exponential

# 9) Do you think that the lectures are too slow paced, too fast paced, about right?
# Answer to 9:
# "I've been able to keep up with things reasonably well - though I wish we had spent more time on
# Selection Sort."

# 10) Do you think that the problem sets are too easy, too hard, about right?
# Answer to 10:
# "The problem sets so far have been a challenge (that is, each has required a bit of digging and research
# into new concepts and/or some study to reinforce existing knowledge, which is great, too). That level of
# challenge, though, feels about right."
