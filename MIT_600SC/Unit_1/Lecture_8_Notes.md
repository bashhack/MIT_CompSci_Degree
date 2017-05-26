# MIT 6.00SC - Lecture 8 Notes
# ============================

* The goal in our study of computation efficiency is not to become experts -
  as this is a much greater task than we can cover in a semester. Instead,
  we will aim to develop an 'intuition' for how to approach the question
  of efficiency.

* Why is efficiency so important? Though computers are fast, and powerful, in
  their computational abilities, some problems are enormous.

* Given the scale of problems we face in computer science, these concerns
  can mean the difference between days and years.

* Efficiency is about choosing the right algorithm(s), not about coding details.

* A successful computer scientist might invent only a single meaningful
  algorithm in their career - most never having discovered any.

* The key is: Reduce it to a previously solved problem!

* Efficiency is measured in both SPACE and TIME - we can often trade
  one for the other.

* We begin thinking of computational efficiency with a general recommendation
  to count the steps a computation will take for an input of that size.

* When we think about how long an algorithm will take to run, there are
  a few ways to look at it: (1) Best Case, (2) Worst Case, and (3) Expected Case

* (TODO: INSERT NOTES TAKEN FROM EARLIER...)

* Let's dive into a specific example to analyze:

```python
def f(n):
  assert n >= 0    # 1 step = 1 step for assert
  answer = 1       # 1 step = 2 steps
  while n > 1:     # 1 step
    answer *= n    # 1 step
    n -= 1         # 1 step = 3 steps for loop * n
  return answer    # 1 step = 1 step for return
```
  We would say then that 2 + 3n + 1 is the basic representation. We tend to
  drop both additive and multiplicative constants from our notation, leaving a
  representation that models the growth with respect to size of input as
  simply `n`. Because we are modeling asymptotic growth, we use the Greek
  letter omicron or Big O to notate this as: O(n)

* The Big O notation gives us an upper bound of the asymptotic growth of
  the function: formally, writing `f(x) E O(x**2)`, the function `f` "grows
  no faster" than the quadratic polynomial `x**2`

* Types of Big O:
  - O(1) - constant
  - O(log n) - logarithmic
  - O(n) - linear
  - O(n log n) - log linear
  - O(n^c) - polynomial
  - O(c^n) - exponential

* Our aim, ideally, is to define a tight bound (having provided both
  an upper bound and lower bound).

# Check Yourself
# ==================
