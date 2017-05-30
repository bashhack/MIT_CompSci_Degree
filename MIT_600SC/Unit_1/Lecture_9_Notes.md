# MIT 6.00SC - Lecture 8 Notes
# ============================

* Discussion begins with O(1) - constant time - example:
  Let's imagine an int takes '4 units' of memory - how would
  we get to the 'i'th location of a List of ints: L[i]
  We know that we can access the start so getting to
  the 'i'th would be start + 4 * i

* This would be a very conventional way to construct a list,
  but it relies on each element being the same size (in our example,
  4 units) - this trick of ours only works on a list where
  its elements are of a fixed size. In Python, our lists are not
  homogenous - they can contain ints, strings, chars, other lists,
  etc.

* The oldest notion of a list is the linked list, where each
  element of the list is a pointer to the next elem, value

 1 -> 2 -> 3 -> 4 -> 5

 Visualizing them as a JSON-like structure looks like this:

 {
   value: 1,
   next: {
     value: 2,
     next: {
       value: 3,
       next: {...}
     }
   }
 }

* Accessing the 'i'th element of the linked list is O(i) - not very good!
  Certainly worse that our binary search of O(log n)

* Instead of the linked list, Python uses 'indirection' (in the technical
  definition) to implement lists as an evenly divided list of pointers to
  a disparate collection of objects. Now, we're back to the first example,
  where we can in constant time access any element in a list even though the
  objects in the list are of varying size.

* 'All problems in computer science can be solved by another level of indirection,
   except the one problem of having too many levels of indirection'

* There's an assumption present in our discussion of efficiency so far! In our
  binary search examples, our algorithm is based on the assumption that the L(ist)
  is sorted.

* 'Amoratized complexity' - i.e., the cost of the sorting (or other algorithm)
  can be 'allocated' over each of the times we search the L - if we search a L
  one million times, the overhead of the sort is negligable

* We can reduce this insight to:
  If we plan on k searches, is O(sort(L)) + k * log(len(L)) < k * len(L)

* The rest of the lecture will be about sorting and optimizing our sorting:

---

* Lesson No. 1 - Bubble Sort is likely not the way to go! lol - Prof. Guttag
  shows President Obama speaking at Google

* We'll begin by looking at 'Selection Sort' - where the basic idea is establishing
  and maintaining an invariant (i.e., a pointer into the list) - this invariant will divide
  L into a prefix & suffix - and the invariant we will maintain is that the prefix is
  always sorted (inv = prefix is sorted)

```python
def selection_sort(L):
  """Assumes that L is a list of elements that can be compared using  >
     Sorts L in ascending order"""
  for i in range(len(L) - 1):
    # Invariant: the list L[:i] is sorted
    minIndx = i
    minVal = L[i]
    j = i + 1
    while j < len(L):
      if minVal > L[j]:
        minIndx = j
        minVal = L[j]
      j += 1
    temp = L[i]
    L[i] = L[minIndx]
    L[minIndx] = temp
```
  Selection sort is O(n**2)

* John von Neumann in the 40's used a divide and conquer method (which we've used before),
  to discover the following sorting algorithm (Merge Sort):

  First, we need to declare/define a threshold input size, the smallest problem
  Next, how many instances at each division
  Next, combine sub-solutions

```python
def merge_sort(left, right, lt):
  """Assumes left and right are sorted lists.
     lt defines an ordering on the elements of the lists.
     Returns a new sorted (by lt) list containing the same elements
     as (left + right) would contain."""
     result = []
     i, j = 0, 0
     while i < len(left) and j < len(right):
       if lt(left[i], right[j]):
         result.append(left[i])
         i += 1
       else:
         result.append(right[j])
         j += 1
     while (i < len(left)):
       result.append(left[i])
       i += 1
     while (j < len(right)):
       result.apend(right(j))
       j += 1
     return result

def sort(L, lt = lambda x,y: x < y):
  """Returns a new sorted list containing the same elements as L"""
  if len(L) < 2:
    return L[:]
  else:
    middle = int(len(L)/2)
    left = sort(L[:middle], lt)
    right = sort(L[middle:], lt)
    print left, right
    return merge(left, right, lt)

L = [35, 4, 5, 29, 17, 58, 0]
newL = sort(L)
print 'Sorted list =', newL
L = [1.0, 2.25, 24.5, 12.0, 2.0, 23.0, 19.125, 1.0]
newL = sort(L, float.__lt__)
print 'Sorted list =', newL
```
  Merge sort ends up being linear time O(n)

* Review of binary search algorithm:
```python
def binary_search(L, e, low, high):
  if high - low < 2:
    return L[low] == e or L[high] == e
  mid = low + int((low + high) / 2)
  if L[mid] == e:
    return True
  if L[mid] > e:
    return binary_search(L, e, low, mid - 1)
  else:
    return binary_search(L, e, mid + 1, high)
```

# Check Yourself
# ==================

1) What is indirection (in computing)?
"Indirection is a means of applying abstraction to a particular problem. A great example is the way
in which Python handles lists internally. In some languages a list consists of homogenous objects (i.e.,
ints/floats/some other data structure or native object), so we can then deduce that each element in the
list occupies equal space in memory. In Python, lists are not homogenous - so how can we be assured that
we can access some 'i'th element in constant time. The magic here is indirection, in this case through
the use of pointers. Each disparate object in a list (that may be of different sizes in memory) is
represented in the list via a pointer (itself of equal size)."

2) We know that a linear search works on all lists and is O(len(L)). Can we sort a list in sub-linear time?
"This is 'provably false', sorting of a list often takes (as in the case of merge sort, for example) O(n log n)."

3) Can we even do it in linear time?
"Likely, no - we may see O(n) in best case time complexity with selection or bubble sort but generally, O(n log n)
is more likely to appear across all best/average/worst case time complexity calculations."
