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

* (TODO: INSERT NOTES TAKEN FROM EARLIER ON W540 Workstation...)

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

* Types of Big O (from best to worst):
  - O(1) - constant
  - O(log n) - logarithmic
  - O(n) - linear
  - O(n log n) - log linear (NOTE: Try not to have anything worse than this!)
  - O(n^c) - polynomial
  - O(c^n) - exponential

* Our aim, ideally, is to define a tight bound (having provided both
  an upper bound and lower bound).

* Here's another example:

```python
def fact(n):
  assert n >= 0
  if n <= 1:
    return n
  else:
    return n * fact(n - 1)
```

* Notice that the efficiency is actually the same between the recursive
  and iterative versions of the factorial functions

* Let's look at another example:

```python
def g(n):
  x = 0
  for i in range(n):
    for j in range(n):
      x += 1
  return x
```
  Here, our complexity (starting from the inner loop!) is O(n**2)

* Next example:

```python
def h(x):
  assert type(x) == int and x >= 0
  answer = 0
  s = str(x)
  for c in s:
    answer += int(c)
  return answer
```
  Here, we would say that this is O(n) where n is log10(x)

* Next example:

```python
def search(L, e):
  for elem in L:
    if elem === e:
      return True
    if elem > e:
      return False
  return False
```
  Here, our complexity is O(len(L)) - or O(n) where n is len(L)

```python
def bSearch(L, e, low, high):
  global numCalls
  numCalls += 1
  if high - low < 2:
    return L[low] == e or L[high] == e
  mid = low + int((high - low)/2)
  if L[mid] == e:
    return True
  if L[mid] > e:
    return bSearch(L, e, low, mid - 1)
  else:
    return bSearch(L, e, mid + 1, high)
```
  Here, we see our complexity as O(log2(len(L))) - or O(log n)

* Our interface using these search functions might look like:
```python
def search(L, e):
  return bSearch(L, e, 0, len(L) - 1)
```


# Check Yourself
# ==================

1) Why is efficiency important?
"Understanding efficiency is fundamental to our approach in problem solving matters
both large and small. Choosing the right algorithm is more important than choosing some
'tricky' solution, and whether we choose the right algorithm can make orders of magnitude
difference in how long a calculation will take to resolve (if at all). We can protect ourselves
by aiming to stay with solutions to problems that reside below O(n log n) or log linear time,
avoiding both the worst case runtimes of polynomial and exponential runtimes."

2) What notation do we use to state computational complexity?
"We use the the Greek letter Omicron, and colloquially say 'Big O', to speak about computational
complexity. Donald Knuth popularized this, but others before him were certainly the originators.
While Big O describes our upper bound, we may want to describe a tight bound (factoring
in both upper/lower bounds) in which case we can use Big Theta, and, finally, in the event that we
want to speak of the minimum runtime we may use Big Omega."
