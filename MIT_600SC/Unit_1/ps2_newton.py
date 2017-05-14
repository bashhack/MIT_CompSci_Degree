# Problem Set 2 - A/B/C - Successive Approximation
# =============================================================================

# Problem Set 2a
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 20 minutes


def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    eval_of_poly = 0.0
    for idx, val in enumerate(poly):
        eval_of_poly += (val * (x ** idx))
    return eval_of_poly


# Problem Set 2b
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 40 minutes


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # -13.39 + 17.5x^2 + 3x^3 + x^4
    >>> print compute_deriv(poly)               # 35^x + 9x^2 + 4x^3
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """

    # Using Khan Academy to refresh my knowledge:
    # Let's start with: 4x^2 + 6x
    # First, we would bring the exponent down and
    #   multiply it by the coefficient: 8x^1 => 8x
    # Next, we would look at the second term, 6x (or 6x^1),
    #   which (following above rules) is the constant 6
    # The final derivative is then simple 8x + 6
    # Let's do another example:
    # x^2 + 8x + 13
    # => 2x + 8 (NOTE: we drop the constant, which 13x^0)
    # 3x^2 + x + 9
    # => 6x + 1
    # 4x^4 + 3x^3 + x + 19
    # 16x^3 + 9x^2 + 1

    poly_deriv_result = ()
    if len(poly) < 2:
        return (0.0,)
    for idx in xrange(1, len(poly)):
        # We will start at idx 1, as we know
        # x^0 (i.e., any constant) will be dropped
        poly_deriv_result = poly_deriv_result + (poly[idx] * idx,)
    return poly_deriv_result


# Problem Set 2c
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 45 minutes


# Utility Function for `compute_root`
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats. epsilon > 0.0
    returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon


def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    root = x_0
    iter_count = 0
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_deriv(poly), root))
        iter_count += 1
    return (root, iter_count)


# Test Cases
# ==========


# A:
# f(x) = 7x^4 + 9.3x^3 + 5x^2
print evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), -13)  # 180339.9

# B:
# -13.39 + 17.5x^2 + 3x^3 + x^4
print compute_deriv((-13.39, 0.0, 17.5, 3.0, 1.0))  # (0.0, 35.0, 9.0, 4.0)
# x^2 + 8x + 13
print compute_deriv((13, 8.0, 1.0)) # 2x + 8
# 3x^2 + x + 9
print compute_deriv((9, 1.0, 3.0))  # 6x + 1

# C:
# x^4 + 3x^3 + 17.5x^2 - 13.39
print compute_root((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, .0001) # (0.806790753796352, 7)
