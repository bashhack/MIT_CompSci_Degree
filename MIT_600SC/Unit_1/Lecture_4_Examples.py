# Original (From Lecture 3)
# x = 0.5
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high + low)/2.0

# while abs(ans**2 - x) >= epsilon and ans <= x:
#     print 'high=', high, 'low=', low, 'ans=', ans
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0

# print 'numGuesses =', numGuesses
# print ans, 'is close to square root of', x


# Fixing for our error with nums less than 1:
# Our condition for the while loop was failing
# because the answer was outside of our search area.
# We would reach a point where ans = 1.0/2.0 = 0.5
# which would then meet the condition ans <= high,
# keeping us within the loop, infinitely
x = 0.5
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(x, 1.0)  # fixes our initial error, our search range was 0 - .5, but the answer is outside search range
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon and ans <= high:
    print 'high=', high, 'low=', low, 'ans=', ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x


def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats. epsilon > 0.0
    returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon


print withinEpsilon(2, 3, 1)  # 2 - 3 = -1 = 1 = 1 <= 1 = True
val = withinEpsilon(2, 3, 0.5)  # 2 - 3 = -1 = 1 = 1 <= 0.5 = False
print val


def f(x):
    x = x + 1
    print 'x in fn scope =', x
    return x


x = 3
z = f(x)
print 'z =', z
print 'x in global scope =', x


def f1(x):
    def g():
        x = 'abc'
    x = x + 1
    print 'x =', x
    g()
    # assert False
    return x


x = 3
z = f1(x)


def isEven(i):
    """assumes i a positive int
    returns True if i is even, otherwise False"""
    return i % 2 == 0


def findRoot(pwr, val, epsilon):
    """assumes pwr an int; val, epsilon floats
    pwr and epsilon > 0
    if it exists,
        returns a value within epsilon of val**pwr
        otherwise returns None"""
    assert type(pwr) == int and type(val) == float and type(epsilon) == float
    assert pwr > 0 and epsilon > 0

    if isEven(pwr) and val < 0:
        return None

    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low)/2.0

    while not withinEpsilon(ans**pwr, val, epsilon):
        # print 'ans =', ans, 'low =', low, 'high =', high
        if ans**pwr < val:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0

    return ans


def testFindRoot():
    """x float, epsilon float, pwr positive int"""
    for x in (-1.0, 1.0, 3456.0):
        for pwr in (1, 2, 3):
            ans = findRoot(pwr, x, 0.001)
            if ans is None:
                print 'The answer is imaginary'
            else:
                print ans, 'to the power of', pwr, 'is close to', x


sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print 'sumDigits =', sumDigits

x = 100
divisors = ()
for i in range(1, x):
    if x % i == 0:
        divisors = divisors + (i,)

print divisors[0]
print divisors[1]
print divisors[2]
print divisors[2:4]
