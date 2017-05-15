def isPal(x):
    """requires x is a list
       returns True if the list is a palindrome; False otherwise"""
    assert type(x) == list
    # temp = x  # original with bug
    temp = x[:]
    temp.reverse()
    print 'x=', x  # testing for debug
    print 'temp=', temp  # testing for debug
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """requires: n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the inputs are a palindrome; 'No' otherwise"""
    assert type(n) == int and n > 0

    result = []  # fix, after debug
    for i in range(n):
        # result = []  # original with bug
        elem = raw_input('Enter something: ')
        result.append(elem)
        print 'result=', result
    if isPal(result):
        print 'Is a palindrome'
    else:
        print 'Is not a palindrome'


# Adding a test case to automate process, a 'test harness'
def isPalTest():
    L = [1, 2]
    result = isPal(L)
    print 'Should print False', result
    L = [1, 2, 1]
    result = isPal(L)
    print 'Should print True', result

isPalTest()
