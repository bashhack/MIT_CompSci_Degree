def keySearch(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None


def hanoi(n, f, t, s):
    assert n > 0
    if n == 1:
        print 'move from', f, 'to', t
    else:
        hanoi(n - 1, f, s, t)
        hanoi(1, f, t, s)
        hanoi(n - 1, s, t, f)


for i in range(1, 5):
    print 'New Hanoi Example: hanoi(', i, ', "f", "t", "s")'
    print '----------------------'
    print hanoi(i, 'f', 't', 's')


print hanoi(1, 'f', 't', 's')
print hanoi(5, 'f', 't', 's')


def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c
    return ans


def checkForPalindrome(s, indent=' '):
    print indent, 'checkForPalindrome called with', repr(s)
    if len(s) <= 1:
        print indent, 'About to return True from base case'
        return True
    else:
        ans = (
            # [1:-1] makes copy without first/last
            s[0] == s[-1] and checkForPalindrome(s[1:-1], indent + indent)
        )
        print indent, 'About to return', ans, 'for', s
        return ans


def isPalindrome(s):
    """
    Returns True if s is a palindrome, and False otherwise
    """
    return checkForPalindrome(toChars(s))


print isPalindrome('racecar')
print isPalindrome('laughton')


def fibonacci(n):
    """
    assumes n an int != 0
    returns Fibonacci of n
    """
    assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test_fib(n):
    for i in range(n + 1):
        print 'fib of', i, '=', fibonacci(i)


test_fib(6)


def listToTuple(L):
    r = ()
    for elem in L:
        r += (elem,)
    return r


print listToTuple([1, 2, 3, 4, 5])


def tupleToList(T):
    r = []
    for elem in T:
        r.append(elem)
    return r


print tupleToList((1, 2, 3, 4, 5))

D1 = {1: 'one', 'two': 2, 'apple': 3, 4: 52}

keys = D1.keys()
# keys.sort()
# print keys

print D1
for k, v in D1.items():
    print 'k=', k, 'v=', v
