# MIT 6.00SC - Lecture 7 Notes
# ============================

* Quick discussion of floating point numbers in programming:
  * In base 10, we learn that a decimal is represented by some
    combination of 0-9, where the rightmost place is 10^0, then 10^1, then 10^2
  * In base 2 (i.e., binary) numbers: 0 1
  * The rightmost place is `2**0`, next over is `2**1`, `2**2`, etc.
  * 101 = `1 * 2**2 + 0 * 2**1 + 1 * 1**0`
  * Given n digits, how many different binary numbers can you represent? `2**n`
  * Computers work well in binary as switches (on/off) are easy to implement
    in the machine
  * Let's look at `0.125` in base 10 => `1 * 10**-1 + 2 * 10**-2 + 5 * 10**-3`
  * How about `0.1` in base 2...it's infinite!
    - There is only a binary approximation to decimal `0.1`, which is rounded to 17 digits
  * Because of the nature of approximation in floating point values, never directly
    compare them!
    - Instead, try:
    ```python
    x = 0.0
    numIters = 100000

    for i in range(numIters):
        x += 0.1
    print x  #prints 10000.0 because print automatically rounds
    print repr(x)
    print 10.0*x == numIters

    def withinEpsilon(x, y, epsilon=0.00001):
        return abs(x - y) < epsilon

    if withinEpsilon(10.0*x, numIters):
        print 'Good enough!'
    ```

  * The goal of debugging is not to eliminate one bug quickly, but rather to move
    toward a bug-free program. These goals on their own do not necessarily share
    the same tools/techniques.
  * While there are dedicated debuggers, it is often `print` which comes to the rescue
  * The key to being a good debugger is being systematic in our search for the bug:
    - Search for bugs using some approximation to binary search
    - "How could it have produced the output it did?"
    - Study available data =>
      Program text / Test Results =>
      Form hypothesis consistent with the data =>
      Design and run a repeatable experiment =>
      For experiment to be useful, must have potential to refute the hypothesis
  * Tips:
    - Find smaller input which will produce bug
    - Find the 'midway' point to ask whether the bug is 'above this' or 'below this',
      using our binary search method
  * For example, see `Lecture_7_Examples.py`

# Check Yourself
# ==================

1) Why do computers use binary representations?
"For the computer, a binary representation works well to represent the basic mechanism
of the `switch` - a simple on/off - that is fundamental to its architecture."

2) Why shouldn't we test for equality with floats?
"Because floats are approximations (see 17-digit rounding), comparing them is going to
be unreliable, at best."

3) When debugging, how can you ensure that the values in your program are the ones you think they are?
"Though we can use PDB and/or tesitng harnesses, the simple `print` should be and often is
an invaluable tool in quickly identifying/verifying the correctness of our program and its
values."


# Problem Set 4
# ==================
# TO DO...
