# MIT 6.00SC - Lecture 3 Notes
# ==========================

* Discussion of looping constructs:
  * Be thinking about a decrement function!
    * A decrementing function will:
      - Map set of program variables to an integer
      - When the loop is entered for the first time, its value is non-negative
      - When value <= 0, the loop terminates
      - It's decreased each iteration
    * In other words, a decrementing function moves us closer to termination
  * Going back to recitation form Lec 2:
    ```python
        x = int(raw_input('Enter an integer: '))
        ans = 0

        while ans * ans * ans < abs(x):
            ans = ans + 1
            print 'current guess =', ans

        if ans * ans * ans != abs(x):
            print x, 'is not a perfect cube'
        else:
            if x < 0:
                ans = -ans
            print 'Cube root of ' + str(x) + ' is ' + str(ans)
    ```
  * Above example is algorithm known as 'Exhaustive Enumeration' aka BRUTE FORCE
  * Brute force is actually often the correct algorithm, given the computing power of modern computers
  * We can abstract the while loop above into a for loop:
    ```python
    x = int(raw_input('Enter an integer: '))
    for ans in range(0, abs(x) + 1):
        if ans**3 == abs(x):
            break
    if ans**3 != abs(x):
        print x, 'is not a perfect cube'
    else:
        if x < 0:
            ans = -ans
        print 'Cube root of ' + str(x) + ' is ' + str(ans)
    ```

  * Approximation as a problem solving technique:
    - Find a 'y' such that 'y' * 'y' = x +/- Epsilon
    - Ex. of technique
    ```python
    x = 25
    epsilon = 0.01
    numGuesses = 0
    ans = 0.0

    # 5**2 - 25 = 25 - 25 = abs(0) = 0 >= 0.01 = false
    # 4**2 - 25 = 16 - 25 = abs(-9) = 9 >= 0.01 = true

    while abs(ans**2 - x) >= epsilon and ans <= x:
        ans += 0.00001
        numGuesses += 1
    if abs(ans**2 - x) >= epsilon:
        print 'Failed on square root of', x
    else:
        print ans, 'is close to square root of', x
    ```

  * The problem with our above code is the performance is subpar,
    and our brute force algorithm chokes under heavy load...we can
    instead use a `bisection` algorithm (i.e., `binary search`)

  * Binary seach relies on halving the search space each iteration
    (effectively log2):
    (make initial guess at halfway)
    <--   .   -->
            (too big)
    <--   xxxxxx>

    (too small)
    <xxx  xxxxxx>

    (make guess at halfway)
    <xxx . xxxxxx>

  * Ex. of our square root program with binary search:
    ```python
    x = 25.0
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon and ans <= x:
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print 'numGuesses =', numGuesses
    print ans, 'is close to square root of', x
    ```
  * Let's abstract the above into a more useful and generic program:
    ```python
    def withinEpsilon(x, y, epsilon):
        "x, y, epsilon all ints or floats
        returns true if x is within epsilon of y"
        return abs(x - y) <= epsilon
    if withinEpsilon(25, 26, 1):
        print 'yes'
    else:
        print 'no'
    if withinEpsilon(25, 26, 0.9):
        print 'yes'
    else:
        print 'no'
    ```

# Check Yourself
# ==========================

1) What does it mean for a program to terminate?
"A program will terminate when a value is returned or an error thrown. If our program does not terminate,
we likely have an infinite loop in our logic."

2) What is a for loop?
"A for loop provides a means of iterating over an enumerable object, providing us with a variable
for each iteration representing the current item that we can then modify/process."

# Problem Set
# ==========================

* None assigned (still work on Problem Set 1 from Lecture 2)
