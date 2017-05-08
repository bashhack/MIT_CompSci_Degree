# MIT 6.00SC - Lecture 6 Notes
# ==========================

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
