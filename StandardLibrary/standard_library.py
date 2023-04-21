# standard_library.py
"""Python Essentials: The Standard Library.
<Griffin Brandstetter>
<MTH 420>
<4/21/2023>
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return(min(L), max(L), sum(L)/len(L))

print(prob1([1,2,4,6,7]))

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    int1 = 1
    int2 = int1
    int2 = 2
    if int1 == int2:
           print('integers are mutable')
    else:
           print('integers are immutable')
            
    string1 = 'abc'
    string2 = string1
    string2 = 'def'
    if string1 == string2:
           print('strings are mutable')
    else:
           print('strings are immutable')
            
    list1 = [1,2,3]
    list2 = list1
    list2 = [4,5,6]
    if list1 == list2:
           print('lists are mutable')
    else:
           print('lists are immutable')
            
    tuple1 = (1,2,3)
    tuple2 = tuple1
    tuple2 = (4,5,6)
    if tuple1 == tuple2:
           print('tuples are mutable')
    else:
           print('tuples are immutable')
            
    set1 = {1,2,3}
    set2 = set1
    set2 = {4,5,6}
    if set1 == set2:
           print('sets are mutable')
    else:
           print('sets are immutable')
           
    return
prob2()

# Problem 3
import calculator
from math import sqrt 

def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    h = sqrt(calculator.sum(calculator.product(a,a), calculator.product(b,b)))
    return(h)

print(hypot(3,4))


# Problem 4
import itertools

def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    P = []
    for i in range(len(A)+1):
        P.extend(list(itertools.combinations(A,i)))
        
    return(P)

print(power_set({1,2,3,5,8,4}))


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
