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

* As an example, let's imagine some function T that maps natural numbers to
  natural numbers, T: N -> N <- the number of steps for an input of that size
                      |_ size of input

* A "step" in this context (computational complexity) takes constant time

* Random Access Machine (RAM) - instructions are exectuted one after the other,
  that is they are sequential, and we assume constant time to access any object
  in memory. In early days of computers, memory was a physical tape, and there
  was drift/variance from reading something at start of tape vs end. Modern
  memory also has drift whether accessing data in L1, L2, L3 cache

* When we think about how long an algorithm will take to run, there are
  a few ways to look at it: (1) Best Case, (2) Worst Case, (3) Expected Case

* As an example, linear seach has a best case where the element being
  searched for is at index 0. The worst case might be having to traverse all
  elements in the data structure only to discover it's not there. The expected case
  is rarely used, and it's too hard to accurately model expected value.

* Given the above info, we almost always rely on using the Worst Case in evaluating
  our computational complexity. A benefit of using the worst case is that we have
  an known upper bound and that is happens often.

* Let's examine the following factorial function:
```python
def f(n):
  assert n >= 0
  answer = 1
  while n > 1:
    answer *= n
    n -= 1
  return answer
```



# Check Yourself
# ==================
