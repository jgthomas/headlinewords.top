

""" 
Some utilities for functional programming.  

Functions allow the currying of operators and other
functions including generator expressions for use in 
pipelines of data processing.

The curried operators and functions take the role of
functions mapped onto the data, or as the criteria
for filtering, or both.

The curried generator expressions take the role of
the map() and filter() functions.

"""


import itertools
import functools


def is_not_in(y):
    """
    Return function that tests if x is not in the specified y.

    Example:
    >>> nums = [1, 2, 3, 4]
    >>> test = is_not_in(nums)
    >>> test(5)
    True

    """
    def is_not(x):
        return x not in y
    return is_not


def is_in(y):
    """
    Return function that tests if x is in the specified y.

    Example:
    >>> nums = [1, 2, 3, 4]
    >>> test = is_in(nums)
    >>> test(2)
    True

    """
    def is_in(x):
        return x in y
    return is_in


def to_power(power):
    """
    Return a function that raises a number to the specified power.

    Example: raise to power 3
    >>> pow_three = to_power(3)
    >>> pow_three(2)
    8
    >>> pow3(5)
    125

    """
    def nth_power(number):
        return number ** power
    return nth_power


def use_operator(o, x):
    """
    Return a curried version of the specified operator, that
    applies x to every supplied y

    Examples: add 3; subtract 7
    >>> from operator import add, sub
    >>> add3 = use_operator(add, 3)
    >>> add3(10)
    10
    >>> sub7 = use_operator(sub, 7)
    >>> sub7(10)
    3

    """
    def oper(y):
        return o(y, x)
    return oper


def map_over(func):
    """
    Return generator that applies a function to all elements.
    Works like map()

    Example: generator to add 3 to every element
    >>> from operator import add
    >>> nums = [1, 2, 3, 4]
    >>> add3 = use_operator(add, 3)
    >>> add_three = map_over(add3)
    >>> nums_plus_three = (add_three(nums))
    >>> list(nums_plus_three)
    [4, 5, 6, 7]

    """
    def generator(data):
        return (func(x) for x in data)
    return generator


def filter_by(func):
    """
    Return generator that filters all elements by func.
    Works like filter()

    Example: return only odd numbers
    >>> is_odd = lambda x: x % 2 != 0
    >>> nums = [1, 2, 3, 4, 5]
    >>> odd = filter_by(is_odd)
    >>> odd_nums = (odd(nums))
    >>> list(odd_nums)
    [1, 3, 5]

    """
    def generator(data):
        return (x for x in data if func(x))
    return generator


def map_over_filter_by(map_func, filter_func):
    """
    Return generator that maps a function only to those
    elements filtered by some criteria, leaving the other
    elements intact.

    Example: add 100 to all the odd numbers
    >>> from operator import add
    >>> is_odd = lambda x: x % 2 != 0
    >>> add100 = use_operator(add, 100)

    >>> nums = [1, 2, 3, 4, 5]
    
    >>> add_100_to_odd = map_over_filter_by(add100, is_odd)
    >>> odd_plus_100 = (add_100_to_odd(nums))
    >>> list(odd_plus_100)
    [101, 2, 103, 4, 105]

    """
    def generator(data):
        return (map_func(x) if filter_func(x) else x for x in data)
    return generator


def take(n, iterator):
    """ Return the first n elements. """
    return itertools.islice(iterator, n)


def drop(n, it):
    """ Return all but the first n elements """
    return itertools.islice(it, n, None)


def tail(it):
    """ Return all but the first element. """
    t = functools.partial(drop, 1)
    return t(it)


def iterate(f, x):
    """
    Applies f to x, then f(f(x)), then f(f(f(x))), etc.

    Example: apply double three times to an x of 2
    >>> double = lambda x: x + x
    >>> take(4, iterate(double, 2))
    [2, 4, 8, 16]

    """
    return itertools.accumulate(itertools.repeat(x), lambda fx, _: f(fx))


def compose(f, g):
    """
    Return a function that applies two functions.

    Functions are applied from right to left, i.e. in
    reverse order to which they are input.

    Example: raise a number to **2 and add 100
    >>> num = 3
    >>> add100 = use_operator(add, 100)
    >>> pow2 = to_power(2)
    >>> new_num = compose(add_100, pow2)
    >>> new_num(3)
    109

    """
    def composed(x):
        return f(g(x))
    return composed


def compose_many(*funcs):
    """
    Returns a function that applies multiple functions.

    Extends compose to cases with more than two functions.

    Example: raise to **2, add 100, subtract 20
    >>> num = 3
    >>> sub20 = use_operator(sub, 20)
    >>> add100 = use_operator(add, 100)
    >>> pow2 = to_power(2)
    >>> new_num = compose_many(sub20, add_100, pow2)
    >>> new_num(3)
    89

    """
    return functools.reduce(compose, funcs)
